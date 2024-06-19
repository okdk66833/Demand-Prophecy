#설치 모듈: CTkTable,tensorflow,numpy,matplotlib,customtkinter
#필요 파일: main.py,module폴더,img폴더,__pycache__폴더,setting

import tkinter as tk,tkinter.messagebox,customtkinter,tkinter.messagebox
from CTkTable import *
import os,sys,re
os.environ['KERAS_BACKEND'] = 'tensorflow'
os.environ['TF_ENABLE_ONEDNN_OPTS'] ='0'
import random,time
from PIL import Image
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.ticker as ticker
import module.process as ps,module.mathod as md

# 그래프 한글 출력
plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False

# 변수
fee,w,result,demandForecast,numList=[],[],[0,0,0,0],0,[]
feeLabelList,feeInputList=[],[]
weightLabelList,weightInputList=[],[]
stat,num=0,0
feeI=0

# 정보 창
def infoWindow():
    global iconImage

    info=customtkinter.CTk()
    # 창 설정
    info.title("정보")
    info.geometry(f"{500}x{450}")
    info.minsize(500,450)
    info.maxsize(500,450)
    info.iconbitmap("img/iconNoBG.ico")

    # 창 그리드 설정
    info.grid_columnconfigure(0,weight=1)
    info.grid_rowconfigure((0,1,3),weight=0)
    info.grid_rowconfigure(2,weight=1)

    info.Label1=customtkinter.CTkLabel(info,text="정보",font=titleFont)
    info.Label1.grid(row=0,column=0,columnspan=3,padx=20,pady=(20,0),sticky="w")

    # info.logoLabel=customtkinter.CTkLabel(info,image=logoImage,text="")
    # info.logoLabel.grid(row=0,column=0,padx=10,pady=10)

    # 텍스트박스
    info.textbox0=customtkinter.CTkTextbox(info,font=textboxFont)
    info.textbox0.grid(row=1,column=0,padx=20,pady=20,sticky="nsew")
    info.textbox0.insert("0.0","경기대학교 인문사회과학전공자를위한파이썬활용\n\n"
                    +"수평적 패턴의 수요 예측 프로그램 alpha 2.5\n\n"
                    +"구성원\n조장: 이민호\n조원: 김도경, 남윤도, 허민준\n\n"
                    +"copyright 2024 all rights reserved."
    )
    info.textbox0.configure(state="disabled")

    #프레임4
    info.frame4 =customtkinter.CTkFrame(info)
    info.frame4.grid(row=3,column=0,padx=20,pady=20,sticky="e")
    info.frame4.grid_columnconfigure(0,weight=0)

    ## frame4 버튼 1
    info.frame4Button1=customtkinter.CTkButton(info.frame4,command=lambda:info.destroy(),text="확인",font=buttonFont,corner_radius=5,height=35)
    info.frame4Button1.grid(row=0,column=0,padx=5,pady=5)
    info.mainloop()

