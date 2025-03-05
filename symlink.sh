#!/bin/sh

SOURCE=$1

# skip past first arg and loop
for ITEM in ${@:2}; do

  # if item is a directory create a symlink
  if [[ -d "./$ITEM" ]]; then
    ln -s "../$SOURCE" "$ITEM/$(basename $SOURCE)"
  fi
done
