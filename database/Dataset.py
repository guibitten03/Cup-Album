import pandas as pd

class Dataset:
    
    def __init__(self) -> None:
        self.stickers_collection = self.read_sticker_data()

    
    def read_sticker_data(self):
        return pd.read_json(path_or_buf = "../.data/players_reshape.json").to_dict()


# if __name__ == "__main__":
#     print(Dataset().stickers_collection)