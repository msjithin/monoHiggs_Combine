signal_array=("ZprimeBaryonic_mzp1000_mchi100" "ZprimeBaryonic_mzp1000_mchi1" "ZprimeBaryonic_mzp1000_mchi200" "ZprimeBaryonic_mzp1000_mchi400" "ZprimeBaryonic_mzp1000_mchi600" "ZprimeBaryonic_mzp1000_mchi800" "ZprimeBaryonic_mzp100_mchi1" "ZprimeBaryonic_mzp100_mchi50" "ZprimeBaryonic_mzp1500_mchi100" "ZprimeBaryonic_mzp1500_mchi1" "ZprimeBaryonic_mzp1500_mchi200" "ZprimeBaryonic_mzp1500_mchi400" "ZprimeBaryonic_mzp1500_mchi600" "ZprimeBaryonic_mzp1500_mchi800" "ZprimeBaryonic_mzp2000_mchi100" "ZprimeBaryonic_mzp2000_mchi1" "ZprimeBaryonic_mzp2000_mchi200" "ZprimeBaryonic_mzp2000_mchi400" "ZprimeBaryonic_mzp2000_mchi600" "ZprimeBaryonic_mzp2000_mchi800" "ZprimeBaryonic_mzp200_mchi100" "ZprimeBaryonic_mzp200_mchi150" "ZprimeBaryonic_mzp200_mchi1" "ZprimeBaryonic_mzp200_mchi50" "ZprimeBaryonic_mzp2500_mchi100" "ZprimeBaryonic_mzp2500_mchi1" "ZprimeBaryonic_mzp2500_mchi200" "ZprimeBaryonic_mzp2500_mchi400" "ZprimeBaryonic_mzp2500_mchi600" "ZprimeBaryonic_mzp2500_mchi800" "ZprimeBaryonic_mzp3000_mchi100" "ZprimeBaryonic_mzp3000_mchi1" "ZprimeBaryonic_mzp3000_mchi200" "ZprimeBaryonic_mzp300_mchi150" "ZprimeBaryonic_mzp3500_mchi100" "ZprimeBaryonic_mzp3500_mchi1" "ZprimeBaryonic_mzp350_mchi50" "ZprimeBaryonic_mzp500_mchi100" "ZprimeBaryonic_mzp500_mchi1" "ZprimeBaryonic_mzp500_mchi200" "ZprimeBaryonic_mzp500_mchi400" "ZprimeBaryonic_mzp650_mchi50" "ZprimeBaryonic_mzp800_mchi50")

get_combineCards(){
        
    for i in "${signal_array[@]}"
    do
	echo $i
	sh add_auto_MC_Stat.sh $i
	cd $i
	combineCards.py xtt_et_1_13TeV_2017.txt xtt_mt_1_13TeV_2017.txt xtt_tt_1_13TeV_2017.txt > xtt_cmb_1_13TeV_2017.txt
	combineCards.py xtt_et_1_13TeV_2018.txt xtt_mt_1_13TeV_2018.txt xtt_tt_1_13TeV_2018.txt > xtt_cmb_1_13TeV_2018.txt
	combineCards.py xtt_cmb_1_13TeV_2017.txt xtt_cmb_1_13TeV_2018.txt >  xtt_cmb_1_13TeV_201718.txt
	cd ..
    done   
}


get_combineCards
