from flask import Flask, render_template_string, request
import numpy as np
from PIL import Image
import tensorflow as tf
import base64
from io import BytesIO

app = Flask(__name__)

# Încarcă modelul
try:
    model = tf.keras.models.load_model("animal_detector.keras")
except Exception as e:
    print(f"Eroare la încărcarea modelului: {e}")
    model = None

IMG_SIZE = (224, 224)
history = []

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
<title>Animal Detector</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">

<style>
body {
    background-color: #1a1a1d;
    color: white;
    background-image: radial-gradient(circle at 50% 50%, rgba(0,140,255,0.2) 0%, transparent 40%),
                      radial-gradient(circle at 20% 50%, rgba(0,140,255,0.15) 0%, transparent 40%);
    font-size: 1.15rem;
}

/* distanță orizontală în plus între coloane */
.col-left { padding-right: 25px; }
.col-right { padding-left: 25px; }

.card {
    background-color: #222227;
    border: 1px solid #333;
    border-radius: 12px;
    box-shadow: 0 0 15px rgba(0, 123, 255, 0.2);
    transform: scale(1.05);
    transition: transform .2s ease, box-shadow .2s ease;
}

.card:hover {
    transform: scale(1.09);
    box-shadow: 0 0 25px rgba(0, 123, 255, 0.4);
}

.btn-primary {
    background-color: #007bff;
    border-color: #007bff;
    box-shadow: 0 0 15px #007bff;
}
.btn-primary:hover {
    background-color: #3399ff;
    border-color: #3399ff;
    box-shadow: 0 0 25px #3399ff;
}

.progress-bar {
    background-color: #007bff;
    box-shadow: 0 0 10px #007bff;
}

.blue-glow {
    color: #007bff;
    text-shadow: 0 0 8px #007bff;
}

.img-preview {
    max-width: 100%;
    max-height: 450px;
    border-radius: 10px;
    box-shadow: 0 0 15px rgba(0, 123, 255, 0.4);
}

#previewBox {
    border: 2px dashed #007bff;
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    color: #007bff;
}

.history-img {
    width: 110px;
    height: 110px;
    object-fit: cover;
    border-radius: 8px;
}
</style>
</head>

<body>

<audio id="soundPredict" src="/static/dingsfx.mp3"></audio>
<audio id="soundResult" src="/static/datasfx.mp3"></audio>

<div class="container py-5">
<h2 class="text-center mb-5 blue-glow">Animal Detector</h2>

<!-- AICI AM MODIFICAT gx-5 -->
<div class="row gx-5">

<!-- LEFT -->
<div class="col-md-6 col-left">
<div class="card p-4 shadow-sm mb-4">
<form action="/predict" method="POST" enctype="multipart/form-data">
<label class="form-label blue-glow">Upload an Image</label>
<input type="file" name="image" accept="image/*" class="form-control mb-3" required onchange="previewImage(event)">
<div id="previewBox">Image preview appears here</div>
<button class="btn btn-primary w-100 mt-3">Predict</button>
</form>
</div>

{% if image_url %}
<div class="card p-3 shadow-sm">
<h5 class="blue-glow">Uploaded Image:</h5>
<img src="{{ image_url }}" class="img-preview">
</div>
{% endif %}
</div>

<!-- RIGHT -->
<div class="col-md-6 col-right">
{% if result %}
<div class="card p-4 shadow-sm">
<h4 class="blue-glow mb-4">Prediction Details</h4>

<p>
    <strong class='blue-glow'>Species:</strong>
    <span style='color:white;'>{{ result.species }}</span>
</p>

<p>
    <strong class='blue-glow'>Status:</strong>
    <span style='color:white;'>{{ result.owner_status }}</span>

    <button type="button" 
            class="btn btn-sm btn-outline-info ms-3"
            onclick="toggleProbability()"
            id="probToggleBtn">
        Show Probability
    </button>
</p>

<!-- Ascuns inițial -->
<div id="probContainer" hidden class="mt-3">
    <p>
        <strong class="blue-glow">Owner Probability:</strong>
        <span style="color:white;">
            {{ "%.2f"|format(result.owner_prob * 100) }}%
        </span>
    </p>

    <div class="progress mb-3">
        <div class="progress-bar" role="progressbar"
             style="width: {{ result.owner_prob * 100 }}%;">
        </div>
    </div>
</div>

{% if result.size %}
<p>
    <strong class='blue-glow'>Size:</strong>
    <span style='color:white;'>{{ result.size }}</span>
</p>
{% endif %}

</div>
{% endif %}

{% if history %}
<div class="card p-3 shadow-sm mt-4">
<h5 class="blue-glow">Recent Detections:</h5>
<div class="d-flex gap-3">
{% for item in history %}
<div>
    <img src="{{ item.img }}" class="history-img">
    <p class="small text-center">{{ item.species }}</p>
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
    reader.onload = function() {
        document.getElementById('previewBox').innerHTML =
            `<img src="${reader.result}" class='img-preview'>`;

        const soundPredict = document.getElementById('soundPredict');
        if (soundPredict) {
            soundPredict.play().catch(e => {});
        }
    }
    reader.readAsDataURL(event.target.files[0]);
}

function toggleProbability() {
    const box = document.getElementById("probContainer");
    const btn = document.getElementById("probToggleBtn");

    const hidden = box.hidden;

    box.hidden = !hidden;
    btn.textContent = hidden ? "Hide Probability" : "Show Probability";
}

window.addEventListener("DOMContentLoaded", function() {
    {% if result %}
    const soundResult = document.getElementById('soundResult');
    if (soundResult) soundResult.play().catch(e => {});
    {% endif %}
});
</script>

</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_PAGE, history=history)

@app.route("/predict", methods=["POST"])
def predict():
    if model is None:
        return render_template_string(HTML_PAGE, result=None, history=history)

    file = request.files.get("image")
    if not file:
        return render_template_string(HTML_PAGE, result=None, history=history)

    file_bytes = file.read()
    img_stream = BytesIO(file_bytes)
    img = Image.open(img_stream).convert("RGB").resize(IMG_SIZE)
    arr = np.expand_dims(np.array(img) / 255.0, 0)

    species_pred, owner_pred, size_pred = model.predict(arr, verbose=0)

    species = "dog" if np.argmax(species_pred[0]) == 1 else "cat"
    owner_prob = float(owner_pred[0][0])
    owner_status = "Owner ✅" if owner_prob > 0.40 else "Owner ❌"

    size = None
    if species == "dog":
        size_labels = ["small", "medium", "big"]
        size = size_labels[np.argmax(size_pred[0])]

    result = type("obj", (object,), {
        "species": species,
        "owner_prob": owner_prob,
        "owner_status": owner_status,
        "size": size
    })()

    image_url = "data:image/jpeg;base64," + base64.b64encode(file_bytes).decode()
    history.insert(0, {"img": image_url, "species": species})
    if len(history) > 3:
        history.pop()

    return render_template_string(HTML_PAGE, result=result, image_url=image_url, history=history)

if __name__ == "__main__":
    app.run(debug=True)
