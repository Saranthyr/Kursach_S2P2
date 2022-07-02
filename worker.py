import subprocess
import uuid
import os


def convert(source, output, v_bitrate, a_bitrate, ext, upscale, width, height):
    output = output + ext
    if upscale == 'up':
        result = subprocess.run(['ffmpeg', '-i', source, '-vf',
                                 'scale=' + width + ':' + height + ':flags=lanczos,setsar=1:1',
                                 '-b:v', v_bitrate, '-b:a', a_bitrate, '-c:v',
                                'libx265', output], capture_output=True, text=True)
        with open('log.log', 'w') as log:
            log.write(str(result.stdout))
    if upscale is None:
        result = subprocess.run(['ffmpeg', '-i', source, '-b:v', v_bitrate, '-b:a', a_bitrate, '-c:v',
                                 'libx265', '-o', output], text=True, capture_output=True)
        with open('log.log', 'a') as log:
            log.write(str(result.stderr))
            log.write(str(result.stdout))
