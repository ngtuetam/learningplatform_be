from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    short_description = models.TextField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
        
class Course(models.Model):
    categories = models.ManyToManyField(Category)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    short_description = models.TextField(blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    DRAFT = "draft"
    PUBLISHED = "published"

    STATUS_CHOICES = [
        (DRAFT, "Draft"),
        (PUBLISHED, "Published")
    ]

    ARTICLE = 'article'
    QUIZ = 'quiz'
    EXAM_PREP = 'exam_prep'

    LESSON_TYPE_CHOICES = [
        (ARTICLE, 'Article'),
        (QUIZ, 'quiz'),
        (EXAM_PREP, 'exam_prep')
    ]

    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    short_description = models.TextField(blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PUBLISHED)
    lesson_type = models.CharField(max_length=20, choices=LESSON_TYPE_CHOICES, default=ARTICLE)

    def __str__(self):
        return self.title



