from apps.login import models
from .serializers import WorksModelSerializer, MembersModelSerializer, DepartmentModelSerializer
from rest_framework.views import APIView
import json
from apps.login.models import Works, Members, Department
from django.http import JsonResponse


# Create your views here.

# 部门作品
class WorksAPIView(APIView):
    def get(self, request):
        id = request.query_params['id']
        grade = request.query_params['grade']
        name = request.query_params['name']
        nm1 = nm2 = nm3 = Works.objects.all()
        if id:
            nm1 = Works.objects.filter(id=id)
        if grade:
            nm2 = Works.objects.filter(grade=grade)
        if name:
            nm3 = Works.objects.filter(name=name)
        nm = nm1 & nm2 & nm3
        nms = WorksModelSerializer(instance=nm, many=True)
        return JsonResponse({'code': 200, 'message': '查看成功', 'data': nms.data})

    def post(self, request):
        data = json.loads(request.body.decode())
        if data.get('id'):
            nm = models.Works.objects.filter(id=id).first()
            nms = WorksModelSerializer(instance=nm, data=data)
        else:
            nms = WorksModelSerializer(data=data)
        if not nms.is_valid(raise_exception=True):
            return JsonResponse({'code': 400, 'message': '参数不正确'})
        nms.save()
        return JsonResponse({'code': 200, 'message': '获取成功'})

    def delete(self, request):
        data = json.loads(request.body.decode())
        id = data['id']
        if id == '':
            return JsonResponse({'code': 400, 'message': 'id为空'})
        Works.objects.filter(id=id).first().delete()
        return JsonResponse({'code': 200, 'message': '删除成功'})

# 部门详情
class DepartmentAPIView(APIView):
    def get(self, request):
        id = request.query_params['id']
        department_cn = request.query_params['department_cn']
        department_en = request.query_params['department_en']
        status = request.query_params['status']
        nm1 = nm2 = nm3 = nm4 = Department.objects.all()
        if id:
            nm1 = Works.objects.filter(id=id)
        if department_cn:
            nm2 = Works.objects.filter(department_cn=department_cn)
        if department_en:
            nm3 = Works.objects.filter(department_en=department_en)
        if status:
            nm3 = Works.objects.filter(status=status)
        nm = nm1 & nm2 & nm3 & nm4
        nms = WorksModelSerializer(instance=nm, many=True)
        return JsonResponse({'code': 200, 'message': '查看成功', 'data': nms.data})

    def post(self, request):
        data = json.loads(request.body.decode())
        if data.get('id'):
            nm = models.Department.objects.filter(id=id).first()
            nms = DepartmentModelSerializer(instance=nm, data=data)
        else:
            nms = DepartmentModelSerializer(data=data)
        if not nms.is_valid(raise_exception=True):
            return JsonResponse({'code': 400, 'message': '参数不正确'})
        nms.save()
        return JsonResponse({'code': 200, 'message': '获取成功'})

    def delete(self, request):
        data = json.loads(request.body.decode())
        id = data['id']
        if id == '':
            return JsonResponse({'code': 400, 'message': 'id为空'})
        Department.objects.filter(id=id).first().delete()
        return JsonResponse({'code': 200, 'message': '删除成功'})


# 历史成员
class MembersAPIView(APIView):
    def get(self, request):
        id = request.query_params['id']
        years = request.query_params['years']
        name = request.query_params['name']
        department = request.query_params['department']
        nm1 = nm2 = nm3 = nm4 = Members.objects.all()
        if id:
            nm1 = Works.objects.filter(id=id)
        if years:
            nm2 = Works.objects.filter(department_cn=years)
        if name:
            nm3 = Works.objects.filter(department_en=name)
        if department:
            nm3 = Works.objects.filter(status=department)
        nm = nm1 & nm2 & nm3 & nm4
        nms = WorksModelSerializer(instance=nm, many=True)
        return JsonResponse({'code': 200, 'message': '查看成功', 'data': nms.data})

    def post(self, request):
        data = json.loads(request.body.decode())
        if data.get('id'):
            nm = models.Members.objects.filter(id=id).first()
            nms = MembersModelSerializer(instance=nm, data=data)
        else:
            nms = MembersModelSerializer(data=data)
        if not nms.is_valid(raise_exception=True):
            return JsonResponse({'code': 400, 'message': '参数不正确'})
        nms.save()
        return JsonResponse({'code': 200, 'message': '获取成功'})

    def delete(self, request):
        data = json.loads(request.body.decode())
        id = data['id']
        if id == '':
            return JsonResponse({'code': 400, 'message': 'id为空'})
        Members.objects.filter(id=id).first().delete()
        return JsonResponse({'code': 200, 'message': '删除成功'})