# 설정 창
def settingWindow():

    def saveSetting():
        line=[]
        displayMode=''
        line.append(setting.switch1.get())
        line.append(setting.switch2.get())
        line.append(setting.switch3.get())
        line.append(setting.switch4.get())
        tmp=[0,0]
        if setting.option1.get()=="라이트": 
            tmp[0]=0
            displayMode='Light'
        elif setting.option1.get()=="다크": 
            tmp[0]=1
            displayMode='Dark'
        else: 
            tmp[0]=2
            displayMode='System'

        if setting.option2.get()=="80%": tmp[1]=0
        elif setting.option2.get()=="90%": tmp[1]=1
        elif setting.option2.get()=="100%": tmp[1]=2
        elif setting.option2.get()=="110%": tmp[1]=3
        elif setting.option2.get()=="120%": tmp[1]=4
        
        line.append(tmp[0])
        line.append(tmp[1])
        ps.settingEdit(line)

        reloadTabview()
        customtkinter.set_appearance_mode(displayMode)
        setting.frame4Button3.configure(state="disabled")
        if tmp[1]>2:
            setting.geometry(f"{600}x{500}")
            setting.minsize(600,500)
            setting.maxsize(66000,500)
        else:
            setting.geometry(f"{500}x{400}")
            setting.minsize(500,400)
            setting.maxsize(500,400)
    def enableSave1():
        setting.frame4Button3.configure(state="normal")
    def enableSave2(input):
        setting.frame4Button3.configure(state="normal")
    def saveQuit():
        #print(setting.frame4Button3.cget("state"))
        if setting.frame4Button3.cget("state")=='normal': saveSetting()
        setting.destroy()

    # 설정 창
    setting=customtkinter.CTk()

    # 창 설정
    setting.title("설정")
    setting.geometry(f"{500}x{400}")
    setting.minsize(500,400)
    setting.maxsize(500,400)
    setting.iconbitmap("img/iconNoBG.ico")

    # 창 그리드 설정
    setting.grid_columnconfigure(0,weight=1)
    setting.grid_rowconfigure((0,1,2,4),weight=0)
    setting.grid_rowconfigure(3,weight=1)

    #레이블1
    setting.Label1=customtkinter.CTkLabel(setting,text="설정",font=titleFont)
    setting.Label1.grid(row=0,column=0,columnspan=3,padx=20,pady=(20,0),sticky="w")

    #프레임2
    setting.frame2 =customtkinter.CTkFrame(setting)
    setting.frame2.grid(row=1,column=0,padx=20,pady=(20,0),sticky="ew")
    setting.frame2.grid_columnconfigure((0,1),weight=1)
    setting.frame2.grid_rowconfigure((0,1,2),weight=1)

    ## frame2 레이블 프레임
    setting.frame6=customtkinter.CTkFrame(setting.frame2)
    setting.frame6.grid(row=0,column=0,columnspan=2,padx=10,pady=10,sticky="nsew")
    setting.frame6.grid_columnconfigure(0,weight=1)

    ##레이블2
    setting.Label1=customtkinter.CTkLabel(setting.frame6,text="사용 기법",font=frameTitleFont)
    setting.Label1.grid(row=0,column=0,pady=5)

    ###스위치 1
    setting.switch1=customtkinter.CTkSwitch(setting.frame2,text="단순이동평균법",font=buttonFont,command=enableSave1)
    setting.switch1.grid(row=1,column=0,padx=5,pady=5)

    ###스위치 2
    setting.switch2=customtkinter.CTkSwitch(setting.frame2,text="가중이동평균법",font=buttonFont,command=enableSave1)
    setting.switch2.grid(row=1,column=1,padx=5,pady=5)

    ###스위치 3
    setting.switch3=customtkinter.CTkSwitch(setting.frame2,text="지수평활법",font=buttonFont,command=enableSave1)
    setting.switch3.grid(row=2,column=0,padx=5,pady=5)

    ###스위치 4
    setting.switch4=customtkinter.CTkSwitch(setting.frame2,text="tensorflow AI",font=buttonFont,command=enableSave1)
    setting.switch4.grid(row=2,column=1,padx=5,pady=5)

    #프레임1
    setting.frame1 =customtkinter.CTkFrame(setting)
    setting.frame1.grid(row=2,column=0,padx=20,pady=(20,0),sticky="nsew")
    setting.frame1.grid_columnconfigure((0,1),weight=1)
    ## frame1 레이블 프레임
    setting.frame7=customtkinter.CTkFrame(setting.frame1)
    setting.frame7.grid(row=0,column=0,columnspan=2,padx=10,pady=10,sticky="nsew")
    setting.frame7.grid_columnconfigure(0,weight=1)

    ###레이블3
    setting.Label3=customtkinter.CTkLabel(setting.frame7,text="화면 모드 및 UI 스케일링",font=frameTitleFont)
    setting.Label3.grid(row=0,column=0,pady=5)
    
    ## 옵션 1
    setting.option1=customtkinter.CTkOptionMenu(setting.frame1,values=["라이트","다크","시스템 설정"],command=enableSave2)
    setting.option1.grid(row=1,column=0,pady=5)

    ## 옵션 2
    setting.option2=customtkinter.CTkOptionMenu(setting.frame1,values=["80%","90%","100%","110%","120%"],command=enableSave2)
    setting.option2.grid(row=1,column=1,pady=5)

    #프레임4
    setting.frame4 =customtkinter.CTkFrame(setting)
    setting.frame4.grid(row=4,column=0,padx=20,pady=20,sticky="e")
    setting.frame4.grid_columnconfigure(0,weight=0)

    ## frame4 버튼 1
    setting.frame4Button1=customtkinter.CTkButton(setting.frame4,command=saveQuit,text="확인",font=buttonFont,corner_radius=5,height=35)
    setting.frame4Button1.grid(row=0,column=0,padx=5,pady=5)

    ## frame4 버튼 2
    setting.frame4Button2=customtkinter.CTkButton(setting.frame4,command=lambda:setting.destroy(),text="취소",font=buttonFont,corner_radius=5,height=35)
    setting.frame4Button2.grid(row=0,column=1,padx=5,pady=5)

    ## frame4 버튼 3
    setting.frame4Button3=customtkinter.CTkButton(setting.frame4,command=saveSetting,text="적용",font=buttonFont,corner_radius=5,height=35)
    setting.frame4Button3.grid(row=0,column=2,padx=5,pady=5)

    #기본 설정
    setting.frame4Button3.configure(state="disabled")
    line=ps.settingGet()
    if line[0]=="0": setting.switch1.deselect()
    else: setting.switch1.select()
    if line[1]=="0": setting.switch2.deselect()
    else: setting.switch2.select()
    if line[2]=="0": setting.switch3.deselect()
    else: setting.switch3.select()
    if line[3]=="0": setting.switch4.deselect()
    else: setting.switch4.select()
    if line[4]=="0": setting.option1.set("라이트")
    elif line[4]=="1": setting.option1.set("다크")
    else: setting.option1.set("시스템 설정")
    if line[5]=="0": setting.option2.set("80%")
    if line[5]=="1": setting.option2.set("90%")
    if line[5]=="2": setting.option2.set("100%")
    if line[5]=="3": setting.option2.set("110%")
    if line[5]=="4": setting.option2.set("120%")
    if int(line[5])>2:
        setting.geometry(f"{600}x{500}")
        setting.minsize(600,500)
        setting.maxsize(600,500)
    else:
        setting.geometry(f"{500}x{400}")
        setting.minsize(500,400)
        setting.maxsize(500,400)

    setting.mainloop()

# 탭뷰 제로딩
def reloadTabview():
    line=ps.settingGet()
    #print(line)
    main.tabview =customtkinter.CTkTabview(main,width=250)
    main.tabview.grid(row=0,column=2,rowspan=4,padx=(20,20),pady=(20,20),sticky="nsew")
    main.tabview.add("  종합  ")
    if line[0]=='1': main.tabview.add("  단순이동평균법  ")
    if line[1]=='1': main.tabview.add("  가중이동평균법  ")
    if line[2]=='1': main.tabview.add("  지수평활법  ")
    if line[3]=='1': main.tabview.add("  Tensorflow  ")
    if line[5]=='0': customtkinter.set_widget_scaling(0.8)
    elif line[5]=='1': customtkinter.set_widget_scaling(0.9)
    elif line[5]=='2': customtkinter.set_widget_scaling(1)
    elif line[5]=='3': customtkinter.set_widget_scaling(1.1)
    elif line[5]=='4': customtkinter.set_widget_scaling(1.2)

    if line[1]=='0' and line[2]=='0': 
        for i in range(feeI): weightInputList[i].configure(state="disabled")
        main.frame5Button1.configure(state="disabled")
        main.frame5Button2.configure(state="disabled")
    else:
        for i in range(feeI): weightInputList[i].configure(state="normal")
        main.frame5Button1.configure(state="normal")
        main.frame5Button2.configure(state="normal")

