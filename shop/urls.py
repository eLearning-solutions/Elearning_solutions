from . import views
from django.urls import path

app_name = 'shop'

urlpatterns = [
    path('', views.CourseList.as_view(), name='home'),
    path('checkout/', views.checkout, name="checkout"),
    path('<slug:slug>/', views.CourseDetail.as_view(), name='course_detail'),

]
