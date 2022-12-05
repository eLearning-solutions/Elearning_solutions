from django.views import generic
from .models import Course


class CourseList(generic.ListView):
    queryset = Course.objects.order_by('-created_on')
    template_name = 'shop/index.html'


class CourseDetail(generic.DetailView):
    model = Course
    template_name = 'shop/course_detail.html'

