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
import pandas as pd
        
def checkHistogram(f, histogram):
    isthere=  f.GetListOfKeys().Contains(histogram)
    #print(isthere)
    return isthere


def GetKeyNames( self, dir = "" ):
    self.cd(dir)
    return [key.GetName() for key in ROOT.gDirectory.GetListOfKeys()]
ROOT.TFile.GetKeyNames = GetKeyNames
signals = [
    'MH3_200_MH4_100',
    'MH3_200_MH4_150',
    'MH3_300_MH4_100',
    'MH3_300_MH4_150',
    'MH3_400_MH4_100',
    'MH3_400_MH4_150',
    'MH3_400_MH4_200',
    'MH3_400_MH4_250',
    'MH3_500_MH4_150',
    'MH3_500_MH4_200',
    'MH3_500_MH4_250',
    'MH3_500_MH4_300',
    'MH3_600_MH4_100',
    'MH3_600_MH4_150',
    'MH3_600_MH4_200',
    'MH3_600_MH4_250',
    'MH3_600_MH4_300',
    'MH3_600_MH4_350',
    'MH3_600_MH4_400',
    'MH3_600_MH4_500',
    'MH3_700_MH4_250',
    'MH3_700_MH4_300',
    'MH3_700_MH4_350',
    'MH3_700_MH4_400',
    'MH3_800_MH4_250',
    'MH3_800_MH4_300',
    'MH3_800_MH4_350',
    'MH3_800_MH4_500',
    'MH3_900_MH4_300',
    'MH3_900_MH4_350',
    'MH3_900_MH4_400',
    'MH3_900_MH4_500'] 


fractions = { 'etau':{} , 'mutau':{} , 'tautau': {} }
def get_siginal_fraction(channel, signal=None):
    fname = 'bin/aux/2017/'+channel+'.root'
    inFile = ROOT.TFile(fname,"r")
    if signal is None:
        signal = 'MH3_200_MH4_100'
    signal_hist = inFile.Get(channel+'/'+signal)
    total_integral = signal_hist.Integral()
    lower_integral = 0
    for ibin in range(signal_hist.GetNbinsX()):
        if signal_hist.GetBinCenter(ibin) > 200: continue
        lower_integral +=  signal_hist.GetBinContent(ibin)
        #print "for ibin={} , value = {} , content ={}".format(ibin, signal_hist.GetBinCenter(ibin) , signal_hist.GetBinContent(ibin))
    print "For signal "+signal + " in channel "+channel
    print "total = {} , till 200 = {} , fraction = {} \n\n".format(total_integral, lower_integral, lower_integral/total_integral)
    fractions[channel][signal] = lower_integral/total_integral
    


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-ch","--channel",
                    help="name of channel 'etau', 'mutau', or 'tautau'. Default=etau")
    print 'python get_contents.py -ch etau,mutau,tautau'
    args =  parser.parse_args()
    if args.channel is None:
        channel = 'etau'
    else:
        channel = args.channel
    print 'channel = ', channel
    channels = ['etau', 'mutau', 'tautau']
    for ch in channels:
        for signal in signals:
            get_siginal_fraction(ch, signal)
    
    print fractions
