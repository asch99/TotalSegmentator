FROM nvcr.io/nvidia/pytorch:20.10-py3

RUN apt-get update
# Needed for fury vtk. ffmpeg also needed
RUN apt-get install ffmpeg libsm6 libxext6 -y
RUN apt-get install xvfb -y

RUN pip install flask gunicorn

# prevent error for SKLEARN
ENV SKLEARN_ALLOW_DEPRECATED_SKLEARN_PACKAGE_INSTALL=True

# force download to specific folder
ENV TOTALSEG_WEIGHTS_PATH /appdata

# allow generate once
ENV MPLCONFIGDIR /appdata

# installing pyradiomics results in an error in github actions
# RUN pip pyradiomics

COPY . /app
RUN pip install /app

RUN python /app/totalsegmentator/download_pretrained_weights.py

# create fontlist once
RUN python -c "import matplotlib.pyplot as plt; fig = plt.figure()"

# make accessible
RUN chmod -R a+rw /appdata

# expose not needed if using -p
# If using only expose and not -p then will not work
# EXPOSE 80