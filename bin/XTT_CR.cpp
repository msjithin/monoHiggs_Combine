#include <string>
#include <map>
#include <set>
#include <iostream>
#include <utility>
#include <vector>
#include <cstdlib>
#include "boost/algorithm/string/predicate.hpp"
#include "boost/program_options.hpp"
#include "boost/lexical_cast.hpp"
#include "boost/regex.hpp"
#include "CombineHarvester/CombineTools/interface/CombineHarvester.h"
#include "CombineHarvester/CombineTools/interface/Algorithm.h"
#include "CombineHarvester/CombineTools/interface/CardWriter.h"
#include "CombineHarvester/CombineTools/interface/Observation.h"
#include "CombineHarvester/CombineTools/interface/Process.h"
#include "CombineHarvester/CombineTools/interface/Utilities.h"
#include "CombineHarvester/CombineTools/interface/Systematics.h"
#include "CombineHarvester/CombineTools/interface/BinByBin.h"
#include "CombineHarvester/CombineTools/interface/AutoRebin.h"
#include "TH2.h"
#include "TH1.h"
#include "TF1.h"

using namespace std;
using boost::starts_with;
namespace po = boost::program_options;

template <typename T>

void To1Bin(T* proc)
{
  std::cout<<"Making CR into 1 bin"<<std::endl;
  std::unique_ptr<TH1> originalHist = proc->ClonedScaledShape();
  TH1F *hist = new TH1F("hist","hist",1,0,1);
  double err = 0;
  double rate = originalHist->IntegralAndError(0, originalHist->GetNbinsX() + 1, err);
  hist->SetDirectory(0);
  hist->SetBinContent(1, rate);
  hist->SetBinError(1, err);
  proc->set_shape(*hist, true);  // True means adjust the process rate to the
  // integral of the hist
  std::cout<<"CR is now one bin!"<<std::endl;
  std::cout<<"...."<<std::endl;
}

template <typename T>
void MergeBins(T* proc)
{
  std::cout<<"Merging CR bins into 1 bin"<<std::endl;
  std::unique_ptr<TH1> originalHist = proc->ClonedScaledShape();
  TH1F *hist = new TH1F("hist","hist",3,0,13);
  double err = 0;
  double rate = 0;
  hist->SetDirectory(0);

  rate = originalHist->IntegralAndError(1, 6 , err);
  hist->SetBinContent(1, rate);
  hist->SetBinError(1, err);

  rate = originalHist->IntegralAndError(7, 12 , err);
  hist->SetBinContent(2, rate);
  hist->SetBinError(2, err);

  rate = originalHist->IntegralAndError(13, 14 , err);
  hist->SetBinContent(3, rate);
  hist->SetBinError(3, err);

  proc->set_shape(*hist, true);  // True means adjust the process rate to the
  // integral of the hist
  std::cout<<" CR Region reduced"<<std::endl;
  std::cout<<"...."<<std::endl;
}


bool BinIsControlRegion(ch::Object const* obj)
{
  return (boost::regex_search(obj->bin(),boost::regex{"_cr$"}) || (obj->channel() == std::string("mm")));
}

bool BinIsQCDControlRegion(ch::Object const* obj)
{
  return (boost::regex_search(obj->bin(),boost::regex{"_QCD_"}) && boost::regex_search(obj->bin(),boost::regex{"_cr$"}));
}

bool BinIsWControlRegion(ch::Object const* obj)
{
  return (boost::regex_search(obj->bin(),boost::regex{"_W_"}) && boost::regex_search(obj->bin(),boost::regex{"_cr$"}));
}

// Useful to have the inverse sometimes too
bool BinIsNotControlRegion(ch::Object const* obj)
{
  return !BinIsControlRegion(obj);
}

bool BinIsNotWControlRegion(ch::Object const* obj)
{
  return !BinIsWControlRegion(obj);
}




