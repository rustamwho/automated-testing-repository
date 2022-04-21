from django.shortcuts import render
import requests
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response


class ActivateUser(GenericAPIView):

    def get(self, request, uid, token):
        """ Activation url after register new user. """
        payload = {'uid': uid, 'token': token}

        url = "http://localhost:8000/api/auth/users/activation/"
        response = requests.post(url, data=payload)

        if response.status_code == 204:
            return Response({}, response.status_code)
        else:
            return Response(response.json())
        # TODO: добавить шаблон подтверждения регистрации
        # TODO: добавить шаблон подтверждения активации
