import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from predict import MalariaPredictor
from data_loader import MalariaDataLoader
import warnings
warnings.filterwarnings('ignore')

# Page configuration
st.set_page_config(
    page_title="Malaria Outbreak Risk Predictor",
    page_icon="🦟",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .risk-low { color: green; font-weight: bold; }
    .risk-medium { color: orange; font-weight: bold; }
    .risk-high { color: red; font-weight: bold; }
    .recommendation-box {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

class MalariaPredictionApp:
    def __init__(self):
        self.predictor = MalariaPredictor()
        self.regions = ['Region_A', 'Region_B', 'Region_C']
    
    def render_sidebar(self):
        """Render the sidebar with input controls"""
        st.sidebar.title("🦟 Input Parameters")
        st.sidebar.markdown("Adjust the parameters to predict malaria outbreak risk")
        
        # Climate parameters
        st.sidebar.subheader("Climate Data")
        temperature = st.sidebar.slider(
            "Average Temperature (°C)", 
            min_value=15, max_value=40, value=28
        )
        rainfall = st.sidebar.slider(
            "Monthly Rainfall (mm)", 
            min_value=0, max_value=300, value=120
        )
        humidity = st.sidebar.slider(
            "Humidity (%)", 
            min_value=30, max_value=100, value=75
        )
        
        # Regional parameters
        st.sidebar.subheader("Regional Data")
        population_density = st.sidebar.slider(
            "Population Density (people/km²)", 
            min_value=10, max_value=1000, value=200
        )
        healthcare_access = st.sidebar.slider(
            "Healthcare Access Index", 
            min_value=0.0, max_value=1.0, value=0.5
        )
        historical_cases = st.sidebar.slider(
            "Historical Cases (previous season)", 
            min_value=0, max_value=200, value=50
        )
        
        # Categorical parameters
        region = st.sidebar.selectbox("Region", self.regions)
        month = st.sidebar.selectbox("Month", range(1, 13), format_func=lambda x: f"Month {x}")
        
        return {
            'avg_temperature': temperature,
            'rainfall': rainfall,
            'humidity': humidity,
            'population_density': population_density,
            'healthcare_access': healthcare_access,
            'historical_cases': historical_cases,
            'month': month,
            'region': region
        }
    
    def prepare_input_data(self, user_input):
        """Prepare user input for model prediction"""
        input_data = user_input.copy()
        region = input_data.pop('region')
        
        # Convert to feature format
        features = {
            'avg_temperature': input_data['avg_temperature'],
            'rainfall': input_data['rainfall'],
            'humidity': input_data['humidity'],
            'population_density': input_data['population_density'],
            'healthcare_access': input_data['healthcare_access'],
            'historical_cases': input_data['historical_cases'],
            'month': input_data['month'],
        }
        
        # Add region one-hot encoding
        for r in self.regions:
            features[f'region_{r}'] = 1 if r == region else 0
            
        return features
    
    def render_risk_display(self, prediction_result):
        """Display risk prediction results"""
        risk_level = prediction_result['risk_level']
        probabilities = prediction_result['probabilities']
        confidence = prediction_result['confidence']
        
        # Risk level display
        st.subheader("🎯 Prediction Result")
        
        risk_colors = {
            'Low': 'green',
            'Medium': 'orange', 
            'High': 'red'
        }
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(
                "Outbreak Risk", 
                risk_level,
                delta=f"Confidence: {confidence:.1%}"
            )
        
        with col2:
            risk_color = risk_colors.get(risk_level, 'gray')
            st.markdown(f"<h3 style='color: {risk_color};'>Risk Level: {risk_level}</h3>", 
                       unsafe_allow_html=True)
        
        with col3:
            st.metric(
                "Highest Probability",
                f"{max([float(p) for p in probabilities.values()]):.1%}"
            )
        
        # Probability visualization
        st.subheader("📊 Risk Probability Distribution")
        
        fig = go.Figure(data=[
            go.Bar(x=list(probabilities.keys()), 
                  y=[float(p) for p in probabilities.values()],
                  marker_color=['green', 'orange', 'red'])
        ])
        
        fig.update_layout(
            title="Probability of Each Risk Level",
            xaxis_title="Risk Level",
            yaxis_title="Probability",
            yaxis_tickformat=".0%"
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    def render_recommendations(self, risk_level):
        """Display recommendations based on risk level"""
        st.subheader("💡 Recommended Actions")
        
        recommendations = self.predictor.get_risk_recommendations(risk_level)
        
        for i, recommendation in enumerate(recommendations, 1):
            st.markdown(f"""
            <div class="recommendation-box">
                {i}. {recommendation}
            </div>
            """, unsafe_allow_html=True)
    
    def render_data_insights(self):
        """Show sample data insights"""
        st.sidebar.markdown("---")
        if st.sidebar.button("Generate Sample Insights"):
            with st.spinner("Generating insights..."):
                loader = MalariaDataLoader()
                data = loader.generate_sample_data(500)
                
                st.subheader("📈 Sample Data Insights")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    # Risk distribution
                    fig1 = px.pie(data, names='outbreak_risk', 
                                 title='Outbreak Risk Distribution in Sample Data')
                    st.plotly_chart(fig1, use_container_width=True)
                
                with col2:
                    # Temperature vs Risk
                    fig2 = px.box(data, x='outbreak_risk', y='avg_temperature',
                                 title='Temperature Distribution by Risk Level')
                    st.plotly_chart(fig2, use_container_width=True)
    
    def run(self):
        """Main application runner"""
        # Header
        st.markdown('<div class="main-header">🦟 AI-Powered Malaria Outbreak Risk Predictor</div>', 
                   unsafe_allow_html=True)
        st.markdown("*SDG 3: Good Health and Well-being | Using ML for Preventive Healthcare*")
        
        try:
            # User input
            user_input = self.render_sidebar()
            
            # Prepare and make prediction
            input_features = self.prepare_input_data(user_input)
            
            if st.sidebar.button("Predict Outbreak Risk", type="primary"):
                with st.spinner("Analyzing risk factors..."):
                    prediction_result = self.predictor.predict_risk(input_features)
                    
                    # Display results
                    self.render_risk_display(prediction_result)
                    self.render_recommendations(prediction_result['risk_level'])
            
            # Data insights
            self.render_data_insights()
            
            # Ethical considerations
            with st.expander("🔍 Ethical Considerations & Limitations"):
                st.markdown("""
                - **Data Bias**: Model performance may vary across different regions based on data availability
                - **Transparency**: This is a demonstration model using synthetic data
                - **Human Oversight**: Predictions should always be verified by healthcare professionals
                - **Privacy**: Real implementation would require careful handling of health data
                - **Continuous Monitoring**: Models need regular updates and monitoring for drift
                """)
            
        except Exception as e:
            error_message = str(e)
            st.error(f"Application error: {error_message}")
            
            if "Model not loaded" in error_message:
                st.info("💡 The model file was not found. Attempting to train the model now...")
                try:
                    from model_trainer import main as train_model
                    train_model()
                    st.success("✅ Model trained successfully! Please refresh the page to use the app.")
                except Exception as train_e:
                    st.error(f"❌ Model training failed: {str(train_e)}")
                    st.info("Please ensure all project files are uploaded to GitHub.")

# Run the application
if __name__ == "__main__":
    app = MalariaPredictionApp()
    app.run()
