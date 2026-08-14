from datetime import date, timedelta
from django.db.models import Sum, Count
from leads.models import Lead
from clients.models import Client
from contracts.models import Contract
from campaigns.models import Campaign
from .models import DailyReport

def get_stats(start_date=None, end_date=None):
    qs_leads = Lead.objects.all()
    qs_clients = Client.objects.all()
    qs_contracts = Contract.objects.all()
    qs_campaigns = Campaign.objects.all()

    if start_date:
        qs_leads = qs_leads.filter(created_at__date__gte=start_date)
        qs_clients = qs_clients.filter(created_at__date__gte=start_date)
        qs_contracts = qs_contracts.filter(created_at__date__gte=start_date)
        qs_campaigns = qs_campaigns.filter(start_date__gte=start_date)

    if end_date:
        qs_leads = qs_leads.filter(created_at__date__lte=end_date)
        qs_clients = qs_clients.filter(created_at__date__lte=end_date)
        qs_contracts = qs_contracts.filter(created_at__date__lte=end_date)

        qs_campaigns = qs_campaigns.filter(start_date__lte=end_date)

    total_leads = qs_leads.count()
    total_clients = qs_clients.count()
    total_campaigns = qs_campaigns.count()

    contracts_agg = qs_contracts.aggregate(
        total_count=Count("id"),
        total_revenue=Sum("amount"),
    )
    total_contracts = contracts_agg["total_count"] or 0
    total_revenue = contracts_agg["total_revenue"] or 0
    avg_contract_value = (total_revenue / total_contracts) if total_contracts else 0

    return {
        "leads": total_leads,
        "clients": total_clients,
        "contracts": total_contracts,
        "campaigns": total_campaigns,
        "revenue": total_revenue,
        "avg_contract_value": avg_contract_value,
    }


def build_daily_report(report_date=None, user=None):
    from django.utils import timezone
    if report_date is None:
        report_date = timezone.now().date()

    stats = get_stats(start_date=report_date, end_date=report_date)

    report, created = DailyReport.objects.update_or_create(
        date=report_date,
        defaults={
            "leads_count": stats["leads"],
            "clients_count": stats["clients"],
            "contracts_count": stats["contracts"],
            "campaigns_count": stats["campaigns"],
            "revenue": stats["revenue"],
            "avg_contract_value": stats["avg_contract_value"],
            "updated_by": user,
        },
    )
    return report
