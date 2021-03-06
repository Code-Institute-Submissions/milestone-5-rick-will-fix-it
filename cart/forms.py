from django import forms
from checkout.models import OrderLineItem

class ContributionForm(forms.ModelForm):
    """ Displays minimum amount required."""    
    def __init__(self, *args, **kwargs):
        super(ContributionForm, self).__init__(*args, **kwargs)
        self.fields['contribution'].widget.attrs['min'] = 10.00

    """ Validates the form, if it meets minimum requirement """
    def clean_price(self):
        contribution = self.cleaned_data['contribution']
        if contribution < 10.00:
            raise forms.ValidationError("Contribution cannot be less than €10")
        return contribution
    
    class Meta:
        model = OrderLineItem
        fields = ['contribution',]