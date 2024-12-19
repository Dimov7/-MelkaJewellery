from django.contrib.auth import get_user_model

from MelkaJewellery.accounts.forms import AccountCreationForm, CustomLoginForm, ProfileEditForm
from MelkaJewellery.accounts.models.profile import Profile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

UserModel = get_user_model()


class AccountCreateView(CreateView):
    form_class = AccountCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form = super().form_valid(form)

        return form


class CustomLoginView(LoginView):
    form_class = CustomLoginForm


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'registration/profile-details.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return Profile.objects.get(pk=self.request.user.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['user'] = context['profile'].user

        return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = 'registration/profile-edit.html'
    form_class = ProfileEditForm
    success_url = reverse_lazy('profile-details')

    def get_object(self, queryset=None):
        return Profile.objects.get(pk=self.request.user.pk)


class AccountDeleteView(LoginRequiredMixin, DeleteView):
    model = UserModel
    success_url = reverse_lazy('index')
    template_name = 'registration/profile-delete.html'

    def get_object(self, queryset=None):
        return UserModel.objects.get(pk=self.request.user.pk)
