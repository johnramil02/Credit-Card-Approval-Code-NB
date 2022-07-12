import matplotlib.pyplot as plot
import pandas as pd

# credit_card_0 = pd.read_csv("original dataset 0.csv")
# print(credit_card_0["Debt"]) 

# credit_card_1 = pd.read_csv("original dataset 1.csv")
# print(credit_card_1["Debt"]) 

# #Box Plot for Debt
# plot.suptitle('Debt', fontsize=14, fontweight='bold')
# plot.boxplot((credit_card_1["Debt"], credit_card_0["Debt"]))

# Box Plot for YearsEmployed
# plot.suptitle('Years Employed', fontsize=14, fontweight='bold')
# plot.boxplot((credit_card_1["YearsEmployed"], credit_card_0["YearsEmployed"]))

#Box Plot for CreditScore
# plot.suptitle('Credit Score', fontsize=14, fontweight='bold')
# plot.boxplot((credit_card_1["CreditScore"], credit_card_0["CreditScore"]))

# Box Plot for Income
# plot.suptitle('Income', fontsize=14, fontweight='bold')
# plot.boxplot((credit_card_1["Income"], credit_card_0["Income"]))

# -----------------------------------------------------

# BOXPLOT FOR PREDICTED BY MODEL
pred_credit_card_0 = pd.read_csv("feature_test 0.csv")
print(pred_credit_card_0["Debt"]) 

pred_credit_card_1 = pd.read_csv("feature_test 1.csv")
print(pred_credit_card_1["Debt"]) 

 

# Box Plot for Debt
# plot.suptitle('Debt [Predicted by model]', fontsize=14, fontweight='bold')
# plot.boxplot((pred_credit_card_1["Debt"], pred_credit_card_0["Debt"]))

# Box Plot for YearsEmployed
# plot.suptitle('Years Employed [Predicted by model]', fontsize=14, fontweight='bold')
# plot.boxplot((pred_credit_card_1["YearsEmployed"], pred_credit_card_0["YearsEmployed"]))

#Box Plot for CreditScore
# plot.suptitle('Credit Score [Predicted by model]', fontsize=14, fontweight='bold')
# plot.boxplot((pred_credit_card_1["CreditScore"], pred_credit_card_0["CreditScore"]))

# Box Plot for Income
plot.suptitle('Income [Predicted by model]', fontsize=14, fontweight='bold')
plot.boxplot((pred_credit_card_1["Income"], pred_credit_card_0["Income"]))

plot.xticks([1, 2], ['Approved ', 'Not Approved'])
plot.show()