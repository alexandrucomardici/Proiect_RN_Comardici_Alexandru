from flask import Flask, render_template_string, request
import numpy as np
from PIL import Image
import tensorflow as tf
import base64
from io import BytesIO

# --------------------------------------------------
# App setup
# --------------------------------------------------

app = Flask(__name__)

IMG_SIZE = (224, 224)
history = []

# --------------------------------------------------
# Load AI model
# --------------------------------------------------

try:
    model = tf.keras.models.load_model("animal_detector.keras")
except Exception as err:
    print(f"[ERROR] Model load failed: {err}")
    model = None

# --------------------------------------------------
# Frontend template
# --------------------------------------------------

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
<title>Animal Detector</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">

<style>
/* --- THEME COLORS --- */
:root {
    --bg-main: #0b0f1a;
    --card-bg: rgba(255,255,255,0.08);
    --border-glow: rgba(0,255,255,0.35);
    --accent1: #00f5ff;
    --accent2: #8a2be2;
    --text-soft: #cfd3ff;
}

/* --- GLOBAL --- */
body {
    min-height: 100vh;
    background:
        radial-gradient(circle at 20% 20%, rgba(138,43,226,0.25), transparent 40%),
        radial-gradient(circle at 80% 60%, rgba(0,245,255,0.25), transparent 40%),
        linear-gradient(180deg, #05070f, #0b0f1a);
    color: var(--text-soft);
    font-size: 1.1rem;
    overflow-x: hidden;
}

/* --- LAYOUT --- */
.col-left  { padding-right: 30px; }
.col-right { padding-left: 30px; }

/* --- TITLE EFFECT --- */
.blue-glow {
    background: linear-gradient(90deg, var(--accent1), var(--accent2));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: 0 0 20px rgba(0,245,255,0.35);
    letter-spacing: 1px;
}

/* --- GLASS CARD --- */
.card {
    background: var(--card-bg);
    backdrop-filter: blur(18px);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 18px;
    box-shadow:
        0 0 30px rgba(0,0,0,0.6),
        inset 0 0 30px rgba(255,255,255,0.03);
    transition: transform .25s ease, box-shadow .25s ease;
}

.card:hover {
    transform: translateY(-6px) scale(1.03);
    box-shadow:
        0 0 40px rgba(0,245,255,0.25),
        inset 0 0 40px rgba(255,255,255,0.05);
}

/* --- BUTTONS --- */
.btn-primary {
    background: linear-gradient(135deg, var(--accent1), var(--accent2));
    border: none;
    border-radius: 14px;
    font-weight: 600;
    box-shadow: 0 0 25px rgba(0,245,255,0.5);
}

.btn-primary:hover {
    box-shadow: 0 0 40px rgba(138,43,226,0.8);
    transform: scale(1.02);
}

/* --- IMAGE PREVIEW --- */
#previewBox {
    border: 2px dashed rgba(0,245,255,0.5);
    border-radius: 16px;
    padding: 25px;
    text-align: center;
    background: rgba(0,0,0,0.25);
}

.img-preview {
    max-width: 100%;
    max-height: 450px;
    border-radius: 16px;
    box-shadow: 0 0 35px rgba(0,245,255,0.45);
}

/* --- PROGRESS BAR --- */
.progress {
    background: rgba(255,255,255,0.1);
    border-radius: 20px;
    height: 14px;
}

.progress-bar {
    background: linear-gradient(90deg, var(--accent1), var(--accent2));
    box-shadow: 0 0 20px var(--accent1);
}

/* --- HISTORY --- */
.history-img {
    width: 110px;
    height: 110px;
    object-fit: cover;
    border-radius: 14px;
    box-shadow: 0 0 18px rgba(0,245,255,0.45);
}

/* --- PROB BUTTON --- */
.btn-outline-info {
    border-radius: 12px;
    border-color: var(--accent1);
    color: var(--accent1);
}

.btn-outline-info:hover {
    background: var(--accent1);
    color: #000;
    box-shadow: 0 0 20px var(--accent1);
}
</style>
</head>

<body>

<audio id="soundPredict" src="/static/dingsfx.mp3"></audio>
<audio id="soundResult" src="/static/datasfx.mp3"></audio>

<div class="container py-5">
<h2 class="text-center mb-5 blue-glow">Animal Detector AI</h2>

<div class="row gx-5">

