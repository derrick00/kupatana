from django import forms

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
