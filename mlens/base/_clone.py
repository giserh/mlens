#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""ML-ENSEMBLE

author: Sebastian Flennerhag
date: 10/01/2017
licence: MIT
Support functions for cloning ensemble estimators
"""

from __future__ import division, print_function

from ._setup import check_estimators, _check_names
from sklearn.base import clone


def _clone_base_estimators(base_estimators, as_dict=True):
    """Created named clones of base estimators for fitting"""
    if as_dict:
        return {case: [(est_name, clone(est)) for est_name, est in
                       _check_names(estimators)]
                for case, estimators in base_estimators}
    else:
        return [(case, [(est_name, clone(est)) for est_name, est in
                        _check_names(estimators)])
                for case, estimators in base_estimators]


def _clone_preprocess_cases(preprocess):
    """Created named clones of base preprocessing pipes for fitting"""
    if preprocess is None:
        return

    if isinstance(preprocess, dict):
        return [(case, [clone(trans) for trans in
                check_estimators(process_pipe)])
                for case, process_pipe in preprocess.items()]
    else:
        return [(case, [clone(trans) for trans in
                check_estimators(process_pipe)])
                for case, process_pipe in preprocess]