from django.contrib.auth.decorators import login_required
from django.urls import path, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'addresscountry', api.AddressCountryViewSet)
router.register(r'addressprovince', api.AddressProvinceViewSet)
router.register(r'addresszone', api.AddressZoneViewSet)
router.register(r'addressdistrict', api.AddressDistrictViewSet)
router.register(r'addressvdcmunicipality', api.AddressVDCMunicipalityViewSet)
router.register(r'institution', api.InstitutionViewSet)
router.register(r'member', api.MemberViewSet)

urlpatterns = (
    # urls for Django Rest Framework API
    path('api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for AddressCountry
    path('addresscountry/', views.AddressCountryListView.as_view(), name='addresscountry_list'),
    path('addresscountry/create/', login_required(views.AddressCountryCreateView.as_view()),
         name='addresscountry_create'),
    path('addresscountry/detail/<int:pk>/', views.AddressCountryDetailView.as_view(),
         name='addresscountry_detail'),
    path('addresscountry/update/<int:pk>/', login_required(views.AddressCountryUpdateView.as_view()),
         name='addresscountry_update'),
)

urlpatterns += (
    # urls for AddressProvince
    path('addressprovince/', views.AddressProvinceListView.as_view(), name='addressprovince_list'),
    path('addressprovince/create/', login_required(views.AddressProvinceCreateView.as_view()),
         name='addressprovince_create'),
    path('addressprovince/detail/<int:pk>/', views.AddressProvinceDetailView.as_view(),
         name='addressprovince_detail'),
    path('addressprovince/update/<int:pk>/', login_required(views.AddressProvinceUpdateView.as_view()),
         name='addressprovince_update'),
)

urlpatterns += (
    # urls for AddressZone
    path('addresszone/', views.AddressZoneListView.as_view(), name='addresszone_list'),
    path('addresszone/create/', login_required(views.AddressZoneCreateView.as_view()), name='addresszone_create'),
    path('addresszone/detail/<int:pk>/', views.AddressZoneDetailView.as_view(),
         name='addresszone_detail'),
    path('addresszone/update/<int:pk>/', login_required(views.AddressZoneUpdateView.as_view()),
         name='addresszone_update'),
)

urlpatterns += (
    # urls for AddressDistrict
    path('addressdistrict/', views.AddressDistrictListView.as_view(), name='addressdistrict_list'),
    path('addressdistrict/create/', login_required(views.AddressDistrictCreateView.as_view()),
         name='addressdistrict_create'),
    path('addressdistrict/detail/<int:pk>/', views.AddressDistrictDetailView.as_view(),
         name='addressdistrict_detail'),
    path('addressdistrict/update/<int:pk>/', login_required(views.AddressDistrictUpdateView.as_view()),
         name='addressdistrict_update'),
)

urlpatterns += (
    # urls for AddressVDCMunicipality
    path('addressvdcmunicipality/', views.AddressVDCMunicipalityListView.as_view(),
         name='addressvdcmunicipality_list'),
    path('addressvdcmunicipality/create/', login_required(views.AddressVDCMunicipalityCreateView.as_view()),
         name='addressvdcmunicipality_create'),
    path('addressvdcmunicipality/detail/<int:pk>/', views.AddressVDCMunicipalityDetailView.as_view(),
         name='addressvdcmunicipality_detail'),
    path('addressvdcmunicipality/update/<int:pk>/', login_required(views.AddressVDCMunicipalityUpdateView.as_view()),
         name='addressvdcmunicipality_update'),
)

urlpatterns += (
    # urls for Institution
    path('institution/', views.InstitutionListView.as_view(), name='institution_list'),
    path('institution/create/', login_required(views.InstitutionCreateView.as_view()), name='institution_create'),
    path('institution/detail/<int:pk>/', views.InstitutionDetailView.as_view(),
         name='institution_detail'),
    path('institution/update/<int:pk>/', login_required(views.InstitutionUpdateView.as_view()),
         name='institution_update'),
)

urlpatterns += (
    # urls for Member
    path('member/', views.MemberListView.as_view(), name='member_list'),
    path('member/create/', login_required(views.MemberCreateView.as_view()), name='member_create'),
    path('member/detail/<int:pk>/', views.MemberDetailView.as_view(), name='member_detail'),
    path('member/update/<int:pk>/', login_required(views.MemberUpdateView.as_view()), name='member_update'),
)
