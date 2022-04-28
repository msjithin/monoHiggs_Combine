#!/usr/bin/env python
import ROOT
import re
from array import array
import sys
import csv
from math import sqrt
from math import pi
import datetime
import argparse
# from sys import path
# path.append("../../../MacrosAndScripts/")
# from myPlotStyle import *
ROOT.gStyle.SetFrameLineWidth(1)
ROOT.gStyle.SetLineWidth(2)
ROOT.gStyle.SetOptStat(0)


def GetKeyNames( self, dir = "" ):
    self.cd(dir)
    return [key.GetName() for key in ROOT.gDirectory.GetListOfKeys()]
ROOT.TFile.GetKeyNames = GetKeyNames

bkg_mapping = { 'etau_2017' : {}, 'mutau_2017': {}, 'tautau_2017':{}, 'etau_2018' : {}, 'mutau_2018': {}, 'tautau_2018':{} }
    

def fix_binning(inFile, channelName, year):
    bkg_mapping = { 'etau_2017' : {}, 'mutau_2017': {}, 'tautau_2017':{}, 'etau_2018' : {}, 'mutau_2018': {}, 'tautau_2018':{} }
    keyList = inFile.GetKeyNames(channelName)
    inFile.cd(channelName)
    for hist in keyList:
        tmpHist = inFile.Get(channelName + '/' + hist)
        if 'Up' in hist[-10:] or 'Down' in hist[-10:] : continue
        if 'data' in hist : continue
        bkgname = hist.split('_')
        if 'MH3' in bkgname : bkgname = '_'.join(bkgname[:4])
        else : bkgname = bkgname[0]
        print bkgname
        for ibin in range(1, tmpHist.GetNbinsX() + 1):
            ibinContent = tmpHist.GetBinContent(ibin)
            if ibinContent <= 0 :
                new_content = 0.001
                #print "check this ************************** " , hist
                if bkgname not in bkg_mapping[channelName+"_"+year]:
                    bkg_mapping[channelName+"_"+year][bkgname] = [ibin]
                    #bkg_mapping[channelName+"_"+year][bkgname].append(ibin)
                    #print " doubling !!!!!!!!!!! " , ibin, bkgname , channelName
                else :
                    bkg_mapping[channelName+"_"+year][bkgname].append(ibin)
                tmpHist.SetBinContent(ibin, new_content)
                #print hist , ibin , ' bin content set to 0.001'
                tmpHist.Write()
    return bkg_mapping

def fix_binning_systematics(inFile, channelName, year, bkg_mapping):
    keyList = inFile.GetKeyNames(channelName)
    inFile.cd(channelName)
    for hist in keyList:
        #print hist
        tmpHist = inFile.Get(channelName + '/' + hist)
        if 'Up' not in hist[-10:] and 'Down' not in hist[-10:] : continue
        bkgname = hist.split('_')
        if 'MH3' in bkgname : bkgname = '_'.join(bkgname[:4])
        else : bkgname = bkgname[0]
        bkg_hist = inFile.Get(channelName + '/' + bkgname)
        for ibin in range(1, tmpHist.GetNbinsX() + 1):
            ibinContent = tmpHist.GetBinContent(ibin)
            bkg_bin_content = bkg_hist.GetBinContent(ibin)
            new_content = 0.001
            if 'Up'    in hist[-10:] : 
                new_content = new_content*1.05
                bkg_bin_content = bkg_bin_content*1.05
            elif 'Down'  in hist[-10:] : 
                new_content = new_content*0.95
                bkg_bin_content = bkg_bin_content*0.95
            if bkgname in bkg_mapping[channelName+"_"+year]:
                if ibin in bkg_mapping[channelName+"_"+year][bkgname]:
                    tmpHist.SetBinContent(ibin, new_content)
                    tmpHist.Write()
                else:
                    tmpHist.SetBinContent(ibin, bkg_bin_content)
                    tmpHist.Write()
            else:
                if ibinContent <= 0 :
                    tmpHist.SetBinContent(ibin, bkg_bin_content)
                    #print hist , ibin , ' bin content set to 0.001'
                    tmpHist.Write()

def fix_binning_v2(inFile, channelName, year):
    keyList = inFile.GetKeyNames(channelName)
    inFile.cd(channelName)


    ZTTjet = inFile.Get(channelName + '/' + 'ZTTjet')
    ZTTjet_up = inFile.Get(channelName + '/' + 'ZTTjet_CMS_htt_boson_scale_met_Jet_2017Up')
    ZTTjet_dn = inFile.Get(channelName + '/' + 'ZTTjet_CMS_htt_boson_scale_met_Jet_2017Down')
    ibin = 1
    ibinContent = ZTTjet.GetBinContent(ibin)
    
    ZTTjet_up.SetBinContent(ibin, ibinContent * 1.05)
    ZTTjet_dn.SetBinContent(ibin, ibinContent * 0.95)
    ZTTjet_up.Write()
    ZTTjet_dn.Write()
 

def fix_BinRange(inFile, channelName):
    keyList = inFile.GetKeyNames(channelName)
    inFile.cd(channelName)
    for hist in keyList:
        #print hist
        tmpHist = inFile.Get(channelName + '/' + hist)
        #print hist , ' integral = ', tmpHist.Integral()
        if  tmpHist.GetNbinsX() > 16 :
            print "hist = ", hist
            print "nbins = ", tmpHist.GetNbinsX()
            print "  "
            ZTT_hist = ROOT.TH1F( hist, hist, 16, 40, 200 )
            for i in range(1, 21):
                if i<5: continue
                ZTT_hist.SetBinContent( i-4, tmpHist.GetBinContent(i) )
            tmpHist = ZTT_hist.Clone()
            tmpHist.Write()
        

def main():
    channels = ['etau', 'mutau', 'tautau']
    years = ['2017' , '2018']
    
    inputFile =  ROOT.TFile('bin/aux/2017/mutau_tmass200.root',"UPDATE")            
    fix_binning_v2(inputFile, 'mutau', '2017')
    inputFile.Close()
                

if __name__=="__main__":
    main()
