# YAML Validation Report

## Summary

| Repo | Files Scanned | Errors | Warnings | Info |
|------|--------------|--------|----------|------|
| KKUH | 254 | 4 | 9 | 108 |
| Alibaba | 222 | 0 | 3 | 193 |
| WAVE1 | 244 | 8 | 43 | 234 |
| CS | 240 | 0 | 45 | 203 |
| KAUH | 226 | 6 | 3 | 162 |
| S2 | 224 | 0 | 2 | 130 |
| S3 | 224 | 6 | 6 | 174 |
| HMG | 263 | 1 | 6 | 159 |
| **Total** | **1897** | **25** | **117** | **1363** |

Files with issues: 999

## KKUH

### `PROD/base/base-utility-service-java-sev/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/base/medispan/overlays/PROD/kustomization.yaml`

- [i] [INFO] (line 19) Unusual target kind 'Namespace'
- [i] [INFO] (line 27) Unusual target kind 'Namespace'

### `PROD/base/webserver/kustomization.yaml`

- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/base/webserver

### `PROD/billing/csi-bm-approval-java-service/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/billing/csi-bm-approval-ui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/billing/csi-bm-billing-java-service/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/billing/csi-bm-billing-ui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/billing/csi-bm-inte-bridge-java-service/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/billing/csi-bm-invoice-java-service/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/billing/csi-bm-invoice-ui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/billing/csi-bm-promotion-java-service/kustomization.yaml`

- [i] [INFO] (line 20) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/bloodbank/bb-bloodbankgui-mgt/kustomization.yaml`

- [i] [INFO] (line 19) Unusual target kind 'Namespace'
- [i] [INFO] (line 27) Unusual target kind 'Namespace'

### `PROD/bloodbank/bb-bloodbankgui/kustomization.yaml`

- [i] [INFO] (line 25) Unusual target kind 'Namespace'
- [i] [INFO] (line 33) Unusual target kind 'Namespace'

### `PROD/bloodbank/csi-blood-transfusion-java/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/bloodbank/csi-java-bb-service/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/cssd/csi-cssd-java-sev/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 3 line(s) have trailing whitespace

### `PROD/cssd/csi-cssd-java-sev/overlays/kustomization.yaml`

- [x] [ERROR] Duplicate top-level key 'namespace' found 2 times at lines 18, 29
- [x] [ERROR] Duplicate top-level key 'patchesJSON6902' found 2 times at lines 19, 30
- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] (line 30) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] (line 22) Unusual target kind 'Namespace'
- [i] [INFO] (line 33) Unusual target kind 'Namespace'
- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/cssd/csi-cssd-node-sev/overlays/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/cssd/csi-cssd-ui/kustomization.yaml`

- [i] [INFO] (line 24) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `PROD/dms/csi-document-management-service/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `PROD/dms/document-management-engine/kustomization.yaml`

- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/sasmitha.athige/BASE/src/branch/main/dms/dmsstorageengine

### `PROD/ehr/csi-ehr-com-ip-discharge-dotnet-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-common-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-config-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-ic-bundle-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-ic-dashboard-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-ip-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-ldr-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-opd-patient-pomr-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-opd-ui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-or-anesthesia-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-specialized-clinic-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-template-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-workflow-automation-service-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/er/csi-ehr-er-functions-dotnet-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/integration/csi-ie-general/kustomization.yaml`

- [i] [INFO] 3 line(s) have trailing whitespace

### `PROD/lab/lab-labgui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/lab/lab-labmgt-srv/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/pharmacy/csi-java-ehr-ip-doctor-prescription/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/pharmacy/csi-phr-base/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/renal/ren-hemodialysis-srv/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/rms/csi-ds-dental-core-java-sev/kustomization.yaml`

- [i] [INFO] (line 21) Unusual target kind 'Namespace'

### `PROD/rms/csi-mlm-ui/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `PROD/rms/csi-rms-masterdata-java-sev/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/rms/csi-rms-morgue-java-service/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/rms/csi-rms-resource-registry-java-sev/kustomization.yaml`

- [i] [INFO] 3 line(s) have trailing whitespace

### `PROD/security/csi-iam-service/kustomization.yaml`

- [i] [INFO] (line 22) Unusual target kind 'Namespace'
- [i] [INFO] (line 27) Unusual target kind 'Namespace'

### `PROD/security/csi-master-data-management-service/kustomization.yaml`

- [i] [INFO] (line 22) Unusual target kind 'Namespace'
- [i] [INFO] (line 27) Unusual target kind 'Namespace'

### `PROD/security/csi-roles-permissions-management-service/kustomization.yaml`

- [i] [INFO] (line 22) Unusual target kind 'Namespace'
- [i] [INFO] (line 27) Unusual target kind 'Namespace'

### `PROD/security/csi-ui-registry-service/kustomization.yaml`

- [i] [INFO] (line 22) Unusual target kind 'Namespace'
- [i] [INFO] (line 27) Unusual target kind 'Namespace'

### `PROD/security/securitycentralauth/kustomization.yaml`

- [i] [INFO] (line 19) Unusual target kind 'Namespace'
- [i] [INFO] (line 24) Unusual target kind 'Namespace'

### `PROD/security/securityiamcache/kustomization.yaml`

- [i] [INFO] (line 22) Unusual target kind 'Namespace'
- [i] [INFO] (line 27) Unusual target kind 'Namespace'

### `UAT/base/csi-uif-settings/kustomization.yaml`

- [i] [INFO] (line 25) Unusual target kind 'Namespace'
- [i] [INFO] (line 33) Unusual target kind 'Namespace'
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/base/facadpatientsnapshot/kustomization.yaml`

- [i] [INFO] (line 22) Unusual target kind 'Namespace'
- [i] [INFO] (line 30) Unusual target kind 'Namespace'
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/base/facadpatientsnapshot

### `UAT/base/medispan/overlays/PROD/kustomization.yaml`

- [!] [WARNING] (line 15) Namespace 'vida-prod' doesn't contain 'uat' but file is in UAT
- [i] [INFO] (line 19) Unusual target kind 'Namespace'
- [i] [INFO] (line 27) Unusual target kind 'Namespace'

### `UAT/base/webserver/kustomization.yaml`

- [i] [INFO] (line 22) Unusual target kind 'Namespace'
- [i] [INFO] (line 30) Unusual target kind 'Namespace'
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/base/webserver

### `UAT/billing/csi-bm-promotion-java-service/kustomization.yaml`

- [i] [INFO] (line 24) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/bloodbank/bb-donation-srv/kustomization.yaml`

- [i] [INFO] 3 line(s) have trailing whitespace

### `UAT/cssd/csi-cssd-java-sev/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/cssd/csi-cssd-java-sev/overlays/kustomization.yaml`

- [x] [ERROR] Duplicate top-level key 'namespace' found 2 times at lines 18, 29
- [x] [ERROR] Duplicate top-level key 'patchesJSON6902' found 2 times at lines 19, 30
- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] (line 30) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [!] [WARNING] (line 18) Namespace 'csi-perf' doesn't contain 'uat' but file is in UAT
- [i] [INFO] (line 22) Unusual target kind 'Namespace'
- [i] [INFO] (line 33) Unusual target kind 'Namespace'
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/cssd/csi-cssd-node-sev/overlays/kustomization.yaml`

- [!] [WARNING] (line 18) Namespace 'csi-perf' doesn't contain 'uat' but file is in UAT

### `UAT/cssd/csi-cssd-ui/kustomization.yaml`

- [i] [INFO] (line 24) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/dms/csi-document-management-service/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/dms/dmsstorageengine/kustomization.yaml`

- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/sasmitha.athige/BASE/src/branch/main/dms/dmsstorageengine

### `UAT/ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-com-opd-patient-dotnet-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-common-scheduler-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-ic-bundle-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-initialassessment-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-ldr-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-opd-java-sev/kustomization.yaml`

- [i] [INFO] 3 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-template-java-sev/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/empi/csi-empi-api/kustomization.yaml`

- [i] [INFO] 3 line(s) have trailing whitespace

### `UAT/empi/csi-empi-patient-registration-srv/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/empi/csi-empi-patient-service-read/kustomization.yaml`

- [i] [INFO] (line 24) Unusual target kind 'Namespace'
- [i] [INFO] (line 32) Unusual target kind 'Namespace'

### `UAT/er/csi-ehr-er-functions-dotnet-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/integration/vida-data-gateway/kustomization.yaml`

- [i] [INFO] (line 18) Unusual target kind 'Namespace'
- [i] [INFO] (line 26) Unusual target kind 'Namespace'

### `UAT/lab/lab-labgui/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/lab/lab-labmgt-srv/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/notification/csi-vidaplus-external/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/otp-service/kustomization.yaml`

- [!] [WARNING] (line 11) Namespace 'vida-prod' doesn't contain 'uat' but file is in UAT

### `UAT/pharmacy/phr-pharmacygui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/rms/csi-morgue-ui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/rms/csi-rms-masterdata-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/rms/csi-rms-morgue-java-service/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

## Alibaba

### `PROD/base/base-utility-service-java-sev/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/base/csi-personalization-service-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/base/csi-uif-admin-ui/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `PROD/base/csi-uif-settings/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/billing/csi-bm-approval-java-service/kustomization.yaml`

- [!] [WARNING] Inconsistent patchesJson6902 casing: 'patchesJson6902' at line(s) 23, 'patchesJSON6902' at line(s) 24
- [i] [INFO] (line 24) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/billing/csi-bm-approval-ui/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/billing/csi-bm-billing-java-service/kustomization.yaml`

- [i] [INFO] 3 line(s) have trailing whitespace

### `PROD/billing/csi-bm-billing-ui/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 4 line(s) have trailing whitespace

### `PROD/billing/csi-bm-inte-bridge-java-service/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/billing/csi-bm-invoice-java-service/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/billing/csi-bm-invoice-ui/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/billing/csi-bm-promotion-java-service/kustomization.yaml`

- [i] [INFO] (line 24) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/bloodbank/bb-bloodbankgui/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 3 line(s) have trailing whitespace

### `PROD/bloodbank/bb-donation-srv/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/bloodbank/csi-java-bb-service/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/bloodbank/csi-net-bb-mgt-srv/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/dms/csi-document-management-service/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/dms/document-management-engine/kustomization.yaml`

- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/sasmitha.athige/BASE/src/branch/main/dms/dmsstorageengine

### `PROD/ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev/kustomization.yaml`

- [i] [INFO] (line 18) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-com-opd-master-dotnet-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-com-opd-patient-dotnet-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-common-java-sev/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-common-scheduler-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-config-java-sev/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-ic-bundle-java-sev/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-ic-dashboard-java-sev/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `PROD/ehr/csi-ehr-initialassessment-java-sev/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-ip-java-sev/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-ldr-java-sev/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-listener-java-sev/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-opd-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-opd-patient-pomr-java-sev/kustomization.yaml`

- [i] [INFO] (line 18) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 3 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-opd-ui/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `PROD/ehr/csi-ehr-or-book-java-sev/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-or-booking-java-sev/kustomization.yaml`

