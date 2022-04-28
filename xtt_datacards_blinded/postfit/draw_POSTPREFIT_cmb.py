#!/usr/bin/env python
import ROOT
from ROOT import *
import sys
import re
from array import array
import ROOT as rt
import argparse
 

def add_lumi( channel_='et', year_="2017"):
    lowX=0.55
    lowY=0.84
    lumi  = ROOT.TPaveText(lowX, lowY+0.04, lowX+0.30, lowY+0.14, "NDC")
    lumi.SetBorderSize(   0 )
    lumi.SetFillStyle(    0 )
    lumi.SetTextAlign(   12 )
    lumi.SetTextColor(    1 )
    lumi.SetTextSize(0.06)
    lumi.SetTextFont (   42 )
    if year_=="2018":
        lumiProcessed="11.94"
    else:
        lumiProcessed="8.2"
    ch_label = "e#tau_{h} "
    if channel_=="mt":
        ch_label = "#mu#tau_{h} "
    if channel_=="et":
        ch_label = "e#tau_{h} "
    if channel_=="tt":
        ch_label = "#tau_{h}#tau_{h} "
    
    lumi.AddText(ch_label + " " + year_+ " " + lumiProcessed+"fb^{-1} (13 TeV)")
    return lumi

def add_CMS():
    lowX=0.21
    lowY=0.70
    lumi  = ROOT.TPaveText(lowX, lowY+0.06, lowX+0.15, lowY+0.16, "NDC")
    lumi.SetTextFont(61)
    lumi.SetTextSize(0.08)
    lumi.SetBorderSize(   0 )
    lumi.SetFillStyle(    0 )
    lumi.SetTextAlign(   12 )
    lumi.SetTextColor(    1 )
    lumi.AddText("CMS")
    return lumi

def add_Preliminary():
    lowX=0.21
    lowY=0.63
    lumi  = ROOT.TPaveText(lowX, lowY+0.06, lowX+0.15, lowY+0.16, "NDC")
    lumi.SetTextFont(52)
    lumi.SetTextSize(0.06)
    lumi.SetBorderSize(   0 )
    lumi.SetFillStyle(    0 )
    lumi.SetTextAlign(   12 )
    lumi.SetTextColor(    1 )
    lumi.AddText("Preliminary")
    return lumi

def make_legend():
    output = ROOT.TLegend(0.5, 0.6, 0.92, 0.85, "", "brNDC")
    output.SetLineWidth(0)
    output.SetLineStyle(0)
    output.SetFillStyle(0)
    output.SetBorderSize(0)
    output.SetTextFont(62)
    output.SetNColumns(2)
    
    return output

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


def MakePlot_v2(cat='prefit', ch='et',  year="2017"):
    Status = ''
    Channel = ch
    HistName = ''
    Xaxis = "tot tr. mass [GeV]"
    MinRange, MaxRange = 40, 200
    ROOT.gStyle.SetFrameLineWidth(3)
    ROOT.gStyle.SetLineWidth(3)
    ROOT.gStyle.SetOptStat(0)
