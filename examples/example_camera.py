from shoplift_detector.camera_stream import CameraStream
from shoplift_detector.detection import ShopliftingPrediction


def main():
    # Configuration de la caméra
    stream = CameraStream(source=0)  # 0 correspond à la webcam par défaut
    if not stream.initialize_stream():
        print("Impossible de démarrer le flux vidéo.")
        return

    # Charger le modèle
    sp = ShopliftingPrediction(
        model_path="shoplift_detector/models/lrcn_160S_90_90Q.h5"
    )
    sp.load_model()

    try:
        while True:
            ret, frame = stream.get_frame()
            if not ret:
                print("Impossible de lire une frame depuis le flux vidéo.")
                continue

            # Logique de détection
            # Ici, ajoutez vos traitements avec `sp.predict(frame)`
            print("Traitement en cours...")

            # Afficher le flux vidéo en temps réel
            cv2.imshow('Flux Détection', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    except KeyboardInterrupt:
        print("\nInterruption de l'exécution...")
    finally:
        stream.release_stream()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
