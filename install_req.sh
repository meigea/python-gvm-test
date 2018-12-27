#!/bin/bash

PIP_HOME="/usr/local/python3/bin/pip3"
exec "$PIP_HOME" install redis==3.0.1 --index-url https://pypi.tuna.tsinghua.edu.cn/simple && \
git clone https://github.com/greenbone/python-gvm && cd python-gvm && exec "$PIP_HOME" install . && \
git clone https://github.com/martinblech/xmltodict && cd xmltodict && exec "$PIP_HOME" install .