# Algorithm Comparison: Bubble Sort vs Quicksort

This project compares **Bubble Sort** and **Quicksort** by measuring:
- Number of iterations
- Execution time

It generates an animated visualization using Matplotlib and exports the result as an MP4 video.

## Author
Monjaraz Briseño Luis Fernando

## Features
- Runs both algorithms on the same random datasets
- Evaluates multiple input sizes
- Tracks and prints iteration count and elapsed time
- Plots side-by-side graphs for Bubble Sort and Quicksort
- Exports an animation video with FFmpeg

## Requirements
- Python 3.8+
- NumPy
- Matplotlib
- FFmpeg installed and available in PATH

Install Python dependencies:

```bash
pip install numpy matplotlib
```

## File Structure

```text
Algorithm Comparation/
├── Algorithm Comparation Bubble vs Quicksort.py
└── README.md
```

## How to Run

From the project folder:

```bash
python "Algorithm Comparation Bubble vs Quicksort.py"
```

The script will:
1. Generate random arrays for predefined sizes
2. Run Bubble Sort and Quicksort
3. Print iteration and timing results in terminal
4. Draw both plots while iterating
5. Save the animation as:

```text
MonjarazBriseñoLuisFernando_Tarea11_BurbujaVsQuicksort.mp4
```

## Input Sizes Used

```python
[100, 200, 400, 800, 1600, 3200, 6400, 12800]
```

## Algorithms

### Bubble Sort (`Burbuja`)
- Repeatedly compares adjacent elements and swaps when needed
- Iteration complexity (average/worst): approximately $O(n^2)$
- Very slow for large arrays

### Quicksort (`Quicksort`)
- Recursive divide-and-conquer algorithm
- Uses the first element as pivot in this implementation
- Average complexity: $O(n \log n)$
- Worst-case complexity: $O(n^2)$ (depends on pivot quality)

## Output and Visualization
- Left chart: Bubble Sort iterations vs number of elements
- Right chart: Quicksort iterations vs number of elements
- Time labels are shown near each plotted point
- Terminal output logs both iteration counts and times for each size

## Notes
- Random seeds are fixed for reproducibility (`random.seed(10)` and `np.random.seed(10)`).
- The script uses interactive plotting (`plt.ion()`) while generating frames.
- FFmpeg is required by `matplotlib.animation` to export MP4.

## Troubleshooting

### FFmpeg not found
If you get an error related to FFmpeg writer:
- Install FFmpeg
- Add it to your system PATH
- Restart your terminal/IDE

### Slow execution for large sizes
Bubble Sort has quadratic behavior and becomes expensive for large arrays. This is expected and part of the comparison.

### Plot window does not appear
Some environments may block interactive windows. Run the script locally in a desktop session.

## Educational Value
This project is useful to understand practical differences between algorithmic complexities:
- $O(n^2)$ (Bubble Sort)
- $O(n \log n)$ (Quicksort average case)

It combines theory, timing, and visualization in one experiment.
