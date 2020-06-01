import os
import pprint

import mutagen
from mutagen.id3 import ID3


def get_mp3_title(file):
    try:
        audio = ID3(file)
        return audio["TIT2"].text[0]
    except KeyError:
        return file
    except mutagen.id3.ID3NoHeaderError:
        return file


def on_env(env, config, files):
    def generate_playlist(directory):
        full_dir = config['docs_dir'] + directory
        for (dirpath, dirnames, filenames) in os.walk(full_dir):
            mp3_files = list(
                map(
                    lambda filename: {
                        "directory": directory,
                        "file": filename,
                        "title": get_mp3_title(full_dir + filename),
                    },
                    filter(lambda filename: filename.endswith(".mp3"), filenames)
                )
            )
            return mp3_files
    env.filters['generate_playlist'] = generate_playlist
    return env
