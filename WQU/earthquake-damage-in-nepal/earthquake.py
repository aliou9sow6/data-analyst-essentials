import warnings

import wqet_grader

warnings.simplefilter(action="ignore", category=FutureWarning)
wqet_grader.init("Project 4 Assessment")

# Import libraries 
import sqlite3

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from category_encoders import OneHotEncoder
from IPython.display import VimeoVideo
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.utils.validation import check_is_fitted
from sklearn.tree import DecisionTreeClassifier
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OrdinalEncoder

# %load_ext sql
# %sql sqlite:////home/jovyan/nepal.sqlite

# Example: Run SQL query using sqlite3 in Python
conn = sqlite3.connect('/home/jovyan/nepal.sqlite')
query0 = """
SELECT DISTINCT district_id
FROM id_map
LIMIT 5
"""
df = pd.read_sql_query(query0, conn)
print(df)
conn.close()

# Example: Run SQL query using sqlite3 in Python
conn = sqlite3.connect('/home/jovyan/nepal.sqlite')
query1 = """
SELECT count(*) AS number_of_observations_
FROM id_map
WHERE district_id = 1
"""
df_count = pd.read_sql_query(query1, conn)
print(df_count)
conn.close()

# Example: Run SQL query using sqlite3 in Python
conn = sqlite3.connect('/home/jovyan/nepal.sqlite')
query2 = """
SELECT count(*) AS number_of_observations_
FROM id_map
WHERE district_id = 3
"""
df_count_3 = pd.read_sql_query(query2, conn)
print(df_count_3)
conn.close()

# Example: Run SQL query using sqlite3 in Python
conn = sqlite3.connect('/home/jovyan/nepal.sqlite')
query3 = """
SELECT DISTINCT im.building_id AS b_id, 
        bs.*, 
        bd.damage_grade
FROM id_map AS im
JOIN building_structure AS bs ON im.building_id = bs.building_id
JOIN building_damage AS bd ON im.building_id = bd.building_id
WHERE im.district_id = 3
LIMIT 5
"""
df_buildings = pd.read_sql_query(query3, conn)
print(df_buildings)
conn.close()

# Build `wrangle` function 
def wrangle(db_path):
    # Connect to database
    conn = sqlite3.connect(db_path)

    # Construct query
    query = """
        SELECT distinct(i.building_id) AS b_id,
           s.*,
           d.damage_grade
        FROM id_map AS i
        JOIN building_structure AS s ON i.building_id = s.building_id
        JOIN building_damage AS d ON i.building_id = d.building_id
        WHERE district_id = 3
    """
    # Execute query
    # Note: Ensure that the database path is correct
    # Read query results into DataFrame
    df = pd.read_sql(query, conn, index_col="b_id")
    
    # Identify leaky columns
    drop_cols = []
    for col in df.columns:
        if "post_eq" in col:
            drop_cols.append(col)
            
    # Create binary target
    df["damage_grade"] = df["damage_grade"].str[-1].astype(int)
    df["severe_damage"] = (df["damage_grade"] > 3).astype(int)

    # Drop old target
    drop_cols.append("damage_grade")
    
    # Drop the multicollinearlity column
    drop_cols.append("count_floors_pre_eq")
    drop_cols.append("building_id")
    
    # Drop clumns 
    df.drop(columns=drop_cols, inplace=True)
    
    return df

# Example: Run wrangle function
df = wrangle('/home/jovyan/nepal.sqlite')
print(df.shape)
print(df.head())

print(df["severe_damage"].value_counts(normalize=True))


# Plot value counts of `"severe_damage"`
class_counts = df["severe_damage"].value_counts(normalize=True)


plt.figure(figsize=(8, 2))
sns.barplot(x=class_counts.index, y=class_counts, order=[0, 1])

plt.xlabel("severe_damage")
plt.ylabel("Relative Frequency")
plt.title("Kavrepalanchok, Class Balance")

# Don't delete the code below 👇
plt.savefig("images/4-5-6.png", dpi=150)
plt.show()

# Create the boxplot
plt.figure(figsize=(8, 6))
sns.boxplot(x=df["severe_damage"], y=df["plinth_area_sq_ft"])

plt.xlabel("severe Damage")
plt.ylabel("Plinth Area [sq. ft.]")
plt.title("Kavrepalanchok, Plinth Area vs Building Damage")

plt.show()
# Don't delete the code below 👇
plt.savefig("images/4-5-7.png", dpi=150)

roof_pivot = df.pivot_table(
    values="severe_damage",
    index="roof_type",
    aggfunc="mean"
)
roof_pivot

