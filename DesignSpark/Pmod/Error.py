# -*- coding: utf-8 -*-
# Copyright (c) 2017 RS Components Ltd
# SPDX-License-Identifier: MIT License

class Error(Exception):
    """
    Base class for exceptions in this library.
    """
    pass

class portCapabilitySupport(Error):
    """
    Exception raised when a port does not support the module type.
    """

class portCapabilityConflict(Error):
    """
    Exception raised when the port is already using shared GPIO pins.
    """
  
class portInUse(Error):
    """
    Exception raised when the port is already assigned.
    """  

class incorrectPortName(Error):
    """
    Exception raised when the port name given does not exist in the port map.
    """
    
class incorrectModuleName(Error):
    """
    Exception raised when the module name given does not exist in the module map.
    """
