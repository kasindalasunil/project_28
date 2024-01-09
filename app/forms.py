from django import forms

from app.models import *

class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'
        


class WebpageForm(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'
        #specific columns which are required
        #fields=['topic_name','name','url']
        #except that everything will display
        #exclude=['email']
        #labels are used to change the column name
        #labels={'topic_name':'tn'}
        #widgets used to change the type 
        #widgets={'topic_name':forms.PasswordInput()}



        
class AccessRecordForm(forms.ModelForm):
    class Meta:
        model=AccessRecord
        fields='__all__'

