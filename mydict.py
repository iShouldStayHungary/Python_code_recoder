#-*- coding: utf-8 -*-
class Dict(dict):
    def __init__(self,**kw):
        super().__init__(**kw)

    def __getattr(self,key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict object has no attribution")

    def __set__(self, key, value):
        self[key] = value
        