# 🇨🇳 China Weather App

A simple and interactive web application built with Streamlit that displays current weather conditions for major cities in China.

## 🌟 Features

- **Real-time Weather Data**: Fetches up-to-date weather information using the [Open-Meteo API](https://open-meteo.com/).
- **Major Cities Coverage**: Includes pre-configured coordinates for 10+ major Chinese cities including Beijing, Shanghai, Guangzhou, Shenzhen, and more.
- **Interactive UI**: User-friendly interface to select cities and view data instantly.
- **Key Metrics**: Displays Temperature, Wind Speed, and Wind Direction.

## 🛠️ Tech Stack

- **Python**: Core programming language.
- **Streamlit**: For building the interactive web interface.
- **Requests**: For handling HTTP requests to the weather API.
- **Open-Meteo API**: Free weather API for forecast data (no API key required).

## 🚀 Getting Started

### Prerequisites

- Python 3.12 or higher
- [uv](https://github.com/astral-sh/uv) (recommended for dependency management)

### Installation

1. **Clone the repository** (if applicable) or navigate to the project directory.

2. **Install dependencies**:
   
   Using `uv`:
   ```bash
   uv sync
   ```
   
   Or manually with `pip`:
   ```bash
   pip install streamlit requests
   ```

### Running the App

To start the application, run the following command:

```bash
uv run streamlit run app.py
```

Or if you are using standard pip:

```bash
streamlit run app.py
```

The app will open in your default web browser at `http://localhost:8501`.

## 📂 Project Structure

- `app.py`: Main application file containing the Streamlit logic.
- `pyproject.toml`: Project configuration and dependencies (managed by `uv`).
- `README.md`: Project documentation.

## 📝 License

This project is open-source and available for personal and educational use.
