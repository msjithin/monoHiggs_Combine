# get one json file from list
import json
import os 
import glob
import pandas as pd
import make_2dplot as plot2d
import argparse


mA_ticks = [200.0, 300.0, 400.0, 500.0, 600.0, 700.0, 800.0, 900.0]
ma_ticks = [100.0, 150.0, 200.0, 250.0, 300.0, 350.0, 400.0, 500.0]

def get_json(channel, year):
    files = glob.glob('limits/limits_'+year+'_'+channel+'*')
    #inFile = 'limits/limits_etau_MH3_200_MH4_150.json'
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
        print 'infile name == ', inFile
        #print inFile.split('_')
        mA = float(inFile.split('_')[-2])
        ma = float(inFile.split('_')[-1])
        values = data['120.0']
        values['mA'] = mA
        values['ma'] = ma
        out[ str(mA)+'_'+str(ma) ] = values
        data_json = json.dumps(out)
        
        with open('sample_'+year+'_'+channel+'.json', 'w+') as json_file:
            json.dump(out, json_file, indent=4, sort_keys=True)

def get_limits(channel, year):
    mA = []
    ma = []
    obs = []
    expected = []
    exp_p1 = []
    exp_m1 = []
    if not os.path.isfile('sample_'+year+'_'+channel+'.json'):
        return 
    with open('sample_'+year+'_'+channel+'.json') as f:
        data = json.load(f)
        for key, values in data.items():
            mA.append(values['mA'])
            ma.append(values['ma'])
            obs.append(values['obs'])
            expected.append(values['exp0'])
            exp_p1.append(values['exp+1'])
            exp_m1.append(values['exp-1'])
            

    #tmp_dict = {'mA':mA , 'ma':ma, 'obs':obs, 'expected':expected, 'exp_p1':exp_p1 , 'exp_m1':exp_m1}
    tmp_dict = {'mA':mA , 'ma':ma, 'expected':expected, 'exp_p1':exp_p1 , 'exp_m1':exp_m1}
    df = pd.DataFrame(tmp_dict)
    df = df.sort_values(['mA'])
    print df
    

def get_arrays(channel, year):
    if not os.path.isfile('sample_'+year+'_'+channel+'.json'):
        return
    arr_exp0 = [] 
    arr_exp_p1 = []
    arr_exp_m1 = []
    arr_obs = []
    with open('sample_'+year+'_'+channel+'.json') as f:
        data = json.load(f)
        #for key, values in data.items():
        for mA in mA_ticks: 
            tmp_exp0 = []
            tmp_exp_p1 = []
            tmp_exp_m1 = []
            tmp_obs = []
            for ma in ma_ticks:
                masspoint = str(mA)+'_'+str(ma)
                values = data.get(masspoint)
                if values is not None:
                    tmp_exp0.append(values['exp0'])
                    tmp_exp_p1.append(values['exp+1'])
                    tmp_exp_m1.append(values['exp-1'])
                    tmp_obs.append(values['obs'])
                else:
                    tmp_obs.append(0)
                    tmp_exp0.append(0)
                    tmp_exp_p1.append(0)
                    tmp_exp_m1.append(0)
            arr_exp0.append(tmp_exp0)
            arr_exp_p1.append(tmp_exp_p1)
            arr_exp_m1.append(tmp_exp_m1)
            arr_obs.append(tmp_obs)

    return arr_obs, arr_exp0 , arr_exp_p1, arr_exp_m1

def make_2dplot(channel, year):
    obs , expected, std_p1, std_m1 = get_arrays(channel, year)
    # for d in obs:
    #     print ( d )
    plot2d.make_plot(channel, year, obs , expected, std_p1, std_m1 )
        
if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-ch","--channel",
                    help="name of channel 'etau', 'mutau', 'tautau' or 'cmb'. Default=ALL")
    parser.add_argument("-y","--year",
                    help="year, options '2017', '2018', 'cmb'")

    print 'python gather_limits.py -ch etau,mutau,tautau,cmb'
    args =  parser.parse_args()
    channels = []
    if args.channel is None or args.year is None:
        print "python gather_limits.py -ch etau,mutau,tautau,cmb -y 2017,2018,cmb"
        exit()
    else:
        channels.append(args.channel)
    if args.year is None:
        year = '2017'
    else:
        year = args.year
        
    for ch in channels:
        print '*'*20
        print 'for channel :', ch
        get_json(ch, year)
        get_limits(ch, year) # prints dataframe for verifying
        make_2dplot(ch , year)
        
