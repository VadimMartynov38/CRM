from django.urls import path
from . import views

app_name = "statistic"

urlpatterns = [
    path("", views.StatisticsDashboardView.as_view(), name="statistics_dashboard"),
    path("reports/", views.DailyReportsListView.as_view(), name="daily_reports_list"),
    path("refresh/", views.StatisticsRefreshView.as_view(), name="statistics_refresh"),

]
