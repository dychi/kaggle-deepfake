from __future__ import print_function
import os
import sys
import subprocess

if __name__ == "__main__":
    dir_path = sys.argv[1]
    dst_dir_path = sys.argv[2]

    for dirname, _, filenames in os.walk(dir_path):
        for filename in filenames:
            if ".mp4" not in filename:
                continue
            name, ext = os.path.splitext(filename)
            dst_directory_path = os.path.join(dst_dir_path, name)
            print('Destination Directory:', dst_directory_path)
            video_file_path = os.path.join(dirname, filename)
            # print('Video Path:', video_file_path)

            try:
                if os.path.exists(dst_directory_path):
                    if not os.path.exists(os.path.join(dst_directory_path, 'image_00001.jpg')):
                        subprocess.call("rm -r {}".format(dst_directory_path), shell=True)
                        print("Remove {}".format(dst_directory_path))
                        os.mkdir(dst_directory_path)
                    else:
                        continue
                else:
                    os.mkdir(dst_directory_path)
            except:
                print(dst_directory_path)
                continue
            cmd = 'touch {0}/image_%05d.jpg'.format(dst_directory_path)
            print(cmd)
            subprocess.call(cmd, shell=True)
            print('\n')
            break