- [i] [INFO] (line 18) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-specialized-clinic-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-template-java-sev/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-workflow-automation-service-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/ehr-ic-ui/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 3 line(s) have trailing whitespace

### `PROD/empi/csi-empi-api/kustomization.yaml`

- [i] [INFO] (line 20) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 3 line(s) have trailing whitespace

### `PROD/empi/csi-empi-webui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/empi/csi-empi-wrapper/kustomization.yaml`

- [i] [INFO] (line 16) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/er/csi-ehr-er-functions-dotnet-sev/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/er/csi-ehr-er-ui/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `PROD/integration/csi-ie-general/kustomization.yaml`

- [i] [INFO] 4 line(s) have trailing whitespace

### `PROD/integration/csi-ie-mobile/kustomization.yaml`

- [i] [INFO] 3 line(s) have trailing whitespace

### `PROD/lab/lab-labgui/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/lab/lab-labmgt-srv/kustomization.yaml`

- [i] [INFO] (line 24) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/lab/lab-scheduled/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/lab/lab-vidaptor-integration/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/pharmacy/csi-java-ehr-ip-doctor-prescription/kustomization.yaml`

- [i] [INFO] (line 20) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 4 line(s) have trailing whitespace

### `PROD/pharmacy/csi-phr-base/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/pharmacy/csi-phr-cron/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/pharmacy/phr-pharmacygui/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/renal/ren-hemodialysis-srv/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/reporting/csi-rf-file-uploader/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/reporting/csi-rf-reportingservice/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/reporting/csi-streaming-etl/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/rms/csi-morgue-ui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/rms/csi-pms-adt-request-java-sev/kustomization.yaml`

- [i] [INFO] 3 line(s) have trailing whitespace

### `PROD/rms/csi-rms-masterdata-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/rms/csi-rms-morgue-java-service/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/rms/csi-rms-reservation-java-sev/kustomization.yaml`

- [i] [INFO] 3 line(s) have trailing whitespace

### `PROD/rms/csi-rms-resource-registry-java-sev/kustomization.yaml`

- [i] [INFO] 4 line(s) have trailing whitespace

### `PROD/rms/csi-rms-ui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/rms/csi-setup-ui/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/support-portal/support-portal/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/base/base-utility-service-java-sev/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 3 line(s) have trailing whitespace

### `UAT/base/csi-uif-admin-ui/kustomization.yaml`

- [i] [INFO] (line 24) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/base/csi-uif-settings/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 3 line(s) have trailing whitespace

### `UAT/billing/csi-bm-approval-java-service/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/billing/csi-bm-approval-ui/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/billing/csi-bm-billing-java-service/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 3 line(s) have trailing whitespace

### `UAT/billing/csi-bm-billing-ui/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 3 line(s) have trailing whitespace

### `UAT/billing/csi-bm-inte-bridge-java-service/kustomization.yaml`

- [i] [INFO] (line 24) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/billing/csi-bm-invoice-java-service/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/billing/csi-bm-invoice-ui/kustomization.yaml`

- [i] [INFO] (line 24) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/billing/csi-bm-promotion-java-service/kustomization.yaml`

- [i] [INFO] (line 24) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/bloodbank/bb-bloodbankgui/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/bloodbank/bb-donation-srv/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/bloodbank/csi-java-bb-service/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev/kustomization.yaml`

- [i] [INFO] (line 24) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-com-opd-master-dotnet-sev/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-com-opd-patient-dotnet-sev/kustomization.yaml`

- [i] [INFO] (line 24) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/ehr/csi-ehr-common-java-sev/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-common-scheduler-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-config-java-sev/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-ic-bundle-java-sev/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/ehr/csi-ehr-ic-dashboard-java-sev/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/ehr/csi-ehr-initialassessment-java-sev/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-ip-java-sev/kustomization.yaml`

- [i] [INFO] (line 18) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-ldr-java-sev/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-listener-java-sev/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-opd-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-opd-patient-pomr-java-sev/kustomization.yaml`

- [i] [INFO] (line 18) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-opd-ui/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-or-anesthesia-java-sev/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-or-book-java-sev/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-or-booking-java-sev/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-specialized-clinic-java-sev/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-template-java-sev/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/ehr-ic-ui/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/empi/csi-empi-api/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/empi/csi-empi-webui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/empi/csi-empi-wrapper/kustomization.yaml`

- [i] [INFO] (line 16) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/er/csi-ehr-er-functions-dotnet-sev/kustomization.yaml`

- [i] [INFO] (line 25) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/er/csi-ehr-er-ui/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/him/csi-him-ui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/integration/csi-ie-general/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/integration/csi-ie-generalii/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/integration/csi-ie-mobile/kustomization.yaml`

- [i] [INFO] 3 line(s) have trailing whitespace

### `UAT/lab/lab-labgui/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/lab/lab-labmgt-srv/kustomization.yaml`

- [i] [INFO] (line 24) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/pharmacy/csi-java-ehr-ip-doctor-prescription/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 4 line(s) have trailing whitespace

### `UAT/pharmacy/csi-net-base-integrations-medispan/kustomization.yaml`

- [i] [INFO] (line 20) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/pharmacy/csi-phr-base/kustomization.yaml`

- [i] [INFO] (line 18) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/pharmacy/phr-pharmacygui/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/pharmacy/phrbasebgjava/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/renal/ren-hemodialysis-srv/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/reporting/csi-rf-file-uploader/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/rms/csi-morgue-ui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/rms/csi-pms-adt-request-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/rms/csi-rms-masterdata-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/rms/csi-rms-morgue-java-service/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/rms/csi-rms-reservation-java-sev/kustomization.yaml`

- [i] [INFO] 3 line(s) have trailing whitespace

### `UAT/rms/csi-rms-resource-registry-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/security/securityiamcache/kustomization.yaml`

- [!] [WARNING] (line 20) Namespace 'moh-prod' doesn't contain 'uat' but file is in UAT
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/support-portal/support-portal/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

## WAVE1

### `PROD/base/webserver/kustomization.yaml`

- [i] [INFO] (line 22) Unusual target kind 'Namespace'
- [i] [INFO] (line 30) Unusual target kind 'Namespace'
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/base/webserver

### `PROD/billing/csi-bm-approval-java-service/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/billing/csi-bm-approval-ui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/billing/csi-bm-billing-java-service/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/billing/csi-bm-billing-ui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/billing/csi-bm-inte-bridge-java-service/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/billing/csi-bm-invoice-java-service/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/billing/csi-bm-promotion-java-service/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/bloodbank/bb-bloodbankgui/kustomization.yaml`

- [i] [INFO] (line 25) Unusual target kind 'Namespace'
- [i] [INFO] (line 33) Unusual target kind 'Namespace'
- [i] [INFO] 1 line(s) have trailing whitespace
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/bloodbank/bloodbankui

### `PROD/bloodbank/bb-donation-srv/kustomization.yaml`

- [i] [INFO] (line 26) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `PROD/bloodbank/csi-blood-transfusion-java/kustomization.yaml`

- [i] [INFO] (line 25) Unusual target kind 'Namespace'
- [i] [INFO] (line 33) Unusual target kind 'Namespace'

### `PROD/bloodbank/csi-java-bb-service/kustomization.yaml`

- [i] [INFO] (line 25) Unusual target kind 'Namespace'
- [i] [INFO] (line 33) Unusual target kind 'Namespace'

### `PROD/bloodbank/csi-net-bb-mgt-srv/kustomization.yaml`

- [i] [INFO] (line 26) Unusual target kind 'Namespace'
- [i] [INFO] (line 34) Unusual target kind 'Namespace'
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/bloodbank/csinetbbmgtsrv

### `PROD/dms/csi-dms-ui/kustomization.yaml`

- [i] [INFO] (line 22) Unusual target kind 'Namespace'
- [i] [INFO] (line 30) Unusual target kind 'Namespace'
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/dms/dmsui

### `PROD/dms/document-management-engine/kustomization.yaml`

- [i] [INFO] (line 22) Unusual target kind 'Namespace'
- [i] [INFO] (line 30) Unusual target kind 'Namespace'
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/sasmitha.athige/BASE/src/branch/main/dms/dmsstorageengine

### `PROD/dms/document-management-middleware/kustomization.yaml`

- [i] [INFO] (line 22) Unusual target kind 'Namespace'
- [i] [INFO] (line 30) Unusual target kind 'Namespace'

### `PROD/econsent/e-consent-ui/kustomization.yaml`

- [i] [INFO] (line 22) Unusual target kind 'Namespace'
- [i] [INFO] (line 30) Unusual target kind 'Namespace'
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/econsent/econsentui

### `PROD/econsent/e-consent-v2/kustomization.yaml`

- [i] [INFO] (line 22) Unusual target kind 'Namespace'
- [i] [INFO] (line 30) Unusual target kind 'Namespace'
- [!] [WARNING] (line 36) Target block missing 'patch:' field

### `PROD/econsent/e-consent/kustomization.yaml`

- [i] [INFO] (line 22) Unusual target kind 'Namespace'
- [i] [INFO] (line 30) Unusual target kind 'Namespace'

### `PROD/ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev/kustomization.yaml`

- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/ehr/ehripdashboardwiddotnet

### `PROD/ehr/csi-ehr-common-java-sev/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-common-scheduler-java-sev/kustomization.yaml`

- [i] [INFO] (line 25) Unusual target kind 'Namespace'
- [i] [INFO] (line 33) Unusual target kind 'Namespace'

### `PROD/ehr/csi-ehr-config-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-ic-bundle-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-listener-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-opd-patient-pomr-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-opd-ui/kustomization.yaml`

- [i] [INFO] (line 25) Unusual target kind 'Namespace'
- [i] [INFO] (line 33) Unusual target kind 'Namespace'
- [i] [INFO] 1 line(s) have trailing whitespace
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/ehr/ehropdui

### `PROD/ehr/ehr-ic-ui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/ehr/ehricui

### `PROD/empi/csi-empi-crs-integration/kustomization.yaml`

- [i] [INFO] (line 25) Unusual target kind 'Namespace'
- [i] [INFO] (line 33) Unusual target kind 'Namespace'
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/empi/empicrsintegration

### `PROD/empi/csi-empi-hijridate-service/kustomization.yaml`

- [i] [INFO] (line 25) Unusual target kind 'Namespace'
- [i] [INFO] (line 33) Unusual target kind 'Namespace'
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/empi/empihijridatedotnet

### `PROD/empi/csi-empi-patient-registration-srv/kustomization.yaml`

- [i] [INFO] (line 25) Unusual target kind 'Namespace'
- [i] [INFO] (line 33) Unusual target kind 'Namespace'
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/empi/empiwritedotnet

### `PROD/empi/csi-empi-patient-service-read/kustomization.yaml`

- [i] [INFO] (line 25) Unusual target kind 'Namespace'
- [i] [INFO] (line 33) Unusual target kind 'Namespace'

### `PROD/empi/csi-empi-webui/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/empi/empiui

### `PROD/empi/empi-db-sync/overlays/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/er/csi-ehr-er-ui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/er/ehrerui

