"""Runs ChartExtractor given an AWS Batch job."""

from ChartExtractor.extraction.extraction import digitize_sheet
from datetime import datetime
import onnxruntime as ort
import os
from PIL import Image

print("Hello from inside the container!")
print(f"ORT device: {ort.get_device()}")
PASSED_INPUT = os.environ.get("PASSED_INPUT")
NON_PASSED_INPUT = os.environ.get("NON_PASSED_INPUT")
print(f"This job was passed the input of \"{PASSED_INPUT}\"!")
print(f"If an input was not passed, it will come out like this: {NON_PASSED_INPUT}...")

intraop_image = Image.open("/ChartExtractor/data/RC_0001_intraoperative.JPG")
prepostop_image = Image.open("/ChartExtractor/data/RC_0001_preoperative_postoperative.JPG")

start = datetime.now()
data = digitize_sheet(intraop_image, prepostop_image)
end = datetime.now()
print(f"Data: {data}")
print(f"Time Elapsed: {end-start}")
