from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User



# @login_required
# def home(request):
#     return render(request,'registration/home.html')



class users(LoginRequiredMixin,ListView):
    queryset = User
    template_name = 'registration/home.html'



class Profile(LoginRequiredMixin,ListView):
    template_name = 'registration/users.html'
    paginate_by = 10

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()
        else:
            return User.objects.filter(phone=self.request.user)




class ProfileEdit(LoginRequiredMixin,CreateView):
    model = User
    fields = ['phone','first_name','last_name','password','is_active','is_staff','is_superuser','user_permissions','image']
    template_name = 'registration/EditUser.html'








