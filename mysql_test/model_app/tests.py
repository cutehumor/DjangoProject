import time

from django.test import TestCase
from .models import Students
# Create your tests here.

class StudentsTestCase(TestCase):
    def setUp(self) -> None:
        self.start_time = time.time()

    # 添加数据
    def test_insert_data(self):
        # 方法一：对象管理器
        # Students.objects.create(name='test', gender='男', score='99.5')

        # 方式二：实例化对象
        s = Students(name='test', gender='男', score='99.5')
        s.save()

        '''
        修改：s.name = '小李'
        删除：s.delete()
        查询主键：s = Students.objects.get(pk=1)
        查询主键：s = Students.objects.get(id=1)
        查询所有：s = Students.objects.all()
        过滤查询：s = Students.objects.filter(gender='男')
        
        __contains, __startswith, __endswith, __gte, __lte, __year, __month, __day
        首字查询：s = Students.objects.filter(name__startswith='王')
        模糊查询：s = Students.objects.filter(name__contains='雷')
        排除查询：s = Students.objects.exclude(score__gte=80)
        
        QuerySet同样适用数据切片
        
        升序排序查询：s = Students.objects.order_by('score')
        降序排序查询：s = Students.objects.order_by('-score')
        前三排序查询：s = Students.objects.order_by('-score')[:3]
        
        原生查询：使用原生SQL语句
        all = Students.objects.raw('select * from students;')
        for i in all:
            print(i.id, '--', i.name)
        RawQuerySet就是SQL语句
        QuerySet是列表
        '''

        print(f'Time Cost: {time.time() - self.start_time} ')

    def tearDown(self) -> None:
        print('Test Done!')

'''
Q查询
from django.db.models import Q
q1 = Q(score__gt=90)
q2 = Q(gender='男')
s = Students.objects.filter(q1&q2)
s[0].name

F查询（生成SQL表达式，直接对数据库进行操作）
from django.db.models import F
s = Students.objects.get(id=1)
s.score = F('score') - 5
s.save()

聚合查询（数据统计）
from django.db.models import Sum, Avg, Max, Min, Count
avg_score = Students.objects.all().aggregate(Avg("score"))
avg_score = Students.objects.aggregate(Avg("score"))
avg_score = Students.objects.filter(gender='男').aggregate(Avg("score"))

分组查询
score_avg = Students.objects.values("gender").annotate(Avg("score"))
'''
