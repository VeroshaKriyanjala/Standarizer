# DM-Initiator Update Log - WAVE1

Mode: LIVE

## Version Check

- base-utility-service-java-sev: `V4.0.2512_W4-174_prod`
  - Threshold: `V4.0.2510_W1-4893_prod`
- csi-iam-service: `V4.0.2602_W2_108_prod`
  - Threshold: `V4.0.2510_W4_14_prod`
- **Conditions met: YES**

## Changes (48 total)

| Service | Change |
|---------|--------|
| `base/configui` | Replaced Sync reference with DM-Initiator |
| `base/configui` | Updated Deployment target name: csi-config-ui -> configui |
| `base/facadpatientsnapshot` | Updated Deployment target name: csi-patient-snapshot-java-sev -> facadpatientsnapshot |
| `bloodbank/bb-donation_srv` | Updated Deployment target name: bb-donation-srv -> bb-donation_srv |
| `dms/dmsmiddleware` | Updated Deployment target name: document-management-middleware -> dmsmiddleware |
| `empi/empi-db-sync/overlays` | Updated Deployment target name: csi-empi-db-sync -> overlays |
| `notification/csi-vidaplus-external` | Updated Deployment target name: csi-net-ext -> csi-vidaplus-external |
| `pharmacy/phrbasebgjava` | Replaced Sync reference with DM-Initiator |
| `pharmacy/phrbasebgjava` | Updated Deployment target name: csi-phr-base-bgservice -> phrbasebgjava |
| `rms/csi-rms-morgue-java-service` | Replaced Sync reference with DM-Initiator |
| `rms/csi-rms-morgue-java-service` | Added new sync-presync/sync-postsync Job patches |
| `rms/csi-rms-morgue-java-service` | Commented out line 24: - target: |
| `rms/csi-rms-morgue-java-service` | Commented out line 25: group: batch |
| `rms/csi-rms-morgue-java-service` | Commented out line 26: version: v1 |
| `rms/csi-rms-morgue-java-service` | Commented out line 27: kind: Job |
| `rms/csi-rms-morgue-java-service` | Commented out line 28: name: .* |
| `rms/csi-rms-morgue-java-service` | Commented out line 29: patch: | |
| `rms/csi-rms-morgue-java-service` | Commented out line 30: - op: replace |
| `rms/csi-rms-morgue-java-service` | Commented out line 31: path: /metadata/name |
| `rms/csi-rms-morgue-java-service` | Commented out line 32: value: before-csi-rms-morgue |
| `rms/csi-rms-morgue-java-service` | Commented out line 33: namespace: moh-prod |
| `rms/csi-rms-morgue-java-service` | Commented out line 34: - op: add |
| `rms/csi-rms-morgue-java-service` | Commented out line 35: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-morgue-java-service` | Commented out line 36: value: |
| `rms/csi-rms-morgue-java-service` | Commented out line 37: name: CSI_MODULENAME |
| `rms/csi-rms-morgue-java-service` | Commented out line 38: value: "csi-rms-morgue" |
| `rms/csi-rms-morgue-java-service` | Commented out line 39: - op: add |
| `rms/csi-rms-morgue-java-service` | Commented out line 40: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-morgue-java-service` | Commented out line 41: value: |
| `rms/csi-rms-morgue-java-service` | Commented out line 42: name: CSI_DATA_VERSION |
| `rms/csi-rms-morgue-java-service` | Commented out line 43: value: "4.0.127.0" |
| `rms/csi-rms-morgue-java-service` | Commented out line 44: - op: add |
| `rms/csi-rms-morgue-java-service` | Commented out line 45: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-morgue-java-service` | Commented out line 46: value: |
| `rms/csi-rms-morgue-java-service` | Commented out line 47: name: CSI_PROJECT_NAME |
| `rms/csi-rms-morgue-java-service` | Commented out line 48: value: "csi-rms-morgue-java-service" |
| `rms/csi-rms-morgue-java-service` | Commented out line 49: - op: add |
| `rms/csi-rms-morgue-java-service` | Commented out line 50: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-morgue-java-service` | Commented out line 51: value: |
| `rms/csi-rms-morgue-java-service` | Commented out line 52: name: CSI_MODULE_NAME |
| `rms/csi-rms-morgue-java-service` | Commented out line 53: value: "rmsmorgue" |
| `rms/csi-rms-morgue-java-service` | Commented out line 54: - op: add |
| `rms/csi-rms-morgue-java-service` | Commented out line 55: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-morgue-java-service` | Commented out line 56: value: |
| `rms/csi-rms-morgue-java-service` | Commented out line 57: name: CSI_PARENT_MODULE_NAME |
| `rms/csi-rms-morgue-java-service` | Commented out line 58: value: "rms" |
| `security/securityiamcache` | Updated Deployment target name: infinispan-server -> securityiamcache |
| `support-portal/support-portal` | Updated Deployment target name: support-portal -> csi-support-portal |
