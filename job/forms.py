from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Reset, MultiField,\
    Div
from crispy_forms.bootstrap import PrependedText, AppendedText, FormActions
from django import forms
from django.forms import ModelForm

from job.models import Company

class RegisterForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.form_method = 'post'

        self.helper.form_class = 'form-signin pt-5'
        self.helper.label_class = 'text-muted'
        self.helper.field_class = 'col-lg-12'

        self.helper.layout = Layout(
            Fieldset('', 'email', 'password',),
            FormActions(
                Submit('submit', 'Зарегистрироваться'),
            )
        )


class ApplicationForm(forms.Form):

    name = forms.CharField(label='Ваше имя:', required=False)
    phone = forms.CharField(label='Ваш телефон:', required=False)
    text = forms.CharField(widget=forms.Textarea, label='О себе:')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.form_class = 'card-body mx-3'
        self.helper.label_class = 'mb-1 mt-2'
        self.helper.field_class = 'form-group'

        self.helper.layout = Layout(
            Fieldset('', 'name', 'phone', 'text'),
            FormActions(
                Submit('submit', 'Отправить'),
            )
        )


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        exclude = []
        fields = ['name', 'location', 'logo', 'description', 'employee_count',
                  'owner']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.form_class = ''
        self.helper.label_class = 'mb-1 mt-2'
        self.helper.field_class = 'form-group'

        self.helper.layout = Layout(
            Div(
                Div('name', css_class='col-6'),
                Div('logo', css_class='col-6'),
                css_class='row'),
            Div(
                Div('employee_count', css_class='col-6'),
                Div('location', css_class='col-6'),
                css_class='row'),
            'description',
            'owner',
            FormActions(
                Submit('submit', 'Записать'),
            )
        )
