"""
A basic implementation (initial) of AFS data models. AFS data models
can be used by any application which wants to support data interoperability using AFS
"""
from enum import Enum
from typing import Union
from typing import List

from pydantic import BaseModel
from pydantic.config import ConfigDict

from fansipan_afs.afs_change import ChangeTypeClassEnum

#current version
AFS_VERSION="0.1"

class DetectionTypeClassEnum(str, Enum):
    """Types of detection
    """
    OBJECT_DETECTION="object_detection"
    OBJECT_RECOGNITION="object_recognition"
    OBJECT_CLASSIFICATION="object_classification"
    ANOMALY_DETECTION="anomaly_detection"

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

class DetectionModel(BaseModel):
    """Capture detection models
    """
    detectionModelRefId: str =None
    detectionModelName: str = None
    detectionType:DetectionTypeClassEnum=None
    deploymentRefId: str = None
    deploymentInfo: dict= None
    modelInfo:dict=None

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
    domainCategory: str = None
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
