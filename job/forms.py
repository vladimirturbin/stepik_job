from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Reset
from crispy_forms.bootstrap import PrependedText, AppendedText, FormActions
from django import forms


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