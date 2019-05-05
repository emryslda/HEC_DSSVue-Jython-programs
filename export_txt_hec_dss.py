from hec.script import *
from hec.heclib.dss import *
from hec.heclib.util import *
from hec.io import *
import java
import os 
#THIS COMES FROM BASH SCRIPT - export rainfallmm=something - 
rainfallmm=os.environ["rainfall"]

Part_B='TRY'
try : 
  try :
    Part_A=''
    Part_C='FLOW'
    Part_D=''
    Part_E='5MIN'
    Part_F='RUN:RUN'+rainfallmm 
    pathname="/"+Part_A+"/"+Part_B+"/"+Part_C+"/"+Part_D+"/"+Part_E+"/"+Part_F+"/"
    print(pathname) 
    dss_location='/Run'+rainfallmm+'.dss'
    dir_path='/HEC/output/'+rainfallmm+'mm/'
    
    if os.path.isfile(dir_path)==True:
       print("Directory created:"+dir_path)
       os.mkdir('/HEC/output/'+rainfallmm+'mm/')
       
    else:
       print("Directory alreasy exists")
    
    out_txt_path=dir_path+Part_B+'_'+Part_C+'_'+Part_E+'_'+'out'+ rainfallmm +'mm.txt'
    myDss =HecDss.open(dss_location)
    flow=myDss.get(pathname,1)
    data=flow.values
    f=open(out_txt_path, 'w') 
    f.write("%s\n" % flow.numberValues)
    f.write("Q(cms)\n" )
    for line in data:
      f.write("%s\n" % line)
    f.close()
    if flow.numberValues == 0 :      
      MessageBox.showError("No Data", "Error")    
    else :      
      plot = Plot.newPlot("Timeseries Output")      
      plot.addData(flow)      
      plot.showPlot()    
  except Exception, e :
    MessageBox.showError(' '.join(e.args), "Python Error")
  except java.lang.Exception, e :
    MessageBox.showError(e.getMessage(), "Error")
finally :
  myDss.close()
