import json
import os 
import glob
import pandas as pd

xsec_map  = {
    'MZp_200_MChi_1': 2.67, 
    'MZp_2500_MChi_600': 0.004033, 'MZp_1000_MChi_400': 0.09047, 'MZp_2000_MChi_800': 0.007706, 'MZp_300_MChi_150': 0.3163, 'MZp_2500_MChi_1': 0.004382, 'MZp_500_MChi_400': 0.0001253, 
    'MZp_500_MChi_100': 0.9952, 'MZp_3000_MChi_200': 0.001456, 
    'MZp_1500_MChi_600': 0.02549, 
    'MZp_1500_MChi_1': 0.0505, 
    'MZp_2000_MChi_100': 0.01422, 'MZp_2500_MChi_100': 0.004391, 'MZp_2500_MChi_800': 0.003516, 
    'MZp_1000_MChi_1': 0.2094, 'MZp_200_MChi_50': 2.184, 'MZp_3500_MChi_1': 0.0005255, 
    'MZp_1000_MChi_100': 0.2077, 'MZp_350_MChi_50': 1.858, 'MZp_2000_MChi_200': 0.01413, 
    'MZp_2500_MChi_400': 0.004283, 'MZp_1000_MChi_200': 0.1947, 'MZp_100_MChi_1': 3.322, 
    'MZp_500_MChi_1': 1.139, 'MZp_2000_MChi_1': 0.01425, 
    'MZp_1500_MChi_800': 0.0002038, 'MZp_200_MChi_150': 0.0033, 'MZp_100_MChi_50': 0.9046, 
    'MZp_3500_MChi_100': 0.0005227, 
    'MZp_2500_MChi_200': 0.00435, 
    'MZp_2000_MChi_600': 0.01176, 
    'MZp_1000_MChi_800': 5.138e-06, 'MZp_1500_MChi_200': 0.04976, 
    'MZp_650_MChi_50': 0.6549, 'MZp_500_MChi_200': 0.4235, 
    'MZp_2000_MChi_400': 0.01351, 'MZp_1500_MChi_100': 0.05066, 
    'MZp_1500_MChi_400': 0.04371, 'MZp_3000_MChi_100': 0.001463, 'MZp_3000_MChi_1': 0.001458, 
    'MZp_200_MChi_100': 0.5484, 'MZp_1000_MChi_600': 0.0001443, 'MZp_800_MChi_50': 0.3935,

    '2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100' : 3.628e-01 , 
    '2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_150' : 3.209e-01 , 
    '2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_300_MH4_100' : 2.892e+00 , 
    '2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_300_MH4_150' : 1.596e+00 , 
    '2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_400_MH4_100' : 1.352e+00 , 
    '2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_400_MH4_150' : 9.943e-01 , 
    '2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_400_MH4_200' : 5.997e-01 , 
    '2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_400_MH4_250' : 2.301e-01 , 
    '2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_500_MH4_150' : 5.070e-01 , 
    '2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_500_MH4_200' : 3.709e-01 , 
    '2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_500_MH4_250' : 2.375e-01 , 
    '2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_500_MH4_300' : 1.295e-01 , 
    '2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_600_MH4_100' : 3.778e-01 , 
    '2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_600_MH4_150' : 2.981e-01 , 
    '2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_600_MH4_200' : 2.313e-01 , 
    '2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_600_MH4_250' : 1.657e-01 , 
    '2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_600_MH4_300' : 1.160e-01 , 
    '2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_600_MH4_350' : 7.739e-02 , 
    '2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_600_MH4_400' : 4.035e-02 , 
    '2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_600_MH4_500' : 5.494e-03 , 
    '2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_700_MH4_250' : 1.084e-01 , 
    '2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_700_MH4_300' : 8.360e-02 , 
    '2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_700_MH4_350' : 6.513e-02 , 
    '2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_700_MH4_400' : 4.227e-02 , 
    '2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_800_MH4_250' : 7.091e-02 , 
    '2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_800_MH4_300' : 5.730e-02 , 
    '2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_800_MH4_350' : 4.830e-02 , 
    '2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_800_MH4_500' : 1.604e-02 , 
    '2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_900_MH4_300' : 3.757e-02 , 
    '2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_900_MH4_350' : 3.359e-02 , 
    '2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_900_MH4_400' : 2.559e-02 , 
    '2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_900_MH4_500' : 1.432e-02 ,

}
def get_limits(channel, year):
    mZp = []
    mChi = []
    obs = []
    expected = []
    exp_p1 = []
    exp_m1 = []
    exp_p2 = []
    exp_m2 = []
    name = []
    xsec = []
    savename = []
    if not os.path.isfile('sample_'+year+'_'+channel+'.json'):
        return 
    with open('sample_'+year+'_'+channel+'.json') as f:
        data = json.load(f)
        for key, values in data.items():
            #print key, values, len(values)
            mZp.append(values['mA'])
            mChi.append(values['ma'])
            #obs.append(values['obs'])
            obs.append(0)
            _name = 'MZp_'+str(int(values['mA']))+'_MChi_'+str(int(values['ma']))
            _savename = str(values['mA'])+'_'+str(values['ma'])
            savename.append(_savename)
            name.append(_name)
            xsec.append(xsec_map[_name])
            #print name
            if 'exp0' in values:
                expected.append(values['exp0'])
                exp_p1.append(values['exp+1'])
                exp_m1.append(values['exp-1'])
                exp_p2.append(values['exp+2'])
                exp_m2.append(values['exp-2'])
            else:
                expected.append(0)
                exp_p1.append(0)
                exp_m1.append(0)
                exp_p2.append(0)
                exp_m2.append(0)
                
    #tmp_dict = {'mA':mA , 'ma':ma, 'obs':obs, 'expected':expected, 'exp_p1':exp_p1 , 'exp_m1':exp_m1}
    tmp_dict = {'mZp':mZp , 'mChi':mChi, 'obs':obs, 'exp0':expected, 'exp+1':exp_p1 , 'exp-1':exp_m1, 'exp+2':exp_p2 , 'exp-2':exp_m2, 'name': name, 'xsec':xsec, 'savename':savename}
    df = pd.DataFrame(tmp_dict)
    df = df.sort_values(['mChi'])
    # df['exp+1'] = df['exp+1']/df['xsec']
    # df['exp-1'] = df['exp-1']/df['xsec']
    # df['exp+2'] = df['exp+2']/df['xsec']
    # df['exp-2'] = df['exp-2']/df['xsec']
    # df['exp0'] = df['exp0']/df['xsec']
    #df = df[df['mChi']==1]
    df = df.set_index('savename')
    print df
    result = df.to_json(r'new_json.json', orient="index")
    #result = df.to_dict('dict', orient="index")
    #print result
    # with open('new_json.json', 'w') as f:
    #     f.write(result)
    jstr = json.dumps(result, indent=4)
    #print jstr
    with open("my_json.json", "w") as file:
        json.dump(result, file, indent=4, sort_keys=True)



get_limits('cmb', 'cmb')


