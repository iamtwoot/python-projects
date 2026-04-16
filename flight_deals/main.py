from data_manager import DataManager
import requests_cache
from datetime import datetime, timedelta

requests_cache.install_cache("flight_cache", expire_after=3600)

# --------------------- Set the Dates --------------------- #
tomorrow = datetime.today() + timedelta(days=1)
six_months_from_today = datetime.today() + timedelta(days=180)

# Cannot use an API for flights due to restrictions on Russian phone numbers

# data_manager = DataManager()
# sheet_data = data_manager.get_data()