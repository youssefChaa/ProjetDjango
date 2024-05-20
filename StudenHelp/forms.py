from django.forms import ModelForm, CharField, PasswordInput
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Poste, Evenement, tp, ts, EvenClub, EvenSocial, Stage, Logement, Transport, Recommandation, Reaction


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.form_class = 'login-form'
    helper.form_show_labels = False
    helper.add_input(Submit('submit', 'Se connecter', css_class='btn-primary'))


class UserRegistrationForm(UserCreationForm):
    nom = forms.CharField(max_length=50)
    prenom = forms.CharField(label='Prenom')
    email = forms.EmailField(label='Adresse e-mail')
    telephone = forms.CharField(max_length=20)
    helper = FormHelper()
    helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
    helper.form_method = 'POST'


class PosteForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_method = 'POST'

    helper.add_input(Submit('submit', 'Valider', css_class='btn-primary'))

    class Meta:
        model = Poste
        fields = ['image', 'type']


class EvenClubForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_method = 'POST'

    helper.add_input(Submit('submit', 'Valider', css_class='btn-primary'))

    class Meta:
        model = EvenClub
        fields = ['intitule', 'description', 'lieu', 'contactinfo', 'club', 'image', 'type']


class EvenementForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_method = 'POST'

    helper.add_input(Submit('submit', 'Valider', css_class='btn-primary'))

    class Meta:
        model = Evenement
        fields = ['intitule', 'description', 'lieu', 'contactinfo', 'image', 'type']


class TransportForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_method = 'POST'

    helper.add_input(Submit('submit', 'Valider', css_class='btn-primary'))

    class Meta:
        model = Transport
        fields = ['depart', 'destination', 'heure_dep', 'nbre_sieges', 'contactinfo', 'image', 'type']


class RecommandationForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_method = 'POST'

    helper.add_input(Submit('submit', 'Valider', css_class='btn-primary'))

    class Meta:
        model = Recommandation
        fields = ['text', 'image', 'type']


class EventSocialForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_method = 'POST'

    helper.add_input(Submit('submit', 'Valider', css_class='btn-primary'))

    class Meta:
        model = EvenSocial
        fields = ['prix', 'intitule', 'description', 'lieu', 'contactinfo', 'image', 'type']


class StageForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_method = 'POST'

    helper.add_input(Submit('submit', 'Valider', css_class='btn-primary'))

    class Meta:
        model = Stage
        fields = ['specialite', 'typestg', 'societe', 'sujet', 'contactinfo', 'duree', 'image', 'type']


class LogementForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_method = 'POST'

    helper.add_input(Submit('submit', 'Valider', css_class='btn-primary'))

    class Meta:
        model = Logement
        fields = ['image', 'type', 'localisation', 'description', 'contactinfo']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Reaction
        fields = ('comment', 'like')
