#!/usr/bin/env python

from lib.component.business.business_base import BusinessBase
from lib.component.business.project.pou.instructions.floating_point_math.add_real import AddReal
from lib.component.business.project.pou.instructions.floating_point_math.divide_real import DivideReal
from lib.component.business.project.pou.instructions.floating_point_math.square_root import SquareRoot
from lib.component.business.project.pou.instructions.floating_point_math.subtract_real import SubtractReal
from lib.component.business.project.pou.instructions.floating_point_math.multiply_real import MultiplyReal
from lib.component.business.project.pou.instructions.floating_point_math.pid_calculation import PIDCalculation
from lib.component.business.project.pou.instructions.floating_point_math.sine_calculation import SineCalculation
from lib.component.business.project.pou.instructions.floating_point_math.cosine_calculation import CosineCalculation
from lib.component.business.project.pou.instructions.floating_point_math.tangent_calculation import TangentCalculation
from lib.component.business.project.pou.instructions.floating_point_math.natural_logarithm_calculation import \
    NaturalLogarithmCalculation
from lib.component.business.project.pou.instructions.floating_point_math.natural_exponential_calculation import \
    NaturalExponentialCalculation


class FloatingPointMathCollector(BusinessBase):
    """Floating-Point Math instructions collector class.
    Args:
    Example:
    Return:
    Author: cai, yong
    IsInterface: False
    ChangeInfo: cai, yong 2019-12-05
    """

    def __init__(self, own_software, params=None):
        super(FloatingPointMathCollector, self).__init__(own_software, params)

    @property
    def add_config(self):
        """[business type -- business class] config dict.
        Args:
        Example:
        Return:
        Author: cai, yong
        IsInterface: False
        ChangeInfo: cai, yong 2019-12-05
        """

        config = {
            'add_real': AddReal,
            'subtract_real': SubtractReal,
            'multiply_real': MultiplyReal,
            'divide_real': DivideReal,
            'square_root': SquareRoot,
            'sine_calculation': SineCalculation,
            'cosine_calculation': CosineCalculation,
            'tangent_calculation': TangentCalculation,
            'natural_logarithm_calculation': NaturalLogarithmCalculation,
            'natural_exponential_calculation': NaturalExponentialCalculation,
            'pid_calculation': PIDCalculation
        }

        return config
