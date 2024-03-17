from django import forms

class MonthForm(forms.Form):
    selected_date = forms.DateField(
        widget=forms.SelectDateWidget(years=[2024]),
        label='Select a Month in 2024'
    )
