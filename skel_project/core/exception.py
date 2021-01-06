# -*- coding: utf-8 -*-


class PathNotFound(Exception):
    def __init__(self, string=""):
        self.string = string

    def __str__(self):
        return "Path not found: {}".format(self.string)


class MethodNotImplementedError(Exception):
    def __init__(self, string=""):
        self.string = string

    def __str__(self):
        return "Method not implemented: {}".format(self.string)
