from calibre.customize import FileTypePlugin

class HelloWorld(FileTypePlugin):

    name                = 'Calibre Spotlight' # Name of the plugin
    description         = 'Exposes the Calibre database to macOS Spotlight'
    supported_platforms = ['osx'] # Platforms this plugin will run on
    author              = 'Dan Bailey' # The author of this plugin
    version             = (1, 0, 0)   # The version number of this plugin
    file_types          = {'epub', 'mobi', 'azw'} # The file types that this plugin will be applied to
    on_postprocess      = True # Run this plugin after conversion is complete
    minimum_calibre_version = (0, 7, 53)

    # def run(self, path_to_ebook):
        # from calibre.ebooks.metadata.meta import get_metadata, set_metadata
        # with open(path_to_ebook, 'r+b') as file:
        #    ext  = os.path.splitext(path_to_ebook)[-1][1:].lower()
        #    mi = get_metadata(file, ext)
        #    mi.publisher = 'Hello World'
        #    set_metadata(file, mi, ext)
        # return path_to_ebook