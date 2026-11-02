# Free support helpers

These original, general-purpose helpers are free under the repository MIT licence. They use the Python standard library, make no network calls and do not modify product inputs. Python 3.10 or later is required. PowerShell discovery is optional.

## Inspect file structure

```text
python tools/inspect_file.py products/avktj-robot-mission-test-and-acceptance-pack/support-example.csv --required item --required status
python tools/inspect_file.py products/avktj-robot-mission-test-and-acceptance-pack/support-example.json
```

CSV inspection checks header names and row widths; JSON inspection checks syntax and optional top-level keys. A successful check does not prove that evidence is complete, calculations are correct or a paid input schema is satisfied. The default inspection limit is 10 MB.

## Check a purchased download

```text
python tools/verify_download.py "path/to/extracted/product/FILE_MANIFEST.json"
```

The verifier checks listed file hashes and byte sizes. It rejects paths outside the extracted product folder. It does not evaluate technical content or validate a live environment. An older pack with another manifest format may need its own supplied instructions.

## Optional prerequisite discovery

```powershell
./tools/Check-Environment.ps1
```

This reports local PowerShell and available Python command paths. It does not install software, authenticate to providers or collect cloud inventory.
