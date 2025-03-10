import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create figure and axis
fig, ax = plt.subplots(figsize=(6, 8))
ax.set_xlim(0, 6)
ax.set_ylim(0, 10)
ax.axis('off')  # Hide axis labels

# Define positions for the elements
positions = {
    "Start": (3, 9),
    "Image Acquisition": (3, 7.5),
    "Data Processing": (3, 6),
    "Crack Detection": (3, 4.5),
    "Display Results": (3, 3),
    "User Feedback": (3, 1.5),
    "End": (3, 0.5)
}

# Draw shapes
shapes = {
    "Start": patches.Ellipse(positions["Start"], width=2, height=0.8, edgecolor='black', facecolor='lightgray'),
    "Image Acquisition": patches.Rectangle((2, 7.1), width=2, height=0.8, edgecolor='black', facecolor='lightblue'),
    "Data Processing": patches.Rectangle((2, 5.6), width=2, height=0.8, edgecolor='black', facecolor='lightblue'),
    "Crack Detection": patches.Rectangle((2, 4.1), width=2, height=0.8, edgecolor='black', facecolor='lightblue'),
    "Display Results": patches.Rectangle((2, 2.6), width=2, height=0.8, edgecolor='black', facecolor='lightblue'),
    "User Feedback": patches.Rectangle((2, 1.1), width=2, height=0.8, edgecolor='black', facecolor='lightblue'),
    "End": patches.Ellipse(positions["End"], width=2, height=0.8, edgecolor='black', facecolor='lightgray'),
}

# Add shapes to plot
for shape in shapes.values():
    ax.add_patch(shape)

# Add text labels
for label, (x, y) in positions.items():
    ax.text(x, y, label, fontsize=12, ha='center', va='center', fontweight='bold')

# Draw arrows to indicate flow
arrows = [
    ((3, 8.6), (3, 8)),  # Start to Image Acquisition
    ((3, 7.1), (3, 6.5)),  # Image Acquisition to Data Processing
    ((3, 5.6), (3, 5)),  # Data Processing to Crack Detection
    ((3, 4.1), (3, 3.5)),  # Crack Detection to Display Results
    ((3, 2.6), (3, 2)),  # Display Results to User Feedback
    ((3, 1.1), (3, 0.9))  # User Feedback to End
]

for (x1, y1), (x2, y2) in arrows:
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="->", lw=1.5))

# Save and display the flowchart
plt.savefig("jackal_crack_detection_flowchart.png", dpi=300)
plt.show()
