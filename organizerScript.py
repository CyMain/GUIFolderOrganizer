import pathlib


# file suffixes for categorizing by file extensions

extensions_dict = {
    "Images":{
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
    },
    "Docs":{
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
    },
    "Zipped_Files":{
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
    },
    "Executables":{
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
    },
    "Videos":{
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
    },
    "Audios":{
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
    },
    "Incomplete_Downloads":{
        ".fdmdownload",
        ".crdownload"
    },
    "Code":{
        ".py",
    }
}

class FolderOrganizer():
    def __init__(self, target_path):
        self.target_path = pathlib.Path(target_path)

    def organize_folder(self):
        path = self.target_path
        # keys, values, then check the file ext against each value, and if the file ext
        # is found in the value, then pass the key into a function that makes a folder for that key
        # if it does not exist, and then add the file to that new folder.
        for item in path.iterdir():
            for key, value in extensions_dict.items():
                if item.suffix in value:
                    self.organize(item, key)

    def make_folder(self, folder_type):
        folder_to_make = self.target_path / folder_type
        try:
            folder_new = False
            if not folder_to_make.exists():
                folder_new == True

            folder_to_make.mkdir(exist_ok=True)

            if folder_new:
                print(f"{folder_to_make} successfully created")

            print(folder_to_make, " folder made")
            return folder_to_make
        except:
            print("Could not make: ", folder_to_make)
            raise FolderNotFoundError(f"Could not make: {folder_to_make}")

    def organize(self, item, folder_type):
        target_folder = self.make_folder(folder_type)
        item.move_into(target_folder)






class FolderNotFoundError(Exception):
    """Used when a target directory does not exist."""

    pass
