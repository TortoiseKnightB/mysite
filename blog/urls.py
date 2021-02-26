# !/usr/bin/python3
# @Author : Tortoise Knight
# @Time : 2021/2/19 9:18 上午
# @File : urls.py
# @Software: PyCharm
# ⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠹⢿⣿⣿⣿⣿⣿⡿⠋⣿⣿⣿⣿⣿                            |
# ⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠈⠻⣿⣿⡿⠏⠀⠀⣿⣿⣿⣿⣿                            |
# ⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠙⠋⠀⠀⠀⢀⣿⣿⣿⣿⣿                            |
# ⣿⣿⣷⡈⠉⠉⠉⠉⠉⠀⣀⡤⠴⠶⠶⠶⠤⣄⡀⠸⠿⠿⠛⢛⣿ code is far away from bugs |
# ⣿⣿⣿⣿⡄⠀⠀⠀⣰⠚⠁⠀⠀⠀⠀⠀⠀⠀⠳⣄⠀⠀⢠⣾⣿with the god Rick protecting|
# ⣿⣿⣿⣿⣷⠀⠀⡜⠁⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⠘⡆⢠⣿⣿⣿                            |
# ⣿⣿⠿⠛⠉⠀⢰⠇⠀⠰⣾⡯⠭⠭⣭⠭⡭⠭⠭⠭⢿⡀⠙⠿⣿                            |
# ⣿⣤⣀⠀⠀⠀⢸⠀⢠⣧⣤⣤⣤⠤⢼⣾⠥⣤⡤⠤⠬⡇⣠⣴⣾                            |
# ⣿⣿⣿⣿⡦⠀⢸⠀⠈⢧⡀⠁⠀⠀⡠⠛⣄⠈⠀⢀⣠⠇⣿⣿⣿                            |
# ⣿⣿⠿⠋⠀⠀⣸⡄⠀⢤⣉⠓⠚⠋⠁⡀⢸⡩⣯⡭⢿⡀⠙⠿⣿                            |
# ⣿⣷⣤⣄⡀⢼⠋⠀⠀⠀⠉⠉⠁⠀⠀⠳⣼⠇⠀⠀⣼⢹⣾⣿⣿                            |
# ⣿⣿⣿⣿⡟⠈⠳⣤⠀⠀⡀⠀⠀⣀⣀⣀⣀⣀⡀⠀⣿⡻⣿⣿⣿                            |
# ⣿⣿⣿⣿⣾⣿⣿⠞⣆⠸⡇⠚⠉⠁⠀⣿⣿⡟⠉⢁⣿⣿⣿⣿⣿  where is my stupid Morty? |
# ⣿⣿⣿⣿⣿⣿⣿⣶⣿⣆⠈⠁⠀⠰⡖⠙⠛⠃⣠⣿⣿⣿⣿⣿⣿                            |
# ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡦⣄⣀⣀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿                            |
# ⣿⣿⣿⣿⣿⣿⡿⠿⠟⠛⡛⢷⣤⣀⣠⢾⣛⠛⠿⢿⣿⣿⣿⣿⣿                            |
# ⣿⣿⣿⣿⣿⠃⠀⠀⠀⢰⠃⢸⠀⠀⠀⠘⡟⣆⠀⠀⢹⣿⣿⣿⣿                            |
# ---------------------------------------------------------
from django.urls import path
from . import views

# start with blog
urlpatterns = [
    # http://localhost:8000/blog/
    path('', views.blog_list, name="blog_list"),
    path('<int:blog_pk>', views.blog_detail, name="blog_detail"),
    path('type/<int:blog_type_pk>', views.blogs_with_type, name="blogs_with_type"),
    path('data/<int:year>/<int:month>', views.blogs_with_date, name="blogs_with_date"),
]
