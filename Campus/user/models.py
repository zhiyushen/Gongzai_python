# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Users(models.Model):
    #openid
    username = models.CharField(primary_key=True,max_length=100,default=1)
    #昵称
    nickName = models.CharField(max_length=100,blank=True, null=True)
    #初一-大四 ,其他,0-8
    grade = models.SmallIntegerField(blank=True, null=True)
    #1男 2女
    gender = models.CharField(blank=True, null=True,max_length=10)
    height = models.SmallIntegerField(blank=True, null=True)
    weight = models.SmallIntegerField(blank=True, null=True)
    age = models.SmallIntegerField(blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    chin = models.SmallIntegerField(blank=True, null=True)
    # 仰卧起坐
    abdominalcurl = models.SmallIntegerField(db_column='AbdominalCurl', blank=True,
                                             null=True)  # Field name made lowercase.
    jump = models.SmallIntegerField(blank=True, null=True)
    starttrain = models.DateField(db_column='StartTrain', blank=True, null=True)  # Field name made lowercase.
    nexttest = models.DateField(db_column='NextTest', blank=True, null=True)  # Field name made lowercase.
    # 是否有氧训练，1有，2无
    aerobic = models.SmallIntegerField(db_column='Aerobic', blank=True, null=True)  # Field name made lowercase.
    # 是否训练仰卧起坐，1有，2无
    train_abdominalcurl = models.SmallIntegerField(blank=True, null=True)
    train_chin = models.SmallIntegerField(blank=True, null=True)
    train_jump = models.SmallIntegerField(blank=True, null=True)
    train_run = models.SmallIntegerField(blank=True, null=True)
    # 是否合格，1是，2否
    iscompliance = models.SmallIntegerField(blank=True, null=True)
    # 引体向上段位
    # 0青铜 1白银 2黄金 3钻石
    chin_level = models.SmallIntegerField(blank=True, null=True)
    min_score = models.SmallIntegerField(blank=True,null=True)
    sec_score = models.SmallIntegerField(blank=True,null=True)
    T1=  models.FloatField(blank=True,null=True)
    T2 = models.FloatField(blank=True, null=True)
    T3 = models.FloatField(blank=True, null=True)
    T4 = models.FloatField(blank=True, null=True)
    strength = models.CharField(max_length=20,blank=True,null=True)
    avatar = models.CharField(max_length=100,blank=True,null=True)
    class Meta:
        managed = True
        db_table = 'users'



#四种训练类型
class TainList(models.Model):
    day = models.SmallIntegerField(default=1)
    type = models.CharField(max_length=20, blank=True, null=True)
    week = models.SmallIntegerField(default=1)
    trainContent = models.CharField(max_length=50, blank=True, null=True)
    trainName = models.CharField(max_length=50, blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'TrainList'

class JXRecord(models.Model):
    openid = models.CharField(max_length=100)
    #完成训练的具体时间(eg.2023-5-2 16:13)
    trainDate = models.DateField(auto_now=True)
    trainTime = models.TimeField(auto_now=True)
    #训练的第几天
    day = models.SmallIntegerField(default=1)
    trainName = models.CharField(max_length=50, blank=True, null=True)
    trainTime1 = models.SmallIntegerField(blank=True, null=True)
    trainTime2 = models.SmallIntegerField(blank=True, null=True)
    trainTime3 = models.SmallIntegerField(blank=True, null=True)
    trainTime4 = models.SmallIntegerField(blank=True, null=True)
    trainTime5 = models.SmallIntegerField(blank=True, null=True)
    trainTime6 = models.SmallIntegerField(blank=True, null=True)
    restTime1 = models.SmallIntegerField(blank=True, null=True,default=120)
    restTime2 = models.SmallIntegerField(blank=True, null=True,default=120)
    restTime3 = models.SmallIntegerField(blank=True, null=True,default=120)
    restTime4 = models.SmallIntegerField(blank=True, null=True,default=120)
    restTime5 = models.SmallIntegerField(blank=True, null=True,default=120)
    LongRunTime = models.SmallIntegerField(blank=True, null=True)
    LSDTime = models.SmallIntegerField(blank=True, null=True)
    finish = models.BooleanField(default=False)
    flag = models.BooleanField(default=False)


    class Meta:
        managed = True
        db_table = 'JXRecord'