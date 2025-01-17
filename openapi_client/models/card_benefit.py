# coding: utf-8

"""
    Engine by MoneyLion API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.58.0
    Contact: help@engine.tech
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class CardBenefit(str, Enum):
    """
    Benefits or benefit categories related to a credit card
    """

    """
    allowed enum values
    """
    NO_FOREIGN_TRANSACTION_FEES = 'No Foreign Transaction Fees'
    PURCHASE_PROTECTION = 'Purchase Protection'
    RETURN_PROTECTION = 'Return Protection'
    PRICE_PROTECTION = 'Price Protection'
    FRAUD_PROTECTION = 'Fraud Protection'
    EXTENDED_WARRANTY = 'Extended Warranty'
    TRAVEL_ACCIDENT_INSURANCE = 'Travel Accident Insurance'
    TRIP_INTERRUPTION_INSURANCE = 'Trip Interruption Insurance'
    CAR_RENTAL_INSURANCE = 'Car Rental Insurance'
    BAGGAGE_INSURANCE = 'Baggage Insurance'
    BAGGAGE_DELAY_INSURANCE = 'Baggage Delay Insurance'
    HOTEL_BURGLARY_INSURANCE = 'Hotel Burglary Insurance'
    TRAVEL_AMPERSAND__EMERGENCY_ASSISTANCE = 'Travel & Emergency Assistance'
    ROADSIDE_ASSISTANCE = 'Roadside Assistance'
    CONCIERGE_SERVICE = 'Concierge Service'
    LOUNGE_ACCESS = 'Lounge Access'
    IDENTITY_THEFT_ASSISTANCE = 'Identity Theft Assistance'
    IN_MINUS_FLIGHT_SAVINGS = 'In-Flight Savings'
    FREE_CHECKED_BAG = 'Free Checked Bag'
    PRIORITY_BOARDING = 'Priority Boarding'
    NO_BLACKOUT_DATES = 'No Blackout Dates'
    FREE_COMPANION_TICKET = 'Free Companion Ticket'
    DISCOUNT_COMPANION_TICKET = 'Discount Companion Ticket'
    GLOBAL_ENTRY_OR_TSA_PRECHECK = 'Global Entry or TSA PreCheck'
    PRIVATE_JET_PERKS = 'Private Jet Perks'
    LOUNGE_ACCESS_DISCOUNT = 'Lounge Access Discount'
    ENUM_24_SLASH_7_CARDHOLDER_SUPPORT = '24/7 Cardholder Support'
    AUTHORIZED_USER = 'Authorized User'
    ENTERTAINMENT_ACCESS = 'Entertainment Access'
    AIRLINE_FEE_CREDIT = 'Airline Fee Credit'
    LATE_FEE_PASS = 'Late Fee Pass'
    CREDIT_SCORE_REPORTING = 'Credit Score Reporting'
    NO_FLIGHT_CHANGE_FEES = 'No Flight Change Fees'
    ENUM_24_SLASH_7_ACCOUNT_MONITORING = '24/7 Account Monitoring'
    AMEX_OFFERS = 'Amex Offers'
    VISA_SIGNATURE_OFFERS = 'Visa Signature Offers'
    MASTERCARD_OFFERS = 'MasterCard Offers'
    FREE_HOTEL_STAY = 'Free Hotel Stay'
    EXTENDED_HOTEL_STAY = 'Extended Hotel Stay'
    DINING_CONCIERGE = 'Dining Concierge'
    ENUM_2_LOUNGE_PASSES = '2 Lounge Passes'
    HILTON_HONORS_SILVER_MEMBERSHIP = 'Hilton Honors Silver Membership'
    HILTON_HONORS_GOLD_MEMBERSHIP = 'Hilton Honors Gold Membership'
    WORLD_OF_HYATT_DISCOVERIST_STATUS = 'World of Hyatt Discoverist Status'
    SPG_GOLD_MEMBERSHIP = 'SPG Gold Membership'
    MARRIOTT_REWARDS_SILVER_STATUS = 'Marriott Rewards Silver Status'
    HERTZ_PRESIDENTS_CIRCLE_ELITE_STATUS = 'Hertz Presidents Circle Elite Status'
    ENUM_2_FREE_CHECKED_BAGS = '2 Free Checked Bags'
    AUTO_DISCOUNTS = 'Auto Discounts'
    INCIRCLE_PARTNERSHIP = 'InCircle Partnership'
    SHOPRUNNER = 'ShopRunner'
    WIFI_ACCESS = 'WiFi Access'
    SHOPSAFE = 'ShopSafe'
    BOA_PREFERRED_REWARDS = 'BoA Preferred Rewards'
    MASTERCARD_FUEL_REWARDS_NETWORK = 'MasterCard Fuel Rewards Network'
    MISSED_EVENT_TICKET_PROTECTION = 'Missed Event Ticket Protection'
    ACCOUNT_FREEZING = 'Account Freezing'
    CELL_PHONE_PROTECTION = 'Cell Phone Protection'
    GPA_REWARDS = 'GPA Rewards'
    IN_MINUS_FLIGHT_WI_FI_CREDIT = 'In-Flight WiFi Credit'
    CITI_PRIVATE_PASS = 'Citi Private Pass'
    PRICELESS_CITIES = 'Priceless Cities'
    THE_HOTEL_COLLECTION = 'The Hotel Collection'
    BY_INVITATION_ONLY = 'By Invitation Only'
    LUXURY_HOTEL_COLLECTION = 'Luxury Hotel Collection'
    EXPEDIA_PLUS__SILVER_STATUS = 'Expedia+ Silver Status'
    EXPEDIA_PLUS__GOLD_STATUS = 'Expedia+ Gold Status'
    DOLLAR_100_AMERICAN_AIRLINES_DISCOUNT = '$100 American Airlines Discount'
    DISNEY_PARKS_PERKS_AND_SAVINGS = 'Disney Parks Perks and Savings'
    RITZ_MINUS_CARLTON_GOLD_ELITE_STATUS = 'Ritz-Carlton Gold Elite Status'
    RITZ_MINUS_CARLTON_CLUB_LEVEL_UPGRADE = 'Ritz-Carlton Club Level Upgrade'
    ANNUAL_TRAVEL_CREDIT = 'Annual Travel Credit'
    IHG_PLATINUM_ELITE_STATUS = 'IHG Platinum Elite Status'
    QUICKBOOKS_CONNECT = 'QuickBooks Connect'
    RECEIPTMATCH = 'ReceiptMatch'
    EMPLOYEE_SPENDING_LIMITS = 'Employee Spending Limits'
    FX_INTERNATIONAL_PAYMENTS = 'FX International Payments'
    NO_PRE_MINUS_SET_SPENDING_LIMIT = 'No Pre-Set Spending Limit'
    PURCHASE_FINANCING = 'Purchase Financing'
    AMEX_OPEN_SAVINGS = 'Amex Open Savings'
    AMAZON_SPECIAL_FINANCING = 'Amazon Special Financing'
    DOLLAR_100_RITZ_MINUS_CARLTON_HOTEL_CREDIT = '$100 Ritz-Carlton Hotel Credit'
    BRITISH_AIRWAYS_COMPANION_TICKET = 'British Airways Companion Ticket'
    MERCEDES_MINUS_BENZ_GIFT_CERTIFICATES = 'Mercedes-Benz Gift Certificates'
    MERCEDES_MINUS_BENZ_EXCESS_MILEAGE_WAIVER = 'Mercedes-Benz Excess Mileage Waiver'
    JETBLUE_ANNUAL_STATEMENT_CREDIT = 'JetBlue Annual Statement Credit'
    ENUM_20_PERCENT__DISCOUNT_ON_DELTA_FLIGHTS_FOR_DELTA_PRIVATE_JET_MEMBERS = '20% Discount on Delta Flights for Delta Private Jet Members'
    EXPENSE_REPORT_FEATURES = 'Expense Report Features'
    BUSINESS_CELL_PHONE_PROTECTION = 'Business Cell Phone Protection'
    FREE_SHIPPING_ON_MOST_TARGET_DOT_COM_ORDERS = 'Free Shipping on most Target.com orders'
    ENUM_30_EXTRA_DAYS_FOR_RETURNS = '30 Extra Days for Returns'
    FREE_CLOTHING_ALTERTAIONS = 'Free clothing altertaions'
    PERSONAL_SHOPPING = 'Personal shopping'
    SHOPMYWAY_SAVINGS = 'Shopmyway Savings'
    ONLINE_SUBSCRIPTION_CREDIT = 'Online Subscription Credit'
    UBER_EXCLUSIVE_ACCESS = 'Uber Exclusive Access'
    AIRLINE_BENEFITS = 'Airline Benefits'
    HOTEL_BENEFITS = 'Hotel Benefits'
    OTHER_TRAVEL_BENEFITS = 'Other Travel Benefits'
    EMERGENCY_ASSISTANCE = 'Emergency Assistance'
    EXPERIENCES = 'Experiences'
    SHOPPING_BENEFITS = 'Shopping Benefits'
    CARDHOLDER_BENEFITS = 'Cardholder Benefits'
    ENHANCED_SECURITY = 'Enhanced Security'
    BUSINESS_BENEFITS = 'Business Benefits'
    OTHER_BENEFITS = 'Other Benefits'
    IN_MINUS_FLIGHT_DISCOUNTS = 'In-Flight Discounts'
    FEE_COVERAGE = 'Fee Coverage'
    FLIGHT_CREDITS_AMPERSAND__DISCOUNTS = 'Flight Credits & Discounts'
    HOTEL_MEMBERSHIP_STATUS = 'Hotel Membership Status'
    HOTEL_CREDIT_AMPERSAND__FREE_STAYS = 'Hotel Credit & Free Stays'
    TRAVEL_CREDIT = 'Travel Credit'
    TRAVEL_EXPERIENCES_PROGRAMS = 'Travel Experiences Programs'
    CAR_RENTAL_MEMBERSHIP_STATUS = 'Car Rental Membership Status'
    EXTRA_GAS_REWARDS = 'Extra Gas Rewards'
    SHOPPING_PROTECTION = 'Shopping Protection'
    SHOPPING_DISCOUNTS = 'Shopping Discounts'
    FREE_SHIPPING = 'Free Shipping'
    THE_BOINGO_AMERICAN_EXPRESS_PREFERRED_PLAN = 'The Boingo American Express Preferred Plan'
    AIRSPACE_LOUNGE = 'AirSpace Lounge'
    UBER_MONTHLY_CREDIT = 'Uber Monthly Credit'
    RIDE_SHARE_BENEFITS = 'Ride Share Benefits'
    DELTA_SKY_CLUB = 'Delta Sky Club'
    ADMIRALS_CLUB_MEMBERSHIP = 'Admirals Club Membership'
    PRIORITY_PASS_SELECT_MEMBERSHIP_LEFT_PARENTHESIS_PRESTIGE_RIGHT_PARENTHESIS = 'Priority Pass Select Membership (Prestige)'
    PRIORITY_PASS_SELECT_MEMBERSHIP_LEFT_PARENTHESIS_STANDARD_PLUS_RIGHT_PARENTHESIS = 'Priority Pass Select Membership (Standard Plus)'
    DAILY_BREAKFAST = 'Daily Breakfast'
    EARLY_CHECK_MINUS_IN_AMPERSAND__LATE_CHECK_MINUS_OUT = 'Early Check-in & Late Check-out'
    ROOM_UPGRADES = 'Room Upgrades'
    COMPLEMENTARY_WIFI = 'Complementary WiFi'
    AMEX_HOTEL_COLLECTION_CREDIT = 'Amex Hotel Collection Credit'
    TEMPORARY_ACCOUNT_NUMBERS = 'Temporary Account Numbers'
    ONE_MINUS_TIME_50_PERCENT__DISCOUNT_ON_COMPANION_TICKET = 'One-Time 50% Discount on Companion Ticket'
    AIRLINE_TRAVEL_CREDIT = 'Airline Travel Credit'
    UNITED_CLUB_MEMBERSHIP = 'United Club Membership'
    CHIP_TECHNOLOGY = 'Chip Technology'
    EARN_MORE_MILES_FOR_SHARING_TRAVEL_STORIES = 'Earn More Miles for Sharing Travel Stories'
    MASTERCARD_WORLD_ELITE_CONCIERGE_AND_LUXURY_TRAVEL_BENEFITS = 'Mastercard World Elite Concierge and Luxury Travel Benefits'
    ENUM_20_PERCENT__SAVINGS_ON_DELTA_IN_MINUS_FLIGHT_PURCHASES = '20% Savings on Delta In-Flight Purchases'
    ENUM_25_PERCENT__SAVINGS_ON_UNITED_IN_MINUS_FLIGHT_FOOD_AND_DRINK_PURCHASES = '25% Savings on United In-Flight Food and Drink Purchases'
    DOLLAR_100_HILTON_PROPERTIES_CREDIT = '$100 Hilton Properties Credit'
    DOLLAR_250_HILTON_RESORT_CREDIT = '$250 Hilton Resort Credit'
    HILTON_HONORS_DIAMOND_MEMBERSHIP = 'Hilton Honors Diamond Membership'
    FREE_BIRTHDAY_GIFT = 'Free Birthday Gift'
    ENUM_2X_POINTS_DURING_YOUR_BIRTHDAY_MONTH = '2x Points During Your Birthday Month'
    CAR_RENTAL_VIP_PERKS = 'Car Rental VIP Perks'
    FREE_SHIPPING_WITH_THE_PURCHASE_OF_A_BRA = 'Free shipping with the purchase of a bra'
    MONTHLY_DINING_CREDIT = 'Monthly Dining Credit'
    AMAZON_PRIME_STUDENT = 'Amazon Prime Student'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of CardBenefit from a JSON string"""
        return cls(json.loads(json_str))


