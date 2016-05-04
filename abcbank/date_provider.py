from datetime import datetime, timedelta


class DateProvider:
    @staticmethod
    def now():
        return datetime.now()

    @staticmethod
    def tenDaysAgo():
        return datetime.now() - timedelta(days=10)