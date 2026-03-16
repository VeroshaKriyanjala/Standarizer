# PROD Folder Rename Plan - KAUH

Based on UAT rename history (`final.md`) and PROD git history.

## Planned Renames (9)

Old name found in PROD, will be renamed to new standard name.

| Old Name (in PROD) | New Name (standard) |
|---|---|
| `PROD/base/csi.uif.settings` | `PROD/base/csi-uif-settings` |
| `PROD/bloodbank/bb-donation_srv` | `PROD/bloodbank/bb-donation-srv` |
| `PROD/dms/dmsmiddleware` | `PROD/dms/document-management-middleware` |
| `PROD/econsent/econsent` | `PROD/econsent/e-consent` |
| `PROD/econsent/econsentui` | `PROD/econsent/e-consent-ui` |
| `PROD/lab/lab-labmgt_srv` | `PROD/lab/lab-labmgt-srv` |
| `PROD/reporting/reportingupload` | `PROD/reporting/csi-rf-file-uploader` |
| `PROD/rms/rmsrules` | `PROD/rms/csi-rms-rules-java-sev` |
| `PROD/support-portal/csi-support-portal` | `PROD/support-portal/support-portal` |

## Already Correct (85)

PROD already has the new standard name.

| Service Name |
|---|
| `PROD/apigateway/api-gateway` |
| `PROD/base/base-utility-service-java-sev` |
| `PROD/base/csi-uif-admin-ui` |
| `PROD/base/csi-uif-admin-ui` |
| `PROD/base/csi-personalization-service-java-sev` |
| `PROD/billing/csi-bm-billing-ui` |
| `PROD/billing/csi-bm-approval-ui` |
| `PROD/billing/csi-bm-approval-java-service` |
| `PROD/billing/csi-bm-invoice-java-service` |
| `PROD/billing/csi-bm-billing-java-service` |
| `PROD/billing/csi-bm-invoice-ui` |
| `PROD/bloodbank/csi-java-bb-service` |
| `PROD/bloodbank/bb-bloodbankgui` |
| `PROD/bloodbank/csi-blood-transfusion-java` |
| `PROD/bloodbank/csi-net-bb-mgt-srv` |
| `PROD/dms/csi-dms-ui` |
| `PROD/ehr/csi-ehr-common-java-sev` |
| `PROD/ehr/csi-ehr-config-java-sev` |
| `PROD/ehr/csi-ehr-ic-bundle-java-sev` |
| `PROD/ehr/csi-ehr-ic-dashboard-java-sev` |
| `PROD/ehr/ehr-ic-ui` |
| `PROD/ehr/csi-ehr-initialassessment-java-sev` |
| `PROD/ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` |
| `PROD/ehr/csi-ehr-com-ip-discharge-dotnet-sev` |
| `PROD/ehr/csi-ehr-ip-java-sev` |
| `PROD/ehr/csi-ehr-ldr-java-sev` |
| `PROD/ehr/csi-ehr-listener-java-sev` |
| `PROD/ehr/csi-ehr-opd-java-sev` |
| `PROD/ehr/csi-ehr-com-opd-master-dotnet-sev` |
| `PROD/ehr/csi-ehr-com-opd-patient-dotnet-sev` |
| `PROD/ehr/csi-ehr-opd-ui` |
| `PROD/ehr/csi-ehr-or-anesthesia-java-sev` |
| `PROD/ehr/csi-ehr-or-booking-java-sev` |
| `PROD/ehr/csi-ehr-or-book-java-sev` |
| `PROD/ehr/csi-ehr-opd-patient-pomr-java-sev` |
| `PROD/ehr/csi-ehr-common-scheduler-java-sev` |
| `PROD/ehr/csi-ehr-specialized-clinic-java-sev` |
| `PROD/ehr/csi-ehr-template-java-sev` |
| `PROD/ehr/csi-workflow-automation-service-java-sev` |
| `PROD/empi/csi-empi-crs-integration` |
| `PROD/empi/csi-empi-hijridate-service` |
| `PROD/empi/csi-empi-patient-service-read` |
| `PROD/empi/csi-empi-webui` |
| `PROD/empi/csi-empi-patient-registration-srv` |
| `PROD/er/csi-ehr-er-ui` |
| `PROD/er/csi-ehr-er-functions-dotnet-sev` |
| `PROD/hhc/hhc-service` |
| `PROD/hhc/hhc-ui` |
| `PROD/him/csi-health-information-srv` |
| `PROD/integration/csi-ie-general` |
| `PROD/integration/csi-ie-mobile` |
| `PROD/integration/csi-ie-generalii` |
| `PROD/lab/lab-scheduled` |
| `PROD/lab/lab-labgui` |
| `PROD/lab/lab-vidaptor-integration` |
| `PROD/notification/noty-builder-ui` |
| `PROD/notification/csi-net-base-email` |
| `PROD/notification/csi-net-base-notifications` |
| `PROD/notification/csi-net-base-notifications-query` |
| `PROD/notification/csi-net-base-sms` |
| `PROD/notification/csi-net-base-message-templates` |
| `PROD/notification/csi-net-base-wss` |
| `PROD/pharmacy/csi-java-ehr-ip-doctor-prescription` |
| `PROD/pharmacy/csi-net-base-integrations-medispan` |
| `PROD/pharmacy/phr-pharmacygui` |
| `PROD/pharmacy/csi-phr-base` |
| `PROD/renal/ren-hemodialysis-srv` |
| `PROD/reporting/csi-streaming-etl` |
| `PROD/reporting/csi-rf-reportingservice` |
| `PROD/reporting/report-studio-ui` |
| `PROD/rms/csi-pms-adt-ui` |
| `PROD/rms/csi-ds-dental-core-java-sev` |
| `PROD/rms/csi-mlm-ui` |
| `PROD/rms/csi-pms-adt-request-java-sev` |
| `PROD/rms/csi-rms-masterdata-java-sev` |
| `PROD/rms/csi-rms-morgue-java-service` |
| `PROD/rms/csi-morgue-ui` |
| `PROD/rms/csi-rms-reservation-java-sev` |
| `PROD/rms/csi-rms-resource-registry-java-sev` |
| `PROD/rms/csi-rms-ui` |
| `PROD/rms/csi-setup-ui` |
| `PROD/security/csi-iam-service` |
| `PROD/security/csi-master-data-management-service` |
| `PROD/security/csi-roles-permissions-management-service` |
| `PROD/security/csi-ui-registry-service` |

