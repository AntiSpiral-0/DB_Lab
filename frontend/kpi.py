import streamlit as st
from utils.query_database import QueryDatabase

class DeviceKPI:
    def __init__(self) -> None:
        
        self._db = QueryDatabase('10_lab_overview/backend/youtube_data.db')
        self._device_data = self._db.fetch_table("SELECT * FROM marts.mart_device;")
        

    def display_device_kpis(self):
        df = self._device_data
        st.markdown("- KPIer för enheter")
        st.dataframe(df)#display

class ContentKPI:
    def __init__(self) -> None:
        
        self._db = QueryDatabase('10_lab_overview/backend/youtube_data.db')
        self._content_data = self._db.fetch_table("SELECT * FROM marts.kpi_dashboard ;")
        

    def display_Content_kpis(self):
        df = self._content_data
        st.markdown("- KPIer för innehall")
        st.dataframe(df)#display

class osKPI:
    def __init__(self) -> None:
        
        self._db = QueryDatabase('10_lab_overview/backend/youtube_data.db')
        self._os_data = self._db.fetch_table("SELECT * FROM marts.kpi_operating_systems ;")
        

    def display_os_kpis(self):
        df = self._os_data
        st.markdown("- KPIer för Os")
        st.dataframe(df)#display
class geographyKPI:
    def __init__(self) -> None:
        
        self._db = QueryDatabase('10_lab_overview/backend/youtube_data.db')
        self._geografi_data = self._db.fetch_table("SELECT * FROM marts.kpi_geografi ;")
        

    def display_Content_kpis(self):
        df = self._geografi_data
        st.markdown("- KPIer för geografi")
        st.dataframe(df)#display