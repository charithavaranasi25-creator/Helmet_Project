
import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np
import cv2

# ---------- Page Setup ----------
st.set_page_config(
    page_title="Helmet Detection System",
    page_icon="🪖",
    layout="wide"
)

st.title("🪖 Helmet Detection System")
st.write(
    "Upload an image to detect helmets and head regions "
    "using a YOLO deep-learning model."
)

# ---------- Load YOLO Model ----------
@st.cache_resource
def load_model():
    return YOLO("final.pt")

try:
    model = load_model()
    st.success("Helmet detection model loaded successfully!")
except Exception as e:
    st.error(f"Unable to load the model: {e}")
    st.stop()

# ---------- Image Upload ----------
uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    try:
        image = Image.open(uploaded_file).convert("RGB")
        img_array = np.array(image)

        st.subheader("Uploaded Image")

        col1, col2 = st.columns(2)

        with col1:
            st.image(
                image,
                caption="Original Image",
                use_container_width=True
            )

        # ---------- Detection ----------
        if st.button("🔍 Detect Helmet", type="primary"):
            with st.spinner("Detecting objects..."):
                results = model(img_array, verbose=False)
                result = results[0]

                # YOLO plot returns an image in BGR format
                annotated_image = result.plot()
                annotated_rgb = cv2.cvtColor(
                    annotated_image,
                    cv2.COLOR_BGR2RGB
                )

            with col2:
                st.image(
                    annotated_rgb,
                    caption="Detection Result",
                    use_container_width=True
                )

            # ---------- Detection Summary ----------
            st.subheader("Detection Summary")

            if result.boxes is not None and len(result.boxes) > 0:
                st.success(
                    f"Detected {len(result.boxes)} object(s)."
                )

                for box in result.boxes:
                    class_id = int(box.cls[0].item())
                    confidence = float(box.conf[0].item())
                    class_name = model.names[class_id]

                    st.write(
                        f"**{class_name}** — "
                        f"Confidence: {confidence:.2%}"
                    )
            else:
                st.warning("No objects were detected in this image.")

            st.info(
                "The results depend on the classes learned by "
                "your trained YOLO model."
            )

    except Exception as e:
        st.error(f"Error processing the image: {e}")

# ---------- Footer ----------
st.divider()
st.caption(
    "Helmet Detection System | Python • YOLO • OpenCV • Streamlit"
)
