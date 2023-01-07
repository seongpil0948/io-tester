import os


def requiredEnv(key: str):
    val = os.environ.get(f"{key}")
    assert val is not None and len(
        val) > 1, f"{key} is required"
    return val


TARGET_REPO_PATH = os.environ.get(
    "TARGET_REPO_PATH", "/Users/sp/Codes/Io/io-front")
ENTRY_URL = os.environ.get("ENTRY_URL", "http://localhost:5173")

CREDENTIAL_PATH = requiredEnv("CREDENTIAL_PATH")

VENDOR_PROD_COLLECTION = u"vendorProduct"
USER_COLLECTION = u"user"

OUT_PATH = os.path.join(os.getcwd(), "out")
if not os.path.exists(OUT_PATH):
    os.makedirs(OUT_PATH)