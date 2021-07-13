
from profiles.models import Profile
from django import forms
from django.core.exceptions import ValidationError
from .models import Expense


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'

    def clean_price(self):
        budget = Profile.objects.first().budget
        budget_left = budget - sum(e.price for e in Expense.objects.all())
        price = float(self.cleaned_data['price'])
        if budget_left < price:
            raise ValidationError('Not enough budget')
        return price


class DeleteExpenseForm(forms.ModelForm):
    title = forms.CharField(disabled=True)
    image_url = forms.URLField(disabled=True)
    description = forms.CharField(widget=forms.TextInput, disabled=True)
    price = forms.FloatField(disabled=True)
    class Meta:
        model = Expense
        fields = '__all__'

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for (_, field) in self.fields.items():
    #         field.widget.attrs['disabled'] = 'disabled'
    
    

