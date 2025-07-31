from flask import Flask, render_template, request
import requests

app = Flask(__name__)

PLATFORMS = {
    "Facebook": "https://www.facebook.com/{}",
    "Instagram": "https://www.instagram.com/{}",
    "X (Twitter)": "https://x.com/{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "GitHub": "https://github.com/{}",
    "TikTok": "https://www.tiktok.com/@{}",
    "Pinterest": "https://www.pinterest.com/{}",
    "LinkedIn": "https://www.linkedin.com/in/{}",
    "Snapchat": "https://www.snapchat.com/add/{}"
}

def check_username(platform, url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return True
    except:
        pass
    return False

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    username = None

    if request.method == 'POST':
        username = request.form['username']
        for platform, base_url in PLATFORMS.items():
            full_url = base_url.format(username)
            found = check_username(platform, full_url)
            results.append({
                "platform": platform,
                "found": found,
                "url": full_url,
                "suspicious": "No"
            })

    return render_template('index.html', results=results, username=username)

if __name__ == '__main__':
    app.run(debug=True)
