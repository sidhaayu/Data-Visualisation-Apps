# 📊 Streamlit Data Visualization App

A simple and beginner-friendly interactive data visualization app built with Streamlit.
This app allows users to upload their own dataset or work with a default sample dataset, then create multiple visualizations by selecting columns directly from the UI.

## 🚀 Features

📥 Upload your own CSV dataset

📂 Or use a built-in default dataset

🔍 Automatic detection of numeric and categorical columns

✏️ Select columns and row ranges interactively

## 📊 Multiple visualization types:

Bar Chart

Line Chart

Area Chart

Scatter Plot

Box Plot

Histogram

### ⚡ Real-time visualization updates

### 🖼 Clean Streamlit-based UI

## 🧰 Technologies Used

Python 3.x

Streamlit

Pandas

NumPy

Matplotlib / Seaborn



## ▶️ How to Run the App
1. Clone the repository
git clone https://github.com/your-username/visualization-app.git
cd visualization-app

2. Create and activate a virtual environment
python -m venv venv


Windows

.\venv\Scripts\activate


Mac/Linux

source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Run the Streamlit app
streamlit run app.py

## 📤 Using the App
1. Uploading a Dataset

Use the sidebar upload box to upload any CSV file.

2. Using the Default Dataset

If no file is uploaded, the app automatically loads a built-in sample dataset.

3. Column Selection

Choose:

X-axis column

Y-axis column

Row range (optional)

4. Choose Visualization Type

Pick from:

Bar Chart

Line Chart

Area Chart

Scatter Plot

Box Plot

Histogram

The visualization updates instantly.

## 📝 Example requirements.txt
streamlit
pandas
numpy
matplotlib
seaborn

## 🛠 Future Enhancements

Add correlation heatmaps

Add color/style customization

Export dashboard as PDF

Add machine learning insights
