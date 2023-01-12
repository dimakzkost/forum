from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view

from chat.models import Message
from chat.serializers import MessageSerializer


@api_view(['GET'])
def mess_get(request, user_id):
    mess = (Message.objects.filter(receiver_id=user_id) or Message.objects.filter(sender_id=user_id)) \
           and Message.objects.filter(delivered=False)
    serializer = MessageSerializer(mess, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['PATCH'])
def mess_patch(request, mess_id):
    mess = Message.objects.filter(id=mess_id).first()
    if mess:
        mess.delivered = True
        mess.save()
        return HttpResponse(status=status.HTTP_200_OK)
    else:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def mess_del(request, mess_id):
    mess = Message.objects.filter(id=mess_id).first()
    if mess:
        mess.delete()
        return HttpResponse(status=status.HTTP_200_OK)
    else:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)