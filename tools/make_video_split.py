"""Reproduce KA-Diff's video-file split without loading pose data."""

import argparse
import csv
import hashlib
from pathlib import Path


def collect(root):
    if not root.is_dir():
        raise ValueError(f'Directory not found: {root}')
    all_names = sorted(p.name for p in root.glob('*.pkl') if p.is_file())
    train = [n for n in all_names if n.endswith('_train.pkl')]
    test = [n for n in all_names if n.endswith('_test.pkl')]
    if not train or not test or len(train) + len(test) != len(all_names):
        raise ValueError(f'Expected only train and test PKL files in {root}')
    return train, test


def make_rows(train, test):
    ranked = sorted(train, key=lambda name: hashlib.sha256(
        f'kadiff-val-split-v1:{name}'.encode()).hexdigest())
    val_names = set(ranked[:max(1, round(0.10 * len(ranked)))])
    splits = {
        'train': [name for name in train if name not in val_names],
        'validation': [name for name in train if name in val_names],
        'test': test,
    }
    seen = set()
    for label, names in splits.items():
        upstream = 'val' if label == 'test' else 'train'
        for i, name in enumerate(names):
            seq_id = Path(name).stem.rsplit('_', 1)[0]
            if seq_id in seen:
                raise ValueError(f'Duplicate sequence ID: {seq_id}')
            seen.add(seq_id)
            # The upstream val directory retains the `_test` filename suffix.
            yield name, upstream, f'{Path(name).stem}.json', label, i


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--hrnet', type=Path, required=True)
    parser.add_argument('--vitpose', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    train, test = collect(args.hrnet)
    if (train, test) != collect(args.vitpose):
        parser.error('The two variant directories have different filename sets.')
    rows = list(make_rows(train, test))
    with args.out.open('x', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(['track_file', 'posetrack21_split', 'posetrack21_annotation',
                         'benchmark_split', 'split_index'])
        writer.writerows(rows)
    print(f'Wrote {len(rows)} filename-only records to {args.out}.')


if __name__ == '__main__':
    main()
