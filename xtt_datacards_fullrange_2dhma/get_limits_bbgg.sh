#!bin/bash
#example commands to run impact plots, any signal directory is ok. 
set -e
# combineCards.py card_1.txt card_2.txt card_3.txt > card_combined.txt


signal_array=("2HDMa_bbgg_sinp_0p35_tanb_1p0_mXd_10_MH3_500_MH4_300" "2HDMa_bbgg_sinp_0p35_tanb_1p0_mXd_10_MH3_700_MH4_400" "2HDMa_bbgg_sinp_0p35_tanb_1p0_mXd_10_MH3_900_MH4_500" "2HDMa_bbgg_sinp_0p1_tanb_1p0_mXd_10_MH3_600_MH4_200" "2HDMa_bbgg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_150" "2HDMa_bbgg_sinp_0p35_tanb_0p5_mXd_10_MH3_600_MH4_250" "2HDMa_bbgg_sinp_0p35_tanb_1p0_mXd_10_MH3_300_MH4_150" "2HDMa_bbgg_sinp_0p35_tanb_1p0_mXd_10_MH3_500_MH4_250" "2HDMa_bbgg_sinp_0p3_tanb_1p0_mXd_10_MH3_600_MH4_200" "2HDMa_bbgg_sinp_0p35_tanb_1p0_mXd_10_MH3_600_MH4_100" "2HDMa_bbgg_sinp_0p35_tanb_1p0_mXd_10_MH3_800_MH4_250" "2HDMa_bbgg_sinp_0p35_tanb_1p0_mXd_10_MH3_600_MH4_300" "2HDMa_bbgg_sinp_0p4_tanb_1p0_mXd_10_MH3_600_MH4_200" "2HDMa_bbgg_sinp_0p35_tanb_1p0_mXd_10_MH3_700_MH4_350" "2HDMa_bbgg_sinp_0p35_tanb_1p0_mXd_10_MH3_1200_MH4_350" "2HDMa_bbgg_sinp_0p8_tanb_1p0_mXd_10_MH3_600_MH4_200" "2HDMa_bbgg_sinp_0p35_tanb_1p0_mXd_10_MH3_400_MH4_150" "2HDMa_bbgg_sinp_0p35_tanb_1p0_mXd_10_MH3_1200_MH4_250" "2HDMa_bbgg_sinp_0p35_tanb_8p0_mXd_10_MH3_600_MH4_250" "2HDMa_bbgg_sinp_0p35_tanb_2p0_mXd_10_MH3_600_MH4_250" "2HDMa_bbgg_sinp_0p35_tanb_1p0_mXd_10_MH3_1600_MH4_250" "2HDMa_bbgg_sinp_0p35_tanb_1p0_mXd_10_MH3_400_MH4_200" "2HDMa_bbgg_sinp_0p35_tanb_1p0_mXd_10_MH3_600_MH4_250" "2HDMa_bbgg_sinp_0p35_tanb_4p0_mXd_10_MH3_600_MH4_250" "2HDMa_bbgg_sinp_0p35_tanb_20p0_mXd_10_MH3_600_MH4_250" "2HDMa_bbgg_sinp_0p35_tanb_1p0_mXd_10_MH3_1000_MH4_150" "2HDMa_bbgg_sinp_0p35_tanb_1p0_mXd_10_MH3_1600_MH4_150" "2HDMa_bbgg_sinp_0p35_tanb_1p0_mXd_10_MH3_1600_MH4_350" "2HDMa_bbgg_sinp_0p35_tanb_0p5_mXd_10_MH3_600_MH4_150" "2HDMa_bbgg_sinp_0p35_tanb_20p0_mXd_10_MH3_600_MH4_150" "2HDMa_bbgg_sinp_0p35_tanb_2p0_mXd_10_MH3_600_MH4_150" "2HDMa_bbgg_sinp_0p35_tanb_1p0_mXd_10_MH3_1200_MH4_150" "2HDMa_bbgg_sinp_0p35_tanb_1p5_mXd_10_MH3_600_MH4_250" "2HDMa_bbgg_sinp_0p35_tanb_1p0_mXd_10_MH3_600_MH4_400" "2HDMa_bbgg_sinp_0p35_tanb_4p0_mXd_10_MH3_600_MH4_150" "2HDMa_bbgg_sinp_0p35_tanb_1p0_mXd_10_MH3_700_MH4_250" "2HDMa_bbgg_sinp_0p9_tanb_1p0_mXd_10_MH3_600_MH4_200" "2HDMa_bbgg_sinp_0p35_tanb_1p0_mXd_10_MH3_400_MH4_100" "2HDMa_bbgg_sinp_0p2_tanb_1p0_mXd_10_MH3_600_MH4_200" "2HDMa_bbgg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100" "2HDMa_bbgg_sinp_0p35_tanb_1p0_mXd_10_MH3_1000_MH4_350" "2HDMa_bbgg_sinp_0p6_tanb_1p0_mXd_10_MH3_600_MH4_200" "2HDMa_bbgg_sinp_0p35_tanb_50p0_mXd_10_MH3_600_MH4_150" "2HDMa_bbgg_sinp_0p35_tanb_1p0_mXd_10_MH3_600_MH4_150" "2HDMa_bbgg_sinp_0p35_tanb_1p0_mXd_10_MH3_900_MH4_300" "2HDMa_bbgg_sinp_0p35_tanb_1p0_mXd_10_MH3_1000_MH4_250" "2HDMa_bbgg_sinp_0p35_tanb_1p0_mXd_10_MH3_900_MH4_350" "2HDMa_bbgg_sinp_0p35_tanb_1p0_mXd_10_MH3_600_MH4_500" "2HDMa_bbgg_sinp_0p35_tanb_1p0_mXd_10_MH3_600_MH4_350" "2HDMa_bbgg_sinp_0p35_tanb_1p0_mXd_10_MH3_800_MH4_300" "2HDMa_bbgg_sinp_0p35_tanb_1p0_mXd_10_MH3_300_MH4_100" "2HDMa_bbgg_sinp_0p35_tanb_1p0_mXd_10_MH3_400_MH4_250" "2HDMa_bbgg_sinp_0p35_tanb_1p0_mXd_10_MH3_800_MH4_350" "2HDMa_bbgg_sinp_0p7_tanb_1p0_mXd_10_MH3_600_MH4_200" "2HDMa_bbgg_sinp_0p35_tanb_1p0_mXd_10_MH3_500_MH4_150" "2HDMa_bbgg_sinp_0p35_tanb_50p0_mXd_10_MH3_600_MH4_250" "2HDMa_bbgg_sinp_0p35_tanb_1p0_mXd_10_MH3_800_MH4_500" "2HDMa_bbgg_sinp_0p35_tanb_1p0_mXd_10_MH3_600_MH4_200" "2HDMa_bbgg_sinp_0p5_tanb_1p0_mXd_10_MH3_600_MH4_200" "2HDMa_bbgg_sinp_0p35_tanb_1p0_mXd_10_MH3_500_MH4_200" "2HDMa_bbgg_sinp_0p35_tanb_1p0_mXd_10_MH3_900_MH4_400" "2HDMa_bbgg_sinp_0p35_tanb_1p5_mXd_10_MH3_600_MH4_150" "2HDMa_bbgg_sinp_0p35_tanb_8p0_mXd_10_MH3_600_MH4_150" "2HDMa_bbgg_sinp_0p35_tanb_1p0_mXd_10_MH3_700_MH4_300" "2HDMa_bbgg_sinp_0p35_tanb_1p0_mXd_10_MH3_800_MH4_150")


