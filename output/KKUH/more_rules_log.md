# More Rules Execution Log - KKUH

Mode: LIVE

## Rules Applied

- **Rule 1**: Replace CENTRAL-BASE-REPO with DEPLOYMENT-BASE-REPO in bases
- **Rule 2**: Do not change images section (preserved)
- **Rule 3**: Update patchesJson6902 Deployment target name
- **Rule 4**: Update metadata.name and container name in hpa.yaml, patch-hpa.yaml, patch-pod.yaml

## Changes (58 total)

- Rule 1: 5 changes
- Rule 3: 2 changes
- Rule 4: 51 changes

- `billing/csi-bm-inte-bridge-java-service`: Rule 1: Updated base URL to DEPLOYMENT-BASE-REPO
- `billing/csi-bm-invoice-java-service`: Rule 1: Updated base URL to DEPLOYMENT-BASE-REPO
- `integration/vida-data-gateway`: Rule 1: Updated base URL to DEPLOYMENT-BASE-REPO
- `pharmacy/phr-ui-v2`: Rule 1: Updated base URL to DEPLOYMENT-BASE-REPO
- `rms/csi-mlm-ui`: Rule 1: Updated base URL to DEPLOYMENT-BASE-REPO
- `notification/csi-vidaplus-external`: Rule 3: Updated patchesJson6902 Deployment target name to 'csi-vidaplus-external'
- `pharmacy/phr-ui-v2`: Rule 3: Updated patchesJson6902 Deployment target name to 'phr-ui-v2'
- `base/base-utility-service-java-sev`: Rule 4: patch-pod.yaml - updated name to 'base-utility-service-java-sev'
- `base/csi-personalization-service-java-sev`: Rule 4: patch-pod.yaml - updated name to 'csi-personalization-service-java-sev'
- `base/csi-uif-admin-ui`: Rule 4: patch-pod.yaml - updated name to 'csi-uif-admin-ui'
- `billing/csi-bm-approval-ui`: Rule 4: patch-pod.yaml - updated name to 'csi-bm-approval-ui'
- `billing/csi-bm-billing-ui`: Rule 4: hpa.yaml - updated name to 'csi-bm-billing-ui'
- `billing/csi-bm-billing-ui`: Rule 4: patch-pod.yaml - updated name to 'csi-bm-billing-ui'
- `bloodbank/bb-bloodbankgui`: Rule 4: patch-pod.yaml - updated name to 'bb-bloodbankgui'
- `bloodbank/bb-donation-srv`: Rule 4: patch-pod.yaml - updated name to 'bb-donation-srv'
- `bloodbank/csi-blood-transfusion-java`: Rule 4: patch-pod.yaml - updated name to 'csi-blood-transfusion-java'
- `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev`: Rule 4: patch-pod.yaml - updated name to 'csi-ehr-com-ip-dashboardwidget-dotnet-sev'
- `ehr/csi-ehr-com-ip-discharge-dotnet-sev`: Rule 4: patch-pod.yaml - updated name to 'csi-ehr-com-ip-discharge-dotnet-sev'
- `ehr/csi-ehr-com-opd-master-dotnet-sev`: Rule 4: patch-pod.yaml - updated name to 'csi-ehr-com-opd-master-dotnet-sev'
- `ehr/csi-ehr-com-opd-patient-dotnet-sev`: Rule 4: patch-pod.yaml - updated name to 'csi-ehr-com-opd-patient-dotnet-sev'
- `ehr/csi-ehr-common-java-sev`: Rule 4: patch-pod.yaml - updated name to 'csi-ehr-common-java-sev'
- `ehr/csi-ehr-common-scheduler-java-sev`: Rule 4: patch-pod.yaml - updated name to 'csi-ehr-common-scheduler-java-sev'
- `ehr/csi-ehr-config-java-sev`: Rule 4: patch-pod.yaml - updated name to 'csi-ehr-config-java-sev'
- `ehr/csi-ehr-ip-java-sev`: Rule 4: patch-pod.yaml - updated name to 'csi-ehr-ip-java-sev'
- `ehr/csi-ehr-ldr-java-sev`: Rule 4: patch-pod.yaml - updated name to 'csi-ehr-ldr-java-sev'
- `ehr/csi-ehr-listener-java-sev`: Rule 4: patch-pod.yaml - updated name to 'csi-ehr-listener-java-sev'
- `ehr/csi-ehr-opd-java-sev`: Rule 4: patch-pod.yaml - updated name to 'csi-ehr-opd-java-sev'
- `ehr/csi-ehr-opd-patient-pomr-java-sev`: Rule 4: patch-pod.yaml - updated name to 'csi-ehr-opd-patient-pomr-java-sev'
- `ehr/csi-ehr-or-book-java-sev`: Rule 4: patch-pod.yaml - updated name to 'csi-ehr-or-book-java-sev'
- `ehr/csi-ehr-or-booking-java-sev`: Rule 4: patch-pod.yaml - updated name to 'csi-ehr-or-booking-java-sev'
- `ehr/csi-ehr-specialized-clinic-java-sev`: Rule 4: patch-pod.yaml - updated name to 'csi-ehr-specialized-clinic-java-sev'
- `ehr/csi-ehr-template-java-sev`: Rule 4: patch-pod.yaml - updated name to 'csi-ehr-template-java-sev'
- `ehr/csi-workflow-automation-service-java-sev`: Rule 4: patch-pod.yaml - updated name to 'csi-workflow-automation-service-java-sev'
- `ehr/ehr-ic-ui`: Rule 4: patch-pod.yaml - updated name to 'ehr-ic-ui'
- `empi/csi-empi-crs-integration`: Rule 4: patch-pod.yaml - updated name to 'csi-empi-crs-integration'
- `empi/csi-empi-hijridate-service`: Rule 4: patch-pod.yaml - updated name to 'csi-empi-hijridate-service'
- `empi/csi-empi-patient-registration-srv`: Rule 4: patch-pod.yaml - updated name to 'csi-empi-patient-registration-srv'
- `empi/csi-empi-patient-service-read`: Rule 4: patch-pod.yaml - updated name to 'csi-empi-patient-service-read'
- `empi/csi-empi-webui`: Rule 4: patch-pod.yaml - updated name to 'csi-empi-webui'
- `er/csi-ehr-er-functions-dotnet-sev`: Rule 4: patch-pod.yaml - updated name to 'csi-ehr-er-functions-dotnet-sev'
- `lab/lab-labgui`: Rule 4: patch-pod.yaml - updated name to 'lab-labgui'
- `lab/lab-labmgt-srv`: Rule 4: patch-pod.yaml - updated name to 'lab-labmgt-srv'
- `lab/lab-scheduled`: Rule 4: patch-pod.yaml - updated name to 'lab-scheduled'
- `lab/lab-vidaptor-integration`: Rule 4: patch-pod.yaml - updated name to 'lab-vidaptor-integration'
- `notification/csi-net-base-email`: Rule 4: patch-hpa.yaml - updated name to 'csi-net-base-email'
- `notification/csi-net-base-email`: Rule 4: patch-pod.yaml - updated name to 'csi-net-base-email'
- `notification/csi-net-base-message-templates`: Rule 4: patch-pod.yaml - updated name to 'csi-net-base-message-templates'
- `notification/csi-net-base-notifications-query`: Rule 4: patch-pod.yaml - updated name to 'csi-net-base-notifications-query'
- `notification/csi-net-base-sms`: Rule 4: patch-pod.yaml - updated name to 'csi-net-base-sms'
- `pharmacy/phr-pharmacygui`: Rule 4: patch-pod.yaml - updated name to 'phr-pharmacygui'
- `pharmacy/phr-ui-v2`: Rule 4: hpa.yaml - updated name to 'phr-ui-v2'
- `renal/ren-hemodialysis-srv`: Rule 4: patch-pod.yaml - updated name to 'ren-hemodialysis-srv'
- `reporting/csi-rf-reportingservice`: Rule 4: patch-pod.yaml - updated name to 'csi-rf-reportingservice'
- `reporting/report-studio-ui`: Rule 4: patch-pod.yaml - updated name to 'report-studio-ui'
- `rms/csi-ds-dental-core-java-sev`: Rule 4: patch-pod.yaml - updated name to 'csi-ds-dental-core-java-sev'
- `rms/csi-pms-adt-ui`: Rule 4: patch-pod.yaml - updated name to 'csi-pms-adt-ui'
- `rms/csi-rms-reservation-java-sev`: Rule 4: patch-pod.yaml - updated name to 'csi-rms-reservation-java-sev'
- `rms/csi-rms-resource-registry-java-sev`: Rule 4: patch-pod.yaml - updated name to 'csi-rms-resource-registry-java-sev'
