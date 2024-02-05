from utils import from_buffer,from_path,from_url
import platform

class PyjPDFExtract:
    """
    PyjPDF is a class that provides methods for creating PDF documents from various sources.
    """

    def __init__(self):
        if platform.system() != 'Windows':
            raise Exception('PyjPDF is only available for Windows for now')

    def from_buffer(self, stream, *args, **kwargs):
        """
        Load a PDF document from a buffer.

        Args:
            stream: The buffer containing the PDF data.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            The created PDF object.
        """
        return from_buffer(stream, *args, **kwargs)
    
    def from_file(self, path, *args, **kwargs):
        """
        Load a PDF document from a file path.

        Args:
            path (str): The path to the PDF file.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            The loaded PDF document.

        """
        return from_path(path, *args, **kwargs)

    def from_url(self, url, *args, **kwargs):
        """
        Load a PDF document from a URL.

        Args:
            url (str): The URL of the PDF document.
            *args: Additional positional arguments to pass to the underlying `from_url` function.
            **kwargs: Additional keyword arguments to pass to the underlying `from_url` function.

        Returns:
            The loaded PDF document.

        """
        return from_url(url, *args, **kwargs)