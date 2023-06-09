from datetime import date
from django.db.models import Sum, F
from django.db.models.functions import Abs
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import *


class ClubsAPIView(APIView):
    def get(self, request):
        clubs = Club.objects.annotate(umum_summa=Sum('futbolchilari__tr_narxi')).order_by('-umum_summa')
        serializer = ClubSerializer(clubs, many=True)
        return Response(serializer.data)



class PlayersAPIView(APIView):
    def get(self, request):
        player = Player.objects.order_by("-tr_narxi").all()
        serializer = PlayerSerializer(player, many=True)
        return Response(serializer.data)


class Latest_trAPIView(APIView):
    def get(self, request):
        tr = Transfer.objects.filter(mavsum=Hozirgi_mavsum.objects.all()[0]).order_by('-narxi')
        serializer = TransferSerializer(tr, many=True)
        return Response(serializer.data)

class ClubCountryView(APIView):
    def get(self, request, country):
        clubs = Club.objects.filter(davlat=country)
        serializer = ClubSerializer(clubs, many=True)
        return Response(serializer.data)


class TransferAPIView(APIView):
    def get(self, request):
        tr = Transfer.objects.all()
        serializer = TransferSerializer(tr, many=True)
        return Response(serializer.data)



class Transfer_mAPIView(APIView):
    def get(self, request, m):
        m_tr = Transfer.objects.filter(mavsum=m)
        serializer = TransferSerializer(m_tr, many=True)
        return Response(serializer.data)



class ClubPlayersAPIView(APIView):
    def get(self, request, pk):
        club_player = Player.objects.filter(club__id=pk).order_by('-tr_narxi')
        serializer = PlayerSerializer(club_player, many=True)
        return Response(serializer.data)


class Tr_recordsAPIView(APIView):
    def get(self, request):
        tr_r = Transfer.objects.filter(narxi__gt=50).order_by('-narxi')[:100]
        serializer = TransferSerializer(tr_r, many=True)
        return Response(serializer.data)


class U20playersAPIView(APIView):
    def get(self, request):
        from datetime import date, timedelta
        bugun = date.today()
        boshi = bugun - timedelta(days=7295)
        pl = Player.objects.filter(t_yil__range=[boshi, bugun])
        serializer = PlayerSerializer(pl, many=True)
        return Response(serializer.data)


class AccuratePrAPIView(APIView):
    def get(self, request):
        result = Transfer.objects.annotate(difference=Abs(F('narxi') - F('tax_narx')))

        result = result.annotate(divergence=100 * F('difference') / F('narxi')).order_by('divergence')
        serializer = TransferSerializer(result, many=True)
        return Response(serializer.data)

