import json
from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from pymysql import NULL

from .models import Users, TainList,JXRecord
from django.db.models import F
from .serializers import UsersSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.utils import timezone
import pytz
import requests


# 数据库django和sqlserver数据库的读写
# 序列化器
# drf框架


class UserViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = UsersSerializer
    queryset = Users.objects.all()


class WeixinLogin(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        """
        提供 post 请求
        """
        # 从请求中获得code
        code = json.loads(request.body).get('code')
        # 填写你的测试号密钥
        appid = 'wxd1fa40f8454dd256'
        appsecret = '09de143a2a8d4eab2b2a1fec95d14699'

        # 微信接口服务地址
        base_url = 'https://api.weixin.qq.com/sns/jscode2session'
        # 微信接口服务的带参数的地址
        url = base_url + "?appid=" + appid + "&secret=" + appsecret + "&js_code=" + code + "&grant_type=authorization_code"
        print(url)
        response = requests.get(url)
        # 处理获取的 openid
        try:
            openid = response.json()['openid']
        except KeyError:
            return Response({'code': 'fail'})

        return Response({'openid': openid})
#查询用户是否同意过协议
class CheckAgreeAndFill(APIView):
    def post(self, request, format=None):
        openid = request.data.get('openid')
        user = Users.objects.filter(username = openid)
        isAgree = 0
        isFill = 0
        islog = 0
        nickName=""
        avatar=""
        if user.exists():
            isAgree = 1
            u = user.first()
            if u.weight!=None:
                isFill = 1
            if u.nickName != None:
                islog = 1
                nickName = u.nickName
            if  u.avatar != None:
                avatar = u.avatar
        return Response({"isAgree": isAgree,"isFill": isFill,"islog":islog,"nickName":nickName,"avatar":avatar}, status=201)

#存入用户的openid
class setOpenid(APIView):
    def post(self, request, format=None):
        openid = request.data.get('openid')
        print(openid)
        Users.objects.create(username = openid)
        return Response({"success":1}, status=201)

#存入用户名和头像
class setNickname(APIView):
    def post(self, request, format=None):
        openid = request.data.get('openid')
        print(openid)
        nickname = request.data.get('nickname')
        print(nickname)
        avatar = request.data.get('avatarUrl')
        print(avatar)
        user = Users.objects.get(username = openid)
        user.nickName = nickname
        user.avatar = avatar
        user.save()
        print(user)
        return Response({"success": 1}, status=201)

#获得用户基本信息
class getUserData(APIView):
    def post(self, request, format=None):
        openid = request.data.get('openid')
        type = request.data.get('type')
        birthday = Users.objects.get(username=openid).birthdate
        grade_radio = Users.objects.get(username=openid).grade
        nickname = "小功"
        avatar = " "
        if Users.objects.get(username=openid).nickName!=None:
            nickname = Users.objects.get(username=openid).nickName
        if Users.objects.get(username=openid).avatar!=None:
            avatar = Users.objects.get(username=openid).avatar
        weight = Users.objects.get(username=openid).weight
        height = Users.objects.get(username=openid).height
        min = Users.objects.get(username=openid).min_score
        sec = Users.objects.get(username=openid).sec_score
        gender = Users.objects.get(username=openid).gender
        gender_radio = 0
        if gender=="男":
            gender_radio = 1
        else: gender_radio = 2
        strength = Users.objects.get(username=openid).strength
        startTrain = Users.objects.get(username=openid).starttrain
        name = []
        state = []
        for i in range(20):
            name.append(TainList.objects.filter(type=strength)[i].trainName)
            # 将功补过
            if TainList.objects.filter(type=strength)[i].trainName == None:
                rs = JXRecord.objects.filter(openid=openid, day=i + 1)
                if rs.exists():
                    r = JXRecord.objects.filter(openid=openid, day=i + 1).last()
                    if r.finish == True:
                        state.pop()
                        state.append(0)
                        state.append(3)
                    else:
                        state.append(0)
                else:
                    state.append(0)
            if TainList.objects.filter(type=strength)[i].trainName != None:
                records = JXRecord.objects.filter(openid=openid, day=i + 1)
                if records.exists():
                    record = JXRecord.objects.filter(openid=openid, day=i + 1).last()
                    finish = record.finish
                    if finish == True:
                        state.append(1)
                    else:
                        state.append(2)
                else:
                    state.append(2)

        return Response({"birthday": birthday,"grade":grade_radio,"nickname":nickname,"weight":weight,"avatar":avatar,'list': name,'state':state,
                         "height":height,"min":min,"sec":sec,"gender":gender,"gender_radio":gender_radio,"type":type,"startTrain":startTrain}, status=201)

#保存用户修改的信息
class setUserData(APIView):
    def post(self, request, format=None):
        openid = request.data['openid']
        user = Users.objects.get(username = openid)
        flag = request.data.get('flag')
        #生日和年级
        if flag == 1:
            birthday = request.data['birthday']
            grade =  request.data['grade']
            user.birthdate = birthday
            user.grade = grade
            user.save()
        if flag == 2:
            height = request.data['height']
            weight = request.data['weight']
            user.height = height
            user.weight = weight
            user.save()
        return Response({"success": 1}, status=201)


#将问卷信息存入数据库
class DataFill(APIView):
    permission_classes = [AllowAny]
    serializer_class = UsersSerializer

    def post(self, request, format=None):
        gender_radio = request.data.get('gender')
        min_score = int(request.data['min_score'])
        sec_score = int(request.data['sec_score'])
        openid = request.data.get('openid')
        height = request.data['height']
        weight = request.data['weight']
        trainType=request.data.get('trainType')
        birthdate = request.data.get('birthdate')
        grade = request.data.get('grade')
        startTrain = request.data.get('starttrain')
        gender=''
        gradation=''
        #判断类型
        if trainType==1:
            gradation='M-R'
        elif trainType==0:
            gradation = 'M-L'
        elif trainType==3:
            gradation = 'F-R'
        else:
            gradation = 'F-L'
        #判断性别和T
        if gender_radio == '1':
            gender = '男'
            if min_score>=6:
                s=90
            elif min_score==5 and sec_score>=30:
                s=60
            elif min_score==4 and sec_score>=10 or min_score==5 and sec_score<30:
                s=40
            elif min_score==3 and sec_score>=50 or min_score==4 and sec_score<10:
                s=30
            elif min_score<3 or min_score==3 and sec_score<50:
                s=25
        else:
            gender = '女'
            if min_score>=6:
                s=60
            elif min_score>=5:      #默认小于6
                s=40
            elif min_score>=4:      #默认小于5
                s=30
            elif min_score<4:
                s=25
        T=min_score*60+sec_score
        T1=T-s/4
        T2=T-2*s/4
        T3=T-3*s/4
        T4=T-s
        record = Users.objects.filter(username=openid)
        record.update(gender=gender,height=height,weight=weight,birthdate = birthdate,grade = grade,starttrain=startTrain,
                            min_score=min_score,sec_score=sec_score,strength=gradation,T1=T1,T2=T2,T3=T3,T4=T4)
        return Response({'gradation': gradation}, status=201)


#获得训练内容
class TrainList(APIView):
    def post(self, request, format=None):
        name=[]
        state=[]
        type = "M-L"
        openid = request.data.get('openid')
        typeid=request.data.get('type')
        if typeid == 0:
            type="M-L"
        elif typeid == 1:
            type="M-R"
        elif typeid == 2:
            type="F-L"
        elif typeid == 3:
            type="F-R"
        # for i in range(28):
        #     name.append(TainList.objects.filter(type=type)[i].trainName)
        #     #将功补过
        #     if TainList.objects.filter(type=type)[i].trainName == None:
        #         rs = JXRecord.objects.filter(openid=openid, day=i + 1)
        #         if rs.exists():
        #             r = JXRecord.objects.filter(openid=openid, day=i + 1).last()
        #             if r.finish==True:
        #                 state.pop()
        #                 state.append(0)
        #                 state.append(3)
        #             else:
        #                 state.append(0)
        #         else:
        #             state.append(0)
        #     if TainList.objects.filter(type=type)[i].trainName !=None:
        #         records = JXRecord.objects.filter(openid=openid, day=i + 1)
        #         if records.exists():
        #             record = JXRecord.objects.filter(openid=openid, day=i+1).last()
        #             finish = record.finish
        #             if finish==True:
        #                 state.append(1)
        #             else:
        #                 state.append(2)
        #         else:
        #             state.append(2)
        # if typeid==0 or typeid==1:
        #     name.append("1000m模拟")
        #     name.append("1000m模拟")
        # else:
        #     name.append("800m模拟")
        #     name.append("800m模拟")
        # #如果第29天完成了，那第30天没有任务
        # records = JXRecord.objects.filter(openid=openid, day=29)
        # if records.exists():
        #     state.append(1)
        #     name[29]=" "
        # #否则第29天旷工，第30天有任务，完成的话，两天都完工，否则都旷工
        # else:
        #     state.append(2)
        # records = JXRecord.objects.filter(openid=openid, day=30)
        # if records.exists():
        #     state[28]=1
        #     state.append(1)
        # else:
        #     state.append(2)

        for i in range(20):
            name.append(TainList.objects.filter(type=type)[i].trainName)
            #将功补过
            if TainList.objects.filter(type=type)[i].trainName == None:
                rs = JXRecord.objects.filter(openid=openid, day=i + 1)
                if rs.exists():
                    r = JXRecord.objects.filter(openid=openid, day=i + 1).last()
                    if r.finish==True:
                        state.pop()
                        state.append(0)
                        state.append(3)
                    else:
                        state.append(0)
                else:
                    state.append(0)
            if TainList.objects.filter(type=type)[i].trainName !=None:
                records = JXRecord.objects.filter(openid=openid, day=i + 1)
                if records.exists():
                    record = JXRecord.objects.filter(openid=openid, day=i+1).last()
                    finish = record.finish
                    if finish==True:
                        state.append(1)
                    else:
                        state.append(2)
                else:
                    state.append(2)
        # if typeid==0 or typeid==1:
        #     name.append("1000m模拟")
        #     name.append("1000m模拟")
        # else:
        #     name.append("800m模拟")
        #     name.append("800m模拟")
        # #如果第29天完成了，那第30天没有任务
        # records = JXRecord.objects.filter(openid=openid, day=29)
        # if records.exists():
        #     state.append(1)
        #     name[29]=" "
        # #否则第29天旷工，第30天有任务，完成的话，两天都完工，否则都旷工
        # else:
        #     state.append(2)
        # records = JXRecord.objects.filter(openid=openid, day=30)
        # if records.exists():
        #     state[28]=1
        #     state.append(1)
        # else:
        #     state.append(2)
        return Response({'list': name,'state':state}, status=201)

#匹配T
class getT(APIView):
    def post(self,request,format=None):
        username = request.data.get('openid')
        T=[]
        T.append(Users.objects.filter(username=username)[0].T1)
        T.append(Users.objects.filter(username=username)[0].T2)
        T.append(Users.objects.filter(username=username)[0].T3)
        T.append(Users.objects.filter(username=username)[0].T4)
        return JsonResponse(T,safe=False,status=201)

#间歇跑类型的跑步时间记录
class JXSpendRecord(APIView):
    def post(self,request):
        openid = request.data.get('openid')
        trainName = request.data.get('trainName')
        date = request.data.get('date')
        day = request.data.get('day')
        time = request.data.get('trainTime')
        type = 0
        if trainName=="1000m模拟" or trainName=="800m模拟":
            flag = request.data.get('flag')
            JXRecord.objects.create(
                openid=openid,
                day=day,
                trainName=trainName,
                LongRunTime=time,
                finish = True,
                flag = flag
            )
        elif trainName=='LSD':
            JXRecord.objects.create(
                openid=openid,
                day=day,
                trainName=trainName,
                LSDTime=time,
                finish=True,
            )
        else:
            if trainName=="变距间歇跑":
                type=request.data.get('type')
            currentTime = request.data.get('currentTimeId')
            #如果是第一次
            if(currentTime == 1):
                flag = request.data.get('flag')
                JXRecord.objects.create(
                    openid = openid,
                    day = day,
                    trainName = trainName,
                    trainTime1 = time,
                    flag=flag
                )
            elif currentTime ==2:
                record = JXRecord.objects.get(openid = openid,trainDate = date)
                record.trainTime2 = time
                if trainName=='变距间歇跑' and type==1:
                    record.finish = True
                record.save()
            elif currentTime == 3:
                record = JXRecord.objects.get(openid=openid,trainDate = date)
                record.trainTime3 = time
                if trainName=='400*3间歇跑' or trainName == '200*3间歇跑' or (trainName=="变距间歇跑" and type==0):
                    record.finish = True
                record.save()
            elif currentTime == 4:
                record = JXRecord.objects.get(openid=openid,trainDate = date)
                record.trainTime4 = time
                print(time)
                if trainName=='200*4间歇跑':
                    record.finish = True
                record.save()
            elif currentTime == 5:
                record = JXRecord.objects.get(openid=openid, trainDate = date)
                record.trainTime5 = time
                if trainName == '100*5间歇跑':
                    record.finish = True
                record.save()
            elif currentTime == 6:
                record = JXRecord.objects.get(openid=openid, trainDate = date)
                record.trainTime6 = time
                if trainName == '100*6间歇跑':
                    record.finish = True
                record.save()
        return Response(openid,status=201)

#间歇跑类型的休息时间记录
class JXRestRecord(APIView):
    def post(self, request):
        openid = request.data.get('openid')
        currentTime = request.data['currentTimeId']
        day = request.data['day']
        date = request.data.get('date')
        time = request.data.get('restTime')
        # 如果是第一次
        if (currentTime == 1):
            record = JXRecord.objects.get(openid=openid, trainDate = date)
            record.restTime1 = time
            record.save()
        elif currentTime == 2:
            record = JXRecord.objects.get(openid=openid, trainDate = date)
            record.restTim2 = time
            record.save()
        elif currentTime == 3:
            record = JXRecord.objects.get(openid=openid, trainDate = date)
            record.restTime3 = time
            record.save()
        elif currentTime == 4:
            record = JXRecord.objects.get(openid=openid,trainDate = date)
            record.restTime4 = time
            record.save()
        elif currentTime == 5:
            record = JXRecord.objects.get(openid=openid, trainDate = date)
            record.restTime5 = time
            record.save()
        return Response(openid, status=201)

#获取该第几组了
class getRecord(APIView):
    def post(self, request):
        openid = request.data.get('openid')
        #训练第几天
        day = request.data['day']
        print(day)
        #具体日期
        date = request.data.get('date')
        print(date)
        records = JXRecord.objects.filter(openid=openid,  trainDate = date)
        result=[]
        id=0
        finish=False
        if records.exists():
            finish = JXRecord.objects.filter(openid=openid,  trainDate = date).last().finish
            record = JXRecord.objects.filter(openid=openid,  trainDate = date).last()
            result.append(record.trainTime1)
            result.append(record.restTime1)
            id=1
            if record.trainTime2!=None:
                result.append(record.trainTime2)
                result.append(record.restTime2)
                id=2
            if record.trainTime3!=None:
                result.append(record.trainTime3)
                result.append(record.restTime3)
                id=3
            if record.trainTime4!=None:
                result.append(record.trainTime4)
                result.append(record.restTime4)
                id=4
            if record.trainTime5!=None:
                result.append(record.trainTime5)
                result.append(record.restTime5)
                id=5
            if record.trainTime6 != None:
                result.append(record.trainTime6)
                print(record.trainTime6)
                id = 6
        else:
            id=0
        return Response({"id":id,"result":result,"finish":finish}, status=201)







# #训练层次
# class TrainSign(APIView):
#     permission_classes = [AllowAny]
#     serializer_class = RecodTrainSerializer
#
#     def post(self, request, format=None):
#         # 处理获取的 openid
#         username = request.data['user']
#         # 根据openid确定用户的本地身份
#         try:
#             user = Users.objects.get(username=username)
#         except Users.DoesNotExist:
#             return Response({'msg': '数据不存在'}, status=404)
#
#         serializer = RecodTrainSerializer(data=request.data)  # 这是新增数据，如果是修改已有的数据，需要instance、data两个数据对象
#
#         # 3.校验
#         if serializer.is_valid(raise_exception=True):
#             # 4.保存
#             serializer.save()
#             return Response({'msg': '更新数据成功'}, status=201)
