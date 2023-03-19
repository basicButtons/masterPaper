#  Copyright (c) Microsoft Corporation.
#  Licensed under the MIT License.
"""
Qlib provides two kinds of interfaces. 
(1) Users could define the Quant research workflow by a simple configuration.
(2) Qlib is designed in a modularized way and supports creating research workflow by code just like building blocks.

The interface of (1) is `qrun XXX.yaml`.  The interface of (2) is script like this, which nearly does the same thing as `qrun XXX.yaml`
"""
import qlib
from qlib.constant import REG_CN
from qlib.utils import init_instance_by_config, flatten_dict
from qlib.workflow import R
from qlib.workflow.record_temp import SignalRecord, PortAnaRecord, SigAnaRecord
from qlib.tests.data import GetData
from qlib.tests.config import CSI300_BENCH, CSI300_GBDT_TASK
from qlib.data import D
from utils import removerDotCodeList


def entry():
    instruments = ["sz000001"]
    fields = [
        "P($$assettoequity_q)",
        # "P(Ref($$assettoequity_q,1))",
        # "P(Ref($$assettoequity_q,4))",
        "P($$assetturnratio_q)",
        # "P(Ref($$assetturnratio_q,1))",
        # "P(Ref($$assetturnratio_q,4))",
        "P($$cfotogr_q)",
        # "P(Ref($$cfotogr_q,1))",
        # "P(Ref($$cfotogr_q,4))",
        "P($$cfotonp_q)",
        # "P(Ref($$cfotonp_q,1))",
        # "P(Ref($$cfotonp_q,4))",
        "P($$cfotoor_q)",
        # "P(Ref($$cfotoor_q,1))",
        # "P(Ref($$cfotoor_q,4))",
        "P($$dupontassetstoequity_q)",
        # "P(Ref($$dupontassetstoequity_q,1))",
        # "P(Ref($$dupontassetstoequity_q,4))",
        "P($$dupontassetturn_q)",
        # "P(Ref($$dupontassetturn_q,1))",
        # "P(Ref($$dupontassetturn_q,4))",
        "P($$dupontnitogr_q)",
        # "P(Ref($$dupontnitogr_q,1))",
        # "P(Ref($$dupontnitogr_q,4))",
        "P($$dupontpnitoni_q)",
        # "P(Ref($$dupontpnitoni_q,1))",
        # "P(Ref($$dupontpnitoni_q,4))",
        "P($$dupontroe_q)",
        # "P(Ref($$dupontroe_q,1))",
        # "P(Ref($$dupontroe_q,4))",
        "P($$epsttm_q)",
        # "P(Ref($$epsttm_q,1))",
        # "P(Ref($$epsttm_q,4))",
        "P($$liabilitytoasset_q)",
        # "P(Ref($$liabilitytoasset_q,1))",
        # "P(Ref($$liabilitytoasset_q,4))",
        "P($$liqashare_q)",
        # "P(Ref($$liqashare_q,1))",
        # "P(Ref($$liqashare_q,4))",
        "P($$mbrevenue_q)",
        # "P(Ref($$mbrevenue_q,1))",
        # "P(Ref($$mbrevenue_q,4))",
        "P($$netprofit_q)",
        # "P(Ref($$netprofit_q,1))",
        # "P(Ref($$netprofit_q,4))",
        "P($$npmargin_q)",
        # "P(Ref($$npmargin_q,1))",
        # "P(Ref($$npmargin_q,4))",
        "P($$roeavg_q)",
        # "P(Ref($$roeavg_q,1))",
        # "P(Ref($$roeavg_q,4))",
        "P($$totalshare_q)",
        # "P(Ref($$totalshare_q,1))",
        # "P(Ref($$totalshare_q,4))",
        "P($$yoyepsbasic_q)",
        # "P(Ref($$yoyepsbasic_q,1))",
        # "P(Ref($$yoyepsbasic_q,4))",
        "P($$yoyequity_q)",
        # "P(Ref($$yoyequity_q,1))",
        # "P(Ref($$yoyequity_q,4))",
        "P($$yoyliability_q)",
        # "P(Ref($$yoyliability_q,1))",
        # "P(Ref($$yoyliability_q,4))",
        "P($$yoyni_q)",
        # "P(Ref($$yoyni_q,1))",
        # "P(Ref($$yoyni_q,4))",
        "P($$yoypni_q)",
        # "P(Ref($$yoypni_q,1))",
        # "P(Ref($$yoypni_q,4))",
    ]
    # Mao Tai published 2019Q2 report at 2019-07-13 & 2019-07-18
    # - http://www.cninfo.com.cn/new/commonUrl/pageOfSearch?url=disclosure/list/search&lastPage=index
    data = D.features(instruments, fields, start_time="2015-01-01",
                      end_time="2015-12-31", freq="day")
    print(data)


if __name__ == "__main__":

    # use default data
    provider_uri = "~/.qlib/qlib_data/cn_data"  # target_dir
    GetData().qlib_data(target_dir=provider_uri, region=REG_CN, exists_skip=True)
    qlib.init(provider_uri=provider_uri, region=REG_CN)

    entry()
    # model = init_instance_by_config(CSI300_GBDT_TASK["model"])
    # dataset = init_instance_by_config(CSI300_GBDT_TASK["dataset"])

    # port_analysis_config = {
    #     "executor": {
    #         "class": "SimulatorExecutor",
    #         "module_path": "qlib.backtest.executor",
    #         "kwargs": {
    #             "time_per_step": "day",
    #             "generate_portfolio_metrics": True,
    #         },
    #     },
    #     "strategy": {
    #         "class": "TopkDropoutStrategy",
    #         "module_path": "qlib.contrib.strategy.signal_strategy",
    #         "kwargs": {
    #             "signal": (model, dataset),
    #             "topk": 50,
    #             "n_drop": 5,
    #         },
    #     },
    #     "backtest": {
    #         "start_time": "2017-01-01",
    #         "end_time": "2020-08-01",
    #         "account": 100000000,
    #         "benchmark": CSI300_BENCH,
    #         "exchange_kwargs": {
    #             "freq": "day",
    #             "limit_threshold": 0.095,
    #             "deal_price": "close",
    #             "open_cost": 0.0005,
    #             "close_cost": 0.0015,
    #             "min_cost": 5,
    #         },
    #     },
    # }

    # # NOTE: This line is optional
    # # It demonstrates that the dataset can be used standalone.
    # example_df = dataset.prepare("train")
    # print(example_df.head())

    # # start exp
    # # with R.start(experiment_name="workflow"):
    # #     R.log_params(**flatten_dict(CSI300_GBDT_TASK))
    # #     model.fit(dataset)
    # #     R.save_objects(**{"params.pkl": model})

    # #     # prediction
    # #     recorder = R.get_recorder()
    # #     sr = SignalRecord(model, dataset, recorder)
    # #     sr.generate()

    # #     # Signal Analysis
    # #     sar = SigAnaRecord(recorder)
    # #     sar.generate()

    # #     # backtest. If users want to use backtest based on their own prediction,
    # #     # please Refer to https://qlib.readthedocs.io/en/latest/component/recorder.html#record-template.
    # #     par = PortAnaRecord(recorder, port_analysis_config, "day")
    # #     par.generate()
