from django.contrib import admin
from .models import User
from .models import Poste
from .models import Recommandation
from .models import Transport
from .models import Logement
from .models import Stage
from .models import Evenement
from .models import EvenClub
from .models import EvenSocial
from .models import Reaction
# Register your models here.

admin.site.register(Poste)
admin.site.register(Recommandation)
admin.site.register(Transport)
admin.site.register(Logement)
admin.site.register(Stage)
admin.site.register(Evenement)
admin.site.register(EvenClub)
admin.site.register(EvenSocial)
admin.site.register(Reaction)
