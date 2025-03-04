from setuptools import setup, find_packages

setup(name='TotalSegmentator',
        version='1.4.0',
        description='Robust segmentation of 104 classes in CT images.',
        long_description="See Readme.md on github for more details.",
        url='https://github.com/wasserth/TotalSegmentator',
        author='Jakob Wasserthal',
        author_email='jakob.wasserthal@usb.ch',
        python_requires='>=3.5',
        license='Apache 2.0',
        packages=find_packages(),
        install_requires=[
            'numpy',
            'psutil',
            # Any version <2.1.0 because of this issue: 
            # https://github.com/SimpleITK/SimpleITK/issues/1433
            # AS: skip it, just use dcm2niix for conversion
            #'SimpleITK==2.0.2',
            'nibabel>=2.3.0',
            'tqdm>=4.45.0',
            'p_tqdm',
            'xvfbwrapper',
            'fury',
            'batchgenerators==0.21',
            # This does not work if want to upload to pypi
            # 'nnunet @ git+https://github.com/wasserth/nnUNet_cust@working_2022_03_18#egg=nnUNet'
            'nnunet-customized==1.1',
            'requests',
            # for conversion of dicom to nii.gz
            'dcm2niix',
            'nipype'
        ],
        zip_safe=False,
        classifiers=[
            'Intended Audience :: Science/Research',
            'Programming Language :: Python',
            'Topic :: Scientific/Engineering',
            'Operating System :: Unix',
            'Operating System :: MacOS'
        ],
        scripts=[
            'bin/TotalSegmentator', 'bin/totalseg_combine_masks', 'bin/TotalSegmentator_dicom'
        ]
    )
