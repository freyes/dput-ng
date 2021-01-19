# -*- coding: utf-8 -*-
"""
FTPS Uploader implementation.
"""

import dput.uploaders.ftp

class FtpsUploader(dput.uploaders.ftp.FtpUploader):
    def initialize(self, **kwargs):
        super().initialize(**kwargs, use_tls=True)
