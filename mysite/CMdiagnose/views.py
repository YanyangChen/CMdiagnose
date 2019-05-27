from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from .models import Body, Tongue, Person, Cases

class NewDetailView(generic.TemplateView):
    # https://docs.djangoproject.com/en/2.2/ref/class-based-views/generic-editing/#django.views.generic.edit.CreateView
    # model = Person
    template_name = 'CMdiagnose/newdetail.html'

class DetailView(generic.DetailView):
    model = Person
    template_name = 'CMdiagnose/detail.html'


class ResultsView(generic.DetailView):
    model = Person
    template_name = 'CMdiagnose/results.html'

class IndexView(generic.ListView):
    template_name = 'CMdiagnose/index.html'
    context_object_name = 'Person_list'
    def get_queryset(self):
        return Person.objects.all()

def tell(request, person_id):
    the_person = get_object_or_404(Person, pk=person_id)
    try:
        #envalue the Person object's body situation
        the_person.body.general = request.POST['general']
        # the_person = person.get(pk=request.POST['choice'])
    except (KeyError, Person.DoesNotExist):
        # Redisplay the person telling form.
        return render(request, 'CMdiagnose/detail.html', {
            'person': person,
            'error_message': "You didn't submit any symptoms.",
        })
    else:
        caselist=Cases.objects.all()
        the_person.body.result=''
        for case in caselist:
            case.case_check(the_person.body)
        the_person.body.save()
        the_person.tongue.save()
        the_person.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('CMdiagnose:results', args=(the_person.id,)))

def newPerson(request):
    b=Body()
    b.general=request.POST['general']
    b.head=''
    b.head += request.POST['head']
    b.general += b.head
    
    b.save()
    t=Tongue(body=b)
    t.save()
    the_person = Person(body=b,tongue=t)
    try:

        the_person = Person(body=b,tongue=t)
        # the_person.body.general = request.POST['general']
        # the_person = person.get(pk=request.POST['choice'])
    except (KeyError, the_person.DoesNotExist):
        # Redisplay the person telling form.
        return render(request, 'CMdiagnose/detail.html', {
            'person': person,
            'error_message': "You didn't submit any symptoms.",
        })
    else:
        print (the_person.body.general)
        caselist=Cases.objects.all()
        the_person.body.result=''
        for case in caselist:
            case.case_check(the_person.body)
        the_person.body.save()
        the_person.tongue.save()
        the_person.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('CMdiagnose:results', args=(the_person.id,)))

# def index(request):
#     return HttpResponse("欢迎光临笔花医镜电子诊断系统")



