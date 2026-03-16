# PROD Folder Rename Plan - S2

Based on UAT rename history (`final.md`) and PROD git history.

## Planned Renames (2)

Old name found in PROD, will be renamed to new standard name.

| Old Name (in PROD) | New Name (standard) |
|---|---|
| `PROD/econsent/econsent` | `PROD/econsent/e-consent` |
| `PROD/econsent/econsentui` | `PROD/econsent/e-consent-ui` |

## Already Correct (96)

PROD already has the new standard name.

| Service Name |
|---|
| `PROD/apigateway/api-gateway` |
| `PROD/base/base-utility-service-java-sev` |
| `PROD/base/csi-uif-settings` |
| `PROD/base/csi-uif-admin-ui` |
| `PROD/base/csi-uif-settings` |
| `PROD/base/csi-uif-admin-ui` |
| `PROD/base/csi-personalization-service-java-sev` |
| `PROD/billing/csi-bm-billing-ui` |
| `PROD/billing/csi-bm-approval-ui` |
| `PROD/billing/csi-bm-approval-java-service` |
| `PROD/billing/csi-bm-invoice-java-service` |
| `PROD/billing/csi-bm-billing-java-service` |
| `PROD/billing/csi-bm-invoice-ui` |
| `PROD/bloodbank/bb-donation-srv` |
| `PROD/bloodbank/csi-java-bb-service` |
| `PROD/bloodbank/bb-donation-srv` |
| `PROD/bloodbank/bb-bloodbankgui` |
| `PROD/bloodbank/csi-blood-transfusion-java` |
| `PROD/bloodbank/csi-net-bb-mgt-srv` |
| `PROD/dms/document-management-middleware` |
| `PROD/dms/document-management-engine` |
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
| `PROD/lab/lab-labmgt-srv` |
| `PROD/lab/lab-labmgt-srv` |
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
| `PROD/reporting/csi-rf-file-uploader` |
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
| `PROD/rms/csi-rms-rules-java-sev` |
| `PROD/rms/csi-rms-ui` |
| `PROD/rms/csi-setup-ui` |
| `PROD/security/csi-iam-service` |
| `PROD/security/csi-master-data-management-service` |
| `PROD/security/csi-roles-permissions-management-service` |
| `PROD/security/csi-ui-registry-service` |
| `PROD/support-portal/support-portal` |

## Not in PROD (0)

Neither old nor new name exists in this repo's PROD.

All services accounted for.

---

## Git History - Matches (80)

PROD git rename history **agrees** with `final.md`.

