from django import forms

from flatblocks.models import FlatBlock
from tinymce.widgets import TinyMCE

class FlatBlockForm(forms.ModelForm):
    class Meta:
        model = FlatBlock
        exclude = ('slug', )

class FlatBlockAdminForm(forms.ModelForm):
    header = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 2}))
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 16}))

    class Meta:
        model = FlatBlock
        exclude = ('slug', )