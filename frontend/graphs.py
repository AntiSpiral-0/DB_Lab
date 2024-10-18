import streamlit as st
import matplotlib.pyplot as plt
from utils.query_database import QueryDatabase
from pathlib import Path
# one of the tables is geografi and this is one graph// again i had problems with the path so i kept adding the specific path
class ViewsTrend:
    def __init__(self) -> None:

        db_path = Path(__file__).parent.parent / "backend" / "youtube_data.db"
        self._db = QueryDatabase(db_path)
        self._views_data = self._db.fetch_table("SELECT * FROM marts.mart_geografi;")

    def display_plot(self):
        df = self._views_data
        st.markdown("## Visningstrender")

       
        fig, ax = plt.subplots()
        ax.plot(df['date_view'], df['views'], marker='o')

        ax.set_xlabel("Date")
        ax.set_ylabel("Views")
        ax.set_title("Trend of Views Over Time")
        plt.xticks(rotation=45)
        st.pyplot(fig)  




    



