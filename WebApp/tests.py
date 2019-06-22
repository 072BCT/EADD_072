import unittest

from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.test import Client
from django.urls import reverse

from .models import AddressCountry, AddressProvince, AddressZone, AddressDistrict, AddressVDCMunicipality, Institution, \
    Member


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_addresscountry(**kwargs):
    defaults = {}
    defaults["CountryName"] = "CountryName"
    defaults.update(**kwargs)
    return AddressCountry.objects.create(**defaults)


def create_addressprovince(**kwargs):
    defaults = {}
    defaults["ProvinceName"] = "ProvinceName"
    defaults.update(**kwargs)
    if "Country" not in defaults:
        defaults["Country"] = create_addresscountry()
    return AddressProvince.objects.create(**defaults)


def create_addresszone(**kwargs):
    defaults = {}
    defaults["ZoneName"] = "ZoneName"
    defaults.update(**kwargs)
    if "Province" not in defaults:
        defaults["Province"] = create_addressprovince()
    return AddressZone.objects.create(**defaults)


def create_addressdistrict(**kwargs):
    defaults = {}
    defaults["DistrictName"] = "DistrictName"
    defaults.update(**kwargs)
    if "Zone" not in defaults:
        defaults["Zone"] = create_addresszone()
    return AddressDistrict.objects.create(**defaults)


def create_addressvdcmunicipality(**kwargs):
    defaults = {}
    defaults["VDCMunicipalityName"] = "VDCMunicipalityName"
    defaults.update(**kwargs)
    if "District" not in defaults:
        defaults["District"] = create_addressdistrict()
    return AddressVDCMunicipality.objects.create(**defaults)


def create_institution(**kwargs):
    defaults = {}
    defaults["InstitutionName"] = "InstitutionName"
    defaults["InstitutionEmail"] = "InstitutionEmail"
    defaults["InstitutionPhone"] = "InstitutionPhone"
    defaults["InstitutionWebsite"] = "InstitutionWebsite"
    defaults["InstitutionAddressStreet"] = "InstitutionAddressStreet"
    defaults["InstitutionNote"] = "InstitutionNote"
    defaults.update(**kwargs)
    if "InstitutionAddressVDCMunicipality" not in defaults:
        defaults["InstitutionAddressVDCMunicipality"] = create_addressvdcmunicipality()
    return Institution.objects.create(**defaults)


def create_member(**kwargs):
    defaults = {}
    defaults["MemberRegistrationID"] = "MemberRegistrationID"
    defaults["MemberName"] = "MemberName"
    defaults["MemberGender"] = "MemberGender"
    defaults["MemberBirthDate"] = "MemberBirthDate"
    defaults["MemberFatherName"] = "MemberFatherName"
    defaults["MemberPhone"] = "MemberPhone"
    defaults["MemberVerified"] = "MemberVerified"
    defaults["MemberRegisterDateTime"] = "MemberRegisterDateTime"
    defaults["MemberRegisterAgent"] = "MemberRegisterAgent"
    defaults["MemberNote"] = "MemberNote"
    defaults["MemberStreetTemporaryAddress"] = "MemberStreetTemporaryAddress"
    defaults["MemberStreetPermanentAddress"] = "MemberStreetPermanentAddress"
    defaults.update(**kwargs)
    if "MemberPermanentAddress" not in defaults:
        defaults["MemberPermanentAddress"] = create_addressvdcmunicipality()
    if "MemberTemporaryAddress" not in defaults:
        defaults["MemberTemporaryAddress"] = create_addressvdcmunicipality()
    if "MemberInstitution" not in defaults:
        defaults["MemberInstitution"] = create_institution()
    return Member.objects.create(**defaults)