# 탭뷰 결과 출력
def resultTabview():
    global feeI,feeInputList,weightInputList,fee,w,demandForecast,numList
    line=ps.settingGet()
    if line[0]=='1':
        main.tabview.tab("  단순이동평균법  ").grid_rowconfigure((0,2,3,4),weight=0) 
        main.tabview.tab("  단순이동평균법  ").grid_rowconfigure((1,5),weight=1) 
        main.tabview.tab("  단순이동평균법  ").grid_columnconfigure(0,weight=1)
        ## 레이블1
        main.tabviewLabel1 =customtkinter.CTkLabel(main.tabview.tab("  단순이동평균법  "),text="입력 값",font=frameTitleFont)
        main.tabviewLabel1.grid(row=0,column=0,pady=10)

        # 스크롤 프레임 3
        main.scrollableFrame3=customtkinter.CTkScrollableFrame(main.tabview.tab("  단순이동평균법  "))
        main.scrollableFrame3.grid(row=1,column=0,padx=10,pady=10,sticky="nsew")
        main.scrollableFrame3.columnconfigure(0,weight=1)

        table=[['번호','수요']]
        for i in range(feeI):
            tmp=[]
            tmp.append(numList[i])
            tmp.append(fee[i])
            table.append(tmp)
        #print(table)
        main.table1=CTkTable(main.scrollableFrame3,row=feeI+1,column=2,values=table,corner_radius=5,font=textboxFont)
        main.table1.grid(row=1,column=0,sticky="nsew")

        ## 레이블
        main.tabviewLabel2 =customtkinter.CTkLabel(main.tabview.tab("  단순이동평균법  "),text="결과",font=frameTitleFont)
        main.tabviewLabel2.grid(row=2,column=0,pady=10)

        # 텍스트박스
        main.textbox2=customtkinter.CTkTextbox(main.tabview.tab("  단순이동평균법  "),font=textboxFont,height=10)
        main.textbox2.grid(row=3,column=0,padx=10,pady=10,sticky="ew")
        main.textbox2.insert("0.0",result[0])
        main.textbox2.configure(state="disabled")

        ## 레이블
        main.tabviewLabel3 =customtkinter.CTkLabel(main.tabview.tab("  단순이동평균법  "),text="그래프",font=frameTitleFont)
        main.tabviewLabel3.grid(row=4,column=0,pady=10)

        # 그래프
        fig=plt.Figure(figsize=(5,4),dpi=100)
        ax=fig.add_subplot(111)
        ax.plot(numList+[len(numList)+1],fee+[result[0]],marker='o',linestyle='-.',color='#2cc985')
        ax.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))
        xticks_labels=numList +['결과']
        ax.set_xticks(range(1,len(xticks_labels)+1))
        ax.set_xticklabels(xticks_labels)
        canvas=FigureCanvasTkAgg(fig,master=main.tabview.tab("  단순이동평균법  "))
        canvas.draw()
        canvas.get_tk_widget().grid(row=5,column=0,padx=10,pady=10,sticky="nsew")

    if line[1]=='1':
            main.tabview.tab("  가중이동평균법  ").grid_rowconfigure((0,2,3,4),weight=0) 
            main.tabview.tab("  가중이동평균법  ").grid_rowconfigure((1,5),weight=1) 
            main.tabview.tab("  가중이동평균법  ").grid_columnconfigure(0,weight=1)
            ## 레이블1
            main.tabviewLabel4=customtkinter.CTkLabel(main.tabview.tab("  가중이동평균법  "),text="입력 값",font=frameTitleFont)
            main.tabviewLabel4.grid(row=0,column=0,pady=10)

            # 스크롤 프레임 3
            main.scrollableFrame4=customtkinter.CTkScrollableFrame(main.tabview.tab("  가중이동평균법  "))
            main.scrollableFrame4.grid(row=1,column=0,padx=10,pady=10,sticky="nsew")
            main.scrollableFrame4.columnconfigure(0,weight=1)

            table=[['번호','수요','가중치']]
            for i in range(feeI):
                tmp=[]
                tmp.append(numList[i])
                tmp.append(fee[i])
                tmp.append(w[i])
                table.append(tmp)
            #print(table)
            main.table1=CTkTable(main.scrollableFrame4,row=feeI+1,column=3,values=table,corner_radius=5)
            main.table1.grid(row=1,column=0,sticky="nsew")

            ## 레이블
            main.tabviewLabel5=customtkinter.CTkLabel(main.tabview.tab("  가중이동평균법  "),text="결과",font=frameTitleFont)
            main.tabviewLabel5.grid(row=2,column=0,pady=10)

            # 텍스트박스
            main.textbox3=customtkinter.CTkTextbox(main.tabview.tab("  가중이동평균법  "),font=textboxFont,height=10)
            main.textbox3.grid(row=3,column=0,padx=10,pady=10,sticky="ew")
            main.textbox3.insert("0.0",result[1])
            main.textbox3.configure(state="disabled")

            ## 레이블
            main.tabviewLabel6 =customtkinter.CTkLabel(main.tabview.tab("  가중이동평균법  "),text="그래프",font=frameTitleFont)
            main.tabviewLabel6.grid(row=4,column=0,pady=10)

            # 그래프
            fig=plt.Figure(figsize=(5,4),dpi=100)
            ax2=fig.add_subplot(111)
            ax2.plot(numList+[len(numList)+1],fee+[result[1]],marker='o',linestyle='-.',color='#2cc985')
            ax2.plot(numList,w,marker='x',linestyle='--',color='#ff5733',label='가중치')
            ax2.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))
            xticks_labels2=numList +['결과']
            ax2.set_xticks(range(1,len(xticks_labels2)+1))
            ax2.set_xticklabels(xticks_labels2)
            canvas2=FigureCanvasTkAgg(fig,master=main.tabview.tab("  가중이동평균법  "))
            canvas2.draw()
            canvas2.get_tk_widget().grid(row=5,column=0,padx=10,pady=10,sticky="nsew")

    if line[2]=='1':
            main.tabview.tab("  지수평활법  ").grid_rowconfigure((0,2,3,4),weight=0) 
            main.tabview.tab("  지수평활법  ").grid_rowconfigure((1,5),weight=1) 
            main.tabview.tab("  지수평활법  ").grid_columnconfigure(0,weight=1)
            ## 레이블1
            main.tabviewLabel7=customtkinter.CTkLabel(main.tabview.tab("  지수평활법  "),text="입력 값",font=frameTitleFont)
            main.tabviewLabel7.grid(row=0,column=0,pady=10)

            # 스크롤 프레임 3
            main.scrollableFrame5=customtkinter.CTkScrollableFrame(main.tabview.tab("  지수평활법  "))
            main.scrollableFrame5.grid(row=1,column=0,padx=10,pady=10,sticky="nsew")
            main.scrollableFrame5.columnconfigure(0,weight=1)

            table=[['수요','가중치','사용자의 예측값']]
            
            tmp=[]
            tmp.append(fee[-1])
            tmp.append(w[-1])
            tmp.append(demandForecast)
            table.append(tmp)

            #print(table)
            main.table3=CTkTable(main.scrollableFrame5,row=2,column=3,values=table,corner_radius=5)
            main.table3.grid(row=1,column=0,sticky="nsew")

            ## 레이블
            main.tabviewLabel8=customtkinter.CTkLabel(main.tabview.tab("  지수평활법  "),text="결과",font=frameTitleFont)
            main.tabviewLabel8.grid(row=2,column=0,pady=10)

            # 텍스트박스
            main.textbox4=customtkinter.CTkTextbox(main.tabview.tab("  지수평활법  "),font=textboxFont,height=10)
            main.textbox4.grid(row=3,column=0,padx=10,pady=10,sticky="ew")
            main.textbox4.insert("0.0",result[2])
            main.textbox4.configure(state="disabled")

            ## 레이블
            main.tabviewLabel9 =customtkinter.CTkLabel(main.tabview.tab("  지수평활법  "),text="그래프",font=frameTitleFont)
            main.tabviewLabel9.grid(row=4,column=0,pady=10)

            # 그래프
            fig=plt.Figure(figsize=(5,4),dpi=100)
            ax3=fig.add_subplot(111)
            ax3.plot([0,1],[fee[-1],result[2]],marker='o',linestyle='-.',color='#2cc985',label='예측치')
            ax3.plot(1,demandForecast,marker='x',color='red',label='사용자의 예측값')
            ax3.set_xticks([0,1])
            ax3.set_xticklabels([1,'결과'])
            ax3.legend()
            canvas3=FigureCanvasTkAgg(fig,master=main.tabview.tab("  지수평활법  "))
            canvas3.draw()
            canvas3.get_tk_widget().grid(row=5,column=0,padx=10,pady=10,sticky="nsew")

    if line[3]=='1':
        main.tabview.tab("  Tensorflow  ").grid_rowconfigure((0,2,3,4),weight=0) 
        main.tabview.tab("  Tensorflow  ").grid_rowconfigure((1,5),weight=1) 
        main.tabview.tab("  Tensorflow  ").grid_columnconfigure(0,weight=1)
        ## 레이블1
        main.tabviewLabel10 =customtkinter.CTkLabel(main.tabview.tab("  Tensorflow  "),text="입력 값",font=frameTitleFont)
        main.tabviewLabel10.grid(row=0,column=0,pady=10)

        # 스크롤 프레임 3
        main.scrollableFrame6=customtkinter.CTkScrollableFrame(main.tabview.tab("  Tensorflow  "))
        main.scrollableFrame6.grid(row=1,column=0,padx=10,pady=10,sticky="nsew")
        main.scrollableFrame6.columnconfigure(0,weight=1)

        table=[['번호','수요']]
        for i in range(feeI):
            tmp=[]
            tmp.append(numList[i])
            tmp.append(fee[i])
            table.append(tmp)
        #print(table)
        main.table4=CTkTable(main.scrollableFrame6,row=feeI+1,column=2,values=table,corner_radius=5,font=textboxFont)
        main.table4.grid(row=1,column=0,sticky="nsew")

        ## 레이블
        main.tabviewLabel11 =customtkinter.CTkLabel(main.tabview.tab("  Tensorflow  "),text="결과",font=frameTitleFont)
        main.tabviewLabel11.grid(row=2,column=0,pady=10)

        # 텍스트박스
        main.textbox5=customtkinter.CTkTextbox(main.tabview.tab("  Tensorflow  "),font=textboxFont,height=10)
        main.textbox5.grid(row=3,column=0,padx=10,pady=10,sticky="ew")
        main.textbox5.insert("0.0",result[3])
        main.textbox5.configure(state="disabled")

        ## 레이블
        main.tabviewLabel12 =customtkinter.CTkLabel(main.tabview.tab("  Tensorflow  "),text="그래프",font=frameTitleFont)
        main.tabviewLabel12.grid(row=4,column=0,pady=10)

        # 그래프
        fig=plt.Figure(figsize=(5,4),dpi=100)
        ax4=fig.add_subplot(111)
        ax4.plot(numList+[len(numList)+1],fee+[result[3]],marker='o',linestyle='-.',color='#2cc985')
        ax4.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))
        xticks_labels=numList +['결과']
        ax4.set_xticks(range(1,len(xticks_labels)+1))
        ax4.set_xticklabels(xticks_labels)
        canvas4=FigureCanvasTkAgg(fig,master=main.tabview.tab("  Tensorflow  "))
        canvas4.draw()
        canvas4.get_tk_widget().grid(row=5,column=0,padx=10,pady=10,sticky="nsew")

    main.tabview.tab("  종합  ").grid_rowconfigure((0,2,3,4),weight=0) 
    main.tabview.tab("  종합  ").grid_rowconfigure((1,5),weight=1) 
    main.tabview.tab("  종합  ").grid_columnconfigure(0,weight=1)
    ## 레이블1
    main.tabviewLabel13 =customtkinter.CTkLabel(main.tabview.tab("  종합  "),text="입력 값",font=frameTitleFont)
    main.tabviewLabel13.grid(row=0,column=0,pady=10)

    # 스크롤 프레임 3
    main.scrollableFrame6=customtkinter.CTkScrollableFrame(main.tabview.tab("  종합  "))
    main.scrollableFrame6.grid(row=1,column=0,padx=10,pady=10,sticky="nsew")
    main.scrollableFrame6.columnconfigure(0,weight=1)

    table=[['번호','수요','가중치']]
    for i in range(feeI):
        tmp=[]
        tmp.append(numList[i])
        tmp.append(fee[i])
        if line[1]=='1': tmp.append(w[i])
        table.append(tmp)
    #print(table)
    main.table5=CTkTable(main.scrollableFrame6,row=feeI+1,column=2,values=table,corner_radius=5,font=textboxFont)
    main.table5.grid(row=1,column=0,sticky="nsew")

    ## 레이블
    main.tabviewLabel14 =customtkinter.CTkLabel(main.tabview.tab("  종합  "),text="결과",font=frameTitleFont)
    main.tabviewLabel14.grid(row=2,column=0,pady=10)

    # 스크롤 프레임 3
    main.scrollableFrame7=customtkinter.CTkScrollableFrame(main.tabview.tab("  종합  "))
    main.scrollableFrame7.grid(row=3,column=0,padx=10,pady=10,sticky="nsew")
    main.scrollableFrame7.columnconfigure(0,weight=1)

    theNum=0
    table2=[['방법','예측값']]
    if line[0]=='1':
        theNum+=1
        tmp=[]
        tmp.append('단순이동평균법')
        tmp.append(result[0])
        table2.append(tmp)
    if line[1]=='1':
        theNum+=1
        tmp=[]
        tmp.append('가중이동평균법')
        tmp.append(result[1])
        table2.append(tmp)
    if line[2]=='1':
        theNum+=2
        tmp=[]
        tmp.append('지수평활법')
        tmp.append(result[2])
        table2.append(tmp)
        tmp=[]
        tmp.append('(지수평활법)사용자 예측값')
        tmp.append(demandForecast)
        table2.append(tmp)
    if line[3]=='1':
        theNum+=1
        tmp=[]
        tmp.append('tensorflow')
        tmp.append(result[3])
        table2.append(tmp)
        
    #print(table)
    main.table6=CTkTable(main.scrollableFrame7,row=theNum+1,column=2,values=table2,corner_radius=5,font=textboxFont)
    main.table6.grid(row=1,column=0,sticky="nsew")

    ## 레이블
    main.tabviewLabel15 =customtkinter.CTkLabel(main.tabview.tab("  종합  "),text="그래프",font=frameTitleFont)
    main.tabviewLabel15.grid(row=4,column=0,pady=10)

    # 그래프
    fig=plt.Figure(figsize=(5,4),dpi=100)
    ax5=fig.add_subplot(111)
    if line[0]=='1':
        ax5.plot(len(numList)+1,result[0],marker='o',linestyle='None',label='단순이동평균법',color='#0de18f')
        ax5.plot([numList[-1],len(numList)+1],[fee[-1],result[0]],linestyle='--',color='#0de18f')
    if line[1]=='1':
        ax5.plot(len(numList)+1,result[1],marker='o',linestyle='None',label='가중이동평균법',color='#0bbb77')
        ax5.plot([numList[-1],len(numList)+1],[fee[-1],result[1]],linestyle='--',color='#0bbb77')
    if line[2]=='1':
        ax5.plot(len(numList)+1,result[2],marker='o',linestyle='None',label='지수평활법',color='#09955f')
        ax5.plot([numList[-1],len(numList)+1],[fee[-1],result[2]],linestyle='--',color='#09955f')
    if line[3]=='1':
        ax5.plot(len(numList)+1,result[3],marker='o',linestyle='None',label='tensorflow',color='#076f47')
        ax5.plot([numList[-1],len(numList)+1],[fee[-1],result[3]],linestyle='--',color='#076f47')
    ax5.plot(numList,fee,marker='o',linestyle='-.',color='#2cc985')
    ax5.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))
    xticks_labels=numList+['결과']
    ax5.set_xticks(range(1,len(xticks_labels)+1))
    ax5.set_xticklabels(xticks_labels)
    ax5.legend()
    canvas5=FigureCanvasTkAgg(fig,master=main.tabview.tab("  종합  "))
    canvas5.draw()
    canvas5.get_tk_widget().grid(row=5,column=0,padx=10,pady=10,sticky="nsew")

