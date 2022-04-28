


def fix_channel_names(year='2017'):
    #read input file
    fin = open("2hdma_med400_ps100/xtt_cmb_1_13TeV_"+year+".txt", "rt")
    #read file contents to string
    data = fin.read()
    #replace all occurrences of the required string
    if year=="20172018":
        data = data.replace('ch1_ch1', 'et_2018')
        data = data.replace('ch1_ch2', 'mt_2018')
        data = data.replace('ch1_ch3', 'tt_2018')
        data = data.replace('ch2_ch1', 'et_2017')
        data = data.replace('ch2_ch2', 'mt_2017')
        data = data.replace('ch2_ch3', 'tt_2017')
    else:
        data = data.replace('ch1', 'et_'+year)
        data = data.replace('ch2', 'mt_'+year)
        data = data.replace('ch3', 'tt_'+year)
    #close the input file
    fin.close()
    #open the input file in write mode
    fin = open("2hdma_med400_ps100/xtt_cmb_1_13TeV_"+year+".txt", "wt")
    #overrite the input file with the resulting data
    fin.write(data)
    #close the file
    fin.close()
    



if __name__=="__main__":
    fix_channel_names(year='2017')
    fix_channel_names(year='2018')
    fix_channel_names(year='20172018')
