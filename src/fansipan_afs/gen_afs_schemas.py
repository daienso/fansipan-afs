"""
Generate json schemas of the current versions
"""
import argparse
import json
from pathlib import Path

from fansipan_afs.afs_datamodels import AFS_VERSION, DetectionConfig, FeatureInstances


if __name__ == '__main__':
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--output_dir', default=".", help='print schema')
    args = parser.parse_args()
    #create dir if not exist
    if Path(args.output_dir).exists():
        Path(args.output_dir).mkdir(parents=True,exist_ok=True)
    #create file
    file1 = f'{args.output_dir}/featureinstance_schema_{AFS_VERSION}.json'
    print(f'FeatureInstance schema into {file1}')
    with open(file1, mode="w", encoding="utf-8") as instance_fp:
        json.dump(FeatureInstances.model_json_schema(), instance_fp, indent=4)
    file2 = f'{args.output_dir}/detection_config_schema_{AFS_VERSION}.json'
    print(f'DetectionConfig schema into {file2}')
    with open(file2, mode="w", encoding="utf-8") as config_fp:
        json.dump(DetectionConfig.model_json_schema(), config_fp, indent=4)
    