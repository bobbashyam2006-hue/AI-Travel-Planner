import json
import streamlit as st
from agents.orchestrator_agent import run_orchestrator

st.set_page_config(page_title='AI Travel Planner', page_icon='🌍', layout='wide')
st.title('🌍 AI Travel Planning Agent')
st.caption('Personalized multi-agent travel planning using Ollama and free APIs.')

with st.sidebar:
    st.header('✈️ Trip Details')
    destination = st.text_input('Destination', 'Goa')
    number_of_days = st.number_input('Number of Days', 1, 30, 4)
    number_of_travelers = st.number_input('Number of Travelers', 1, 50, 2)
    budget = st.number_input('Total Budget (₹)', 1000.0, 10000000.0, 50000.0, 1000.0)
    travel_date = st.date_input('Travel Start Date')
    preferences = st.text_area('Travel Preferences', 'Beaches, food, sightseeing and adventure')
    generate = st.button('🚀 Generate Travel Plan', use_container_width=True)

if generate:
    if not destination.strip():
        st.error('Please enter a destination.')
        st.stop()
    try:
        with st.spinner('🤖 Running the AI travel agents...'):
            result = run_orchestrator(destination.strip(), int(number_of_days), float(budget), int(number_of_travelers), preferences.strip() or 'General sightseeing', str(travel_date))
    except Exception as e:
        st.error('Unable to generate the travel plan.')
        st.exception(e)
        st.info('Make sure Ollama is running and llama3 is installed.')
        st.stop()

    st.success('✅ Travel plan generated!')
    st.header('📋 Trip Summary')
    c1, c2, c3, c4 = st.columns(4)
    c1.metric('Destination', destination)
    c2.metric('Days', number_of_days)
    c3.metric('Travelers', number_of_travelers)
    c4.metric('Budget', f'₹{budget:,.0f}')
    st.write(f'**Start Date:** {travel_date}')
    st.write(f'**Preferences:** {preferences}')

    st.header('🏛️ Destination Research')
    research = result['destination_research']
    st.write(research.get('summary', ''))
    for item in research.get('attractions', []): st.write(f'📍 {item}')

    st.header('🌦️ Weather')
    weather = result['weather']
    st.write(weather.get('summary', 'Weather unavailable.'))
    for day in weather.get('daily', []): st.write(f"**{day.get('date', '')}** — {day.get('description', '')}")

    st.header('🍴 Restaurants')
    restaurants = result['places'].get('restaurants', [])
    if restaurants:
        for item in restaurants: st.write(f'🍽️ {item}')
    else: st.info('No restaurant data was found from OpenStreetMap.')

    st.header('🎯 Activities')
    activities = result['places'].get('activities', [])
    if activities:
        for item in activities: st.write(f'🎯 {item}')
    else: st.info('No activity data was found from OpenStreetMap.')

    st.header('🗓️ Day-wise Itinerary')
    final_plan = result['final_plan']
    for day in final_plan.get('itinerary', []):
        with st.container(border=True):
            st.subheader(f"Day {day.get('day', '?')}")
            st.write(f"🌅 **Morning:** {day.get('morning', '')}")
            st.write(f"☀️ **Afternoon:** {day.get('afternoon', '')}")
            st.write(f"🌙 **Evening:** {day.get('evening', '')}")

    st.header('💰 Estimated Budget')
    total = float(final_plan.get('total_estimated_cost', 0))
    remaining = float(final_plan.get('budget_remaining', budget - total))
    c1, c2 = st.columns(2)
    c1.metric('Estimated Cost', f'₹{total:,.0f}')
    c2.metric('Remaining', f'₹{remaining:,.0f}')
    st.write(f"**Status:** {final_plan.get('budget_status', '')}")
    for category, amount in final_plan.get('budget_breakdown', {}).items(): st.write(f"**{category.title()}:** ₹{float(amount):,.0f}")

    st.header('💡 Travel Tips')
    for tip in final_plan.get('travel_tips', []): st.write(f'• {tip}')

    st.download_button('⬇️ Download Travel Plan JSON', data=json.dumps(result, indent=4, ensure_ascii=False), file_name='travel_plan.json', mime='application/json')
