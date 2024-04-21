import tkinter as tk
import webbrowser
from tkinter import messagebox

from Analyse import name_include_words_of_city, create_line_num, special_city_number, city_lines_count, \
    city_station_count, most_station_number, call_create_door_by_city
import pandasgui as pg
import os




def keywords_line_station_name():
    def on_button_click():
        city = city_entry.get()
        keyword = keyword_entry.get()
        datas=name_include_words_of_city(city, keyword)
        pg.show(datas)
    # 创建主窗口并设置标题
    root = tk.Tk()
    root.title("各种城市地铁站名爱用字分析")

    # 创建城市输入框
    city_label = tk.Label(root, text="城市:")
    city_label.pack()

    city_entry = tk.Entry(root)
    city_entry.pack()

    # 创建关键词输入框
    keyword_label = tk.Label(root, text="关键词:")
    keyword_label.pack()

    keyword_entry = tk.Entry(root)
    keyword_entry.pack()

    # 创建确定按钮，并绑定点击事件
    confirm_button = tk.Button(root, text="确定", command=on_button_click)
    confirm_button.pack()

    # 运行主循环
    root.mainloop()
def line_number_with_line_of_city():
    def on_button_click():
        city = city_entry.get()
        create_line_num(city)
    # 创建主窗口并设置标题
    root = tk.Tk()
    root.title("各种城市线路站点数量的折线图趋势分布")

    # 创建城市输入框
    city_label = tk.Label(root, text="城市:")
    city_label.pack()

    city_entry = tk.Entry(root)
    city_entry.pack()

    # 创建确定按钮，并绑定点击事件
    confirm_button = tk.Button(root, text="确定", command=on_button_click)
    confirm_button.pack()

    # 运行主循环
    root.mainloop()
def much_city_analize():
    def on_button_click():
        citys = city_entry.get()
        city_list=citys.split(',')
        if len(city_list)!=4:
            print("输入错误")
            messagebox.showwarning("错误", "请输入4个城市名，使用(半角逗号),分开")
            return
        special_city_number(city_list)
    # 创建主窗口并设置标题
    root = tk.Tk()
    root.title("各种城市线路站点数量的折线图趋势分布")

    # 创建城市输入框
    city_label = tk.Label(root, text="城市:")
    city_label.pack()

    city_entry = tk.Entry(root)
    city_entry.pack()

    # 创建确定按钮，并绑定点击事件
    confirm_button = tk.Button(root, text="确定", command=on_button_click)
    confirm_button.pack()

    # 运行主循环
    root.mainloop()
def city_lines():
    df=city_lines_count()
    pg.show(df)
def city_station():
    df=city_station_count()
    pg.show(df)
def most_station():
    df=most_station_number()
    pg.show(df)
def call_create_door_by_city_call():
    def on_button_click():
        city = city_entry.get()
        df=call_create_door_by_city(city)
        pg.show(df)
        # 创建主窗口并设置标题
    root = tk.Tk()
    root.title("各种城市线路站点数量的折线图趋势分布")

    # 创建城市输入框
    city_label = tk.Label(root, text="城市:")
    city_label.pack()

    city_entry = tk.Entry(root)
    city_entry.pack()

    # 创建确定按钮，并绑定点击事件
    confirm_button = tk.Button(root, text="确定", command=on_button_click)
    confirm_button.pack()

    # 运行主循环
    root.mainloop()
def city_realway_map():
    # 获取当前脚本所在的绝对路径
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # 构建生成的HTML文件的绝对路径
    html_file_path = os.path.join(script_dir, "../res/subway_map/index.html")

    # 使用 webbrowser 打开生成的 HTML 文件
    webbrowser.open_new_tab(html_file_path)