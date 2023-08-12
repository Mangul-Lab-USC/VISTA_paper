#!/bin/bash

# Specify the path to the Python script
PYTHON_SCRIPT="REFtoVCF.py"

FILES=$(ls HG*_dipcall.dip.vcf)

for FILE in $FILES; do
  BASENAME=$(basename "$FILE" _dipcall.dip.vcf)

  OUTPUT_FILE="${BASENAME}_reference.vcf"

  python "$PYTHON_SCRIPT" "$FILE" "$OUTPUT_FILE"

  echo "Converted $FILE to $OUTPUT_FILE"
done