X = df.drop(columns=["severe_damage"]) # Delete the target column
y = df["severe_damage"] # Define the target column
print("X shape:", X.shape)
print("y shape:", y.shape)

X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("X_train shape:", X_train.shape)
print("y_train shape:", y_train.shape)
print("X_val shape:", X_val.shape)
print("y_val shape:", y_val.shape)

acc_baseline = y.value_counts(normalize=True).max()
print("Baseline Accuracy:", round(acc_baseline, 2))

model_lr = make_pipeline(
    OneHotEncoder(use_cat_names=True),
    LogisticRegression(max_iter=1000) 
)
# 
model_lr.fit(X_train, y_train)

# Verify the prescision
train_acc = model_lr.score(X_train, y_train)
val_acc = model_lr.score(X_val, y_val)

print("Training Accuracy:", round(train_acc, 2))
print("Validation Accuracy:", round(val_acc, 2))

lr_train_acc = model_lr.score(X_train, y_train)
lr_val_acc = model_lr.score(X_val, y_val)

print("Logistic Regression, Training Accuracy Score:", lr_train_acc)
print("Logistic Regression, Validation Accuracy Score:", lr_val_acc)

#------------------------------Part----------------------------------------------------
# Create the Decision Tree model
depth_hyperparams = range(1, 16)
training_acc = []
validation_acc = []

for d in depth_hyperparams:
    model_dt = make_pipeline(
        OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1), 
        DecisionTreeClassifier(max_depth=d, random_state=42)
    )
    model_dt.fit(X_train, y_train)

    train_score = model_dt.score(X_train, y_train)
    val_score = model_dt.score(X_val, y_val)

    training_acc.append(train_score)
    validation_acc.append(val_score)

    print(f"Depth {d}: Train Acc = {train_score:.2f}, Val Acc = {val_score:.2f}")
# # Build and train a new decision tree model `final_model_dt`, using the value for `max_depth` 
# # that yielded the best validation accuracy score in your plot above.

# # Define the optimal value of max_depth
# best_depth = depth_hyperparams[np.argmax(validation_acc)]
# # Building et training the final model
# final_model_dt = make_pipeline(
#     OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1),
#     DecisionTreeClassifier(max_depth=best_depth, random_state=42)
# )

# final_model_dt.fit(X_train, y_train)    
# # Verify the accuracy model
# train_acc_final = final_model_dt.score(X_train, y_train)
# val_acc_final = final_model_dt.score(X_val, y_val)
# print(f"Final Model - Max Depth: {best_depth}")


#------------------------------Part----------------------------------------------------
# Plot the training and validation accuracies
# Define the deep values
depth_hyperparams = range(1, 16)

# Plot the validation curve
plt.figure(dpi=150)
plt.plot(depth_hyperparams, training_acc, label="Training Accuracy", marker="o")
plt.plot(depth_hyperparams, validation_acc, label="Validation Accuracy", marker="o")
# Add the label and the title
plt.xlabel("Max Depth")
plt.ylabel("Accuracy Score")
plt.title("Validation Curve, Decision Tree Model")
plt.legend()
# Display the Graph
plt.show()
# Don't delete the code below 👇
plt.savefig("images/4-5-15.png", dpi=150)

# -------------------------------------------------------------------------
# Create the Decision Tree model with the best depth
# Define the optimal value of max_depth
best_depth = depth_hyperparams[np.argmax(validation_acc)]

# Building et training the final model
final_model_dt = make_pipeline(
    OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1),
    DecisionTreeClassifier(max_depth=best_depth, random_state=42)
)

final_model_dt.fit(X_train, y_train)

# Verify the accuracy model
train_acc_final = final_model_dt.score(X_train, y_train)
val_acc_final = final_model_dt.score(X_val, y_val)

# Verify the accuracy model
train_acc_final = final_model_dt.score(X_train, y_train)
val_acc_final = final_model_dt.score(X_val, y_val)
print(f"Final Model - Max Depth: {best_depth}")
print(f"Training Accuracy: {train_acc_final: 2f}")
print(f"Validation Accuracy: {val_acc_final: 2f}")
# Save the final model
wqet_grader.save_model(final_model_dt, "final_model_dt")
# Display the video
VimeoVideo("859870626", width=800, height=450, autoplay=False)
# --------------------------------------------------------------

# Evaluate 
X_test = pd.read_csv("data/kavrepalanchok-test-features.csv", index_col="b_id")
y_test_pred = final_model_dt.predict(X_test)
y_test_pred[:5]

# Communicate the results

feat_imp = pd.Series(
    final_model_dt.named_steps["decisiontreeclassifier"].feature_importances_, 
    index=X_train.columns
)

feat_imp = feat_imp.sort_values()
feat_imp.head()

