"""
A basic implementation (initial) of AFS data models. AFS data models
can be used by any application which wants to support data interoperability using AFS
It is possible to incorporate  standard vocabularies, such as from
https://www.w3.org/TR/vocab-dcat-3/
"""
from datetime import datetime
from enum import Enum
from typing import Union
from typing import List

from pydantic import BaseModel
from pydantic.config import ConfigDict
from pydantic import Field

from fansipan_afs.afs_change import ChangeTypeClassEnum

#current version
AFS_VERSION="0.2"

class DetectionTypeClassEnum(str, Enum):
    """Types of detection
    """
    OBJECT_DETECTION="object_detection"
    OBJECT_RECOGNITION="object_recognition"
    OBJECT_CLASSIFICATION="object_classification"
    ANOMALY_DETECTION="anomaly_detection"

class RegulationClassEnum(str, Enum):
    """Name of some regulations/frameworks
    """
    FDA_21_CFR = "FDA 21 CFR Part 820"
    ISO13485 = "ISO 13485:2016"
    ISO14971 = "ISO 14971:2019"
    ISO_IEC_42001_2023 = "ISO/IEC 42001:2023"
    NISTAI_RMF_10 = "NIST AI RMF 1.0"
    EU_AI_ACT = "EU AI Act"
    ISO31000 = "ISO 31000"
    NISTCSF_20 = "NIST CSF 2.0"
    COBIT = "COBIT"

class ComplianceResultClassEnum(str, Enum):
    """Compliance/Conformity results
    """
    COMPLIANT = "Compliant"
    CONFORMANT = "Conformant"
    NONCOMFORMANT = "Nonconformant"
    NONE = "None"

#application specific detection results schemas as examples
class ObjectDetectionResult(BaseModel):
    """Capture detection results
    """
    classname: str
    score: float = None
    count: int = None

## common afs entities

class AnalyticsSubject(BaseModel):
    """Represent analytics subject
    """
    analyticsSubjectId: str
    specs: dict=None

class ModelComplianceDoc(BaseModel):
    """model compliance doc
    """
    type_: str = Field("afs:ModelComplianceDoc", alias='@type')
    documentId: str
    issuanceDate: Union[float,str]
    expirationDate: Union[float,str]
    issuer: str
    holder: str
    registryId: str
    modelId: str
    complianceScope: dict[RegulationClassEnum,ComplianceResultClassEnum]
    extra: dict=None

class DetectionModel(BaseModel):
    """Capture detection models
    """
    
    detectionModelRefId: str =None
    detectionModelName: str = None
    detectionType: DetectionTypeClassEnum=None
    deploymentRefId: str = None
    deploymentInfo: dict= None
    modelInfo: dict=None
    complianceCert: ModelComplianceDoc = None

class DetectionConfig(BaseModel):
    """Capture detection configurations
    """
    timestamp: float
    analyticsSubject: AnalyticsSubject = None
    domainCategory: str = None
    detectionModel: DetectionModel = None
    config: dict = None

class CommonDetectionResult(BaseModel):
    """For common detection result
    """
    domainCategory: str = None
    detectionResult: Union[ObjectDetectionResult,dict]
    detectionSourceRefId: str = None
    additionalData: dict = None

class FeatureInstance(BaseModel):
    """for analytics features
    """
    featureInstanceId: str
    timestamp: float
    detectionResults: List[CommonDetectionResult] = None
    analyticsSubject: AnalyticsSubject
    domainApplication: str = None
    detectionModel: DetectionModel = None
    detectionConfig: DetectionConfig = None


class FeatureInstances(BaseModel):
    """ List of features
    """
    model_config = ConfigDict(title='Fansipan ATS')
    featureInstances: List[FeatureInstance]

class DataSource(BaseModel):
    """Capture data sources
    """
    name: str=None
    type: str=None
    sourceRefId: str=None
    properties: dict=None

class DataSourceChange(BaseModel):
    """Changes of data source
    """
    timestamp: float
    analyticsSubject: AnalyticsSubject = None
    changeType: ChangeTypeClassEnum = None
    dataSources: List[DataSource]
