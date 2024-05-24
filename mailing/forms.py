from django.forms import ModelForm, BooleanField, forms, DateTimeInput

from mailing.models import Client, Message, SubscribeSettings


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ClientForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Client
        fields = ('email', 'fio', 'comment')


class MessageForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Message
        fields = ('title', 'text')


class SubscribeForm(StyleFormMixin, ModelForm):
    class Meta:
        model = SubscribeSettings
        # fields = '__all__'
        fields = ('start_time', 'end_time', 'frequency', 'message', 'client')

        widgets = {
            "start_time": DateTimeInput(attrs={"placeholder": "ДД.ММ.ГГГГ ЧЧ:ММ:СС", "type": "datetime-local"}),
            "end_time": DateTimeInput(attrs={"placeholder": "ДД.ММ.ГГГГ ЧЧ:ММ:СС", "type": "datetime-local"}),
        }


class SubscribeManagerForm(ModelForm):
    class Meta:
        model = SubscribeSettings
        fields = ('is_active',)
