from django.db.models import ForeignKey, CASCADE
from django.forms import ModelForm, CharField, TextInput, DateField, ChoiceField
from django.forms.widgets import DateInput, Select
from .models import Tag, Quote, Author


class TagForm(ModelForm):
    name = CharField(min_length=3, max_length=100, required=True, widget=TextInput())

    class Meta:
        model = Tag
        fields = ['name']


class AuthorForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    fullname = CharField(min_length=3, max_length=25, required=True, widget=TextInput())
    # born_date = DateField(required=True, widget=DateInput()).input_formats  #(format=('%d.%m.%Y'))
    born_date = DateField(required=True) #.input_formats  # (format=('%d.%m.%Y'))
    born_location = CharField(min_length=3, max_length=100, required=True, widget=TextInput())
    bio = CharField(min_length=3, max_length=1000, required=True, widget=TextInput())

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'bio']

        widgets = {'born_date': DateInput(format=('%d.%m.%Y'), attrs={'type': 'date'})}


class QuoteForm(ModelForm):
    quote = CharField(min_length=5, max_length=1000, required=True, widget=TextInput())
    author = ForeignKey(Author, on_delete=CASCADE, null=False, unique=False)
    # author = ForeignKey(AuthorForm)

    class Meta:
        model = Quote
        # fields = "__all__"
        fields = ['quote', 'author']
        exclude = ['tags'] #'authors'

        # widgets = {'author': Select()}