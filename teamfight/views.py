from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.db import transaction
from django.contrib import messages
from django.views import generic

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

import datetime
# Create your views here.

def TeamFightIndexView(request):

    context = {"a": "b"}
    return render(request, 'teamfight_index.html', context=context)