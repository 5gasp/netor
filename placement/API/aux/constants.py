# @Author: Daniel Gomes
# @Date:   2022-08-16 09:40:42
# @Email:  dagomes@av.it.pt
# @Copyright: Insituto de Telecomunicações - Aveiro, Aveiro, Portugal
# @Last Modified by:   Daniel Gomes
# @Last Modified time: 2022-10-29 15:17:21


SECRET_KEY = "99cb3e97787cf81a7f418c42b96a06f77ce25ddbb2f7f83a53cf3474896624f9"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60
DEFAULT_ADMIN_CREDENTIALS = {
    "username": "admin",
    "password": "admin"
}
IDP_ADMIN_USER = "NetOr-Admin"
IDP_TENANT_USER = "NetOr-Tenant"

DB_NAME = None
DB_LOCATION = None
DB_USER = None
DB_PASSWORD = None

RABBITMQ_USER = None
RABBITMQ_PASS = None
RABBITMQ_IP = None
RABBITMQ_PORT = None


REDIS_USER = None
REDIS_PASS = None
REDIS_IP = None
REDIS_PORT = None


IDP_IP = None
IDP_CLIENTID = None
IDP_ClIENT_SECRET = None
IDP_ADMIN_ClIENTSECRET = None
IDP_REALM = None
IDP_CALLBACK_URI = None


DOMAIN_HOST = None
DOMAIN_PORT = None

TOPIC_CREATEVSI = "createVSI"
TOPIC_REMOVEVSI = "removeVSI"
TOPIC_MODIFYVSI = "modifyVSI"
TOPIC_INSTANTIATE_NSI = "instantiateNsi"
TOPIC_DELETE_NSI = "deleteNSI"
TOPIC_ACTION_NS = "actionNs"
TOPIC_ACTION_NSI = "actionNsi"
TOPIC_FETCH_NS_INFO = "getNsInfo"
TOPIC_FETCH_NSI_INFO = "getNsiInfo"
TOPIC_NSI_INFO = "nsiInfo"
TOPIC_ERROR = "errorOccured"
TOPIC_VSI_STATUS = "statusUpdate"


TOPIC_DOMAININFO = "domainInfo"
TOPIC_CATALOGUEINFO = "catalogueInfo"
TOPIC_TENANTINFO = "tenantInfo"
TOPIC_PLACEMENTINFO = "placementInfo"
INFO_TOPICS = [TOPIC_DOMAININFO, TOPIC_CATALOGUEINFO, TOPIC_TENANTINFO]


TOPIC_UPDATE_NFVO_IDS = 'updateResourcesNfvoIds'
TOPIC_ACTION_RESPONSE = 'actionResponse'
EXCHANGE_MGMT = "vsLCM_Management"
QUEUE_COORDINATOR = "vsCoordinator"

CREATING_STATUS = "creating"
FAILING_STATUS = "fail"
TERMINATED_STATUS = "terminated"