import random

import gradio as gr

demo = gr.Blocks()

with demo:
    gr.Markdown(
        "Load the flashcards in the table below, then use the Practice tab to practice."
    )

    with gr.Tab("Word Bank"):
        flashcards_table = gr.Dataframe(headers=["front", "back"], type="array")
    with gr.Tab("Practice"):
        with gr.Row():
            with gr.Column():
                front = gr.Textbox(label="Prompt")
                with gr.Row():
                    new_btn = gr.Button("New Card")
                    flip_btn = gr.Button("Flip Card")
            with gr.Column(visible=False) as answer_col:
                back = gr.Textbox(label="Answer")
                selected_card = gr.State()
                with gr.Row():
                    correct_btn = gr.Button("Correct")
                    incorrect_btn = gr.Button("Incorrect")

    with gr.Tab("Results", visible=False) as results_tab:
        results = gr.State(value={})
        correct_field = gr.Markdown("# Correct: 0")
        incorrect_field = gr.Markdown("# Incorrect: 0")
        gr.Markdown("Card Statistics: ")
        results_table = gr.Dataframe(headers=["Card", "Correct", "Incorrect"])

    def load_new_card(flashcards):
        card = random.choice(flashcards)
        return (
            card,
            card[0],
            gr.Column(visible=False),
        )

    new_btn.click(
        load_new_card,
        [flashcards_table],
        [selected_card, front, answer_col],
    )

    def flip_card(card):
        return card[1], gr.Column(visible=True)

    flip_btn.click(flip_card, [selected_card], [back, answer_col])

    def mark_correct(card, results):
        if card[0] not in results:
            results[card[0]] = [0, 0]
        results[card[0]][0] += 1
        correct_count = sum(result[0] for result in results.values())
        return (
            results,
            f"# Correct: {correct_count}",
            [[front, scores[0], scores[1]] for front, scores in results.items()],
        )

    def mark_incorrect(card, results):
        if card[0] not in results:
            results[card[0]] = [
                0, 0]
        results[card[0]][1] += 1
        incorrect_count = sum(result[1] for result in results.values())
        return (
            results,
            f"# Inorrect: {incorrect_count}",
            [[front, scores[0], scores[1]] for front, scores in results.items()],
        )

    def toggle_results_tab():
        return gr.Tab("Results", visible=True)

    correct_btn.click(
        mark_correct,
        [selected_card, results],
        [results, correct_field, results_table],
    )

    incorrect_btn.click(mark_incorrect, [selected_card, results], [results, incorrect_field, results_table])

    # set results tab to visible when correct or incorrect button is clicked
    correct_btn.click(fn=toggle_results_tab, outputs=[results_tab])
    incorrect_btn.click(fn=toggle_results_tab, outputs=[results_tab])

if __name__ == "__main__":
    demo.launch()
