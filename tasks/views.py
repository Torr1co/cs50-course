from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

tasks = []
# Create your views here.
class NewTaskform(forms.Form):
	task = forms.CharField(label = "New task")
	priority = forms.IntegerField(label = "Priority", min_value=1, max_value=8)


def index(request):
	if 'tasks' not in request.session:
		request.session['tasks'] = []
	return render(request, "tasks/index.html", {
		"tasks":tasks
		})

def add(request):
	if request.method == "POST":
		form = NewTaskform(request.POST)
		if form.is_valid():
			task = form.cleaned_data["task"]
			request.session['tasks'] += [task]
			return HttpResponseRedirect(reverse("tasks:tasks"))
		else:
			return render(request, 'tasks/add.html', {
				"form":form
				})


	return render(request, 'tasks/add.html', {
		"form":NewTaskform()
		})
