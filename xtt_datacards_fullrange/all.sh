#!bin/bash

set -e

signal_array=("2hdma_med200_ps100" "2hdma_med200_ps150" "2hdma_med300_ps100" "2hdma_med300_ps150" "2hdma_med400_ps100" "2hdma_med400_ps150" "2hdma_med400_ps200" "2hdma_med400_ps250" "2hdma_med500_ps150" "2hdma_med500_ps200" "2hdma_med500_ps250" "2hdma_med500_ps300" "2hdma_med600_ps100" "2hdma_med600_ps150" "2hdma_med600_ps200" "2hdma_med600_ps250" "2hdma_med600_ps300" "2hdma_med600_ps350" "2hdma_med600_ps400" "2hdma_med600_ps500" "2hdma_med700_ps250" "2hdma_med700_ps300" "2hdma_med700_ps350" "2hdma_med700_ps400" "2hdma_med800_ps250" "2hdma_med800_ps300" "2hdma_med800_ps350" "2hdma_med800_ps500" "2hdma_med900_ps300" "2hdma_med900_ps350" "2hdma_med900_ps400" "2hdma_med900_ps500")

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



if [ -z "$output_dir" ]
then
      echo "\$output_dir is empty"
      echo "do 'source set_final_dir.sh'"
      exit 1
else
      echo "\$output_dir is NOT empty"
      echo $output_dir
fi

get_combineCards

# bash run_all.sh  &> impact_text_out

# bash get_pull_plots.sh all  &> diffnuisanceout


# bash get_limits.sh cmb
