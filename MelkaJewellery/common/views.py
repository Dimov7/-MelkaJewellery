from MelkaJewellery.accounts.models.profile import Profile
from MelkaJewellery.common.forms import ContactPageForm, EmailFieldForm, AccountCreationForm, CustomLoginForm, \
    ProfileEditForm
from MelkaJewellery.common.models import ContactPageModel, EmailFieldModel, ShopPageModel
from MelkaJewellery.jewels.models import Jewels, Collection
from django.views.generic import ListView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

UserModel = get_user_model()

class AccountCreateView(CreateView):
    form_class = AccountCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form = super().form_valid(form)

        return form


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'profile-details.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return Profile.objects.get(pk=self.request.user.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['user'] = context['profile'].user

        return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = 'profile-edit.html'
    form_class = ProfileEditForm
    success_url = reverse_lazy('profile-details')

    def get_object(self, queryset=None):
        return Profile.objects.get(pk=self.request.user.pk)


class AccountDeleteView(LoginRequiredMixin, DeleteView):
    model = UserModel
    success_url = reverse_lazy('index')
    template_name = 'profile-delete.html'

    def get_object(self, queryset=None):
        return UserModel.objects.get(pk=self.request.user.pk)


class IndexPage(LoginRequiredMixin, ListView):
    template_name = 'index.html'
    model = Jewels
    context_object_name = 'jewellery'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['collection'] = Collection.objects.all()
        context['email_form'] = EmailFieldForm()
        return context


class ContactPage(LoginRequiredMixin, CreateView):
    template_name = 'contact.html'
    model = ContactPageModel
    form_class = ContactPageForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['email_form'] = EmailFieldForm()
        return context


class EmailFieldFooter(LoginRequiredMixin, CreateView):
    model = EmailFieldModel
    form_class = EmailFieldForm
    success_url = reverse_lazy('index')
    template_name = 'base.html'


class ShopPageView(LoginRequiredMixin, ListView):
    template_name = 'shop.html'
    model = ShopPageModel
