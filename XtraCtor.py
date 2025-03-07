import fitz
import os

def extract_images(pdf_path, output_folder):
    doc = fitz.open(pdf_path)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    image_count = 0

    for page_num in range(len(doc)):
        page = doc[page_num]
        images = page.get_images(full=True)

        for img_index, img in enumerate(images):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            img_ext = base_image["ext"]

            img_filename = f"{output_folder}/page{page_num+1}_img{img_index+1}.{img_ext}"
            with open(img_filename, "wb") as img_file:
                img_file.write(image_bytes)

            image_count += 1

    print(f"Extracted {image_count} images. Check '{output_folder}'.")

pdf_file = "sample.pdf"
output_folder = "extracted_images"
extract_images(pdf_file, output_folder)
