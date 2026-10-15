import gradio as gr


def inputFoodForm(lookup_function):
    return gr.Interface(
        fn=lookup_function,
        inputs=[
            gr.Textbox(label="Food name", placeholder="Banana"),
            gr.Number(label="Quantity", value=1),
            gr.Textbox(label="Unit", value="piece"),
        ],
        outputs=gr.JSON(label="Result"),
        title="NutriWise Food Lookup",
    )