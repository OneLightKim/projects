from django.shortcuts import render
import pandas as pd
# Create your views here.
bar = pd.read_csv("./battery/TripA_con_bar.csv")
ts = pd.read_csv("./battery/TripA_con_bar_newTS.csv")
re_su = pd.read_csv("./battery/TripA_report_summary.csv")
re = pd.read_csv("./battery/TripA_report.csv")

def main(request):
    
    date =[]
    for i in range(32):
        str_="2014.7."+str(i+1)
        date.append(str_)
        
    time = request.GET.get("time")
    if time == None:
        time = bar.TripA_num.str.slice(0,8).unique()
        dt={'data':time,"date":date}
        return render(request,'main.html',dt)
    else:
        dt1 = bar.loc[bar.TripA_num.str.slice(0,8)==time,"displayed SoC [%]"]
        dt2 = bar.loc[bar.TripA_num.str.slice(0,8)==time,"AirCon Power [kW]"]
        dt3 = bar.loc[bar.TripA_num.str.slice(0,8)==time,"Heating Power CAN [kW]"]
        dt4 = ts.loc[ts.TripA_num==time,"Velocity_kmh"]
        dt5 = ts.loc[ts.TripA_num==time,"Motor Torque_Nm"]
        dt1 = list(dt1)
        dt2 = list(dt2)
        dt3 = list(dt3)
        dt4 = list(dt4)
        dt5 = list(dt5)
        label_len = []
        for i in range(3600):
            label_len.append(i+1)
        return render(request,'chart.html',context={'data1':dt1, 'data2':dt2, 'data3':dt3, 'data4':dt4,'data5':dt5, 'time':time,'label_len':label_len})
    

def report(request):
    time = request.GET.get("time")
    day = time

    day1=day+"-1"
    day2=day+"-2"
    day3=day+"-3"

    d_summary = re_su.loc[re_su['TripA_num']==day,"주행 요약"].values[0]
    d_report1 = re[re['TripA_num']==day1].sector_report.values[0]
    d_report2 = re[re['TripA_num']==day2].sector_report.values[0]
    d_report3 = re[re['TripA_num']==day3].sector_report.values[0]

    dt={'d_report':"    "+day+d_summary,"d_report1":day1+" "+d_report1,"d_report2":day2+" "+d_report2,"d_report3":day3+" "+d_report3,'day':day}
    return render(request,"report.html",dt)

