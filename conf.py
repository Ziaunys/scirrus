class ConfigObject(object):

    client_id = '6482e060ad0be4c70ee8cf6df6ff7aeb'
    comment_url = 'https://api.soundcloud.com/comments/{id}.json'
    track_url = 'https://api.soundcloud.com/tracks/{id}.json'
    min_range = 100
    max_range = 50000

    def __init__(self, args):
        parser = argparse.ArgumentParser()
        parser_options = [('-k', {'type': int, 'default': 3,
                                'help': "the number of desired clusters"}),
                          ('-n', {'type': int, 'default': 30,
                                'help': "the number of tracks to use"}),
                          ('--min_comment', {'type': int, 'default': 10,
                                'help': "min required comments per track"}),]
        [ parser.add_argument(arg, **opts) for (arg, opts) in parser_options ]
        args = parser.parse_args()
        self.__dict__.update(dict(args._get_kwargs()))





