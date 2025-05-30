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

    title = re.sub(r"\(Visualizer\)", "", title, flags=re.IGNORECASE)    
    title = re.sub(r"\(Official Visualizer\)", "", title, flags=re.IGNORECASE)    
    title = re.sub(r"\(Official Audio\)", "", title, flags=re.IGNORECASE)
    title = re.sub(r"\(Audio\)", "", title, flags=re.IGNORECASE)
    title = re.sub(r"\[Official Music Video\]", "", title, flags=re.IGNORECASE)
    title = re.sub(r"\(Official Music Video\)", "", title, flags=re.IGNORECASE)
    title = re.sub(r"\(Mini Version\)", "", title, flags=re.IGNORECASE)
    title = re.sub(r"\(prod. [A-Za-z0-9]+\)", "", title, flags=re.IGNORECASE)
    title = re.sub(r"\(VIP\)", "", title, flags=re.IGNORECASE)
    title = re.sub(r"\(dir. [A-Za-z0-9]+\)", "", title, flags=re.IGNORECASE)
    title = re.sub(r"\(Screensaver\)", "", title, flags=re.IGNORECASE)
    
    if("ft." in title): 
        title = re.sub(r"\(ft. [A-Za-z0-9]+\)", "", title, flags=re.IGNORECASE)
        title = title.split("ft.", 1)[0]
        title = title.split("FT.", 1)[0]
        title = title.split("Ft.", 1)[0]
    elif("feat." in title):  
        title = re.sub(r"\(feat. [A-Za-z0-9]+\)", "", title, flags=re.IGNORECASE)
        title = title.split("feat.", 1)[0]
        title = title.split("Feat.", 1)[0]
        title = title.split("FEAT.", 1)[0]
    
    return title.strip()
