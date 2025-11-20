import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MalariaDataLoader:
    """Data loader for malaria outbreak prediction"""
    
    def __init__(self):
        self.data = None
        self.features = None
        self.target = None
        
    def generate_sample_data(self, n_samples=1000):
        """
        Generate synthetic malaria outbreak data for demonstration.
        In a real project, this would load from WHO/NASA APIs.
        """
        logger.info("Generating sample malaria outbreak data...")
        
        np.random.seed(42)
        
        # Simulate climate and health data
        data = {
            'region': np.random.choice(['Region_A', 'Region_B', 'Region_C'], n_samples),
            'avg_temperature': np.random.normal(28, 5, n_samples),  # Celsius
            'rainfall': np.random.gamma(2, 50, n_samples),  # mm/month
            'humidity': np.random.normal(75, 15, n_samples),  # Percentage
            'population_density': np.random.lognormal(5, 1, n_samples),  # People per sq km
            'healthcare_access': np.random.uniform(0, 1, n_samples),  # Index 0-1
            'historical_cases': np.random.poisson(50, n_samples),  # Previous cases
            'month': np.random.randint(1, 13, n_samples)  # Month of year
        }
        
        # Create risk level based on features (with some noise)
        risk_score = (
            data['avg_temperature'] * 0.3 +
            data['rainfall'] * 0.2 +
            data['humidity'] * 0.25 +
            data['historical_cases'] * 0.15 +
            (1 - data['healthcare_access']) * 0.1 +
            np.random.normal(0, 2, n_samples)
        )
        
        # Convert to risk categories with better distribution
        # Use percentiles to ensure balanced classes
        low_threshold = np.percentile(risk_score, 33)
        high_threshold = np.percentile(risk_score, 67)
        
        data['outbreak_risk'] = pd.cut(risk_score, 
                                     bins=[-np.inf, low_threshold, high_threshold, np.inf], 
                                     labels=['Low', 'Medium', 'High'])
        
        self.data = pd.DataFrame(data)
        logger.info(f"Generated {n_samples} samples")
        logger.info(f"Risk distribution:\n{self.data['outbreak_risk'].value_counts()}")
        
        return self.data
    
    def preprocess_data(self):
        """Preprocess data for model training"""
        if self.data is None:
            raise ValueError("No data loaded. Call generate_sample_data() first.")
        
        logger.info("Preprocessing data...")
        
        # Handle missing values
        self.data = self.data.dropna()
        
        # Separate features and target
        self.target = self.data['outbreak_risk']
        
        # One-hot encode categorical features
        self.features = pd.get_dummies(self.data.drop('outbreak_risk', axis=1), 
                                       columns=['region'], 
                                       drop_first=False)
        
        logger.info(f"Features shape: {self.features.shape}")
        logger.info(f"Feature columns: {list(self.features.columns)}")
        
        return self.features, self.target
    
    def train_test_split(self, test_size=0.2, random_state=42):
        """Split data into training and testing sets"""
        if self.features is None or self.target is None:
            raise ValueError("Data not preprocessed. Call preprocess_data() first.")
        
        X_train, X_test, y_train, y_test = train_test_split(
            self.features, self.target, 
            test_size=test_size, 
            random_state=random_state,
            stratify=self.target
        )
        
        logger.info(f"Training set size: {len(X_train)}")
        logger.info(f"Testing set size: {len(X_test)}")
        
        return X_train, X_test, y_train, y_test

# Test the data loader
if __name__ == "__main__":
    loader = MalariaDataLoader()
    data = loader.generate_sample_data(1000)
    features, target = loader.preprocess_data()
    X_train, X_test, y_train, y_test = loader.train_test_split()
    
    print("\n✅ Data loader test completed successfully!")
    print(f"Sample data:\n{data.head()}")