#입력 추가
def addFeeFrame():
    line=ps.settingGet()
    global feeI,feeLabelList,feeInputList
    global weightI,weightLabelList,weightInputList

    feeLabel=customtkinter.CTkLabel(main.scrollableFrame1,text=f"{feeI+1}",font=infoFont,width=50)
    feeLabel.grid(row=feeI,column=0,padx=5,pady=5)

    feeInput=customtkinter.CTkEntry(main.scrollableFrame1)
    feeInput.grid(row=feeI,column=1,sticky="ew",padx=5,pady=5)

    weightLabel=customtkinter.CTkLabel(main.scrollableFrame2,text=f"{feeI+1}",font=infoFont,width=50)
    weightLabel.grid(row=feeI,column=0,padx=5,pady=5)

    weightInput=customtkinter.CTkEntry(main.scrollableFrame2)
    weightInput.grid(row=feeI,column=1,sticky="ew",padx=5,pady=5)

    weightLabelList.append(weightLabel)
    weightInputList.append(weightInput)

    feeLabelList.append(feeLabel)
    feeInputList.append(feeInput)
    if line[1]=='0' and line[2]=='0': weightInput.configure(state="disabled")
    feeI+=1 

# 입력 한개 삭제
def deleteFeeFrame():
    global feeI,feeLabelList,feeInputList
    global weightI,weightLabelList,weightInputList
    if feeI>0: 
        feeI-=1
        #print(feeI,"요소 제거 실행")
        feeLabelList[feeI].destroy()
        feeInputList[feeI].destroy()
        feeLabelList.pop()
        feeInputList.pop()

        weightLabelList[feeI].destroy()
        weightInputList[feeI].destroy()
        weightLabelList.pop()
        weightInputList.pop()

