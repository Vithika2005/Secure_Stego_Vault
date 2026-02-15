from PIL import Image
import numpy as np

def detect_lsb_anomaly(image_path: str) -> float:
    """
    Returns anomaly score based on LSB distribution.
    Higher = more likely hidden data.
    """
    img = Image.open(image_path).convert("RGB")
    pixels = np.array(img)

    lsb = pixels & 1
    ones_ratio = lsb.mean()

    # Ideal natural images ~0.5, deviations suggest manipulation
    anomaly_score = abs(0.5 - ones_ratio)

    return anomaly_score
