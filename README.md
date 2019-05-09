# HEC_DSS_import scripts
# This is a jython repository for manipulating \t-separated .txt files in HEC_DSSVue. 

-In order to run this script from Linux it is necessary to go inside the HEC-DSSVue folder and run:

./hec-dssvue.sh selected-script.py

if you want to run the program from anywhere in the system create a simbolic link with ln -sf command to /usr/local/bin folder


# import_txt_hec_dss.py

-import_txt_hec_dss.py will import DATETIME and RAIN in .DSS file.
modified from the samples and useful to read a list of .txt files with the following format:

01/04/2001	00:00	   0	   0  
respectivetily:

Date(D,M,Y) Hour CUMRAIN RAIN 

# export_txt_hec_dss.py
output format:

N° of total point

Q(cms)

1 column data

# delete_all_records.py

It delete all record inside a specific .dss file
