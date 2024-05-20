from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from .models import Poste, User, Recommandation, Evenement, EvenClub, EvenSocial, Transport, Logement, Stage
from .models import Reaction
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import TransportForm, EvenementForm, RecommandationForm, StageForm, LogementForm, EventSocialForm, PosteForm, EvenClubForm, CommentForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


def index(request):
    return HttpResponse("run application")


def profile(request):
    posts = Poste.objects.all()
    evenement_form = EvenementForm()
    even_club_form = EvenClubForm()
    transport_form = TransportForm()
    recommandation_form = RecommandationForm()
    stage_form = StageForm()
    logement_form = LogementForm()
    return render(request, 'profile.html', {
        'posts': posts,
        'evenement_form': evenement_form,
        'even_club_form': even_club_form,
        'transport_form': transport_form,
        'recommandation_form': recommandation_form,
        'stage_form': stage_form,
        'logement_form': logement_form,
    })


@login_required
def home(request):
    posts = Poste.objects.all()
    evenement_form = EvenementForm()
    even_club_form = EvenClubForm()
    transport_form = TransportForm()
    recommandation_form = RecommandationForm()
    stage_form = StageForm()
    logement_form = LogementForm()
    return render(request, 'home.html', {
        'posts': posts,
        'evenement_form': evenement_form,
        'even_club_form': even_club_form,
        'transport_form': transport_form,
        'recommandation_form': recommandation_form,
        'stage_form': stage_form,
        'logement_form': logement_form,
    })


def offre(request):
    posts = Poste.objects.all()
    evenement_form = EvenementForm()
    even_club_form = EvenClubForm()
    transport_form = TransportForm()
    recommandation_form = RecommandationForm()
    stage_form = StageForm()
    logement_form = LogementForm()
    return render(request, 'offre.html', {
        'posts': posts,
        'evenement_form': evenement_form,
        'even_club_form': even_club_form,
        'transport_form': transport_form,
        'recommandation_form': recommandation_form,
        'stage_form': stage_form,
        'logement_form': logement_form, })


def demmandes(request):
    posts = Poste.objects.all()
    evenement_form = EvenementForm()
    even_club_form = EvenClubForm()
    transport_form = TransportForm()
    recommandation_form = RecommandationForm()
    stage_form = StageForm()
    logement_form = LogementForm()
    return render(request, 'demandes.html', {
        'posts': posts,
        'evenement_form': evenement_form,
        'even_club_form': even_club_form,
        'transport_form': transport_form,
        'recommandation_form': recommandation_form,
        'stage_form': stage_form,
        'logement_form': logement_form, })


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, user)
            messages.success(request, f'Coucou {user.username}, Votre compte a été créé avec succès !')
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('index')


def choix(request):
    return render(request, 'choix.html')


