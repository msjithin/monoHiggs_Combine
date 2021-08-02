

# combine 3 channels into one
rm datacard_monoHiggs_cmb_v2017.txt
combineCards.py datacard_monoHiggs_etau_v2017.txt datacard_monoHiggs_mutau_v2017.txt datacard_monoHiggs_tautau_v2017.txt > datacard_monoHiggs_cmb_v2017.txt
