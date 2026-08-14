from django.views.generic import TemplateView, ListView, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta

from .services import build_daily_report, get_stats
from .models import DailyReport


class StatisticsDashboardView(LoginRequiredMixin, TemplateView):
    template_name = "crm_statistics/dashboard.html"

    @property
    def today(self):
        return timezone.now().date()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        stats_30d = get_stats(
            start_date=(self.today - timedelta(days=30)),
            end_date=self.today,
        )
        recent_reports = DailyReport.objects.order_by("-date")[:7]
        context.update({
            "stats_30d": stats_30d,
            "recent_reports": recent_reports,
            "today": self.today,
        })
        return context


class DailyReportsListView(LoginRequiredMixin, ListView):
    model = DailyReport
    template_name = "crm_statistics/daily_reports_list.html"
    context_object_name = "reports"
    paginate_by = 20


class StatisticsRefreshView(LoginRequiredMixin, RedirectView):
    pattern_name = "statistics_dashboard"

    def get_redirect_url(self, *args, **kwargs):
        days = int(self.request.GET.get("days", 60))
        today = timezone.now().date()

        for i in range(days):
            report_date = today - timedelta(days=i)
            build_daily_report(report_date=report_date)

        return super().get_redirect_url(*args, **kwargs)
