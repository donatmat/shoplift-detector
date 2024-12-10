from shoplift_detector.video_processor import VideoProcessor
from shoplift_detector.detection import ShopliftingPrediction


def main():
    # Charger le modèle
    sp = ShopliftingPrediction(
        model_path="shoplift_detector/models/lrcn_160S_90_90Q.h5"
    )
    sp.load_model()

    # Chargement de la vidéo
    vp = VideoProcessor(video_path="examples/test_video.mp4")
    if not vp.load_video():
        print("Échec du chargement de la vidéo.")
        return

    while True:
        ret, frame = vp.get_next_frame()
        if not ret:
            print("Fin de la vidéo ou erreur de lecture.")
            break

        # Logique de détection avec le modèle
        # Ajoutez ici vos traitements avec `sp.predict(frame)`
        print("Traitement de la vidéo en cours...")

        # Afficher la vidéo en temps réel
        cv2.imshow("Vidéo de Test", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    vp.release_video()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