get_cmb(){
    for i in "${signal_array[@]}"
    do
	echo $i
	#get_combineCards
	combineTool.py -M T2W -i ${i}/xtt_cmb_1_13TeV_201718.txt -o cmb_workspace_201718.root
	combineTool.py -M AsymptoticLimits -t -1 -d ${i}/cmb_workspace_201718.root --there -n .limit_cmb --expectSignal=0  --parallel 10 --cminDefaultMinimizerStrategy 0 --rMin -20 --rMax 20 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH
    done   
}


cmb(){
    get_cmb
    combineTool.py -M CollectLimits 2HDMa_bbgg*/*.limit_cmb.* --use-dirs -o limits_bbgg/limits_cmb.json
    #python gather_limits.py -ch cmb -y 'cmb'
    #cp limit_cmb.png $output_dir/
}
# combineTool.py -M T2W -i 2HDMa_bbgg_sinp_0p1_tanb_1p0_mXd_10_MH3_600_MH4_200/xtt_cmb_1_13TeV_201718.txt -o cmb_workspace_201718.root
# combineTool.py -M AsymptoticLimits -t -1 -d 2HDMa_bbgg_sinp_0p1_tanb_1p0_mXd_10_MH3_600_MH4_200/cmb_workspace_201718.root --there -n .limit_cmb --expectSignal=0  --parallel 10 --cminDefaultMinimizerStrategy 0 --rMin -20 --rMax 20 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH

# #"$@"
cmb

# python gather_limits.py

# # make 1d scan plots
# python make_plot1d.py

# python get_mu.py  
# python make_plot2d.py

# python make_sinetheta_scan.py
# python make_tanbeta_scan.py

# # copy png files 
# cp *.png ~/public_html/zprimeB/xsec_1pb/no_drcut/with_iso_v2/
