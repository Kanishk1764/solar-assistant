# Solar Industry AI Assistant
A Streamlit-based intelligent assistant for solar industry consulting, providing real-time information and ROI calculations for solar installations.

## Project Overview
This project implements an AI-powered assistant specializing in solar industry consulting. It combines LLM capabilities with practical tools like ROI calculation to assist both technical and non-technical users in understanding solar technology, installation processes, and financial implications.

## Features
- Interactive chat interface with solar industry expertise
- Solar ROI calculator with detailed breakdown
- Documentation hub with maintenance schedules
- Real-time API integration with OpenRouter
- Conversation history tracking
- User-friendly interface with dark/light mode support

## Technical Stack
- **Frontend**: Streamlit
- **AI Integration**: OpenRouter API
- **Model**: Meta Llama 3.1 8B Instruct
- **Language**: Python 3.8+

## Local Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager
- OpenRouter API key

### Installation Steps
1. Clone the repository:
```bash
https://github.com/Kanishk1764/solar-assistant.git
cd solar-assistant
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install streamlit requests
```

4. Create a `.env` file in the project root:
```
OPENROUTER_API_KEY=your_api_key_here
```

5. Run the application:
```bash
streamlit run app.py
```

## Project Structure
```
solar-assistant/
├── app.py              # Main application file
├── requirements.txt    # Project dependencies
├── .env               # Environment variables
└── README.md          # Project documentation
```

## Core Components

### AI Chat Assistant
The chat assistant integrates with OpenRouter API to provide expert responses about solar technology. Key features:
- Context-aware responses using solar industry knowledge base
- Conversation history tracking
- Error handling and response validation
- User-friendly chat interface

### ROI Calculator
Interactive calculator for estimating solar installation returns:
- System cost input
- Annual energy savings estimation
- Incentives/rebates consideration
- Detailed financial breakdown
- Visual metrics display

### Documentation Hub
Centralized resource center including:
- Quick reference links
- Maintenance schedules
- Best practices
- Industry regulations

## API Integration

### OpenRouter Configuration
```python
headers = {
    "Authorization": f"Bearer {api_key}",
    "HTTP-Referer": "http://localhost:8501",
    "Content-Type": "application/json",
    "OpenRouter-Referrer": "http://localhost:8501"
}
```

### System Context
The assistant uses a predefined context that covers:
- Solar panel technology
- Installation processes
- Maintenance requirements
- Cost analysis
- Industry regulations
- Market trends

## Known Limitations
- ROI calculator assumes linear energy savings
- Chat responses limited by model context window
- Local deployment required for development
- Rate limits based on OpenRouter API tier

## Future Improvements
1. Enhanced Data Persistence
   - Database integration for conversation history
   - User preference saving
   - Session management

2. Advanced Analytics
   - Historical performance tracking
   - Energy production forecasting
   - Weather data integration

3. UI/UX Enhancements
   - Mobile responsiveness optimization
   - Custom theming options
   - Interactive visualizations

4. Feature Additions
   - PDF report generation
   - Multiple language support
   - Integration with solar monitoring APIs

## Troubleshooting

### Common Issues
1. API Connection Errors
   - Verify API key in .env file
   - Check internet connection
   - Confirm OpenRouter service status

2. Streamlit Interface Issues
   - Clear browser cache
   - Restart Streamlit server
   - Check console for error messages

3. ROI Calculator Errors
   - Ensure positive input values
   - Verify calculation logic
   - Check for floating-point precision issues

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License
MIT License - feel free to use this project as you see fit.

## Contact
For support or questions, please open an issue in the repository.
