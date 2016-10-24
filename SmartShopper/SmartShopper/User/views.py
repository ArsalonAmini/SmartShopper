from django.http import HttpResponse
from django.template import loader
from .models import SignUp
# Create your views here.



def index(request):
    all_SignUp = SignUp.objects.all()
    template = loader.get_template('index.html')
    context = {
        'all_SignUp': all_SignUp,
        }
    return HttpResponse(template.render(context, request))


def detail(request, SignUp_id):
    return HttpResponse("<h2>details for signup id:" +str(SignUp_id) + "</h2>")



#class UserFormView():
#    form_class = UserForm 
#    template_name = 'registration_form.html'

#    #display blank for to user
#    def get(self, request):
#        form = self.form_class(None)
#        return render(request, self.template_name, {'form': form})
        

#    # process form data 
#    def post(self, request):
#        form = self.form_class(request.POST)

#        if form.is_valid():

#            user = form.save(commit=False) 

#            #clean (normalized) data 
#            username = form.cleaned_data['username']
#            username = form.cleaned_data['password']
#            user.set_password(password)
#            user.save() 

#            # returns User objects if credentials are correct
#            user = authenticate(username=username, password=password) 

#            if user is not None:
                
#                if user.is_active:
#                    login(request, user)
#                    return redirect ('app/index.html')


#        return render(request, self.template_name, {'form': form})