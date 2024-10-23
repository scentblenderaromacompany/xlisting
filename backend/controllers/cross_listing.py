from backend.integrations.ebay.ebay_api import create_ebay_listing
from backend.integrations.facebook.facebook_api import create_facebook_listing
from backend.integrations.etsy.etsy_api import create_etsy_listing
from backend.integrations.offerup.offerup_automation import automate_offerup_listing

def cross_list_item(item_data: dict):
    create_ebay_listing(item_data)
    create_facebook_listing(item_data)
    create_etsy_listing(item_data)
    automate_offerup_listing(item_data)
    # Implement additional cross-listing logic as needed
