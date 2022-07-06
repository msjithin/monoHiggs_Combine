#!bin/bash
#example commands to run impact plots, any signal directory is ok. 
set -e
# combineCards.py card_1.txt card_2.txt card_3.txt > card_combined.txt

signal_array=("2hdma_med200_ps100" "2hdma_med200_ps150" "2hdma_med300_ps100" "2hdma_med300_ps150" "2hdma_med400_ps100" "2hdma_med400_ps150" "2hdma_med400_ps200" "2hdma_med400_ps250" "2hdma_med500_ps150" "2hdma_med500_ps200" "2hdma_med500_ps250" "2hdma_med500_ps300" "2hdma_med600_ps100" "2hdma_med600_ps150" "2hdma_med600_ps200" "2hdma_med600_ps250" "2hdma_med600_ps300" "2hdma_med600_ps350" "2hdma_med600_ps400" "2hdma_med600_ps500" "2hdma_med700_ps250" "2hdma_med700_ps300" "2hdma_med700_ps350" "2hdma_med700_ps400" "2hdma_med800_ps250" "2hdma_med800_ps300" "2hdma_med800_ps350" "2hdma_med800_ps500" "2hdma_med900_ps300" "2hdma_med900_ps350" "2hdma_med900_ps400" "2hdma_med900_ps500")


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
    combineTool.py -M CollectLimits 2hdma*/*.limit_2018_cmb.* --use-dirs -o limits/limits_2018_cmb.json
    python gather_limits.py -ch cmb -y '2018'
    #cp limit_cmb.png $output_dir/
}

#"$@"
cmb

