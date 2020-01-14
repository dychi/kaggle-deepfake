from __future__ import print_function
import os
import sys
import json
import subprocess
import pandas as pd

if __name__ == "__main__":
    # 動画のパス
    dir_path = sys.argv[1]
    # jpg書き出し先のディレクトリパス
    dst_dir_path = sys.argv[2]

    # metadata.jsonからラベルの取り出し
    metadata_json = json.load(open(os.path.join(dir_path, "metadata.json"), encoding='utf8'))
    metadata_df = pd.DataFrame(metadata_json).transpose()
    print(metadata_df)

    for dirname, _, filenames in os.walk(dir_path):
        for filename in filenames:
            print("Video File Name:", filename)
            # 動画のラベル
            video_label = metadata_df.loc[filename]['label'].lower()
            # 動画ラベルのディレクトリパス
            video_label_path = os.path.join(dst_dir_path, video_label)
            if ".mp4" not in filename:
                continue
            name, ext = os.path.splitext(filename)
            # 動画ごとの書き出し先ディレクトリ
            dst_video_dir_path = os.path.join(video_label_path, name)
            # 作成する元動画ディレクトリのパス
            video_file_path = os.path.join(dirname, filename)

            try:
                # label名のディレクトリが存在しているか確認
                if os.path.exists(video_label_path):
                    print("label dirあり")
                else:
                    os.mkdir(video_label_path)
                # 動画の書き出し先ディレクトリの確認
                if os.path.exists(dst_video_dir_path):
                    if not os.path.exists(os.path.join(dst_video_dir_path, 'image_00001.jpg')):
                        subprocess.call("rm -r {}".format(dst_video_dir_path), shell=True)
                        print("Remove {}".format(dst_video_dir_path))
                        os.mkdir(dst_video_dir_path)
                    else:
                        continue
                else:
                    os.mkdir(dst_video_dir_path)
            except:
                continue
            # ローカルでのテスト
            # cmd = 'touch {0}/image_%05d.jpg'.format(dst_directory_path)
            # 動画の書き出し
            cmd = 'ffmpeg -i \"{0}\" -vf scale=-1:360 \"{1}/image_%05d.jpg\"'.format(video_file_path, dst_video_dir_path)
            print(cmd)
            subprocess.call(cmd, shell=True)
            print('\n')
            if video_label == 'real':
                break
