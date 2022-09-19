from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login as django_login, logout as django_logout

from .serializers import EmployeeSerializer, QuestionSerializer, LoginSerializer
from .models import Question

from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authtoken.models import Token
from rest_framework.filters import SearchFilter, OrderingFilter

from django_filters.rest_framework import DjangoFilterBackend
from django_filters import FilterSet
from django_filters import rest_framework as filters

from django.contrib.auth import get_user_model
User = get_user_model()

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        django_login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=200)


class LogOutView(APIView):
    authentication_classes = (TokenAuthentication, )

    def post(self, request):
        django_logout(request)
        return Response(status=204)

@csrf_exempt
def poll(request):
    if request.method == "GET":
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        # return serializer.data
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        # import pdb; pdb.set_trace()
        json_parser = JSONParser()
        data = json_parser.parse(request)
        serializer = QuestionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def poll_details(request, id=None):
    # instance = get_object_or_404(Question, id=id)
    try:
        instance = Question.objects.get(id=id)
    except Question.DoesNotExists as e:
        return JsonResponse({"error": "Given Question Object not found"}, status=404)

    if request.method == "GET":
        serializer = QuestionSerializer(instance)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "PUT":
        json_parser = JSONParser()
        data = json_parser.parse(request)
        serializer = QuestionSerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        else:
            return JsonResponse(serializer.errors, status=400)
    elif request.method == "DELETE":
        instance.delete()
        return HttpResponse(status=204)


class Poll(APIView):
    def get(self, request):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        data = request.data
        serializer = QuestionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)


class PollViewSet(APIView):
    def get_object(self, id):
        try:
            return Question.objects.get(id=id)
        except Question.DoesNotExist as e:
            return Response({"error": "Given Question Object not found"}, status=404)

    def get(self, request, id=None):
        instance = self.get_object(id)
        if instance.status_code != 404:
            serializer = QuestionSerializer(instance)
            return Response(serializer.data, status=200)
        else:
            return Response({"error": "Given Question Object not found"}, status=404)

    def put(self, request, id):
        data = request.data
        instance = self.get_object(id)
        serializer = QuestionSerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)

    def delete(self, request, id):
        instance = self.get_object(id)
        if instance.status_code != 404:
            instance.delete()
            return Response(status=204)
        else:
            return Response({"error": "Given Question Object not found to delete"}, status=404)


class PollGenericAPIView(generics.GenericAPIView,
                         mixins.CreateModelMixin,
                         mixins.ListModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.DestroyModelMixin):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    lookup_field = "id"
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def perform_create(self, serializer):
        # import pdb; pdb.set_trace()
        serializer.save(created_by=self.request.user)

    def put(self, request, id=None):
        return self.update(request, id)

    def perform_update(self, serializer):
        serializer.save(created_by=self.request.user)

    def delete(self, request, id=None):
        return self.destroy(request, id)


class QuestionFilter(FilterSet):
    title = filters.CharFilter('title')

    class Meta:
        model = Question
        fields = ('title', 'status')


class FilterSortSearch(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = (DjangoFilterBackend,OrderingFilter, SearchFilter)
    # filter_fields = ('title', 'status')
    filter_class = QuestionFilter
    ordering_fields = ('title', )
    ordering = ('title', )
    search_fields = ('title', )


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = EmployeeSerializer

