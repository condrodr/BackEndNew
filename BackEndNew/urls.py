"""
URL configuration for BackEndNew project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Customer import views as c_views
from Driver import views as d_views
from LedgerKas import views as l_views
from Pembelian import views as beli_views
from Penjualan import views as jual_views
from Produk import views as p_views
from ReturBarang import views as ret_views
from Salesman import views as sales_views
from Stok import views as stok_views
from Kas import views as kas_views
from SuratJalanKeluar import views as sjk_views
from SuratJalanMasuk import views as sjm_views
from UserProfile import views as profile_views
from Mutasi import views as mutasi_views
from EndUser import views as end_views
from django.conf import settings
from . import choice as c
from . import api as a
from django.conf.urls.static import static
from rest_framework import routers


router = routers.DefaultRouter()
#Customer
router.register('registeredcustomer',c_views.RegisteredCustomerView)
router.register('loyaltypointcustomer',c_views.LoyaltyPointCustomerView)
router.register('datapotensicustomer',c_views.DataPotensiCustomerView)
router.register('dailyregisteredcustomer',c_views.DailyRegisteredCustomerReportView)
router.register('kontrakoutletpromotion',c_views.KontrakOutletPromotionView)
router.register('daftarpromosiberjalan',c_views.DaftarPromosiBerjalanView)
#Driver
router.register('driver',d_views.DriverView)
router.register('plankiriman',d_views.PlanKirimanView)
router.register('detailplankiriman',d_views.DetailPlanKirimanView)
router.register('updatenotakirimsebagian',d_views.UpdateNotaKirimSebagianView)
router.register('detailsisanotaterkirimsebagian',d_views.DetailSisaNotaTerkirimSebagianView)
#LedgerKas
router.register('kas',l_views.KasView)
router.register('masterakun',l_views.MasterAkunView)
router.register('journalentry',l_views.JournalEntryView)
router.register('journalentryline',l_views.JournalEntryLineView)
#Pembelian
router.register('notapembelian',beli_views.NotaPembelianView)
router.register('detailpembelian',beli_views.DetailPembelianView)
#Penjualan
router.register('notapenjualan',jual_views.NotaPenjualanView)
router.register('detailpenjualan',jual_views.DetailPenjualanView)
#Produk
router.register('produk',p_views.ProdukView)
router.register('produkpromotion',p_views.ProdukPromotionView)
#ReturBarang
router.register('notaretur',ret_views.NotaReturView)
router.register('detailretur',ret_views.DetailReturView)
#Kas
# router.register('kas',kas_views.KasView)
# # router.register('journalentry',kas_views.JournalEntryView)
# # router.register('journalentryline',kas_views.JournalEntryLineView)
#Salesman
router.register('salesman',sales_views.SalesmanView)
router.register('catatansalesman',sales_views.CatatanSalesmanView)
#Stok
router.register('stok',stok_views.StokView)
router.register('stoktransit',stok_views.StokTransitView)
router.register('kartustok',stok_views.KartuStokView)
router.register('lokasistok',stok_views.LokasiStokView)
router.register('selisihbongkarmuat',stok_views.SelisihBongkarMuatView)

#Mutasi
router.register('notamutasikeluarcart',mutasi_views.NotaMutasiKeluarCartView)
router.register('terimamutasicart',mutasi_views.TerimaMutasiCartView)
router.register('detailmutasikeluarcart',mutasi_views.DetailMutasiKeluarCartView)

#SuratJalanKeluar
router.register('sjkeluar',sjk_views.SJKeluarView)
router.register('detailsjkeluar',sjk_views.DetailSJKeluarView)
router.register('detaillokasikeluarproduk',sjk_views.DetailLokasiKeluarProdukView)
#SuratJalanMasuk
router.register('sjmasuk',sjm_views.SJMasukView)
router.register('detailsjmasuk',sjm_views.DetailSJMasukView)
#Profile
router.register('profile',profile_views.ProfileView)

#EndUser
router.register('jualanrekomender',end_views.JualanRekomenderView)
router.register('rewardspinwheel',end_views.RewardSpinWheelView)
router.register('rekomender',end_views.RekomenderView)
router.register('rewardlist',end_views.RewardListView)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    path('api/choices/', c.get_all_choices, name='get_all_choices'),
    path('api/summary_rekomender/',a.summary_rekomender),
    path('api/summary_outlet/',a.summary_outlet)
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)