# Release verification

Release archives are generated from `skills/*`:

```bash
python3 tools/package_skills.py
python3 tools/check_release_archives.py
```

The packaging command writes:

```text
dist/ant-plain-language.zip
dist/ant-compact.zip
dist/ant-low-words.zip
dist/ant-product-map.zip
dist/SHA256SUMS
```

Each archive should contain only its skill folder, including:

```text
<skill>/SKILL.md
<skill>/agents/openai.yaml
```

`ant-plain-language` also includes its `references/` files.
`ant-product-map` also includes its `references/` files.

After uploading a GitHub Release, download the assets and compare checksums:

```bash
TAG="$(git describe --tags --abbrev=0)"
mkdir -p /tmp/ant-release-check
gh release download "$TAG" --repo SDV-G-Deploy/ant-skills --dir /tmp/ant-release-check --pattern '*.zip'
gh release download "$TAG" --repo SDV-G-Deploy/ant-skills --dir /tmp/ant-release-check --pattern 'SHA256SUMS'
sha256sum dist/*.zip /tmp/ant-release-check/*.zip
sha256sum -c /tmp/ant-release-check/SHA256SUMS --ignore-missing
```

The matching local and downloaded archive pairs should have identical hashes, and the downloaded `SHA256SUMS` check should pass.
