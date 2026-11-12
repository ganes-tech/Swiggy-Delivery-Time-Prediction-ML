import streamlit as st
import pandas as pd
import pickle

# ---------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------

st.image("C:\\Users\\Ganesh\\Downloads\\Swiggy Delivery Time Prediction.png", use_container_width=True)



st.set_page_config(
    page_title="Swiggy Delivery Time Prediction",
    layout="wide"
)

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------

st.markdown("""
<style>

.main {
    background-color: #f8f9fa;
}

.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #666;
    margin-bottom: 30px;
}

.section-title {
    font-size: 22px;
    font-weight: bold;
    margin-top: 20px;
    margin-bottom: 15px;
}

.result-box {
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    background-color: #f0fff4;
    border: 2px solid #28a745;
    margin-top: 25px;
}

.result-title {
    font-size: 20px;
    font-weight: bold;
}

.result-time {
    font-size: 40px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------
# HEADER
# ---------------------------------------------------



st.divider()


# ---------------------------------------------------
# USER NAME
# ---------------------------------------------------



# ---------------------------------------------------
# LOAD MODEL
# ---------------------------------------------------

with open(r"C:\Project-ML\model.pkl", "rb") as file:
    model = pickle.load(file)


# ---------------------------------------------------
# FORM
# ---------------------------------------------------

with st.form("prediction_form"):

    # -----------------------------------------------
    # DELIVERY PARTNER
    # -----------------------------------------------

    st.markdown(
        '<div class="section-title">👨‍💼 Delivery Partner Details</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input(
            "Age",
            min_value=20,
            max_value=39,
            value=20
        )

    with col2:
        ratings = st.number_input(
            "Rating",
            min_value=2.5,
            max_value=5.0,
            value=2.5,
            step=0.1
        )

    with col3:
        vehicle_condition = st.selectbox(
            "Vehicle Condition",
            options=["0", "1", "2", "3"],
            index=None,
            placeholder="Select condition..."
        )


    st.divider()


    # -----------------------------------------------
    # ORDER DETAILS
    # -----------------------------------------------

    st.markdown(
        '<div class="section-title">🍔 Order Details</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        type_of_order = st.selectbox(
            "Type of Order",
            options=[
                "snack",
                "drinks",
                "buffet",
                "meal"
            ],
            index=None,
            placeholder="Select order type..."
        )

    with col2:
        multiple_deliveries = st.number_input(
            "Multiple Deliveries",
            min_value=0,
            max_value=3,
            step=1,
            value=0
        )

    with col3:
        festival = st.radio(
            "Festival",
            options=["no", "yes"],
            horizontal=True,
            index=None
        )


    st.divider()


    # -----------------------------------------------
    # WEATHER & TRAFFIC
    # -----------------------------------------------

    st.markdown(
        '<div class="section-title">🌦️ Weather & Traffic</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        weather = st.selectbox(
            "Weather",
            options=[
                "sunny",
                "stormy",
                "sandstorms",
                "cloudy",
                "fog",
                "windy"
            ],
            index=None,
            placeholder="Select weather..."
        )

    with col2:
        traffic = st.selectbox(
            "Traffic",
            options=[
                "high",
                "jam",
                "low",
                "medium"
            ],
            index=None,
            placeholder="Select traffic..."
        )

    with col3:
        distance = st.number_input(
            "Distance (km)",
            min_value=1,
            max_value=21,
            value=1
        )


    st.divider()


    # -----------------------------------------------
    # VEHICLE & LOCATION
    # -----------------------------------------------

    st.markdown(
        '<div class="section-title">🛵 Vehicle & Location</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        type_of_vehicle = st.selectbox(
            "Type of Vehicle",
            options=[
                "motorcycle",
                "scooter",
                "electric_scooter",
                "bicycle"
            ],
            index=None,
            placeholder="Select vehicle..."
        )

    with col2:
        city_type = st.selectbox(
            "City Type",
            options=[
                "urban",
                "metropolitian",
                "semi-urban"
            ],
            index=None,
            placeholder="Select city type..."
        )

   



    st.divider()


    # -----------------------------------------------
    # DATE & TIME
    # -----------------------------------------------

    st.markdown(
        '<div class="section-title">📅 Date & Time</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        order_day = st.number_input(
            "Order Day",
            min_value=1,
            max_value=31,
            value=1
        )

    with col2:
        order_month = st.number_input(
            "Order Month",
            min_value=2,
            max_value=4,
            value=2
        )

    with col3:
        order_day_of_week = st.selectbox(
            "Day of Week",
            options=[
                "saturday",
                "friday",
                "tuesday",
                "monday",
                "sunday",
                "wednesday",
                "thursday"
            ],
            index=None,
            placeholder="Select day..."
        )

    with col4:
        is_weekend = st.toggle("Weekend?")


    col1, col2, col3 = st.columns(3)

    with col1:
        pickup_time_minutes = st.number_input(
            "Pickup Time (minutes)",
            min_value=5,
            max_value=15,
            step=5,
            value=5
        )

    with col2:
        order_time_hour = st.number_input(
            "Order Hour",
            min_value=0,
            max_value=23,
            value=0
        )

    with col3:
        order_time_of_day = st.selectbox(
            "Time of Day",
            options=[
                "morning",
                "evening",
                "afternoon",
                "night",
                "after_midnight"
            ],
            index=None,
            placeholder="Select time..."
        )


    st.write("")


    # -----------------------------------------------
    # PREDICT BUTTON
    # -----------------------------------------------

    predict_clicked = st.form_submit_button(
        "🚀 Predict Delivery Time",
        use_container_width=True
    )


# ---------------------------------------------------
# PREDICTION
# ---------------------------------------------------

if predict_clicked:

    # Check dropdowns

    required_values = [
        weather,
        traffic,
        vehicle_condition,
        type_of_order,
        type_of_vehicle,
        city_type,
        order_day_of_week,
        order_time_of_day
    ]

    if any(value is None for value in required_values):

        st.warning(
            "⚠️ Please select all the required options before predicting."
        )

    else:

        # Create input dataframe

        input_data = pd.DataFrame([{

            "age": age,

            "ratings": ratings,

            "weather": weather,

            "traffic": traffic,

            "vehicle_condition": vehicle_condition,

            "type_of_order": type_of_order,

            "type_of_vehicle": type_of_vehicle,

            "multiple_deliveries": multiple_deliveries,

            "festival": festival,

            "city_type": city_type,

            "order_day": order_day,

            "order_month": order_month,

            "order_day_of_week": order_day_of_week,

            "is_weekend": is_weekend,

            "pickup_time_minutes": pickup_time_minutes,

            "order_time_hour": order_time_hour,

            "order_time_of_day": order_time_of_day,

            "distance": distance

        }])


        # Prediction

        prediction = model.predict(input_data)

        predicted_time = prediction[0]


        # Display result

        st.markdown(
            f"""
            <div class="result-box">

                
                    🎉 Estimated Delivery Time:{predicted_time:.2f} minutes
                    
                    📦 Your order is estimated to arrive in
                    approximately {predicted_time:.0f} minutes.
                

            </div>
            """,
            unsafe_allow_html=True
        )


# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.divider()

st.caption(
    "🤖 Machine Learning Project | Swiggy Delivery Time Prediction"
)