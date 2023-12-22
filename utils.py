from streamlit_ws_localstorage import injectWebsocketCode, getOrCreateUID
import json
# local_storage = injectWebsocketCode(hostPort='wsauthserver.supergroup.ai/', uid=getOrCreateUID())
def get_local_storage_value(local_key):
    local_storage = injectWebsocketCode(hostPort='wsauthserver.supergroup.ai/', uid=getOrCreateUID())
    local_storage_value = local_storage.getLocalStorageVal(local_key)
    return local_storage_value
def set_local_storage_value(local_key,local_value):
    local_storage = injectWebsocketCode(hostPort='wsauthserver.supergroup.ai/', uid=getOrCreateUID())
    local_storage_value = local_storage.setLocalStorageVal(local_key,local_value)
    return local_storage_value
