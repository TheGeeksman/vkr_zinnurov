from django.forms import ModelForm
from .models import BoardExample


# Create the form class.
class BoardForm(ModelForm):
    class Meta:
        model = BoardExample
        fields = ['board_model', 'photo']
