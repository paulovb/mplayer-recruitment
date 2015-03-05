from django import forms


class RecruitmentForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    mail = forms.EmailField(required=True)

    has_html = forms.BooleanField(required=False)
    comp_html = forms.IntegerField(required=False)
    has_css = forms.BooleanField(required=False)
    comp_css = forms.IntegerField(required=False)
    has_javascript = forms.BooleanField(required=False)
    comp_javascript = forms.IntegerField(required=False)
    has_python = forms.BooleanField(required=False)
    comp_python = forms.IntegerField(required=False)
    has_django = forms.BooleanField(required=False)
    comp_django = forms.IntegerField(required=False)
    has_ios = forms.BooleanField(required=False)
    has_ios = forms.IntegerField(required=False)
    has_android = forms.BooleanField(required=False)
    comp_android = forms.IntegerField(required=False)