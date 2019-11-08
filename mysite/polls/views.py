from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Question
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'


    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or-404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        #Vuelva a mostrar el formulario de votación de preguntas.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "No seleccionaste una opción.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Siempre devuelve un HttpResponseRedirect después de tratar con éxito
        # con datos POST. Esto evita que los datos se publiquen dos veces si un
        # usuario presiona el botón Atrás.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
