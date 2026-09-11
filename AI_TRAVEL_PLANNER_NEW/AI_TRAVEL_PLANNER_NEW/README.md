# AI TRAVEL PLANNER

Multi-agent AI travel planner using Python, Streamlit, Ollama, Open-Meteo and OpenStreetMap/Overpass.

Agents: Destination Research, Weather, Restaurant & Activity, Itinerary & Budget. The Orchestrator coordinates them.

## Setup

```powershell
python -m pip install -r requirements.txt
ollama pull llama3
python -m streamlit run app.py
```

Open http://localhost:8501.

CLI: `python main.py`