# 입력 전체 삭제
def deleteAllFeeFrame():
    global feeI,feeLabelList,feeInputList,weightLabelList,weightInputList
    for i in range(feeI):
        feeLabelList[i].destroy()
        feeInputList[i].destroy()
        weightLabelList[i].destroy()
        weightInputList[i].destroy()
    feeLabelList.clear()
    feeInputList.clear()
    weightLabelList.clear()
    weightInputList.clear()
    feeI=0

# 수요 입력 초기화
def resetFeeFrame():
    global feeI,feeInputList
    for i in range(feeI):
        feeInputList[i].destroy()
        feeInputList[i]=customtkinter.CTkEntry(main.scrollableFrame1)
        feeInputList[i].grid(row=i,column=1,sticky="ew",padx=5,pady=5)

# 가중치 자동 입력
def randomWeightFrame():
    global feeI,weightLabelList,weightInputList,w
    while True:
        randomF=[random.uniform(0.01,1) for _ in range(feeI)]
        total=sum(randomF)
        normalizedF=[round(x / total,2) for x in randomF]
        adjustment=round(1-sum(normalizedF),2)
        normalizedF[0]+=adjustment
        if sum(normalizedF)==1: break

    normalizedF.sort()

    for i in range(feeI):
        entryTmp=customtkinter.StringVar()
        weightInputList[i].configure(textvariable=entryTmp)
        entryTmp.set(normalizedF[i])

# 가중치 입력 초기화
def resetWeightFrame():
    global feeI,weightLabelList,weightInputList
    for i in range(feeI):
        weightInputList[i].destroy()
        weightInputList[i]=customtkinter.CTkEntry(main.scrollableFrame2)
        weightInputList[i].grid(row=i,column=1,sticky="ew",padx=5,pady=5)

