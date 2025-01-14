#   Copyright (c) 2020 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from .auto_cast import auto_cast  # noqa: F401
from .auto_cast import decorate  # noqa: F401
from .auto_cast import amp_guard  # noqa: F401
from .auto_cast import amp_decorate  # noqa: F401
from .auto_cast import low_precision_op_list  # noqa: F401
from .auto_cast import FP16_WHITE_LIST  # noqa: F401
from .auto_cast import FP16_BLACK_LIST  # noqa: F401
from .auto_cast import PURE_FP16_WHITE_LIST  # noqa: F401
from .auto_cast import PURE_FP16_BLACK_LIST  # noqa: F401

from . import grad_scaler  # noqa: F401
from .grad_scaler import GradScaler  # noqa: F401
from .grad_scaler import AmpScaler  # noqa: F401
from .grad_scaler import OptimizerState  # noqa: F401

__all__ = ['auto_cast', 'GradScaler', 'decorate']
