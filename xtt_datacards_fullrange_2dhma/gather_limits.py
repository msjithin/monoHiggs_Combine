# get one json file from list
import json
import os 
import glob
import pandas as pd
import make_2dplot as plot2d
import argparse


mA_ticks = [200.0, 300.0, 400.0, 500.0, 600.0, 700.0, 800.0, 900.0, 1000.0, 1200.0, 1600.0]
ma_ticks = [100.0, 150.0, 200.0, 250.0, 300.0, 350.0, 400.0, 500.0]

def get_json(channel, year, cat='gg'):
    _path =  ''
    if cat=='gg':
        _path = 'limits/limits_cmb_2HDMa_gg_*'
    elif cat=='bb':
        _path = 'limits/limits_cmb_2HDMa_bb_*'
    elif cat=='bbgg':
        _path = 'limits_bbgg/limits_cmb_2HDMa_bbgg_*'

    files = glob.glob(_path)
    #inFile = 'limits/limits_cmb_2HDMa_bbgg_sinp_0p1_tanb_1p0_mXd_10_MH3_600_MH4_200.json'
    out = {}
    nPoint = 0
    if not files :
        return
    for inFile in files:
        if 'sinp_0p35_tanb_1p0' not in inFile: continue
        print inFile
        with open(inFile) as f:
            data = json.load(f)
        
        inFile = inFile.split('/')[-1]
        inFile = inFile.replace('.json', '')
        inFile = inFile.split('_')
        mA = float(inFile[1 + inFile.index('MH3')])
        ma = float(inFile[1 + inFile.index('MH4')])
        values = data['120.0']
        values['mA'] = mA
        values['ma'] = ma
        values['proc']  = inFile[1 + inFile.index('2HDMa')]
        values['sinetheta']  = inFile[1 + inFile.index('sinp')].replace('p', '.')
        values['tanbeta']  = inFile[1 + inFile.index('tanb')].replace('p', '.')
        out[ str(mA)+'_'+str(ma) ] = values
        data_json = json.dumps(out)
        
        with open('sample_'+year+'_'+channel+'_'+cat+'.json', 'w+') as json_file:
            json.dump(out, json_file, indent=4, sort_keys=True)

        
if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-ch","--channel",
                    help="name of channel 'etau', 'mutau', 'tautau' or 'cmb'. Default=ALL")
    parser.add_argument("-y","--year",
                    help="year, options '2017', '2018', 'cmb'")

    print 'python gather_limits.py -ch etau,mutau,tautau,cmb'
    args =  parser.parse_args()
    channels = []
    
    get_json('cmb', 'cmb', 'gg')
    get_json('cmb', 'cmb', 'bb')
    #get_json('cmb', 'cmb', 'bbgg')