# 입력 제어
def inputControl(input):
    if input=='enable':
        main.frame1Button1.configure(state="normal")
        main.frame1Button2.configure(state="normal")
        main.frame2Button1.configure(state="normal")
        main.frame2Button2.configure(state="normal")
        main.frame2Button3.configure(state="normal")
        main.frame2Button4.configure(state="normal")
        main.frame5Button1.configure(state="normal")
        main.frame5Button2.configure(state="normal")
        main.frame6Button1.configure(state="normal")
        for i in range(feeI):
            feeInputList[i].configure(state="normal")
            weightInputList[i].configure(state="normal")
    else:
        # 모든 입력 비활성화
        main.frame1Button1.configure(state="disabled")
        main.frame1Button2.configure(state="disabled")
        main.frame2Button1.configure(state="disabled")
        main.frame2Button2.configure(state="disabled")
        main.frame2Button3.configure(state="disabled")
        main.frame2Button4.configure(state="disabled")
        main.frame5Button1.configure(state="disabled")
        main.frame5Button2.configure(state="disabled")
        main.frame6Button1.configure(state="disabled")
        for i in range(feeI):
            feeInputList[i].configure(state="disabled")
            weightInputList[i].configure(state="disabled")

# 로딩바
def updateStat(a):
    global stat
    #print(stat/100,a)
    stat+=a
    main.frame6progressbar1.set(stat/100)
    main.frame6Label1.configure(text=str(float(round(stat,2)))+'%')
    main.update_idletasks()
    if float(round(stat,2))==100: main.frame6Label1.configure(text='완료')
    
# 예측 시작
def startProphecy():
    #텐서플로우 예측
    def runTensorflow():
        numListpy=np.array(numList,dtype=np.float32)
        feepy=np.array(fee,dtype=np.float32)
        model =keras.Sequential([keras.layers.Dense(units=1,input_shape=[1])])
        model.compile(optimizer='sgd',loss='mean_squared_error')
        class CustomCallback(keras.callbacks.Callback): 
            def on_epoch_end(self,epoch,logs=None): 
                updateStat(num/100)
        model.fit(numListpy,feepy,epochs=100,callbacks=[CustomCallback()])
        resultNum=np.array([len(numList)+1],dtype=np.float32)
        resultFee=model.predict(resultNum)
        return resultFee[0][0]
    
    # 변수 선언
    global feeI,feeInputList,weightInputList,fee,w,demandForecast,numList,result
    global stat,num
    fee,w,result,demandForecast,numList=[],[],[0,0,0,0],0,[]
    stat,num=0,0
    line=ps.settingGet()
    inputControl('disable')
    pattern=re.compile(r'^[0-9.]+$')
    if line[0]=='1':num+=1
    if line[1]=='1':num+=1
    if line[2]=='1':num+=1
    if line[3]=='1':num+=1
    num=96/num
    updateStat(0)
    time.sleep(0.1)

    # 입력 오류 검사
    if feeI==0:
        tkinter.messagebox.showerror("오류","수요 및 가중치가 1개 이상 필요합니다.")
        inputControl('enable')
        return 0    
    for i in range(feeI):
        numList.append(i+1)
        for string in feeInputList[i].get():
            if pattern.match(string):
                continue
            else:
                tkinter.messagebox.showerror("오류","수요에는 숫자와 온점만 입력할 수 있습니다.")
                inputControl('enable')
                return 0    
        if feeInputList[i].get()=='':
            tkinter.messagebox.showerror("오류","수요는 비워둘 수 없습니다.")
            inputControl('enable')
            return 0    
        else: fee.append(float(feeInputList[i].get()))
        if line[1]=='1' or line[2]=='1':
            for string in weightInputList[i].get():
                if pattern.match(string): continue
                else:
                    tkinter.messagebox.showerror("오류","가중치에는 숫자와 온점만 입력할 수 있습니다.")
                    inputControl('enable')
                    return 0    
            if weightInputList[i].get()=='':
                tkinter.messagebox.showerror("오류","가중치는 비워둘 수 없습니다.")
                inputControl('enable')
                return 0    
            else: w.append(float(weightInputList[i].get()))
    if line[1]=='1':
        if sum(w)!=1:
            tkinter.messagebox.showerror("오류","가중치의 합이 1이 아닙니다.")
            inputControl('enable')
            return 0    
    if line[2]=='1':
        step=0
        while True:
            if step==3:
                tkinter.messagebox.showerror("오류","지수평활법에 필요한 다음 달의 예측치 입력을 너무 많이 잘못 입력하였습니다.")
                inputControl('enable')
                return 0  
            flag=False
            dialog=customtkinter.CTkInputDialog(text="지수평활법에 필요한 다음 달의 예측치를 입력하세요.",title="입력창")
            dialogInput=dialog.get_input()
            if dialogInput==None:
                tkinter.messagebox.showerror("오류","다음 달의 예측치는 비워둘 수 없습니다.")
                step+=1
                flag=True
                continue
            for string in dialogInput:
                if pattern.match(string): continue
                else:
                    step+=1
                    tkinter.messagebox.showerror("오류","다음 달의 예측치에는 숫자와 온점만 입력할 수 있습니다.")  
                    flag=True
                    break
            if dialogInput=='': 
                step+=1
                tkinter.messagebox.showerror("오류","다음 달의 예측치는 비워둘 수 없습니다.")
                flag=True
            if flag==True: continue
            demandForecast=float(dialogInput)
            #print(demandForecast)
            break
    time.sleep(0.1)

    #결과 저장
    if line[0]=='1': 
        result[0]=round(md.demandProphecy(1,fee,0,0),2)
        updateStat(num)
        time.sleep(0.1)
    if line[1]=='1': 
        result[1]=round(md.demandProphecy(2,fee,w,0),2)
        updateStat(num)
        time.sleep(0.1)
    if line[2]=='1': 
        result[2]=round(md.demandProphecy(3,fee,w,demandForecast),2)
        updateStat(num)
        time.sleep(0.1)  
    if line[3]=='1': 
        result[3]=round(runTensorflow(),2)
        time.sleep(0.1)
    inputControl('enable')
    #print(result) 
    resultTabview()
    updateStat(4)
    
