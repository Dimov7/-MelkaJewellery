from MelkaJewellery.common.forms import ContactPageForm
from MelkaJewellery.common.models import ContactPageModel
from MelkaJewellery.jewels.models import Jewels, Collection
from django.views.generic import ListView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django.views.generic import CreateView

UserModel = get_user_model()


class IndexPage(ListView):
    template_name = 'index.html'
    model = Jewels
    context_object_name = 'jewellery'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['collection'] = Collection.objects.all()
        return context


class ContactPage(LoginRequiredMixin, CreateView):
    template_name = 'contact.html'
    model = ContactPageModel
    form_class = ContactPageForm
    success_url = reverse_lazy('index')