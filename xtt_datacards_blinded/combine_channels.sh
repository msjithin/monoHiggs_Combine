
if [ -z "$*" ]; 
then 
    echo "No args"; 
    echo 'syntax : bash combine_channels.sh dir_name'
else
    cd $1
    echo 'directory $1'
    echo "combining 2017"
    combineCards.py xtt_et_1_13TeV_2017.txt xtt_mt_1_13TeV_2017.txt xtt_tt_1_13TeV_2017.txt > xtt_cmb_1_13TeV_2017.txt

    echo "combining 2018"
    combineCards.py xtt_et_1_13TeV_2018.txt xtt_mt_1_13TeV_2018.txt xtt_tt_1_13TeV_2018.txt > xtt_cmb_1_13TeV_2018.txt

    echo "combining 2017+2018"
    combineCards.py xtt_cmb_1_13TeV_2018.txt xtt_cmb_1_13TeV_2017.txt > xtt_cmb_1_13TeV_20172018.txt

fi