#프로그램 실행 위치 지정
scriptPath =os.path.abspath(__file__)
scripDir =os.path.dirname(scriptPath)
os.chdir(scripDir)
#print(f"현재 실행 위치: {os.getcwd()}")

# 메인 창
main=customtkinter.CTk()

# 창 설정
customtkinter.set_default_color_theme("green")  
main.title("수평적 패턴의 수요 예측 프로그램")
main.geometry(f"{1500}x{800}")
main.minsize(1500,800)
main.iconbitmap("img/iconNoBG.ico")

# 폰트 설정
titleFont=customtkinter.CTkFont(family="나눔고딕",size=25,weight="bold")
buttonFont=customtkinter.CTkFont(family="나눔고딕",size=15)
frameTitleFont=customtkinter.CTkFont(family="나눔고딕",size=18,weight="bold")
infoFont=customtkinter.CTkFont(family="나눔고딕",size=13)
textboxFont=customtkinter.CTkFont(family="나눔고딕",size=16)

# 그리드 설정
main.grid_columnconfigure(0,weight=0)
main.grid_columnconfigure((1,2),weight=1)
main.grid_rowconfigure((0,1,2),weight=1)
main.grid_rowconfigure(3,weight=0)

# frame 1 사이드바 프레임
main.frame1=customtkinter.CTkFrame(main,width=200,corner_radius=0)
main.frame1.grid(row=0,column=0,rowspan=4,sticky="nsew")
main.frame1.grid_rowconfigure(0,weight=0)  
main.frame1.grid_rowconfigure(1,weight=0)  
main.frame1.grid_rowconfigure(2,weight=1)  
main.frame1.grid_rowconfigure(3,weight=0)  
main.frame1.grid_rowconfigure(4,weight=0)  

## frame1 아이콘
iconLight=Image.open("img/iconLight.jpg")
iconLight=iconLight.resize((100,100))
iconDark=Image.open("img/iconDark.jpg")
iconDark=iconDark.resize((100,100))
iconImage=customtkinter.CTkImage(light_image=iconLight,dark_image=iconDark,size=(100,100))
main.iconLabel=customtkinter.CTkLabel(main.frame1,image=iconImage,text="")
main.iconLabel.grid(row=0,column=0,padx=20,pady=10)

## frame1 레이블1
main.frame1Label1=customtkinter.CTkLabel(main.frame1,text="수평적 패턴 수요\n예측 프로그램",font=titleFont)
main.frame1Label1.grid(row=1,column=0,padx=20,pady=10)

## frame1 버튼1
main.frame1Button1=customtkinter.CTkButton(main.frame1,command=settingWindow,text="프로그램 설정",font=buttonFont,corner_radius=5,height=35)
main.frame1Button1.grid(row=3,column=0,padx=10,pady=5,sticky="ew")

## frame1 버튼2
main.frame1Button2=customtkinter.CTkButton(main.frame1,command=infoWindow,text="프로그램 정보",font=buttonFont,corner_radius=5,height=35)
main.frame1Button2.grid(row=4,column=0,padx=10,pady=(5,10),sticky="ew")

# 텍스트박스
main.textbox=customtkinter.CTkTextbox(main,font=textboxFont)
main.textbox.grid(row=0,column=1,padx=(20,0),pady=(20,0),sticky="nsew")

# frame2 월별 수요 입력 프레임
main.frame2 =customtkinter.CTkFrame(main)
main.frame2.grid(row=1,column=1,padx=(20,0),pady=(20,0),sticky="nsew")
main.frame2.grid_rowconfigure(0,weight=0) 
main.frame2.grid_rowconfigure(1,weight=1) 
main.frame2.grid_columnconfigure(0,weight=1)

## frame2 레이블 프레임
main.frame7=customtkinter.CTkFrame(main.frame2)
main.frame7.grid(row=0,column=0,padx=10,pady=10,sticky="nsew")
main.frame7.grid_columnconfigure(0,weight=1)

### frame2 레이블
main.frame2Label1=customtkinter.CTkLabel(main.frame7,text="월별 수요 입력",font=frameTitleFont)
main.frame2Label1.grid(row=0,column=0,pady=5)

## scrollFrame1
main.scrollableFrame1=customtkinter.CTkScrollableFrame(main.frame2)
main.scrollableFrame1.grid(row=1,column=0,padx=10,pady=10,sticky="nsew")
main.scrollableFrame1.columnconfigure(0,weight=0)
main.scrollableFrame1.columnconfigure(1,weight=1)

## frame2 버튼 프레임
main.frame3=customtkinter.CTkFrame(main.frame2)
main.frame3.grid(row=2,column=0,pady=(5,10))

### frame2 버튼 1
main.frame2Button1=customtkinter.CTkButton(main.frame3,command=addFeeFrame,text="추가",font=buttonFont,corner_radius=5,height=35)
main.frame2Button1.grid(row=0,column=0,padx=5,pady=5)

### frame2 버튼 2
main.frame2Button2=customtkinter.CTkButton(main.frame3,command=deleteFeeFrame,text="삭제",font=buttonFont,corner_radius=5,height=35)
main.frame2Button2.grid(row=0,column=1,padx=5,pady=5)

### frame 버튼 3
main.frame2Button3=customtkinter.CTkButton(main.frame3,command=resetFeeFrame,text="초기화",font=buttonFont,corner_radius=5,height=35)
main.frame2Button3.grid(row=0,column=3,padx=5,pady=5)

### frame2 버튼 4
main.frame2Button4=customtkinter.CTkButton(main.frame3,command=deleteAllFeeFrame,text="전체 삭제",font=buttonFont,corner_radius=5,height=35)
main.frame2Button4.grid(row=0,column=2,padx=5,pady=5)

# frame4 월별 가중치 입력
main.frame4=customtkinter.CTkFrame(main)
main.frame4.grid(row=2,column=1,padx=(20,0),pady=(20,0),sticky="nsew")
main.frame4.grid_rowconfigure(0,weight=0) 
main.frame4.grid_rowconfigure(1,weight=1) 
main.frame4.grid_rowconfigure(2,weight=0)
main.frame4.grid_columnconfigure(0,weight=1)

## frame4 레이블 프레임
main.frame8=customtkinter.CTkFrame(main.frame4)
main.frame8.grid(row=0,column=0,padx=10,pady=10,sticky="nsew")
main.frame8.grid_columnconfigure(0,weight=1)

