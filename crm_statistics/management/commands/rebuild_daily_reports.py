from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from crm_statistics.services import build_daily_report

class Command(BaseCommand):
    help = "Перестроить ежедневные отчёты за последние N дней"

    def add_arguments(self, parser):
        parser.add_argument("--days", type=int, default=30, help="Количество дней")

    def handle(self, *args, **options):
        days = options["days"]
        today = timezone.now().date()
        for i in range(days):
            report_date = today - timedelta(days=i)
            build_daily_report(report_date=report_date)
            self.stdout.write(f"Отчёт за {report_date} готов")