### `PROD/hhc/hhc-service/kustomization.yaml`

- [i] [INFO] (line 22) Unusual target kind 'Namespace'
- [i] [INFO] (line 30) Unusual target kind 'Namespace'

### `PROD/hhc/hhc-ui/kustomization.yaml`

- [i] [INFO] (line 19) Unusual target kind 'Namespace'
- [i] [INFO] (line 27) Unusual target kind 'Namespace'

### `PROD/him/csi-health-information-srv/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/him/csi-him-ui/kustomization.yaml`

- [i] [INFO] (line 25) Unusual target kind 'Namespace'
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/him/csi-him-ui

### `PROD/integration/csi-ie-general/kustomization.yaml`

- [i] [INFO] (line 42) Unusual target kind 'Namespace'
- [i] [INFO] (line 50) Unusual target kind 'Namespace'
- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/integration/csi-ie-mobile/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/integration/vida-data-gateway/kustomization.yaml`

- [i] [INFO] (line 18) Unusual target kind 'Namespace'
- [i] [INFO] (line 26) Unusual target kind 'Namespace'

### `PROD/lab/lab-labgui/kustomization.yaml`

- [i] [INFO] (line 25) Unusual target kind 'Namespace'
- [i] [INFO] (line 33) Unusual target kind 'Namespace'
- [i] [INFO] 1 line(s) have trailing whitespace
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/lab/labui

### `PROD/lab/lab-labmgt-srv/kustomization.yaml`

- [i] [INFO] (line 20) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/lab/lab-scheduled/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/lab/labscheduled

### `PROD/lab/lab-vidaptor-integration/kustomization.yaml`

- [i] [INFO] (line 25) Unusual target kind 'Namespace'
- [i] [INFO] (line 33) Unusual target kind 'Namespace'
- [i] [INFO] 1 line(s) have trailing whitespace
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/lab/labvidaptor

### `PROD/notification/csi-net-base-email/kustomization.yaml`

- [i] [INFO] (line 22) Unusual target kind 'Namespace'
- [i] [INFO] (line 30) Unusual target kind 'Namespace'
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/notification/notynetbaseemail

### `PROD/notification/csi-net-base-message-templates/kustomization.yaml`

- [i] [INFO] (line 24) Unusual target kind 'Namespace'
- [i] [INFO] (line 32) Unusual target kind 'Namespace'

### `PROD/notification/csi-net-base-notifications-query/kustomization.yaml`

- [i] [INFO] (line 22) Unusual target kind 'Namespace'
- [i] [INFO] (line 30) Unusual target kind 'Namespace'

### `PROD/notification/csi-net-base-notifications/kustomization.yaml`

- [i] [INFO] (line 22) Unusual target kind 'Namespace'
- [i] [INFO] (line 30) Unusual target kind 'Namespace'

### `PROD/notification/csi-net-base-sms/kustomization.yaml`

- [i] [INFO] (line 22) Unusual target kind 'Namespace'
- [i] [INFO] (line 30) Unusual target kind 'Namespace'
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/notification/notynetbasesms

### `PROD/notification/csi-net-base-wss/kustomization.yaml`

- [i] [INFO] (line 24) Unusual target kind 'Namespace'
- [i] [INFO] (line 32) Unusual target kind 'Namespace'
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/notification/notynetbasewss

### `PROD/notification/noty-builder-ui/kustomization.yaml`

- [i] [INFO] (line 19) Unusual target kind 'Namespace'
- [i] [INFO] (line 27) Unusual target kind 'Namespace'
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/notification/notyui

### `PROD/notification/notyexternalservices/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/otp-service/kustomization.yaml`

- [i] [INFO] (line 15) Unusual target kind 'Namespace'
- [i] [INFO] (line 23) Unusual target kind 'Namespace'

### `PROD/pharmacy/csi-phr-base/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/pharmacy/csi-phr-cron/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/pharmacy/csi-phr-cron

### `PROD/pharmacy/phr-pharmacygui/kustomization.yaml`

- [i] [INFO] (line 24) Unusual target kind 'Namespace'
- [i] [INFO] (line 32) Unusual target kind 'Namespace'
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/pharmacy/pharmacyui

### `PROD/pharmacy/phrbasebgjava/kustomization.yaml`

- [i] [INFO] (line 25) Unusual target kind 'Namespace'
- [i] [INFO] (line 33) Unusual target kind 'Namespace'
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/pharmacy/phrbasebgjava

### `PROD/renal/ren-hemodialysis-srv/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/reporting/csi-rf-file-uploader/kustomization.yaml`

- [i] [INFO] (line 25) Unusual target kind 'Namespace'
- [i] [INFO] (line 33) Unusual target kind 'Namespace'

### `PROD/reporting/csi-streaming-etl/kustomization.yaml`

- [i] [INFO] (line 22) Unusual target kind 'Namespace'
- [i] [INFO] (line 30) Unusual target kind 'Namespace'
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/reporting/csistreamingetl

### `PROD/reporting/report-studio-ui/kustomization.yaml`

- [i] [INFO] (line 22) Unusual target kind 'Namespace'
- [i] [INFO] (line 30) Unusual target kind 'Namespace'
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/reporting/reportstudio

### `PROD/rms/csi-mlm-ui/kustomization.yaml`

- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/rms/mlmui

### `PROD/rms/csi-morgue-ui/kustomization.yaml`

- [i] [INFO] (line 25) Unusual target kind 'Namespace'
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/rms/rmsmorgueui

### `PROD/rms/csi-pms-adt-request-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/rms/csi-pms-adt-ui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/rms/csi-rms-masterdata-java-sev/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/rms/csi-rms-morgue-java-service/kustomization.yaml`

- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/rms/rmsmorgue

### `PROD/rms/csi-rms-reservation-java-sev/kustomization.yaml`

- [i] [INFO] 4 line(s) have trailing whitespace

### `PROD/rms/csi-rms-resource-registry-java-sev/kustomization.yaml`

- [i] [INFO] 3 line(s) have trailing whitespace

### `PROD/rms/csi-rms-rules-java-sev/kustomization.yaml`

- [!] [WARNING] (line 18) Namespace 's3-uat' doesn't contain 'prod' but file is in PROD
- [i] [INFO] (line 22) Unusual target kind 'Namespace'
- [i] [INFO] (line 30) Unusual target kind 'Namespace'
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/rms/rmsrules

### `PROD/rms/csi-rms-ui/kustomization.yaml`

- [i] [INFO] (line 25) Unusual target kind 'Namespace'
- [i] [INFO] (line 33) Unusual target kind 'Namespace'

### `PROD/rms/csi-setup-ui/kustomization.yaml`

- [i] [INFO] (line 24) Unusual target kind 'Namespace'
- [i] [INFO] (line 32) Unusual target kind 'Namespace'
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/rms/setupui

### `PROD/support-portal/support-portal/kustomization.yaml`

- [i] [INFO] (line 22) Unusual target kind 'Namespace'
- [i] [INFO] (line 30) Unusual target kind 'Namespace'
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/support-portal/support-portal

### `UAT/base/base-utility-service-java-sev/kustomization.yaml`

- [i] [INFO] 3 line(s) have trailing whitespace

### `UAT/base/csi-personalization-service-java-sev/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/base/csi-uif-admin-ui/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/base/csi-uif-settings/kustomization.yaml`

- [i] [INFO] (line 20) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 3 line(s) have trailing whitespace

### `UAT/base/webserver/kustomization.yaml`

- [i] [INFO] (line 22) Unusual target kind 'Namespace'
- [i] [INFO] (line 30) Unusual target kind 'Namespace'
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/base/webserver

### `UAT/billing/csi-bm-approval-java-service/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/billing/csi-bm-approval-ui/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/billing/csi-bm-billing-java-service/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 5 line(s) have trailing whitespace

### `UAT/billing/csi-bm-billing-ui/kustomization.yaml`

- [i] [INFO] (line 21) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 3 line(s) have trailing whitespace

### `UAT/billing/csi-bm-inte-bridge-java-service/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/billing/csi-bm-invoice-java-service/kustomization.yaml`

- [i] [INFO] 3 line(s) have trailing whitespace

### `UAT/billing/csi-bm-invoice-ui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/billing/csi-bm-promotion-java-service/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/bloodbank/bb-bloodbankgui-mgt/kustomization.yaml`

- [i] [INFO] (line 20) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] (line 23) Unusual target kind 'Namespace'
- [i] [INFO] (line 31) Unusual target kind 'Namespace'
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/bloodbank/bb-bloodbankgui/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] (line 25) Unusual target kind 'Namespace'
- [i] [INFO] (line 33) Unusual target kind 'Namespace'
- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/bloodbank/bb-donation_srv/kustomization.yaml`

- [i] [INFO] (line 24) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/bloodbank/csi-blood-transfusion-java/kustomization.yaml`

- [i] [INFO] (line 20) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] (line 23) Unusual target kind 'Namespace'
- [i] [INFO] (line 31) Unusual target kind 'Namespace'

### `UAT/bloodbank/csi-java-bb-service/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] (line 25) Unusual target kind 'Namespace'
- [i] [INFO] (line 33) Unusual target kind 'Namespace'
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/bloodbank/csi-net-bb-mgt-srv/kustomization.yaml`

- [i] [INFO] (line 21) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/dms/csi-document-management-service/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/dms/dmsmiddleware/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] (line 22) Unusual target kind 'Namespace'
- [i] [INFO] (line 30) Unusual target kind 'Namespace'

### `UAT/dms/dmsstorageengine/kustomization.yaml`

- [x] [ERROR] Duplicate top-level key 'namespace' found 2 times at lines 18, 29
- [x] [ERROR] Duplicate top-level key 'patchesJSON6902' found 2 times at lines 19, 30
- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] (line 30) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] (line 22) Unusual target kind 'Namespace'
- [i] [INFO] (line 33) Unusual target kind 'Namespace'
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/sasmitha.athige/BASE/src/branch/main/dms/dmsstorageengine

### `UAT/econsent/econsent/kustomization.yaml`

- [x] [ERROR] Duplicate top-level key 'namespace' found 2 times at lines 18, 29
- [x] [ERROR] Duplicate top-level key 'patchesJSON6902' found 2 times at lines 19, 30
- [!] [WARNING] Inconsistent patchesJson6902 casing: 'patchesJSON6902' at line(s) 19,30, 'patchesJson6902' at line(s) 40
- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] (line 30) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] (line 22) Unusual target kind 'Namespace'
- [i] [INFO] (line 33) Unusual target kind 'Namespace'

### `UAT/econsent/econsentui/kustomization.yaml`

- [x] [ERROR] Duplicate top-level key 'namespace' found 2 times at lines 18, 29
- [x] [ERROR] Duplicate top-level key 'patchesJSON6902' found 2 times at lines 19, 30
- [!] [WARNING] Inconsistent patchesJson6902 casing: 'patchesJSON6902' at line(s) 19,30, 'patchesJson6902' at line(s) 40
- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] (line 30) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] (line 22) Unusual target kind 'Namespace'
- [i] [INFO] (line 33) Unusual target kind 'Namespace'
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/econsent/econsentui

### `UAT/ehr/csi-ehr-com-opd-master-dotnet-sev/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-com-opd-patient-dotnet-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-common-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-common-scheduler-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-config-java-sev/kustomization.yaml`

- [i] [INFO] 3 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-ic-dashboard-java-sev/kustomization.yaml`

