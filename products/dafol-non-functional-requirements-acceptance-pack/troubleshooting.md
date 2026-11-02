# Troubleshooting MGCA Non-functional Requirements Acceptance Pack

## Check the delivery first

Extract the full purchased ZIP and keep the original untouched. Confirm the product code and release in VERSION.txt. If FILE_MANIFEST.json is supplied, use the free [download verifier](../../tools/README.md) to check file integrity. An integrity pass confirms bytes, not technical suitability.

## Check the observation

### Check 1

Express a quality requirement with its unit, test condition and evidence source.

### Check 2

Keep an untested criterion distinct from a failed criterion.

### Check 3

Retain the environment and workload assumptions used for a measured result.

## A CSV or JSON example will not open

Try the synthetic support examples in this folder with tools/inspect_file.py. Check UTF-8 encoding, the delimiter, duplicate column names and JSON syntax. This helper does not validate the schema or business rules of a paid product input. Follow the documentation supplied with that product for its exact schema.

## A workbook result looks unexpected

Use a disposable copy, reproduce the supplied fictional example in your intended spreadsheet application and record the input and result. Do not replace formula cells with typed values to hide an error. The product validation record identifies which application checks were performed.

## Raise a useful support request

Give the product code, release, affected filename, application/runtime version, the exact step, expected behaviour and a minimal fictional reproduction. Send order information privately to sales@mgca.co.uk. A public support discussion must not include paid product files or customer data.
