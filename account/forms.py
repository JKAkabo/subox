from django import forms

from .models import Saving, Withdrawal

class SavingForm(forms.ModelForm):
    class Meta:
        model = Saving
        fields = ('amount', )


class WithdrawalForm(forms.ModelForm):
    class Meta:
        model = Withdrawal
        fields = ('amount', )
