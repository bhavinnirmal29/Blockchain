from django import forms


class BlockForm(forms.Form):
    data = forms.CharField(label='Data', max_length=100)