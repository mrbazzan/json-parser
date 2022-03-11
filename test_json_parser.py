
import sys
import os
import json_parser


def json_load(stream_fd, chunk_size=1024):

    def read_chunk():
        while True:
            chunk = os.read(stream_fd, chunk_size)
            if chunk:
                yield chunk
            else:
                break
    return json_parser.parse_json(text_iter=read_chunk())


for data in json_load(sys.stdin.fileno()):
    print(data)
    sys.exit()
