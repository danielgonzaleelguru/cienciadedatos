"""
Lee de forma paralela  los datos en Disco y  genera el archivo con el promedio de temperatura sin informara  el progremo del avance.

"""


import rasterio as r
import geopandas as gpd
import os
import fiona as f 
import pandas as pd
from  rasterio.plot  import  show
from  rasterio.plot  import  show_hist
from  rasterio.mask  import  mask
from  shapely.geometry import box
from fiona.crs import from_epsg
import pycrs 
from multiprocessing import cpu_count
from time import time

print(cpu_count())

dir_list = "C:\\Users\\User\\Downloads\\TemperaturaZonaEstudio\\"


def generateDayOfYear(year):
    sr = pd.Series(pd.date_range(str(year)+'-01-01',periods = 365, freq = 'D')) 
    listDate=[]
    for index, value in sr.items():
        v = value.date().strftime("%Y.%m.%d")
        listDate.append(v)

    return listDate



def readRasterByURL(year):
    list=[]
    listYear = generateDayOfYear(year)
    for d in listYear:        
        url = "http://data.chc.ucsb.edu/products/CHIRTSdaily/v1.0/global_tifs_p05/Tmax/"+str(year)+"/Tmax."+d+".tif"
        print(url)
        sum=0
        raster = r.open(url)
        value1=raster.read(1)[1175,2115]
        #print(value1)            
        value2=raster.read(1)[1175,2116]
        #print(value2)
        sum=value1+value2
        #print("Suma:"+str(sum))
        #show((raster, 1), cmap='terrain')
        average=sum/2
        t=(d,value1,value2,average)
        print(t)
        list.append(t)  
        print("Promedio:"+str(average)) 
      
    dataFrame = pd.DataFrame(list,columns=["Fecha","1175-2115","1175-2116","Promedio"])
    dataFrame.to_csv("C:\\Users\\User\\Downloads\\TemperaturaZonaEstudio\\data_"+str(year)+".csv",index=False)



def FindDirectoryToRead():  
    listDirectory=[]       
    for root, dirs, files in os.walk(dir_list):
        for dir in dirs:
            listDirectory.append(dir)
    return listDirectory



def readRasterDirectory(year):
    path=dir_list+"\\"+year+"\\"
   
    sum=0
    for root, dirs, files in os.walk(path):
        
        for f in files:            
            print(f)        
            raster = r.open(path+f)
            value1=raster.read(1)[1175,2115]
            #print(value1)            
            value2=raster.read(1)[1175,2116]
            #print(value2)
            sum=value1+value2
            #print("Suma:"+str(sum))
            #show((raster, 1), cmap='terrain')
        average=sum/2
        print("Promedio:"+str(average))  

from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor


if __name__ == "__main__":
    executor =  ProcessPoolExecutor(max_workers=2)
    start_time = time()    

    a = executor.submit(readRasterByURL('1986')) 
    b = executor.submit(readRasterByURL('1987'))
 

    print(a)
    print(b)         
    elapsed_time = time() - start_time
    print("Elapsed time: %0.10f seconds." % elapsed_time)