""" main goals of EDA are generally:

    Uncover the data structure and determine how it is coded
    Inspect and “get to know” the data by summarizing and visualizing it
    Detect outliers, missing data, and other anomalies and decide how/whether to address these issues
    Find new avenues for analysis and further research
    Prepare for model building or analysis, including the following:
        Check assumptions
        Select features
        Choose an appropriate method 
"""

# Data inspection
print(df.head())

# Data cleaning

# Numerical summarization
df.describe(include = 'all')

# Data visualization

# Categorical variables
# nominal: describe something
# ordinal: inherent ranking
# binary: two possible variations

# Numerical variable
# continuous: measurement
# discrete: counting
        
# Print data types
print(df.dtypes)

# Convert Numerical data types
# Convert Categorical
# int32 int64
# float32 float64
# object
# string
# bool
df['id'] = df['id'].astype("string")

# Ordinal categorical variables
movies['rating'] = pd.Categorical(movies['rating'],['NR', 'G' , 'PG', 'PG-13', 'R'], ordered=True)

# One hot encoding
titanic = pd.get_dummies(data=titanic, columns=['Embarked'])
print(titanic.head())

# How many (non-null) observations do we have?
# How many unique columns/features do we have?
# Which columns (if any) contain missing data?
# What is the data type of each column?
print(heart.info())
print(heart.ca.unique())
heart[heart.isnull().any(axis=1)]

# Plot a single feature
import matplotlib.pyplot as plt 
plt.hist(cars['selling_price'])
plt.show()

# Quantitative variables: central location and spread
# Mean
rentals.rent.mean()
# Median
rentals.rent.median()
# Mode
rentals.rent.mode()
# Trimmed mean
from scipy.stats import trim_mean
trim_mean(rentals.rent, proportiontocut=0.1)  # trim extreme 10%
# Range
rentals.rent.max() - rentals.rent.min()
# Interquartile range
rentals.rent.quantile(0.75) - rentals.rent.quantile(0.25)
from scipy.stats import iqr
iqr(rentals.rent)  # alternative way
# Variance
rentals.rent.var()
# Standard deviation
rentals.rent.std()
# Mean absolute deviation
rentals.rent.mad()

# Quantitative variables: visualization
import matplotlib.pyplot as plt 
import seaborn as sns
# Boxplot for rent
sns.boxplot(x='rent', data=rentals)
plt.show()
plt.close()
# Histogram for rent
sns.histplot(x='rent', data=rentals)
plt.show()
plt.close()

# Categorical variables:
cars.fuel.value_counts()
cars.fuel.value_counts(normalize=True)

import matplotlib.pyplot as plt 
import seaborn as sns
# Bar chart for borough
sns.countplot(x='borough', data=rentals)
plt.show()
plt.close()
# Pie chart for borough
rentals.borough.value_counts().plot.pie()
plt.show()
plt.close()

# Box plot side by side
sns.boxplot(data = df, x = 'school', y = 'G3')
plt.show()

# Create the overlapping histograms here:
plt.hist(scores_urban,normed=True,alpha=0.5,label="Urban",color="blue")
plt.hist(scores_rural,normed=True,alpha=0.5,label="Rural",color="red")
plt.legend()
plt.show()

# Scatter plot, two quantitative variables
plt.scatter(x = housing.price, y = housing.sqfeet)
plt.xlabel('Rental Price (USD)')
plt.ylabel('Area (Square Feet)')
plt.show()

# Covariance matrix
cov_mat_price_sqfeet = np.cov(housing.price, housing.sqfeet)

# Pearson correlation
from scipy.stats import pearsonr
corr_price_sqfeet, p = pearsonr(housing.price, housing.sqfeet)