- [i] [INFO] (line 20) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/ehr/csi-ehr-initialassessment-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-ip-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-ldr-java-sev/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-listener-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-opd-patient-pomr-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-opd-ui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-or-anesthesia-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-or-book-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-or-booking-java-sev/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-specialized-clinic-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-template-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/ehr-ic-ui/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/empi/csi-empi-crs-integration/kustomization.yaml`

- [x] [ERROR] Duplicate top-level key 'namespace' found 2 times at lines 18, 32
- [x] [ERROR] Duplicate top-level key 'patchesJSON6902' found 2 times at lines 22, 33
- [!] [WARNING] Inconsistent patchesJson6902 casing: 'patchesJSON6902' at line(s) 22,33, 'patchesJson6902' at line(s) 43
- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] (line 33) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] (line 25) Unusual target kind 'Namespace'
- [i] [INFO] (line 36) Unusual target kind 'Namespace'

### `UAT/empi/csi-empi-hijridate-service/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/empi/csi-empi-webui/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/er/csi-ehr-er-functions-dotnet-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/er/csi-ehr-er-ui/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/hhc/hhc-service/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/hhc/hhc-ui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/him/csi-him-ui/kustomization.yaml`

- [i] [INFO] (line 26) Unusual target kind 'Namespace'

### `UAT/integration/csi-ie-general/kustomization.yaml`

- [i] [INFO] (line 28) Unusual target kind 'Namespace'
- [i] [INFO] (line 36) Unusual target kind 'Namespace'
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/integration/csi-ie-mobile/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/lab/lab-labgui/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] (line 55) Unusual target kind 'Namespace'
- [i] [INFO] (line 63) Unusual target kind 'Namespace'
- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/lab/lab-scheduled/kustomization.yaml`

- [i] [INFO] (line 15) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/lab/lab-vidaptor-integration/kustomization.yaml`

- [i] [INFO] (line 21) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/pharmacy/csi-java-ehr-ip-doctor-prescription/kustomization.yaml`

- [i] [INFO] 3 line(s) have trailing whitespace

### `UAT/pharmacy/csi-net-base-integrations-medispan/kustomization.yaml`

- [i] [INFO] (line 20) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/pharmacy/csi-phr-base/kustomization.yaml`

- [i] [INFO] (line 20) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/pharmacy/csi-phr-cron/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/pharmacy/phr-pharmacygui/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/pharmacy/phr-ui-v2/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/pharmacy/phrbasebgjava/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] (line 25) Unusual target kind 'Namespace'
- [i] [INFO] (line 33) Unusual target kind 'Namespace'
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/pharmacy/phrbasebgjava

### `UAT/rms/csi-pms-adt-ui/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/rms/csi-rms-masterdata-java-sev/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/rms/csi-rms-reservation-java-sev/kustomization.yaml`

- [i] [INFO] 3 line(s) have trailing whitespace

### `UAT/rms/csi-rms-resource-registry-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/rms/csi-rms-rules-java-sev/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] (line 22) Unusual target kind 'Namespace'
- [i] [INFO] (line 31) Unusual target kind 'Namespace'

### `UAT/security/securityiamcache/kustomization.yaml`

- [!] [WARNING] (line 20) Namespace 'moh-prod' doesn't contain 'uat' but file is in UAT

### `UAT/support-portal/support-portal/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

## CS

### `PROD/base/csi-personalization-service-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/base/document-generator-core/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/base/webserver/kustomization.yaml`

- [i] [INFO] (line 22) Unusual target kind 'Namespace'
- [i] [INFO] (line 30) Unusual target kind 'Namespace'
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/base/webserver

### `PROD/billing/csi-bm-approval-java-service/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/billing/csi-bm-approval-ui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/billing/csi-bm-billing-java-service/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/billing/csi-bm-billing-ui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/billing/csi-bm-inte-bridge-java-service/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/billing/csi-bm-invoice-java-service/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/billing/csi-bm-promotion-java-service/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/bloodbank/bb-bloodbankgui/kustomization.yaml`

- [i] [INFO] (line 25) Unusual target kind 'Namespace'
- [i] [INFO] (line 33) Unusual target kind 'Namespace'
- [i] [INFO] 1 line(s) have trailing whitespace
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/bloodbank/bloodbankui

### `PROD/bloodbank/csi-blood-transfusion-java/kustomization.yaml`

- [i] [INFO] (line 25) Unusual target kind 'Namespace'
- [i] [INFO] (line 33) Unusual target kind 'Namespace'

### `PROD/bloodbank/csi-java-bb-service/kustomization.yaml`

- [i] [INFO] (line 25) Unusual target kind 'Namespace'
- [i] [INFO] (line 33) Unusual target kind 'Namespace'

### `PROD/bloodbank/csi-net-bb-mgt-srv/kustomization.yaml`

- [i] [INFO] (line 26) Unusual target kind 'Namespace'
- [i] [INFO] (line 34) Unusual target kind 'Namespace'
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/bloodbank/csinetbbmgtsrv

### `PROD/dms/csi-dms-ui/kustomization.yaml`

- [i] [INFO] (line 22) Unusual target kind 'Namespace'
- [i] [INFO] (line 30) Unusual target kind 'Namespace'
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/dms/dmsui

### `PROD/dms/document-management-engine/kustomization.yaml`

- [i] [INFO] (line 22) Unusual target kind 'Namespace'
- [i] [INFO] (line 30) Unusual target kind 'Namespace'
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/sasmitha.athige/BASE/src/branch/main/dms/dmsstorageengine

### `PROD/dms/document-management-middleware/kustomization.yaml`

- [i] [INFO] (line 22) Unusual target kind 'Namespace'
- [i] [INFO] (line 30) Unusual target kind 'Namespace'

### `PROD/econsent/e-consent-ui/kustomization.yaml`

- [i] [INFO] (line 22) Unusual target kind 'Namespace'
- [i] [INFO] (line 30) Unusual target kind 'Namespace'
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/econsent/econsentui

### `PROD/econsent/e-consent-v2/kustomization.yaml`

- [i] [INFO] (line 22) Unusual target kind 'Namespace'
- [i] [INFO] (line 30) Unusual target kind 'Namespace'
- [!] [WARNING] (line 36) Target block missing 'patch:' field

### `PROD/econsent/e-consent/kustomization.yaml`

- [i] [INFO] (line 22) Unusual target kind 'Namespace'
- [i] [INFO] (line 30) Unusual target kind 'Namespace'

### `PROD/ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/ehr/ehripdashboardwiddotnet

### `PROD/ehr/csi-ehr-common-java-sev/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-common-scheduler-java-sev/kustomization.yaml`

- [i] [INFO] (line 25) Unusual target kind 'Namespace'
- [i] [INFO] (line 33) Unusual target kind 'Namespace'

### `PROD/ehr/csi-ehr-config-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-ic-bundle-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-listener-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-opd-patient-pomr-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-opd-ui/kustomization.yaml`

- [i] [INFO] (line 25) Unusual target kind 'Namespace'
- [i] [INFO] (line 33) Unusual target kind 'Namespace'
- [i] [INFO] 1 line(s) have trailing whitespace
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/ehr/ehropdui

### `PROD/ehr/csi-ehr-specialized-clinic-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/ehr-ic-ui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/ehr/ehricui

### `PROD/empi/csi-empi-crs-integration/kustomization.yaml`

- [i] [INFO] (line 25) Unusual target kind 'Namespace'
- [i] [INFO] (line 33) Unusual target kind 'Namespace'
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/empi/empicrsintegration

### `PROD/empi/csi-empi-hijridate-service/kustomization.yaml`

- [i] [INFO] (line 25) Unusual target kind 'Namespace'
- [i] [INFO] (line 33) Unusual target kind 'Namespace'
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/empi/empihijridatedotnet

### `PROD/empi/csi-empi-patient-registration-srv/kustomization.yaml`

- [i] [INFO] (line 25) Unusual target kind 'Namespace'
- [i] [INFO] (line 33) Unusual target kind 'Namespace'
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/empi/empiwritedotnet

### `PROD/empi/csi-empi-patient-service-read/kustomization.yaml`

- [i] [INFO] (line 25) Unusual target kind 'Namespace'
- [i] [INFO] (line 33) Unusual target kind 'Namespace'

### `PROD/empi/csi-empi-webui/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/empi/empiui

### `PROD/er/csi-ehr-er-functions-dotnet-sev/kustomization.yaml`

- [i] [INFO] 3 line(s) have trailing whitespace

### `PROD/er/csi-ehr-er-ui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/er/ehrerui

### `PROD/hhc/hhc-service/kustomization.yaml`

- [i] [INFO] (line 22) Unusual target kind 'Namespace'
- [i] [INFO] (line 30) Unusual target kind 'Namespace'

### `PROD/hhc/hhc-ui/kustomization.yaml`

- [i] [INFO] (line 19) Unusual target kind 'Namespace'
- [i] [INFO] (line 27) Unusual target kind 'Namespace'

### `PROD/him/csi-health-information-srv/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/him/csi-him-ui/kustomization.yaml`

- [i] [INFO] (line 25) Unusual target kind 'Namespace'
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/him/csi-him-ui

### `PROD/integration/csi-ie-general/kustomization.yaml`

- [i] [INFO] (line 26) Unusual target kind 'Namespace'
- [i] [INFO] (line 34) Unusual target kind 'Namespace'

### `PROD/integration/csi-ie-mobile/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/lab/lab-labgui/kustomization.yaml`

- [i] [INFO] (line 25) Unusual target kind 'Namespace'
- [i] [INFO] (line 33) Unusual target kind 'Namespace'
- [i] [INFO] 1 line(s) have trailing whitespace
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/lab/labui

### `PROD/lab/lab-labmgt-srv/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/lab/lab-scheduled/kustomization.yaml`

- [i] [INFO] (line 25) Unusual target kind 'Namespace'
- [i] [INFO] (line 33) Unusual target kind 'Namespace'
- [i] [INFO] 1 line(s) have trailing whitespace
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/lab/labscheduled

### `PROD/lab/lab-vidaptor-integration/kustomization.yaml`

- [i] [INFO] (line 25) Unusual target kind 'Namespace'
- [i] [INFO] (line 33) Unusual target kind 'Namespace'
- [i] [INFO] 1 line(s) have trailing whitespace
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/lab/labvidaptor

### `PROD/notification/csi-net-base-email/kustomization.yaml`

- [i] [INFO] (line 22) Unusual target kind 'Namespace'
- [i] [INFO] (line 30) Unusual target kind 'Namespace'
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/notification/notynetbaseemail

### `PROD/notification/csi-net-base-message-templates/kustomization.yaml`

- [i] [INFO] (line 24) Unusual target kind 'Namespace'
- [i] [INFO] (line 32) Unusual target kind 'Namespace'

