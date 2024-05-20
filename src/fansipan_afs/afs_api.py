"""
Some simple APIs for using AFS
"""
import json

from fansipan_afs.afs_datamodels import AnalyticsSubject, DataSourceChange, DetectionConfig, DetectionModel


class AFSAPI:
    @staticmethod
    def save_detection_config(checkpoint_ts,analytics_subject,
                              domain_category,detection_model,
                              config:dict=None,checkpoint_filename=None):
        config_checkpoint=DetectionConfig(timestamp=checkpoint_ts,
            analyticsSubject=AnalyticsSubject(analyticsSubjectId=analytics_subject),
            domainCategory=domain_category,
            detectionModel=DetectionModel(detectionModelName=detection_model),
            config=config)
        if checkpoint_filename is None:
            checkpoint_filename=f'{analytics_subject}-config-{checkpoint_ts}.json'
        with open(checkpoint_filename,mode="w",encoding="utf-8") as checkpoint_fp:
            json.dump(config_checkpoint.dict(exclude_none=True),checkpoint_fp,indent=4)
    @staticmethod
    def save_datasource_change(checkpoint_ts,analytics_subject,list_datasources,
                               change_type,checkpoint_filename=None):
        """Save changes of data sources
        """
        config_checkpoint=DataSourceChange(timestamp=checkpoint_ts,
            analyticsSubject=AnalyticsSubject(analyticsSubjectId=analytics_subject),
            dataSources=list_datasources,
            changeType=change_type)
        if checkpoint_filename is None:
            checkpoint_filename=f'{analytics_subject}-datasource-{checkpoint_ts}.json'
        with open(checkpoint_filename,mode="w",encoding="utf-8") as checkpoint_fp:
            json.dump(config_checkpoint.dict(exclude_none=True),checkpoint_fp,indent=4)
