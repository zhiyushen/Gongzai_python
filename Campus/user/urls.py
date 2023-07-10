from django.urls import path
from .views import UserViewSet, WeixinLogin, DataFill,\
    TrainList,getT,JXSpendRecord,JXRestRecord,getRecord,\
    CheckAgreeAndFill,setOpenid,getUserData,setUserData,setNickname

from rest_framework import routers

app_name = 'user'

urlpatterns = [
    path('login/', WeixinLogin.as_view(), name='Login'),
    path('data/fill/', DataFill.as_view(), name='Data'),
    path('train/list/',TrainList.as_view(),name='List'),
    path('train/T/',getT.as_view(),name='T'),
    path('train/JXSpendRecord/',JXSpendRecord.as_view(),name='JXSpendRecord'),
    path('train/JXRestRecord/',JXRestRecord.as_view(),name='JXRestRecord'),
    path('train/getRecord/',getRecord.as_view(),name='getRecord'),
    path('data/checkAgree/',CheckAgreeAndFill.as_view(),name='checkAgree'),
    path('data/setOpenid/',setOpenid.as_view(),name='setOpenid'),
    path('data/getUserData/',getUserData.as_view(),name='getUserData'),
    path('data/setUserData/',setUserData.as_view(),name='setUserData'),
    path('data/setNickname/',setNickname.as_view(),name='setNickname'),
]
router = routers.DefaultRouter()  # 创建路由器
router.register(r'info',UserViewSet, basename='User')  # 注册路由
urlpatterns = urlpatterns + router.urls