# -*- coding: utf-8 -*-


class PathNotFound(Exception):
    def __init__(self, string=""):
        self.string = string

    def __str__(self):
        return f"Path not found: {self.string}"


class MethodNotImplementedError(Exception):
    def __init__(self, string=""):
        self.string = string

    def __str__(self):
        return f"Method not implemented: {self.string}"
