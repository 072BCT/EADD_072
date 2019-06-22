from django import forms
from django.contrib import admin

from .models import AddressCountry, AddressProvince, AddressZone, AddressDistrict, AddressVDCMunicipality, Institution, \
    Member


class AddressCountryAdminForm(forms.ModelForm):
    class Meta:
        model = AddressCountry
        fields = '__all__'


class AddressCountryAdmin(admin.ModelAdmin):
    form = AddressCountryAdminForm
    list_display = ['CountryName']
    # readonly_fields = ['CountryName']


admin.site.register(AddressCountry, AddressCountryAdmin)


class AddressProvinceAdminForm(forms.ModelForm):
    class Meta:
        model = AddressProvince
        fields = '__all__'


class AddressProvinceAdmin(admin.ModelAdmin):
    form = AddressProvinceAdminForm
    list_display = ['ProvinceName']
    # readonly_fields = ['ProvinceName']


admin.site.register(AddressProvince, AddressProvinceAdmin)


class AddressZoneAdminForm(forms.ModelForm):
    class Meta:
        model = AddressZone
        fields = '__all__'


class AddressZoneAdmin(admin.ModelAdmin):
    form = AddressZoneAdminForm
    list_display = ['ZoneName']
    # readonly_fields = ['ZoneName']


admin.site.register(AddressZone, AddressZoneAdmin)


class AddressDistrictAdminForm(forms.ModelForm):
    class Meta:
        model = AddressDistrict
        fields = '__all__'


class AddressDistrictAdmin(admin.ModelAdmin):
    form = AddressDistrictAdminForm
    list_display = ['DistrictName']
    # readonly_fields = ['DistrictName']


admin.site.register(AddressDistrict, AddressDistrictAdmin)


class AddressVDCMunicipalityAdminForm(forms.ModelForm):
    class Meta:
        model = AddressVDCMunicipality
        fields = '__all__'


class AddressVDCMunicipalityAdmin(admin.ModelAdmin):
    form = AddressVDCMunicipalityAdminForm
    list_display = ['VDCMunicipalityName']
    # readonly_fields = ['VDCMunicipalityName']


admin.site.register(AddressVDCMunicipality, AddressVDCMunicipalityAdmin)


class InstitutionAdminForm(forms.ModelForm):
    class Meta:
        model = Institution
        fields = '__all__'


class InstitutionAdmin(admin.ModelAdmin):
    form = InstitutionAdminForm
    list_display = ['InstitutionName', 'InstitutionEmail', 'InstitutionPhone', 'InstitutionWebsite',
                    'InstitutionAddressStreet', 'InstitutionNote']
    # readonly_fields = ['InstitutionName', 'InstitutionEmail', 'InstitutionPhone', 'InstitutionWebsite', 'InstitutionAddressStreet', 'InstitutionNote']


admin.site.register(Institution, InstitutionAdmin)


class MemberAdminForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'


class MemberAdmin(admin.ModelAdmin):
    form = MemberAdminForm
    list_display = ['MemberRegistrationID', 'MemberName', 'MemberGender', 'MemberBirthDate', 'MemberFatherName',
                    'MemberPhone', 'MemberVerified', 'MemberRegisterDateTime', 'MemberRegisterAgent', 'MemberNote',
                    'MemberStreetTemporaryAddress', 'MemberStreetPermanentAddress']
    # readonly_fields = ['MemberRegistrationID', 'MemberName', 'MemberGender', 'MemberBirthDate', 'MemberFatherName', 'MemberPhone', 'MemberVerified', 'MemberRegisterDateTime', 'MemberRegisterAgent', 'MemberNote', 'MemberStreetTemporaryAddress', 'MemberStreetPermanentAddress']


admin.site.register(Member, MemberAdmin)
