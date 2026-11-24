# KA-Diff: PoseTrack21-derived pose-repair benchmarks

This repository documents two evaluation protocols for local repair of detected 2D human pose sequences. The protocols share PoseTrack21-derived detector tracks; they are not separate collections of source video.

| Protocol | Evaluation target |
|---|---|
| [Controlled Local Corruption](controlled-corruption/README.md) | Repair of known synthetic corruption with paired test seeds |
| [Natural Detection Errors](natural-errors/README.md) | Repair of selected detector failures with annotation-assisted region information |

The settings are in [protocols.json](protocols.json). The [data format and split guide](DATA_FORMAT.md) explains how to use the track data after receiving access. The split tool reproduces the video-file assignment on local track files.

## Data access

The protocols are public. The derived HRNet-W48 and ViTPose-H track archives are distributed by request, subject to approval and the PoseTrack21 data access terms. See [how to request access](DATA_ACCESS.md). No track archives, source frames, or upstream annotation packages are publicly downloadable from this repository. Obtain source frames through the [official PoseTrack21 access process](https://github.com/anDoer/PoseTrack21#how-to-get-the-dataset).

Please cite the accompanying KA-Diff manuscript and both PoseTrack papers listed in the [upstream citation instructions](https://github.com/anDoer/PoseTrack21#citation). Benchmark citation information is in [CITATION.cff](CITATION.cff).
