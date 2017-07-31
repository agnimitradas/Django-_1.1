from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse
from django.views import generic

from main.models import QuestionsModel, ChoiceModel


def index(request):
    latest_question_list = QuestionsModel.objects.order_by('-created_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request,'main/index.html',context)


def detail(request, question_id):
    """
    try:
    question = QuestionsModel.objects.get(pk=question_id)
    context = {
        'question': question,
    }
    except QuestionsModel.DoesNotExist:
        raise Http404("Question does not exist")
    """
    question = get_object_or_404(QuestionsModel,pk=question_id)
    choice = ChoiceModel.objects.all().filter(question = question_id)

    context = {
        'question': question,
        'choice': choice,
    }
    print(question)
    print(choice)
    return render(request,'main/details.html',context)


def results(request, question_id):
    votes = ChoiceModel.objects.all().filter(question=question_id)
    context = {
        'votes': votes
    }
    print("votes")
    print(votes)
    return render(request,'main/results.html',context)

def vote(request, question_id):
    choice = get_object_or_404(ChoiceModel, pk=question_id)
    try:
        selected_choice = ChoiceModel.objects.get(pk=request.POST['choice'])
        print(selected_choice)
    except (KeyError, ChoiceModel.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'main/details.html', {
            'question': choice,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('results', args=(choice.id,)))


"""Using Generic Class Detailed View"""
class DetailView(generic.DetailView):
    model = QuestionsModel
    template_name = 'main/details.html'
