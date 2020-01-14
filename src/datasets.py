import os
import json

from torch.util.data import Dataset


class DFDCDataset(Dataset):
    def __init__(self, data_path):
        self.data_path = data_path

    def __getitem__(self, item):
        with open(os.path.join(self.data_path, item)) as f:
            metadata_json = json.load(f)
        clip = None
        return clip, targets