### `PROD/notification/csi-net-base-notifications-query/kustomization.yaml`

- [i] [INFO] (line 22) Unusual target kind 'Namespace'
- [i] [INFO] (line 30) Unusual target kind 'Namespace'

### `PROD/notification/csi-net-base-notifications/kustomization.yaml`

- [i] [INFO] (line 22) Unusual target kind 'Namespace'
- [i] [INFO] (line 30) Unusual target kind 'Namespace'

### `PROD/notification/csi-net-base-sms/kustomization.yaml`

- [i] [INFO] (line 22) Unusual target kind 'Namespace'
- [i] [INFO] (line 30) Unusual target kind 'Namespace'
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/notification/notynetbasesms

### `PROD/notification/csi-net-base-wss/kustomization.yaml`

- [i] [INFO] (line 22) Unusual target kind 'Namespace'
- [i] [INFO] (line 30) Unusual target kind 'Namespace'
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/notification/notynetbasewss

### `PROD/notification/noty-builder-ui/kustomization.yaml`

- [i] [INFO] (line 19) Unusual target kind 'Namespace'
- [i] [INFO] (line 27) Unusual target kind 'Namespace'
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/notification/notyui

### `PROD/notification/notyexternalservices/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/otp-service/kustomization.yaml`

- [i] [INFO] (line 15) Unusual target kind 'Namespace'
- [i] [INFO] (line 23) Unusual target kind 'Namespace'

### `PROD/pharmacy/csi-java-ehr-ip-doctor-prescription/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/pharmacy/csi-net-base-integrations-medispan/kustomization.yaml`

- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/pharmacy/medispan

### `PROD/pharmacy/csi-phr-cron/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/pharmacy/csi-phr-cron

### `PROD/pharmacy/phr-bff/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/pharmacy/phr-pharmacygui/kustomization.yaml`

- [i] [INFO] (line 24) Unusual target kind 'Namespace'
- [i] [INFO] (line 32) Unusual target kind 'Namespace'
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/pharmacy/pharmacyui

### `PROD/pharmacy/phr-ui-v2/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/pharmacy/phrbasebgjava/kustomization.yaml`

- [i] [INFO] (line 25) Unusual target kind 'Namespace'
- [i] [INFO] (line 33) Unusual target kind 'Namespace'
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/pharmacy/phrbasebgjava

### `PROD/renal/ren-hemodialysis-srv/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/reporting/csi-rf-file-uploader/kustomization.yaml`

- [i] [INFO] (line 25) Unusual target kind 'Namespace'
- [i] [INFO] (line 33) Unusual target kind 'Namespace'
- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/reporting/csi-rf-jdbc-sink/kustomization.yaml`

- [i] [INFO] (line 22) Unusual target kind 'Namespace'
- [i] [INFO] (line 30) Unusual target kind 'Namespace'
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/reporting/csi-rf-jdbc-sink

### `PROD/reporting/csi-rf-reportingservice/kustomization.yaml`

- [i] [INFO] (line 22) Unusual target kind 'Namespace'
- [i] [INFO] (line 30) Unusual target kind 'Namespace'
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/reporting/reportingengv2

### `PROD/reporting/csi-streaming-etl/kustomization.yaml`

- [i] [INFO] (line 22) Unusual target kind 'Namespace'
- [i] [INFO] (line 30) Unusual target kind 'Namespace'
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/reporting/csistreamingetl

### `PROD/reporting/report-studio-ui/kustomization.yaml`

- [i] [INFO] (line 22) Unusual target kind 'Namespace'
- [i] [INFO] (line 30) Unusual target kind 'Namespace'
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/reporting/reportstudio

### `PROD/rms/csi-mlm-ui/kustomization.yaml`

- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/rms/mlmui

### `PROD/rms/csi-morgue-ui/kustomization.yaml`

- [i] [INFO] (line 25) Unusual target kind 'Namespace'
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/rms/rmsmorgueui

### `PROD/rms/csi-pms-adt-request-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/rms/csi-pms-adt-ui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/rms/csi-rms-masterdata-java-sev/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/rms/csi-rms-morgue-java-service/kustomization.yaml`

- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/rms/rmsmorgue

### `PROD/rms/csi-rms-reservation-java-sev/kustomization.yaml`

- [i] [INFO] 3 line(s) have trailing whitespace

### `PROD/rms/csi-rms-resource-registry-java-sev/kustomization.yaml`

- [i] [INFO] 3 line(s) have trailing whitespace

### `PROD/rms/csi-rms-rules-java-sev/kustomization.yaml`

- [!] [WARNING] (line 18) Namespace 's3-uat' doesn't contain 'prod' but file is in PROD
- [i] [INFO] (line 22) Unusual target kind 'Namespace'
- [i] [INFO] (line 30) Unusual target kind 'Namespace'
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/rms/rmsrules

### `PROD/rms/csi-rms-ui/kustomization.yaml`

- [i] [INFO] (line 25) Unusual target kind 'Namespace'
- [i] [INFO] (line 33) Unusual target kind 'Namespace'

### `PROD/rms/csi-setup-ui/kustomization.yaml`

- [i] [INFO] (line 24) Unusual target kind 'Namespace'
- [i] [INFO] (line 32) Unusual target kind 'Namespace'
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/rms/setupui

### `PROD/support-portal/support-portal/kustomization.yaml`

- [i] [INFO] (line 22) Unusual target kind 'Namespace'
- [i] [INFO] (line 30) Unusual target kind 'Namespace'
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/support-portal/support-portal

### `UAT/base/base-utility-service-java-sev/kustomization.yaml`

- [i] [INFO] 3 line(s) have trailing whitespace

### `UAT/base/csi-personalization-service-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/base/csi-uif-settings/kustomization.yaml`

- [i] [INFO] (line 20) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 3 line(s) have trailing whitespace

### `UAT/base/webserver/kustomization.yaml`

- [i] [INFO] (line 22) Unusual target kind 'Namespace'
- [i] [INFO] (line 30) Unusual target kind 'Namespace'
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/base/webserver

### `UAT/billing/csi-bm-approval-java-service/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/billing/csi-bm-approval-ui/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/billing/csi-bm-billing-java-service/kustomization.yaml`

- [i] [INFO] 4 line(s) have trailing whitespace

### `UAT/billing/csi-bm-billing-ui/kustomization.yaml`

- [i] [INFO] 3 line(s) have trailing whitespace

### `UAT/billing/csi-bm-inte-bridge-java-service/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/billing/csi-bm-invoice-java-service/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/billing/csi-bm-invoice-ui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/billing/csi-bm-promotion-java-service/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/bloodbank/bb-bloodbankgui/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/bloodbank/bb-donation-srv/kustomization.yaml`

- [i] [INFO] (line 24) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/bloodbank/csi-blood-transfusion-java/kustomization.yaml`

- [i] [INFO] (line 17) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/bloodbank/csi-java-bb-service/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/bloodbank/csi-net-bb-mgt-srv/kustomization.yaml`

- [i] [INFO] (line 24) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/dms/dmsstorageengine/kustomization.yaml`

- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/sasmitha.athige/BASE/src/branch/main/dms/dmsstorageengine

### `UAT/econsent/econsentui/kustomization.yaml`

- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/econsent/econsentui

### `UAT/ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-com-ip-discharge-dotnet-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-com-opd-master-dotnet-sev/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-com-opd-patient-dotnet-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-common-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-config-java-sev/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-ic-bundle-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-ic-dashboard-java-sev/kustomization.yaml`

- [i] [INFO] (line 20) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/ehr/csi-ehr-initialassessment-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-ldr-java-sev/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-listener-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-opd-patient-pomr-java-sev/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-opd-ui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-or-anesthesia-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-or-book-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-or-booking-java-sev/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-specialized-clinic-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-template-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/ehr-ic-ui/kustomization.yaml`

- [i] [INFO] (line 24) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/empi/csi-empi-crs-integration/kustomization.yaml`

- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/empi/empicrsintegration

### `UAT/empi/csi-empi-webui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/er/csi-ehr-er-functions-dotnet-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/er/csi-ehr-er-ui/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/hhc/hhc-service/kustomization.yaml`

- [i] [INFO] (line 22) Unusual target kind 'Namespace'
- [i] [INFO] (line 30) Unusual target kind 'Namespace'

### `UAT/hhc/hhc-ui/kustomization.yaml`

- [i] [INFO] (line 19) Unusual target kind 'Namespace'
- [i] [INFO] (line 27) Unusual target kind 'Namespace'

### `UAT/integration/csi-ie-general/kustomization.yaml`

- [i] [INFO] (line 26) Unusual target kind 'Namespace'
- [i] [INFO] (line 34) Unusual target kind 'Namespace'
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/integration/csi-ie-mobile/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/lab/lab-labgui/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 4 line(s) have trailing whitespace

### `UAT/lab/lab-labmgt-srv/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/lab/lab-scheduled/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/lab/lab-vidaptor-integration/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/pharmacy/csi-java-ehr-ip-doctor-prescription/kustomization.yaml`

- [i] [INFO] (line 24) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 3 line(s) have trailing whitespace

### `UAT/pharmacy/csi-net-base-integrations-medispan/kustomization.yaml`

- [i] [INFO] (line 20) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/pharmacy/csi-phr-cron/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/pharmacy/phr-pharmacygui/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/pharmacy/phr-ui-v2/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/pharmacy/phrbasebgjava/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] (line 25) Unusual target kind 'Namespace'
- [i] [INFO] (line 33) Unusual target kind 'Namespace'
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/pharmacy/phrbasebgjava

### `UAT/renal/ren-hemodialysis-srv/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/reporting/csi-rf-jdbc-sink/kustomization.yaml`

- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/reporting/csi-rf-jdbc-sink

### `UAT/rms/adtui/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/rms/csi-rms-masterdata-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/rms/csi-rms-morgue-java-service/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/rms/csi-rms-reservation-java-sev/kustomization.yaml`

- [i] [INFO] 3 line(s) have trailing whitespace

### `UAT/rms/csi-rms-resource-registry-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/security/securityiamcache/kustomization.yaml`

- [!] [WARNING] (line 20) Namespace 'moh-prod' doesn't contain 'uat' but file is in UAT

## KAUH

### `PROD/base/base-utility-service-java-sev/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/base/csi-uif-admin-ui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/base/csi-uif-settings/kustomization.yaml`

- [i] [INFO] 3 line(s) have trailing whitespace

### `PROD/billing/csi-bm-approval-ui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/billing/csi-bm-billing-java-service/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/billing/csi-bm-billing-ui/kustomization.yaml`

- [i] [INFO] 3 line(s) have trailing whitespace

### `PROD/billing/csi-bm-invoice-java-service/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/bloodbank/bb-bloodbankgui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/bloodbank/csi-net-bb-mgt-srv/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/bloodbank/csi-net-patientinfo-api/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/dms/csi-document-management-service/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-com-opd-master-dotnet-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-common-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-config-java-sev/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-ic-bundle-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-ip-java-sev/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-ldr-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-opd-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-opd-patient-pomr-java-sev/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-or-booking-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-medispan-node-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/ehr-ic-ui/kustomization.yaml`

