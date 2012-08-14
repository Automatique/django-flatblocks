from django import forms

from flatblocks.models import FlatBlock
from tinymce.widgets import TinyMCE

class FlatBlockForm(forms.ModelForm):
    class Meta:
        model = FlatBlock
        exclude = ('slug', )

class FlatBlockAdminForm(forms.ModelForm):
    header = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 2}), required=False)
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 16}), required=False)

    class Meta:
        model = FlatBlock