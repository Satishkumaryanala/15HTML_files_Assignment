"""
URL configuration for project_AHA project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('metromonial/',metromonial,name='metromonial'),
    path('Form_1/',Form_1,name='Form_1'),
    path('Form_2/',Form_2,name='Form_2'),
    path('Combinator_selector/',Combinator_selector,name='Combinator_selector'),
    path('Ass_table2/',Ass_table2,name='Ass_table2'),
    path('Ass_table3/',Ass_table3,name='Ass_table3'),
    path('Ass_table4/',Ass_table4,name='Ass_table4'),
    path('Ass_table5/',Ass_table5,name='Ass_table5'),
    path('Ass_table6/',Ass_table6,name='Ass_table6'),
    path('Ass_divTag/',Ass_divTag,name='Ass_divTag'),
    path('Ass_animation1/',Ass_animation1,name='Ass_animation1'),
    path('Ass_animation2/',Ass_animation2,name='Ass_animation2'),
    path('Ass_transform/',Ass_transform,name='Ass_transform'),
    path('digital_watch/',digital_watch,name='digital_watch'),
    path('fees_calculator/',fees_calculator,name='fees_calculator'),
]
