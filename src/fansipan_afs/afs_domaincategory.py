"""
Some python enums for using in AFS
"""
from enum import Enum

class DomainCategoryEnum(str, Enum):
    """Common pre-defined categories
    """
    PERSON="app.object.person"
    MACHINE="app.object.machine"
    TRASH="app.object.trash"
    VIOLATIONS="app.behavior.violations"
    SYSTEM_CHANGES="app.behavior.systemchanges"
    TRENDS="app.behavior.trends"
    SURFACE_DEFECTS="app.defects.surface_defects"
    STRUCTURE_DEFECTS="app.defects.structure_defects"
    ASSETS="app.entity.assets"
    SPACES="app.entity.spaces"
    ENVIRONMENTS="app.entity.environments"
    IOC="app.ioc"
    INCIDENT="app.ioc.incident"
    SAFETY="app.ioc.safety"
    QUALITY_CONTROL="app.ioc.qualitycontrol"
    