from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Course, Lesson
from .serializers import CourseListSerializer, CourseDetailSerializer, LessonListSerializer


# Create your views here.
@api_view(['GET'])
def get_courses(request):
    courses = Course.objects.all()
    serializers = CourseListSerializer(courses, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def get_course(request, slug):
    course = Course.objects.get(slug=slug)
    course_serializer = CourseDetailSerializer(course)
    lesson_serializer = LessonListSerializer(course.lessons.all(), many=True)

    data = {
        'course': course_serializer.data,
        'lessons': lesson_serializer.data
    }

    return Response(data)