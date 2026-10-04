import pathlib


# file suffixes for categorizing by file extensions
image_suffixes = {
  ".jpg",
  ".jpeg",
  ".png",
  ".gif",
  ".webp",
  ".svg",
  ".bmp",
  ".tiff",
  ".tif",
  ".heic",
  ".heif",
  ".avif",
  ".ico",
  ".jfif"
}

document_suffixes = {
  ".pdf",
  ".doc",
  ".docx",
  ".txt",
  ".rtf",
  ".odt",
  ".ppt",
  ".pptx",
  ".odp",
  ".xls",
  ".xlsx",
  ".csv",
  ".ods",
  ".epub",
  ".mobi",
  ".md",
  ".tex"
}

zipped_suffixes = {
  ".zip",
  ".rar",
  ".7z",
  ".tar",
  ".gz",
  ".tgz",
  ".bz2",
  ".xz",
  ".iso",
  ".cab",
  ".z",
  ".lz",
  ".arj"
}

program_suffixes = {
  ".exe",
  ".msi",
  ".app",
  ".dmg",
  ".deb",
  ".rpm",
  ".apk",
  ".aab",
  ".bin",
  ".sh",
  ".bat",
  ".cmd",
  ".ps1",
  ".jar",
  ".appimage",
  ".msix"
}

vid_suffixes = {
  ".mp4",
  ".mkv",
  ".avi",
  ".mov",
  ".wmv",
  ".flv",
  ".webm",
  ".m4v",
  ".mpg",
  ".mpeg",
  ".3gp",
  ".ogv",
  ".mts",
  ".m2ts",
  ".vob"
}

audio_suffixes = {
  ".mp3",
  ".wav",
  ".aac",
  ".flac",
  ".ogg",
  ".m4a",
  ".wma",
  ".opus",
  ".aiff",
  ".mid",
  ".midi",
  ".alac",
  ".pcm",
  ".weba"
}

incomplete_download_suffixes = {
    ".fdmdownload",
    ".crdownload"
}


def organize_folder(target_dir:str):
    path = pathlib.Path(target_dir)
    for item in path.iterdir():
        print(item)

organize_folder("./")