- [i] [INFO] 3 line(s) have trailing whitespace

### `PROD/er/csi-ehr-er-functions-dotnet-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/him/csi-him-ui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/integration/csi-ie-general/kustomization.yaml`

- [i] [INFO] 3 line(s) have trailing whitespace

### `PROD/integration/csi-ie-mobile/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/lab/lab-labmgt-srv/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/lab/lab-scheduled/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/pharmacy/csi-java-ehr-ip-doctor-prescription/kustomization.yaml`

- [i] [INFO] 3 line(s) have trailing whitespace

### `PROD/pharmacy/csi-phr-base/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/pharmacy/phr-pharmacygui/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/renal/ren-hemodialysis-srv/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/reporting/csi-streaming-etl/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/rms/csi-mlm-ui/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `PROD/rms/csi-pms-adt-ui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/rms/csi-rms-masterdata-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/rms/csi-rms-morgue-java-service/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/rms/csi-rms-reservation-java-sev/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/rms/csi-rms-resource-registry-java-sev/kustomization.yaml`

- [i] [INFO] 4 line(s) have trailing whitespace

### `PROD/rms/csi-setup-ui/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/security/csi-iam-service/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/support-portal/support-portal/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/base/base-utility-service-java-sev/kustomization.yaml`

- [i] [INFO] (line 21) Unusual target kind 'Namespace'
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/base/csi-personalization-service-java-sev/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/base/csi-uif-admin-ui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/base/csi-uif-settings/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/base/document-generator-core/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/base/facadpatientsnapshot/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/base/meddispaan/overlays/PROD/kustomization.yaml`

- [x] [ERROR] Duplicate top-level key 'namespace' found 2 times at lines 15, 26
- [x] [ERROR] Duplicate top-level key 'patchesJSON6902' found 2 times at lines 16, 27
- [i] [INFO] (line 16) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] (line 27) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [!] [WARNING] (line 15) Namespace 'kauh-prod' doesn't contain 'uat' but file is in UAT
- [i] [INFO] (line 19) Unusual target kind 'Namespace'
- [i] [INFO] (line 30) Unusual target kind 'Namespace'

### `UAT/base/webserver/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/billing/csi-bm-approval-java-service/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/billing/csi-bm-billing-java-service/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/billing/csi-bm-billing-ui/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/billing/csi-bm-inte-bridge-java-service/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/billing/csi-bm-invoice-java-service/kustomization.yaml`

- [i] [INFO] 3 line(s) have trailing whitespace

### `UAT/billing/csi-bm-invoice-ui/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/billing/csi-bm-promotion-java-service/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/bloodbank/bb-bloodbankgui-mgt/kustomization.yaml`

- [x] [ERROR] Duplicate top-level key 'namespace' found 2 times at lines 18, 29
- [x] [ERROR] Duplicate top-level key 'patchesJSON6902' found 2 times at lines 19, 30
- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] (line 30) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] (line 22) Unusual target kind 'Namespace'
- [i] [INFO] (line 33) Unusual target kind 'Namespace'
- [i] [INFO] 3 line(s) have trailing whitespace

### `UAT/bloodbank/bb-bloodbankgui/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/bloodbank/bb-donation-srv/kustomization.yaml`

- [i] [INFO] (line 20) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 4 line(s) have trailing whitespace

### `UAT/bloodbank/csi-blood-transfusion-java/kustomization.yaml`

- [i] [INFO] (line 27) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] (line 30) Unusual target kind 'Namespace'

### `UAT/bloodbank/csi-java-bb-service/kustomization.yaml`

- [i] [INFO] 3 line(s) have trailing whitespace

### `UAT/bloodbank/csi-net-bb-mgt-srv/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/bloodbank/csi-net-patientinfo-api/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/dms/csi-dms-ui/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/dms/csi-document-management-service/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/dms/document-management-middleware/kustomization.yaml`

- [i] [INFO] (line 15) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/econsent/econsent/kustomization.yaml`

- [i] [INFO] (line 15) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/econsent/econsentui/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev/kustomization.yaml`

- [i] [INFO] (line 20) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-com-ip-discharge-dotnet-sev/kustomization.yaml`

- [i] [INFO] (line 20) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-com-opd-master-dotnet-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-com-opd-patient-dotnet-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-common-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-common-scheduler-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-config-java-sev/kustomization.yaml`

- [i] [INFO] (line 18) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/ehr/csi-ehr-ic-bundle-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-ic-dashboard-java-sev/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-initialassessment-java-sev/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-ip-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-ldr-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-listener-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-opd-java-sev/kustomization.yaml`

- [i] [INFO] 3 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-opd-patient-pomr-java-sev/kustomization.yaml`

- [i] [INFO] (line 20) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/ehr/csi-ehr-or-book-java-sev/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-template-java-sev/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/empi/csi-empi-api/kustomization.yaml`

- [i] [INFO] 3 line(s) have trailing whitespace

### `UAT/empi/csi-empi-crs-integration/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/empi/csi-empi-hijridate-service/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/empi/csi-empi-patient-service-read/kustomization.yaml`

- [i] [INFO] (line 16) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/empi/csi-empi-webui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/empi/csi-empi-wrapper/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/er/csi-ehr-er-functions-dotnet-sev/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/er/csi-ehr-er-ui/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/hhc/hhc-service/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/hhc/hhc-ui/kustomization.yaml`

- [i] [INFO] (line 16) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/him/csi-health-information-srv/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/him/csi-him-ui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/integration/csi-ie-general/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/integration/csi-ie-generalii/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/integration/csi-ie-mobile/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/lab/lab-labgui/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/lab/lab-labmgt-srv/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/lab/lab-scheduled/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/lab/lab-vidaptor-integration/kustomization.yaml`

- [!] [WARNING] Inconsistent patchesJson6902 casing: 'patchesJSON6902' at line(s) 22, 'patchesJson6902' at line(s) 44
- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/notification/csi-net-base-message-templates/kustomization.yaml`

- [i] [INFO] (line 15) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/notification/csi-net-base-notifications/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/notification/csi-net-base-sms/kustomization.yaml`

- [i] [INFO] (line 18) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/notification/csi-net-base-wss/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/pharmacy/csi-phr-base/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/pharmacy/csi-phr-cron/kustomization.yaml`

- [i] [INFO] (line 15) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/pharmacy/phr-pharmacygui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/pharmacy/phr-ui-v2/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/pharmacy/phrbasebgjava/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/pharmacy/phrbasebgjava

### `UAT/renal/ren-hemodialysis-srv/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/reporting/csi-rf-file-uploader/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/reporting/csi-rf-jdbc-sink/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/reporting/csi-streaming-etl/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/reporting/report-studio-ui/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/rms/csi-ds-dental-core-java-sev/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/rms/csi-mlm-ui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/rms/csi-morgue-ui/kustomization.yaml`

- [i] [INFO] (line 21) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/rms/csi-pms-adt-request-java-sev/kustomization.yaml`

- [i] [INFO] 3 line(s) have trailing whitespace

### `UAT/rms/csi-rms-masterdata-java-sev/kustomization.yaml`

- [i] [INFO] 3 line(s) have trailing whitespace

### `UAT/rms/csi-rms-morgue-java-service/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/rms/csi-rms-resource-registry-java-sev/kustomization.yaml`

- [i] [INFO] (line 24) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 3 line(s) have trailing whitespace

### `UAT/rms/csi-rms-ui/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/rms/csi-setup-ui/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/security/csi-master-data-management-service/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/security/securitycentralauth/kustomization.yaml`

- [x] [ERROR] Duplicate top-level key 'namespace' found 2 times at lines 18, 29
- [x] [ERROR] Duplicate top-level key 'patchesJSON6902' found 2 times at lines 19, 30
- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] (line 30) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] (line 22) Unusual target kind 'Namespace'
- [i] [INFO] (line 33) Unusual target kind 'Namespace'
- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/support-portal/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/support-portal/support-portal/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

## S2

### `PROD/base/csi-uif-settings/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/base/webserver/kustomization.yaml`

- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/base/webserver

### `PROD/billing/csi-bm-approval-java-service/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/billing/csi-bm-approval-ui/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `PROD/billing/csi-bm-billing-ui/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/billing/csi-bm-inte-bridge-java-service/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `PROD/billing/csi-bm-promotion-java-service/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `PROD/bloodbank/bb-bloodbankgui/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/bloodbank/bb-donation-srv/kustomization.yaml`

- [i] [INFO] (line 24) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 3 line(s) have trailing whitespace

### `PROD/bloodbank/csi-java-bb-service/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/bloodbank/csi-net-bb-mgt-srv/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/econsent/e-consent/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-com-opd-master-dotnet-sev/kustomization.yaml`

- [i] [INFO] (line 18) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-com-opd-patient-dotnet-sev/kustomization.yaml`

- [i] [INFO] (line 18) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `PROD/ehr/csi-ehr-common-java-sev/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-common-scheduler-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-initialassessment-java-sev/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-ip-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-ldr-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-listener-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-opd-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-opd-patient-pomr-java-sev/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `PROD/ehr/csi-ehr-or-book-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-or-booking-java-sev/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `PROD/ehr/csi-ehr-template-java-sev/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/ehr/ehr-ic-ui/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `PROD/empi/csi-empi-webui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/er/csi-ehr-er-ui/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/hhc/hhc-service/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/him/csi-health-information-srv/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/him/csi-him-ui/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/integration/csi-ie-general/kustomization.yaml`

- [i] [INFO] 6 line(s) have trailing whitespace

### `PROD/integration/csi-ie-generalii/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/lab/lab-labmgt-srv/kustomization.yaml`

- [i] [INFO] 6 line(s) have trailing whitespace

### `PROD/lab/lab-scheduled/kustomization.yaml`

- [i] [INFO] 4 line(s) have trailing whitespace

### `PROD/pharmacy/csi-java-ehr-ip-doctor-prescription/kustomization.yaml`

- [i] [INFO] (line 20) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `PROD/pharmacy/csi-net-base-integrations-medispan/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `PROD/pharmacy/csi-phr-base/kustomization.yaml`

- [i] [INFO] (line 18) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `PROD/pharmacy/phr-pharmacygui/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/pharmacy/phrbasebgjava/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/renal/ren-hemodialysis-srv/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `PROD/rms/csi-mlm-ui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/rms/csi-morgue-ui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/rms/csi-pms-adt-request-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/rms/csi-rms-masterdata-java-sev/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/rms/csi-rms-resource-registry-java-sev/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/rms/csi-rms-ui/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `PROD/support-portal/support-portal/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/base/base-utility-service-java-sev/kustomization.yaml`

- [i] [INFO] 4 line(s) have trailing whitespace

### `UAT/base/csi-uif-admin-ui/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/base/csi-uif-settings/kustomization.yaml`

- [i] [INFO] 3 line(s) have trailing whitespace

### `UAT/base/webserver/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] (line 22) Unusual target kind 'Namespace'
- [i] [INFO] (line 30) Unusual target kind 'Namespace'

