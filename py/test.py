"""
MOOD FOOD TRACKER - Sample flow for learning Streamlit + MongoDB
------------------------------------------------------------------
This is ONE file so you can see the whole flow top-to-bottom.
Later, split into app.py / pages/ / db.py as discussed.

Run with:  streamlit run mood_tracker_demo.py
"""

import streamlit as st
import pymongo
import pandas as pd
from datetime import datetime

# ------------------------------------------------------------------
# 1. CONNECT TO MONGODB
# ------------------------------------------------------------------
# @st.cache_resource means: "only create this connection ONCE,
# even though Streamlit re-runs the whole script on every click."
# Without this, you'd reconnect to MongoDB every single interaction.
@st.cache_resource
def get_collection():
    client = pymongo.MongoClient("YOUR_CONNECTION_STRING_HERE")
    db = client["mood_tracker"]        # database name
    return db["entries"]               # collection (like a table)

entries = get_collection()

# ------------------------------------------------------------------
# 2. PAGE SETUP
# ------------------------------------------------------------------
st.set_page_config(page_title="Mood Food Tracker", layout="centered")
st.title("🍽️ Mood Food Tracker")
st.caption("Log what you eat and how you feel — spot your patterns over time.")

# Streamlit apps are often split into "tabs" so one file can hold
# multiple "pages" of functionality for this demo.
tab_add, tab_view, tab_analysis = st.tabs(["➕ Add Entry", "📋 View / Delete", "📊 Analysis"])

# ------------------------------------------------------------------
# 3. CREATE (Add a new entry)
# ------------------------------------------------------------------
with tab_add:
    st.subheader("Log a new entry")

    # st.form groups inputs together so nothing runs until "Submit" is clicked.
    # Without a form, Streamlit would re-run on every keystroke.
    with st.form("add_entry_form"):
        food = st.text_input("What did you eat?")
        mood = st.selectbox("How were you feeling?",
                             ["Happy", "Sad", "Stressed", "Tired", "Neutral"])
        intensity = st.slider("How strong was that feeling?", 1, 5, 3)
        meal_type = st.radio("Meal type", ["Breakfast", "Lunch", "Dinner", "Snack"])
        submitted = st.form_submit_button("Save Entry")

        if submitted:
            if food.strip() == "":
                st.error("Please enter what you ate.")
            else:
                # INSERT into MongoDB
                entries.insert_one({
                    "food": food,
                    "mood": mood,
                    "mood_intensity": intensity,
                    "meal_type": meal_type,
                    "timestamp": datetime.now()
                })
                st.success(f"Saved: {food} while feeling {mood} ✅")

# ------------------------------------------------------------------
# 4. READ + DELETE (View past entries)
# ------------------------------------------------------------------
with tab_view:
    st.subheader("Your logged entries")

    # READ from MongoDB — find() returns everything in the collection
    all_entries = list(entries.find().sort("timestamp", -1))  # newest first

    if not all_entries:
        st.info("No entries yet. Add one in the first tab!")
    else:
        for entry in all_entries:
            col1, col2 = st.columns([4, 1])
            with col1:
                st.write(
                    f"**{entry['food']}** — felt *{entry['mood']}* "
                    f"({entry['mood_intensity']}/5) at {entry['meal_type']}, "
                    f"{entry['timestamp'].strftime('%b %d, %I:%M %p')}"
                )
            with col2:
                # DELETE — each row gets its own button, keyed by its unique _id
                if st.button("Delete", key=str(entry["_id"])):
                    entries.delete_one({"_id": entry["_id"]})
                    st.rerun()  # refresh the page so the deleted row disappears

# ------------------------------------------------------------------
# 5. ANALYSIS (turn raw data into insight)
# ------------------------------------------------------------------
with tab_analysis:
    st.subheader("Patterns in your data")

    all_entries = list(entries.find())

    if not all_entries:
        st.info("Log a few entries first, then come back here.")
    else:
        # Convert MongoDB documents into a pandas DataFrame — this makes
        # grouping and charting much easier than looping manually.
        df = pd.DataFrame(all_entries)

        # --- Chart 1: How often each mood appears ---
        st.write("**Mood frequency**")
        mood_counts = df["mood"].value_counts()
        st.bar_chart(mood_counts)

        # --- Chart 2: Most common food per mood ---
        st.write("**Most logged food per mood**")
        top_food_per_mood = df.groupby("mood")["food"].agg(
            lambda x: x.value_counts().idxmax()
        )
        st.dataframe(top_food_per_mood.rename("Most common food"))

        # --- Chart 3: Mood intensity trend over time ---
        st.write("**Mood intensity over time**")
        df_sorted = df.sort_values("timestamp")
        st.line_chart(df_sorted.set_index("timestamp")["mood_intensity"])

        # --- Chart 4: Average intensity by meal type ---
        st.write("**Average mood intensity by meal type**")
        avg_by_meal = df.groupby("meal_type")["mood_intensity"].mean()
        st.bar_chart(avg_by_meal)