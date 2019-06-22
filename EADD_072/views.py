from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from EADD_072.forms import UserRegisterForm, UserUpdateForm
from WebApp.models import Member


def login(request, template_name='registration/login.html',
          redirect_field_name=REDIRECT_FIELD_NAME,
          authentication_form=AuthenticationForm,
          extra_context=None, redirect_authenticated_user=False):
    # warnings.warn(
    #     'The login() view is superseded by the class-based LoginView().',
    #     RemovedInDjango21Warning, stacklevel=2
    # )
    return LoginView.as_view(
        template_name=template_name,
        redirect_field_name=redirect_field_name,
        form_class=authentication_form,
        extra_context=extra_context,
        redirect_authenticated_user=redirect_authenticated_user,
    )(request)


def logout(request, next_page=None,
           template_name='logged_out.html',
           redirect_field_name=REDIRECT_FIELD_NAME,
           extra_context=None):
    # warnings.warn(
    #     'The logout() view is superseded by the class-based LogoutView().',
    #     RemovedInDjango21Warning, stacklevel=2
    # )
    return LogoutView.as_view(
        next_page=next_page,
        template_name=template_name,
        redirect_field_name=redirect_field_name,
        extra_context=extra_context,
    )(request)


_sentinel = object()


def start(request):
    """Start page with a documentation.
    """
    # return render(request,"start.html")
    return render(request, "WebApp/homepage.html")


def editprofile(request):
    if not request.user.is_authenticated:
        return HttpResponse("you are not authenticated", {'error_message': 'Error Message Customize here'})

    post = get_object_or_404(Member, pk=request.user.id)
    if request.method == "POST":

        form = UserUpdateForm(request.POST, request.FILES, instance=post)

        # if request.user.isAdmin:
        #     form = UserUpdateFormForAdmin(request.POST, request.FILES, instance=post)

        if form.is_valid():
            # post.date_last_update = datetime.now()
            post.save()
            return redirect('start')
    else:

        # form = UserUpdateForm(instance=post)
        form = UserUpdateForm(request.POST, request.FILES, instance=post)

        # if request.user.isAdmin == 1:
        #     form = UserUpdateFormForAdmin(instance=post)

    return render(request, 'registration/editprofile.html', {'form': form})


class register(generic.CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('loginsuccess')
    template_name = 'registration/register.html'


def loginsuccess(request):
    return render(request, "registration/registrationsuccessful.html")
