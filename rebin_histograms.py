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
from array import array


def GetKeyNames( self, dir = "" ):
    self.cd(dir)
    return [key.GetName() for key in ROOT.gDirectory.GetListOfKeys()]
ROOT.TFile.GetKeyNames = GetKeyNames

bkg_mapping = { 'etau_2017' : {}, 'mutau_2017': {}, 'tautau_2017':{}, 'etau_2018' : {}, 'mutau_2018': {}, 'tautau_2018':{} }
    
def fix_binning_v2(inFile, channelName, year):
    #if channelName == 'mutau' and year == '2017' : return 
    
    keyList = inFile.GetKeyNames(channelName)
    inFile.cd(channelName)
    for hist in keyList:
        #if 'htt_boson' not in hist: continue
        #print hist
        tmpHist = inFile.Get(channelName + '/' + hist)
        #print(tmpHist.Integral() , 'nbis = ', tmpHist.GetNbinsX())
        #tmpHist = tmpHist.Rebin(2, hist)
        new_binning = array('d', [40, 60, 90, 120, 150, 180, 200])
        tmpHist = tmpHist.Rebin(6, hist, new_binning )
        #print(tmpHist.Integral() , 'nbis = ', tmpHist.GetNbinsX())
        #print()
        tmpHist.Write()


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
    
    for ch in channels:
        for yr in years:
            channelName = ch
            year = yr
            #if ch=='etau' and yr=='2017': 
            inputFile =  ROOT.TFile('bin/aux/'+year+'/'+channelName+'_tmass200.root',"UPDATE")            
            fix_binning_v2(inputFile, channelName, year)
            inputFile.Close()
                

if __name__=="__main__":
    main()
