import pandas as pd
import numpy as np
import joblib
import logging
from model_trainer import MalariaModelTrainer

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MalariaPredictor:
    """Predictor for malaria outbreak risk"""
    
    def __init__(self, model_path='malaria_model.pkl'):
        self.trainer = MalariaModelTrainer()
        try:
            self.trainer.load_model(model_path)
            logger.info("Model loaded successfully!")
        except FileNotFoundError:
            logger.warning(f"Model file not found at {model_path}. Please train the model first.")
            self.trainer = None
    
    def predict_risk(self, input_data):
        """
        Predict malaria outbreak risk
        
        Args:
            input_data: dict or DataFrame with features
        
        Returns:
            dict with risk_level, probabilities, and confidence
        """
        if self.trainer is None or self.trainer.model is None:
            raise ValueError("Model not loaded. Please train the model first.")
        
        # Convert input to DataFrame if needed
        if isinstance(input_data, dict):
            input_df = pd.DataFrame([input_data])
        else:
            input_df = input_data
        
        # Ensure all required features are present
        for feature in self.trainer.feature_names:
            if feature not in input_df.columns:
                input_df[feature] = 0
        
        # Reorder columns to match training data
        input_df = input_df[self.trainer.feature_names]
        
        # Make prediction
        prediction = self.trainer.model.predict(input_df)[0]
        probability = self.trainer.model.predict_proba(input_df)
        
        risk_levels = self.trainer.risk_levels
        
        result = {
            'risk_level': prediction,
            'probabilities': {
                level: f"{prob:.3f}" for level, prob in zip(risk_levels, probability[0])
            },
            'confidence': max(probability[0])
        }
        
        return result
    
    def get_risk_recommendations(self, risk_level):
        """Get recommendations based on risk level"""
        recommendations = {
            'Low': [
                "Continue routine surveillance",
                "Maintain standard prevention measures",
                "Monitor climate changes"
            ],
            'Medium': [
                "Increase surveillance frequency",
                "Stockpile essential medications",
                "Community awareness campaigns",
                "Enhanced mosquito control measures"
            ],
            'High': [
                "Activate emergency response plan",
                "Deploy rapid response teams",
                "Mass distribution of prevention tools",
                "Coordinate with regional health authorities",
                "Prepare healthcare facilities for increased cases"
            ]
        }
        
        return recommendations.get(risk_level, ["No specific recommendations available"])

# Unit tests for predictor
def test_predictor():
    """Test the predictor functionality"""
    # First, ensure we have a trained model
    from model_trainer import main
    trainer, _ = main()
    
    predictor = MalariaPredictor()
    
    # Test prediction with sample data
    sample_input = {
        'avg_temperature': 30,
        'rainfall': 120,
        'humidity': 85,
        'population_density': 200,
        'healthcare_access': 0.3,
        'historical_cases': 75,
        'month': 6,
        'region_Region_A': 1,
        'region_Region_B': 0,
        'region_Region_C': 0
    }
    
    try:
        result = predictor.predict_risk(sample_input)
        print("✅ Prediction test passed!")
        print(f"Prediction: {result}")
        
        recommendations = predictor.get_risk_recommendations(result['risk_level'])
        print("Recommendations:", recommendations)
        
    except Exception as e:
        print(f"❌ Prediction test failed: {e}")

if __name__ == "__main__":
    test_predictor()
