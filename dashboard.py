import streamlit as st
from frontend.kpi import ContentKPI, DeviceKPI, osKPI,geographyKPI
from frontend.graphs import ViewsTrend

content_kpi = ContentKPI()
device_kpi = DeviceKPI()
geografi_kpi = geographyKPI()  # Make sure this line comes after the class definition
views_graph = ViewsTrend()
os_kpi = osKPI()



def layout():
    st.markdown("# Data-Driven YouTuber Dashboard")
    st.markdown("Den här dashboarden syftar till att utforska datan i min YouTube-kanal")
    content_kpi.display_Content_kpis() # my own content kpi here
    device_kpi.display_device_kpis()
    views_graph.display_plot()
    geografi_kpi.display_geografi_kpis()
    os_kpi.display_os_kpis()

if __name__ == "__main__":
    layout()
