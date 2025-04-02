from django import forms  
JOBS=(
    ("python","Développeur python"),
    ("javaScript","Développeur JavaScript"),
    ("csharp","Développeur C#"),
)



class signupForms(forms.Form):
    pseudo=forms.CharField(max_length=8, required=False, strip=False,widget=forms.Textarea)
    email=forms.EmailField()
    password=forms.CharField(min_length=8,widget=forms.PasswordInput)
    job=forms.ChoiceField(choices=JOBS, widget=forms.RadioSelect)
    cug_accept=forms.BooleanField(initial=True)
