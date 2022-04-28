

if [ -z "$output_dir" ]
then
      echo "\$output_dir is empty"
      exit 1
else
      echo "\$output_dir is NOT empty"
      echo $output_dir
fi

bash run_fit_v2.sh -y 2017 -e 
bash run_fit_v2.sh -y 2017 -m 
bash run_fit_v2.sh -y 2017 -t
 
bash run_fit_v2.sh -y 2018 -e 
bash run_fit_v2.sh -y 2018 -m
bash run_fit_v2.sh -y 2018 -t 
 
bash run_cmb_v2.sh





# bash run_fit.sh -y 2017 -e 
# bash run_fit.sh -y 2017 -m 
# bash run_fit.sh -y 2017 -t
 
# bash run_fit.sh -y 2018 -e 
# bash run_fit.sh -y 2018 -m
# bash run_fit.sh -y 2018 -t 
 


# bash run_cmb.sh
