from qlib.data.dataset.loader import StaticDataLoader
from qlib.data import D
from qlib.constant import REG_CN
from qlib.tests.data import GetData
import qlib


def removeDot(code: str):
    return code.replace(".", "")


if __name__ == "__main__":
    provider_uri = "~/.qlib/qlib_data/cn_data"  # target_dir
    GetData().qlib_data(target_dir=provider_uri, region=REG_CN, exists_skip=True)
    qlib.init(provider_uri=provider_uri, region=REG_CN)
    data = StaticDataLoader(config={"feature": "../getData/res1.csv"})
    resDF = data.load()
    resDF = resDF.rename_axis(['instrument', 'datetime'])
    index_list = resDF.index.levels[0].tolist()
    instruments = list(map(removeDot, index_list))
    fields = ["Ref($close,40)-$close", "Ref($close,30)-$close",
              "Ref($close,20)-$close", "Ref($close,10)-$close"]
    data = D.features(instruments, fields, start_time="2014-01-01",
                      end_time="2022-12-31", freq="day")
    total = resDF.join(data, how="left")
    print(total)
