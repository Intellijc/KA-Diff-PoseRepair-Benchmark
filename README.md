# KA-Diff: PoseTrack21-derived pose-repair benchmarks

This repository documents the two evaluation protocols used in the KA-Diff study. Both protocols use detector tracks derived from PoseTrack21. They are not separate collections of source video.

| Protocol | Evaluation target |
|---|---|
| [Controlled Local Corruption](controlled-corruption/README.md) | Repair of known synthetic corruption with paired test seeds |
| [Natural Detection Errors](natural-errors/README.md) | Repair of selected detector failures with annotation-assisted region information |

The protocol settings are in [protocols.json](protocols.json). This documentation release does not include detector-track files, source images, or source annotations. Obtain PoseTrack21 through the [official access process](https://github.com/anDoer/PoseTrack21#how-to-get-the-dataset). Please cite the [upstream PoseTrack papers](https://github.com/anDoer/PoseTrack21#citation) and the accompanying KA-Diff manuscript if you use these protocols. See [CITATION.cff](CITATION.cff) for the benchmark citation information.
