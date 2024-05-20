from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from .views import ModifierPoste, SupprimerPoste, ModifierRecommandation, ModifierEvenement, ModifierEvenClub
from .views import SupprimerRecommandation, SupprimerEvenement, SupprimerEvenClub, SupprimerEvenSocial
from .views import SupprimerTransport, SupprimerStage, DetailRecommandation
from .views import ModifierEvenSocial, ModifierTransport, ModifierLogement, ModifierStage, Addcomment
urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('choix/', views.choix, name='choix'),
    path('eventClub/', views.eventClub, name='eventClub'),
    path('eventSocial/', views.eventSocial, name='eventSocial'),
    path('stage/', views.stage, name='stage'),
    path('logement/', views.logement, name='logement'),
    path('transport/', views.transport, name='transport'),
    path('recommandation/', views.recommandation, name='recommandation'),
    path('evenemnt/', views.evenemnt, name='evenemnt'),
    path('post/', views.post, name='post'),
    path('offre/', views.offre, name='offre'),
    path('Notification/', views.Notif, name='Notification'),

    path('damandes/', views.demmandes, name='demandes'),
    path('<int:pk>/Modifier_Poste/', ModifierPoste.as_view(), name='modifier_Poste'),
    path('<int:pk>/Modifier_Recommandation/', ModifierRecommandation.as_view(), name='modifier_Recommandation'),
    path('<int:pk>/Modifier_Evenement/', ModifierEvenement.as_view(), name='modifier_Evenement'),
    path('<int:pk>/Modifier_EvenClub/', ModifierEvenClub.as_view(), name='modifier_EvenClub'),
    path('<int:pk>/Modifier_EvenSocial/', ModifierEvenSocial.as_view(), name='modifier_EvenSocial'),
    path('<int:pk>/Modifier_Transport/', ModifierTransport.as_view(), name='modifier_Transport'),
    path('<int:pk>/Modifier_Logement/', ModifierLogement.as_view(), name='modifier_Logement'),
    path('<int:pk>/Modifier_Stage/', ModifierStage.as_view(), name='modifier_Stage'),

    path('<int:pk>/Supprimer_Poste/', SupprimerPoste.as_view(), name='supprimer_Poste'),
    path('<int:pk>/Supprimer_Recommandation/', SupprimerRecommandation.as_view(), name='supprimer_Recommandation'),
    path('<int:pk>/Supprimer_Evenement/', SupprimerEvenement.as_view(), name='supprimer_Evenement'),
    path('<int:pk>/Supprimer_EvenClub/', SupprimerEvenClub.as_view(), name='supprimer_EvenClub'),
    path('<int:pk>/Supprimer_EvenSocial/', SupprimerEvenSocial.as_view(), name='supprimer_EvenSocial'),
    path('<int:pk>/Supprimer_Transport/', SupprimerTransport.as_view(), name='supprimer_Transport'),
    path('<int:pk>/Supprimer_Stage/', SupprimerStage.as_view(), name='supprimer_Stage'),
    path('<int:pk>/', DetailRecommandation.as_view(), name='Drec'),
    path('post/<int:pk>/comment', Addcomment.as_view(), name='add_comment')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
