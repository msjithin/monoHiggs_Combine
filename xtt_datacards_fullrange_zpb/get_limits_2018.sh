#!bin/bash
#example commands to run impact plots, any signal directory is ok. 
set -e
# combineCards.py card_1.txt card_2.txt card_3.txt > card_combined.txt

signal_array=("ZprimeBaryonic_mzp1000_mchi100" "ZprimeBaryonic_mzp1000_mchi1" "ZprimeBaryonic_mzp1000_mchi200" "ZprimeBaryonic_mzp1000_mchi400" "ZprimeBaryonic_mzp1000_mchi600" "ZprimeBaryonic_mzp1000_mchi800" "ZprimeBaryonic_mzp100_mchi1" "ZprimeBaryonic_mzp100_mchi50" "ZprimeBaryonic_mzp1500_mchi100" "ZprimeBaryonic_mzp1500_mchi1" "ZprimeBaryonic_mzp1500_mchi200" "ZprimeBaryonic_mzp1500_mchi400" "ZprimeBaryonic_mzp1500_mchi600" "ZprimeBaryonic_mzp1500_mchi800" "ZprimeBaryonic_mzp2000_mchi100" "ZprimeBaryonic_mzp2000_mchi1" "ZprimeBaryonic_mzp2000_mchi200" "ZprimeBaryonic_mzp2000_mchi400" "ZprimeBaryonic_mzp2000_mchi600" "ZprimeBaryonic_mzp2000_mchi800" "ZprimeBaryonic_mzp200_mchi100" "ZprimeBaryonic_mzp200_mchi150" "ZprimeBaryonic_mzp200_mchi1" "ZprimeBaryonic_mzp200_mchi50" "ZprimeBaryonic_mzp2500_mchi100" "ZprimeBaryonic_mzp2500_mchi1" "ZprimeBaryonic_mzp2500_mchi200" "ZprimeBaryonic_mzp2500_mchi400" "ZprimeBaryonic_mzp2500_mchi600" "ZprimeBaryonic_mzp2500_mchi800" "ZprimeBaryonic_mzp3000_mchi100" "ZprimeBaryonic_mzp3000_mchi1" "ZprimeBaryonic_mzp3000_mchi200" "ZprimeBaryonic_mzp300_mchi150" "ZprimeBaryonic_mzp3500_mchi100" "ZprimeBaryonic_mzp3500_mchi1" "ZprimeBaryonic_mzp350_mchi50" "ZprimeBaryonic_mzp500_mchi100" "ZprimeBaryonic_mzp500_mchi1" "ZprimeBaryonic_mzp500_mchi200" "ZprimeBaryonic_mzp500_mchi400" "ZprimeBaryonic_mzp650_mchi50" "ZprimeBaryonic_mzp800_mchi50")


get_cmb(){
    for i in "${signal_array[@]}"
    do
	echo $i
	#get_combineCards
	combineTool.py -M T2W -i ${i}/xtt_cmb_1_13TeV_2018.txt -o cmb_workspace_2018.root
	combineTool.py -M AsymptoticLimits -t -1 -d ${i}/cmb_workspace_2018.root --there -n .limit_2018_cmb --expectSignal=0  --parallel 10 --cminDefaultMinimizerStrategy 0 --rMin -20 --rMax 20 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH
    done   
}


cmb(){
    get_cmb
    combineTool.py -M CollectLimits ZprimeBaryonic*/*.limit_2018_cmb.* --use-dirs -o limits/limits_2018_cmb.json
    python gather_limits.py -ch cmb -y 2018
    #cp limit_cmb.png $output_dir/
}

#"$@"
cmb

