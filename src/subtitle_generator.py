def generate_srt(scenes, durations):
    srt = ""
    for i, (text, duration) in enumerate(zip(scenes, durations)):
        start = i * duration
        end = (i + 1) * duration
        srt += f"{i+1}\n"
        srt += f"00:00:{start:02d},000 --> 00:00:{end:02d},000\n"
        srt += f"{text}\n\n"
    with open("assets/subtitles/output.srt", "w") as f:
        f.write(srt)
