# Set Up Guide 🖥️

1. Run Docker Compose from the Airflow project, which can be found here.
   [https://github.com/PunnyOz2/DS_DE_FinalProject](https://github.com/PunnyOz2/DS_DE_FinalProject.git)

3. Set up a virtual environment (optional but recommended)
   ```shell
   python3 -m venv .venv
   ```

   ```shell
   # activate a virtual environment on MacOS or Linux
   source .venv/bin/activate
    ```
4. Install all the necessary packages
   ```shell
   pip install redis pandas geopy streamlit plotly pydeck watchdog
   ```
5. Run the project using Streamlit 🎉
   ```shell
   streamlit run main.py
   ```
