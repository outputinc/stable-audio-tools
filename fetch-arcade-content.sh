#!/bin/bash

#
# fetch-arcade-content.sh
#
# Fetch Arcade Content / Output folder from S3, and unpack it to the shared
# location on disk expected by Arcade.
#
# Usage
# -----
# ./scripts/fetch-arcade-content.sh [--testing] [--no-copy]
#
# Must be run from text2track repo root.
#
# Options
# -------
# --testing
#     Use (smaller) testing content archive.
#
# --no-copy
#     Do not copy to shared location; content will be left in place.
#


set -eu

THIS_SCRIPT=$(basename "$0")
OUTPUT_FOLDER_S3_URL="s3://text2track-internal/arcade/OutputFolder.tar"

DO_COPY=true

for arg in "$@"; do
  case $arg in
    --testing)
      # fetch content for CI testing
      OUTPUT_FOLDER_S3_URL="s3://text2track-internal/testing/arcade/OutputFolder.tar"
      ;;
    --no-copy)
      # disable copy step
      DO_COPY=false
      ;;
    *)
      echo "Unknown argument: ${arg}"
      ;;
  esac
done

START_TIME=$SECONDS

# copy from S3 and unpack
echo "downloading archive from S3"
# piping directly to tar improves overall runtime
aws s3 cp "$OUTPUT_FOLDER_S3_URL" - | tar -x

ELAPSED_TIME=$(($SECONDS - $START_TIME))

THIS_SCRIPT=$(basename "$0")
echo "${THIS_SCRIPT}: completed in ${ELAPSED_TIME} seconds"