<!-- LEFT PANEL -->
<div class="col-md-6 col-left">
<div class="card p-4 mb-4">
<form action="/predict" method="POST" enctype="multipart/form-data">
<label class="form-label blue-glow">Upload an Image</label>
<input type="file" name="image" accept="image/*" class="form-control mb-3" required onchange="previewImage(event)">
<div id="previewBox">Image preview appears here</div>
<button class="btn btn-primary w-100 mt-3">Run Detection</button>
</form>
</div>

{% if image_url %}
<div class="card p-3">
<h5 class="blue-glow">Uploaded Image</h5>
<img src="{{ image_url }}" class="img-preview">
</div>
{% endif %}
</div>

<!-- RIGHT PANEL -->
<div class="col-md-6 col-right">
{% if result %}
<div class="card p-4">
<h4 class="blue-glow mb-4">Prediction Details</h4>

<p><strong class="blue-glow">Species:</strong>
<span style="color:white;font-weight:700;">{{ result.species }}</span></p>

<p>
<strong class="blue-glow">Status:</strong>
<span style="color:white;font-weight:700;">{{ result.owner_status }}</span>

<button class="btn btn-sm btn-outline-info ms-3"
        onclick="toggleProbability()"
        id="probToggleBtn">
Show Probability
</button>
</p>

<div id="probContainer" hidden class="mt-3">
<p>
<strong class="blue-glow">Owner Probability:</strong>
<span style="color:white;font-weight:700;">
{{ "%.2f"|format(result.owner_prob * 100) }}%
</span>
</p>

<div class="progress mb-3">
<div class="progress-bar" style="width: {{ result.owner_prob * 100 }}%;"></div>
</div>
</div>

{% if result.size %}
<p><strong class="blue-glow">Size:</strong>
<span style="color:white;font-weight:700;">{{ result.size }}</span></p>
{% endif %}
</div>
{% endif %}

{% if history %}
<div class="card p-3 mt-4">
<h5 class="blue-glow">Recent Detections</h5>
<div class="d-flex gap-3">
{% for item in history %}
<div>
<img src="{{ item.img }}" class="history-img">
<p class="small text-center mt-1">
<span style="color:white;font-weight:700;">{{ item.species }}</span>
</p>
</div>
{% endfor %}
</div>
</div>
{% endif %}
</div>
</div>
</div>

<script>
function previewImage(event) {
    const reader = new FileReader();
    reader.onload = () => {
        document.getElementById('previewBox').innerHTML =
            `<img src="${reader.result}" class="img-preview">`;
        document.getElementById('soundPredict')?.play().catch(()=>{});
    };
    reader.readAsDataURL(event.target.files[0]);
}

function toggleProbability() {
    const box = document.getElementById("probContainer");
    const btn = document.getElementById("probToggleBtn");
    box.hidden = !box.hidden;
    btn.textContent = box.hidden ? "Show Probability" : "Hide Probability";
}

window.addEventListener("DOMContentLoaded", () => {
    {% if result %}
    document.getElementById('soundResult')?.play().catch(()=>{});
    {% endif %}
});
</script>

</body>
</html>
"""

# --------------------------------------------------
# Routes
# --------------------------------------------------

@app.route("/")
def index():
    return render_template_string(HTML_PAGE, history=history)


@app.route("/predict", methods=["POST"])
def predict():

    if model is None:
        return render_template_string(HTML_PAGE, history=history)

    file = request.files.get("image")
    if not file:
        return render_template_string(HTML_PAGE, history=history)

    # Read and prepare image
    raw_bytes = file.read()
    image = Image.open(BytesIO(raw_bytes)).convert("RGB").resize(IMG_SIZE)
    image_array = np.expand_dims(np.array(image) / 255.0, axis=0)

    # Model prediction
    species_pred, owner_pred, size_pred = model.predict(image_array, verbose=0)

    species = "dog" if np.argmax(species_pred[0]) == 1 else "cat"
    owner_prob = float(owner_pred[0][0])
    owner_status = "Owner ✅" if owner_prob > 0.40 else "Owner ❌"

    size = None
    if species == "dog":
        size_labels = ["small", "medium", "big"]
        size = size_labels[np.argmax(size_pred[0])]

    # Build result object
    result = type("Result", (), {
        "species": species,
        "owner_prob": owner_prob,
        "owner_status": owner_status,
        "size": size
    })()

    image_url = "data:image/jpeg;base64," + base64.b64encode(raw_bytes).decode()

    history.insert(0, {"img": image_url, "species": species})
    history[:] = history[:3]

    return render_template_string(
        HTML_PAGE,
        result=result,
        image_url=image_url,
        history=history
    )


if __name__ == "__main__":
    app.run(debug=True)
