import streamlit as st
import requests

def get_ai_response(prompt, conversation_history):
    """Get response from AI model via OpenRouter"""
    try:
        api_key = "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"

        headers = {
            "Authorization": f"Bearer {api_key}",
            "HTTP-Referer": "http://localhost:8501",  # Required for OpenRouter
            "Content-Type": "application/json",
            "OpenRouter-Referrer": "http://localhost:8501"  # Added this header
        }

        data = {
            "model": "meta-llama/llama-3.1-8b-instruct",
            "messages": [
                {
                    "role": "system",
                    "content": load_solar_context()
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }

        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=data
        )

        # Print response for debugging
        print("Response Status Code:", response.status_code)
        print("Response Content:", response.text)

        if response.status_code == 200:
            response_data = response.json()
            if 'choices' in response_data and len(response_data['choices']) > 0:
                return response_data['choices'][0]['message']['content']
            else:
                return f"Error: Unexpected response format: {response_data}"
        else:
            return f"Error: API request failed with status code {response.status_code}\nResponse: {response.text}"
            
    except Exception as e:
        return f"Error getting response: {str(e)}\nFull error: {type(e).__name__}"


def load_solar_context():
    """Load the solar industry knowledge base context"""
    return """You are a solar industry expert assistant. You provide accurate, helpful information about:
    - Solar panel technology and specifications
    - Installation processes and best practices
    - Maintenance requirements and schedules
    - Cost analysis and ROI calculations
    - Industry regulations and compliance
    - Current market trends and forecasts
    
    Provide clear, concise answers suitable for both technical and non-technical users."""

def calculate_solar_roi(system_cost, annual_energy_savings, incentives=0):
    """Calculate Return on Investment for solar installation"""
    total_cost = system_cost - incentives
    if annual_energy_savings <= 0:
        return float('inf')
    return total_cost / annual_energy_savings

def main():
    st.set_page_config(page_title="Solar Industry Assistant", page_icon="☀️")
    
    # Initialize session state for conversation history
    if 'conversation_history' not in st.session_state:
        st.session_state.conversation_history = []
    
    st.title("☀️ Solar Industry Assistant")
    
    # Sidebar with tools
    st.sidebar.header("Tools")
    tool_choice = st.sidebar.selectbox(
        "Select Tool",
        ["Chat Assistant", "ROI Calculator", "Documentation"]
    )
    
    if tool_choice == "Chat Assistant":
        st.header("Solar Expert Chat")
        
        # Display conversation history
        for message in st.session_state.conversation_history:
            role = message["role"]
            content = message["content"]
            with st.chat_message(role):
                st.write(content)
        
        # Chat input
        if prompt := st.chat_input("Ask about solar energy..."):
            # Display user message
            with st.chat_message("user"):
                st.write(prompt)
            
            # Get and display assistant response
            with st.chat_message("assistant"):
                response = get_ai_response(prompt, str(st.session_state.conversation_history))
                st.write(response)
            
            # Update conversation history
            st.session_state.conversation_history.extend([
                {"role": "user", "content": prompt},
                {"role": "assistant", "content": response}
            ])
    
    elif tool_choice == "ROI Calculator":
        st.header("Solar ROI Calculator")
        
        system_cost = st.number_input("Total System Cost ($)", min_value=0.0, value=20000.0)
        annual_savings = st.number_input("Estimated Annual Energy Savings ($)", min_value=0.0, value=1500.0)
        incentives = st.number_input("Available Incentives/Rebates ($)", min_value=0.0, value=5000.0)
        
        if st.button("Calculate ROI"):
            roi_years = calculate_solar_roi(system_cost, annual_savings, incentives)
            st.success(f"Estimated ROI Period: {roi_years:.1f} years")
            
            # Display detailed breakdown
            st.subheader("Investment Breakdown")
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Total Investment", f"${system_cost:,.2f}")
                st.metric("Incentives", f"${incentives:,.2f}")
            with col2:
                st.metric("Net Cost", f"${(system_cost - incentives):,.2f}")
                st.metric("Annual Savings", f"${annual_savings:,.2f}")
    
    else:  # Documentation
        st.header("Documentation & Resources")
        
        st.subheader("Quick Links")
        st.markdown("""
        - [Solar Panel Basics](https://www.energy.gov/eere/solar/how-does-solar-work)
        - [Installation Guide](https://www.energy.gov/eere/solar/homeowners-guide-going-solar)
        - [Federal Tax Credits](https://www.energy.gov/eere/solar/federal-solar-tax-credits)
        """)
        
        st.subheader("Maintenance Schedule")
        st.markdown("""
        1. **Monthly**
            - Check system performance
            - Clean debris from panels
        2. **Quarterly**
            - Detailed performance analysis
            - Check for damage or wear
        3. **Annually**
            - Professional inspection
            - Deep cleaning
            - Inverter check
        """)

if __name__ == "__main__":
    main()
