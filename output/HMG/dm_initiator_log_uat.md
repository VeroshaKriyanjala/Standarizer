# DM-Initiator Update Log - HMG

Mode: LIVE

## Version Check

- base-utility-service-java-sev: `V4.0.2512_W4-174_prod`
  - Threshold: `V4.0.2510_W1-4893_prod`
- csi-iam-service: `V4.0.2602_W2_108_prod`
  - Threshold: `V4.0.2510_W4_14_prod`
- **Conditions met: YES**

## Changes (88 total)

| Service | Change |
|---------|--------|
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Removed extra Sync reference: # - ../../../Sync-new/ |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Removed extra Sync reference: # - ../../../Sync-new/ |
| `ehr/csi-ehr-data-stream-core` | Replaced commented Sync reference with commented DM-Initiator |
| `ehr/csi-ehr-data-stream-core` | Merged duplicate patchesJson6902 section (line 37) |
| `ehr/csi-ehr-data-stream-core` | Added new sync-presync/sync-postsync Job patches |
| `ehr/csi-ehr-data-stream-core` | Commented out line 38: - target: |
| `ehr/csi-ehr-data-stream-core` | Commented out line 39: group: batch |
| `ehr/csi-ehr-data-stream-core` | Commented out line 40: version: v1 |
| `ehr/csi-ehr-data-stream-core` | Commented out line 41: kind: Job |
| `ehr/csi-ehr-data-stream-core` | Commented out line 42: name: .* |
| `ehr/csi-ehr-data-stream-core` | Commented out line 43: patch: |- |
| `ehr/csi-ehr-data-stream-core` | Commented out line 44: - op: replace |
| `ehr/csi-ehr-data-stream-core` | Commented out line 45: path: /metadata/name |
| `ehr/csi-ehr-data-stream-core` | Commented out line 46: value: before-ehr-data-stream-core |
| `ehr/csi-ehr-data-stream-core` | Commented out line 47: - op: add |
| `ehr/csi-ehr-data-stream-core` | Commented out line 48: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-data-stream-core` | Commented out line 49: value: |
| `ehr/csi-ehr-data-stream-core` | Commented out line 50: name: CSI_MODULENAME |
| `ehr/csi-ehr-data-stream-core` | Commented out line 51: value: "ehr-data-stream-core" |
| `ehr/csi-ehr-data-stream-core` | Commented out line 52: - op: add |
| `ehr/csi-ehr-data-stream-core` | Commented out line 53: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-data-stream-core` | Commented out line 54: value: |
| `ehr/csi-ehr-data-stream-core` | Commented out line 55: name: CSI_DATA_VERSION |
| `ehr/csi-ehr-data-stream-core` | Commented out line 56: value: "4.1.170.0" |
| `ehr/csi-ehr-data-stream-core` | Commented out line 57: - op: add |
| `ehr/csi-ehr-data-stream-core` | Commented out line 58: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-data-stream-core` | Commented out line 59: value: |
| `ehr/csi-ehr-data-stream-core` | Commented out line 60: name: CSI_PROJECT_NAME |
| `ehr/csi-ehr-data-stream-core` | Commented out line 61: value: "csi-ehr-data-stream-core" |
| `ehr/csi-ehr-data-stream-core` | Commented out line 62: - op: add |
| `ehr/csi-ehr-data-stream-core` | Commented out line 63: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-data-stream-core` | Commented out line 64: value: |
| `ehr/csi-ehr-data-stream-core` | Commented out line 65: name: CSI_MODULE_NAME |
| `ehr/csi-ehr-data-stream-core` | Commented out line 66: value: "csi-ehr-data-stream-core" |
| `ehr/csi-ehr-data-stream-core` | Commented out line 67: - op: add |
| `ehr/csi-ehr-data-stream-core` | Commented out line 68: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-data-stream-core` | Commented out line 69: value: |
| `ehr/csi-ehr-data-stream-core` | Commented out line 70: name: CSI_PARENT_MODULE_NAME |
| `ehr/csi-ehr-data-stream-core` | Commented out line 71: value: "ehr" |
| `ehr/csi-ehr-data-stream-core` | Moved non-Job target from duplicate section into merged section |
| `ehr/csi-ehr-listener-java-sev` | Removed extra Sync reference: # - ../../../Sync-new/ |
| `empi/csi-empi-crs-integration` | Updated Deployment target name: csi-net-empi-crs-inte -> csi-empi-crs-integration |
| `empi/empi-db-sync/overlays` | Updated Deployment target name: csi-empi-db-sync -> overlays |
| `lab/lab-labgui` | Updated Deployment target name: csi-lab-labg-ui -> lab-labgui |
| `notification/csi-net-base-email` | Updated Deployment target name: csi-net-noty-email -> csi-net-base-email |
| `notification/csi-net-base-notifications` | Updated Deployment target name: csi-net-noty -> csi-net-base-notifications |
| `notification/csi-net-base-notifications-query` | Updated Deployment target name: csi-net-noty-query -> csi-net-base-notifications-query |
| `notification/csi-net-base-sms` | Updated Deployment target name: csi-net-noty-sms -> csi-net-base-sms |
| `notification/csi-vidaplus-external` | Updated Deployment target name: csi-net-ext -> csi-vidaplus-external |
| `pharmacy/csi-net-base-integrations-medispan` | Updated Deployment target name: csi-net-medispan -> csi-net-base-integrations-medispan |
| `pharmacy/csi-phr-base-bgservice` | Updated Deployment target name: csi-phr-base -> csi-phr-base-bgservice |
| `pharmacy/phr-pharmacygui` | Updated Deployment target name: csi-pharmacy-ui -> phr-pharmacygui |
| `reporting/report-studio-ui` | Updated Deployment target name: csi-report-studio-ui -> report-studio-ui |
| `rms/csi-rms-rules-java-sev` | Updated Deployment target name: csi-rms-rules -> csi-rms-rules-java-sev |
| `security/csi-master-data-management-service` | Replaced commented Sync reference with commented DM-Initiator |
| `security/csi-master-data-management-service` | Added new sync-presync/sync-postsync Job patches |
| `security/csi-master-data-management-service` | Commented out line 20: - target: |
| `security/csi-master-data-management-service` | Commented out line 21: group: batch |
| `security/csi-master-data-management-service` | Commented out line 22: version: v1 |
| `security/csi-master-data-management-service` | Commented out line 23: kind: Job |
| `security/csi-master-data-management-service` | Commented out line 24: name: .* |
| `security/csi-master-data-management-service` | Commented out line 25: patch: |- |
| `security/csi-master-data-management-service` | Commented out line 26: - op: replace |
| `security/csi-master-data-management-service` | Commented out line 27: path: /metadata/name |
| `security/csi-master-data-management-service` | Commented out line 28: value: before-csi-master-data-management-service |
| `security/csi-master-data-management-service` | Commented out line 29: namespace: moh-uat |
| `security/csi-master-data-management-service` | Commented out line 30: - op: add |
| `security/csi-master-data-management-service` | Commented out line 31: path: /spec/template/spec/containers/0/env/- |
| `security/csi-master-data-management-service` | Commented out line 32: value: |
| `security/csi-master-data-management-service` | Commented out line 33: name: CSI_PROJECT_NAME |
| `security/csi-master-data-management-service` | Commented out line 34: value: "csi-master-data-management-service" |
| `security/csi-master-data-management-service` | Commented out line 35: - op: add |
| `security/csi-master-data-management-service` | Commented out line 36: path: /spec/template/spec/containers/0/env/- |
| `security/csi-master-data-management-service` | Commented out line 37: value: |
| `security/csi-master-data-management-service` | Commented out line 38: name: CSI_MODULE_NAME |
| `security/csi-master-data-management-service` | Commented out line 39: value: "csi-master-data-management-service" |
| `security/csi-master-data-management-service` | Commented out line 40: - op: add |
| `security/csi-master-data-management-service` | Commented out line 41: path: /spec/template/spec/containers/0/env/- |
| `security/csi-master-data-management-service` | Commented out line 42: value: |
| `security/csi-master-data-management-service` | Commented out line 43: name: CSI_PARENT_MODULE_NAME |
| `security/csi-master-data-management-service` | Commented out line 44: value: "security" |
| `security/csi-master-data-management-service` | Commented out line 45: - op: add |
| `security/csi-master-data-management-service` | Commented out line 46: path: /spec/template/spec/containers/0/env/- |
| `security/csi-master-data-management-service` | Commented out line 47: value: |
| `security/csi-master-data-management-service` | Commented out line 48: name: IS_INITIAL_DEPLOYMENT |
| `security/csi-master-data-management-service` | Commented out line 49: value: "true" |
| `security/securityiamcache` | Updated Deployment target name: infinispan-server -> securityiamcache |
| `twin-doctor/grafana-dashboard` | Updated Deployment target name: twin-doctor-grafana -> grafana-dashboard |
