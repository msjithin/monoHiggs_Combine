# get one json file from list
import json
import os 
import glob
import pandas as pd
import make_2dplot as plot2d
import argparse

mA_ticks = [200.0, 300.0, 400.0, 500.0, 600.0, 700.0, 800.0, 900.0]
ma_ticks = [100.0, 150.0, 200.0, 250.0, 300.0, 350.0, 400.0, 500.0]

def get_json(mchi = '1'):
    mchi = str(mchi)
    files = glob.glob('limits/limits_cmb_2hdma*_ps'+mchi+'.json')
    #inFile = 'limits/limits_cmb_2hdma_med700_ps250.json'
    out = {}
    nPoint = 0
    if not files :
        return
    for inFile in files:
        print inFile
        with open(inFile) as f:
            data = json.load(f)
        
        inFile = inFile.replace('.json', '')
        inFile = inFile.replace('med', '')
        inFile = inFile.replace('ps', '')
        #print 'infile name == ', inFile
        #print inFile.split('_')
        mA = float(inFile.split('_')[-2])
        ma = float(inFile.split('_')[-1])
        values = data['120.0']
        values['mA'] = mA
        values['ma'] = ma
        #values = values.pop('obs')
        values['obs'] = 0.0
        print values
        out[ str(mA) ] = values
        data_json = json.dumps(out)
        
        with open('ma'+mchi+'.json', 'w+') as json_file:
            json.dump(out, json_file, indent=4, sort_keys=True)

        
if __name__=="__main__":
    # parser = argparse.ArgumentParser()
    # parser.add_argument("-ch","--channel",
    #                 help="name of channel 'etau', 'mutau', 'tautau' or 'cmb'. Default=ALL")
    # parser.add_argument("-y","--year",
    #                 help="year, options '2017', '2018', 'cmb'")

    # print 'python gather_limits.py -ch etau,mutau,tautau,cmb'
    # args =  parser.parse_args()
    # channels = []
    # if args.channel is None or args.year is None:
    #     print "python gather_limits.py -ch etau,mutau,tautau,cmb -y 2017,2018,cmb"
    #     exit()
    # else:
    #     channels.append(args.channel)
    # if args.year is None:
    #     year = '2018'
    # else:
    #     year = args.year
        
    # for ch in channels:
    #     print '*'*20
    #     print 'for channel :', ch
    #     get_json(ch, year)
    #     get_limits(ch, year) # prints dataframe for verifying
    #     make_2dplot(ch , year)
    for ma in ma_ticks:
        get_json(str(int(ma)))
