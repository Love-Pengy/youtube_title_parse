# -*- coding: utf-8 -*-
"""
Remove common fluff
"""
import re


def clean_common_fluff(title):
    """
    Clean common fluff from title
    """
    # Sub Pop includes "(not the video)" on audio tracks.
    # The " video" part might be stripped by other plugins.
    title = re.sub(r"\(not the( video)?\)\s*$", "", title)
    # Lyrics videos
    title = re.sub(
        r"(\s*[-~_/]\s*)?\b(with\s+)?lyrics\s*", "", title, flags=re.IGNORECASE
    )
    title = re.sub(r"\(\s*(with\s+)?lyrics\s*\)\s*", "", title, flags=re.IGNORECASE)
    title = re.sub(r"\s*\(\s*\)", "", title)  # ()
    # (Visualizer)
    title = re.sub(r"\([Vv]{1}isualizer\)", "", title)    
    # (Official Audio)
    title = re.sub(r"\([Oo]{1}fficial [Aa]{1}udio\)", "", title)
    return title.strip()
