from django.http import JsonResponse

from apps.login import models
from .serializers import NewMemberModelSerializer, HistoryModelSerializer

from rest_framework.views import APIView

import json


# Create your views here.

class RegistantView(APIView):
    def get(self, request):
        id = request.query_params['id']
        sex = request.query_params['sex']
        phone_number = request.query_params['phone_number']
        department = request.query_params['department']
        nm1 = nm2 = nm3 = nm4 = models.NewMember.objects.all()
        if id:
            nm1 = models.NewMember.objects.filter(id=id)
        if sex:
            nm2 = models.NewMember.objects.filter(sex=sex)
        if phone_number:
            nm3 = models.NewMember.objects.filter(phone_number=phone_number)
        if department:
            nm4 = models.NewMember.objects.filter(department=department)
        nm = nm1 & nm2 & nm3 & nm4
        nms = NewMemberModelSerializer(instance=nm, many=True)

        return JsonResponse({'code': 200, 'message': 'OK', 'data': nms.data})

    def post(self, request):
        data = json.loads(request.body.decode())
        if data.get('id'):
            nm = models.NewMember.objects.filter(id=data['id']).first()
            nms = NewMemberModelSerializer(instance=nm, data=data)
        else:
            nms = NewMemberModelSerializer(data=data)
        if not nms.is_valid(raise_exception=True):
            return JsonResponse({'code': 400, 'message': '参数不正确'})
        nms.save()
        return JsonResponse({'code': 200, 'message': 'OK'})


class RegistantDeleteView(APIView):
    def post(self, request):
        data = json.loads(request.body.decode())
        id = data['id']
        models.NewMember.objects.filter(id=id).first().delete()
        return JsonResponse({'code': 200, 'message': 'OK'})


class HistoryView(APIView):
    def get(self, request):
        id = request.query_params['id']
        years = request.query_params['year']
        department_id = request.query_params['department']
        h1 = h2 = h3 = models.History.objects.all()
        if id:
            h1 = models.History.objects.filter(id=id)
        if years:
            h2 = models.History.objects.filter(years=years)
        if department_id:
            h3 = models.History.objects.filter(department_id=department_id)
        h = h1 & h2 & h3
        hs = HistoryModelSerializer(instance=h, many=True)

        return JsonResponse({'code': 200, 'message': 'OK', 'data': hs.data})

    def post(self, request):
        data = json.loads(request.body.decode())
        if data.get('id'):
            h = models.History.objects.filter(id=data['id']).first()
            hs = HistoryModelSerializer(instance=h, data=data)
        else:
            hs = HistoryModelSerializer(data=data)
        if not hs.is_valid(raise_exception=True):
            return JsonResponse({'code': 400, 'message': '参数不正确'})
        hs.save()
        return JsonResponse({'code': 200, 'message': 'OK'})


class HistoryDeleteView(APIView):
    def post(self, request):
        data = json.loads(request.body.decode())
        id = data['id']
        models.History.objects.filter(id=id).first().delete()
        return JsonResponse({'code': 200, 'message': 'OK'})

# class CommentsView(APIView):
#     def get(self, request):
#         id = request.query_params['id']
#         keyword = request.query_params['keyword']
#         c1 = c2 = models.Comments.objects.all()
#         if id:
#             c1 = models.Comments.objects.filter(id=id)
#         if keyword:
#             c2 = models.Comments.objects.filter(content__icontains=keyword)
#         c = c1 & c2
#         cs = CommentsModelSerializer(instance=c, many=True)
#
#         return JsonResponse({'code': 200, 'message': 'OK', 'data': cs.data})
#
#     def post(self, request):
#         data = json.loads(request.body.decode())
#         cs = CommentsModelSerializer(data=data)
#         if not cs.is_valid(raise_exception=True):
#             return JsonResponse({'code': 400, 'message': '参数不正确'})
#         cs.save()
#         return JsonResponse({'code': 200, 'message': 'OK'})
