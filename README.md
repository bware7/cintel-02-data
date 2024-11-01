# cintel-02-data
An interactive Shiny app for exploring the Palmer Penguins dataset. This app uses Python libraries like Pandas, Plotly, Matplotlib, and Seaborn to display penguin data in charts and tables, providing insights into key attributes like body mass, bill length, and flipper length. The app includes a sidebar for user interactions, allowing for dynamic data exploration and visualization adjustments.

## Features

Sidebar with User Controls:

  - Dropdown to select attributes for visualization.
  - Adjustable bin count for both Plotly and Seaborn histograms.
  - Checkbox filter to select penguin species for viewing.
  - Link to the project’s GitHub repository for code access.

Visualizations and Data Tables:

  - Plotly Histogram: Displays a histogram for selected attributes with species-specific coloring.
  - Plotly Scatterplot: Interactive scatterplot of body mass vs. bill depth, colored by species.
  - Seaborn Histogram: Displays a histogram of body mass with species-separated bins.
  - Data Table and Data Grid: Display the entire dataset for easy data browsing.
  - Summary Statistics Table: Provides descriptive statistics (mean, min, max, etc.) for numerical attributes.

## Installation
To run this project, ensure the following packages are installed:

    - pandas
    - plotly
    - matplotlib
    - seaborn
    - palmerpenguins
