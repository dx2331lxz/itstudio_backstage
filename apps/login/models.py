from django.db import models
from utils.ImageStorage import ImageStorage
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime


# Create your models here.


def get_default_rev():
    queryset = Department.objects.values_list('id', flat=True)
    for query in queryset:
        return query


class Department(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, verbose_name='部门ID')
    # did = models.IntegerField("部门ID")
    department_cn = models.CharField("部门名称", max_length=10)  # 如“程序部”
    department_en = models.CharField("部门英文名称", max_length=30)  # 如“程序部”
    icon = models.ImageField(verbose_name="部门图标", default=0, storage=ImageStorage())
    background = models.ImageField(verbose_name="部门图标", default=0, storage=ImageStorage())
    content = models.CharField("内容", max_length=800)  # 如部门介绍/部门要求
    introduction = models.CharField("介绍", max_length=800)  # 如部门介绍/部门要求
    status = models.SmallIntegerField("部门状态", choices=[(0, "解散"), (1, "健在")], default=1)

    class Meta:
        db_table = 'it_Department'
        verbose_name_plural = '部门详情'

    def __str__(self):
        return self.department_cn


class History(models.Model):
    # grade = models.IntegerField("年级")
    years = models.IntegerField("年份", default=int(datetime.now().strftime('%Y')), validators=[
        MaxValueValidator(2300),
        MinValueValidator(2000)
    ])
    # did = models.IntegerField("部门ID")
    # did = models.ForeignKey(Department, on_delete=models.DO_NOTHING(), related_name="history", verbose_name="部门id")
    # department_cn = models.CharField("部门", max_length=10)  # 如“程序部”
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING, related_name="history", verbose_name="部门",
                                   default=1)

    class Meta:
        db_table = 'it_History'
        verbose_name_plural = '历史表'

    def __str__(self):
        return self.department.department_cn


class Members(models.Model):
    # 默认id作为成员id
    avatar = models.ImageField("头像", upload_to="avatar", blank=True, default="default/user.jpg",
                               storage=ImageStorage())
    # did = models.IntegerField("所属部门ID", default=0)
    years = models.IntegerField("加入社团年份", default=int(datetime.now().strftime('%Y')), validators=[
        MaxValueValidator(2300),
        MinValueValidator(2000)
    ])
    name = models.CharField("成员姓名", max_length=10)
    motto = models.CharField("座右铭", max_length=300)
    # department_cn = models.CharField("所属部门", max_length=10)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING, related_name="member",
                                   verbose_name="所属部门", default=get_default_rev)

    class Meta:
        db_table = 'it_Members'
        verbose_name_plural = '部门成员'


class Comments(models.Model):
    class Meta:
        verbose_name_plural = u"弹幕内容"
        db_table = 'comments_comments'

    post_time = models.DateTimeField(verbose_name="发布时间")
    content = models.CharField(verbose_name="弹幕内容", max_length=50, blank=False)


class NewMember(models.Model):
    class Meta:
        verbose_name_plural = u"报名信息"
        db_table = 'enroll_newmember'

    schedules = [
        (1, "已报名"),
        (2, "初审中"),
        (3, "面试中"),
        (4, "笔试中"),
        (5, "成功录取"),
        (6, "初审失败"),
        (7, "面试失败"),
        (8, "笔试失败"),
        (9, "复试失败"),
        (10, "未录取")
    ]
    departments = [
        (0, "系统维护"),
        (1, "APP开发"),
        (2, "Web开发"),
        (3, "程序开发"),
        (4, "游戏开发"),
        (5, "UI设计")
    ]
    sex = [
        (0, "男"),
        (1, "女"),
        (2, "保密")
    ]
    name = models.CharField(max_length=20, verbose_name="姓名")
    sex = models.SmallIntegerField(choices=sex, default=2, verbose_name="性别")
    major = models.CharField(max_length=20, verbose_name="年级专业")
    phone_number = models.CharField(max_length=11, unique=True, verbose_name="手机号码")
    email = models.EmailField(unique=True, verbose_name="邮箱")
    department = models.SmallIntegerField(choices=departments, default=0,
                                          verbose_name="意向部门")
    expectation = models.TextField(max_length=200, verbose_name="期待的话")
    status = models.SmallIntegerField(choices=schedules, default=0, verbose_name="报名状态")

    def __str__(self):
        return self.name


class EmailVerifyRecord(models.Model):
    # 验证码
    code = models.CharField(max_length=5, verbose_name="验证码")
    email = models.EmailField(max_length=50, verbose_name="邮箱")
    # 包含注册验证和找回验证
    # send_type = models.CharField(verbose_name="验证码类型", max_length=10,
    #                              choices=(("register", "注册"), ("forget", "找回密码")))
    send_time = models.DateTimeField(verbose_name="发送时间", auto_now_add=True)


class Works(models.Model):
    class Meta:
        verbose_name_plural = u"部门作品"
        db_table = 'work_works'

    grade = models.IntegerField(verbose_name="年份")
    name = models.CharField(verbose_name="事件名称", max_length=30)
    description = models.CharField(verbose_name="事件描述", max_length=200)
    img = models.ImageField(verbose_name="图片", upload_to="image", null=True, blank=True, storage=ImageStorage())
