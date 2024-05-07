# Set Up Guide 🖥️

1. Run Docker Compose from the Airflow project, which can be found here.
   [https://github.com/PunnyOz2/DS_DE_FinalProject](https://github.com/PunnyOz2/DS_DE_FinalProject.git)

3. Set up a virtual environment (optional but recommended)
   ```python
   # create a virtual environment
   python3 -m venv .venv
   ```

   ```python
   # activate a virtual environment
   # on MacOS or Linux
   source .venv/bin/activate
    ```
4. Install all the necessary packages
   ```python
   pip install redis
   pip install numpy
   pip install pandas
   pip install geopy
   pip install streamlit
   pip install plotly
   pip install pydeck
   ```
5. Run the project using Streamlit 🎉
   ```python
   streamlit run main.py
   # then access your localhost
   ```
