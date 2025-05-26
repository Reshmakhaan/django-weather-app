from fpdf import FPDF

# Define the presentation content
slides = [
    {
        "title": "Weather Forecasting Web App",
        "content": "A Django-based real-time weather forecasting app that fetches and displays current and forecasted weather data for any city worldwide using the OpenWeatherMap API."
    },
    {
        "title": "Project Overview",
        "content": "- Users enter a city name.\n- The app fetches weather data via API.\n- Weather details like temperature, humidity, wind speed, and forecast are displayed.\n- Real-time and global coverage."
    },
    {
        "title": "Technologies Used",
        "content": "Frontend:\n- HTML, CSS, Bootstrap, JavaScript\n\nBackend:\n- Python 3.8.1\n- Django 3.1.13\n- Requests library\n- SQLite3 (local development database)"
    },
    {
        "title": "Why Django?",
        "content": "- Rapid development with batteries-included approach\n- Built-in ORM and templating engine\n- Secure and scalable\n- Clean MVC-style (MTV) architecture"
    },
    {
        "title": "App Structure",
        "content": "- manage.py: Entry point\n- settings.py: Configuration\n- views.py: Core logic & API integration\n- urls.py: Routing\n- templates/: UI rendering\n- static/: CSS, JS, images"
    },
    {
        "title": "How It Works",
        "content": "1. User inputs city name.\n2. API call to OpenWeatherMap.\n3. JSON data parsed in views.py.\n4. Data rendered in results.html.\n5. User sees formatted weather data."
    },
    {
        "title": "API Used: OpenWeatherMap",
        "content": "- Endpoint: /data/2.5/forecast\n- Data: 5-day forecast, weather status, wind, clouds, etc.\n- Location: Global\n- Method: requests.get(url).json()"
    },
    {
        "title": "Accuracy",
        "content": "- Highly accurate for current and short-term forecasts.\n- Accuracy depends on OpenWeatherMap’s real-time data.\n- App reliability: High\n- Prediction type: Short-term forecast, not long-range"
    },
    {
        "title": "Conclusion",
        "content": "- Fully functional global weather app\n- Built using clean Django architecture\n- Easily extendable (add charts, history, multiple APIs)\n- Deployed locally, ready for hosting on platforms like Heroku"
    }
]

# Create the PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)

for slide in slides:
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.multi_cell(0, 10, slide["title"], align='C')
    pdf.ln(5)
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 10, slide["content"])

# Save the PDF
presentation_path = "/mnt/data/Weather_Forecasting_App_Presentation.pdf"
pdf.output(presentation_path)

presentation_path
