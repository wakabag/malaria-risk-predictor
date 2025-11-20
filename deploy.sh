#!/bin/bash

# Deployment Script for Malaria Risk Predictor
# This script helps you deploy to GitHub quickly

echo "🦟 Malaria Risk Predictor - GitHub Deployment Helper"
echo "=================================================="
echo ""

# Check if git is initialized
if [ ! -d .git ]; then
    echo "❌ Git repository not initialized!"
    echo "Run: git init"
    exit 1
fi

# Get GitHub username
echo "📝 Enter your GitHub username:"
read GITHUB_USERNAME

if [ -z "$GITHUB_USERNAME" ]; then
    echo "❌ GitHub username is required!"
    exit 1
fi

# Repository name
REPO_NAME="malaria-risk-predictor"

echo ""
echo "📦 Repository details:"
echo "   Username: $GITHUB_USERNAME"
echo "   Repository: $REPO_NAME"
echo ""

# Check if remote already exists
if git remote | grep -q "origin"; then
    echo "⚠️  Remote 'origin' already exists. Removing..."
    git remote remove origin
fi

# Add remote
echo "🔗 Adding GitHub remote..."
git remote add origin "https://github.com/$GITHUB_USERNAME/$REPO_NAME.git"

echo ""
echo "✅ Remote added successfully!"
echo ""
echo "📤 Next steps:"
echo ""
echo "1. Create the repository on GitHub:"
echo "   Go to: https://github.com/new"
echo "   Repository name: $REPO_NAME"
echo "   Visibility: Public"
echo "   DO NOT initialize with README"
echo ""
echo "2. Push your code:"
echo "   git push -u origin main"
echo ""
echo "3. Deploy on Streamlit Cloud:"
echo "   Go to: https://share.streamlit.io"
echo "   Click 'New app'"
echo "   Select: $GITHUB_USERNAME/$REPO_NAME"
echo "   Main file: app.py"
echo ""
echo "🎉 Your app will be live at:"
echo "   https://$GITHUB_USERNAME-$REPO_NAME.streamlit.app"
echo ""
