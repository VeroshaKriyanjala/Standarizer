# More Rules Execution Log - Alibaba

Mode: LIVE

## Rules Applied

- **Rule 1**: Replace CENTRAL-BASE-REPO with DEPLOYMENT-BASE-REPO in bases
- **Rule 2**: Do not change images section (preserved)
- **Rule 3**: Update patchesJson6902 Deployment target name
- **Rule 4**: Update metadata.name and container name in hpa.yaml, patch-hpa.yaml, patch-pod.yaml

## Changes (20 total)

- Rule 1: 12 changes
- Rule 3: 1 changes
- Rule 4: 7 changes

- `bloodbank/csi-blood-transfusion-java`: Rule 1: Updated base URL to DEPLOYMENT-BASE-REPO
- `bloodbank/csi-java-bb-service`: Rule 1: Updated base URL to DEPLOYMENT-BASE-REPO
- `dms/document-management-middleware`: Rule 1: Updated base URL to DEPLOYMENT-BASE-REPO
- `empi/csi-empi-api`: Rule 1: Updated base URL to DEPLOYMENT-BASE-REPO
- `empi/csi-empi-crs-integration`: Rule 1: Updated base URL to DEPLOYMENT-BASE-REPO
- `empi/csi-empi-hijridate-service`: Rule 1: Updated base URL to DEPLOYMENT-BASE-REPO
- `empi/csi-empi-patient-registration-srv`: Rule 1: Updated base URL to DEPLOYMENT-BASE-REPO
- `empi/csi-empi-patient-service-read`: Rule 1: Updated base URL to DEPLOYMENT-BASE-REPO
- `empi/csi-empi-webui`: Rule 1: Updated base URL to DEPLOYMENT-BASE-REPO
- `empi/csi-empi-wrapper`: Rule 1: Updated base URL to DEPLOYMENT-BASE-REPO
- `reporting/csi-streaming-etl`: Rule 1: Updated base URL to DEPLOYMENT-BASE-REPO
- `rms/csi-rms-rules-java-sev`: Rule 1: Updated base URL to DEPLOYMENT-BASE-REPO
- `ehr/csi-workflow-automation-service-java-sev`: Rule 3: Updated patchesJson6902 Deployment target name to 'csi-workflow-automation-service-java-sev'
- `billing/csi-bm-approval-ui`: Rule 4: patch-pod.yaml - updated name to 'csi-bm-approval-ui'
- `bloodbank/csi-blood-transfusion-java`: Rule 4: patch-hpa.yaml - updated name to 'csi-blood-transfusion-java'
- `empi/csi-empi-crs-integration`: Rule 4: hpa.yaml - updated name to 'csi-empi-crs-integration'
- `empi/csi-empi-hijridate-service`: Rule 4: hpa.yaml - updated name to 'csi-empi-hijridate-service'
- `empi/csi-empi-patient-registration-srv`: Rule 4: patch-hpa.yaml - updated name to 'csi-empi-patient-registration-srv'
- `empi/csi-empi-webui`: Rule 4: hpa.yaml - updated name to 'csi-empi-webui'
- `rms/csi-rms-rules-java-sev`: Rule 4: hpa.yaml - updated name to 'csi-rms-rules-java-sev'
