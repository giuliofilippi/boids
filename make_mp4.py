import os
import moviepy.editor as mpy


def make_mp4(folder):

    file_list = (os.listdir(folder))

    print (file_list)

    if '.DS_Store' in file_list:
        file_list.remove('.DS_Store')

    list.sort(file_list, key=lambda x: int(x.split('_')[1].split('.jpeg')[0]))

    file_list = [folder+'/'+f for f in file_list]

    # Here set the seconds per frame

    # 0.3 average, 0.5 is slow, 0.1 is 10 days per second

    clips = [mpy.ImageClip(m).set_duration(0.1) for m in file_list]

    concat_clip = mpy.concatenate_videoclips(clips, method="compose")
    concat_clip.write_videofile("boids.mp4", fps=24)


make_mp4('animation')
