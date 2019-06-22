from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView, UpdateView, CreateView

from .forms import AddressCountryForm, AddressProvinceForm, AddressZoneForm, AddressDistrictForm, \
    AddressVDCMunicipalityForm, InstitutionForm, MemberForm
from .models import AddressCountry, AddressProvince, AddressZone, AddressDistrict, AddressVDCMunicipality, Institution, \
    Member


class AddressCountryListView(ListView):
    model = AddressCountry


class AddressCountryCreateView(CreateView):
    model = AddressCountry
    form_class = AddressCountryForm


class AddressCountryDetailView(DetailView):
    model = AddressCountry


class AddressCountryUpdateView(UpdateView):
    model = AddressCountry
    form_class = AddressCountryForm


class AddressProvinceListView(ListView):
    model = AddressProvince


class AddressProvinceCreateView(CreateView):
    model = AddressProvince
    form_class = AddressProvinceForm


class AddressProvinceDetailView(DetailView):
    model = AddressProvince


class AddressProvinceUpdateView(UpdateView):
    model = AddressProvince
    form_class = AddressProvinceForm


class AddressZoneListView(ListView):
    model = AddressZone


class AddressZoneCreateView(CreateView):
    model = AddressZone
    form_class = AddressZoneForm


class AddressZoneDetailView(DetailView):
    model = AddressZone


class AddressZoneUpdateView(UpdateView):
    model = AddressZone
    form_class = AddressZoneForm


class AddressDistrictListView(ListView):
    model = AddressDistrict


class AddressDistrictCreateView(CreateView):
    model = AddressDistrict
    form_class = AddressDistrictForm


class AddressDistrictDetailView(DetailView):
    model = AddressDistrict


class AddressDistrictUpdateView(UpdateView):
    model = AddressDistrict
    form_class = AddressDistrictForm


class AddressVDCMunicipalityListView(ListView):
    model = AddressVDCMunicipality


class AddressVDCMunicipalityCreateView(CreateView):
    model = AddressVDCMunicipality
    form_class = AddressVDCMunicipalityForm


class AddressVDCMunicipalityDetailView(DetailView):
    model = AddressVDCMunicipality


class AddressVDCMunicipalityUpdateView(UpdateView):
    model = AddressVDCMunicipality
    form_class = AddressVDCMunicipalityForm


class InstitutionListView(ListView):
    model = Institution


class InstitutionCreateView(CreateView):
    model = Institution
    form_class = InstitutionForm


class InstitutionDetailView(DetailView):
    model = Institution


class InstitutionUpdateView(UpdateView):
    model = Institution
    form_class = InstitutionForm


class MemberListView(ListView):
    model = Member


class MemberCreateView(CreateView):
    model = Member
    form_class = MemberForm


class MemberDetailView(DetailView):
    model = Member


class MemberUpdateView(UpdateView):
    model = Member
    form_class = MemberForm
