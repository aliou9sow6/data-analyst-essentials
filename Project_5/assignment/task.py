#Task 6.5.9: Calculate the trimmed variance for the features in df_small_biz. 
# Your calculations should not include the top and bottom 10% of observations. 
# Then create a Series top_ten_trim_var with the 10 features with the largest variance.
import pandas as pd
from typing import List
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.feature_selection import VarianceThreshold
from sklearn.base import BaseEstimator, TransformerMixin


# Task 6.5.9: Calculate the trimmed variance for the features in df_small_biz. Your calculations should not include the top and bottom 10% of observations. Then create a Series top_ten_trim_var with the 10 features with the largest variance.
def calculate_trimmed_variance(df: pd.DataFrame) -> pd.Series:
    # Calculate the lower and upper bounds for trimming
    lower_bound = df.quantile(0.1)
    upper_bound = df.quantile(0.9)

    # Trim the DataFrame
    trimmed = df[(df >= lower_bound) & (df <= upper_bound)]

    # Calculate the variance for each feature
    trimmed_variance = trimmed.var()

    return trimmed_variance

# Calculate the trimmed variance for df_small_biz
trimmed_variance = calculate_trimmed_variance(df_small_biz)

# Create a Series with the 10 features with the largest variance
top_ten_trim_var = trimmed_variance.nlargest(10)
