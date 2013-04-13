# -*- coding: utf-8 -*-

from PyQt4 import QtCore


class Parser(object):
    _instance = None
    _column = 0
    _line = 0

    def __new__(this, *args, **kargs):
        if not this._instance:
            this._instance = super(Parser, this).__new__(this, *args, **kargs)
        return this._instance

    def cursorMovement(self, e):
        if _h(e):
            self._column -= 1
        elif _j(e):
            self._line -= 1
        elif _k(e):
            self._line += 1
        elif _l(e):
            self._column += 1
        print((self._line), (self._column), (e.key()))


def _h(event):
    return (event.key() == QtCore.Qt.Key_H)


def _j(event):
    return (event.key() == QtCore.Qt.Key_J)


def _k(event):
    return (event.key() == QtCore.Qt.Key_K)


def _l(event):
    return (event.key() == QtCore.Qt.Key_L)
