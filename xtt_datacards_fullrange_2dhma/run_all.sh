set -e

# ________________ etau ____________
bash get_impacts_2017_signal_0.sh -e 
#bash get_impacts_2017_signal_1.sh -e 

bash get_impacts_2018_signal_0.sh -e 
#bash get_impacts_2018_signal_1.sh -e 


# # _______________ mutau ____________
bash get_impacts_2017_signal_0.sh -m
#bash get_impacts_2017_signal_1.sh -m 

bash get_impacts_2018_signal_0.sh -m
#bash get_impacts_2018_signal_1.sh -m 


# # ______________ tautau ____________
bash get_impacts_2017_signal_0.sh -t
# #bash get_impacts_2017_signal_1.sh -t 

bash get_impacts_2018_signal_0.sh -t
# #bash get_impacts_2018_signal_1.sh -t 


# # ____________ combined ____________
bash get_impacts_2017_signal_0.sh -c
# bash get_impacts_2017_signal_1.sh -c

bash get_impacts_2018_signal_0.sh -c
# bash get_impacts_2018_signal_1.sh -c

bash get_impacts_combined.sh  -c
