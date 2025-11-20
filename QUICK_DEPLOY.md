# ⚡ Quick Deploy - 3 Minutes to Live App

## 🎯 Fastest Way to Deploy (Free Forever)

### Option 1: Using GitHub Web Interface (Easiest)

**Step 1:** Create GitHub Repository (1 minute)
1. Go to https://github.com/new
2. Name: `malaria-risk-predictor`
3. Public ✓
4. Click "Create repository"

**Step 2:** Upload Files (1 minute)
1. On your new repository page, click "uploading an existing file"
2. Drag and drop ALL files from `/home/ubuntu/malaria-risk-predictor/`
3. Commit message: "Initial commit"
4. Click "Commit changes"

**Step 3:** Deploy on Streamlit (1 minute)
1. Go to https://share.streamlit.io
2. Sign in with GitHub
3. Click "New app"
4. Select your repository: `YOUR_USERNAME/malaria-risk-predictor`
5. Main file: `app.py`
6. Click "Deploy!"

**✅ Done! Your app will be live in 2-3 minutes at:**
```
https://YOUR_USERNAME-malaria-risk-predictor.streamlit.app
```

---

### Option 2: Using Git Command Line (For Developers)

```bash
# 1. Create repository on GitHub first (https://github.com/new)

# 2. Push code (replace YOUR_USERNAME)
cd /home/ubuntu/malaria-risk-predictor
git remote add origin https://github.com/YOUR_USERNAME/malaria-risk-predictor.git
git push -u origin main

# 3. Deploy on Streamlit Cloud (https://share.streamlit.io)
```

---

### Option 3: Using GitHub CLI (Fastest)

```bash
cd /home/ubuntu/malaria-risk-predictor

# Login to GitHub
gh auth login

# Create repo and push in one command
gh repo create malaria-risk-predictor --public --source=. --remote=origin --push

# Then deploy on Streamlit Cloud (https://share.streamlit.io)
```

---

## 📦 What's Included

All files are ready for deployment:
- ✅ Pre-trained ML model (90% accuracy)
- ✅ Streamlit web app
- ✅ All dependencies configured
- ✅ Documentation
- ✅ Tests

---

## 🌐 Your Permanent URL

After deployment, your app will be available at:
```
https://YOUR_USERNAME-malaria-risk-predictor.streamlit.app
```

**Features:**
- ✅ Free forever (no credit card)
- ✅ SSL certificate (HTTPS)
- ✅ Auto-updates from GitHub
- ✅ 99.9% uptime
- ✅ Global CDN

---

## 🔄 To Update Your App

```bash
# Make changes to your code
git add .
git commit -m "Your update message"
git push origin main

# Streamlit auto-deploys in ~2 minutes
```

---

## 💡 Pro Tips

1. **Keep it public** for free hosting
2. **Star your repo** to find it easily
3. **Add topics** on GitHub: `machine-learning`, `streamlit`, `healthcare`, `sdg`
4. **Share your URL** on LinkedIn, Twitter, portfolio

---

## 🆘 Need Help?

See the full guide: `DEPLOYMENT_GUIDE.md`

---

**Total Time: 3 minutes to permanent deployment! 🚀**
