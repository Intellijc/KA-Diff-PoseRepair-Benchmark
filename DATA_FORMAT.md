# Track format and video splits

Each versioned detector archive contains a `tracks/` directory and a detector-specific normalization JSON at the variant root. Use `dataset_stats.json` for HRNet-W48 and `vitpose_h_dataset_stats.json` for ViTPose-H. Do not mix the two variants' statistics.

Each track file is scoped to one video. Legacy PKL files organize `frames` with per-frame `instances`; the pose loader uses instance fields `track_id`, `gt_keypoints`, and `pred_keypoints`. The evaluation uses 17 two-dimensional joint locations. The archives do not include image pixels. PKL is a serialization format; load files only if they come from the authorized source and pass the checksum check.

Each variant has 534 benchmark training video files, 59 development-validation files, and 170 held-out benchmark test files. The 170 files ending in `_test.pkl` correspond to sequences from the upstream PoseTrack21 **validation** split, not its hidden test labels. The windows and their evaluation settings are described in [protocols.json](protocols.json).

After authorized delivery and extraction of both archives, rebuild the video-file split with:

```sh
python3 tools/make_video_split.py \
  --hrnet /path/to/hrnet-w48/tracks \
  --vitpose /path/to/vitpose-h/tracks \
  --out splits.regenerated.csv
```

The script verifies that the two filename inventories agree. It does not deserialize the PKL contents. Keeping the filenames and loader order unchanged matters for paired synthetic-corruption masks.
