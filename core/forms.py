from django.forms import ModelForm
from .models import Feedbacks


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedbacks  # model atrelado ao formulário
        fields = '__all__'  # campos a serem utilizados no form
        exclude = ['user', 'clientname', 'companyname']