| Current Folder | Previous Name |
|---|---|
| `PROD/apigateway/api-gateway` | `PROD/api-gateway/apigateway` |
| `PROD/base/csi-personalization-service-java-sev` | `PROD/base/personalizationjava` |
| `PROD/base/csi-uif-admin-ui` | `PROD/base/formbuilderui` |
| `PROD/base/csi-uif-settings` | `PROD/base/configui` |
| `PROD/billing/csi-bm-approval-ui` | `PROD/billing/bmapprovalui` |
| `PROD/billing/csi-bm-billing-java-service` | `PROD/billing/bmbillingjava` |
| `PROD/billing/csi-bm-billing-ui` | `PROD/billing/billingmasterui` |
| `PROD/billing/csi-bm-invoice-java-service` | `PROD/billing/bmbillinginvoicejava` |
| `PROD/billing/csi-bm-invoice-ui` | `PROD/billing/bminvoiceui` |
| `PROD/bloodbank/bb-bloodbankgui` | `PROD/bloodbank/bloodbankui` |
| `PROD/bloodbank/bb-donation-srv` | `PROD/bloodbank/bloodbanknet` |
| `PROD/bloodbank/csi-blood-transfusion-java` | `PROD/bloodbank/bloodtransfusionjava` |
| `PROD/bloodbank/csi-java-bb-service` | `PROD/bloodbank/bloodbankjava` |
| `PROD/dms/csi-dms-ui` | `PROD/dms/dmsui` |
| `PROD/dms/document-management-engine` | `PROD/dms/dmsstorageengine` |
| `PROD/dms/document-management-middleware` | `PROD/dms/dmsmiddleware` |
| `PROD/ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | `PROD/ehr/ehripdashboardwiddotnet` |
| `PROD/ehr/csi-ehr-com-ip-discharge-dotnet-sev` | `PROD/ehr/ehripdischargedotnet` |
| `PROD/ehr/csi-ehr-com-opd-master-dotnet-sev` | `PROD/ehr/ehropdmasterdotnet` |
| `PROD/ehr/csi-ehr-com-opd-patient-dotnet-sev` | `PROD/ehr/ehropdpatientdotnet` |
| `PROD/ehr/csi-ehr-common-java-sev` | `PROD/ehr/ehrcommonjava` |
| `PROD/ehr/csi-ehr-common-scheduler-java-sev` | `PROD/ehr/ehrschedulerjava` |
| `PROD/ehr/csi-ehr-config-java-sev` | `PROD/ehr/ehrconfigjava` |
| `PROD/ehr/csi-ehr-ic-bundle-java-sev` | `PROD/ehr/ehricbundlejava` |
| `PROD/ehr/csi-ehr-ic-dashboard-java-sev` | `PROD/ehr/ehricdashboardjava` |
| `PROD/ehr/csi-ehr-initialassessment-java-sev` | `PROD/ehr/ehrintitialassessjava` |
| `PROD/ehr/csi-ehr-ip-java-sev` | `PROD/ehr/ehripjava` |
| `PROD/ehr/csi-ehr-ldr-java-sev` | `PROD/ehr/ehrldrjava` |
| `PROD/ehr/csi-ehr-listener-java-sev` | `PROD/ehr/ehrlistnerjava` |
| `PROD/ehr/csi-ehr-opd-java-sev` | `PROD/ehr/ehropdjava` |
| `PROD/ehr/csi-ehr-opd-patient-pomr-java-sev` | `PROD/ehr/ehrpomrjava` |
| `PROD/ehr/csi-ehr-opd-ui` | `PROD/ehr/ehropdui` |
| `PROD/ehr/csi-ehr-or-anesthesia-java-sev` | `PROD/ehr/ehroranesthesiajava` |
| `PROD/ehr/csi-ehr-or-book-java-sev` | `PROD/ehr/ehrorbookjava` |
| `PROD/ehr/csi-ehr-specialized-clinic-java-sev` | `PROD/ehr/ehrspecializedclinicjava` |
| `PROD/ehr/csi-ehr-template-java-sev` | `PROD/ehr/ehrtemplatejava` |
| `PROD/ehr/ehr-ic-ui` | `PROD/ehr/ehricui` |
| `PROD/empi/csi-empi-crs-integration` | `PROD/empi/empicrsintegration` |
| `PROD/empi/csi-empi-hijridate-service` | `PROD/empi/empihijridatedotnet` |
| `PROD/empi/csi-empi-patient-registration-srv` | `PROD/empi/empiwritedotnet` |
| `PROD/empi/csi-empi-patient-service-read` | `PROD/empi/empireaddotnet` |
| `PROD/empi/csi-empi-webui` | `PROD/empi/empiui` |
| `PROD/er/csi-ehr-er-functions-dotnet-sev` | `PROD/er/erfunctiondotnet` |
| `PROD/er/csi-ehr-er-ui` | `PROD/er/ehrerui` |
| `PROD/hhc/hhc-service` | `PROD/hhc/hhcservice` |
| `PROD/hhc/hhc-ui` | `PROD/hhc/hhcui` |
| `PROD/integration/csi-ie-general` | `PROD/integration/csiiegeneral` |
| `PROD/integration/csi-ie-generalii` | `PROD/integration/ieintegration2` |
| `PROD/integration/csi-ie-mobile` | `PROD/integration/csiiemobile` |
| `PROD/lab/lab-labgui` | `PROD/lab/labui` |
| `PROD/lab/lab-labmgt-srv` | `PROD/lab/labmgmtdotnet` |
| `PROD/lab/lab-scheduled` | `PROD/lab/labscheduled` |
| `PROD/lab/lab-vidaptor-integration` | `PROD/lab/labvidaptor` |
| `PROD/notification/csi-net-base-email` | `PROD/notification/notynetbaseemail` |
| `PROD/notification/csi-net-base-message-templates` | `PROD/notification/notynetbasetemplate` |
| `PROD/notification/csi-net-base-notifications` | `PROD/notification/notynetbasenotification` |
| `PROD/notification/csi-net-base-notifications-query` | `PROD/notification/notynetbasequery` |
| `PROD/notification/csi-net-base-sms` | `PROD/notification/notynetbasesms` |
| `PROD/notification/csi-net-base-wss` | `PROD/notification/notynetbasewss` |
| `PROD/notification/noty-builder-ui` | `PROD/notification/noty-ui` |
| `PROD/pharmacy/csi-java-ehr-ip-doctor-prescription` | `PROD/pharmacy/ehripprescriptionjava` |
| `PROD/pharmacy/csi-net-base-integrations-medispan` | `PROD/pharmacy/medispan` |
| `PROD/pharmacy/csi-phr-base` | `PROD/pharmacy/phrbasejava` |
| `PROD/renal/ren-hemodialysis-srv` | `PROD/renal/renalnet` |
| `PROD/reporting/csi-rf-file-uploader` | `PROD/reporting/reportingupload` |
| `PROD/reporting/csi-streaming-etl` | `PROD/reporting/csistreamingetl` |
| `PROD/reporting/report-studio-ui` | `PROD/reporting/reportstudio` |
| `PROD/rms/csi-ds-dental-core-java-sev` | `PROD/rms/dsdental` |
| `PROD/rms/csi-mlm-ui` | `PROD/rms/mlmui` |
| `PROD/rms/csi-morgue-ui` | `PROD/rms/rmsmorgueui` |
| `PROD/rms/csi-pms-adt-ui` | `PROD/rms/adtui` |
| `PROD/rms/csi-rms-reservation-java-sev` | `PROD/rms/rmsreservation` |
| `PROD/rms/csi-rms-resource-registry-java-sev` | `PROD/rms/rmsresourceregistry` |
| `PROD/rms/csi-rms-rules-java-sev` | `PROD/rms/rmsrules` |
| `PROD/rms/csi-rms-ui` | `PROD/rms/rmsui` |
| `PROD/rms/csi-setup-ui` | `PROD/rms/setupui` |
| `PROD/security/csi-iam-service` | `PROD/security/securityiamservice` |
| `PROD/security/csi-master-data-management-service` | `PROD/security/securitymasterdatamgt` |
| `PROD/security/csi-roles-permissions-management-service` | `PROD/security/securityrolespermissions` |
| `PROD/security/csi-ui-registry-service` | `PROD/security/securityuiregistry` |

## Git History - Git-only Renames (1)

Renames found in PROD git history but **NOT** in `final.md`.

| Current Folder | Previous Name |
|---|---|
| `PROD/reporting/reportingeng` | `PROD/reporting/reportingengv2` |

## Git History - Mismatches (4)

Same current folder, but git and `final.md` disagree on previous name.

| Current Folder | Git Previous | final.md Previous |
|---|---|---|
| `PROD/base/base-utility-service-java-sev` | `PROD/bloodbank/csinetbbmgtsrv` | `PROD/base/baseutilityservicejava` |
| `PROD/reporting/csi-rf-reportingservice` | `PROD/reporting/reportingeng` | `PROD/reporting/reportingengv2` |
| `PROD/rms/csi-pms-adt-request-java-sev` | `PROD/rms/rmsmasterdata` | `PROD/rms/pmsadtrequest` |
| `PROD/rms/csi-rms-masterdata-java-sev` | `PROD/rms/rmsmorgue` | `PROD/rms/rmsmasterdata` |

---

## Unaffected PROD Folders (17)

Exist in PROD but have no matching rename in `final.md`. May need manual review.

- `PROD/base/document-generator-core`
- `PROD/base/facadpatientsnapshot`
- `PROD/base/webserver`
- `PROD/billing/csi-bm-inte-bridge-java-service`
- `PROD/billing/csi-bm-promotion-java-service`
- `PROD/bloodbank/bb-bloodbankgui-mgt`
- `PROD/dms/csi-document-management-service`
- `PROD/econsent/e-consent-v2`
- `PROD/empi/empi-services`
- `PROD/him/csi-him-ui`
- `PROD/integration/csi-ie-dashboards`
- `PROD/otp-service`
- `PROD/pharmacy/csi-phr-cron`
- `PROD/pharmacy/phrbasebgjava`
- `PROD/reporting/csi-rf-jdbc-sink`
- `PROD/security/securityiamcache`
- `PROD/utility/ie-dashboards`