def eventClub(request):
    if request.method == 'POST':
        form = EvenClubForm(request.POST, request.FILES)
        if form.is_valid():
            eventClub_instance = form.save(commit=False)
            eventClub_instance.uc = request.user
            eventClub_instance.save()
            form.save()
            return redirect('home')
    else:
        form = EvenClubForm()

    return render(request, 'eventClub.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                pass
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


def transport(request):
    if request.method == 'POST':
        form = TransportForm(request.POST, request.FILES)
        if form.is_valid():
            transport_instance = form.save(commit=False)
            transport_instance.uc = request.user
            transport_instance.save()
            return redirect('home')
    else:
        form = TransportForm()

    return render(request, 'transport.html', {'form': form})


def recommandation(request):
    if request.method == 'POST':
        form = RecommandationForm(request.POST, request.FILES)
        if form.is_valid():
            recommandation_instance = form.save(commit=False)
            recommandation_instance.uc = request.user
            recommandation_instance.save()
            form.save()

            return redirect('home')
    else:
        form = RecommandationForm()

    return render(request, 'recommandation.html', {'form': form})


def post(request):
    if request.method == 'POST':
        form = PosteForm(request.POST, request.FILES)
        if form.is_valid():
            poste_instance = form.save(commit=False)
            poste_instance.uc = request.user
            poste_instance.save()
            form.save()
            return redirect('home')
    else:
        form = PosteForm()
    return render(request, 'post.html', {'form': form})


def eventSocial(request):
    if request.method == 'POST':
        form = EventSocialForm(request.POST, request.FILES)
        if form.is_valid():
            eventSocial_instance = form.save(commit=False)
            eventSocial_instance.uc = request.user
            eventSocial_instance.save()
            return redirect('home')
    else:
        form = EventSocialForm()

    return render(request, 'eventSocial.html', {'form': form})


def stage(request):
    if request.method == 'POST':
        form = StageForm(request.POST, request.FILES)
        if form.is_valid():
            stage_instance = form.save(commit=False)
            stage_instance.uc = request.user
            stage_instance.save()
            return redirect('home')
    else:
        form = StageForm()

    return render(request, 'stage.html', {'form': form})


def logement(request):
    if request.method == 'POST':
        form = LogementForm(request.POST, request.FILES)
        if form.is_valid():
            logement_instance = form.save(commit=False)
            logement_instance.uc = request.user
            logement_instance.save()
            return redirect('home')
    else:
        form = LogementForm()

    return render(request, 'logement.html', {'form': form})


def evenemnt(request):
    if request.method == 'POST':
        form = EvenementForm(request.POST, request.FILES)
        if form.is_valid():
            evenemnt_instance = form.save(commit=False)
            evenemnt_instance.uc = request.user
            evenemnt_instance.save()
            return redirect('home')
    else:
        form = EvenementForm()

    return render(request, 'evenemnt.html', {'form': form})


def Notif(request):
    posts = Poste.objects.all()
    evenement_form = EvenementForm()
    even_club_form = EvenClubForm()
    transport_form = TransportForm()
    recommandation_form = RecommandationForm()
    stage_form = StageForm()
    logement_form = LogementForm()
    return render(request, 'Notification.html', {
        'posts': posts,
        'evenement_form': evenement_form,
        'even_club_form': even_club_form,
        'transport_form': transport_form,
        'recommandation_form': recommandation_form,
        'stage_form': stage_form,
        'logement_form': logement_form, })


class ModifierPoste(UpdateView):

    model = Poste

    template_name = 'Modifier_Poste.html'

    form_class = PosteForm

    success_url = reverse_lazy('profile')


class SupprimerPoste(DeleteView):

    model = Poste

    template_name = 'Supprimer_Poste.html'

    success_url = reverse_lazy('profile')


class ModifierRecommandation(UpdateView):

    model = Recommandation

    template_name = 'Modifier_Recommandation.html'

    form_class = RecommandationForm

    success_url = reverse_lazy('profile')


class SupprimerRecommandation(DeleteView):

    model = Recommandation

    template_name = 'Supprimer_Recommandation.html'

    success_url = reverse_lazy('profile')


class ModifierEvenement(UpdateView):

    model = Evenement

    template_name = 'Modifier_Evenement.html'

    form_class = EvenementForm

    success_url = reverse_lazy('profile')


class DetailRecommandation(DetailView):
    model = Recommandation
    template_name = 'Drec.html'
    context_object_name = 'post'


class SupprimerEvenement(DeleteView):

    model = Evenement
    template_name = 'Supprimer_Evenement.html'
    success_url = reverse_lazy('profile')


class ModifierEvenClub(UpdateView):

    model = EvenClub
    template_name = 'Modifier_EvenClub.html'
    form_class = EvenClubForm
    success_url = reverse_lazy('profile')


class SupprimerEvenClub(DeleteView):

    model = EvenClub
    template_name = 'Supprimer_EvenClub.html'
    success_url = reverse_lazy('profile')


class ModifierEvenSocial(UpdateView):

    model = EvenSocial
    template_name = 'Modifier_EvenSocial.html'
    form_class = EventSocialForm
    success_url = reverse_lazy('profile')


class SupprimerEvenSocial(DeleteView):

    model = EvenSocial
    template_name = 'Supprimer_EvenSocial.html'
    success_url = reverse_lazy('profile')


class ModifierTransport(UpdateView):

    model = Transport
    template_name = 'Modifier_Transport.html'
    form_class = TransportForm
    success_url = reverse_lazy('profile')


class SupprimerTransport(DeleteView):

    model = Transport

    template_name = 'Supprimer_Transport.html'

    success_url = reverse_lazy('profile')


class ModifierLogement(UpdateView):

    model = Logement

    template_name = 'Modifier_Logement.html'

    form_class = LogementForm

    success_url = reverse_lazy('profile')


class SupprimerLogement(DeleteView):

    model = Logement

    template_name = 'Supprimer_Logement.html'

    success_url = reverse_lazy('profile')


class ModifierStage(UpdateView):

    model = Stage

    template_name = 'Modifier_Stage.html'

    form_class = StageForm

    success_url = reverse_lazy('profile')


class SupprimerStage(DeleteView):

    model = Stage

    template_name = 'Supprimer_Stage.html'

    success_url = reverse_lazy('profile')


class Addcomment(CreateView):
    model = Reaction
    form_class = CommentForm
    template_name = 'add_comment.html'

    def form_valid(self, form):
        form.instance.users = self.request.user
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('home')
