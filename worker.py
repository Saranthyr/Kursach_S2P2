import subprocess

import config


def convert(source, name, ext, fps,
            v_bitrate=None, a_bitrate=None,
            width=None, height=None,
            start_time=None, end_time=None, length=None):
    output = name + ext
    command = 'ffmpeg -i ' + source
    if width and height and v_bitrate and a_bitrate:
        command = command + ' -vf scale=' + width\
                  + ':' + height\
                  + ':flags=lanczos,setsar=1:1,fps=' + fps\
                  + ' -b:v ' + v_bitrate + ' -a:b ' + a_bitrate

    if start_time:
        command = command + '-ss ' + start_time
        if end_time:
            command = command + ' -to ' + end_time
        if length:
            command = command + ' -t ' + length

    command = command + ' -c:v libx265 ' + output
    conv = subprocess.run(command, capture_output=True, text=True)
    if ("Error" in str(conv.stderr)) or ("Error" in str(conv.stdout)):
        with open('log.log', 'w') as log:
            log.write(str(conv.stdout))
            log.write(str(conv.stderr))
            log.close()
        return 400
    else:
        thumbnail = config.Config.STORAGE_SETTINGS.thumbnail_folder + name
        comm = "ffmpeg -i " + output + " -ss 00:00:01 -frames:v 1 " + thumbnail + ".png"
        subprocess.run(comm)
        return 200