## frame4 레이블
main.frame4Label1 =customtkinter.CTkLabel(main.frame8,text="월별 가중치 입력",font=frameTitleFont)
main.frame4Label1.grid(row=0,column=0,pady=5)

## scrollFrame2
main.scrollableFrame2=customtkinter.CTkScrollableFrame(main.frame4)
main.scrollableFrame2.grid(row=1,column=0,padx=10,pady=10,sticky="nsew")
main.scrollableFrame2.columnconfigure(0,weight=0)
main.scrollableFrame2.columnconfigure(1,weight=1)

## frame5 버튼 프레임
main.frame5=customtkinter.CTkFrame(main.frame4)
main.frame5.grid(row=2,column=0,pady=(5,10))

### frame5 버튼 1
main.frame5Button1=customtkinter.CTkButton(main.frame5,command=randomWeightFrame,text="자동",font=buttonFont,corner_radius=5,height=35)
main.frame5Button1.grid(row=0,column=0,padx=5,pady=5)

### frame5 버튼 2
main.frame5Button2=customtkinter.CTkButton(main.frame5,command=resetWeightFrame,text="초기화",font=buttonFont,corner_radius=5,height=35)
main.frame5Button2.grid(row=0,column=1,padx=5,pady=5)

# frame6 정보창 프레임
main.frame6=customtkinter.CTkFrame(main)
main.frame6.grid(row=3,column=1,padx=(20,0),pady=(20,20),sticky="nsew")
main.frame6.grid_columnconfigure(0,weight=0)
main.frame6.grid_columnconfigure(1,weight=0)
main.frame6.grid_columnconfigure(2,weight=1)

#frame6 버튼1
main.frame6Button1=customtkinter.CTkButton(main.frame6,command=startProphecy,text="예측시작",font=buttonFont,corner_radius=20,height=35)
main.frame6Button1.grid(row=0,column=0,padx=20,pady=10)

#frame6 레이블2
main.frame6Label1=customtkinter.CTkLabel(main.frame6,text="",font=infoFont)
main.frame6Label1.grid(row=0,column=1,padx=20,pady=10,sticky="nsew")

#frame6 로딩바
main.frame6progressbar1 =customtkinter.CTkProgressBar(main.frame6,orientation="horizontal")
main.frame6progressbar1.grid(row=0,column=2,padx=20,pady=10,sticky="ew")

# 경기대 로고
logoLight=Image.open("img/logoLight.jpg")
logoLight=iconLight.resize((100,42))
logoDark=Image.open("img/logoDark.jpg")
logoDark=iconDark.resize((100,42))
logoImage=customtkinter.CTkImage(light_image=logoLight,dark_image=logoDark,size=(100,42))

#탭뷰
reloadTabview()

#기본 설정
main.textbox.insert("0.0","환영합니다!\n\n"
                    +"수평적 패턴 수요 예측 프로그램은 추세,계절적 패턴,주기적 패턴이 없는 수요를 분석하는 데 중점을 둡니다. 이 프로그램은 복잡한 패턴을 배제하고 수요를 예측하는 간단하면서도 효과적인 통계적 기법들을 제공합니다.\n\n"
                    +"단순이동평균법,가중이동평균법,지수평활법,tensorflow AI 예측 기능을 제공합니다.\n\n"
                    +"직관적인 인터페이스와 간단한 설정으로 누구나 쉽게 사용할 수 있으며 다양한 변수와 모델을 사용할 수 있어,여러 산업 분야에서 활용이 가능합니다.\n\n"
                    +"메서드\n"
                    +"1. 단순이동평균법 (Simple Moving Average)\n단순이동평균법은 가장 기본적인 수요 예측 기법 중 하나로,과거 데이터의 일정 수의 항목들의 평균을 계산하여 미래의 수요를 예측합니다. 예를 들어,5달간의 수요 데이터를 이용해 단순이동평균을 계산하면,각 달의 수요 데이터를 더한 후 5로 나눈 값이 다음 날의 예측값이 됩니다. 새로운 데이터가 추가되면 가장 오래된 데이터가 제외되고,최신 데이터가 포함되어 평균이 다시 계산되므로,최신 경향을 반영할 수 있습니다.\n\n"
                    +"2. 가중이동평균법 (Weighted Moving Average)\n가중이동평균법은 단순이동평균법의 변형으로,각 데이터 포인트에 동일한 가중치를 부여하지 않고,각기 가중치를 달리하여 평균을 계산합니다. 일반적으로 최근 데이터에 더 높은 가중치를 부여하여 최신 트렌드를 더 정확히 반영합니다. 예를 들어,최근 3일의 데이터를 사용한다면 가장 최근의 데이터에 0.5,그 이전 데이터에 0.3,가장 오래된 데이터에 0.2의 가중치를 부여하여 가중평균을 계산합니다.\n\n"
                    +"3. 지수평활법 (Exponential Smoothing)\n지수평활법은 과거 데이터에 지수적으로 감소하는 가중치를 적용하여 수요를 예측하는 방법입니다. 이 방법은 오래된 데이터보다 최근 데이터를 더 중시하여 예측의 정확성을 높입니다. 지수평활법의 핵심은 평활 상수(알파 값)인데,이 값은 0과 1 사이의 값으로,최근 데이터에 부여할 가중치를 결정합니다. 알파 값이 클수록 최근 데이터에 더 많은 가중치를 부여하게 됩니다. 예를 들어,알파 값이 0.8이라면 최근 데이터가 전체 예측값에 큰 영향을 미치게 됩니다.\n\n"
                    +"4. TensorFlow AI 예측 기능\n이 프로그램은 전통적인 통계적 기법 외에도 TensorFlow를 활용한 인공지능 기반 예측 기능을 제공합니다. 인공신경망(Artificial Neural Network)과 머신러닝(Machine Learning) 알고리즘을 사용하여 과거 데이터를 학습하고,복잡한 패턴을 분석하여 더 정확한 예측을 수행합니다. TensorFlow는 강력한 데이터 처리 및 예측 모델링 도구로,대량의 데이터를 빠르게 처리하고 고도의 예측을 가능하게 합니다.")
main.textbox.configure(state="disabled")
main.frame6progressbar1.set(1)
displayMode=''
line=ps.settingGet()
if line[4]=='0': displayMode='Light'
elif line[4]=='1': displayMode='Dark'
elif line[4]=='2': displayMode='System'
customtkinter.set_appearance_mode(displayMode)
main.mainloop()