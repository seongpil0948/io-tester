import firebase_admin
from firebase_admin import firestore, credentials, get_app, App
from config import CREDENTIAL_PATH, VENDOR_PROD_COLLECTION


initialized = False



def getFireApp() -> App:
    appName = "fireApp"
    if not initialized:
        credential = credentials.Certificate(CREDENTIAL_PATH)
        print("credential:", credential)
        fireApp = firebase_admin.initialize_app(credential, name=appName)
        print("appName: ", fireApp)
        initialized = True
        return fireApp
    return get_app(name="fireApp")




def existDbVendorProdIds():
    db = firestore.client(getFireApp())
    vendorProdCollection = db.collection(VENDOR_PROD_COLLECTION)
    docs = vendorProdCollection.stream()
    ids: set[str] = set()
    for doc in docs:
        docData = doc.to_dict()
        prodId = docData.get("vendorProdPkgId", None)
        if prodId is None:
            continue
        ids.add(prodId)
    return ids
