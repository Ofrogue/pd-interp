# Polish Credit Partial Dependence Plots with bootstrapped confidence intervals

See Molnar 2021 http://arxiv.org/abs/2109.01433 for details.  
Dataset  https://archive.ics.uci.edu/ml/datasets/Polish+companies+bankruptcy+data


Install all required packages in your python environment
```sh
pip install scipy catboost shap seaborn jupyter statsmodels
```
or create a separate conda env
```sh
conda create -n pdenv python==3.9 scipy catboost shap seaborn jupyter statsmodels
conda activate pdenv
```

download dataset
```sh
python download.py
```

See jupyter notebook for examples