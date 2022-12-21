# Changes wrt the original version of https://github.com/wasserth/TotalSegmentator

## DICOM 
Input of a folder of DICOM files is possible with the script ```TotalSegmentator_dicom```
 
It converts the DICOM folder to a nii.gz before the actual run, and reorients the final segmentation to DICOM orientation.

## Vertebrae
An option ```vertebrae``` is added to only run the subtask of vertebrae segmentation.

## multilabel
The multilabel option now creates ```.nii.gz``` files in the indicated folder, instead of a file ```<outputfolder name>.nii```

## docker
Some changes are made to the Docker image.
Users can now run the docker container without root priviliges (if they are in the docker group), which avoids problems of ownership of the segmention results.

The image downloads the pretrained weights to a fixed location so spawning a new container does not redownload the data.
The advised invocation of the docker container is now:
```
docker run --rm --gpus 'device=0' --ipc=host --user $(id -u):$(id -g) -v /absolute/path/to/my/data/directory:/tmp wasserth/totalsegmentator_container:master TotalSegmentator -i /tmp/ct.nii.gz -o /tmp/segmentations
```
