import streamlit as st
import matplotlib.pyplot as plt
from utils.query_database import QueryDatabase
# one of the tables is geografi and this is one graph// again i had problems with the path so i kept adding the specific path
class ViewsTrend:
    def __init__(self) -> None:

        self._db = QueryDatabase('10_lab_overview/backend/youtube_data.db')
        self._views_data = self._db.fetch_table("SELECT * FROM marts.mart_geografi;")

    def display_plot(self):
        df = self._views_data
        st.markdown("## Visningstrender")

       
        fig, ax = plt.subplots()
        ax.plot(df['date_view'], df['views'], marker='o')

        ax.set_xlabel("Date")
        ax.set_ylabel("Views")
        ax.set_title("Trend of Views Over Time")

        st.pyplot(fig)  




    



