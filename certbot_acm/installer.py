"""Let's Encrypt ACM installer plugin."""

from __future__ import print_function

import logging

import zope.interface

import boto3
import botocore

from certbot import interfaces
from certbot.plugins import common


logger = logging.getLogger(__name__)


class Installer(common.Plugin):
    zope.interface.implements(interfaces.IInstaller)
    zope.interface.classProvides(interfaces.IPluginFactory)

    description = "ACM installer"

    def __init__(self, *args, **kwargs):
        super(Installer, self).__init__(*args, **kwargs)

    def deploy_cert(self, domain, cert_path, key_path, chain_path, fullchain_path):
        """
        Upload Certificate to ACM
        """
        client = boto3.client('acm')
