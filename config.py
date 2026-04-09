import os

# ==========================================
# API settings
# ==========================================
# For local testing, define GEMINI_API_KEY as an environment variable.
# WARNING: Never paste API keys in this file or commit to GitHub!
LOCAL_API_KEY = ""

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY") or LOCAL_API_KEY

# ==========================================
# Internal lookup data - brand keywords
# ==========================================
KNOWN_BRANDS = {
    "Samsung": ["samsung", "סמסונג", "galaxy"],
    "Apple": ["apple", "אפל", "iphone", "אייפון", "איפון", "macbook", "airpods"],
    "Google": ["google", "pixel", "גוגל", "פיקסל"],
    "Xiaomi": ["xiaomi", "שיאומי"],
    "Dell": ["dell", "דל"],
    "Lenovo": ["lenovo", "לנובו"],
    "HP": ["hp"],
    "LG": ["lg"],
    "Sharp": ["sharp", "שארפ"],
    "Haier": ["haier", "האייר"],
    "Sony": ["sony", "סוני", "playstation", "ps5"]
}