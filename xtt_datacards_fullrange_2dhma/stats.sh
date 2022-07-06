#!bin/bash

set -e

signal_array=("2hdma_med200_ps100" "2hdma_med200_ps150" "2hdma_med300_ps100" "2hdma_med300_ps150" "2hdma_med400_ps100" "2hdma_med400_ps150" "2hdma_med400_ps200" "2hdma_med400_ps250" "2hdma_med500_ps150" "2hdma_med500_ps200" "2hdma_med500_ps250" "2hdma_med500_ps300" "2hdma_med600_ps100" "2hdma_med600_ps150" "2hdma_med600_ps200" "2hdma_med600_ps250" "2hdma_med600_ps300" "2hdma_med600_ps350" "2hdma_med600_ps400" "2hdma_med600_ps500" "2hdma_med700_ps250" "2hdma_med700_ps300" "2hdma_med700_ps350" "2hdma_med700_ps400" "2hdma_med800_ps250" "2hdma_med800_ps300" "2hdma_med800_ps350" "2hdma_med800_ps500" "2hdma_med900_ps300" "2hdma_med900_ps350" "2hdma_med900_ps400" "2hdma_med900_ps500")

get_combineCards(){
        
    for i in "${signal_array[@]}"
    do
	echo $i
	sh add_auto_MC_Stat.sh $i
    done   
}


get_combineCards
