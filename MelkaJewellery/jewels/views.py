from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View

from MelkaJewellery.common.forms import SearchForm
from MelkaJewellery.jewels.forms import JewelsCreateForm, JewelCollectionForm
from MelkaJewellery.jewels.models import Jewels, Collection, SeasonsJewel, CategoryJewel, CollectionJewel
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin

from django.core.paginator import Paginator
from django.views.generic import DetailView

UserModel = get_user_model()


class ShopPageView(LoginRequiredMixin, ListView):
    template_name = 'shop.html'
    model = Jewels
    context_object_name = 'jewellery'
    paginate_by = 3

    def get_queryset(self):
        queryset = Jewels.objects.all()

        season_param = self.request.GET.get('season')
        if season_param:
            queryset = queryset.filter(season_jewel__season=season_param)

        type_param = self.request.GET.get('type')
        if type_param:
            queryset = queryset.filter(type__type=type_param)

        collection_param = self.request.GET.get('collection')
        if collection_param:
            queryset = queryset.filter(collection__collection=collection_param)

        sort_param = self.request.GET.get('sort')
        if sort_param == 'price_asc':
            queryset = queryset.order_by('collection__price')
        elif sort_param == 'price_desc':
            queryset = queryset.order_by('-collection__price')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['collection'] = Collection.objects.all()

        context['seasons'] = SeasonsJewel.objects.all()
        context['selected_season'] = self.request.GET.get('season')

        context['types'] = CategoryJewel.objects.all()
        context['selected_type'] = self.request.GET.get('type')

        context['collection_jewel'] = CollectionJewel.objects.all()
        context['selected_collection_jewel'] = self.request.GET.get('collection')

        context['search_form'] = SearchForm(self.request.GET)

        context['sort'] = self.request.GET.get('sort', '')

        queryset = self.get_queryset()
        paginator = Paginator(queryset, self.paginate_by)
        page = self.request.GET.get('page', 1)
        page_obj = paginator.get_page(page)

        context['jewellery'] = page_obj
        context['total_results'] = paginator.count
        context['start_index'] = page_obj.start_index()
        context['end_index'] = page_obj.end_index()

        return context


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Jewels
    template_name = 'shop-details.html'
    context_object_name = 'detail_jewel'


class CreateJewelView(View):
    def get(self, request, *args, **kwargs):
        jewel_form = JewelsCreateForm()
        collection_form = JewelCollectionForm()

        return render(request, 'jewels/create-jewel.html', {
            'jewel_form': jewel_form,
            'collection_form': collection_form
        })

    def post(self, request, *args, **kwargs):
        jewel_form = JewelsCreateForm(request.POST, request.FILES)
        collection_form = JewelCollectionForm(request.POST)

        if jewel_form.is_valid() and collection_form.is_valid():
            collection = collection_form.save()

            jewel = jewel_form.save(commit=False)
            jewel.collection = collection
            jewel.save()

            return redirect('index')

        return render(request, 'jewels/create-jewel.html', {
            'jewel_form': jewel_form,
            'collection_form': collection_form
        })


class JewelCollectionEditView(UpdateView):
    template_name = 'jewels/edit-jewel.html'
    model = Jewels
    form_class = JewelCollectionForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        jewel = self.object
        collection = jewel.collection

        context['jewel_form'] = self.get_form()

        if 'collection_form' not in context:
            context['collection_form'] = JewelCollectionForm(instance=collection)

        return context

    def post(self, request, *args, **kwargs):

        self.object = self.get_object()
        jewel_form = self.get_form()
        collection_form = JewelCollectionForm(
            request.POST, instance=self.object.collection)

        if jewel_form.is_valid() and collection_form.is_valid():
            collection_form.save()
            jewel_form.save()
            return self.form_valid(jewel_form)

        return self.form_invalid(jewel_form, collection_form)

    def form_invalid(self, jewel_form, collection_form):

        return self.render_to_response(
            self.get_context_data(
                jewel_form=jewel_form, collection_form=collection_form
            )
        )


class JewelDeleteView(DeleteView):
    model = Jewels
    template_name = 'jewels/delete-jewel.html'
    success_url = reverse_lazy('index')
