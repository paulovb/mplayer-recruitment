from django import forms


class RecruitmentForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    mail = forms.EmailField(max_length=255, required=True)
    comp_html = forms.IntegerField(required=False)
    comp_css = forms.IntegerField(required=False)
    comp_javascript = forms.IntegerField(required=False)
    comp_python = forms.IntegerField(required=False)
    comp_django = forms.IntegerField(required=False)
    comp_ios = forms.IntegerField(required=False)
    comp_android = forms.IntegerField(required=False)