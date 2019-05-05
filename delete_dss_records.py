from hec.script import *
from hec.heclib.dss import *
from hec.heclib.util import *
from hec.io import *
import java
import os 
try : 
  try :
    dss_location=#INSERT DSS PATH
    myDss =HecDss.open(dss_location)
    records=myDss.getCatalogedPathnames()
    myDss.delete(records)
  except Exception, e :
    MessageBox.showError(' '.join(e.args), "Python Error")
  except java.lang.Exception, e :
    MessageBox.showError(e.getMessage(), "Error")
finally :
  myDss.close()
