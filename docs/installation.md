# Installation

Mathicon supports Linux x86_64 and Python 3.9–3.13.

## Install from PyPI

```bash
pip install mathicon
```

Verify:

```bash
python -c "from mathicon import point_x_color; print(point_x_color)"
```

## Optional extras

```bash
# Development (pytest, build tools)
pip install mathicon[dev]

# Neural-network visualization icons (torch, aggdraw)
pip install mathicon[nn]
```

## Editable install (from source)

```bash
git clone https://github.com/xuanxinjushi/mathicon.git
cd mathicon
pip install -e ".[dev]"
```

## Command-line tools

After install, two scripts are available:

```bash
mathicon-preview-icons --list
mathicon-icon-gui
```

See [CLI tools](cli-tools.md).

## Dependencies

Installed automatically:

- matplotlib >= 3.0.0
- numpy >= 1.18.0
- Pillow >= 9.0.0
