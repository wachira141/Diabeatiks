#!/usr/bin/bash
#sets the React js library

echo "-----------------------------------------------------------------------"
echo "create a directory webstatics"
echo "---------------------------------------------------------------------"
mkdir -p /home/kenya/Desktop/Portfolio/web_static

cd /home/kenya/Desktop/Portfolio/web_static
sudo npx create-react-app diabetics
# cd /home/kenya/Desktop/Portfolio/web_static/Portfolio/portfolio/src
# npm install styled-components react-router react-icons
sed -i 's\"name": "portfolio"\"name": "Diabetics"\' /home/kenya/Desktop/Portfolio/web_static/diabetics/package.json
sed -i 's\"start": "react-scripts start"\"start":"npm start"\' /home/kenya/Desktop/Portfolio/web_static/diabetics/package.json


npm start