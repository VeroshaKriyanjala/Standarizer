# More Rules Execution Log - KAUH

Mode: LIVE

## Rules Applied

- **Rule 1**: Replace CENTRAL-BASE-REPO with DEPLOYMENT-BASE-REPO in bases
- **Rule 2**: Do not change images section (preserved)
- **Rule 3**: Update patchesJson6902 Deployment target name
- **Rule 4**: Update metadata.name and container name in hpa.yaml, patch-hpa.yaml, patch-pod.yaml

## Changes (14 total)

- Rule 1: 3 changes
- Rule 3: 1 changes
- Rule 4: 10 changes

- `dms/document-management-middleware`: Rule 1: Updated base URL to DEPLOYMENT-BASE-REPO
- `reporting/csi-rf-file-uploader`: Rule 1: Updated base URL to DEPLOYMENT-BASE-REPO
- `rms/csi-rms-rules-java-sev`: Rule 1: Updated base URL to DEPLOYMENT-BASE-REPO
- `billing/csi-bm-approval-java-service`: Rule 3: Updated patchesJson6902 Deployment target name to 'csi-bm-approval-java-service'
- `billing/csi-bm-approval-ui`: Rule 4: patch-pod.yaml - updated name to 'csi-bm-approval-ui'
- `bloodbank/bb-bloodbankgui`: Rule 4: patch-hpa.yaml - updated name to 'bb-bloodbankgui'
- `empi/csi-empi-crs-integration`: Rule 4: hpa.yaml - updated name to 'csi-empi-crs-integration'
- `empi/csi-empi-hijridate-service`: Rule 4: hpa.yaml - updated name to 'csi-empi-hijridate-service'
- `empi/csi-empi-webui`: Rule 4: hpa.yaml - updated name to 'csi-empi-webui'
- `notification/csi-net-base-email`: Rule 4: hpa.yaml - updated name to 'csi-net-base-email'
- `notification/csi-net-base-sms`: Rule 4: hpa.yaml - updated name to 'csi-net-base-sms'
- `pharmacy/phr-pharmacygui`: Rule 4: hpa.yaml - updated name to 'phr-pharmacygui'
- `rms/csi-pms-adt-ui`: Rule 4: hpa.yaml - updated name to 'csi-pms-adt-ui'
- `rms/csi-rms-rules-java-sev`: Rule 4: hpa.yaml - updated name to 'csi-rms-rules-java-sev'
