import sqlite3
import gradio as gr
import pandas as pd

def fetch_points():

    conn = sqlite3.connect('my_database.db')

    cursor = conn.cursor()
                                    # IF NOT EXISTS --> precaution if we rerun
    query = """
        SELECT *
        FROM points;
    """

    cursor.execute(query)
    result = cursor.fetchall()   # might not want to look at all data in query

    conn.close()

    df = pd.DataFrame(result, columns = ["id", "x", "y"])

    return df

iface = gr.Interface(
fn = fetch_points,
inputs = [],
outputs = gr.LinePlot(x = 'x', y = 'y', x_lim = (0,15), y_lim = (0,15))

)

iface.launch()