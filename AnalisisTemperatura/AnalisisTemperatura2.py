"""
Lee de forma paralela  los datos en Disco y  genera el archivo con el promedio de temperatura informado el progremo del análisis.

"""



import multiprocessing as m
import os 
import rasterio as r
import pandas as pd
from time import time
import tqdm 

print(m.cpu_count())

dir_list = "C:\\Users\\User\\Downloads\\TemperaturaZonaEstudio\\"



def FindDirectoryToRead():  
    listDirectory=[]       
    for root, dirs, files in os.walk(dir_list):
        for dir in dirs:
            listDirectory.append(dir)
    return listDirectory

def generateDayOfYear(year):
    sr = pd.Series(pd.date_range(str(year)+'-01-01',periods = 365, freq = 'D')) 
    listDate=[]
    for index, value in sr.items():
        v = value.date().strftime("%Y.%m.%d")
        listDate.append(v)

    return listDate

def readRasterByURL(year):
    start_time = time()  

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

    
    elapsed_time = time() - start_time
    print("Elapsed time : %0.10f seconds." % elapsed_time)



def readRasterDirectory(year):
    estimated_total = 750 
    progress_bar = tqdm.tqdm(total=estimated_total)
    path=dir_list+"\\"+year+"\\"    
    sum=0
    list=[]
    for root, dirs, files in os.walk(path):          
        for f in files:                      
            #print(f) 
            SplitList= f.split(".")           
            fecha=SplitList[1]+"/"+SplitList[2]+"/"+SplitList[3]
            raster = r.open(path+f)
            value1=raster.read(1)[1175,2115]            
            #print(value1)            
            value2=raster.read(1)[1175,2116]              
            #print(value2)
            sum=value1+value2
            #print("Suma:"+str(sum))
            #show((raster, 1), cmap='terrain')
            average=sum/2
            t=(fecha,value1,value2,average)
            print(t)
            list.append(t)  
            #progress_bar.update(1) 
             
    
    

    print("Año analizado:"+year)    
    dataFrame = pd.DataFrame(list,columns=["Fecha","1175-2115","1175-2116","Promedio"])
    dataFrame.to_csv("C:\\Users\\User\\Downloads\\TemperaturaZonaEstudio\\data_"+year+".csv",index=False)
    

if __name__ == "__main__":
    
    # creating processes
    p1 = m.Process(target=readRasterByURL, args=('2011', ))
    p2 = m.Process(target=readRasterByURL, args=('2012', ))
    p3 = m.Process(target=readRasterByURL, args=('2013', ))
    #p3 = m.Process(target=readRasterDirectory, args=('1985', ))
        # starting process 1
      
    p1.start()
    # starting process 2
    p2.start()

    p3.start()

    #p3.start()


   
    