from django import forms

from flatblocks.models import FlatBlock
from tinymce.widgets import TinyMCE

class FlatBlockForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 16}))

    class Meta:
        model = FlatBlock
        exclude = ('slug', )
