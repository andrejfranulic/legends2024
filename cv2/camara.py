import cv2
# Iniciar la captura de video
cap = cv2.VideoCapture(0)  # 0 es generalmente el ID de la cámara web integrada
while True:
    # Captura frame-por-frame
    ret, frame = cap.read()

    # Si frame se lee correctamente ret es True
    if not ret:
        print("No se puede recibir el frame (stream end?). Exiting ...")
        break

    # Nuestra operación en el frame viene aquí
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   # gray = cv2.cvtColor(frame, cv2.COLOR_)


    # Mostrar el frame resultante
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) == ord('x'):
        break

# Cuando todo está hecho, liberar la captura
cap.release()
cv2.destroyAllWindows()