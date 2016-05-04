from datetime import datetime, timedelta


class DateProvider:
    @staticmethod
    def now():
        return datetime.now()

    @staticmethod
    def tenDaysAgo():
        return datetime.now() - timedelta(days=10)

    @staticmethod
    def getTotalDaysPassedRatio():
        now = datetime.now()
        start_year = datetime(now.year, 1, 1, 0, 0, 0)
        days_passed = (datetime.now() - start_year).days
        return float(days_passed)/float(365.0)