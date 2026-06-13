# Basic flow
git init
git add .
git commit -m "Initial commit"
git branch -M main
git push -u origin main

# Branching
git checkout -b feature/new-model
# ...work...
git commit -m "Add new model"
git push origin feature/new-model