int main(int argc, char** argv) {
  //! [part1]
  // First define the location of the "auxiliaries" directory where we can
  // source the input files containing the datacard shapes
  string aux_shapes = string(getenv("CMSSW_BASE")) + "/src/CombineHarvester/CombineTools/bin/aux/";
  string input_dir =
    string(getenv("CMSSW_BASE")) + "/src/CombineHarvester/CombineTools/bin/aux/";
  
    typedef vector<string> VString;
    typedef vector<pair<int, string>> Categories;

    string mass="";
    string signalMass="";
    string model="";
    int control_region = 1;
    int dobbb = 1;
    string year = "2017";

    VString masses;
    VString sig_procs;


    po::variables_map vm;
    po::options_description config("configuration");
    config.add_options()
      ("mass,m", po::value<string>(&mass)->default_value("100"))
      ("signalMass", po::value<string>(&signalMass)->default_value("200"))
      ("control_region", po::value<int>(&control_region)->default_value(1))
      ("dobbb", po::value<int>(&dobbb)->default_value(1))
      ("model", po::value<string>(&model)->default_value("2HDMa"))
      ("year", po::value<string>(&year)->default_value("2017"));
    po::store(po::command_line_parser(argc, argv).options(config).run(), vm);
    po::notify(vm);


    // Create an empty CombineHarvester instance that will hold all of the
    // datacard configuration and histograms etc.
    ch::CombineHarvester cb;
    // Uncomment this next line to see a *lot* of debug information
    // cb.SetVerbosity(3);
    VString chns =
      {"mt","et","tt"};

  map<string, string> input_folders = {
    {"mt", "mutau"},
    {"et", "etau"},
    {"tt", "tautau"}
  };

    // Each entry in the vector below specifies a bin name and corresponding bin_id.

    //ch::Categories cats = {
    //    {1, "_inclusive"}
    //};
    // ch::Categories is just a typedef of vector<pair<int, string>>
    //! [part1]
    map<string, VString> bkg_procs;
    bkg_procs["mt"] = {"jetFakes", "ZTTjet", "ZLLjet", "TT" , "otherMC" , "STT", "VVT"};
    bkg_procs["et"] = {"jetFakes", "ZTTjet", "ZLLjet", "TT" , "otherMC" , "STT", "VVT"};
    bkg_procs["tt"] = {"jetFakes", "ZTTjet", "TT" , "otherMC" , "STT", "VVT"};

    map<string, Categories> cats;
    cats["et"] = {
      {1, "etau"}};
    cats["mt"] = {
      {1, "mutau"}};
    cats["tt"] = {
      {1, "tautau"}};



    masses = {""}; 
    if (model=="Zprime")
      sig_procs = {"Zprime"+signalMass+"A"};
    if (model=="Baryonic")
      sig_procs = {"ZpBaryonic_Zp"+signalMass+"_MChi"};
    if (model=="2HDMa")
      sig_procs = {"MH3_"+signalMass+"_MH4_"+mass};

    //sig_procs = {"MH3_200_MH4_100"};
    //! [part2]
    for (auto chn : chns) {
      cb.AddObservations(
			 {"*"}, {"xtt"}, {"13TeV"}, {chn}, cats[chn]);
      cb.AddProcesses(
		      {"*"}, {"xtt"}, {"13TeV"}, {chn}, bkg_procs[chn], cats[chn], false);
      cb.AddProcesses(
		      masses, {"xtt"}, {"13TeV"}, {chn}, sig_procs, cats[chn], true);
    }


    //Some of the code for this is in a nested namespace, so
    // we'll make some using declarations first to simplify things a bit.
    using ch::syst::SystMap;
    using ch::syst::era;
    using ch::syst::channel;
    using ch::syst::bin_id;
    using ch::syst::process;




    //! [part6]

    cb.cp().process(sig_procs)
      .AddSyst(cb, "CMS_renormalization", "lnN", SystMap<>::init(1.04));

    cb.cp().process(sig_procs)
      .AddSyst(cb, "CMS_PDF", "lnN", SystMap<>::init(1.02)); 

    cb.cp().process(ch::JoinStr({sig_procs,{"ZTTjet", "ZLLjet", "TT" , "otherMC" , "STT", "VVT"}}))
      .AddSyst(cb,"BR_htt_THU", "lnN", SystMap<>::init(1.017));
    
    
    /////////////////
    // Systematics //
    /////////////////
    
    // // Should set a sensible range for our rateParams
    // for (auto sys : cb.cp().syst_type({"rateParam"}).syst_name_set()) {
    //   cb.GetParameter(sys)->set_range(0.0, 5.0);
    // }
    // cb.SetFlag("filters-use-regex", false);
    


    for (string chn : chns) {
      string file = aux_shapes + year +"/" + input_folders[chn]+".root";
        //".inputs-13TeV-met.root";
        cb.cp().channel({chn}).backgrounds().ExtractShapes(
							   file, "$BIN/$PROCESS", "$BIN/$PROCESS_$SYSTEMATIC");
        cb.cp().channel({chn}).signals().ExtractShapes(
						       file, "$BIN/$PROCESS$MASS", "$BIN/$PROCESS_$SYSTEMATIC");
    }
    cout << ">> Scaling signal process rates...\n";
    map<string, TGraph> xs;
    if (dobbb){


      //! [part8]
      auto bbb = ch::BinByBinFactory()
	.SetAddThreshold(0.05) //0.1
	//.SetMergeThreshold(0.8) //0.5
	.SetFixNorm(false)
	.SetVerbosity(1);
      bbb.AddBinByBin(cb.cp().backgrounds().FilterProcs(BinIsControlRegion), cb);

      auto bbb_ctl = ch::BinByBinFactory()
	.SetPattern("CMS_$ANALYSIS_$BIN_$ERA_$PROCESS_bin_$#")
	.SetAddThreshold(0.10)
	//.SetMergeThreshold(0.5)
	.SetFixNorm(false)  // contrary to signal region, bbb *should* change yield here?
	//.SetFixNorm(true)  // contrary to signal region, bbb *should* change yield here?
	.SetVerbosity(1);
      // Will merge but only for non W and QCD processes, to be on the safe side
      bbb_ctl.AddBinByBin(cb.cp().backgrounds().FilterProcs(BinIsNotWControlRegion), cb);
      cout << " done\n";
    }
    // This function modifies every entry to have a standardised bin name of
    // the form: {analysis}_{channel}_{bin_id}_{era}
    // which is commonly used in the xtt analyses
    ch::SetStandardBinNames(cb);
    //! [part8]

    //! [part9]
    // First we generate a set of bin names:
    set<string> bins = cb.bin_set();
    // This method will produce a set of unique bin names by considering all
    // Observation, Process and Systematic entries in the CombineHarvester
    // instance.

    /*
    cb.SetGroup("BinByBin", {"CMS_xtt_.*_bin_.*"});
    cb.SetGroup("UES", {"CMS_scale_m.*"});
    cb.SetGroup("CES", {"CMS_scale_j.*"});
    cb.SetGroup("all", {".*"});
    string metSyst = "CMS_scale_m.*|CMS_scale_j.*";
    cb.SetGroup("MET", {metSyst}); 
    */
    // We create the output root file that will contain all the shapes.
    // Here we define a CardWriter with a template for how the text datacard
    // and the root files should be named.
    ch::CardWriter writer("$TAG/$MASS/$ANALYSIS_$CHANNEL_$BINID_$ERA.txt",
			  "$TAG/$MASS/$ANALYSIS_$CHANNEL.input_$ERA.root");
    writer.SetVerbosity(1);
    writer.WriteCards("output/xtt_cards/"+model+signalMass+"A"+mass+"/cmb", cb);
    for (auto chn : chns) {
      writer.WriteCards("output/xtt_cards/"+model+signalMass+"A"+mass+"/"+chn, cb.cp().channel({chn}));
    }

    if (control_region > 0){

      for (auto chn : chns) {

	if (ch::contains({"et", "mt"}, chn)) {

	  cb.cp().channel({chn}).bin_id({10}).mass({"$MASS", "*"}).WriteDatacard("output/xtt_cards/"+model+signalMass+"A"+mass+"/cmb/"+mass+ "/xtt_"+chn+"_10_13TeV.txt", "output/xtt_cards/"+model+signalMass+"A"+mass+"/cmb/"+mass+ "/xtt_input_"+chn+"_10.root");
	  cb.cp().channel({chn}).bin_id({11}).mass({"$MASS", "*"}).WriteDatacard("output/xtt_cards/"+model+signalMass+"A"+mass+"/cmb/"+mass+ "/xtt_"+chn+"_11_13TeV.txt", "output/xtt_cards/"+model+signalMass+"A"+mass+"/cmb/"+mass+"/xtt_input_"+chn+"_11.root");

	  cb.cp().channel({chn}).bin_id({10}).mass({"$MASS", "*"}).WriteDatacard("output/xtt_cards/"+model+signalMass+"A"+mass+"/"+chn+"/"+mass+ "/xtt_"+chn+"_10_13TeV.txt", "output/xtt_cards/"+model+signalMass+"A"+mass+"/"+chn+"/"+mass+ "/xtt_input_"+chn+"_10.root");
	  cb.cp().channel({chn}).bin_id({11}).mass({"$MASS", "*"}).WriteDatacard("output/xtt_cards/"+model+signalMass+"A"+mass+"/"+chn+"/"+mass+ "/xtt_"+chn+"_11_13TeV.txt", "output/xtt_cards/"+model+signalMass+"A"+mass+"/"+chn+"/"+mass+"/xtt_input_"+chn+"_11.root");



	} // end et mt
	if (ch::contains({"tt"}, chn)) {
	  cb.cp().channel({chn}).bin_id({11}).mass({"$MASS", "*"}).WriteDatacard("output/xtt_cards/"+model+signalMass+"A"+mass+"/cmb/"+mass+ "/xtt_"+chn+"_11_13TeV.txt", "output/xtt_cards/"+model+signalMass+"A"+mass+"/cmb/"+mass+ "/xtt_input_"+chn+"_11.root");
	  cb.cp().channel({chn}).bin_id({11}).mass({"$MASS", "*"}).WriteDatacard("output/xtt_cards/"+model+signalMass+"A"+mass+"/"+chn+"/"+mass+ "/xtt_"+chn+"_11_13TeV.txt", "output/xtt_cards/"+model+signalMass+"A"+mass+"/"+chn+"/"+mass+ "/xtt_input_"+chn+"_11.root");
	}
      } // end CR
    }
}
