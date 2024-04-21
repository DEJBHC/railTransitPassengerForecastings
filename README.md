中国城市轨道交通数据可视化分析—Python
=====
> - A demo based on data visualized analysis written in Python language.
## 概述
> - 本项目是一个基于 Python 的简单数据可视化分析的小Demo。通过这个项目可以练习使用Python数据可视化分析相关的强大的库和模块，练习绘制简单的GUI界面并且连接数据库，更加深了对Python语言的学习和拓展。本项目也可作为学校的大作业、大实验实践或者课程设计等的选题项目。
> - 本项目通过多线程爬虫获取了高德地图中的中国轨道交通的一些数据信息，高德地图这个权威的网站也保证了数据的完整可靠性，然后进行了一些简单并且有趣的数据可视化分析，另外还设计了一个GUI界面，查询数据库或者文件中的一些信息。
>
> - 如发现文档中或者源代码中有错误，欢迎大家在 `Issues` 中研究讨论，欢迎大家 `Fork` 和 `Pull requests` 改善代码，十分感谢！
## 使用语言
- Python 3
## 主要技术
* **网络编程**
* **多线程**
* **文件操作**
* **数据库编程**
* **GUI**
* **数据分析**
## 导入的库和模块
```python
from holoviews import opts
from pyecharts.globals import ThemeType
from wordcloud import WordCloud, ImageColorGenerator
from pyecharts.charts import Line, Bar, Geo
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import jieba
import seaborn as sns
from pyecharts import options as opts
import webbrowser
from pylab import mpl
import os
import tkinter as tk
import webbrowser
from Analyse import name_include_words_of_city, create_line_num, special_city_number, city_lines_count,
   city_station_count, most_station_number, call_create_door_by_city
import pandasgui as pg
import os
from Analyse import *
import tkinter as tk
from tkinter import ttk
from M2 import *
import sqlite3
import tkinter as tk
from tkinter import scrolledtext
import json
import requests
import sqlite3
from bs4 import BeautifulSoup
import threading
```
## 项目整体思路
1. 网页分析
2. 多线程爬虫爬取信息
3. 数据保存至文件中和数据库中
4. 利用 tkinter 绘制 GUI 界面，实现查询线路和站点两个功能
5. 可以选择城市查询地铁图
6. 数据可视化分析
   - （1）直接控制台显示分析结果
   - （2）绘制中国地图、柱状图等，生成 .html 文件
   - （3）绘制词云
   - （4）绘制柱状图、饼状图、折线图、散点图、双变量图等，生成 .png 文件
## 运行
- 本项目已包含数据，但是建议运行Spider.py文件更新数据后再运行Main.py