class AddressCountryViewTest(unittest.TestCase):
    '''
    Tests for AddressCountry
    '''

    def setUp(self):
        self.client = Client()

    def test_list_addresscountry(self):
        url = reverse('addresscountry_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_addresscountry(self):
        url = reverse('addresscountry_create')
        data = {
            "CountryName": "CountryName",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_addresscountry(self):
        addresscountry = create_addresscountry()
        url = reverse('addresscountry_detail', args=[addresscountry.pk, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_addresscountry(self):
        addresscountry = create_addresscountry()
        data = {
            "CountryName": "CountryName",
        }
        url = reverse('addresscountry_update', args=[addresscountry.pk, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class AddressProvinceViewTest(unittest.TestCase):
    '''
    Tests for AddressProvince
    '''

    def setUp(self):
        self.client = Client()

    def test_list_addressprovince(self):
        url = reverse('addressprovince_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_addressprovince(self):
        url = reverse('addressprovince_create')
        data = {
            "ProvinceName": "ProvinceName",
            "Country": create_addresscountry().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_addressprovince(self):
        addressprovince = create_addressprovince()
        url = reverse('addressprovince_detail', args=[addressprovince.pk, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_addressprovince(self):
        addressprovince = create_addressprovince()
        data = {
            "ProvinceName": "ProvinceName",
            "Country": create_addresscountry().pk,
        }
        url = reverse('addressprovince_update', args=[addressprovince.pk, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class AddressZoneViewTest(unittest.TestCase):
    '''
    Tests for AddressZone
    '''

    def setUp(self):
        self.client = Client()

    def test_list_addresszone(self):
        url = reverse('addresszone_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_addresszone(self):
        url = reverse('addresszone_create')
        data = {
            "ZoneName": "ZoneName",
            "Province": create_addressprovince().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_addresszone(self):
        addresszone = create_addresszone()
        url = reverse('addresszone_detail', args=[addresszone.pk, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_addresszone(self):
        addresszone = create_addresszone()
        data = {
            "ZoneName": "ZoneName",
            "Province": create_addressprovince().pk,
        }
        url = reverse('addresszone_update', args=[addresszone.pk, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class AddressDistrictViewTest(unittest.TestCase):
    '''
    Tests for AddressDistrict
    '''

    def setUp(self):
        self.client = Client()

    def test_list_addressdistrict(self):
        url = reverse('addressdistrict_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_addressdistrict(self):
        url = reverse('addressdistrict_create')
        data = {
            "DistrictName": "DistrictName",
            "Zone": create_addresszone().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_addressdistrict(self):
        addressdistrict = create_addressdistrict()
        url = reverse('addressdistrict_detail', args=[addressdistrict.pk, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_addressdistrict(self):
        addressdistrict = create_addressdistrict()
        data = {
            "DistrictName": "DistrictName",
            "Zone": create_addresszone().pk,
        }
        url = reverse('addressdistrict_update', args=[addressdistrict.pk, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class AddressVDCMunicipalityViewTest(unittest.TestCase):
    '''
    Tests for AddressVDCMunicipality
    '''

    def setUp(self):
        self.client = Client()

    def test_list_addressvdcmunicipality(self):
        url = reverse('addressvdcmunicipality_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_addressvdcmunicipality(self):
        url = reverse('addressvdcmunicipality_create')
        data = {
            "VDCMunicipalityName": "VDCMunicipalityName",
            "District": create_addressdistrict().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_addressvdcmunicipality(self):
        addressvdcmunicipality = create_addressvdcmunicipality()
        url = reverse('addressvdcmunicipality_detail', args=[addressvdcmunicipality.pk, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_addressvdcmunicipality(self):
        addressvdcmunicipality = create_addressvdcmunicipality()
        data = {
            "VDCMunicipalityName": "VDCMunicipalityName",
            "District": create_addressdistrict().pk,
        }
        url = reverse('addressvdcmunicipality_update', args=[addressvdcmunicipality.pk, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class InstitutionViewTest(unittest.TestCase):
    '''
    Tests for Institution
    '''

    def setUp(self):
        self.client = Client()

    def test_list_institution(self):
        url = reverse('institution_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_institution(self):
        url = reverse('institution_create')
        data = {
            "InstitutionName": "InstitutionName",
            "InstitutionEmail": "InstitutionEmail",
            "InstitutionPhone": "InstitutionPhone",
            "InstitutionWebsite": "InstitutionWebsite",
            "InstitutionAddressStreet": "InstitutionAddressStreet",
            "InstitutionNote": "InstitutionNote",
            "InstitutionAddressVDCMunicipality": create_addressvdcmunicipality().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_institution(self):
        institution = create_institution()
        url = reverse('institution_detail', args=[institution.pk, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_institution(self):
        institution = create_institution()
        data = {
            "InstitutionName": "InstitutionName",
            "InstitutionEmail": "InstitutionEmail",
            "InstitutionPhone": "InstitutionPhone",
            "InstitutionWebsite": "InstitutionWebsite",
            "InstitutionAddressStreet": "InstitutionAddressStreet",
            "InstitutionNote": "InstitutionNote",
            "InstitutionAddressVDCMunicipality": create_addressvdcmunicipality().pk,
        }
        url = reverse('institution_update', args=[institution.pk, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class MemberViewTest(unittest.TestCase):
    '''
    Tests for Member
    '''

    def setUp(self):
        self.client = Client()

    def test_list_member(self):
        url = reverse('member_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_member(self):
        url = reverse('member_create')
        data = {
            "MemberRegistrationID": "MemberRegistrationID",
            "MemberName": "MemberName",
            "MemberGender": "MemberGender",
            "MemberBirthDate": "MemberBirthDate",
            "MemberFatherName": "MemberFatherName",
            "MemberPhone": "MemberPhone",
            "MemberVerified": "MemberVerified",
            "MemberRegisterDateTime": "MemberRegisterDateTime",
            "MemberRegisterAgent": "MemberRegisterAgent",
            "MemberNote": "MemberNote",
            "MemberStreetTemporaryAddress": "MemberStreetTemporaryAddress",
            "MemberStreetPermanentAddress": "MemberStreetPermanentAddress",
            "MemberPermanentAddress": create_addressvdcmunicipality().pk,
            "MemberTemporaryAddress": create_addressvdcmunicipality().pk,
            "MemberInstitution": create_institution().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_member(self):
        member = create_member()
        url = reverse('member_detail', args=[member.pk, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_member(self):
        member = create_member()
        data = {
            "MemberRegistrationID": "MemberRegistrationID",
            "MemberName": "MemberName",
            "MemberGender": "MemberGender",
            "MemberBirthDate": "MemberBirthDate",
            "MemberFatherName": "MemberFatherName",
            "MemberPhone": "MemberPhone",
            "MemberVerified": "MemberVerified",
            "MemberRegisterDateTime": "MemberRegisterDateTime",
            "MemberRegisterAgent": "MemberRegisterAgent",
            "MemberNote": "MemberNote",
            "MemberStreetTemporaryAddress": "MemberStreetTemporaryAddress",
            "MemberStreetPermanentAddress": "MemberStreetPermanentAddress",
            "MemberPermanentAddress": create_addressvdcmunicipality().pk,
            "MemberTemporaryAddress": create_addressvdcmunicipality().pk,
            "MemberInstitution": create_institution().pk,
        }
        url = reverse('member_update', args=[member.pk, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
