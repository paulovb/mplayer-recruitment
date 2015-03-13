# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from app import tasks
from app.core.recruitment_service import RecruitmentService
from app.form.recruitment_form import RecruitmentForm


def home(request):
    return render_to_response('app/home.html')


def thanks(request):
    return render_to_response('app/thanks.html')


def recruitment(request):
    if request.method == 'POST':
        form = RecruitmentForm(request.POST)

        if form.is_valid():
            RecruitmentService().save(form)
            return HttpResponseRedirect('/thanks/')
    else:
        form = RecruitmentForm()

    return render_to_response(
        'app/recruitment.html', {
            'form': form,
        }
    )