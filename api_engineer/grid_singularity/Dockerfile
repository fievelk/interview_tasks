FROM python:3.8

# Force the stdout and stderr streams to be unbuffered. Send the python output
# (e.g. container log) straight to terminal () without being first buffered.
ENV PYTHONUNBUFFERED=1

# Get the CONTAINER_ROOT_DIR env variable declared in docker-compose.yml
ARG CONTAINER_ROOT_DIR

# Install packages needed for scipy features
RUN apt-get update && \
  apt-get install -y \
  libblas-dev \
  liblapack-dev

# Create and cd into the main source code directory
RUN mkdir ${CONTAINER_ROOT_DIR}
WORKDIR ${CONTAINER_ROOT_DIR}

# Copy and install requirement files
COPY requirements.txt ${CONTAINER_ROOT_DIR}/
RUN pip install -r requirements.txt

COPY . ${CONTAINER_ROOT_DIR}

WORKDIR ${CONTAINER_ROOT_DIR}/grid_challenge/
