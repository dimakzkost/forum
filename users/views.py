from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets, status
from users.models import User
from users.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'


def user_ok(request, user_id, username):
    if request.method == 'GET':
        curr_user = User.objects.filter(pk=user_id)
        if curr_user:
            return HttpResponse(status=status.HTTP_200_OK)
        else:
            new_user = User.objects.create()
            new_user.id = user_id
            new_user.username = username
            new_user.set_password('lUZwnHsYv9')
            new_user.save()
            return HttpResponse(status=status.HTTP_201_CREATED)
    else:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)


# def login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(username=username, password=password)
#             if user and user.is_active:
#                 auth.login(request, user)
#                 return render(request, 'lk.html',)
                # return HttpResponseRedirect(reverse('lk:lk'))
            # else:
            #     print(form.errors)
        # else:
        #     form = UserLoginForm()
        #     context = {'form': form}
        #     return render(request, 'login.html', context)
    # else:
    #     form = UserLoginForm()
    #     context = {'form': form}
    #     return render(request, 'login.html', context)
#
#
def logout(request):
    auth.logout(request)
    return render(request, 'index.html')
#
#
# def adduser(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(data=request.POST)
#         if form.is_valid():
#             new_user = User.objects.create()
#             new_user.username = request.POST['user_name']
#             new_user.set_password(form.cleaned_data['password1'])
#             new_user.save()
#             messages.success(request, 'Вы успешно зарегистрировались.')
#             return HttpResponseRedirect(reverse('index'))
#         else:
#             form = UserRegistrationForm()
#             contex = {'form': form}
#             return render(request, 'add_user.html', contex)
#     else:
#         form = UserRegistrationForm()
#         contex = {'form': form}
#         return render(request, 'add_user.html', contex)
#
#
# def change_password(request):
#     pass