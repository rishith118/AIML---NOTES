import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:\Users\RISHITH\Downloads\ai_student_impact_dataset (1).csv")
sns.set_palette("Pastel1")
sns.pairplot(df)
plt.show()