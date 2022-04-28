import CombineHarvester.CombineTools.plotting as plot
from ROOT import *
import ROOT
import numpy
from style import *
import array 
ROOT.PyConfig.IgnoreCommandLineOptions = True
ROOT.gROOT.SetBatch(ROOT.kTRUE)

plot.ModTDRStyle()
import argparse

def fixBinning(hist=None , refHist=None ):
    if hist is None or refHist is None:
        print "Define input histograms"
        return
    nDivXAxis= refHist.GetNbinsX()
    tmpHist = refHist.Clone()
    tmpHist.Reset()
    for ibin in range(1, nDivXAxis+1):
        tmpHist.SetBinContent(ibin , hist.GetBinContent(ibin))
    return tmpHist

prefit_color = kOrange+8
postfit_color = kBlue+2
other_color = kAzure+1
# declare colors
color_ztt="#ffcc66"
color_zll="#4496c8"
color_tt="#9999cc"
color_ggh="#12cadd"
color_vv="#990099"
color_wjets="#cc6666" 
color_jetfake="#f1cde1"
MinRange, MaxRange = 40, 200

# sr_colormap = {
#   'ZJets':{'leg':'Z #rightarrow #nu#nu','col':kRed},
#   'WJets':{'leg':'W #rightarrow l#nu','col':kViolet},
#   'DYJets':{'leg':'Z #rightarrow ll','col':kSpring},
#   'GJets':{'leg':'#gamma + jets','col':kYellow},
#   'TTJets':{'leg':'TT Jets','col':kPink},
#   'QCD':{'leg':'QCD','col':kYellow+3},
#   'DiBoson':{'leg':'WW/WZ/ZZ','col':kCyan},  
# }
def makeHistogram(graph,template):
    hs = template.Clone();
    npoints = graph.GetN()
    for i in range(npoints):
        x,y=Double(0),Double(0)
        graph.GetPoint(i,x,y)
        xerr = graph.GetErrorX(i)
        yerr = graph.GetErrorY(i)
        hs.SetBinContent(i+1,y)
        hs.SetBinError(i+1,yerr)
    return hs;
def getFitRatio(data_hs, prefit_hs,postfit_hs):
    prefit_ratio = data_hs.Clone('prefit_ratio')
    prefit_ratio.Divide(prefit_hs)
    if not postfit_hs:
        postfit_ratio = None
        return
    postfit_ratio = data_hs.Clone('postfit_ratio')
    postfit_ratio.Divide(postfit_hs)
    return prefit_ratio, postfit_ratio
def SigmaPull(data,postfit,show=True):
    pull = data.Clone("pull")
    pull.Add(postfit,-1)
    TH1.StatOverflows(1)

    addedsqrt = 0
    mean = 0
    sigma = 0
    chi2 = 0
    for ibin in range(1,pull.GetNbinsX()+1):
        if postfit[ibin] <= 0: continue
        if postfit.GetBinError(ibin) == 0 : continue 
        addedsqrt += (pull.GetBinContent(ibin)**2)/(postfit.GetBinError(ibin)**2)
        sigma = TMath.Sqrt(postfit.GetBinError(ibin)**2 + data.GetBinError(ibin)**2)
        pull.SetBinContent(ibin,pull.GetBinContent(ibin)/sigma)

        pull.SetBinError(ibin,0)
        mean += pull.GetBinContent(ibin)
        chi2 += pull.GetBinContent(ibin)**2

    if show:
        print "MEAN: ", mean/pull.GetNbinsX()
        print "CHI2: ", TMath.Sqrt(chi2)/pull.GetNbinsX()
        
        print "Added", TMath.Sqrt(addedsqrt), "divided: ", TMath.Sqrt(addedsqrt)/pull.GetNbinsX()
        print "Added2", addedsqrt, "divided: ", addedsqrt/pull.GetNbinsX()
    
    return pull
    
