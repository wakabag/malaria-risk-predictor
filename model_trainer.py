import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, f1_score
import joblib
import logging
import matplotlib.pyplot as plt
import seaborn as sns
from data_loader import MalariaDataLoader

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MalariaModelTrainer:
    """Model trainer for malaria outbreak risk prediction"""
    
    def __init__(self):
        self.model = None
        self.feature_names = None
        self.risk_levels = ['Low', 'Medium', 'High']
        
    def train_model(self, X_train, y_train, n_estimators=100, random_state=42):
        """Train Random Forest classifier"""
        logger.info("Training Random Forest model...")
        
        self.feature_names = X_train.columns.tolist()
        
        # Initialize and train model
        self.model = RandomForestClassifier(
            n_estimators=n_estimators,
            max_depth=10,
            min_samples_split=5,
            min_samples_leaf=2,
            random_state=random_state,
            class_weight='balanced',
            n_jobs=-1
        )
        
        self.model.fit(X_train, y_train)
        
        logger.info("Model training completed!")
        
        return self.model
    
    def evaluate_model(self, X_test, y_test):
        """Evaluate model performance"""
        if self.model is None:
            raise ValueError("Model not trained. Call train_model() first.")
        
        logger.info("Evaluating model...")
        
        # Make predictions
        y_pred = self.model.predict(X_test)
        
        # Calculate metrics
        accuracy = accuracy_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred, average='weighted')
        
        logger.info(f"Accuracy: {accuracy:.3f}")
        logger.info(f"F1 Score (weighted): {f1:.3f}")
        
        # Classification report
        print("\n📊 Classification Report:")
        print(classification_report(y_test, y_pred))
        
        # Confusion matrix
        cm = confusion_matrix(y_test, y_pred)
        print("\n🔍 Confusion Matrix:")
        print(cm)
        
        return {
            'accuracy': accuracy,
            'f1_score': f1,
            'confusion_matrix': cm,
            'predictions': y_pred
        }
    
    def plot_feature_importance(self, top_n=10):
        """Plot feature importance"""
        if self.model is None:
            raise ValueError("Model not trained. Call train_model() first.")
        
        # Get feature importances
        importances = self.model.feature_importances_
        indices = np.argsort(importances)[::-1][:top_n]
        
        # Create plot
        plt.figure(figsize=(10, 6))
        plt.title("Top Feature Importances")
        plt.bar(range(top_n), importances[indices])
        plt.xticks(range(top_n), [self.feature_names[i] for i in indices], rotation=45, ha='right')
        plt.xlabel("Features")
        plt.ylabel("Importance")
        plt.tight_layout()
        plt.savefig('/home/ubuntu/malaria-risk-predictor/feature_importance.png', dpi=150)
        logger.info("Feature importance plot saved!")
        plt.close()
        
        return importances
    
    def save_model(self, filepath='malaria_model.pkl'):
        """Save trained model to disk"""
        if self.model is None:
            raise ValueError("Model not trained. Call train_model() first.")
        
        model_data = {
            'model': self.model,
            'feature_names': self.feature_names,
            'risk_levels': self.risk_levels
        }
        
        joblib.dump(model_data, filepath)
        logger.info(f"Model saved to {filepath}")
    
    def load_model(self, filepath='malaria_model.pkl'):
        """Load trained model from disk"""
        model_data = joblib.load(filepath)
        self.model = model_data['model']
        self.feature_names = model_data['feature_names']
        self.risk_levels = model_data['risk_levels']
        logger.info(f"Model loaded from {filepath}")

def main():
    """Main training pipeline"""
    # Load and prepare data
    loader = MalariaDataLoader()
    loader.generate_sample_data(1000)
    features, target = loader.preprocess_data()
    X_train, X_test, y_train, y_test = loader.train_test_split()
    
    # Train model
    trainer = MalariaModelTrainer()
    trainer.train_model(X_train, y_train)
    
    # Evaluate model
    results = trainer.evaluate_model(X_test, y_test)
    
    # Plot feature importance
    trainer.plot_feature_importance()
    
    # Save model
    trainer.save_model()
    
    print("\n✅ Model training pipeline completed successfully!")
    
    return trainer, results

if __name__ == "__main__":
    main()
