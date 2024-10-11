import streamlit as st
from frontend.kpi import ContentKPI, DeviceKPI
from frontend.graphs import ViewsTrend

content_kpi = ContentKPI()
device_kpi = DeviceKPI()
views_graph = ViewsTrend()

def layout():
    st.markdown("# Data-Driven YouTuber Dashboard")
    st.markdown("Den här dashboarden syftar till att utforska datan i min YouTube-kanal")
    content_kpi.display_Content_kpis() # my own content kpi here
    device_kpi.display_device_kpis()
    views_graph.display_plot()

if __name__ == "__main__":
    layout()
