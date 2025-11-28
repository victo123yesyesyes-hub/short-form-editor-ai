import moviepy.editor as mp
import uuid

def apply_zoom(clip, factor=1.1):
    return clip.fx(mp.vfx.zoom_in, factor)

def apply_color_match(clip, ref_clip):
    ref_frame = ref_clip.get_frame(1)
    avg_color = ref_frame.mean(axis=0).mean(axis=0)
    return clip.fx(mp.vfx.colorx, 1.1)

def process_video(user_video, ref_video=None, options={}):
    id = str(uuid.uuid4())
    output_path = f"/tmp/{id}.mp4"

    clip = mp.VideoFileClip(user_video)

    if options.get("zoom"):
        clip = apply_zoom(clip)

    if ref_video:
        ref = mp.VideoFileClip(ref_video)
        if options.get("match_color"):
            clip = apply_color_match(clip, ref)

    clip.write_videofile(output_path, codec="libx264")

    return output_path

def handler(inputs):
    user_video = inputs["user_video"]
    ref_video = inputs.get("reference_video")
    options = inputs.get("options", {})

    output = process_video(user_video, ref_video, options)

    return {"output_video": output}
