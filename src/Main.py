from Analyse import *
import tkinter as tk
from tkinter import ttk
from M2 import *

functions = {
    '城市地铁图': city_realway_map,
    '城市线路数': city_lines,  # 各个城市线路数
    '城市站点数': city_station,  # 各个城市线路数
    '城市最大数': most_station,  # 各个城市线路数
    '换乘量统计': total_choose_number,  # 全国各城市的总的换乘站点数量（2换乘、3换乘、4换乘等）分布统计
    '地铁城地图': call_create_map,  # 绘制地图
    '地铁线分布': call_create_line,  # 生成城市地铁线路数量分布情况
    '地铁名词云': call_create_wordcloud,  # 生成地铁名词云
    '地铁常用名': call_create_word,  # 生成柱状图
    '关键词站名': keywords_line_station_name,
    '含门地铁名': call_create_door,  # 选取地铁站名字包含门的数据
    '大学地铁名': create_bar_which_name_include_university,  # 选取数量前5个名字中带有大学的地铁站的城市，并绘制柱状图
    '城市站点线': line_number_with_line_of_city,
    '线路数饼图': line_num_with_pie,  # 各个城市的线路数量的饼状图分布
    '站点数饼图': line_num_pie,  # 各个城市的站点数量的饼状图分布
    '站点数散图': line_with_plot,  # 散点图展示
    '站点数线图': line_with_line,  # 各城市的每条线路的站点数量的变化 折线图
    '站点数柱图': bar_with_best,  # 每个城市的哪条线路的地铁站点数量最多  柱形图
    '大学数线归': university_number_with_line,  # 统计各个城市的大学数量，然后利用回归图进行拟合（分析各个城市的大学数量与站点数量的关系
    '大学数散归': university_number_with_station,  # 统计各个城市的大学数量，然后利用回归图进行拟合（分析各个城市的大学数量与站点数量的关系
    '双变量点图': double_number,  # seaborn的双变量图：可以查看多变量之间的分布关系，也可以显示它本身的单变量情况
    '城市聚合图': much_city_analize,
}


def call_function(func):
    func()


def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))


root = tk.Tk()
root.title("数据分析")
frame = ttk.Frame(root)
# 设置窗口大小
window_width = 700
window_height = 300
center_window(root, window_width, window_height)
frame.pack(fill=tk.X, padx=5, pady=5)
# 设置按钮的列数，可根据实际情况调整
num_columns = 3

# 计算每列应放置多少个按钮
buttons_per_column = len(functions) // num_columns
if len(functions) % num_columns != 0:
    buttons_per_column += 1

# 用于记录当前列和行索引
column_index = 0
row_index = 0

for function_name, actual_function in list(functions.items()):
    btn = ttk.Button(frame, text=function_name, width=30,
                     command=lambda f=actual_function: call_function(f))
    btn.grid(column=column_index, row=row_index, sticky="ew", padx=5, pady=5)

    # 每列放置完按钮后，移动到下一行
    column_index += 1
    if column_index >= num_columns:
        column_index = 0
        row_index += 1

root.mainloop()
