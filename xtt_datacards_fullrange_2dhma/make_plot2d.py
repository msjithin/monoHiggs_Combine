# get one json file from list
import json
import os 
import glob
import pandas as pd
import make_2dplot as plot2d
import argparse


mA_ticks = [200, 300, 400, 500, 600, 700, 800, 900, 1000, 1200, 1600]
ma_ticks = [100, 150, 200, 250, 300, 350, 400, 500]

    
def get_arrays(channel, year,  cat=""):
    # if not os.path.isfile('sample_'+year+'_'+channel+'.json'):
    #     return
    arr_exp0 = [] 
    arr_exp_p1 = []
    arr_exp_m1 = []
    arr_obs = []
    with open('new_json_'+cat+'.json') as f:
        data = json.load(f)
        #for key, values in data.items():
        for mA in mA_ticks: 
            tmp_exp0 = []
            tmp_exp_p1 = []
            tmp_exp_m1 = []
            tmp_obs = []
            for ma in ma_ticks:
                masspoint = str(mA)+'.0_'+str(ma)+'.0'
                print masspoint
                values = data.get(masspoint)
                print values
                if values is not None:
                    print values
                    if 'exp0' in values:
                        tmp_exp0.append(values['exp0'])
                        tmp_exp_p1.append(values['exp+1'])
                        tmp_exp_m1.append(values['exp-1'])
                        tmp_obs.append(values['obs'])
                    else:
                        tmp_exp0.append(0)
                        tmp_exp_p1.append(0)
                        tmp_exp_m1.append(0)
                        tmp_obs.append(0)                    
                else:
                    tmp_obs.append(0)
                    tmp_exp0.append(0)
                    tmp_exp_p1.append(0)
                    tmp_exp_m1.append(0)
            arr_exp0.append(tmp_exp0)
            arr_exp_p1.append(tmp_exp_p1)
            arr_exp_m1.append(tmp_exp_m1)
            arr_obs.append(tmp_obs)
    #print arr_obs
    #print arr_exp0
    return arr_obs, arr_exp0 , arr_exp_p1, arr_exp_m1

def make_2dplot(channel, year, cat=''):
    obs , expected, std_p1, std_m1 = get_arrays(channel, year, cat)
    # for d in obs:
    #     print ( d )
    plot2d.make_plot(channel, year, obs , expected, std_p1, std_m1 , cat )
        
if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-ch","--channel",
                    help="name of channel 'etau', 'mutau', 'tautau' or 'cmb'. Default=ALL")
    parser.add_argument("-y","--year",
                    help="year, options '2017', '2018', 'cmb'")

    print 'python gather_limits.py -ch etau,mutau,tautau,cmb'
    args =  parser.parse_args()
    channels = []
    
    make_2dplot('cmb', '20172018', 'gg')
    make_2dplot('cmb', '20172018', 'bb')
    #make_2dplot('cmb', '20172018', 'bbgg')
    
