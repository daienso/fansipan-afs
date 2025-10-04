"""
A simple test program
"""
from datetime import datetime, timedelta
import json
import os
import sys
import uuid

sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

from fansipan_afs.afs_datamodels import AnalyticsSubject, CommonDetectionResult, DetectionConfig, DetectionModel, FeatureInstance, FeatureInstances, ObjectDetectionResult, ComplianceResultClassEnum, ModelComplianceDoc, RegulationClassEnum
from fansipan_afs.afs_domaincategory import DomainCategoryEnum

def test_instances():

    analyticssubject = AnalyticsSubject(analyticsSubjectId='Fansipan')
    detectionmodel = DetectionModel(
        detectionModelRefId="yolo11n.pt")
    object_detection_ex = ObjectDetectionResult(classname='YOLO.Person', score=0.9)
    detection_result_one = CommonDetectionResult(detectionResult=object_detection_ex
        , additionalData={"source": "test", "meta1": {"submeta": "subvalue"}})
    #detectedresult = DetectedResult(detectedresult=[detectedresult_one])
    timestamp = datetime.now().timestamp()
    detection_config=DetectionConfig(timestamp=timestamp, config={"windowlength":10,
                                      "sampingrate":5})
    featureinstance = FeatureInstance(featureInstanceId=str(uuid.uuid4()),
                                      timestamp=timestamp,
                                      domainApplication=DomainCategoryEnum.SAFETY,
                                      analyticsSubject=analyticssubject,
                                      detectionModel=detectionmodel,
                                      detectionResults=[detection_result_one],
                                      detectionConfig=detection_config)
    featureinstances = FeatureInstances(featureInstances=[featureinstance])
    # just a test, model_dump() return a dict of the object
    print(json.dumps(featureinstances.model_dump(exclude_none=True), indent=4))

def test_compliance():
    documentId =str(uuid.uuid4())
    issueDate = datetime.now().isoformat()
    ayear = timedelta(days=365)
    validUtil = (datetime.now() + ayear).isoformat()
    issuer = "IOC"
    holder = "ioc-f01"
    registryId = f'reg:{str(uuid.uuid4())}'
    modelId = "pump_id_04_6dB"
    complianceScope = {RegulationClassEnum.NISTAI_RMF_10:ComplianceResultClassEnum.CONFORMANT}
    #extra: dict=None #inteded use, version, ...
    compliance_doc = ModelComplianceDoc(documentId=documentId,
                                        issuanceDate=issueDate,
                                        expirationDate=validUtil,
                                        issuer=issuer,
                                        holder= holder,
                                        registryId=registryId,
                                        modelId=modelId,
                                        complianceScope=complianceScope)
    print(json.dumps(compliance_doc.model_dump(exclude_none=True,by_alias=True), indent=4))
if __name__ == '__main__':
    print("Instance example")
    test_instances()
    test_compliance()
