from __future__ import asbsolute_import
from .conf import ConfigObject

import argparse
import random
import requests
import simplejson
import time

# stores configuration options/defaults
config = ConfigObject()

# arbitrary default ranges.
def track_collection(n, min_comment, min_range=100, max_range=50000):
    collect = []
    while True:
        track_id = random.randrange(min_range, max_range, 1)
        r = requests.get(track_url.format(id=track_id),
            params = {'client_id': '6482e060ad0be4c70ee8cf6df6ff7aeb'})
        if r.status_code != 200:
            continue
        track_candid = simplejson.loads(r.content)
        if track_candid['comment_count'] < min_comment:
            continue
        collect.append(track_candid)
        if (len(collect) == n):
            return collect

def comment_collection(tracks):
    track_comm = lambda track_id: requests.get(comment_url.format(id=track_id),
    params = {'client_id': '6482e060ad0be4c70ee8cf6df6ff7aeb'})
    track_ids = [ t.get('id') for t in tracks ]
    collect = map(lambda r: simplejson.loads(r.content),
                map(track_comm, track_ids))
    return collect



tc = track_collection(args.n, args.min_comment)
cc = comment_collection(tc)
def pp_results(tc, cc):
    results = 'Tracks: {track_count} Comments: {comment_count}'
    print results.format(track_count=len(tc), comment_count=len(cc))

# test /me
r = requests.get('https://api.soundcloud.com/users/ziaunys.json',
    params = {'client_id': '6482e060ad0be4c70ee8cf6df6ff7aeb'})

user = simplejson.loads(r.content)

