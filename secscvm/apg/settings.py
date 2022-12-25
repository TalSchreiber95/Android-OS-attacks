# -*- coding: utf-8 -*-

"""
settings.py
~~~~~~~~~~~

Configuration options for the pipeline.

"""
import os

# The absolute path to the root folder of this project
_project_path = '../../../'
# The absolute path of the folder containing compiled Java components
_components_path = _project_path + 'java-components/build/'

fromer_dataset = _project_path + "apks/drebin_apps/"
datasets_for_secsvm = 'data_for_niv_avi/train/'
MB4_dataset = 'data_for_niv_avi/train/'

# COM_dataset = _project_path + 'apks/result/mal_train_.json'
# SB_dataset = _project_path + 'apks/result/mal_train_.json'
# MB1_dataset = _project_path + 'apks/result/mal_train_.json'
# MB2_dataset = _project_path + 'apks/result/mal_train_.json'
# MB3_dataset = _project_path + 'apks/result/mal_train_.json'


def _project(base):
    return os.path.join(_project_path, base)


def _components(base):
    return os.path.join(_components_path, base)


config = {
    # Experiment settings
    'models': _project('data/models/'),
    'X_dataset': _project(datasets_for_secsvm+'train_dataset.json'),
    'y_dataset': _project(datasets_for_secsvm+'labels.json'),
    'X_dataset_test': _project(MB4_dataset+'test_dataset.json'),
    'y_dataset_test': _project(MB4_dataset+'labels.json'),
    # 'meta': _project('data/features/apg-meta.json'),
    'indices': _project(''),  # only needed if using fixed indices
    # Java components
    'extractor': _components('extractor.jar'),
    'injector': _components('injector.jar'),
    'template_injector': _components('templateinjector.jar'),
    'cc_calculator': _components('cccalculator.jar'),
    'class_lister': _components('classlister.jar'),
    'classes_file': _project('all_classes.txt'),
    'extractor_timeout': 300,
    'cc_calculator_timeout': 600,
    # Other necessary components
    'android_sdk': '/usr/lib/android-sdk',
    'template_path': _project('template'),
    'mined_slices': _project('mined-slices'),
    'opaque_pred': _project('opaque-preds/sootOutput'),
    'resigner': _project('apk-signer.jar'),
    'feature_extractor': '/home/harel/attacks_to_compare/intriguing-2020/feature-extractor',
    # Storage for generated bits-and-bobs
    'tmp_dir': '/home/harel/intriguing-2020/tmp',
    'ice_box': '/home/harel/intriguing-2020/ice_box',
    'results_dir': '/home/harel/intriguing-2020/res',
    'goodware_location': '/home/harel/ben',
    # Use if apps are stored with a radix (e.g., radix 3: root/0/0/A/00A384545.apk)
    'storage_radix': 0,
    # Miscellaneous options
    'tries': 1,
    'nprocs_preload': 8,
    'nprocs_evasion': 12,
    'nprocs_transplant': 8
}
