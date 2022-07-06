#!bin/bash

set -e

# signal_array=("2hdma_med200_ps100" "2hdma_med200_ps150" "2hdma_med300_ps100" "2hdma_med300_ps150" "2hdma_med400_ps100" "2hdma_med400_ps150" "2hdma_med400_ps200" "2hdma_med400_ps250" "2hdma_med500_ps150" "2hdma_med500_ps200" "2hdma_med500_ps250" "2hdma_med500_ps300" "2hdma_med600_ps100" "2hdma_med600_ps150" "2hdma_med600_ps200" "2hdma_med600_ps250" "2hdma_med600_ps300" "2hdma_med600_ps350" "2hdma_med600_ps400" "2hdma_med600_ps500" "2hdma_med700_ps250" "2hdma_med700_ps300" "2hdma_med700_ps350" "2hdma_med700_ps400" "2hdma_med800_ps250" "2hdma_med800_ps300" "2hdma_med800_ps350" "2hdma_med800_ps500" "2hdma_med900_ps300" "2hdma_med900_ps350" "2hdma_med900_ps400" "2hdma_med900_ps500")




# if [ -z "$output_dir" ]
# then
#       echo "\$output_dir is empty"
#       echo "do "source set_final_dir.sh""
#       exit 1
# else
#       echo "\$output_dir is NOT empty"
#       echo $output_dir
# fi

bash combine_channels.sh

# bash run_all.sh  &> impact_text_out

# bash get_pull_plots.sh all  &> diffnuisanceout


bash get_limits.sh 