### `UAT/billing/csi-bm-approval-ui/kustomization.yaml`

- [i] [INFO] (line 26) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/billing/csi-bm-billing-java-service/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 3 line(s) have trailing whitespace

### `UAT/billing/csi-bm-billing-ui/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/billing/csi-bm-inte-bridge-java-service/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/billing/csi-bm-invoice-java-service/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/billing/csi-bm-invoice-ui/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/billing/csi-bm-promotion-java-service/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/bloodbank/bb-bloodbankgui/kustomization.yaml`

- [i] [INFO] (line 20) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/bloodbank/bb-donation-srv/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/bloodbank/csi-java-bb-service/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/dms/dmsstorageengine/kustomization.yaml`

- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/sasmitha.athige/BASE/src/branch/main/dms/dmsstorageengine

### `UAT/econsent/econsent/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/econsent/econsentui/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-com-opd-master-dotnet-sev/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-com-opd-patient-dotnet-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-common-scheduler-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-config-java-sev/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-ic-dashboard-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-initialassessment-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-ip-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-ldr-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-listener-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-opd-patient-pomr-java-sev/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/ehr/csi-ehr-opd-ui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-or-anesthesia-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-or-book-java-sev/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-or-booking-java-sev/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-specialized-clinic-java-sev/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-template-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/ehr-ic-ui/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/empi/csi-empi-api/kustomization.yaml`

- [i] [INFO] 4 line(s) have trailing whitespace

### `UAT/er/csi-ehr-er-functions-dotnet-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/er/csi-ehr-er-ui/kustomization.yaml`

- [i] [INFO] (line 25) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/him/csi-health-information-srv/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/him/csi-him-ui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/integration/csi-ie-general/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/integration/csi-ie-mobile/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/lab/lab-labgui/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/lab/lab-labmgt-srv/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/notification/noty-builder-ui/kustomization.yaml`

- [i] [INFO] (line 19) Unusual target kind 'Namespace'
- [i] [INFO] (line 27) Unusual target kind 'Namespace'
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/pharmacy/csi-java-ehr-ip-doctor-prescription/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/pharmacy/csi-phr-base/kustomization.yaml`

- [i] [INFO] (line 24) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/pharmacy/phr-pharmacygui/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/pharmacy/phrbasebgjava/kustomization.yaml`

- [i] [INFO] (line 25) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/rms/csi-pms-adt-ui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/rms/csi-rms-masterdata-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/rms/csi-rms-morgue-java-service/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/rms/csi-rms-reservation-java-sev/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/rms/csi-rms-resource-registry-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/rms/csi-rms-ui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/rms/csi-setup-ui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

## S3

### `PROD/base/base-utility-service-java-sev/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/billing/csi-bm-approval-java-service/kustomization.yaml`

- [i] [INFO] (line 18) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/billing/csi-bm-approval-ui/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/billing/csi-bm-billing-java-service/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/billing/csi-bm-billing-ui/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/billing/csi-bm-inte-bridge-java-service/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/billing/csi-bm-invoice-java-service/kustomization.yaml`

- [i] [INFO] (line 17) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/billing/csi-bm-invoice-ui/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/billing/csi-bm-promotion-java-service/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/bloodbank/bb-bloodbankgui-mgt/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/bloodbank/bb-bloodbankgui/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `PROD/bloodbank/bb-donation-srv/kustomization.yaml`

- [i] [INFO] (line 20) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 6 line(s) have trailing whitespace

### `PROD/bloodbank/csi-java-bb-service/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/dms/document-management-engine/kustomization.yaml`

- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/sasmitha.athige/BASE/src/branch/main/dms/dmsstorageengine

### `PROD/econsent/e-consent-v2/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-com-ip-discharge-dotnet-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-com-opd-master-dotnet-sev/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-com-opd-patient-dotnet-sev/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-common-java-sev/kustomization.yaml`

- [i] [INFO] 3 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-common-scheduler-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-config-java-sev/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-ic-bundle-java-sev/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-ic-dashboard-java-sev/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-initialassessment-java-sev/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-ip-java-sev/kustomization.yaml`

- [i] [INFO] 3 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-ldr-java-sev/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-listener-java-sev/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-opd-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-opd-patient-pomr-java-sev/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-opd-ui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-or-anesthesia-java-sev/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-or-book-java-sev/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-or-booking-java-sev/kustomization.yaml`

- [i] [INFO] (line 18) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `PROD/ehr/csi-ehr-specialized-clinic-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-template-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-workflow-automation-service-java-sev/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `PROD/ehr/ehr-ic-ui/kustomization.yaml`

- [i] [INFO] (line 21) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `PROD/empi/csi-empi-webui/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/er/csi-ehr-er-functions-dotnet-sev/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/er/csi-ehr-er-ui/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/him/csi-health-information-srv/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/him/csi-him-ui/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 3 line(s) have trailing whitespace

### `PROD/integration/csi-ie-general/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/integration/csi-ie-generalii/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/lab/lab-labgui/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/lab/lab-labmgt-srv/kustomization.yaml`

- [i] [INFO] 3 line(s) have trailing whitespace

### `PROD/lab/lab-scheduled/kustomization.yaml`

- [i] [INFO] (line 18) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/lab/lab-vidaptor-integration/kustomization.yaml`

- [i] [INFO] (line 18) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/notification/csi-net-base-notifications/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/notification/noty-builder-ui/kustomization.yaml`

- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/notification/notyui

### `PROD/pharmacy/csi-java-ehr-ip-doctor-prescription/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/pharmacy/csi-net-base-integrations-medispan/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/pharmacy/csi-phr-base/kustomization.yaml`

- [i] [INFO] 3 line(s) have trailing whitespace

### `PROD/pharmacy/phr-pharmacygui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/pharmacy/phrbasebgjava/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/renal/ren-hemodialysis-srv/kustomization.yaml`

- [i] [INFO] (line 24) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `PROD/reporting/csi-rf-file-uploader/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] (line 26) Unusual target kind 'Namespace'
- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/reporting/csi-rf-jdbc-sink/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/reporting/csi-rf-reportingservice/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/rms/csi-mlm-ui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/rms/csi-pms-adt-request-java-sev/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `PROD/rms/csi-pms-adt-ui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/rms/csi-rms-masterdata-java-sev/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/rms/csi-rms-morgue-java-service/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/rms/csi-rms-reservation-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/rms/csi-rms-resource-registry-java-sev/kustomization.yaml`

- [i] [INFO] 3 line(s) have trailing whitespace

### `PROD/rms/csi-rms-rules-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/rms/csi-rms-ui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/base/base-utility-service-java-sev/kustomization.yaml`

- [i] [INFO] 3 line(s) have trailing whitespace

### `UAT/base/csi-uif-admin-ui/kustomization.yaml`

- [i] [INFO] (line 24) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/base/csi-uif-settings/kustomization.yaml`

- [i] [INFO] 3 line(s) have trailing whitespace

### `UAT/base/webserver/kustomization.yaml`

- [x] [ERROR] Duplicate top-level key 'namespace' found 2 times at lines 18, 29
- [x] [ERROR] Duplicate top-level key 'patchesJSON6902' found 2 times at lines 19, 30
- [!] [WARNING] Inconsistent patchesJson6902 casing: 'patchesJSON6902' at line(s) 19,30, 'patchesJson6902' at line(s) 40
- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] (line 30) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] (line 22) Unusual target kind 'Namespace'
- [i] [INFO] (line 33) Unusual target kind 'Namespace'
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/base/webserver

### `UAT/billing/csi-bm-approval-ui/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/billing/csi-bm-billing-java-service/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 3 line(s) have trailing whitespace

### `UAT/billing/csi-bm-billing-ui/kustomization.yaml`

- [i] [INFO] (line 24) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 4 line(s) have trailing whitespace

### `UAT/billing/csi-bm-inte-bridge-java-service/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/billing/csi-bm-invoice-java-service/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/billing/csi-bm-invoice-ui/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/billing/csi-bm-promotion-java-service/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/bloodbank/bb-bloodbankgui-mgt/kustomization.yaml`

- [x] [ERROR] Duplicate top-level key 'namespace' found 2 times at lines 24, 35
- [x] [ERROR] Duplicate top-level key 'patchesJSON6902' found 2 times at lines 25, 36
- [i] [INFO] (line 25) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] (line 36) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] (line 28) Unusual target kind 'Namespace'
- [i] [INFO] (line 39) Unusual target kind 'Namespace'
- [i] [INFO] 4 line(s) have trailing whitespace

### `UAT/bloodbank/bb-bloodbankgui/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/bloodbank/bloodbankjava/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/bloodbank/bloodbanknet/kustomization.yaml`

- [i] [INFO] (line 24) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 3 line(s) have trailing whitespace

### `UAT/bloodbank/csi-blood-transfusion-java/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/bloodbank/csi-net-bb-mgt-srv/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/dms/dmsstorageengine/kustomization.yaml`

- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/sasmitha.athige/BASE/src/branch/main/dms/dmsstorageengine

### `UAT/econsent/e-consent-v2/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-com-opd-master-dotnet-sev/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-com-opd-patient-dotnet-sev/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-common-scheduler-java-sev/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-config-java-sev/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-data-stream-core/kustomization.yaml`

- [x] [ERROR] Duplicate top-level key 'patchesJson6902' found 2 times at lines 21, 38
- [i] [INFO] 5 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-ic-bundle-java-sev/kustomization.yaml`

- [i] [INFO] 3 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-initialassessment-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-ip-java-sev/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-ldr-java-sev/kustomization.yaml`

- [i] [INFO] (line 18) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-listener-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-opd-patient-pomr-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-opd-ui/kustomization.yaml`

- [i] [INFO] 3 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-or-anesthesia-java-sev/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-or-book-java-sev/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-or-booking-java-sev/kustomization.yaml`

- [i] [INFO] 4 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-specialized-clinic-java-sev/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-template-java-sev/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/ehr/csi-workflow-automation-service-java-sev/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/empi/csi-empi-api/kustomization.yaml`

- [i] [INFO] 8 line(s) have trailing whitespace

### `UAT/empi/csi-empi-patient-service-read/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/empi/csi-empi-webui/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/empi/csi-empi-wrapper/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/er/csi-ehr-er-functions-dotnet-sev/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/er/csi-ehr-er-ui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/him/csi-health-information-srv/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/him/csi-him-ui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/integration/csi-ie-general/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/integration/csi-ie-mobile/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/lab/lab-labgui/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/lab/lab-labmgt-srv/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/lab/lab-scheduled/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/lab/lab-vidaptor-integration/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/notification/noty-builder-ui/kustomization.yaml`

- [x] [ERROR] Duplicate top-level key 'patchesStrategicMerge' found 2 times at lines 6, 14

### `UAT/pharmacy/csi-java-ehr-ip-doctor-prescription/kustomization.yaml`

- [i] [INFO] 3 line(s) have trailing whitespace

### `UAT/pharmacy/csi-phr-base/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/pharmacy/phr-pharmacygui/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/pharmacy/phrbasebgjava/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/BASE/BASE-REPO/pharmacy/phrbasebgjava

