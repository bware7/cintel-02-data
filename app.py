import matplotlib.pyplot as plt
from shiny import ui, render, App
import palmerpenguins

penguins_df = palmerpenguins.load_penguins()

app_ui = ui.page_fluid(
    ui.layout_sidebar(
        ui.sidebar(
            ui.h3("Penguin Visualizations By Bin Ware") 
        ),
        ui.output_plot("plot_body_mass"), 
        ui.output_plot("plot_flipper_length")
    )
)

def server(input, output, session):
    @output
    @render.plot  
    def plot_body_mass():
        fig, ax = plt.subplots()
        ax.hist(penguins_df["body_mass_g"].dropna(), bins=20, color="skyblue")
        ax.set_title("Penguin Body Mass")
        ax.set_xlabel("Body Mass (g)")
        ax.set_ylabel("Frequency")
        return fig 

    @output
    @render.plot 
    def plot_flipper_length():
        fig, ax = plt.subplots()
        ax.hist(penguins_df["flipper_length_mm"].dropna(), bins=20, color="salmon")
        ax.set_title("Penguin Flipper Length")
        ax.set_xlabel("Flipper Length (mm)")
        ax.set_ylabel("Frequency")
        return fig  

app = App(app_ui, server)
