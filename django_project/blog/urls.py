from django.contrib import admin
from . import views
from django.urls import path,include

urlpatterns = [
    path('', views.front),
    path('home/', views.home),
    path('algo/', views.algo),
    #path('live/',views.live),
    path('live/liveres/',views.liveres),
    path('home/bjp_inc/', views.bjp_inc),
    path('home/bjp_ncp/', views.bjp_ncp),
    path('home/bjp_aap/', views.bjp_aap),
    path('home/bjp_tmc/', views.bjp_tmc),
    path('home/bjp_bsp/', views.bjp_bsp),
    path('home/bjp_cpim/', views.bjp_cpim),
    path('home/inc_ncp/', views.inc_ncp),
    path('home/inc_aap/', views.inc_aap),
    path('home/inc_tmc/', views.inc_tmc),
    path('home/inc_bsp/', views.inc_bsp),
    path('home/inc_cpim/', views.inc_cpim),
	path('home/ncp_aap/', views.ncp_aap),
	path('home/ncp_tmc/', views.ncp_tmc),
	path('home/ncp_bsp/', views.ncp_bsp),
	path('home/ncp_cpim/', views.ncp_cpim),
	path('home/aap_tmc/', views.aap_tmc),
	path('home/aap_bsp/', views.aap_bsp),
	path('home/aap_cpim/', views.aap_cpim),
	path('home/tmc_bsp/', views.tmc_bsp),
	path('home/tmc_cpim/', views.tmc_cpim),
	path('home/bsp_cpim/', views.bsp_cpim),
]