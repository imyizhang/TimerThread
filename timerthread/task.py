#!/usr/bin/env python
# -*- coding: utf-8 -*-

import functools

from .scheduler import Scheduler


class task(object):

    def __init__(self, trigger, interval):
        self.trigger = trigger
        self.interval = interval

    def __call__(self, fn):
        @functools.wraps(fn)
        def sched(*args, **kwargs):
            scheduler_kwargs = {
                'trigger': self.trigger,
                'interval': self.interval,
                'fn': fn,
                'args': args,
                'kwargs': kwargs
            }
            return Scheduler.create(**scheduler_kwargs)
        fn.sched = sched
        return fn