## Not in PROD (4)

Neither old nor new name exists in this repo's PROD.

| Old Name | Expected New Name |
|---|---|
| `base/configui` | `base/csi-uif-settings` |
| `bloodbank/bloodbanknet` | `bloodbank/bb-donation-srv` |
| `dms/dmsstorageengine` | `dms/document-management-engine` |
| `lab/labmgmtdotnet` | `lab/lab-labmgt-srv` |

---

## Git History - Matches (16)

PROD git rename history **agrees** with `final.md`.

| Current Folder | Previous Name |
|---|---|
| `PROD/empi/csi-empi-crs-integration` | `PROD/empi/empicrsintegration` |
| `PROD/empi/csi-empi-hijridate-service` | `PROD/empi/empihijridatedotnet` |
| `PROD/empi/csi-empi-patient-service-read` | `PROD/empi/empireaddotnet` |
| `PROD/empi/csi-empi-webui` | `PROD/empi/empiui` |
| `PROD/er/csi-ehr-er-functions-dotnet-sev` | `PROD/er/erfunctiondotnet` |
| `PROD/er/csi-ehr-er-ui` | `PROD/er/ehrerui` |
| `PROD/hhc/hhc-service` | `PROD/hhc/hhcservice` |
| `PROD/hhc/hhc-ui` | `PROD/hhc/hhcui` |
| `PROD/him/csi-health-information-srv` | `PROD/him/csinethimservi` |
| `PROD/integration/csi-ie-general` | `PROD/integration/csiiegeneral` |
| `PROD/integration/csi-ie-generalii` | `PROD/integration/ieintegration2` |
| `PROD/integration/csi-ie-mobile` | `PROD/integration/csiiemobile` |
| `PROD/lab/lab-labgui` | `PROD/lab/labui` |
| `PROD/lab/lab-scheduled` | `PROD/lab/labscheduled` |
| `PROD/lab/lab-vidaptor-integration` | `PROD/lab/labvidaptor` |
| `PROD/renal/ren-hemodialysis-srv` | `PROD/renal/renalnet` |

## Git History - Git-only Renames (3)

Renames found in PROD git history but **NOT** in `final.md`.

| Current Folder | Previous Name |
|---|---|
| `PROD/empi/csi-empi-wrapper` | `PROD/empi/empiwritedotnet` |
| `PROD/lab/lab-labmgt_srv` | `PROD/lab/labmgmtdotnet` |
| `PROD/support-portal/csi-support-portal` | `PROD/support-portal/support-portal` |

## Git History - Mismatches (0)

Same current folder, but git and `final.md` disagree on previous name.

No mismatches.

---

## Unaffected PROD Folders (15)

Exist in PROD but have no matching rename in `final.md`. May need manual review.

- `PROD/base/document-generator-core`
- `PROD/base/facadpatientsnapshot`
- `PROD/billing/csi-bm-inte-bridge-java-service`
- `PROD/billing/csi-bm-promotion-java-service`
- `PROD/bloodbank/csi-net-patientinfo-api`
- `PROD/dms/csi-document-management-service`
- `PROD/econsent/e-consent-v2`
- `PROD/ehr/csi-medispan-node-sev`
- `PROD/empi/empi-services`
- `PROD/him/csi-him-ui`
- `PROD/otp-service`
- `PROD/pharmacy/csi-phr-cron`
- `PROD/pharmacy/phrbasebgjava`
- `PROD/reporting/csi-rf-jdbc-sink`
- `PROD/security/securityiamcache`

