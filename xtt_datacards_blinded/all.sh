

if [ -z "$output_dir" ]
then
      echo "\$output_dir is empty"
      exit 1

else
      echo "\$output_dir is NOT empty"
      echo $output_dir
fi


#python fix_channel_names.py
bash run_all.sh &> impact_out


bash run_cmb.sh

bash get_pull_plots.sh all &> diffnuisanceout


