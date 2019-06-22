from rest_framework import viewsets, permissions

from . import models
from . import serializers


class AddressCountryViewSet(viewsets.ModelViewSet):
    """ViewSet for the AddressCountry class"""

    queryset = models.AddressCountry.objects.all()
    serializer_class = serializers.AddressCountrySerializer
    permission_classes = [permissions.IsAuthenticated]


class AddressProvinceViewSet(viewsets.ModelViewSet):
    """ViewSet for the AddressProvince class"""

    queryset = models.AddressProvince.objects.all()
    serializer_class = serializers.AddressProvinceSerializer
    permission_classes = [permissions.IsAuthenticated]


class AddressZoneViewSet(viewsets.ModelViewSet):
    """ViewSet for the AddressZone class"""

    queryset = models.AddressZone.objects.all()
    serializer_class = serializers.AddressZoneSerializer
    permission_classes = [permissions.IsAuthenticated]


class AddressDistrictViewSet(viewsets.ModelViewSet):
    """ViewSet for the AddressDistrict class"""

    queryset = models.AddressDistrict.objects.all()
    serializer_class = serializers.AddressDistrictSerializer
    permission_classes = [permissions.IsAuthenticated]


class AddressVDCMunicipalityViewSet(viewsets.ModelViewSet):
    """ViewSet for the AddressVDCMunicipality class"""

    queryset = models.AddressVDCMunicipality.objects.all()
    serializer_class = serializers.AddressVDCMunicipalitySerializer
    permission_classes = [permissions.IsAuthenticated]


class InstitutionViewSet(viewsets.ModelViewSet):
    """ViewSet for the Institution class"""

    queryset = models.Institution.objects.all()
    serializer_class = serializers.InstitutionSerializer
    permission_classes = [permissions.IsAuthenticated]


class MemberViewSet(viewsets.ModelViewSet):
    """ViewSet for the Member class"""

    queryset = models.Member.objects.all()
    serializer_class = serializers.MemberSerializer
    permission_classes = [permissions.IsAuthenticated]
