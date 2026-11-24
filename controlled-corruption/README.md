# Controlled Local Corruption

This protocol tests reconstruction at a known set of synthetically corrupted frame–joint locations. The paper uses it in the main comparison and in the detector-backbone comparison. The module ablation uses the same controlled setup.

1. Select one detector-track variant and load its matching normalization statistics.
2. Use the benchmark test split and the loader's 32-frame windows. Run each paired test seed listed in [protocols.json](../protocols.json).
3. The loader samples joint dropout, limb dropout, or confidence attenuation with probabilities 0.4, 0.4, and 0.2. The main comparison uses a spatial sampling probability of 0.3 and sampled interval lengths of 5–15 frames. These settings define the random process; 0.3 is not a guarantee that 30% of all locations are masked.
4. Keep the sampled synthetic mask distinct from natural failures and padding. For repair-region scoring, intersect the synthetic mask with the valid GT mask. The conditional model also receives the synthetic region as a repair target. Use the same corrupted observations and scoring mask for every refiner within a detector group.

Fixed masks depend on the seed, track identifier and loader window index. Keep the dataset filenames and loader order unchanged if reproducing them. The loader generates them on demand; this protocol does not require a second archive of duplicated videos or tracks. Duration/ratio sweeps use different settings and should be reported separately.
