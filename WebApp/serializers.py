from rest_framework import serializers

from . import models


class AddressCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AddressCountry
        fields = (
            'pk',
            'CountryName',
        )


class AddressProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AddressProvince
        fields = (
            'pk',
            'ProvinceName',
        )


class AddressZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AddressZone
        fields = (
            'pk',
            'ZoneName',
        )


class AddressDistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AddressDistrict
        fields = (
            'pk',
            'DistrictName',
        )


class AddressVDCMunicipalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AddressVDCMunicipality
        fields = (
            'pk',
            'VDCMunicipalityName',
        )


class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Institution
        fields = (
            'pk',
            'InstitutionName',
            'InstitutionEmail',
            'InstitutionPhone',
            'InstitutionWebsite',
            'InstitutionAddressStreet',
            'InstitutionNote',
        )


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Member
        fields = (
            'pk',
            'MemberRegistrationID',
            'MemberName',
            'MemberGender',
            'MemberBirthDate',
            'MemberFatherName',
            'MemberPhone',
            'MemberVerified',
            'MemberRegisterDateTime',
            'MemberRegisterAgent',
            'MemberNote',
            'MemberStreetTemporaryAddress',
            'MemberStreetPermanentAddress',
        )
