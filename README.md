## Combine limit extraction and impacts for monoHiggs

scram project CMSSW CMSSW_10_2_13
cd CMSSW_10_2_13/src
cmsenv
git clone https://github.com/cms-analysis/HiggsAnalysis-CombinedLimit.git HiggsAnalysis/CombinedLimit
# IMPORTANT: Checkout the recommended tag on the link above
git clone https://github.com/cms-analysis/CombineHarvester.git CombineHarvester
scram b


Datacards are created by .cpp files in bin/

For Zprime baryonic
`bash run_zpb_full.sh `

For 2HDMa do 
`bash run_new2hdma.sh`




