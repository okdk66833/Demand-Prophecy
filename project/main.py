import tkinter,tkinter.messagebox,customtkinter,tkinter.messagebox
import os
import sys
from PIL import Image
import module.process as ps,module.mathod as md
from CTkTable import *

#프로그램 실행 위치 지정
scriptPath = os.path.abspath(__file__)
scripDir = os.path.dirname(scriptPath)
os.chdir(scripDir)
#print(f"현재 실행 위치: {os.getcwd()}")

# 창1
main=customtkinter.CTk()

# 창 설정
customtkinter.set_appearance_mode("System") 
customtkinter.set_default_color_theme("green")  
main.title("수평적 패턴의 수요 예측 프로그램")
main.geometry(f"{1500}x{800}")
main.minsize(1500,800)

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
iconLight=Image.open("Img/iconLight.jpg")
iconLight=iconLight.resize((100,100))
iconDark=Image.open("Img/iconDark.jpg")
iconDark=iconDark.resize((100,100))
iconImage=customtkinter.CTkImage(light_image=iconLight,dark_image=iconDark,size=(100,100))
main.iconLabel=customtkinter.CTkLabel(main.frame1,image=iconImage,text="")
main.iconLabel.grid(row=0,column=0,padx=20,pady=10)

## frame1 레이블1
main.frame1Label1=customtkinter.CTkLabel(main.frame1,text="수평적 패턴 수요\n예측 프로그램",font=titleFont)
main.frame1Label1.grid(row=1,column=0,padx=20,pady=10)

## frame1 버튼1
main.frame1Button1=customtkinter.CTkButton(main.frame1,command=0,text="프로그램 설정",font=buttonFont,corner_radius=20,height=35)
main.frame1Button1.grid(row=3,column=0,padx=10,pady=5,sticky="ew")

## frame1 버튼2
main.frame1Button2=customtkinter.CTkButton(main.frame1,command=0,text="프로그램 정보",font=buttonFont,corner_radius=20,height=35)
main.frame1Button2.grid(row=4,column=0,padx=10,pady=(5,10),sticky="ew")

# 텍스트박스
main.textbox=customtkinter.CTkTextbox(main,font=textboxFont)
main.textbox.grid(row=0,column=1,padx=(20,0),pady=(20,0),sticky="nsew")

# frame2 월별 수요 입력 프레임
main.frame2 = customtkinter.CTkFrame(main)
main.frame2.grid(row=1,column=1,padx=(20,0),pady=(20,0),sticky="nsew")
main.frame2.grid_rowconfigure(0,weight=0) 
main.frame2.grid_rowconfigure(1,weight=1) 
main.frame2.grid_rowconfigure(2,weight=0)
main.frame2.grid_columnconfigure(0,weight=1)

## frame2 레이블 프레임
main.frame7=customtkinter.CTkFrame(main.frame2)
main.frame7.grid(row=0,column=0,padx=10,pady=10,sticky="nsew")
main.frame7.grid_columnconfigure(0,weight=1)

### frame2 레이블
main.frame2Label1 = customtkinter.CTkLabel(main.frame7,text="월별 수요 입력",font=frameTitleFont)
main.frame2Label1.grid(row=0,column=0,pady=5)

## frame2 버튼 프레임
main.frame3=customtkinter.CTkFrame(main.frame2)
main.frame3.grid(row=2,column=0,pady=(5,10))

### frame2 버튼 1
main.frame3Button1=customtkinter.CTkButton(main.frame3,command=0,text="추가",font=buttonFont,corner_radius=20,height=35)
main.frame3Button1.grid(row=0,column=0,padx=5,pady=5)

### frame2 버튼 2
main.frame2.frame3Button2=customtkinter.CTkButton(main.frame3,command=0,text="삭제",font=buttonFont,corner_radius=20,height=35)
main.frame2.frame3Button2.grid(row=0,column=1,padx=5,pady=5)

### frame 버튼 3
main.frame3Button3=customtkinter.CTkButton(main.frame3,command=0,text="초기화",font=buttonFont,corner_radius=20,height=35)
main.frame3Button3.grid(row=0,column=2,padx=5,pady=5)

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
main.frame4Label1 = customtkinter.CTkLabel(main.frame8,text="월별 가중치 입력",font=frameTitleFont)
main.frame4Label1.grid(row=0,column=0,pady=5)

## frame5 버튼 프레임
main.frame5=customtkinter.CTkFrame(main.frame4)
main.frame5.grid(row=2,column=0,pady=(5,10))

### frame5 버튼 1
main.frame5Button1=customtkinter.CTkButton(main.frame5,command=0,text="자동",font=buttonFont,corner_radius=20,height=35)
main.frame5Button1.grid(row=0,column=0,padx=5,pady=5)

### frame5 버튼 2
main.frame5Button2=customtkinter.CTkButton(main.frame5,command=0,text="초기화",font=buttonFont,corner_radius=20,height=35)
main.frame5Button2.grid(row=0,column=1,padx=5,pady=5)

# frame6 정보창 프레임
main.frame6=customtkinter.CTkFrame(main)
main.frame6.grid(row=3,column=1,padx=(20,0),pady=(20,20),sticky="nsew")
main.frame6.grid_columnconfigure(0,weight=0)
main.frame6.grid_columnconfigure(1,weight=0)
main.frame6.grid_columnconfigure(2,weight=1)

#frame6 레이블1
main.frame6Label1=customtkinter.CTkLabel(main.frame6,text="정보창 입니다.",width=100,font=infoFont)
main.frame6Label1.grid(row=0,column=0,padx=20,pady=10,sticky="nsew")

#frame6 레이블2
main.frame6Label2=customtkinter.CTkLabel(main.frame6,text="50%",font=infoFont)
main.frame6Label2.grid(row=0,column=1,padx=20,pady=10,sticky="nsew")

#frame6 로딩바
main.frame6progressbar1 = customtkinter.CTkProgressBar(main.frame6, orientation="horizontal")
main.frame6progressbar1.grid(row=0,column=2,padx=20,pady=10,sticky="ew")

#탭뷰
main.tabview = customtkinter.CTkTabview(main, width=250)
main.tabview.grid(row=0, column=2,rowspan=4,padx=(20, 20), pady=(20, 20), sticky="nsew")
main.tabview.add("  단순이동평균법  ")
main.tabview.add(  "가중이동평균법  ")
main.tabview.add("  지수평활법  ")
main.tabview.add("  Tensorflow  ")

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
main.mainloop()