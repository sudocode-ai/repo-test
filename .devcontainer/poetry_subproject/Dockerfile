FROM jupyter/base-notebook:latest

# Change user to root to run some sneaky commands
USER root

# Install Git as root
RUN apt-get update && apt-get install -y \
    rsync \
    wget \
    git \
    build-essential \
    libffi-dev \
    libtiff-dev \
    python3 \
    python3-dev \
    python3-pip \
    python3-setuptools \
    python-is-python3 \
    jq \
    curl \
    locales \
    locales-all \
    tzdata \
    pkg-config \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Rust
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"

# Install Poetry globally
ENV POETRY_HOME="/opt/poetry" \
    POETRY_VERSION=1.7.1
RUN curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s /opt/poetry/bin/poetry /usr/local/bin/poetry && \
    chmod +x /usr/local/bin/poetry

# Configure Poetry defaults globally
RUN poetry config virtualenvs.in-project true --local && \
    poetry config virtualenvs.create false --local && \
    poetry config installer.max-workers 10
    
# Example: Allow jovyan to run specific commands without a password
# Here, you would replace '/path/to/command' with the actual command path
# For a more general approach (not recommended for security reasons), you could use:
# jovyan ALL=(ALL) NOPASSWD: ALL
# RUN echo 'jovyan ALL=(ALL) NOPASSWD: /path/to/command' >> /etc/sudoers
# This line is just an example; tailor it to your specific needs
RUN echo 'jovyan ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers

USER jovyan

# Set up the environment variables
ENV PATH="/home/jovyan/.cargo/bin:${PATH}"
ENV PATH="/opt/poetry/bin:${PATH}"

RUN conda --no-plugins  install -c conda-forge nb_conda_kernels && \
    conda --no-plugins  init --all && \
    conda --no-plugins  clean -afy

WORKDIR /workspace

ENTRYPOINT ["/bin/bash", "-c"]
