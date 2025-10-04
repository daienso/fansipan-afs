"""
Transform detection results to AFS
Specific classes must be implemented for doing the transformation
"""
from abc import ABC


class AFSResultTransform (ABC):
    """
    This kind of mapping is based on the detection. it cannot be automated
    """
    @staticmethod
    def transform(input_detection_result:dict, afs_domain_category:str, afs_class_name:str,
                  filtered_domain_category_instance=None,
                  filtered_domain_category_result=None,filtered_classname=None):
        """ Specific transform function must be implemented by the developer
        """
