# Alibaba Cloud Transformation Pack

Free supporting resources | MGCA-CT-AL-001 | Published by MGCA Ltd

Plan an evidence-led Alibaba Cloud transformation for one defined initiative.

## Start with the product you purchased

Unzip your purchased pack and open START_HERE.pdf or START_HERE.docx. This public folder supplements the pack with free guidance and small format-checking examples. It does not contain the paid workbook, detailed guide, assessment materials, product automation or release ZIP.

## First checks

1. Confirm the provider, account scope and intended review boundary.
2. Label estimated costs with their currency, period and evidence date.
3. Review identity, networking and operating assumptions before treating a plan as implementable.

## Free resources in this folder

- [Troubleshooting](troubleshooting.md): checks to make before raising a file issue.
- [Official references](references.md): links to authoritative background documentation.
- [Synthetic CSV](support-example.csv) and [synthetic JSON](support-example.json): tiny examples for the shared file-inspection helper. They are not inputs for the paid product tools.
- [Free helper instructions](../../tools/README.md): inspect CSV/JSON structure or verify a purchased file manifest.

## Try the free example

From the root of this resources repository, with Python 3.10 or later:

```text
python tools/inspect_file.py products/jti35-alibaba-cloud-transformation-pack/support-example.csv --required item --required status
python tools/inspect_file.py products/jti35-alibaba-cloud-transformation-pack/support-example.json
```

The helper reports file structure only. It does not score readiness, decide acceptance, compare architecture options or replace the purchased product.

## Product and support

[Product listing](https://payhip.com/b/Jti35) | [All free resources](../../README.md)

For a supplied-file problem, contact sales@mgca.co.uk with the product code, release version, application/runtime version and a fictional or redacted reproduction. Do not post customer files, order details, secrets or confidential diagrams in public issues. The licence and assessment scope supplied with your purchase remain authoritative.
