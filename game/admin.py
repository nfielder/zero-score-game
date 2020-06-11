from django.contrib import admin

from .models import Quiz, Question, Answer


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1


class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
