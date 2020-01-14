from __future__ import print_function
import os
import sys
import subprocess

if __name__ == "__main__":
    # 動画のパス
    dir_path = sys.argv[1]
    # jpg書き出し先のディレクトリパス
    dst_dir_path = sys.argv[2]

    for dirname, _, filenames in os.walk(dir_path):
        for filename in filenames:
            if ".mp4" not in filename:
                continue
            name, ext = os.path.splitext(filename)
            # 動画ごとの書き出し先ディレクトリ
            dst_directory_path = os.path.join(dst_dir_path, name)
            # 作成するディレクトリ(動画名)のパス
            video_file_path = os.path.join(dirname, filename)

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
                continue
            # ローカルでのテスト
            # cmd = 'touch {0}/image_%05d.jpg'.format(dst_directory_path)
            # 動画の書き出し
            cmd = 'ffmpeg -i \"{0}\" -vf scale=-1:360 \"{1}/image_%05d.jpg\"'.format(video_file_path, dst_directory_path)
            print(cmd)
            subprocess.call(cmd, shell=True)
            print('\n')
            break
