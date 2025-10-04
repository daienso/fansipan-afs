"""
Domain categories can be defined in different ways. Here we provide a basic
example.
"""
from enum import Enum

class DomainCategoryEnum(str, Enum):
    """Common pre-defined categories as one example. 
    """
    # detected subject -- ds
    PERSON = "afs.ds.person"
    MACHINE = "afs.ds.machine"
    MACHINE_PUMP = "afs.ds.machine.pump"
    MACHINE_MIXER = "afs.ds.machine.mixer"
    TRASH="afs.ds.trash"
    # detection type -- dt
    OBJ_DETECTION = "afs.dt.object_detection"
    FAULT_DETECTION = "afs.dt.fault_detection"
    ANOMALY_DETECTION = "afs.dt.anomaly_detection"
    VIOLATIONS="afs.dt.violations"
    SYSTEM_CHANGES="afs.dt.systemchanges"
    TRENDS="afs.dt.trends"
    SURFACE_DEFECTS="afs.dt.surface_defects"
    STRUCTURE_DEFECTS="afs.dt.structure_defects"
    # analyticssubject -- as
    ASSET = "afs.as.asset"
    SPACE = "afs.as.space"
    ENVIRONMENT = "afs.as.environment"
    CASE= "afs.as.CASE"
    # domain application -- da
    IOC = "afs.da.ioc"
    INCIDENT="afs.da.incident_management"
    SAFETY="afs.da.safety"
    QUALITY_CONTROL="afs.da.quality_control"
    PM_DA = "afs.da.predictive_maintenance"
    OM_DA = "afs.da.operation_management"
    DS_DA = "afs.da.data_sharing"
