from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.models import ContentType
from django.db import models as models
from django.db.models import CharField, ForeignKey, DateField, BooleanField, DateTimeField
from django.urls import reverse

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Others')
)


class AddressCountry(models.Model):
    # Fields
    CountryName = CharField(max_length=250, blank=True, default="Nepal")

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('addresscountry_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('addresscountry_update', args=(self.pk,))


class AddressProvince(models.Model):
    # Fields
    ProvinceName = CharField(max_length=250, blank=True, null=True)

    # Relationship Fields
    Country = ForeignKey(
        'WebApp.AddressCountry',
        related_name="addressprovinces", on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('addressprovince_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('addressprovince_update', args=(self.pk,))


class AddressZone(models.Model):
    # Fields
    ZoneName = CharField(max_length=250, blank=True, null=True)

    # Relationship Fields
    Province = ForeignKey(
        'WebApp.AddressProvince',
        related_name="addresszones", on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('addresszone_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('addresszone_update', args=(self.pk,))


class AddressDistrict(models.Model):
    # Fields
    DistrictName = CharField(max_length=250, blank=True, null=True)

    # Relationship Fields
    Zone = ForeignKey(
        'WebApp.AddressZone',
        related_name="addressdistricts", on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('addressdistrict_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('addressdistrict_update', args=(self.pk,))


class AddressVDCMunicipality(models.Model):
    # Fields
    VDCMunicipalityName = CharField(max_length=250, blank=True, null=True)

    # Relationship Fields
    District = ForeignKey(
        'WebApp.AddressDistrict',
        related_name="addressvdcmunicipalitys", on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('addressvdcmunicipality_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('addressvdcmunicipality_update', args=(self.pk,))


class Institution(models.Model):
    # Fields
    InstitutionName = CharField(max_length=250, blank=True, null=True)
    InstitutionEmail = CharField(max_length=150, blank=True, null=True)
    InstitutionPhone = CharField(max_length=150, blank=True, null=True)
    InstitutionWebsite = CharField(max_length=150, blank=True, null=True)
    InstitutionAddressStreet = CharField(max_length=100, blank=True, null=True)
    InstitutionNote = CharField(max_length=150, blank=True, null=True)

    # Relationship Fields
    InstitutionAddressVDCMunicipality = ForeignKey(
        'WebApp.AddressVDCMunicipality',
        related_name="institutions", on_delete=models.DO_NOTHING
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('institution_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('institution_update', args=(self.pk,))


class Member(AbstractUser):
    # Fields
    MemberRegistrationID = CharField(max_length=250, blank=True, null=True)
    MemberName = CharField(max_length=500, blank=True, null=True)
    MemberGender = CharField(max_length=1, choices=GENDER_CHOICES)
    MemberBirthDate = DateField(blank=True, null=True)
    MemberFatherName = CharField(max_length=500, blank=True, null=True)
    MemberPhone = CharField(max_length=150, blank=True, null=True)
    MemberVerified = BooleanField(default=False)
    MemberRegisterDateTime = DateTimeField(default=datetime.now(), blank=True)
    MemberRegisterAgent = CharField(max_length=200, blank=True, null=True)
    MemberNote = CharField(max_length=500, blank=True, null=True)
    MemberStreetTemporaryAddress = models.TextField(max_length=100)
    MemberStreetPermanentAddress = models.TextField(max_length=100)

    # Relationship Fields
    MemberPermanentAddress = ForeignKey(
        'WebApp.AddressVDCMunicipality',
        related_name="members", on_delete=models.DO_NOTHING, null=True
    )
    MemberTemporaryAddress = ForeignKey(
        'WebApp.AddressVDCMunicipality',
        related_name="members_2", on_delete=models.DO_NOTHING, null=True
    )
    MemberInstitution = ForeignKey(
        'WebApp.Institution',
        related_name="members", on_delete=models.CASCADE, null=True
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('member_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('member_update', args=(self.pk,))
