import tkinter, tkinter.messagebox, customtkinter, tkinter.messagebox
import os
import sys

#프로그램 실행 위치 지정
scriptPath = os.path.abspath(__file__)
scripDir = os.path.dirname(scriptPath)
os.chdir(scripDir)

# 창1
main = customtkinter.CTk()

# 창 설정
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
main.title("수평적 패턴의 수요 예측 프로그램")
main.geometry(f"{1100}x{580}")

# configure grid layout (4x4)
main.grid_columnconfigure(1, weight=1)
main.grid_columnconfigure((2, 3), weight=0)
main.grid_rowconfigure((0, 1, 2), weight=1)

main.mainloop()