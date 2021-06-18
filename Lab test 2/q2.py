import pandas as pd
df = read_csv("https://www.google.com/url?q=https://drive.google.com/file/d/1v9cCym1JfO7XarlZ3ZrPzRWlKFxy24dW/view?usp%3Dsharing&sa=D&source=editors&ust=1623926421842000&usg=AFQjCNHyqTOQrqYARrLfszbGQ-YFef4nXg",skipinitialspace = True)

X=df['text']
y=df['class']
df.text=df['text'].apply(preprocess_text)
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.4, random_state=42)
from sklearn.naive_bayes import GaussianNB 
from sklearn.metrics import accuracy_score 
gnb = GaussianNB()
pred = gnb.fit(X_train, y_train).predict(X_test)
print("Naive-Bayes accuracy :",accuracy_score(y_test,pred, normalize = True))