# Kaggle DeepFake Competition

## FFmpeg
```shell
wget http://johnvansickle.com/ffmpeg/releases/ffmpeg-release-64bit-static.tar.xz
tar xvf ffmpeg-release-64bit-static.tar.xz
cd ./ffmpeg-3.3.3-64bit-static/; sudo cp ffmpeg ffprobe /usr/local/bin;
```

on kaggle notebook
```
!tar xvf ../input/ffmpeg-static-build/ffmpeg-git-amd64-static.tar.xz
```

on mac
```shell script
brew install ffmpeg
```


## Directory 
```
.
└── data
    └── jpg_video_directory
        ├── fake
        │   └── (video names)
        │       ├── (jgp files)
        └── real
            └── (video names)
                ├── (jgp files)
```