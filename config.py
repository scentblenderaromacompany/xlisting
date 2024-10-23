from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')
EBAY_API_KEY = os.getenv('EBAY_API_KEY')
FACEBOOK_API_KEY = os.getenv('FACEBOOK_API_KEY')
ETSY_API_KEY = os.getenv('ETSY_API_KEY')
