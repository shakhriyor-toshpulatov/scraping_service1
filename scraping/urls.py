from django.urls import path

from scraping.views import home_view, VDetail, VCreate, VUpdate, VDelete

urlpatterns = [
    path('detail/<int:pk>/', VDetail.as_view(), name='detail'),
    path('create/', VCreate.as_view(), name='create'),
    path('update/<int:pk>/', VUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', VDelete.as_view(), name='delete'),
    path('', home_view, name='home'),
]
