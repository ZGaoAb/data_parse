from django.test import TestCase

from parse_work.models import Temperature

class Demo(TestCase):
    datas = Temperature.objects.all()
    for data in datas:
        print(data)


