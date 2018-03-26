#Copyright (c) OHS R&D Development Team.
# Distributed under the terms of the Modified BSD License.

# Ubuntu 16.04 (xenial) from 2017-07-23
# https://github.com/docker-library/official-images/commit/0ea9b38b835ffb656c497783321632ec7f87b60c
FROM rqalpha/base

LABEL maintainer="LIMC <limc@ohs-sys.com>"

USER root

# Install all OS dependencies for fully functional notebook server
RUN apt-get update && apt-get install -yq --no-install-recommends \
    build-essential \
    git \
    jed \
    python-dev \
    unzip \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Switch back to rqalpha to avoid accidental container runs as root
USER $NB_UID
