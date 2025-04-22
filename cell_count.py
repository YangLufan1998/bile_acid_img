import numpy as np
import os
import argparse
import csv
from cellpose import models, io
import matplotlib.pyplot as plt
from skimage import measure

def count_cells(img,model):
    masks, flows, styles, diams = model.eval(img, diameter=None, channels=[0,0])
    cell_count = masks.max()
    return cell_count, masks

def annotate_and_save(img, masks, save_path):
    fig, ax = plt.subplots(figsize=(8,8))
    ax.imshow(img, cmap='gray')
    props = measure.regionprops(masks)
    for prop in props:
        y0, x0 = prop.centroid
        ax.text(x0, y0, str(prop.label),
                color='yellow', fontsize=6,
                ha='center', va='center')
    ax.axis('off')
    fig.savefig(save_path, dpi=300, bbox_inches='tight', pad_inches=0)
    plt.close(fig)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Count cells in all images in a folder and summarize per-sample totals."
    )
    parser.add_argument("input_dir", help="Directory containing image files.")
    parser.add_argument(
        "--output_csv", help="Path to save summary CSV.", default=None
    )
    parser.add_argument(
        "--annotate_dir",
        help="Directory to save annotated images (optional).",
        default=None,
    )

    args = parser.parse_args()
    if args.annotate_dir:
        os.makedirs(args.annotate_dir, exist_ok=True)
    
    model = models.Cellpose(gpu=False, model_type='cyto')
    
    with open(args.output_csv, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['filename', 'cell_count'])

            for fname in sorted(os.listdir(args.input_dir)):
                if not fname.endswith('.tiff'):
                    continue

                img_path = os.path.join(args.input_dir, fname)
                print(f"Processing {fname}...")
                img = io.imread(img_path)
                count, masks = count_cells(img, model)
                print(f"Detected {count} cells")
                writer.writerow([fname, count])

                if args.annotate_dir:
                    out_fname = fname.split(".")[0] + "_annotated.png"
                    save_path = os.path.join(args.annotate_dir, out_fname)
                    annotate_and_save(img, masks, save_path)

    print(f"Done! Results written to {args.output_csv}")

    