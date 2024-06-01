import tkinter,tkinter.messagebox,customtkinter,tkinter.messagebox
import os
import sys
from PIL import Image

#프로그램 실행 위치 지정
scriptPath = os.path.abspath(__file__)
scripDir = os.path.dirname(scriptPath)
os.chdir(scripDir)
#print(f"현재 실행 위치: {os.getcwd()}")

# 창1
main = customtkinter.CTk()

# 창 설정
customtkinter.set_appearance_mode("System") 
customtkinter.set_default_color_theme("green")  
main.title("수평적 패턴의 수요 예측 프로그램")
main.geometry(f"{1100}x{580}")
main.minsize(1100,580)

# 폰트 설정

titleFont=customtkinter.CTkFont(size=24,weight="bold")

# 그리드 설정
main.grid_columnconfigure(0,weight=0)
main.grid_columnconfigure((1,2),weight=1)
main.grid_rowconfigure((0,1,2),weight=1)
main.grid_rowconfigure(3,weight=0)

# sideBar
main.sideBar=customtkinter.CTkFrame(main,width=200,corner_radius=0)
main.sideBar.grid(row=0, column=0, rowspan=4, sticky="nsew")
main.sideBar.grid_rowconfigure(4, weight=1)

# sideBar 아이콘
iconLight=Image.open("Img\iconLight.jpg")
iconLight=iconLight.resize((100, 100))
iconDark=Image.open("Img\iconDark.jpg")
iconDark=iconLight.resize((100, 100))
iconImage=customtkinter.CTkImage(light_image=iconLight,dark_image=iconLight,size=(100, 100))
main.iconLabel=customtkinter.CTkLabel(main.sideBar,image=iconImage,text="")
main.iconLabel.grid(row=1, column=0, padx=20, pady=10)

main.sideBarLabel1=customtkinter.CTkLabel(main.sideBar,text="수평적 패턴\n수요 예측 프로그램",font=titleFont)
main.sideBarLabel1.grid(row=2, column=0, padx=20, pady=10)
main.mainloop()