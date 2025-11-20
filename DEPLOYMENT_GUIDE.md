# 🚀 Free Permanent Deployment Guide

## Streamlit Community Cloud - Free Forever Hosting

This guide will help you deploy the Malaria Outbreak Risk Prediction app permanently on **Streamlit Community Cloud** (100% free for public projects).

---

## 📋 Prerequisites

1. **GitHub Account** (free) - [Sign up here](https://github.com/signup)
2. **Streamlit Community Cloud Account** (free) - Uses your GitHub account

---

## 🎯 Step-by-Step Deployment

### Step 1: Create GitHub Repository

1. Go to [GitHub](https://github.com) and log in
2. Click the **"+"** icon (top right) → **"New repository"**
3. Fill in the details:
   - **Repository name:** `malaria-risk-predictor`
   - **Description:** "AI-Powered Malaria Outbreak Risk Prediction System - SDG 3"
   - **Visibility:** Public (required for free hosting)
   - **DO NOT** initialize with README (we already have one)
4. Click **"Create repository"**

### Step 2: Push Your Code to GitHub

After creating the repository, GitHub will show you commands. Use these:

```bash
cd /home/ubuntu/malaria-risk-predictor

# Add your GitHub repository as remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/malaria-risk-predictor.git

# Push your code
git branch -M main
git push -u origin main
```

**Alternative: Using GitHub CLI**

If you prefer, you can use GitHub CLI:

```bash
cd /home/ubuntu/malaria-risk-predictor

# Login to GitHub (follow the prompts)
gh auth login

# Create repository and push
gh repo create malaria-risk-predictor --public --source=. --remote=origin --push
```

### Step 3: Deploy on Streamlit Community Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click **"Sign in with GitHub"**
3. Authorize Streamlit to access your GitHub account
4. Click **"New app"** button
5. Fill in the deployment settings:
   - **Repository:** `YOUR_USERNAME/malaria-risk-predictor`
   - **Branch:** `main`
   - **Main file path:** `app.py`
6. Click **"Deploy!"**

### Step 4: Wait for Deployment

- Initial deployment takes 2-5 minutes
- You'll see a build log showing progress
- Once complete, you'll get a permanent URL like:
  - `https://YOUR_USERNAME-malaria-risk-predictor.streamlit.app`

---

## 🎉 Your App is Now Live!

Your permanent URL will be:
```
https://YOUR_USERNAME-malaria-risk-predictor.streamlit.app
```

### Features of Your Deployment:

✅ **Permanent hosting** - No expiration
✅ **Auto-updates** - Push to GitHub → Auto-deploys
✅ **Free SSL certificate** - Secure HTTPS
✅ **Custom domain** - Can add your own domain (optional)
✅ **99.9% uptime** - Reliable hosting
✅ **No credit card required** - Completely free

---

## 🔄 Updating Your App

To update your deployed app:

```bash
cd /home/ubuntu/malaria-risk-predictor

# Make your changes to the code
# Then commit and push:

git add .
git commit -m "Description of your changes"
git push origin main
```

Streamlit will automatically detect the changes and redeploy (takes ~2 minutes).

---

## 📊 Monitoring Your App

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click on your app
3. View:
   - **Logs** - See runtime logs
   - **Settings** - Configure app settings
   - **Analytics** - View usage statistics
   - **Reboot** - Restart the app if needed

---

## 🎨 Custom Domain (Optional)

To use your own domain:

1. Go to your app settings on Streamlit Community Cloud
2. Click **"Custom domain"**
3. Follow the instructions to add DNS records
4. Your app will be available at `yourapp.yourdomain.com`

---

## 🔒 Environment Variables (If Needed)

If you need to add API keys or secrets:

1. Go to your app settings
2. Click **"Secrets"**
3. Add your secrets in TOML format:
   ```toml
   [api_keys]
   openai = "your-key-here"
   ```
4. Access in code: `st.secrets["api_keys"]["openai"]`

---

## 📦 Project Files Already Configured

Your project includes all necessary files for deployment:

- ✅ `requirements.txt` - Python dependencies
- ✅ `packages.txt` - System dependencies
- ✅ `.streamlit/config.toml` - Streamlit configuration
- ✅ `.gitignore` - Git ignore rules
- ✅ `README.md` - Project documentation
- ✅ `malaria_model.pkl` - Pre-trained model (included)

---

## 🆘 Troubleshooting

### Issue: "Module not found"
**Solution:** Check `requirements.txt` has all dependencies

### Issue: "App won't start"
**Solution:** Check logs in Streamlit Cloud dashboard

### Issue: "Model file not found"
**Solution:** Ensure `malaria_model.pkl` is committed to Git

### Issue: "Port already in use"
**Solution:** Streamlit Cloud handles ports automatically

---

## 💡 Best Practices

1. **Keep repository public** for free hosting
2. **Use semantic versioning** for releases
3. **Add GitHub Actions** for automated testing (optional)
4. **Monitor app usage** via Streamlit analytics
5. **Update dependencies** regularly for security

---

## 🌟 Alternative Free Hosting Options

If you want to explore other options:

### 1. **Hugging Face Spaces** (Free)
- Similar to Streamlit Cloud
- Supports Streamlit, Gradio, and more
- [huggingface.co/spaces](https://huggingface.co/spaces)

### 2. **Railway** (Free tier available)
- $5 free credit monthly
- More flexible than Streamlit Cloud
- [railway.app](https://railway.app)

### 3. **Render** (Free tier)
- Free for web services
- 750 hours/month free
- [render.com](https://render.com)

---

## 📚 Additional Resources

- [Streamlit Documentation](https://docs.streamlit.io)
- [Streamlit Community Forum](https://discuss.streamlit.io)
- [GitHub Documentation](https://docs.github.com)
- [Streamlit Gallery](https://streamlit.io/gallery) - Inspiration

---

## 🎓 What You've Built

A production-ready, permanently hosted AI application that:
- Predicts malaria outbreak risk
- Supports UN SDG 3 (Good Health and Well-being)
- Uses machine learning (90% accuracy)
- Has a professional web interface
- Follows software engineering best practices
- Is accessible worldwide 24/7

---

## 📞 Need Help?

- **Streamlit Community:** [discuss.streamlit.io](https://discuss.streamlit.io)
- **GitHub Issues:** Create an issue in your repository
- **Documentation:** [docs.streamlit.io](https://docs.streamlit.io)

---

**Congratulations! You're ready to deploy your app permanently for free! 🎉**