### `UAT/renal/ren-hemodialysis-srv/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/rms/csi-ds-dental-core-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/rms/csi-mlm-ui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/rms/csi-pms-adt-request-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/rms/csi-rms-masterdata-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/rms/csi-rms-morgue-java-service/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/rms/csi-rms-reservation-java-sev/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/rms/csi-rms-resource-registry-java-sev/kustomization.yaml`

- [i] [INFO] (line 20) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/rms/csi-rms-ui/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

## HMG

### `PROD/base/base-utility-service-java-sev/kustomization.yaml`

- [i] [INFO] 3 line(s) have trailing whitespace

### `PROD/base/csi-uif-admin-ui/kustomization.yaml`

- [i] [INFO] 4 line(s) have trailing whitespace

### `PROD/base/csi-uif-settings/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/base/webserver/kustomization.yaml`

- [!] [WARNING] Inconsistent patchesJson6902 casing: 'patchesJSON6902' at line(s) 16, 'patchesJson6902' at line(s) 34
- [i] [INFO] (line 16) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] (line 19) Unusual target kind 'Namespace'
- [i] [INFO] (line 27) Unusual target kind 'Namespace'

### `PROD/billing/csi-bm-approval-java-service/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/billing/csi-bm-approval-ui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/billing/csi-bm-billing-java-service/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/billing/csi-bm-billing-ui/kustomization.yaml`

- [i] [INFO] (line 21) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/billing/csi-bm-inte-bridge-java-service/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/billing/csi-bm-invoice-java-service/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/billing/csi-bm-invoice-ui/kustomization.yaml`

- [i] [INFO] (line 20) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `PROD/billing/csi-bm-promotion-java-service/kustomization.yaml`

- [i] [INFO] (line 20) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `PROD/bloodbank/bb-bloodbankgui/kustomization.yaml`

- [i] [INFO] (line 20) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `PROD/bloodbank/bb-donation-srv/kustomization.yaml`

- [i] [INFO] (line 20) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/cssd/csi-cssd-java-sev/kustomization.yaml`

- [i] [INFO] (line 24) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/dms/csi-document-management-service/kustomization.yaml`

- [i] [INFO] (line 18) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `PROD/dms/document-management-engine/kustomization.yaml`

- [!] [WARNING] (line 4) Base URL doesn't reference known BASE repos: https://git.cloudsolutions.com.sa/sasmitha.athige/BASE/src/branch/main/dms/dmsstorageengine

### `PROD/econsent/e-consent-v2/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-com-opd-master-dotnet-sev/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `PROD/ehr/csi-ehr-com-opd-patient-dotnet-sev/kustomization.yaml`

- [i] [INFO] (line 20) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `PROD/ehr/csi-ehr-common-java-sev/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `PROD/ehr/csi-ehr-common-scheduler-java-sev/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-config-java-sev/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-ic-bundle-java-sev/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `PROD/ehr/csi-ehr-ic-dashboard-java-sev/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-initialassessment-java-sev/kustomization.yaml`

- [i] [INFO] (line 20) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `PROD/ehr/csi-ehr-ip-java-sev/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `PROD/ehr/csi-ehr-ldr-java-sev/kustomization.yaml`

- [i] [INFO] (line 20) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-opd-java-sev/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-opd-patient-pomr-java-sev/kustomization.yaml`

- [i] [INFO] (line 18) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `PROD/ehr/csi-ehr-opd-ui/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `PROD/ehr/csi-ehr-or-anesthesia-java-sev/kustomization.yaml`

- [i] [INFO] (line 20) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-or-book-java-sev/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `PROD/ehr/csi-ehr-or-booking-java-sev/kustomization.yaml`

- [i] [INFO] (line 20) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-specialized-clinic-java-sev/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-ehr-template-java-sev/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/ehr/csi-workflow-automation-service-java-sev/kustomization.yaml`

- [i] [INFO] (line 20) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/ehr/ehr-ic-ui/kustomization.yaml`

- [i] [INFO] (line 20) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `PROD/empi/csi-empi-crs-integration/kustomization.yaml`

- [i] [INFO] (line 19) Unusual target kind 'Namespace'
- [i] [INFO] (line 28) Unusual target kind 'Namespace'

### `PROD/empi/csi-empi-hijridate-service/kustomization.yaml`

- [i] [INFO] (line 19) Unusual target kind 'Namespace'
- [i] [INFO] (line 27) Unusual target kind 'Namespace'

### `PROD/empi/csi-empi-patient-registration-srv/kustomization.yaml`

- [i] [INFO] (line 17) Unusual target kind 'Namespace'
- [i] [INFO] (line 25) Unusual target kind 'Namespace'
- [i] [INFO] (line 33) Unusual target kind 'Namespace'

### `PROD/empi/csi-empi-patient-service-read/kustomization.yaml`

- [i] [INFO] (line 18) Unusual target kind 'Namespace'
- [i] [INFO] (line 26) Unusual target kind 'Namespace'
- [i] [INFO] (line 34) Unusual target kind 'Namespace'

### `PROD/empi/csi-empi-webui/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `PROD/er/csi-ehr-er-functions-dotnet-sev/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/er/csi-ehr-er-ui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/hhc/hhc-service/kustomization.yaml`

- [i] [INFO] 3 line(s) have trailing whitespace

### `PROD/hhc/hhc-ui/kustomization.yaml`

- [i] [INFO] 3 line(s) have trailing whitespace

### `PROD/him/csi-him-ui/kustomization.yaml`

- [i] [INFO] (line 20) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `PROD/integration/csi-ie-general/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/integration/csi-ie-mobile/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/integration/csiiemobile-v2/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/lab/lab-labgui/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/lab/lab-labmgt-srv/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/lab/lab-scheduled/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/notification/notyexternalservices/kustomization.yaml`

- [i] [INFO] 3 line(s) have trailing whitespace

### `PROD/pharmacy/csi-java-ehr-ip-doctor-prescription/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/pharmacy/csi-phr-base/kustomization.yaml`

- [i] [INFO] (line 55) Unusual target kind 'ScaledObject'
- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/pharmacy/phr-pharmacygui/kustomization.yaml`

- [i] [INFO] (line 23) Unusual target kind 'Namespace'

### `PROD/pharmacy/phr-ui-v2/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/renal/ren-hemodialysis-srv/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `PROD/reporting/csi-rf-file-uploader/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/rms/csi-ds-dental-core-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/rms/csi-mlm-ui/kustomization.yaml`

- [i] [INFO] (line 20) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `PROD/rms/csi-morgue-ui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/rms/csi-pms-adt-request-java-sev/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/rms/csi-rms-masterdata-java-sev/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/rms/csi-rms-morgue-java-service/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/rms/csi-rms-reservation-java-sev/kustomization.yaml`

- [i] [INFO] (line 21) Unusual target kind 'ScaledObject'
- [i] [INFO] 3 line(s) have trailing whitespace

### `PROD/rms/csi-rms-resource-registry-java-sev/kustomization.yaml`

- [i] [INFO] 4 line(s) have trailing whitespace

### `PROD/rms/csi-rms-ui/kustomization.yaml`

- [i] [INFO] (line 20) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/rms/rmsreservation-360/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `PROD/security/csi-iam-service/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/security/csi-roles-permissions-management-service/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `PROD/twin-doctor/twin-doctor-backend/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/base/base-utility-service-java-sev/kustomization.yaml`

- [i] [INFO] 3 line(s) have trailing whitespace

### `UAT/billing/csi-bm-approval-ui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/billing/csi-bm-billing-ui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/billing/csi-bm-inte-bridge-java-service/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/billing/csi-bm-promotion-java-service/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/bloodbank/bb-bloodbankgui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/bloodbank/bb-donation-srv/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/bloodbank/csi-net-bb-mgt-srv/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/bloodbank/csi-net-patientinfo-api/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/cssd/csi-cssd-java-sev/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 4 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-common-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-data-stream-core/kustomization.yaml`

- [i] [INFO] 5 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-ic-bundle-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-initialassessment-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-ldr-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-opd-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ehr/csi-ehr-opd-patient-pomr-java-sev/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/ehr/ehr-ic-ui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/empi/csi-empi-api/kustomization.yaml`

- [i] [INFO] 3 line(s) have trailing whitespace

### `UAT/empi/csi-empi-crs-integration/kustomization.yaml`

- [x] [ERROR] Duplicate top-level key 'patchesJSON6902' found 2 times at lines 20, 31
- [!] [WARNING] Inconsistent patchesJson6902 casing: 'patchesJSON6902' at line(s) 20,31, 'patchesJson6902' at line(s) 41
- [i] [INFO] (line 20) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] (line 31) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] (line 23) Unusual target kind 'Namespace'
- [i] [INFO] (line 34) Unusual target kind 'Namespace'

### `UAT/empi/csi-empi-hijridate-service/kustomization.yaml`

- [i] [INFO] (line 21) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] (line 24) Unusual target kind 'Namespace'
- [i] [INFO] (line 32) Unusual target kind 'Namespace'

### `UAT/empi/csi-empi-patient-registration-srv/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/empi/csi-empi-patient-service-read/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/empi/csi-empi-wrapper/kustomization.yaml`

- [i] [INFO] (line 16) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/empi/empi-services-proxy/kustomization.yaml`

- [!] [WARNING] Missing 'apiVersion' field
- [!] [WARNING] Missing 'kind' field
- [!] [WARNING] Missing both 'bases' and 'resources' fields

### `UAT/er/csi-ehr-er-functions-dotnet-sev/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')
- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/er/csi-ehr-er-ui/kustomization.yaml`

- [i] [INFO] (line 23) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/hhc/hhc-service/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/hhc/hhc-ui/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/integration/ie-integ-dotnet/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/ivf/csi-ivf-service/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/lab/lab-labgui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/lab/lab-labmgt-srv/kustomization.yaml`

- [i] [INFO] (line 22) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/lab/lab-vidaptor-integration/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/notification/csi-vidaplus-external/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/pharmacy/csi-java-ehr-ip-doctor-prescription/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/pharmacy/csi-net-base-integrations-medispan/kustomization.yaml`

- [i] [INFO] (line 19) Non-standard casing 'patchesJSON6902' (expected 'patchesJson6902')

### `UAT/pharmacy/csi-phr-cron/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/pharmacy/phr-pharmacygui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/pharmacy/phr-ui-v2/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/reporting/csi-rf-file-uploader/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/reporting/csi-rf-reportingservice/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/reporting/csi-streaming-etl/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/rms/csi-ds-dental-core-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/rms/csi-pms-adt-request-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/rms/csi-rms-masterdata-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/rms/csi-rms-reservation-java-sev-360/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/rms/csi-rms-reservation-java-sev/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/rms/csi-rms-resource-registry-java-sev/kustomization.yaml`

- [i] [INFO] 2 line(s) have trailing whitespace

### `UAT/rms/csi-rms-ui/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

### `UAT/support-portal/support-portal/kustomization.yaml`

- [i] [INFO] 1 line(s) have trailing whitespace

