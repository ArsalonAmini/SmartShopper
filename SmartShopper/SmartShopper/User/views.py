from django.shortcuts import render

# Create your views here.

class UserFormView():
    form_class = UserForm 
    template_name = 'registration_form.html'

    #display blank for to user
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})
        

    # process form data 
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False) 

            #clean (normalized) data 
            username = form.cleaned_data['username']
            username = form.cleaned_data['password']
            user.set_password(password)
            user.save() 