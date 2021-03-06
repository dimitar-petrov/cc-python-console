FROM ubuntu

ENV PYENV_ROOT /root/.pyenv
ENV PATH /root/.pyenv/shims:/root/.pyenv/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -yq git mercurial build-essential \
    tzdata zlib1g-dev libssl-dev libbz2-dev libreadline-dev libsqlite3-dev curl && \
    curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash

WORKDIR /code
ENV PYTHON_VERSIONS 3.6.3 2.7.14

COPY test-requirements.txt /code/test-requirements.txt
RUN pyenv install --list
RUN yes | \
    for version in $PYTHON_VERSIONS; do pyenv install $version; done 

RUN pyenv local $PYTHON_VERSIONS && pip install -r /code/test-requirements.txt

ENV GITLAB_SELF_SIGNED_REPO ''
RUN if [ -n $GITLAB_SELF_SIGEND_REPO ]; then \
    openssl s_client -showcerts -connect $GITLAB_SELF_SIGNED_REPO \
    -showcerts </dev/null 2>/dev/null|openssl x509 \
    -outform pem > /usr/local/share/ca-certificates/custom-ss-gitlab.crt; \
    update-ca-certificates; fi

# Add local pypi server for private dependencies
RUN mkdir /root/.pip 
RUN echo '[global]' > /root/.pip/pip.conf
RUN echo 'trusted-host = pypi' >> /root/.pip/pip.conf
RUN echo 'index-url = http://pypi:80' >> /root/.pip/pip.conf