from django.shortcuts import render

from .forms import SavingForm, WithdrawalForm


def add_saving(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'saving/add')