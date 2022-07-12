#!/usr/bin/env python3
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
# coding: utf-8
"""
"""

from concurrent.futures import ThreadPoolExecutor
import grpc

from miniature.environment import PORT
from miniature.server import miniature_pb2
from miniature.server import miniature_pb2_grpc


def load_certs():
    """
    :return: (private_key, certificate_chain)
    """
    try:
        private_key = open("cert.key", "rb").read()
        certificate_chain = open("cert.crt", "rb").read()
        return private_key, certificate_chain
    except FileNotFoundError:
        pass


def grpc_setup():
    private_key, certificate_chain = load_certs()
    credentials = grpc.ssl_server_credentials(
        [(private_key, certificate_chain)],
        require_client_auth=True
    )
    composite_credentials = grpc.composite_channel_credentials(credentials)
    return composite_credentials


def main():
    server = grpc.server(ThreadPoolExecutor(max_workers=5))
    composite_credentials = grpc_setup()
    with grpc.secure_channel("localhost:8080", composite_credentials) as channel:
        # ... create stub and do the call
        pass
