# @Author: Daniel Gomes
# @Date:   2022-09-07 17:11:07
# @Email:  dagomes@av.it.pt
# @Copyright: Insituto de Telecomunicações - Aveiro, Aveiro, Portugal
# @Last Modified by:   Daniel Gomes
# @Last Modified time: 2022-11-05 14:01:18
from pydantic import BaseModel
from typing import Dict, List, Optional, Union


class ComponentConfigs(BaseModel):
    domainPlacementId: int = None
    componentName: str
    conf: Dict

class DomainPlacementBase(BaseModel):
    domainId: str
    componentName: str


class DomainPlacementCreate(DomainPlacementBase):
    pass


class DomainPlacement(DomainPlacementBase):
    domainPlacementId: int


class VSIBase(BaseModel):
    vsiId: int
    description: str
    name: str
    vsdId: str
    domainPlacements: List[DomainPlacementBase]
    additionalConf: List[ComponentConfigs]

class VSICreate(VSIBase):
    domainPlacements: List[DomainPlacementCreate]
    
class VSI(VSIBase):
    statusMessage: Optional[str] = None
    altitude: Optional[float] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    radioRange: Optional[float] = None
    mappedInstanceId: str
    ranEndPointId: Optional[str] = None
    status: str
    domainPlacements: List[DomainPlacement]
    #TODO: Return remaining info


#### Utilities Schema ######

class ServiceComposition(BaseModel):
    sliceEnabled: bool = None
    domainId: str = None
    nfvoId: str = None
    status: str



class PrimitiveStatus(BaseModel):
    actionId: Union[int, str] = None
    domainId: str = None
    nfvoId: str = None # id of the operation given by the nfvo
    status: str = None
    output: str = None
    isAlarm: bool = False # Flag to identify the Alarm Day-2 Actions
