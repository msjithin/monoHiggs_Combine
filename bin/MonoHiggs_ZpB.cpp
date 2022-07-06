#include <string>
#include <map>
#include <set>
#include <iostream>
#include <vector>
#include <utility>
#include <cstdlib>
#include "boost/algorithm/string/predicate.hpp"
#include "boost/program_options.hpp"
#include "boost/lexical_cast.hpp"
#include "boost/regex.hpp"
#include "boost/filesystem.hpp"
#include "CombineHarvester/CombineTools/interface/CombineHarvester.h"
#include "CombineHarvester/CombineTools/interface/Utilities.h"
#include "CombineHarvester/CombineTools/interface/HttSystematics.h"
#include "CombineHarvester/CombineTools/interface/CardWriter.h"
#include "CombineHarvester/CombineTools/interface/CopyTools.h"
#include "CombineHarvester/CombineTools/interface/BinByBin.h"
#include "CombineHarvester/CombineTools/interface/Systematics.h"

namespace po = boost::program_options;
using boost::starts_with;
using namespace std;

int main(int argc, char** argv) {

  string postfix="";
  string prefix="";
  string year = "2017";
  string inputFile="";
  string do_chn="et";
  string WP="WP";
  string Var="";
  string mediatorMass = "";
  string pscalarMass = "";
  po::variables_map vm;
  po::options_description config("configuration");
  config.add_options()
    //    ("mass,m", po::value<string>(&mass)->default_value(mass))
    //      ("input_folder_em", po::value<string>(&input_folder_em)->default_value("USCMS"))
    //      ("input_folder_et", po::value<string>(&input_folder_et)->default_value("USCMS"))
    //      ("input_folder_mt", po::value<string>(&input_folder_mt)->default_value("USCMS"))
    //      ("input_folder_tt", po::value<string>(&input_folder_tt)->default_value("USCMS"))
    //      ("input_folder_mm", po::value<string>(&input_folder_mm)->default_value("USCMS"))
    //      ("input_folder_ttbar", po::value<string>(&input_folder_ttbar)->default_value("USCMS"))
    ("prefix", po::value<string>(&prefix)->default_value(""))
    ("postfix", po::value<string>(&postfix)->default_value(""))
    ("Var", po::value<string>(&Var)->default_value(""))
    ("med", po::value<string>(&mediatorMass)->default_value("400"))
    ("ps", po::value<string>(&pscalarMass)->default_value("100"))
    //      ("vbfcateStr_tt", po::value<string>(&vbfcateStr_tt)->default_value("tt_vbf_ggHMELA_bin"))
    //      ("vbfcateStr_mt", po::value<string>(&vbfcateStr_mt)->default_value("mt_vbf_ggHMELA_bin"))
    //      ("auto_rebin", po::value<bool>(&auto_rebin)->default_value(false))
    //      ("real_data", po::value<bool>(&real_data)->default_value(false))
    //      ("manual_rebin", po::value<bool>(&manual_rebin)->default_value(false))
    //      ("output_folder", po::value<string>(&output_folder)->default_value("sm_run2"))
    //      ("SM125,h", po::value<string>(&SM125)->default_value(SM125))
    //      ("control_region", po::value<int>(&control_region)->default_value(0))
    ("year", po::value<string>(&year)->default_value("2017"))
    ("WP", po::value<string>(&WP)->default_value(""))
    ("inputFile", po::value<string>(&inputFile)->default_value(""))
    ("chn", po::value<string>(&do_chn)->default_value("et"));
  
  //      ("mm_fit", po::value<bool>(&mm_fit)->default_value(true))
  //      ("ttbar_fit", po::value<bool>(&ttbar_fit)->default_value(true))
  //      ("jetfakes", po::value<bool>(&do_jetfakes)->default_value(false))
  //      ("embedded", po::value<bool>(&do_embedded)->default_value(false))
  //      ("shapeSyst", po::value<bool>(&do_shapeSyst)->default_value(false))
  //      ("sync", po::value<bool>(&do_sync)->default_value(false))
  //      ("useSingleVBFdir", po::value<bool>(&useSingleVBFdir)->default_value(false))
  //      ("par", po::value<string>(&par)->default_value("fa3"))
  //      ("is2017", po::value<bool>(&is_2017)->default_value(false))
  //      ("use_ggHint", po::value<bool>(&use_ggHint)->default_value(false))
  //      ("check_neg_bins", po::value<bool>(&check_neg_bins)->default_value(false))
  //      ("poisson_bbb", po::value<bool>(&poisson_bbb)->default_value(false))
  //      ("w_weighting", po::value<bool>(&do_w_weighting)->default_value(false));
  po::store(po::command_line_parser(argc, argv).options(config).run(), vm);
  po::notify(vm);
  






  cout << ">> Making datacards for mediatorMass="<<mediatorMass <<"  and ps mass = "<<pscalarMass<<"\n";  
  //! [part1]
  // First define the location of the "auxiliaries" directory where we can
  // source the input files containing the datacard shapes
  //    string aux_shapes = string(getenv("CMSSW_BASE")) + "/src/auxiliaries/shapes/";
  string aux_shapes = string(getenv("CMSSW_BASE")) + "/src/CombineHarvester/CombineTools/bin/aux/";
    
  // Create an empty CombineHarvester instance that will hold all of the
  // datacard configuration and histograms etc.
  ch::CombineHarvester cb;
    
  typedef vector<pair<int, string>> Categories;
  typedef vector<string> VString;
  // Uncomment this next line to see a *lot* of debug information
  // cb.SetVerbosity(3);
    
  // Here we will just define two categories for an 8TeV analysis. Each entry in
  // the vector below specifies a bin name and corresponding bin_id.
    
  VString chns;
  if (do_chn=="et")
    chns = {"et"};
  else if (do_chn=="mt")
    chns = {"mt"};
  else if (do_chn=="tt")
    chns = {"tt"};
  else if (do_chn=="all")
    chns = {"et", "mt", "tt"}; // add channels { "mt","et", "tt"};
  
  map<string, string> input_folders = {
    {"mt", "mutau"},
    {"et", "etau"},
    {"tt", "tautau"}
  };
    
  map<string, VString> bkg_procs;
  bkg_procs["mt"] = {"jetFakes", "ZTTjet", "ZLLjet", "TT" , "otherMC" , "STT", "VVT"};
  bkg_procs["et"] = {"jetFakes", "ZTTjet", "ZLLjet", "TT" , "otherMC" , "STT", "VVT"};
  bkg_procs["tt"] = {"jetFakes", "ZTTjet", "TT" , "otherMC" , "STT", "VVT"};
    
  VString sig_procs = {"MZp_"+mediatorMass+"_MChi_"+pscalarMass};
  
  map<string, Categories> cats;
  //cats["et_13TeV"] = {
  //      {1, "EleTau_DiJet"}};
    

  cats["mt_13TeV"] = {
    {1, "mutau"},
    //        {2, "fail"}
  };
  cats["et_13TeV"] = {
    {1, "etau"},
    //        {2, "fail"}
  };
  cats["tt_13TeV"] = {
    {1, "tautau"},
    //        {2, "fail"}
  };
    
    
  // ch::Categories is just a typedef of vector<pair<int, string>>
  //! [part1]
    
    
  //! [part2]
  //    vector<string> masses = ch::MassesFromRange("800-1500:100");
  //    vector<string> masses = ch::MassesFromRange("14-15:1");
  //vector<string> masses = ch::MassesFromRange("14-15:1");
  vector<string> masses = {""};
  // Or equivalently, specify the mass points explicitly:
  //! [part2]
    
    
  //! [part4]
  for (auto chn : chns) {
    cb.AddObservations(
		       {"*"}, {"xtt"}, {"13TeV"}, {chn}, cats[chn+"_13TeV"]);
    cb.AddProcesses(
		    {"*"}, {"xtt"}, {"13TeV"}, {chn}, bkg_procs[chn], cats[chn+"_13TeV"], false);
    cb.AddProcesses(
		    masses, {"xtt"}, {"13TeV"}, {chn}, sig_procs, cats[chn+"_13TeV"], true);
  }
       
  cout << ">> Extracting histograms from input root files...\n";
  for (string era : {"13TeV"}) {
    for (string chn : chns) {
            
      string file = aux_shapes + year +"/" + input_folders[chn]+".root";
      cout <<">> file name :  "<< file <<endl;   
      cb.cp().channel({chn}).era({era}).backgrounds().ExtractShapes(
								    file, "$BIN/$PROCESS", "$BIN/$PROCESS_$SYSTEMATIC");
      cb.cp().channel({chn}).era({era}).signals().ExtractShapes(
								file, "$BIN/$PROCESS$MASS", "$BIN/$PROCESS$MASS_$SYSTEMATIC");
    }
  }
    
    
  //Some of the code for this is in a nested namespace, so
  // we'll make some using declarations first to simplify things a bit.
  using ch::syst::SystMap;
  using ch::syst::era;
  using ch::syst::bin_id;
  using ch::syst::process;
  using ch::JoinStr;
    
    
  // Norm systematics
  // cb.cp().process({"jetFakes"})
  //   .AddSyst(cb, "CMS_jetFakesNorm_0jetlow_"+year, "lnN", SystMap<>::init(1.05));
  cb.cp().channel({"et"}).process(ch::JoinStr({{"ZLLjet"}}))
    .AddSyst(cb, "CMS_eFakeTau_"+year, "lnN", SystMap<>::init(1.15));
  cb.cp().channel({"mt"}).process(ch::JoinStr({{"ZLLjet"}}))
    .AddSyst(cb, "CMS_muFakeTau_"+year, "lnN", SystMap<>::init(1.2));

  cb.cp().channel({"et"}).process(ch::JoinStr({sig_procs,{"ZTTjet", "ZLLjet", "TT" , "otherMC" , "STT", "VVT"}}))  
    .AddSyst(cb, "CMS_eff_t_againstemu_et_"+year, "lnN", SystMap<>::init(1.01));
  
  cb.cp().channel({"et"}).process(ch::JoinStr({sig_procs,{"ZTTjet", "ZLLjet", "TT" , "otherMC" , "STT", "VVT"}}))
    .AddSyst(cb, "CMS_eff_e_"+year, "lnN", SystMap<>::init(1.02));
  cb.cp().channel({"mt"}).process(ch::JoinStr({sig_procs,{"ZTTjet", "ZLLjet", "TT" , "otherMC" , "STT", "VVT"}}))
    .AddSyst(cb, "CMS_eff_mu_"+year, "lnN", SystMap<>::init(1.02));
  
  cb.cp().process(ch::JoinStr({sig_procs,{"ZTTjet", "ZLLjet", "otherMC" , "STT", "VVT"}}))
    .AddSyst(cb, "CMS_htt_eff_b_"+year, "lnN", SystMap<>::init(1.005));
  cb.cp().process({"TT"})
    .AddSyst(cb, "CMS_htt_eff_b_TT_"+year, "lnN", SystMap<>::init(1.05));
  
  cb.cp().process({"STT"})
    .AddSyst(cb, "CMS_htt_stXsec", "lnN", SystMap<>::init(1.05));
  
  cb.cp().process({"TT"})
    .AddSyst(cb, "CMS_htt_tjXsec", "lnN", SystMap<>::init(1.042));
  
  cb.cp().process({"VVT"})
    .AddSyst(cb, "CMS_htt_vvXsec", "lnN", SystMap<>::init(1.05));

  cb.cp().process({"ZTTjet", "ZLLjet"})
    .AddSyst(cb, "CMS_htt_zjXsec", "lnN", SystMap<>::init(1.02));

  cb.cp().process(ch::JoinStr({sig_procs,{"ZTTjet", "ZLLjet", "TT" , "otherMC" , "STT", "VVT"}}))
    .AddSyst(cb, "lumi_Run"+year, "lnN", SystMap<>::init(1.02));
  cb.cp().process(ch::JoinStr({sig_procs,{"ZTTjet", "ZLLjet", "TT" , "otherMC" , "STT", "VVT"}}))
    .AddSyst(cb, "lumi_XYfactorization", "lnN", SystMap<>::init(1.008));
  cb.cp().process(ch::JoinStr({sig_procs,{"ZTTjet", "ZLLjet", "TT" , "otherMC" , "STT", "VVT"}}))
    .AddSyst(cb, "lumi_beamBeamDeflection", "lnN", SystMap<>::init(1.004));
  cb.cp().process(ch::JoinStr({sig_procs,{"ZTTjet", "ZLLjet", "TT" , "otherMC" , "STT", "VVT"}}))
    .AddSyst(cb, "lumi_beamCurrentCalibration", "lnN", SystMap<>::init(1.003));
  cb.cp().process(ch::JoinStr({sig_procs,{"ZTTjet", "ZLLjet", "TT" , "otherMC" , "STT", "VVT"}}))
    .AddSyst(cb, "lumi_dynamicBeta", "lnN", SystMap<>::init(1.005));
  cb.cp().process(ch::JoinStr({sig_procs,{"ZTTjet", "ZLLjet", "TT" , "otherMC" , "STT", "VVT"}}))
    .AddSyst(cb, "lumi_ghostsAndSatellites", "lnN", SystMap<>::init(1.001));
  cb.cp().process(ch::JoinStr({sig_procs,{"ZTTjet", "ZLLjet", "TT" , "otherMC" , "STT", "VVT"}}))
    .AddSyst(cb, "lumi_lengthScale", "lnN", SystMap<>::init(1.003));
  
  cb.cp().process(sig_procs)
    .AddSyst(cb, "CMS_renormalization", "lnN", SystMap<>::init(1.04));
  
  cb.cp().process(sig_procs)
    .AddSyst(cb, "CMS_PDF", "lnN", SystMap<>::init(1.02)); 
  
  // cb.cp().process(ch::JoinStr({sig_procs,{"otherMC" , "VVT"}}))
  //   .AddSyst(cb, "BR_htt_THU", "lnN", SystMap<>::init(1.017));
  
  // Shape systematics
  /////////////
  if(year=="2017"){
    cb.cp().process(ch::JoinStr({sig_procs, {"ZTTjet", "ZLLjet", "TT" , "otherMC" , "STT", "VVT"}}))
      .AddSyst(cb, "CMS_Prefiring", "shape", SystMap<>::init(1.00));
  }
  cb.cp().process(ch::JoinStr({sig_procs, {"ZTTjet"}}))
    .AddSyst(cb, "CMS_JER", "lnN", SystMap<>::init(1.0043));
  cb.cp().process(ch::JoinStr({sig_procs, {"ZTTjet"}}))
    .AddSyst(cb, "CMS_JES", "lnN", SystMap<>::init(1.0013));    

  // cb.cp().process(ch::JoinStr({sig_procs, {"ZTTjet"}}))
  //   .AddSyst(cb, "CMS_JER", "shape", SystMap<>::init(1.00));
  // cb.cp().process(ch::JoinStr({sig_procs, {"ZTTjet"}}))
  //   .AddSyst(cb, "CMS_JES", "shape", SystMap<>::init(1.00));    
  cb.cp().process( {"ZTTjet", "ZLLjet"})
    .AddSyst(cb, "CMS_htt_dyShape", "shape", SystMap<>::init(1.00));
  cb.cp().process({"TT"})
    .AddSyst(cb, "CMS_htt_ttbarShape", "shape", SystMap<>::init(1.00));
  //////
  cb.cp().channel({"et"}).process({"jetFakes"})
    .AddSyst(cb, "CMS_FF_closure_OSSS_mvis_et_qcd_"+year, "shape", SystMap<>::init(1.00));
  cb.cp().channel({"et"}).process({"jetFakes"})
    .AddSyst(cb, "CMS_FF_closure_lpt_et_qcd", "shape", SystMap<>::init(1.00));
  cb.cp().channel({"et"}).process({"jetFakes"})
    .AddSyst(cb, "CMS_FF_closure_lpt_et_tt", "shape", SystMap<>::init(1.00));
  cb.cp().channel({"et"}).process({"jetFakes"})
    .AddSyst(cb, "CMS_FF_closure_lpt_et_w", "shape", SystMap<>::init(1.00));
  cb.cp().channel({"et"}).process({"jetFakes"})
    .AddSyst(cb, "CMS_FF_closure_lpt_xtrg_et_qcd_"+year, "shape", SystMap<>::init(1.00));
  cb.cp().channel({"et"}).process({"jetFakes"})
    .AddSyst(cb, "CMS_FF_closure_lpt_xtrg_et_tt_"+year, "shape", SystMap<>::init(1.00));
  cb.cp().channel({"et"}).process({"jetFakes"})
    .AddSyst(cb, "CMS_FF_closure_lpt_xtrg_et_w_"+year, "shape", SystMap<>::init(1.00));
  cb.cp().channel({"et"}).process({"jetFakes"})
    .AddSyst(cb, "CMS_FF_closure_mt_et_w_unc1_"+year, "shape", SystMap<>::init(1.00));
  cb.cp().channel({"et"}).process({"jetFakes"})
    .AddSyst(cb, "CMS_FF_closure_mt_et_w_unc2_"+year, "shape", SystMap<>::init(1.00));
  cb.cp().channel({"et"}).process({"jetFakes"})
    .AddSyst(cb, "CMS_rawFF_et_qcd_unc1_"+year, "shape", SystMap<>::init(1.00));          
  cb.cp().channel({"et"}).process({"jetFakes"})
    .AddSyst(cb, "CMS_rawFF_et_qcd_unc2_"+year, "shape", SystMap<>::init(1.00));          
  cb.cp().channel({"et"}).process({"jetFakes"})
    .AddSyst(cb, "CMS_rawFF_et_tt_unc1_"+year, "shape", SystMap<>::init(1.00));          
  cb.cp().channel({"et"}).process({"jetFakes"})
    .AddSyst(cb, "CMS_rawFF_et_tt_unc2_"+year, "shape", SystMap<>::init(1.00));          
  cb.cp().channel({"et"}).process({"jetFakes"})
    .AddSyst(cb, "CMS_rawFF_et_w_unc1_"+year, "shape", SystMap<>::init(1.00));          
  cb.cp().channel({"et"}).process({"jetFakes"})
    .AddSyst(cb, "CMS_rawFF_et_w_unc2_"+year, "shape", SystMap<>::init(1.00));          
  //////
  cb.cp().channel({"mt"}).process({"jetFakes"})
    .AddSyst(cb, "CMS_FF_closure_OSSS_mvis_mt_qcd_"+year, "shape", SystMap<>::init(1.00));
  cb.cp().channel({"mt"}).process({"jetFakes"})
    .AddSyst(cb, "CMS_FF_closure_lpt_mt_qcd", "shape", SystMap<>::init(1.00));
  cb.cp().channel({"mt"}).process({"jetFakes"})
    .AddSyst(cb, "CMS_FF_closure_lpt_mt_tt", "shape", SystMap<>::init(1.00));
  cb.cp().channel({"mt"}).process({"jetFakes"})
    .AddSyst(cb, "CMS_FF_closure_lpt_mt_w", "shape", SystMap<>::init(1.00));
  cb.cp().channel({"mt"}).process({"jetFakes"})
    .AddSyst(cb, "CMS_FF_closure_lpt_xtrg_mt_qcd_"+year, "shape", SystMap<>::init(1.00));
  cb.cp().channel({"mt"}).process({"jetFakes"})
    .AddSyst(cb, "CMS_FF_closure_lpt_xtrg_mt_tt_"+year, "shape", SystMap<>::init(1.00));
  cb.cp().channel({"mt"}).process({"jetFakes"})
    .AddSyst(cb, "CMS_FF_closure_lpt_xtrg_mt_w_"+year, "shape", SystMap<>::init(1.00));
  cb.cp().channel({"mt"}).process({"jetFakes"})
    .AddSyst(cb, "CMS_FF_closure_mt_mt_w_unc1_"+year, "shape", SystMap<>::init(1.00));
  cb.cp().channel({"mt"}).process({"jetFakes"})
    .AddSyst(cb, "CMS_FF_closure_mt_mt_w_unc2_"+year, "shape", SystMap<>::init(1.00));
  cb.cp().channel({"mt"}).process({"jetFakes"})
    .AddSyst(cb, "CMS_rawFF_mt_qcd_unc1_"+year, "shape", SystMap<>::init(1.00));          
  cb.cp().channel({"mt"}).process({"jetFakes"})
    .AddSyst(cb, "CMS_rawFF_mt_qcd_unc2_"+year, "shape", SystMap<>::init(1.00));          
  cb.cp().channel({"mt"}).process({"jetFakes"})
    .AddSyst(cb, "CMS_rawFF_mt_tt_unc1_"+year, "shape", SystMap<>::init(1.00));          
  cb.cp().channel({"mt"}).process({"jetFakes"})
    .AddSyst(cb, "CMS_rawFF_mt_tt_unc2_"+year, "shape", SystMap<>::init(1.00));          
  cb.cp().channel({"mt"}).process({"jetFakes"})
    .AddSyst(cb, "CMS_rawFF_mt_w_unc1_"+year, "shape", SystMap<>::init(1.00));          
  cb.cp().channel({"mt"}).process({"jetFakes"})
    .AddSyst(cb, "CMS_rawFF_mt_w_unc2_"+year, "shape", SystMap<>::init(1.00));          
  ///////
  cb.cp().channel({"tt"}).process({"jetFakes"})
    .AddSyst(cb, "CMS_FF_closure_tau2pt_tt_qcd", "shape", SystMap<>::init(1.00));
  cb.cp().channel({"tt"}).process({"jetFakes"})
    .AddSyst(cb, "CMS_FF_closure_tt_qcd_osss", "shape", SystMap<>::init(1.00));
  cb.cp().channel({"tt"}).process({"jetFakes"})
    .AddSyst(cb, "CMS_rawFF_tt_qcd_"+year, "shape", SystMap<>::init(1.00));
  //
  //
  cb.cp().channel({"et"}).process(ch::JoinStr({sig_procs, {"ZTTjet"}}))
    .AddSyst(cb, "CMS_eletautrg_"+year, "shape", SystMap<>::init(1.00));
  cb.cp().channel({"et"}).process(ch::JoinStr({{"ZTTjet", "TT"}}))
    .AddSyst(cb, "CMS_scale_e_Scale_"+year, "lnN", SystMap<>::init(1.012));

  // cb.cp().channel({"et"}).process(ch::JoinStr({{"ZTTjet", "TT"}}))
  //   .AddSyst(cb, "CMS_scale_e_Scale_"+year, "shape", SystMap<>::init(1.00));

  cb.cp().channel({"et"}).process(ch::JoinStr({sig_procs, {"ZTTjet", "ZLLjet", "TT" , "otherMC" , "STT", "VVT"}}))
    .AddSyst(cb, "CMS_scale_efaket_1prong1pizero_barrel_"+year, "lnN", SystMap<>::init(1.005));
  cb.cp().channel({"et"}).process(ch::JoinStr({sig_procs, {"ZTTjet", "ZLLjet", "TT" , "otherMC" , "STT", "VVT"}}))
    .AddSyst(cb, "CMS_scale_efaket_1prong1pizero_endcap_"+year, "lnN", SystMap<>::init(1.005));
  cb.cp().channel({"et"}).process(ch::JoinStr({sig_procs, {"ZTTjet", "ZLLjet", "TT" , "otherMC" , "STT", "VVT"}}))
    .AddSyst(cb, "CMS_scale_efaket_1prong_barrel_"+year, "lnN", SystMap<>::init(1.005));
  cb.cp().channel({"et"}).process(ch::JoinStr({sig_procs, {"ZTTjet", "ZLLjet", "TT" , "otherMC" , "STT", "VVT"}}))
    .AddSyst(cb, "CMS_scale_efaket_1prong_endcap_"+year, "lnN", SystMap<>::init(1.005));
  
  cb.cp().channel({"et"}).process(ch::JoinStr({sig_procs, {"ZTTjet", "ZLLjet", "TT" , "otherMC" , "STT", "VVT"}}))
    .AddSyst(cb, "CMS_scale_t_1prong1pizero_"+year, "lnN", SystMap<>::init(1.01));
  cb.cp().channel({"et"}).process(ch::JoinStr({sig_procs, {"ZTTjet", "ZLLjet", "TT" , "otherMC" , "STT", "VVT"}}))
    .AddSyst(cb, "CMS_scale_t_1prong_"+year, "lnN", SystMap<>::init(1.01));
  cb.cp().channel({"et"}).process(ch::JoinStr({sig_procs, {"ZTTjet", "ZLLjet", "TT" , "otherMC" , "STT", "VVT"}}))
    .AddSyst(cb, "CMS_scale_t_3prong1pizero_"+year, "lnN", SystMap<>::init(1.01));
  cb.cp().channel({"et"}).process(ch::JoinStr({sig_procs, {"ZTTjet", "ZLLjet", "TT" , "otherMC" , "STT", "VVT"}}))
    .AddSyst(cb, "CMS_scale_t_3prong_"+year, "lnN", SystMap<>::init(1.01));
  
  cb.cp().channel({"et"}).process(ch::JoinStr({sig_procs, {"ZTTjet", "ZLLjet", "TT" , "otherMC" , "STT", "VVT"}}))
    .AddSyst(cb, "CMS_singleeletrg_"+year, "shape", SystMap<>::init(1.00));
  cb.cp().channel({"et"}).process(ch::JoinStr({sig_procs, {"ZTTjet", "TT" , "otherMC" , "STT", "VVT"}}))
    .AddSyst(cb, "CMS_tauideff_pt30to35_"+year, "shape", SystMap<>::init(1.00));  
  cb.cp().channel({"et"}).process(ch::JoinStr({sig_procs, {"ZTTjet", "TT" , "otherMC" , "STT", "VVT"}}))
    .AddSyst(cb, "CMS_tauideff_pt35to40_"+year, "shape", SystMap<>::init(1.00));
  cb.cp().channel({"et"}).process(ch::JoinStr({sig_procs, {"ZTTjet", "TT" , "otherMC" , "STT", "VVT"}}))
    .AddSyst(cb, "CMS_tauideff_ptgt40_"+year, "shape", SystMap<>::init(1.00));
  ////////
  cb.cp().channel({"mt"}).process(ch::JoinStr({sig_procs, {"ZTTjet", "ZLLjet", "TT" , "otherMC" , "STT", "VVT"}}))
    .AddSyst(cb, "CMS_mutautrg_"+year, "shape", SystMap<>::init(1.00));
  // cb.cp().channel({"mt"}).process(ch::JoinStr({sig_procs, {"ZTTjet", "ZLLjet", "TT" , "otherMC" , "STT", "VVT"}}))
  //   .AddSyst(cb, "CMS_scale_m_etalt1p2_"+year, "shape", SystMap<>::init(1.00));
  // cb.cp().channel({"mt"}).process(ch::JoinStr({sig_procs, {"ZTTjet", "ZLLjet", "TT" , "otherMC" , "STT", "VVT"}}))
  //   .AddSyst(cb, "CMS_scale_m_eta1p2to2p1_"+year, "shape", SystMap<>::init(1.00));
  // cb.cp().channel({"mt"}).process(ch::JoinStr({sig_procs, {"ZTTjet", "ZLLjet", "TT" , "otherMC" , "STT", "VVT"}}))
  //   .AddSyst(cb, "CMS_scale_m_etam2p1to2p4_"+year, "shape", SystMap<>::init(1.00));
  cb.cp().channel({"mt"}).process(ch::JoinStr({sig_procs, {"ZTTjet", "ZLLjet", "TT" , "otherMC" , "STT", "VVT"}}))
    .AddSyst(cb, "CMS_scale_mfaket_1prong1pizero_"+year, "shape", SystMap<>::init(1.00));
  cb.cp().channel({"mt"}).process(ch::JoinStr({sig_procs, {"ZTTjet", "ZLLjet", "TT" , "otherMC" , "STT", "VVT"}}))
    .AddSyst(cb, "CMS_scale_mfaket_1prong1pizero_"+year, "shape", SystMap<>::init(1.00));
  
  cb.cp().channel({"mt"}).process(ch::JoinStr({sig_procs, {"ZTTjet", "ZLLjet", "TT" , "otherMC" , "STT", "VVT"}}))
    .AddSyst(cb, "CMS_scale_t_1prong1pizero_"+year, "lnN", SystMap<>::init(1.01));
  cb.cp().channel({"mt"}).process(ch::JoinStr({sig_procs, {"ZTTjet", "ZLLjet", "TT" , "otherMC" , "STT", "VVT"}}))
    .AddSyst(cb, "CMS_scale_t_1prong_"+year, "lnN", SystMap<>::init(1.01));
  cb.cp().channel({"mt"}).process(ch::JoinStr({sig_procs, {"ZTTjet", "ZLLjet", "TT" , "otherMC" , "STT", "VVT"}}))
    .AddSyst(cb, "CMS_scale_t_3prong1pizero_"+year, "lnN", SystMap<>::init(1.01));
  cb.cp().channel({"mt"}).process(ch::JoinStr({sig_procs, {"ZTTjet", "ZLLjet", "TT" , "otherMC" , "STT", "VVT"}}))
    .AddSyst(cb, "CMS_scale_t_3prong_"+year, "lnN", SystMap<>::init(1.01));
  
  cb.cp().channel({"mt"}).process(ch::JoinStr({sig_procs, {"ZTTjet", "ZLLjet", "TT" , "otherMC" , "STT", "VVT"}}))
    .AddSyst(cb, "CMS_singlemutrg_"+year, "shape", SystMap<>::init(1.00));
  cb.cp().channel({"mt"}).process(ch::JoinStr({sig_procs, {"ZTTjet", "TT" , "otherMC" , "STT", "VVT"}}))
    .AddSyst(cb, "CMS_tauideff_pt30to35_"+year, "shape", SystMap<>::init(1.00));  
  cb.cp().channel({"mt"}).process(ch::JoinStr({sig_procs, {"ZTTjet", "TT" , "otherMC" , "STT", "VVT"}}))
    .AddSyst(cb, "CMS_tauideff_pt35to40_"+year, "shape", SystMap<>::init(1.00));
  cb.cp().channel({"mt"}).process(ch::JoinStr({sig_procs, {"ZTTjet", "TT" , "otherMC" , "STT", "VVT"}}))
    .AddSyst(cb, "CMS_tauideff_ptgt40_"+year, "shape", SystMap<>::init(1.00));

  cb.cp().channel({"tt"}).process(ch::JoinStr({sig_procs, {"ZTTjet", "TT" , "otherMC" , "STT", "VVT"}}))
    .AddSyst(cb, "CMS_doubletautrg_t1_1prong_"+year, "shape", SystMap<>::init(1.00));
  cb.cp().channel({"tt"}).process(ch::JoinStr({sig_procs, {"ZTTjet", "TT" , "otherMC" , "STT", "VVT"}}))
    .AddSyst(cb, "CMS_doubletautrg_t1_1prong1pizero_"+year, "shape", SystMap<>::init(1.00));
  cb.cp().channel({"tt"}).process(ch::JoinStr({sig_procs, {"ZTTjet", "TT" , "otherMC" , "STT", "VVT"}}))
    .AddSyst(cb, "CMS_doubletautrg_t1_3prong_"+year, "shape", SystMap<>::init(1.00));
  cb.cp().channel({"tt"}).process(ch::JoinStr({sig_procs, {"ZTTjet", "TT" , "otherMC" , "STT", "VVT"}}))
    .AddSyst(cb, "CMS_doubletautrg_t1_3prong1pizero_"+year, "shape", SystMap<>::init(1.00));
  
  cb.cp().channel({"tt"}).process(ch::JoinStr({sig_procs, {"ZTTjet", "TT" , "otherMC" , "STT", "VVT"}}))
    .AddSyst(cb, "CMS_scale_t1_1prong1pizero", "lnN", SystMap<>::init(1.02));
  cb.cp().channel({"tt"}).process(ch::JoinStr({sig_procs, {"ZTTjet", "TT" , "otherMC" , "STT", "VVT"}}))
    .AddSyst(cb, "CMS_scale_t1_1prong", "lnN", SystMap<>::init(1.02));
  cb.cp().channel({"tt"}).process(ch::JoinStr({sig_procs, {"ZTTjet", "TT" , "otherMC" , "STT", "VVT"}}))
    .AddSyst(cb, "CMS_scale_t1_3prong1pizero", "lnN", SystMap<>::init(1.02));
  cb.cp().channel({"tt"}).process(ch::JoinStr({sig_procs, {"ZTTjet", "TT" , "otherMC" , "STT", "VVT"}}))
    .AddSyst(cb, "CMS_scale_t1_3prong", "lnN", SystMap<>::init(1.02));
  
  cb.cp().channel({"tt"}).process(ch::JoinStr({sig_procs, {"ZTTjet", "TT" , "otherMC" , "STT", "VVT"}}))
    .AddSyst(cb, "CMS_tauideff_t1_1prong_"+year, "shape", SystMap<>::init(1.00));
  cb.cp().channel({"tt"}).process(ch::JoinStr({sig_procs, {"ZTTjet", "TT" , "otherMC" , "STT", "VVT"}}))
    .AddSyst(cb, "CMS_tauideff_t1_1prong1pizero_"+year, "shape", SystMap<>::init(1.00));
  cb.cp().channel({"tt"}).process(ch::JoinStr({sig_procs, {"ZTTjet", "TT" , "otherMC" , "STT", "VVT"}}))
    .AddSyst(cb, "CMS_tauideff_t1_3prong_"+year, "shape", SystMap<>::init(1.00));
  cb.cp().channel({"tt"}).process(ch::JoinStr({sig_procs, {"ZTTjet", "TT" , "otherMC" , "STT", "VVT"}}))
    .AddSyst(cb, "CMS_tauideff_t1_3prong1pizero_"+year, "shape", SystMap<>::init(1.00));
  cb.cp().channel({"tt"}).process(ch::JoinStr({sig_procs, {"ZTTjet", "TT" , "otherMC" , "STT", "VVT"}}))
    .AddSyst(cb, "CMS_doubletautrg_t2_1prong_"+year, "shape", SystMap<>::init(1.00));
  cb.cp().channel({"tt"}).process(ch::JoinStr({sig_procs, {"ZTTjet", "TT" , "otherMC" , "STT", "VVT"}}))
    .AddSyst(cb, "CMS_doubletautrg_t2_1prong1pizero_"+year, "shape", SystMap<>::init(1.00));
  cb.cp().channel({"tt"}).process(ch::JoinStr({sig_procs, {"ZTTjet", "TT" , "otherMC" , "STT", "VVT"}}))
    .AddSyst(cb, "CMS_doubletautrg_t2_3prong_"+year, "shape", SystMap<>::init(1.00));
  cb.cp().channel({"tt"}).process(ch::JoinStr({sig_procs, {"ZTTjet", "TT" , "otherMC" , "STT", "VVT"}}))
    .AddSyst(cb, "CMS_doubletautrg_t2_3prong1pizero_"+year, "shape", SystMap<>::init(1.00));
  

  cb.cp().channel({"tt"}).process(ch::JoinStr({sig_procs, {"ZTTjet", "TT" , "otherMC" , "STT", "VVT"}}))
    .AddSyst(cb, "CMS_scale_t2_1prong1pizero", "lnN", SystMap<>::init(1.02));
  cb.cp().channel({"tt"}).process(ch::JoinStr({sig_procs, {"ZTTjet", "TT" , "otherMC" , "STT", "VVT"}}))
    .AddSyst(cb, "CMS_scale_t2_1prong", "lnN", SystMap<>::init(1.02));
  cb.cp().channel({"tt"}).process(ch::JoinStr({sig_procs, {"ZTTjet", "TT" , "otherMC" , "STT", "VVT"}}))
    .AddSyst(cb, "CMS_scale_t2_3prong1pizero", "lnN", SystMap<>::init(1.02));
  cb.cp().channel({"tt"}).process(ch::JoinStr({sig_procs, {"ZTTjet", "TT" , "otherMC" , "STT", "VVT"}}))
    .AddSyst(cb, "CMS_scale_t2_3prong", "lnN", SystMap<>::init(1.02));
  

  cb.cp().channel({"tt"}).process(ch::JoinStr({sig_procs, {"ZTTjet", "TT" , "otherMC" , "STT", "VVT"}}))
    .AddSyst(cb, "CMS_tauideff_t2_1prong_"+year, "shape", SystMap<>::init(1.00));
  cb.cp().channel({"tt"}).process(ch::JoinStr({sig_procs, {"ZTTjet", "TT" , "otherMC" , "STT", "VVT"}}))
    .AddSyst(cb, "CMS_tauideff_t2_1prong1pizero_"+year, "shape", SystMap<>::init(1.00));
  cb.cp().channel({"tt"}).process(ch::JoinStr({sig_procs, {"ZTTjet", "TT" , "otherMC" , "STT", "VVT"}}))
    .AddSyst(cb, "CMS_tauideff_t2_3prong_"+year, "shape", SystMap<>::init(1.00));
  cb.cp().channel({"tt"}).process(ch::JoinStr({sig_procs, {"ZTTjet", "TT" , "otherMC" , "STT", "VVT"}}))
    .AddSyst(cb, "CMS_tauideff_t2_3prong1pizero_"+year, "shape", SystMap<>::init(1.00));

  cb.cp().channel({"et", "mt", "tt"}).process(ch::JoinStr({{"ZTTjet"}}))
    .AddSyst(cb, "CMS_htt_boson_reso_met_Jet_"+year, "shape", SystMap<>::init(1.00));
  cb.cp().channel({"et", "mt", "tt"}).process(ch::JoinStr({{"ZTTjet"}}))
    .AddSyst(cb, "CMS_htt_boson_scale_met_Jet_"+year, "shape", SystMap<>::init(1.00));
  cb.cp().channel({"et", "mt", "tt"}).process(ch::JoinStr({{"TT" , "otherMC" , "STT", "VVT"}}))
    .AddSyst(cb, "CMS_scale_met_unclustered_"+year, "shape", SystMap<>::init(1.00));
  // cb.cp().channel({"et", "mt", "tt"}).process(ch::JoinStr({sig_procs, {"ZTTjet"}}))
  //   .AddSyst(cb, "CMS_htt_boson_reso_met_Jet_"+year, "shape", SystMap<>::init(1.00));
  // cb.cp().channel({"et", "mt", "tt"}).process(ch::JoinStr({sig_procs, {"ZTTjet"}}))
  //   .AddSyst(cb, "CMS_htt_boson_scale_met_Jet_"+year, "shape", SystMap<>::init(1.00));
  // cb.cp().channel({"et", "mt", "tt"}).process(ch::JoinStr({sig_procs, {"ZTTjet"}}))
  //   .AddSyst(cb, "CMS_scale_met_unclustered_"+year, "shape", SystMap<>::init(1.00));


  cout << ">> Adding systematic uncertainties...\n";
  // ch::AddSystematics_et_mt(cb);
    
  //cb.cp().process(ch::JoinStr({sig_procs, {"ZTT"}}))
  //    .AddSyst(cb, "CMS_scale_t_mutau_$ERA", "shape", SystMap<>::init(1.00));
  //! [part6]
    
  //! [part7]
  for (string chn : chns) {
    inputFile = input_folders[chn] + ".root";
    cb.cp().channel({chn}).backgrounds().ExtractShapes(
						       aux_shapes + year + "/" + inputFile,
						       "$BIN/$PROCESS",
						       "$BIN/$PROCESS_$SYSTEMATIC");
    cb.cp().channel({chn}).signals().ExtractShapes(
						   aux_shapes + year + "/" + inputFile,
						   "$BIN/$PROCESS$MASS",
						   "$BIN/$PROCESS$MASS_$SYSTEMATIC");
  }
  
    
    
  //! [part7]
    
  //! [part8]
  //    auto bbb = ch::BinByBinFactory()
  //    .SetAddThreshold(0.1)
  //    .SetFixNorm(true);
    
  //    bbb.AddBinByBin(cb.cp().backgrounds(), cb);
    
  // This function modifies every entry to have a standardised bin name of
  // the form: {analysis}_{channel}_{bin_id}_{era}
  // which is commonly used in the htt analyses
  ch::SetStandardBinNames(cb);
    
    
    
  //! [part8]
    
  //! [part9]
  // First we generate a set of bin names:
  set<string> bins = cb.bin_set();
  // This method will produce a set of unique bin names by considering all
  // Observation, Process and Systematic entries in the CombineHarvester
  // instance.
    
  // We create the output root file that will contain all the shapes.
  //TFile output("RHW_mt.inputs.root", "RECREATE");
    
  // Finally we iterate through each bin,mass combination and write a
    
    
  auto pre_drop = cb.syst_name_set();
  //cb.syst_name(droplist, false);
  auto post_drop = cb.syst_name_set();
  cout << ">> Systematics dropped: " << pre_drop.size() - post_drop.size()
       << "\n";
  
    
  string folder = "xtt_datacards_fullrange_zpb";
  boost::filesystem::create_directories(folder);
  boost::filesystem::create_directories(folder + "/common");
  boost::filesystem::create_directories(folder + "/" + "ZprimeBaryonic_mzp"+mediatorMass+"_mchi"+pscalarMass);
  for (auto m : masses) {
    boost::filesystem::create_directories(folder + "/" + m);
  }
    
  for (string chn : chns) {
    TFile output((folder + "/common/"+chn+"_"+year+"_ZprimeBaryonic_mzp"+mediatorMass+"_mchi"+pscalarMass+".root").c_str(),
		 "RECREATE");
    auto bins = cb.cp().channel({chn}).bin_set();
    for (auto b : bins) {
      for (auto m : masses) {
	cout << ">> Writing datacard for bin: " << b << " and mass: " << m
	     << "\r" << flush;
	cb.cp().channel({chn}).bin({b}).mass({m, "*"}).WriteDatacard(
								     folder + "/" + "ZprimeBaryonic_mzp"+mediatorMass+"_mchi"+pscalarMass + "/" + b + "_" + year+ ".txt", output);
      }
    }
    output.Close();
  }
  string final_folder = folder + "/" + "ZprimeBaryonic_mzp"+mediatorMass+"_mchi"+pscalarMass;
  cout << ">> Datacards created in : " << final_folder
       << "\n\n";
  //! [part9]
    
}