def plotCR(ch='et', year="2017"):
    
    fin = ROOT.TFile('postfit_shapes_'+ch+"_"+year+'.root' , "r")
    #f_ref = TFile('../common/'+ch+'_2017_2hdma_med400_ps150.root',"r")
    #hist_ref  = f_ref.Get('xtt_'+ch+'_1_13TeV/data_obs')

    c = TCanvas("c", "canvas",800,800);
    gStyle.SetOptStat(0);
    gStyle.SetLegendBorderSize(0);
    
    pad1 = TPad("pad1","pad1",0.,0.33,1.0,1.0)
    pad1.Draw(); pad1.cd()
    #pad1.SetLogy()
    pad1.SetBottomMargin(0)
    postfitDir = 'xtt_'+ch+'_1_13TeV_postfit'
    prefitDir = 'xtt_'+ch+'_1_13TeV_prefit'
    prefit_hs = fin.Get(prefitDir + '/TotalBkg')
    postfit_hs = fin.Get(postfitDir + '/TotalBkg')
    data_hs = fin.Get(prefitDir +'/data_obs')
    data_clone = data_hs.Clone()
    #data_hs =  makeHistogram(data_graph,prefit_hs)
    #fitfile.getOtherBkg(cr)
    #other_bkg = fitfile.other_bkg
    ZTTjet = fin.Get(postfitDir + '/' + 'ZTTjet')
    if ch=='et' or ch=='mt':
        ZLLjet = fin.Get(postfitDir + '/' + 'ZLLjet')
    jetFakes = fin.Get(postfitDir + '/' + 'jetFakes')    
    TT     = fin.Get(postfitDir + '/' + 'TT')
    STT = fin.Get(postfitDir + '/' + 'STT')
    VVT = fin.Get(postfitDir + '/' + 'VVT')
    otherMC = fin.Get(postfitDir + '/' + 'otherMC')
    new_bining = array.array('d' , [ 40, 60, 90, 120, 150, 180, 210, 235, 260, 285, 325, 400, 2000])
    # ZTTjet = ZTTjet.Rebin(12, 'ZTTjet' , new_bining)
    # ZLLjet  = ZLLjet.Rebin(12, 'ZLLjet' , new_bining)
    # jetFakes = jetFakes.Rebin(12, 'jetFakes' , new_bining)
    # TT  = TT.Rebin(12, 'TT' , new_bining)
    # STT = STT.Rebin(12, 'STT' , new_bining)
    # VVT =  VVT.Rebin(12, 'VVT' , new_bining)
    # otherMC = otherMC.Rebin(12, 'otherMC' , new_bining)
    # jetFakes = fixBinning(jetFakes, hist_ref)
    # ZTTjet = fixBinning(ZTTjet, hist_ref)
    # ZLLjet = fixBinning(ZLLjet, hist_ref)
    # TT     = fixBinning(TT, hist_ref)
    # STT    = fixBinning(STT, hist_ref)
    # VVT    = fixBinning(VVT, hist_ref)
    # otherMC= fixBinning(otherMC, hist_ref)

    jetFakes.SetFillColor(ROOT.TColor.GetColor(color_jetfake))
    ZTTjet.SetFillColor(ROOT.TColor.GetColor(color_ztt))
    if ch=='et' or ch=='mt':
        ZLLjet.SetFillColor(ROOT.TColor.GetColor(color_zll))
    TT.SetFillColor(ROOT.TColor.GetColor(color_tt))
    otherMC.SetFillColor(ROOT.TColor.GetColor(color_ggh))
    VVT.SetFillColor(ROOT.TColor.GetColor(color_vv))
    STT.SetFillColor(ROOT.TColor.GetColor(color_vv))

    # prefit_hs = fixBinning(prefit_hs, hist_ref)
    # postfit_hs = fixBinning(postfit_hs, hist_ref)
    # data_hs = fixBinning(data_hs, hist_ref)
    if ch=='et' or ch=='mt':
        sampleList = [data_hs, ZTTjet, ZLLjet, jetFakes, TT , otherMC, STT, VVT ]
        sampleListRef = ['Data_hist', 'ZTTjet', 'ZLLjet', 'jetFakes', 'TT', 'STT', 'VVT' , 'otherMC' ]
    else:
        sampleList = [data_hs, ZTTjet,  jetFakes, TT , otherMC, STT, VVT ]
        sampleListRef = ['Data_hist', 'ZTTjet', 'jetFakes', 'TT', 'STT', 'VVT' , 'otherMC' ]
        
    stack=ROOT.THStack("stack","stack") 
    stack.Add(otherMC)
    stack.Add(VVT)
    stack.Add(STT)
    stack.Add(TT)
    stack.Add(jetFakes)
    if ch=='et' or ch=='mt':
        stack.Add(ZLLjet)
    stack.Add(ZTTjet)
    
    errorBand = jetFakes.Clone()
    errorBand.Add(ZTTjet)
    if ch=='et' or ch=='mt':
        errorBand.Add(ZLLjet)
    errorBand.Add(TT)
    errorBand.Add(STT)
    errorBand.Add(VVT)
    errorBand.Add(otherMC)
    errorBand.SetMarkerSize(0)
    errorBand.SetFillColor(16)
    errorBand.SetFillStyle(3001)
    errorBand.SetLineWidth(1)

    ### uncomment this to blind data above 200 GeV
    nbins = data_hs.GetNbinsX()
    # for i in range(1, nbins+1):
    #     if i > 8:
    #         data_hs.SetBinContent(i, 0)
    # new_bining = array.array('d' , [ 40, 60, 90, 120, 150, 180, 210, 235, 260, 285, 325, 400, 2000])
    # prefit_hs = prefit_hs.Rebin(12, 'prefit' , new_bining)
    # postfit_hs = postfit_hs.Rebin(12, 'postfit' , new_bining)
    # data_hs = data_hs.Rebin(12, 'data' , new_bining)
    prefit_hs.GetXaxis().SetRangeUser(MinRange ,MaxRange)
    prefit_hs.Draw("hist"); 
    prefit_hs.SetMinimum(0.1)
    prefit_hs.SetMaximum(1.5* max(prefit_hs.GetMaximum(), postfit_hs.GetMaximum(), data_hs.GetMaximum()))
    fit_style(prefit_hs,prefit_color);
    #set_bounds(prefit_hs)
    postfit_hs.Draw("hist same"); 
    fit_style(postfit_hs,postfit_color)
    #other_bkg.Draw("hist same"); other_style(other_bkg,other_color)
    #jetFakes.Draw("hist same");
    stack.Draw("hist same");
    errorBand.Draw("e2same")
    data_hs.Draw("pex0 same") 
    #data_style(data_graph)
    # prefit_hs.Draw("Axis same")
    pad1.RedrawAxis()
    
    leg = getLegend()
    leg.AddEntry(data_hs,"Data","lp")
    leg.AddEntry(postfit_hs,"Post-fit ",'f')
    leg.AddEntry(prefit_hs,"Pre-fit ",'f')
    legendNameList = {
        'Data_hist'  : 'Data obs',
        'ZTTjet'   : 'Z->tautau',
        'jetFakes'      : 'jet-tau fake', 
        'TT'    : 'ttabr',
        'VVT'    : 'VV',
        'STT'    : 'SingleTop', 
        'otherMC' : 'Other'
    }
    if ch=='et' or ch=='mt':
        legendNameList['ZLLjet'] = 'Z-> ll',
    #for i in range(1, len(sampleListRef)):
    #    leg.AddEntry(sampleList[i], legendNameList[sampleListRef[i]], "f")
    leg.AddEntry(data_hs, 'data', "f")
    leg.AddEntry(ZTTjet, 'Z->tautau', "f")
    if ch=='et' or ch=='mt':
        leg.AddEntry(ZLLjet, 'Z-> ll', "f")
    leg.AddEntry(jetFakes, 'jet-tau fake', "f")
    leg.AddEntry(TT, 'ttbar', "f")
    leg.AddEntry(otherMC, 'Other', "f")
    leg.AddEntry(STT, 'SingleTop', "f")
    leg.AddEntry(VVT, 'VV', "f")
    # #leg.AddEntry(other_bkg,"Other Backgrounds",'f')
    leg.Draw()
    
    texCMS,texLumi = getCMSText(ch, year)
    
    ##############################
    c.cd()
    pad2 = TPad("pad2","pad2",0.,0.,1.0,0.33)
    pad2.Draw(); pad2.cd()
    pad2.SetTopMargin(0)
    
    pad3 = TPad("pad3","pad3",0.,0.65,1.,1.)
    pad3.Draw(); pad3.cd()
    pad3.SetTopMargin(0); pad3.SetBottomMargin(0)
    
    prefit_ratio, postfit_ratio = getFitRatio(data_hs, prefit_hs, postfit_hs)
    h1 = errorBand.Clone()
    h3=data_hs.Clone()
    h1.Divide(errorBand)
    errorBandZeroErr=errorBand.Clone()
    for ibin in range(errorBandZeroErr.GetXaxis().GetNbins()):
        errorBandZeroErr.SetBinError(ibin+1,0)
    #######
    h3.Divide(errorBandZeroErr)
    prefit_ratio.GetXaxis().SetRangeUser(MinRange ,MaxRange)
    prefit_ratio.Draw('pe')
    ratio_style(prefit_ratio,prefit_color, 0, 2)
    #prefit_ratio.GetYaxis().SetTitleSize(0.058)
    if postfit_ratio: 
        postfit_ratio.Draw('pesame'); 
        ratio_style(postfit_ratio,postfit_color, 0, 2)
    ###############################
    h1.GetXaxis().SetRangeUser(MinRange ,MaxRange)
    h1.Draw("e2same")
    #h3.Draw("E2same")
    prefit_ratio.SetMaximum(1.5)
    prefit_ratio.SetMinimum(0.5)


    pad2.cd()
    pad4 = TPad("pad4","pad4",0.,0.,1.,0.65)
    pad4.Draw(); pad4.cd()
    pad4.SetTopMargin(0);
    pad4.SetBottomMargin(0.5)
    if postfit_hs:
        sigma_pull = SigmaPull(data_clone, postfit_hs)
        sigma_pull.Draw('hist'); 
        pull_style(sigma_pull,postfit_color)
        #xname = sigma_pull.GetXaxis().GetTitle().replace("(","[").replace(")","]")
        sigma_pull.GetXaxis().SetTitle( "" )
        
    ##############################
    
    outname = '_postfit_pull_'+ch+"_"+year+'.png'
    c.SaveAs(outname)

    pad4.Draw()
    pad4.cd()
    pad4.SetTopMargin(0);
    pad4.SetBottomMargin(0.5)
    den = postfit_hs.Clone()
    n_prefit = prefit_hs.Clone()
    n_postfit = postfit_hs.Clone()
    n_prefit.Divide(den)
    n_postfit.Divide(den)
    n_postfit.GetXaxis().SetRangeUser(MinRange ,MaxRange)
    n_postfit.Draw("hist")
    n_prefit.Draw("histsame")
    n_postfit.GetYaxis().SetLabelSize(0.08)
    n_postfit.GetXaxis().SetLabelSize(0.08)
    n_postfit.SetMaximum(1.2)
    n_postfit.SetMinimum(0.8)
    n_postfit.GetXaxis().SetTitle( "total tr. mass [GeV]" )
    n_postfit.GetYaxis().SetTitle( "#frac{prefit}{postfit}" )
    n_postfit.GetYaxis().SetTitleSize(0.15)
    n_postfit.GetXaxis().SetTitleSize(0.15)
    n_postfit.GetYaxis().SetTitleOffset(0.3)
    outname = '_postfit_ratio_'+ch+"_"+year+'.png'
    c.SaveAs(outname)

if __name__=="__main__":
    channels=['et']
    # Initialize parser
    parser = argparse.ArgumentParser()
    parser.add_argument("-ch",
                        help="name channel to plot : et , mt , tt")
    parser.add_argument("-y",
                        help="year : 2017 or 2018")
    args =  parser.parse_args()
    ch=args.ch
    year = args.y
    if ch is None:
        ch = 'et'
    if year is None:
        year = "2017"
    plotCR(ch, year)