#    ROOT.gStyle.SetErrorX(0.0001);
    RB_=1

    c=ROOT.TCanvas("canvas","",0,0,1000,1000)
    c.cd()

    infile=ROOT.TFile('postfit_shapes_cmb_20172018.root',"r")

    adapt=ROOT.gROOT.GetColor(12)
    new_idx=ROOT.gROOT.GetListOfColors().GetSize() + 1
    #    trans=ROOT.TColor(new_idx, adapt.GetRed(), adapt.GetGreen(),adapt.GetBlue(), "",0.5)
    #    categories=["MuTau_DiJet","MuTau_JetBJet"]
    #    ncat=
    
    category = ch+'_'+year+'_'+cat  # et_2017_prefit
    # if 'ch1' in cat:
    #     ch = 'et'
    # elif 'ch2' in cat:
    #     ch = 'mt'
    # elif 'ch3' in cat:
    #     ch = 'tt'
    Data=infile.Get(category).Get("data_obs")  
    Data.Rebin(RB_)
    
    for ibin in range(Data.GetNbinsX()):
        xbin= ibin+1
        LowEdge=int(Data.GetBinLowEdge(xbin))
        endEdge=int(Data.GetBinLowEdge(xbin)+Data.GetBinWidth(xbin))
        data_val= int(round(infile.Get(category).Get("data_obs").GetBinContent(xbin)))
        bkg_val=infile.Get(category).Get("TotalBkg").GetBinContent(xbin)
        bkg_val_err=infile.Get(category).Get("TotalBkg").GetBinError(xbin)
    #print "data integral = ", Data.Integral()
    ZTTjet = infile.Get(category).Get("ZTTjet")
    ZTTjet.Rebin(RB_)
    if ch=='et' or ch=='mt':
        ZLLjet = infile.Get(category).Get("ZLLjet")
        ZLLjet.Rebin(RB_)
    jetFakes= infile.Get(category).Get("jetFakes")
    jetFakes.Rebin(RB_)
    TT     = infile.Get(category).Get("TT")
    TT.Rebin(RB_)
    STT= infile.Get(category).Get("STT")
    STT.Rebin(RB_)
    VVT = infile.Get(category).Get("VVT")
    VVT.Rebin(RB_)
    otherMC = infile.Get(category).Get("otherMC")
    otherMC.Rebin(RB_)
    
    sig = 'MH3_400_MH4_150'
    Signal=infile.Get(category.replace('postfit','prefit')).Get(sig)
    #Signal.Scale( 50)  # CS x BR  1000_400_440  // factor of 2 is added as we consider the full doublet
    # Signal.Rebin(RB_)
    # #    Signal.SetFillStyle(0.)
    # Signal.SetLineStyle(11)
    # Signal.SetLineWidth(3)
    # Signal.SetLineColor(4)
    # Signal.SetMarkerColor(4)
    # Signal.SetLineStyle(8)

    # Signal.SetLineColor(ROOT.TColor.GetColor(108, 226, 354))
    # Signal.SetMarkerColor(ROOT.TColor.GetColor(108, 226, 354))
    # Signal.SetLineColor(kBlue)
    # ##### chnage binning content
    # ALLSample=[Data, ZTTjet, ZLLjet, jetFakes, TT, STT, VVT, otherMC]
    # for sample in ALLSample:
    #     for ibin in range(sample.GetXaxis().GetNbins()):
    #         # print ibin+1, sample.GetBinWidth(ibin+1)
    #         sample.SetBinContent(ibin+1,1.0*sample.GetBinContent(ibin+1)/sample.GetBinWidth(ibin+1))
    #         sample.SetBinError(ibin+1,1.0*sample.GetBinError(ibin+1)/sample.GetBinWidth(ibin+1))

    #         if sample==Data and sample.GetBinContent(ibin+1)==0: #https://twiki.cern.ch/twiki/bin/view/CMS/PoissonErrorBars
    #             sample.SetBinError(ibin+1,1.0*1.8/sample.GetBinWidth(ibin+1))
    

    

    Data.GetXaxis().SetTitle("")
    Data.GetXaxis().SetTitleSize(0)
    Data.GetXaxis().SetNdivisions(506)
    Data.GetYaxis().SetLabelFont(42)
    Data.GetYaxis().SetLabelOffset(0.01)
    Data.GetYaxis().SetLabelSize(0.06)
    Data.GetYaxis().SetTitleSize(0.075)
    Data.GetYaxis().SetTitleOffset(1.04)
    Data.SetTitle("")
    Data.GetYaxis().SetTitle("Events / GeV")



    # jetFakes.SetFillColor(ROOT.TColor.GetColor(408, 106, 154))
    # ZTTjet.SetFillColor(ROOT.TColor.GetColor(200, 2, 285))
    # ZLLjet.SetFillColor(ROOT.TColor.GetColor(208, 376, 124))
    # TT.SetFillColor(ROOT.TColor.GetColor(150, 132, 232))
    # STT.SetFillColor(ROOT.TColor.GetColor(200, 282, 232))
    # VVT.SetFillColor(ROOT.TColor.GetColor(108, 226, 354))
    # otherMC.SetFillColor(ROOT.TColor.GetColor(108, 226, 354))
    jetFakes.SetFillColor(ROOT.TColor.GetColor(color_jetfake))
    ZTTjet.SetFillColor(ROOT.TColor.GetColor(color_ztt))
    if ch=='et' or ch=='mt':
        ZLLjet.SetFillColor(ROOT.TColor.GetColor(color_zll))
    TT.SetFillColor(ROOT.TColor.GetColor(color_tt))
    otherMC.SetFillColor(ROOT.TColor.GetColor(color_ggh))
    VVT.SetFillColor(ROOT.TColor.GetColor(color_vv))
    STT.SetFillColor(ROOT.TColor.GetColor(color_vv))

    Data.SetMarkerStyle(20)
    Data.SetMarkerSize(1)
    jetFakes.SetLineColor(ROOT.kBlack)
    ZTTjet.SetLineColor(ROOT.kBlack)
    if ch=='et' or ch=='mt':
        ZLLjet.SetLineColor(ROOT.kBlack)
    TT.SetLineColor(ROOT.kBlack)
    STT.SetLineColor(ROOT.kBlack)
    VVT.SetLineColor(ROOT.kBlack)
    Data.SetLineColor(ROOT.kBlack)
    Data.SetLineWidth(2)

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

    pad1 = ROOT.TPad("pad1","pad1",0,0.35,1,1)
    pad1.Draw()
    pad1.cd()
    #    if Status == "LOG" : pad1.SetLogy() ; pad1.SetLogx()
    if Status == "LOG" : pad1.SetLogy()
    
    pad1.SetFillColor(0)
    pad1.SetBorderMode(0)
    pad1.SetBorderSize(10)
    pad1.SetTickx(1)
    pad1.SetTicky(1)
    pad1.SetLeftMargin(0.18)
    pad1.SetRightMargin(0.05)
    pad1.SetTopMargin(0.122)
    pad1.SetBottomMargin(0.026)
    pad1.SetFrameFillStyle(0)
    pad1.SetFrameLineStyle(0)
    pad1.SetFrameLineWidth(3)
    pad1.SetFrameBorderMode(0)
    pad1.SetFrameBorderSize(10)

    Data.GetXaxis().SetLabelSize(0)
    
    if Status == "LOG" :Data.SetMaximum(Data.GetMaximum()*2000); Data.SetMinimum(0.001)
    #    if Status == "LOG" :Data.SetMaximum(999); Data.SetMinimum(0.01)
    if Status=="": Data.SetMaximum(Data.GetMaximum()*2) ;  Data.SetMinimum(0)


    Data.GetXaxis().SetRangeUser(MinRange ,MaxRange)
    
    Data.SetBinErrorOption(rt.TH1.kPoisson)
    Data.Draw("ex0")
    stack.Draw("histsame")
    errorBand.Draw("e2same")
    Data.Draw("ex0same")
    
    legende=make_legend()
    legende.AddEntry(Data,"Observed","elp")
    #    legende.AddEntry(Signal,sigLeg,"l")
    legende.AddEntry(jetFakes,"jetfakes","f")
    #    legende.AddEntry(Signal2,sigLeg2,"l")
    legende.AddEntry(TT,"t#bar{t}","f")
    legende.AddEntry(ZTTjet,"ZTT","f")
    if ch=='et' or ch=='mt':
        legende.AddEntry(ZLLjet,"ZLL","f")
    legende.AddEntry(STT,"STT","f")
    legende.AddEntry(VVT,"VVT ","f")
    legende.AddEntry(otherMC,"otherMC","f")
    legende.AddEntry(errorBand,"Total uncertainty","f")

    legende.Draw()

    l1=add_lumi(ch, year)
    l1.Draw("same")
    l2=add_CMS()
    l2.Draw("same")
    l3=add_Preliminary()
    l3.Draw("same")

    pad1.RedrawAxis()
    
    categ  = ROOT.TPaveText(0.5, 0.5, 0.9, 0.4, "NDC")
    categ.SetBorderSize(   0 )
    categ.SetFillStyle(    0 )
    categ.SetTextAlign(   12 )
    categ.SetTextSize ( 0.06 )
    categ.SetTextColor(    1 )
    categ.SetTextFont (   61 )
    #       if i==1 or i==3:
    categ.AddText(cat.split('_')[-1]+"  "+ ch)
    #       else :
    #        categ.AddText("SS")
    categ.Draw()
    
    c.cd()
    pad2 = ROOT.TPad("pad2","pad2",0,0,1,0.35);
    #    if Status == "LOG" : pad2.SetLogx()
    #    pad2.GetXaxis().SetRangeUser(200,5000)
    pad2.SetTopMargin(0.05);
    pad2.SetBottomMargin(0.35);
    pad2.SetLeftMargin(0.18);
    pad2.SetRightMargin(0.05);
    pad2.SetTickx(1)
    pad2.SetTicky(1)
    pad2.SetFrameLineWidth(3)
    #    pad2.SetGridx()
    pad2.SetGridy()
    pad2.Draw()
    pad2.cd()
    
    h1=errorBand.Clone()
 
    
    h1.SetMinimum(0.1)
    h1.SetMarkerStyle(20)

    h3=Data.Clone()


    h3.Sumw2()
    h1.Sumw2()
    
    
    h1.SetStats(0)
    h3.SetStats(0)
    h1.SetTitle("")
    
    h1.Divide(errorBand)
    #######  set the bin errors to zero befive divinig data to that
    errorBandZeroErr=errorBand.Clone()
    for ibin in range(errorBandZeroErr.GetXaxis().GetNbins()):
        errorBandZeroErr.SetBinError(ibin+1,0)
    #######
    h3.Divide(errorBandZeroErr)

    for jbin in range(h3.GetXaxis().GetNbins()):
        print h3.GetBinContent(jbin+1), " +/- " ,h3.GetBinError(jbin+1)


    #h1.GetXaxis().SetRangeUser(20,2000)
    h1.GetXaxis().SetTitle(Xaxis)
    h1.GetXaxis().SetLabelSize(0.08)
    h1.GetYaxis().SetLabelSize(0.08)
    h1.GetYaxis().SetTitle("Obs./Exp.")
    h1.GetXaxis().SetNdivisions(506)
    h1.GetYaxis().SetNdivisions(5)
    h1.GetXaxis().SetTitleSize(0.15)
    h1.GetYaxis().SetTitleSize(0.15)
    h1.GetYaxis().SetTitleOffset(0.5)
    h1.GetYaxis().SetLabelOffset(0.02)
    h1.GetXaxis().SetTitleOffset(0.9)
    h1.GetXaxis().SetLabelSize(0.11)
    h1.GetYaxis().SetLabelSize(0.11)
    h1.GetXaxis().SetTitleFont(42)
    h1.GetYaxis().SetTitleFont(42)
    h1.GetXaxis().SetRangeUser(MinRange ,MaxRange)
    h1.GetYaxis().SetRangeUser(.01,1.99)
    #    h1.GetYaxis().SetRangeUser(0,1.99)
    #    h1.SetMaximum(1.99)
    #    for i in range(h3.GetNbinsX()):
    #        if i > 5 : h3.SetBinContent(i+1,0)
    # h1.SetMaximum(1.5)
    # h1.SetMinimum(0.5)
    h1.Draw("e2")
    h3.Draw("Ex0psame")
    #    c.cd()
    #    pad1.Draw()
    
    #ROOT.gPad.RedrawAxis()
    
    #    c.Modified()
    #    c.Modified()
    #c.SaveAs("_Finalplot_"+prefix+category+Status+"_"+Channel+"_"+year+".pdf")
    c.SaveAs("_Finalplot_combined_"+category+Status+".png")

    print "Data.Integral()", infile.Get(category).Get("data_obs").Integral()


if __name__=="__main__":
    #MakePlot('postfit_shapes.root' , category,HistName,Xaxis, Status, Channel)
    prefix = ['prefit', 'postfit']
    channels=['et', 'mt', 'tt']
    
    for ch in channels:
        for cat in prefix:
            MakePlot_v2(cat, ch, '2017')
            MakePlot_v2(cat, ch, '2018')
    # MakePlot_v2('ch1_prefit', ch, year)
    # MakePlot_v2('ch1_postfit', ch, year)
    # MakePlot_v2('ch2_prefit', ch, year)
    # MakePlot_v2('ch2_postfit', ch, year)
    # MakePlot_v2('ch3_prefit', ch, year)
    # MakePlot_v2('ch3_postfit', ch, year)
