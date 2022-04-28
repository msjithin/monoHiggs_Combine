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
# from sys import path
# path.append("../../../MacrosAndScripts/")
# from myPlotStyle import *
ROOT.gStyle.SetFrameLineWidth(1)
ROOT.gStyle.SetLineWidth(2)
ROOT.gStyle.SetOptStat(0)
        
def checkHistogram(f, histogram):
    isthere=  f.GetListOfKeys().Contains(histogram)
    #print(isthere)
    return isthere


def GetKeyNames( self, dir = "" ):
    self.cd(dir)
    return [key.GetName() for key in ROOT.gDirectory.GetListOfKeys()]
ROOT.TFile.GetKeyNames = GetKeyNames

cleanup = ['Up', 'ZTTjet_', 'ZLLjet_', 'STT_', 'VVT_', 'TT_', 'jetFakes_', 'otherMC_', 'signal_']
mc_list = ['ZTTjet', 'ZLLjet', 'STT', 'VVT', 'TT', 'otherMC']
def getUncList(channel):
    fname = 'sample_v2_'+channel+'.root'
    inFile = ROOT.TFile(fname,"r")
    keyList = inFile.GetKeyNames()
    tmpList= []
    for tdir in keyList:
        print 'tdir  =  ', tdir
        subdir = 'MH3_200_MH4_100'
        
        keyList3 = inFile.GetKeyNames(tdir+'/'+subdir)
        for hist in keyList3:
            if "Up" not in hist: continue
            for c in cleanup:
                hist = hist.replace(c, "")
                #print 'hist  =  ', hist
            if hist not in tmpList:
                tmpList.append(hist)
    inFile.Close()
    return sorted(tmpList)


def getHistList(channel):
    fname = 'sample_v2_'+channel+'.root'
    inFile = ROOT.TFile(fname,"r")
    keyList = inFile.GetKeyNames()
    mc_list = cleanup[1:]
    tmp_dict = {}
    print mc_list
    for tdir in keyList:
        print 'tdir  =  ', tdir
        subdir = 'MH3_200_MH4_100'
        keyList3 = inFile.GetKeyNames(tdir+'/'+subdir)
        for mc in mc_list:
            for hist in keyList3:
                if "Up" not in hist: continue
                if mc not in hist: continue
                for c in cleanup:
                    hist = hist.replace(c, "")
                if mc not in tmp_dict:
                    tmp_dict[mc] = [hist]
                else:
                    tmp_dict[mc].append(hist)
    inFile.Close()
    for k in tmp_dict:
        print "*"*30
        print 'in Sample ', k, ' found :'
        for v in sorted(tmp_dict[k]):
            print v
    return 

def getIntegrals(channel, year):
    print channel, year
    fname = 'bin/aux/'+year+'/etau.root'
    inFile = ROOT.TFile(fname,"r")
    keyList = inFile.GetKeyNames(channel)
    
    for mc_sample in mc_list:
        nom_hist = inFile.Get(channel+'/'+ mc_sample)
        nominal_integral = nom_hist.Integral()
        for thist in keyList:
            if ('efaket' in thist and mc_sample in thist) :
                tmp_hist = inFile.Get(channel+'/'+thist)
                print thist , tmp_hist.Integral() , '              percent change = ', 100*abs(nominal_integral - tmp_hist.Integral())/nominal_integral
                
    inFile.Close()
    return 


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
    getIntegrals(channel, '2017')
    getIntegrals(channel, '2018')
     
        
    
