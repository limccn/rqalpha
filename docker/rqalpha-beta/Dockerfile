#Copyright (c) OHS R&D Development Team.
# Distributed under the terms of the Modified BSD License.

# Ubuntu 16.04 (xenial) from 2017-07-23
# https://github.com/docker-library/official-images/commit/0ea9b38b835ffb656c497783321632ec7f87b60c
FROM rqalpha/cli

LABEL maintainer="LIMC <limc@ohs-sys.com>"

USER root

# update pandas
RUN conda install --quiet --yes \
    'pandas=0.22.0' \
    'numpy=1.14.2' && \
    conda clean -tipsy

# Install all OS dependencies for fully functional notebook server
COPY start_beta.sh /usr/local/bin/
COPY data2json.py /usr/local/bin/

# Switch back to rqalpha to avoid accidental container runs as root
USER $NB_UID
