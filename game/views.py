from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.views import generic

from .models import Quiz, Question, Answer


class IndexView(generic.ListView):
    template_name = 'game/index.html'

    def get_queryset(self):
        """Return all quizzes."""
        return Quiz.objects.all()


class QuizView(generic.ListView):
    template_name = 'game/quiz.html'

    def get_queryset(self):
        return Question.objects.filter(quiz=self.kwargs['pk'])


class QuestionView(generic.DetailView):
    model = Question
    template_name = 'game/question.html'


def outcome(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    inputted_answer = request.POST['answer'].lower()
    correct_answers_set = question.answer_set.all()
    correct_answers = [{x.answer_text.lower(): x.score}
                       for x in correct_answers_set]
    for x in correct_answers:
        if inputted_answer in x.keys():
            return render(request, 'game/outcome.html', {'score': x[inputted_answer]})
    return render(request, 'game/outcome.html', {'score': 'WRONG'})
