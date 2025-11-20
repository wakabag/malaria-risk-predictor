import unittest
import pandas as pd
import numpy as np
from data_loader import MalariaDataLoader
from model_trainer import MalariaModelTrainer
from predict import MalariaPredictor

class TestMalariaPredictionSystem(unittest.TestCase):
    """Comprehensive tests for the malaria prediction system"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.data_loader = MalariaDataLoader()
        self.model_trainer = MalariaModelTrainer()
        
    def test_data_generation(self):
        """Test data generation functionality"""
        data = self.data_loader.generate_sample_data(100)
        self.assertEqual(len(data), 100)
        self.assertIn('outbreak_risk', data.columns)
        self.assertTrue(all(data['outbreak_risk'].isin(['Low', 'Medium', 'High'])))
    
    def test_data_preprocessing(self):
        """Test data preprocessing"""
        self.data_loader.generate_sample_data(100)
        features, target = self.data_loader.preprocess_data()
        
        self.assertIsInstance(features, pd.DataFrame)
        self.assertIsInstance(target, pd.Series)
        self.assertEqual(len(features), len(target))
    
    def test_model_training(self):
        """Test model training pipeline"""
        # Generate data
        self.data_loader.generate_sample_data(200)
        features, target = self.data_loader.preprocess_data()
        X_train, X_test, y_train, y_test = self.data_loader.train_test_split()
        
        # Train model
        model = self.model_trainer.train_model(X_train, y_train)
        
        self.assertIsNotNone(model)
        self.assertIsNotNone(self.model_trainer.feature_names)
    
    def test_prediction(self):
        """Test prediction functionality"""
        # Train a small model first
        self.data_loader.generate_sample_data(200)
        features, target = self.data_loader.preprocess_data()
        X_train, X_test, y_train, y_test = self.data_loader.train_test_split()
        self.model_trainer.train_model(X_train, y_train)
        
        # Create predictor and test
        predictor = MalariaPredictor()
        predictor.trainer = self.model_trainer
        
        # Create test input
        test_input = X_test.iloc[0:1].copy()
        
        result = predictor.predict_risk(test_input)
        
        self.assertIn('risk_level', result)
        self.assertIn('probabilities', result)
        self.assertIn('confidence', result)
        self.assertIn(result['risk_level'], ['Low', 'Medium', 'High'])

def run_bias_audit():
    """Audit model for potential biases"""
    print("🔍 Running Bias Audit...")
    
    loader = MalariaDataLoader()
    data = loader.generate_sample_data(1000)
    
    # Check distribution across regions
    region_risk = pd.crosstab(data['region'], data['outbreak_risk'], normalize='index')
    print("\nRisk Distribution by Region:")
    print(region_risk)
    
    # Check for fairness in predictions
    features, target = loader.preprocess_data()
    X_train, X_test, y_train, y_test = loader.train_test_split()
    
    trainer = MalariaModelTrainer()
    trainer.train_model(X_train, y_train)
    
    # Predict on test set
    y_pred = trainer.model.predict(X_test)
    
    # Convert to DataFrame for analysis
    results_df = X_test.copy()
    results_df['actual'] = y_test.values
    results_df['predicted'] = y_pred
    
    print("\nAccuracy by Region Type:")
    for region_col in [col for col in X_test.columns if col.startswith('region_')]:
        region_mask = X_test[region_col] == 1
        if region_mask.any():
            region_accuracy = (y_pred[region_mask] == y_test[region_mask]).mean()
            print(f"{region_col}: {region_accuracy:.3f}")

if __name__ == '__main__':
    # Run unit tests
    print("Running Unit Tests...")
    unittest.main(argv=[''], exit=False, verbosity=2)
    
    # Run bias audit
    print("\n" + "="*50)
    run_bias_audit()
