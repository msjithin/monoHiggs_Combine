#!bin/bash

set -e

# if [ -z "$output_dir" ]
# then
#       echo "\$output_dir is empty"
#       echo "do 'source set_final_dir.sh'"
#       exit 1
# else
#       echo "\$output_dir is NOT empty"
#       echo $output_dir
# fi


bash combine_channels.sh

# bash run_all.sh  &> impact_text_out

# bash get_pull_plots.sh all  &> diffnuisanceout


bash get_limits.sh 
