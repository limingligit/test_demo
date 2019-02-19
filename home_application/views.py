# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云(BlueKing) available.
Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
"""
#coding: utf-8
from common.mymako import render_mako_context,render_json
from blueking.component.shortcuts import get_client_by_user, get_client_by_request
from conf.default import APP_ID, APP_TOKEN
import json
from home_application.models import StudentInfo

def home3(request):
    return render_mako_context(request, '/home_application/home3.html')

def formaction(request):
    return
def home1(request):
    data = StudentInfo.objects.all()
    return render_mako_context(request, '/home_application/change_pass.html')
def home2(request):
    data = StudentInfo.objects.all()
    return render_mako_context(request, '/home_application/home.html')
def search_student(request):
    name=request.POST.get('name_info')

    students=StudentInfo.objects.filter(name__icontains=name).values()

    result_list=[]
    for stu in students:
        result_list.append(stu)


    return render_json({'result':True, 'student':result_list})

def get_app_by_user(request):
    #try:
    username = request.user.username
    kwargs = {
        "bk_app_code": APP_ID,
        "bk_app_secret": APP_TOKEN,
        "bk_username": username,
        "fields": [

            "bk_biz_name"
        ],
        "condition": {
            "bk_biz_maintainer": username
        },
    }

    client = get_client_by_request(request)
    result = client.cc.search_business(kwargs)
    print(result)

        #return render_json({"result": True, "data": app_list})
    #except Exception, e:
        #return render_json({"result": False, "error": e})


    return render_json({"result": result, "username": username})


def edit_student(request):

    return render_json({'res':'bb'})


def dev_guide(request):
    """
    开发指引
    """
    return render_mako_context(request, '/home_application/dev_guide.html')


def contactus(request):
    """
    联系我们
    """
    return render_mako_context(request, '/home_application/contact.html')
