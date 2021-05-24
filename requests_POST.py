# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 16:59:43 2021

@author: SESWARAN
"""
import requests
import json
from tkinter import Tk,filedialog,simpledialog
import re
from math import sin,sqrt,cos,pow,radians
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

root = Tk()
root.withdraw()
#appId = simpledialog.askstring(title='Authentication - Part 1/2',prompt='Enter App ID: ')
#appCode = simpledialog.askstring(title='Authentication - Part 2/2',prompt='Enter App Code: ')
appId = '60TjcXPzwsQ7cnlbDoxO'
appCode = 'c7ybJGr7-N8Mp33Jw7x9BA'
gpxfile = filedialog.askopenfilename(title='Choose GPX/KML file')
#fname = gpxfile.split('/')[-1].split('.')[0]+'.json'
fname = gpxfile.split('.')[0]+'.json'

url = "https://fleet.cit.api.here.com/2/calculateroute.json?routeMatch=1"
params = {'mode':'car','app_id':appId,'app_code':appCode,'attributes':'ADAS_ATTRIB_FCn(*),SPEED_LIMITS_FCn(*),SPEED_LIMITS_COND_FCn(*),SPEED_LIMITS_VAR_FCn(*),TRAFFIC_SIGN_FCn(*),LINK_ATTRIBUTE_FCn(*),ROUNDABOUT_FCn(*)'}
#payload="<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?><gpx version=\"1.0\" creator=\"ITN Converter 1.94M (http://www.benichou-software.com)\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns=\"http://www.topografix.com/GPX/1/0\" xmlns:topografix=\"http://www.topografix.com/GPX/Private/TopoGrafix/0/2\" xsi:schemaLocation=\"http://www.topografix.com/GPX/1/0 http://www.topografix.com/GPX/1/0/gpx.xsd http://www.topografix.com/GPX/Private/TopoGrafix/0/2 http://www.topografix.com/GPX/Private/TopoGrafix/0/2/topografix.xsd\"><time>2021-01-15T15:16:50Z</time><bounds minlat=\"52.188410\" minlon=\"-1.476800\" maxlat=\"52.215410\" maxlon=\"-1.433650\"/><rte><name>HiL Smoke Test Route</name><rtept lat=\"52.193360\" lon=\"-1.476800\"/><rtept lat=\"52.193250\" lon=\"-1.476690\"/><rtept lat=\"52.193170\" lon=\"-1.476540\"/><rtept lat=\"52.192890\" lon=\"-1.476270\"/><rtept lat=\"52.192700\" lon=\"-1.476070\"/><rtept lat=\"52.192460\" lon=\"-1.475820\"/><rtept lat=\"52.192250\" lon=\"-1.475560\"/><rtept lat=\"52.191970\" lon=\"-1.475210\"/><rtept lat=\"52.191900\" lon=\"-1.475130\"/><rtept lat=\"52.191620\" lon=\"-1.474770\"/><rtept lat=\"52.191160\" lon=\"-1.474060\"/><rtept lat=\"52.191110\" lon=\"-1.473960\"/><rtept lat=\"52.190740\" lon=\"-1.473370\"/><rtept lat=\"52.190660\" lon=\"-1.473210\"/><rtept lat=\"52.190300\" lon=\"-1.472470\"/><rtept lat=\"52.190000\" lon=\"-1.471850\"/><rtept lat=\"52.189820\" lon=\"-1.471480\"/><rtept lat=\"52.189780\" lon=\"-1.471380\"/><rtept lat=\"52.189420\" lon=\"-1.470310\"/><rtept lat=\"52.189360\" lon=\"-1.470130\"/><rtept lat=\"52.189270\" lon=\"-1.469830\"/><rtept lat=\"52.189160\" lon=\"-1.469480\"/><rtept lat=\"52.189030\" lon=\"-1.469040\"/><rtept lat=\"52.188970\" lon=\"-1.468800\"/><rtept lat=\"52.188690\" lon=\"-1.467470\"/><rtept lat=\"52.188660\" lon=\"-1.467330\"/><rtept lat=\"52.188590\" lon=\"-1.466860\"/><rtept lat=\"52.188500\" lon=\"-1.466270\"/><rtept lat=\"52.188420\" lon=\"-1.465360\"/><rtept lat=\"52.188410\" lon=\"-1.464540\"/><rtept lat=\"52.188450\" lon=\"-1.464020\"/><rtept lat=\"52.188490\" lon=\"-1.463670\"/><rtept lat=\"52.188510\" lon=\"-1.463470\"/><rtept lat=\"52.188520\" lon=\"-1.463390\"/><rtept lat=\"52.188600\" lon=\"-1.462940\"/><rtept lat=\"52.188710\" lon=\"-1.462560\"/><rtept lat=\"52.188850\" lon=\"-1.462190\"/><rtept lat=\"52.188960\" lon=\"-1.461980\"/><rtept lat=\"52.189040\" lon=\"-1.461810\"/><rtept lat=\"52.189120\" lon=\"-1.461670\"/><rtept lat=\"52.189230\" lon=\"-1.461500\"/><rtept lat=\"52.189440\" lon=\"-1.461230\"/><rtept lat=\"52.189780\" lon=\"-1.460900\"/><rtept lat=\"52.189960\" lon=\"-1.460760\"/><rtept lat=\"52.190140\" lon=\"-1.460670\"/><rtept lat=\"52.190450\" lon=\"-1.460540\"/><rtept lat=\"52.191110\" lon=\"-1.460290\"/><rtept lat=\"52.191180\" lon=\"-1.460280\"/><rtept lat=\"52.191300\" lon=\"-1.460240\"/><rtept lat=\"52.191400\" lon=\"-1.460200\"/><rtept lat=\"52.191500\" lon=\"-1.460150\"/><rtept lat=\"52.191640\" lon=\"-1.460070\"/><rtept lat=\"52.191770\" lon=\"-1.460000\"/><rtept lat=\"52.191890\" lon=\"-1.459930\"/><rtept lat=\"52.192070\" lon=\"-1.459820\"/><rtept lat=\"52.192140\" lon=\"-1.459770\"/><rtept lat=\"52.192240\" lon=\"-1.459670\"/><rtept lat=\"52.192280\" lon=\"-1.459630\"/><rtept lat=\"52.192400\" lon=\"-1.459540\"/><rtept lat=\"52.192590\" lon=\"-1.459400\"/><rtept lat=\"52.192670\" lon=\"-1.459330\"/><rtept lat=\"52.192740\" lon=\"-1.459260\"/><rtept lat=\"52.192800\" lon=\"-1.459210\"/><rtept lat=\"52.192880\" lon=\"-1.459120\"/><rtept lat=\"52.192970\" lon=\"-1.459020\"/><rtept lat=\"52.193240\" lon=\"-1.458640\"/><rtept lat=\"52.193380\" lon=\"-1.458450\"/><rtept lat=\"52.193430\" lon=\"-1.458380\"/><rtept lat=\"52.193630\" lon=\"-1.458050\"/><rtept lat=\"52.193660\" lon=\"-1.458000\"/><rtept lat=\"52.193880\" lon=\"-1.457570\"/><rtept lat=\"52.193970\" lon=\"-1.457380\"/><rtept lat=\"52.194170\" lon=\"-1.456960\"/><rtept lat=\"52.194360\" lon=\"-1.456580\"/><rtept lat=\"52.194370\" lon=\"-1.456570\"/><rtept lat=\"52.194480\" lon=\"-1.456340\"/><rtept lat=\"52.194710\" lon=\"-1.455870\"/><rtept lat=\"52.194890\" lon=\"-1.455510\"/><rtept lat=\"52.195020\" lon=\"-1.455280\"/><rtept lat=\"52.195110\" lon=\"-1.455160\"/><rtept lat=\"52.195240\" lon=\"-1.455000\"/><rtept lat=\"52.195430\" lon=\"-1.454810\"/><rtept lat=\"52.195560\" lon=\"-1.454690\"/><rtept lat=\"52.195590\" lon=\"-1.454670\"/><rtept lat=\"52.195720\" lon=\"-1.454560\"/><rtept lat=\"52.195880\" lon=\"-1.454430\"/><rtept lat=\"52.195960\" lon=\"-1.454370\"/><rtept lat=\"52.196110\" lon=\"-1.454230\"/><rtept lat=\"52.196250\" lon=\"-1.454080\"/><rtept lat=\"52.196500\" lon=\"-1.453790\"/><rtept lat=\"52.196710\" lon=\"-1.453520\"/><rtept lat=\"52.196800\" lon=\"-1.453390\"/><rtept lat=\"52.196910\" lon=\"-1.453250\"/><rtept lat=\"52.197030\" lon=\"-1.453110\"/><rtept lat=\"52.197180\" lon=\"-1.452990\"/><rtept lat=\"52.197220\" lon=\"-1.452950\"/><rtept lat=\"52.197360\" lon=\"-1.452860\"/><rtept lat=\"52.197510\" lon=\"-1.452780\"/><rtept lat=\"52.197800\" lon=\"-1.452660\"/><rtept lat=\"52.198010\" lon=\"-1.452590\"/><rtept lat=\"52.198090\" lon=\"-1.452550\"/><rtept lat=\"52.198180\" lon=\"-1.452510\"/><rtept lat=\"52.198360\" lon=\"-1.452440\"/><rtept lat=\"52.198620\" lon=\"-1.452330\"/><rtept lat=\"52.198630\" lon=\"-1.452320\"/><rtept lat=\"52.199020\" lon=\"-1.452120\"/><rtept lat=\"52.199240\" lon=\"-1.451980\"/><rtept lat=\"52.199600\" lon=\"-1.451710\"/><rtept lat=\"52.199850\" lon=\"-1.451460\"/><rtept lat=\"52.199990\" lon=\"-1.451300\"/><rtept lat=\"52.200300\" lon=\"-1.450900\"/><rtept lat=\"52.200480\" lon=\"-1.450640\"/><rtept lat=\"52.200490\" lon=\"-1.450620\"/><rtept lat=\"52.200610\" lon=\"-1.450420\"/><rtept lat=\"52.200950\" lon=\"-1.449810\"/><rtept lat=\"52.201080\" lon=\"-1.449580\"/><rtept lat=\"52.201440\" lon=\"-1.448950\"/><rtept lat=\"52.201590\" lon=\"-1.448720\"/><rtept lat=\"52.201670\" lon=\"-1.448600\"/><rtept lat=\"52.201730\" lon=\"-1.448520\"/><rtept lat=\"52.201850\" lon=\"-1.448360\"/><rtept lat=\"52.201970\" lon=\"-1.448210\"/><rtept lat=\"52.202410\" lon=\"-1.447780\"/><rtept lat=\"52.202610\" lon=\"-1.447600\"/><rtept lat=\"52.202790\" lon=\"-1.447420\"/><rtept lat=\"52.202900\" lon=\"-1.447310\"/><rtept lat=\"52.203140\" lon=\"-1.447080\"/><rtept lat=\"52.203700\" lon=\"-1.446430\"/><rtept lat=\"52.204350\" lon=\"-1.445570\"/><rtept lat=\"52.204470\" lon=\"-1.445410\"/><rtept lat=\"52.204620\" lon=\"-1.445190\"/><rtept lat=\"52.204860\" lon=\"-1.444820\"/><rtept lat=\"52.205080\" lon=\"-1.444400\"/><rtept lat=\"52.205290\" lon=\"-1.443870\"/><rtept lat=\"52.205350\" lon=\"-1.443710\"/><rtept lat=\"52.205630\" lon=\"-1.442930\"/><rtept lat=\"52.205700\" lon=\"-1.442730\"/><rtept lat=\"52.205840\" lon=\"-1.442340\"/><rtept lat=\"52.205980\" lon=\"-1.442000\"/><rtept lat=\"52.206050\" lon=\"-1.441890\"/><rtept lat=\"52.206120\" lon=\"-1.441780\"/><rtept lat=\"52.206170\" lon=\"-1.441700\"/><rtept lat=\"52.206260\" lon=\"-1.441590\"/><rtept lat=\"52.206290\" lon=\"-1.441560\"/><rtept lat=\"52.206550\" lon=\"-1.441250\"/><rtept lat=\"52.206720\" lon=\"-1.441050\"/><rtept lat=\"52.206850\" lon=\"-1.440910\"/><rtept lat=\"52.207290\" lon=\"-1.440420\"/><rtept lat=\"52.207300\" lon=\"-1.440420\"/><rtept lat=\"52.207360\" lon=\"-1.440350\"/><rtept lat=\"52.207460\" lon=\"-1.440240\"/><rtept lat=\"52.207610\" lon=\"-1.440120\"/><rtept lat=\"52.207800\" lon=\"-1.439960\"/><rtept lat=\"52.208060\" lon=\"-1.439810\"/><rtept lat=\"52.208100\" lon=\"-1.439790\"/><rtept lat=\"52.208380\" lon=\"-1.439640\"/><rtept lat=\"52.208400\" lon=\"-1.439640\"/><rtept lat=\"52.208580\" lon=\"-1.439590\"/><rtept lat=\"52.208760\" lon=\"-1.439550\"/><rtept lat=\"52.208840\" lon=\"-1.439530\"/><rtept lat=\"52.208970\" lon=\"-1.439520\"/><rtept lat=\"52.209120\" lon=\"-1.439510\"/><rtept lat=\"52.209240\" lon=\"-1.439510\"/><rtept lat=\"52.209670\" lon=\"-1.439490\"/><rtept lat=\"52.209890\" lon=\"-1.439490\"/><rtept lat=\"52.210010\" lon=\"-1.439480\"/><rtept lat=\"52.210040\" lon=\"-1.439480\"/><rtept lat=\"52.210130\" lon=\"-1.439450\"/><rtept lat=\"52.210200\" lon=\"-1.439410\"/><rtept lat=\"52.210250\" lon=\"-1.439370\"/><rtept lat=\"52.210290\" lon=\"-1.439330\"/><rtept lat=\"52.210300\" lon=\"-1.439320\"/><rtept lat=\"52.210350\" lon=\"-1.439260\"/><rtept lat=\"52.210400\" lon=\"-1.439200\"/><rtept lat=\"52.210450\" lon=\"-1.439110\"/><rtept lat=\"52.210500\" lon=\"-1.438990\"/><rtept lat=\"52.210650\" lon=\"-1.438560\"/><rtept lat=\"52.210660\" lon=\"-1.438550\"/><rtept lat=\"52.210740\" lon=\"-1.438300\"/><rtept lat=\"52.210740\" lon=\"-1.438290\"/><rtept lat=\"52.210900\" lon=\"-1.437820\"/><rtept lat=\"52.210980\" lon=\"-1.437540\"/><rtept lat=\"52.211100\" lon=\"-1.437290\"/><rtept lat=\"52.211140\" lon=\"-1.437200\"/><rtept lat=\"52.211180\" lon=\"-1.437120\"/><rtept lat=\"52.211200\" lon=\"-1.437060\"/><rtept lat=\"52.211400\" lon=\"-1.436670\"/><rtept lat=\"52.211470\" lon=\"-1.436550\"/><rtept lat=\"52.211530\" lon=\"-1.436450\"/><rtept lat=\"52.211570\" lon=\"-1.436400\"/><rtept lat=\"52.211600\" lon=\"-1.436350\"/><rtept lat=\"52.211800\" lon=\"-1.436070\"/><rtept lat=\"52.211910\" lon=\"-1.435950\"/><rtept lat=\"52.212030\" lon=\"-1.435850\"/><rtept lat=\"52.212470\" lon=\"-1.435530\"/><rtept lat=\"52.212570\" lon=\"-1.435450\"/><rtept lat=\"52.212600\" lon=\"-1.435420\"/><rtept lat=\"52.212610\" lon=\"-1.435410\"/><rtept lat=\"52.212640\" lon=\"-1.435370\"/><rtept lat=\"52.212670\" lon=\"-1.435330\"/><rtept lat=\"52.212740\" lon=\"-1.435240\"/><rtept lat=\"52.212850\" lon=\"-1.435100\"/><rtept lat=\"52.213130\" lon=\"-1.434650\"/><rtept lat=\"52.213180\" lon=\"-1.434580\"/><rtept lat=\"52.213410\" lon=\"-1.434270\"/><rtept lat=\"52.213510\" lon=\"-1.434140\"/><rtept lat=\"52.213600\" lon=\"-1.434040\"/><rtept lat=\"52.213710\" lon=\"-1.433930\"/><rtept lat=\"52.213810\" lon=\"-1.433850\"/><rtept lat=\"52.213980\" lon=\"-1.433740\"/><rtept lat=\"52.214110\" lon=\"-1.433650\"/><rtept lat=\"52.214120\" lon=\"-1.433660\"/><rtept lat=\"52.214130\" lon=\"-1.433680\"/><rtept lat=\"52.214140\" lon=\"-1.433690\"/><rtept lat=\"52.214160\" lon=\"-1.433690\"/><rtept lat=\"52.214170\" lon=\"-1.433680\"/><rtept lat=\"52.214240\" lon=\"-1.433820\"/><rtept lat=\"52.214320\" lon=\"-1.433960\"/><rtept lat=\"52.214330\" lon=\"-1.433990\"/><rtept lat=\"52.214570\" lon=\"-1.434500\"/><rtept lat=\"52.214640\" lon=\"-1.434680\"/><rtept lat=\"52.214800\" lon=\"-1.435090\"/><rtept lat=\"52.215130\" lon=\"-1.435780\"/><rtept lat=\"52.215250\" lon=\"-1.435510\"/><rtept lat=\"52.215380\" lon=\"-1.435240\"/><rtept lat=\"52.215410\" lon=\"-1.435200\"/></rte></gpx>"
payload = open(gpxfile, 'r').read()
headers = {
  'Content-Type': 'text/plain'
}
response = requests.request("POST", url, params=params,headers=headers, data=payload)
print(response.status_code)

dataJson = json.loads(response.text)

with open(fname, 'w') as json_file:
    json.dump(dataJson, json_file)

del fname,headers,json_file,params,payload,response,root,url,appId,appCode   
#%%

AyProfile = {
       "SpeedAy":[0,16,64,96,200,360], #in kph
       "AyD" : [4,4,2.5,1.5,1.5,0],
       "AyC" : [2,2.3,1.7,1.2,1.25,0],
       "AyE" : [2,2,1.25,0.75,1,0]
       }
#%% Access data
link_list = dataJson['response']['route'][0]['leg'][0]['link']
linklen = len(link_list)
#%%
linkNo = []
linkFc =[]
linkIntersection = []
linkUrban=[]
linkHpx = []
linkHpy = []
linkCurvature = []
linkSpdFrom = []
linkSpdTo = []
linkSpdUnits = []
for links in range(linklen):#:
    adasAtt = link_list[links]['attributes']['ADAS_ATTRIB_FCN'][0]
    linkAtt = link_list[links]['attributes']['LINK_ATTRIBUTE_FCN'][0]
    linkNo.append(links+1)
    linkFc.append(linkAtt['FUNCTIONAL_CLASS'])
    linkIntersection.append(linkAtt['INTERSECTION_CATEGORY'])
    linkUrban.append(linkAtt['URBAN'])
    linkHpx.append(adasAtt['HPX'])
    linkHpy.append(adasAtt['HPY'])
    linkCurvature.append(adasAtt['CURVATURES'])
    try:
        spdlimAtt = link_list[links]['attributes']['SPEED_LIMITS_FCN'][0]
        linkSpdFrom.append(spdlimAtt['FROM_REF_SPEED_LIMIT'])
        linkSpdTo.append(spdlimAtt['TO_REF_SPEED_LIMIT'])
        linkSpdUnits.append(spdlimAtt['SPEED_LIMIT_UNIT'])
    except:
        print('SpdLimAttrib missing')
        
linkData = pd.DataFrame(list(zip(linkNo,linkFc,linkIntersection,linkUrban,linkHpx,linkHpy,linkCurvature,linkSpdFrom,linkSpdFrom,linkSpdTo)),columns=['linkNo','linkFc','linkIntersection','linkUrban','linkHpx','linkHpy','linkCurvature','linkSpdFromKph','linkSpdUnits','linkSpdToKph'])

#%%
linklon = []
linklat = []
linkRad = []
for links in range(linklen):#:
    linklon.append(linkHpx[links].strip('[').strip(']').split(','))
    linklat.append(linkHpy[links].strip('[').strip(']').split(','))
    linkRad.append(linkCurvature[links].strip('[').strip(']').split(','))

#%%
def hp2hp(link):
    link = [int(point) for point in link]
    linkHp =np.cumsum(link).tolist()
    return linkHp

def hp2wgs(link):
    link = [point/10000000 for point in link]
    return link

def str2int(linkCur,linkWgs):
    if not linkCur[0]:
        return [0]*len(linkWgs)
    
    linkCur = [int(point) for point in linkCur]
    linkCur = [0]+linkCur+[0]
    return linkCur

def spdlim(linkSl,linkWgs):
    linkSl = linkSl*len(linkWgs)
    return linkSl

#%%
linklonHpx = [hp2hp(link) for link in linklon]
linklatHpy = [hp2hp(link) for link in linklat]
linklonWgs = [hp2wgs(link) for link in linklonHpx]
linklatWgs = [hp2wgs(link) for link in linklatHpy]
#linkRadius = [str2int(link) for link in linkRad]
linkRadiusP = []
for link in range(len(linkRad)):
    linkRadiusP.append(str2int(linkRad[link], linklatWgs[link]))

linkSpdlim = [[int(link)] for link in linkSpdTo]
linkspdLimP = []
for link in range(len(linkSpdlim)):
    linkspdLimP.append(spdlim(linkSpdlim[link], linklatWgs[link]))
    
Latitude = sum(linklatWgs,[])
Longitude = sum(linklonWgs,[])
SpdLimKPH = sum(linkspdLimP,[])
Curvature = sum(linkRadiusP,[])

#%%


linkDataOut = pd.DataFrame(list(zip(Latitude,Longitude,SpdLimKPH,Curvature)),columns=['Latitude','Longitude','SpdLimKPH','Curvature'])

linkDataOut['AyDyn'] = np.interp(linkDataOut['SpdLimKPH'],AyProfile['SpeedAy'],AyProfile['AyD']) 
#Target Lateral Acceleration - Comfort
linkDataOut['AyCmf'] = np.interp(linkDataOut['SpdLimKPH'],AyProfile['SpeedAy'],AyProfile['AyC'])
#Target Lateral Acceleration - ECO
linkDataOut['AyEco'] = np.interp(linkDataOut['SpdLimKPH'],AyProfile['SpeedAy'],AyProfile['AyE'])

linkDataOut['CornerTgtSpdCmf_KPH'] = np.sqrt(np.abs(linkDataOut['Curvature']) * (linkDataOut['AyCmf']))*3.6 # comfort KPH
linkDataOut['CornerTgtSpdEco_KPH'] = np.sqrt(np.abs(linkDataOut['Curvature']) * (linkDataOut['AyEco']))*3.6 # comfort KPH
linkDataOut['CornerTgtSpdDyn_KPH'] = np.sqrt(np.abs(linkDataOut['Curvature']) * (linkDataOut['AyDyn']))*3.6 # comfort KPH

linkDataOut['spdLimChange'] = linkDataOut['SpdLimKPH'] != linkDataOut['SpdLimKPH'].shift()
linkDataOut['cornerSpdAdap_Cmf'] = linkDataOut.loc[(linkDataOut['CornerTgtSpdCmf_KPH'] < linkDataOut['SpdLimKPH']) & (linkDataOut['CornerTgtSpdCmf_KPH'] > 0),['CornerTgtSpdCmf_KPH']]
linkDataOut['cornerSpdAdap_Eco'] = linkDataOut.loc[(linkDataOut['CornerTgtSpdEco_KPH'] < linkDataOut['SpdLimKPH']) & (linkDataOut['CornerTgtSpdCmf_KPH'] > 0),['CornerTgtSpdEco_KPH']]
linkDataOut['cornerSpdAdap_Dyn'] = linkDataOut.loc[(linkDataOut['CornerTgtSpdDyn_KPH'] < linkDataOut['SpdLimKPH']) & (linkDataOut['CornerTgtSpdCmf_KPH'] > 0),['CornerTgtSpdDyn_KPH']]

        
#deg to rad conv
Latitude_wgs_rad = linkDataOut['Latitude'].apply(lambda x:radians(x))
Longitude_wgs_rad = linkDataOut['Longitude'].apply(lambda x:radians(x))

# to calculate dist b/w shape points (same formula used in route validation as well)
lat1 = Latitude_wgs_rad.shift(1)
lat2 = Latitude_wgs_rad        
lon1 = Longitude_wgs_rad.shift(1)
lon2 = Longitude_wgs_rad                
length = 2*6371000*(np.sqrt(np.power(np.sin((lat1-lat2)/2),2)+np.cos(lat1)*np.cos(lat2)*np.power(np.sin((lon1-lon2)/2),2)))
length = length.fillna(0) # fill nan values with zero
gps_distance = length.cumsum() # find the cumulative distance (running total)
linkDataOut['Gps_Distance'] = gps_distance



Number_SpdLimChange = linkDataOut['spdLimChange'].sum()

Number_Corner_Cmf = (linkDataOut.cornerSpdAdap_Cmf.isnull() & linkDataOut.cornerSpdAdap_Cmf.shift(1).notna()).sum()
Number_Corner_Eco = (linkDataOut.cornerSpdAdap_Eco.isnull() & linkDataOut.cornerSpdAdap_Eco.shift(1).notna()).sum()
Number_Corner_Dyn = (linkDataOut.cornerSpdAdap_Dyn.isnull() & linkDataOut.cornerSpdAdap_Dyn.shift(1).notna()).sum()

Linklen = []
linkFclass = []
for links in range(len(link_list)):
    Linklen.append(link_list[links]['length'])
    linkFclass.append(link_list[links]['functionalClass'])
fcRatio = pd.DataFrame(list(zip(Linklen,linkFclass)),columns=['Linklen','linkFclass'])
fcRatioSum = fcRatio.groupby(['linkFclass']).sum()

fname = gpxfile.replace('/','\\')+'_sl_'+str(Number_SpdLimChange)+'_cmf_'+str(Number_Corner_Cmf)+'_eco_'+str(Number_Corner_Eco)+'_dyn'+str(Number_Corner_Dyn)+'.csv'
linkDataOut.to_csv(fname,index_label='timestamps') 

fname = gpxfile.replace('/','\\')+'FcProportion'+'.csv'
fcRatioSum.to_csv(fname,index_label='timestamps') 

#%%
# def linkAnalyse(link_sel):
#     #link_sel = Link_list[0]
#     link_LEN = link_sel['length']
#     #% Link Attributes
#     link_LINK = link_sel['attributes']['LINK_ATTRIBUTE_FCN'][0]
#     #
#     link_fc = link_LINK['FUNCTIONAL_CLASS']
#     link_intersecCat = link_LINK['INTERSECTION_CATEGORY']
#     link_urban = link_LINK['URBAN']
    
#     #% Speed Limits
#     link_SPDLIM = link_sel['attributes']['SPEED_LIMITS_FCN'][0]
#     #
#     link_spd_kph = link_SPDLIM['TO_REF_SPEED_LIMIT'] 
#     link_spd_units = link_SPDLIM['SPEED_LIMIT_UNIT'] 
#     if link_spd_units == 'M':
#         link_spd_local = round(int(link_spd_kph)/1.609)
#         link_spd_units = 'MPH'
#     else:
#         link_spd_local = link_spd_kph
#         link_spd_units = 'KPH'
    
#     #% Cordinates
#     link_ADAS = link_sel['attributes']['ADAS_ATTRIB_FCN'][0]
#     #
#     link_lon = link_ADAS['HPX']
#     link_lon = re.sub(r'\[','',link_lon)
#     link_lon = re.sub(r'\]','',link_lon).split(',')
    
#     link_lat = link_ADAS['HPY']
#     link_lat = re.sub(r'\[','',link_lat)
#     link_lat = re.sub(r'\]','',link_lat).split(',')
    
#     link_lon_hpx = [int(link_lon[0])]
#     for link in range(1,len(link_lon)):
#         link_lon_hpx.append(int(link_lon[link])+int(link_lon_hpx[link-1]))  
    
#     link_lat_hpx = [int(link_lat[0])]
#     for link in range(1,len(link_lat)):
#         link_lat_hpx.append(int(link_lat[link])+int(link_lat_hpx[link-1])) 
        
    
#     link_lon_wgs = [lon / 10000000 for lon in link_lon_hpx]
#     link_lat_wgs = [lat / 10000000 for lat in link_lat_hpx]
    
    
#     #% Curvature
#     link_curv = link_ADAS['CURVATURES']
#     link_curv= re.sub(r'\[','',link_curv)
#     link_curv = re.sub(r'\]','',link_curv).split(',')
#     link_curv_wgs = [0]
#     if link_curv[0] != '':
#         for curvs in range(len(link_curv)):
#             link_curv_wgs.append(int(link_curv[curvs]))
#     link_curv_wgs.append(0)
    
#     #% lengths
#     link_lengths = [0]
#     for link in range(1,len(link_lon_wgs)-1):
#         lat1 = radians(link_lat_wgs[link-1])
#         lat2 = radians(link_lat_wgs[link])
#         lon1 = radians(link_lon_wgs[link-1])
#         lon2 = radians(link_lon_wgs[link])
#         distance = 2*6371000*(sqrt(pow(sin((lat1-lat2)/2),2)+cos(lat1)*cos(lat2)*pow(sin((lon1-lon2)/2),2)))
#         link_lengths.append(distance)   
#     link_lengths.append(link_LEN-link_lengths[-1]) 
    
#     link_shape_distance = [0]
#     for link in range(1,len(link_lengths)-1):
#         distance = link_shape_distance[link-1]+link_lengths[link]
#         link_shape_distance.append(distance)
#     link_shape_distance.append(link_lengths[-1])
    
#     outDict = {'length':link_LEN,'functional_class':link_fc,'intersection_cat':link_intersecCat, 
#                'urban':link_urban,'speed_limit':link_spd_local,'speed units':link_spd_units,
#                'latitude':link_lat_wgs,'longitude':link_lon_wgs,'length': link_lengths,'distance':link_shape_distance,
#                'curvature':link_curv_wgs}
#     return outDict
# #%%
# route_len = []
# route_fc = []
# route_ic = []
# route_urban = []
# route_speed = []
# route_speedunits = []
# route_latitude = []
# route_longitude = []
# route_distance = []
# route_curvature = []
# route_lengths=[]

# for links in range(3):#range(len(Link_list)):
#     outDict = linkAnalyse(Link_list[links])   
#     route_len.append(outDict['length'])       
#     route_fc.append(outDict['functional_class'])    
#     route_ic.append(outDict['intersection_cat'])  
#     route_urban.append(outDict['urban']) 
#     route_speed.append(outDict['speed_limit'])
#     route_speedunits.append(outDict['speed units'])
#     route_latitude.append(outDict['latitude'])
#     route_longitude.append(outDict['longitude'])
#     route_distance.append(outDict['distance'])
#     route_curvature.append(outDict['curvature'])
#     route_lengths.append(outDict['length'])

# curvatures = []
# distance = []
# latitude = []
# longitude = []
# speedlimit = []
# speedlimitunits = []
# linkref = []
# for links in range(len(route_curvature)):
#     for points in range(len(route_curvature[links])):
#         linkref.append(links)
#         curvatures.append(route_curvature[links][points])
#         latitude.append(route_latitude[links][points])
#         longitude.append(route_longitude[links][points])
#         speedlimit.append(route_speed[links])
#         speedlimitunits.append(route_speedunits[links])
#         if links == 0 and  points == 0:
#             distance.append(route_lengths[links][points])
#         else:            
#             dist = distance[-1]+route_lengths[links][points]
#             distance.append(dist)

            
# #%%
# latA = np.array(latitude)
# lonA = np.array(longitude)
# latlon = np.array([latA,lonA])
# latlon = latlon.transpose()
     
