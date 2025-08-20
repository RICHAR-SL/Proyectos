import gradio as gr

# tus funciones process_uploaded_image, process_camera_image, etc.

def create_gradio_interface():
    with gr.Blocks() as upload_interface:
        gr.Markdown("# 📸 Subir Imagen")
        input_image = gr.Image(type="pil", label="Imagen")
        output_image = gr.Image(label="Resultado")
        analysis_text = gr.Textbox(label="📊 Detalles")
        input_image.change(fn=process_uploaded_image, inputs=input_image, outputs=[output_image, analysis_text])

    with gr.Blocks() as camera_interface:
        gr.Markdown("# 📹 Cámara Web")
        camera_input = gr.Image(sources=["webcam"], type="pil", label="Captura")
        camera_output = gr.Image(label="Resultado")
        camera_analysis = gr.Textbox(label="📊 Detalles")
        camera_input.change(fn=process_camera_image, inputs=camera_input, outputs=[camera_output, camera_analysis])

    demo = gr.TabbedInterface(
        [upload_interface, camera_interface],
        ["📸 Subir Imagen", "📹 Cámara Web"],
        title="🧠 Detector de Emociones"
    )
    return demo

demo = create_gradio_interface()
