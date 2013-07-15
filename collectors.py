from .conf import ConfigObject
from numpy import random

import argparse
import grequests
import simplejson
import time

class Collector:

    def __init__(self, config_object):
        self.conf = config_object

    def track_collection(self, n=self.conf.n,
                     min_comment=self.conf.min_comment,
                     min_range=self.conf.min_range,
                     max_range=self.conf.min_range):
    t_id_vector = random.randint(min_range, max_range, size=n)
    # these will probably be helpers, but for now.. lambdas!
    r = lambda t_id: grequests.get(track_url.format(id=t_id),
                         params = {'client_id': self.conf.client_id})
    res = map(r, t_id_vector)

    return coll

    def comment_collection(self, tracks):
        t_comm = lambda t_id: grequests.get(self.conf.comment_url.format(id=t_id),
                              params = {'client_id': self.conf.client_id})
        t_ids = [ t.get('id') for t in tracks ]
        collect = map(lambda r: simplejson.loads(r.content),
                    map(t_comm, t_ids))
        return collect


    def pp_results(tc, cc):
        results = 'Tracks: {track_count} Comments: {comment_count}'
        print results.format(track_count=len(tc), comment_count=len(cc))

def main():
    config_object = ConfigObject()
    c = Collector(config_object)
    tc = c.track_collection()
    cc = c.comment_collection(tc)


