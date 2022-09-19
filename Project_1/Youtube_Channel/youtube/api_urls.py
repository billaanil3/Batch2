from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('poll/', poll),
    path('poll/<int:id>/', poll_details),
    path('poll_api_view/', Poll.as_view()),
    path('poll_api_view/<int:id>/', PollViewSet.as_view()),
    path('poll_api_generic_view/', PollGenericAPIView.as_view()),
    path('poll_api_generic_view/<int:id>/', PollGenericAPIView.as_view()),
    path('filter_sort_search/', FilterSortSearch.as_view())
    # path('auth/login/', LoginView.as_view()),
    # path('auth/logout/', LogOutView.as_view()),
]