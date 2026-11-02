# Earth Observation Change-detection Starter Kit

Free supporting resources | SSE-CD-001 | Published by MGCA Ltd

Learn a reproducible change-detection workflow with synthetic data.

## Start with the product you purchased

Unzip your purchased pack and open START_HERE.pdf or START_HERE.docx. This public folder supplements the pack with free guidance and small format-checking examples. It does not contain the paid workbook, detailed guide, assessment materials, product automation or release ZIP.

## First checks

1. Check that before and after samples describe aligned locations and comparable inputs.
2. Retain band definitions, scaling and invalid-data rules with the sample.
3. An observed index change is not automatically a verified real-world land-cover change.

## Free resources in this folder

- [Troubleshooting](troubleshooting.md): checks to make before raising a file issue.
- [Official references](references.md): links to authoritative background documentation.
- [Synthetic CSV](support-example.csv) and [synthetic JSON](support-example.json): tiny examples for the shared file-inspection helper. They are not inputs for the paid product tools.
- [Free helper instructions](../../tools/README.md): inspect CSV/JSON structure or verify a purchased file manifest.

## Try the free example

From the root of this resources repository, with Python 3.10 or later:

```text
python tools/inspect_file.py products/xjw2y-earth-observation-change-detection-starter-kit/support-example.csv --required item --required status
python tools/inspect_file.py products/xjw2y-earth-observation-change-detection-starter-kit/support-example.json
```

The helper reports file structure only. It does not score readiness, decide acceptance, compare architecture options or replace the purchased product.

## Product and support

[Product listing](https://payhip.com/b/XJw2Y) | [All free resources](../../README.md)

For a supplied-file problem, contact sales@mgca.co.uk with the product code, release version, application/runtime version and a fictional or redacted reproduction. Do not post customer files, order details, secrets or confidential diagrams in public issues. The licence and assessment scope supplied with your purchase remain authoritative.
