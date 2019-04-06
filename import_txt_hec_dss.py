#INSERT THIS CODE IN HEC_DSSVue Script Editor.
#Created on 06/04/2019
#I will try to take this code up to date.

from hec.script import *
from hec.heclib.dss import *
from hec.heclib.util import *
from hec.io import *
import java
import os 

try : 
  try :
    #IF IT DOES NOT EXIST IT CREATES IT
    myDss = HecDss.open(PATH_TO_DSS") 
    path=PATH_TO_TXTFILES
    list_files=os.listdir(path)
    for line in list_files: #LOOP OVER THE FILES
      file=path+'/'+line; #READ A FILE
      staz_name= ''.join([i for i in line if not i.isdigit()])
      #DELETE SOME ISSUES
      staz_name=staz_name.replace('.txt','')
      staz_name=staz_name.replace('_','')
      #CREATE TIMESERIES
      tsc = TimeSeriesContainer()
      #CHANGE THE 15MIN INTERVAL FOR YOUR NEEDS
      #SETUP PATHNAME
      tsc.fullName =  "/BASIN/"+staz_name+"/RAIN//15MIN/OBSERVATION/"
      station_file=open(file,'r')
      #JUMP THE HEADERS
      header1 = station_file.readline()
      header2 = station_file.readline() 
      header3 = station_file.readline()
      header4 = station_file.readline()
      data=[]
      ora=[]
      cum=[]
      rain=[]
      for line in station_file:
         columns=line.split()
         dates=columns[0][3:6]+columns[0][0:3]+columns[0][6:10]
         data.append(dates)
         ora.append(columns[1])
         cum.append(columns[2])
         precipitation=float(columns[3])
         rain.append(precipitation)    
      station_file.close()
      #SETUP THE INTERVAL                  
      tsc.interval = 15 
      times = []
      start = HecTime(data[0],ora[0])
      for value in rain :
        times.append(start.value())
        start.add(tsc.interval)
      tsc.times = times
      tsc.values = rain
      tsc.numberValues = len(rain)
      tsc.units = "mm"
      tsc.type = "PRECIPITATION"
      myDss.put(tsc)#HERE IT WILL UPDATE THE DSS FILE
    
  except Exception, e :
    MessageBox.showError(' '.join(e.args), "Python Error")
  except java.lang.Exception, e :
    MessageBox.showError(e.getMessage(), "Error")
finally :
  myDss.close()
