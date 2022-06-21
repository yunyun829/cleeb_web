from django.forms import ModelForm
from cleebweb_app.models import MatchLog


class LogForm(ModelForm):
    class Meta:
        model = MatchLog
        fields = ('legion_name', 'date', 'win_lose', 'attack_target', 'debuff_target', 'front_type', 'absence', 'detail')
