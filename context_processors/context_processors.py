# from account.forms import LoginUser
from django.shortcuts import redirect,render
from django.contrib.auth import authenticate,login
from account.models import User
from django.contrib.auth.models import BaseUserManager
























# def Loginadmin(request):
#     # if request.user.is_authenticated == True:
#     #     return redirect('home:main')
#     if request.method == 'POST':
#         form = LoginUser(data=request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(username=cd['email'],password=cd['password'])
#             if user is not None:
#                 login(request,user)
#                 return {'form': form}
#                 # return redirect('home:main')
#             else:
#                 form.add_error('email','ایمیل وجود ندارد')
#
#         # email = request.POST.get('email')
#         # password = request.POST.get('password')
#         # us = authenticate(request,email=email,password=password)
#         # if us is not None:
#         #     login(request,us)
#         #     return redirect('home:main')
#         # else:
#         #     context['error'].append('یوزر نیم یا پسورد درست نیست')
#         #     return render(request, 'account/login.html',context)
#
#         else:
#             return {'form': form}
#     else:
#         form = LoginUser()
#         return {'form':form}