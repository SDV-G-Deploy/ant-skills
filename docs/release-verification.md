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
dist/SHA256SUMS
```

Each archive should contain only its skill folder, including:

```text
<skill>/SKILL.md
<skill>/agents/openai.yaml
```

`ant-plain-language` also includes its `references/` files.

After uploading a GitHub Release, download the assets and compare checksums:

```bash
mkdir -p /tmp/ant-release-check
gh release download v0.3.4 --repo SDV-G-Deploy/ant-skills --dir /tmp/ant-release-check --pattern '*.zip'
sha256sum dist/*.zip /tmp/ant-release-check/*.zip
```

The matching local and downloaded archive pairs should have identical hashes.
