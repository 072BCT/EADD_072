from django import forms

from .models import AddressCountry, AddressProvince, AddressZone, AddressDistrict, AddressVDCMunicipality, Institution, \
    Member


class AddressCountryForm(forms.ModelForm):
    class Meta:
        model = AddressCountry
        fields = ['CountryName']


class AddressProvinceForm(forms.ModelForm):
    class Meta:
        model = AddressProvince
        fields = ['ProvinceName', 'Country']


class AddressZoneForm(forms.ModelForm):
    class Meta:
        model = AddressZone
        fields = ['ZoneName', 'Province']


class AddressDistrictForm(forms.ModelForm):
    class Meta:
        model = AddressDistrict
        fields = ['DistrictName', 'Zone']


class AddressVDCMunicipalityForm(forms.ModelForm):
    class Meta:
        model = AddressVDCMunicipality
        fields = ['VDCMunicipalityName', 'District']


class InstitutionForm(forms.ModelForm):
    class Meta:
        model = Institution
        fields = ['InstitutionName', 'InstitutionEmail', 'InstitutionPhone', 'InstitutionWebsite',
                  'InstitutionAddressStreet', 'InstitutionNote', 'InstitutionAddressVDCMunicipality']


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['MemberRegistrationID', 'MemberName', 'MemberGender', 'MemberBirthDate', 'MemberFatherName',
                  'MemberPhone', 'MemberVerified', 'MemberRegisterDateTime', 'MemberRegisterAgent', 'MemberNote',
                  'MemberStreetTemporaryAddress', 'MemberStreetPermanentAddress', 'MemberPermanentAddress',
                  'MemberTemporaryAddress', 'MemberInstitution']
