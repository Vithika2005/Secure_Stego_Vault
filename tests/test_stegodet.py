from stego.detection import detect_lsb_anomaly

print("Testing clean image...")
score_clean = detect_lsb_anomaly("assets/sample.png")
print("Clean score:", score_clean)

print("\nTesting stego image...")
score_stego = detect_lsb_anomaly("data/vault.png")
print("Stego score:", score_stego)
