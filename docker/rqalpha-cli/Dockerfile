# Copyright (c) OHS R&D Development Team.
# Distributed under the terms of the Modified BSD License.

# Ubuntu 16.04 (xenial) from 2017-07-23
# https://github.com/docker-library/official-images/commit/0ea9b38b835ffb656c497783321632ec7f87b60c
FROM rqalpha/minial

LABEL maintainer="LIMC <limc@ohs-sys.com>"

USER root

# libav-tools for matplotlib anim
RUN apt-get update && \
    apt-get install -y --no-install-recommends libav-tools fontconfig && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install TA-lib
RUN wget https://jaist.dl.sourceforge.net/project/ta-lib/ta-lib/0.4.0/ta-lib-0.4.0-src.tar.gz && \
    tar xf ta-lib-0.4.0-src.tar.gz && rm ta-lib-0.4.0-src.tar.gz && \
    cd ta-lib && \
    ./configure --prefix=/usr &&\
    make && make install && \
    rm -rf /home/$NB_USER/ta-lib/

# fix chinese display bug
RUN mkdir /usr/share/fonts/chinese && \
    wget https://static.ricequant.com/data/WenQuanYi%20Micro%20Hei.ttf && \
    mv WenQuanYi\ Micro\ Hei.ttf /usr/share/fonts/chinese/ && \
    fc-cache -fv

USER $NB_UID

# add channels in china
RUN conda config --add channels 'https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/'

# Install Python 3 packages
# Remove pyqt and qt pulled in for matplotlib since we're only ever going to
# use notebook-friendly backends in these images
RUN conda install --quiet --yes \
    'pandas=0.19*' \
    'numexpr=2.6*' \
    'matplotlib=2.0*' \
    'scipy=0.19*' \
    'seaborn=0.7*' \
    'sympy=1.0*' \
    'cython=0.25*' \
    'statsmodels=0.8*' \
    'cloudpickle=0.2*' \
    'dill=0.2*' \
    'h5py=2.6*' \
    'vincent=0.4.*' \
    'beautifulsoup4=4.5.*' \
    'docopt=0.6.*' \ 
    'future=0.16.*' \ 
    'contextlib2=0.5.*' \
    'pyqt=5.6.*' \
    'qt=5.6.*' \
    'raven=6.5.*' \  
    'typing=3.6.*' \ 
    'lxml=4.1.*' \
    'bcolz=1.1.*' \
    'xlrd'  && \
    conda remove --quiet --yes --force qt pyqt && \
    conda clean -tipsy && \
    # Install RQAlpha
    pip install -i https://pypi.tuna.tsinghua.edu.cn/simple rqalpha && \
    rm -rf /home/$NB_USER/.rqalpha/bundle/ && \
    rqalpha update_bundle && \
    # Install RQAlpha libs
    pip install tushare TA-lib pyecharts && \
    rm -rf /home/$NB_USER/.cache/pip/ && \
    #npm cache clean && \
    rm -rf /home/$NB_USER/.cache/yarn && \
    rm -rf /home/$NB_USER/.node-gyp && \
    fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER  

# Import matplotlib the first time to build the font cache.
ENV XDG_CACHE_HOME /home/$NB_USER/.cache/
RUN MPLBACKEND=Agg python -c "import matplotlib.pyplot" && \
    fix-permissions /home/$NB_USER

# fix display bug
RUN echo "backend: Agg" > ~/.config/matplotlib/matplotlibrc && \
    rm -rf ~/.cache/matplotlib && \
    rm -rf ~/.fontconfig && \
    fix-permissions /home/$NB_USER

# Copy default run strategy file
COPY run_strategy.sh /usr/local/bin/

# Switch back to rqalpha to avoid accidental container runs as root
USER $NB_UID
