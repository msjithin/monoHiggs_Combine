



set -e

# # ____________ combined ____________
# bash get_impacts_2017_signal_0.sh -c
bash get_impacts_2017_signal_1.sh -c

# bash get_impacts_2018_signal_0.sh -c
bash get_impacts_2018_signal_1.sh -c

bash get_impacts_combined.sh  -c

bash get_pull_plots.sh cmb
