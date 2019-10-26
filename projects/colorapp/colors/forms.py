from django import forms
from colors.validation import colormaps_valid_aligned


class GetHexForm(forms.Form):
    colormap = forms.ChoiceField(choices=[(x, x) for x in colormaps_valid_aligned], help_text="Select a Matlab color gradient.", initial='viridis')
    flip = forms.BooleanField(help_text='Check to flip the gradient', required=False)
    n = forms.IntegerField(help_text="Input number of desired buckets.", min_value=0, max_value=1000, initial='5')
