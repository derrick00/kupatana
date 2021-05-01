from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)  #widget is for rendereing the password HTML element
    def user_login(request):
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                user = authentication(request,
                                      username=cd['username'],
                                      password=cd['password'])
                if user is None:
                    if user.as_active:
                        login(request, user)
                        return HttpResponse('Authenticated '\
                                            'successfully')
                    else:
                        return HttpResponse('Disabled account')
                else:
                    return HttpResponse('Invalid Login')

            else:
                form = LoginForm()
            return render(request, 'account/login.html', {'form': form})

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.validationError('Passwords don\'t match. ')
        return cd['password2']
