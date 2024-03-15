# Warehouse Optimization or Prediction

Not working because of low memory for free render tier

[Link to Project](https://unsupervised-learning-cluster-streamlit.onrender.com)

Try cloning
`streamlit run dashboard.py`

![GIF](src/Animation.gif)

Tech Stack:

1. Python

Libraries Used:

1. Pandas
2. Numpy
3. pmdarima.auto_arima
4. Plotly
5. matplotlib
6. streamlit
7. statsmodel.tsa

## About Dataset

The dataset contains historical product demand for a manufacturing company with footprints globally. The company provides thousands of products within dozens of product categories. There are four central warehouses to ship products within the region it is responsible for. Since the products are manufactured in different locations all over the world, it normally takes more than one month to ship products via ocean to different central warehouses. If forecasts for each product in different central with reasonable accuracy for the monthly demand for month after next can be achieved, it would be beneficial to the company in multiple ways.

demand_hist_prod.csv - CSV data file containing product demand for encoded product id's

## Acknowledgements

This dataset is all real-life data and products/warehouse and category information encoded.

## Inspiration

Is it possible to make forecasts for thousands of products (some of them are highly variable in terms of monthly demand) for the the months after next?
