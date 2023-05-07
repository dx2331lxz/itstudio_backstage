from django.http import JsonResponse

from apps.login import models
from .serializers import NewMemberModelSerializer

from rest_framework.views import APIView

import json
# Create your views here.

class RegistantView(APIView):
    def get(self,request):
        id = request.query_params['id']
        sex = request.query_params['sex']
        phone_number = request.query_params['phone_number']
        department = request.query_params['department']
        nm1=nm2=nm3=nm4=models.NewMember.objects.all()
        if id:
            nm1 = models.NewMember.objects.filter(id=id)
        if sex:
            nm2 = models.NewMember.objects.filter(sex=sex)
        if phone_number:
            nm3 = models.NewMember.objects.filter(phone_number=phone_number)
        if department:
            nm4 = models.NewMember.objects.filter(department=department)
        nm = nm1& nm2& nm3& nm4
        nms = NewMemberModelSerializer(instance=nm, many=True)

        return JsonResponse({'code':200,'message':'OK','data':nms.data})

    def post(self,request):
        data = json.loads(request.body.decode())
        if data.get('id'):
            nm = models.NewMember.objects.filter(id=id).first()
            nms = NewMemberModelSerializer(instance=nm,data=data)
        else:
            nms = NewMemberModelSerializer(data=data)
        if not nms.is_valid(raise_exception=True):
            return JsonResponse({'code': 400, 'message': '参数不正确'})
        nms.save()
        return JsonResponse({'code': 200, 'message': 'OK'})

class RegistantDeleteView(APIView):
    def post(self,request):
        data = json.loads(request.body.decode())
        id = data['id']
        models.NewMember.objects.filter(id=id).first().delete()
        return JsonResponse({'code':200,'message':'OK'})



