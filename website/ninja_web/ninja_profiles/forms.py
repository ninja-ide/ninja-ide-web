
from django.forms import ModelForm
from ninja_profiles.models import NinjaProfile
 
class NinjaProfileForm(ModelForm):
  class Meta:
      model = NinjaProfile
      exclude = ('user', 'score',)
