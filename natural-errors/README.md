# Natural Detection Errors

This protocol evaluates repair on selected errors in detector tracks with no added synthetic corruption. The paper reports this comparison separately from the controlled corruption results.

Use the same held-out video definition and detector-specific normalization as in the controlled benchmark. Set the test corruption ratio to zero. The loader can still handle native missing detections and padding; zero additional corruption does not bypass preprocessing.

The region rules use annotation-assisted priors to identify eligible errors. A frame–joint location enters the local scoring region when the repair score is at least 0.5 and the GT location is valid. The paper's protocol excludes non-repairable events such as shot changes, person absence and whole-body collapse from the targets. This benchmark measures local repair given supplied region information. It does not evaluate detector-only region discovery.

Report global errors on valid observations and local measures on the designated repair region. Use the corresponding checkpoint and inference settings of the released experiment version. A condition made using the ground truth for this benchmark should not be described as a detector-only input.
