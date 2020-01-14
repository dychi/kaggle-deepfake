import os
import json

from torch.utils.data import Dataset


def make_dataset():
    pass


def detect_face():
    pass


class DFDCDataset(Dataset):
    def __init__(self, data_path):
        self.data_path = data_path
        # データの取得
        self.data = make_dataset()
        # 顔検出を記載
        self.face_detected_data = detect_face()

    def __getitem__(self, item):
        with open(os.path.join(self.data_path, item)) as f:
            metadata_json = json.load(f)
        clip = None
        return clip, targets
