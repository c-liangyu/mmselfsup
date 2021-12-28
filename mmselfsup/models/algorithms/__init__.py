# Copyright (c) OpenMMLab. All rights reserved.
from .base import BaseModel
from .byol import BYOL
from .classification import Classification
from .deepcluster import DeepCluster
from .densecl import DenseCL
from .mae import MAE
from .moco import MoCo
from .npid import NPID
from .odc import ODC
from .relative_loc import RelativeLoc
from .rotation_pred import RotationPred
from .simclr import SimCLR
from .simsiam import SimSiam
from .swav import SwAV
from .vit_classification import VitClassification

__all__ = [
    'BaseModel', 'BYOL', 'Classification', 'DeepCluster', 'DenseCL', 'MoCo',
    'NPID', 'ODC', 'RelativeLoc', 'RotationPred', 'SimCLR', 'SimSiam', 'SwAV',
    'MAE', 'VitClassification'
]
