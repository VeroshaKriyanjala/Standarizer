# DM-Initiator Update Log - Alibaba

Mode: LIVE

## Version Check

- base-utility-service-java-sev: `V4.0.2510_W1-4893_prod`
  - Threshold: `V4.0.2510_W1-4893_prod`
- csi-iam-service: `V4.0.2602_W2_108_prod`
  - Threshold: `V4.0.2510_W4_14_prod`
- **Conditions met: YES**

## Changes (168 total)

| Service | Change |
|---------|--------|
| `bloodbank/csi-java-bb-service` | Replaced commented Sync reference with commented DM-Initiator |
| `bloodbank/csi-java-bb-service` | Added new sync-presync/sync-postsync Job patches |
| `bloodbank/csi-java-bb-service` | Commented out line 23: - target: |
| `bloodbank/csi-java-bb-service` | Commented out line 24: group: batch |
| `bloodbank/csi-java-bb-service` | Commented out line 25: version: v1 |
| `bloodbank/csi-java-bb-service` | Commented out line 26: kind: Job |
| `bloodbank/csi-java-bb-service` | Commented out line 27: name: .* |
| `bloodbank/csi-java-bb-service` | Commented out line 28: patch: |- |
| `bloodbank/csi-java-bb-service` | Commented out line 29: - op: replace |
| `bloodbank/csi-java-bb-service` | Commented out line 30: path: /metadata/name |
| `bloodbank/csi-java-bb-service` | Commented out line 31: value: before-bloodbankjava |
| `bloodbank/csi-java-bb-service` | Commented out line 32: - op: add |
| `bloodbank/csi-java-bb-service` | Commented out line 33: path: /spec/template/spec/containers/0/env/- |
| `bloodbank/csi-java-bb-service` | Commented out line 34: value: |
| `bloodbank/csi-java-bb-service` | Commented out line 35: name: CSI_MODULENAME |
| `bloodbank/csi-java-bb-service` | Commented out line 36: value: "bb-bloodbankgui" |
| `bloodbank/csi-java-bb-service` | Commented out line 37: - op: add |
| `bloodbank/csi-java-bb-service` | Commented out line 38: path: /spec/template/spec/containers/0/env/- |
| `bloodbank/csi-java-bb-service` | Commented out line 39: value: |
| `bloodbank/csi-java-bb-service` | Commented out line 40: name: CSI_DATA_VERSION |
| `bloodbank/csi-java-bb-service` | Commented out line 41: value: "4.0.127.0" |
| `bloodbank/csi-java-bb-service` | Commented out line 42: - op: add |
| `bloodbank/csi-java-bb-service` | Commented out line 43: path: /spec/template/spec/containers/0/env/- |
| `bloodbank/csi-java-bb-service` | Commented out line 44: value: |
| `bloodbank/csi-java-bb-service` | Commented out line 45: name: CSI_PROJECT_NAME |
| `bloodbank/csi-java-bb-service` | Commented out line 46: value: "csi-java-bb-service" |
| `bloodbank/csi-java-bb-service` | Commented out line 47: - op: add |
| `bloodbank/csi-java-bb-service` | Commented out line 48: path: /spec/template/spec/containers/0/env/- |
| `bloodbank/csi-java-bb-service` | Commented out line 49: value: |
| `bloodbank/csi-java-bb-service` | Commented out line 50: name: CSI_MODULE_NAME |
| `bloodbank/csi-java-bb-service` | Commented out line 51: value: "bloodbankjava" |
| `bloodbank/csi-java-bb-service` | Commented out line 52: - op: add |
| `bloodbank/csi-java-bb-service` | Commented out line 53: path: /spec/template/spec/containers/0/env/- |
| `bloodbank/csi-java-bb-service` | Commented out line 54: value: |
| `bloodbank/csi-java-bb-service` | Commented out line 55: name: CSI_PARENT_MODULE_NAME |
| `bloodbank/csi-java-bb-service` | Commented out line 56: value: "bloodbank" |
| `empi/csi-empi-api` | Replaced Sync reference with DM-Initiator |
| `empi/csi-empi-api` | Added new sync-presync/sync-postsync Job patches |
| `empi/csi-empi-api` | Commented out line 50: - target: |
| `empi/csi-empi-api` | Commented out line 51: group: batch |
| `empi/csi-empi-api` | Commented out line 52: version: v1 |
| `empi/csi-empi-api` | Commented out line 53: kind: Job |
| `empi/csi-empi-api` | Commented out line 54: name: .* |
| `empi/csi-empi-api` | Commented out line 55: patch: |- |
| `empi/csi-empi-api` | Commented out line 56: - op: replace |
| `empi/csi-empi-api` | Commented out line 57: path: /metadata/name |
| `empi/csi-empi-api` | Commented out line 58: value: before-csi-empi-api |
| `empi/csi-empi-api` | Commented out line 59: namespace: vida-uat |
| `empi/csi-empi-api` | Commented out line 60: - op: add |
| `empi/csi-empi-api` | Commented out line 61: path: /spec/template/spec/containers/0/env/- |
| `empi/csi-empi-api` | Commented out line 62: value: |
| `empi/csi-empi-api` | Commented out line 63: name: CSI_MODULENAME |
| `empi/csi-empi-api` | Commented out line 64: value: "csi-empi-api" |
| `empi/csi-empi-api` | Commented out line 65: - op: add |
| `empi/csi-empi-api` | Commented out line 66: path: /spec/template/spec/containers/0/env/- |
| `empi/csi-empi-api` | Commented out line 67: value: |
| `empi/csi-empi-api` | Commented out line 68: name: CSI_DATA_VERSION |
| `empi/csi-empi-api` | Commented out line 69: value: "4.1.170.0" |
| `empi/csi-empi-api` | Commented out line 70: - op: add |
| `empi/csi-empi-api` | Commented out line 71: path: /spec/template/spec/containers/0/env/- |
| `empi/csi-empi-api` | Commented out line 72: value: |
| `empi/csi-empi-api` | Commented out line 73: name: CSI_PROJECT_NAME |
| `empi/csi-empi-api` | Commented out line 74: value: "csi-empi-api" |
| `empi/csi-empi-api` | Commented out line 75: - op: add |
| `empi/csi-empi-api` | Commented out line 76: path: /spec/template/spec/containers/0/env/- |
| `empi/csi-empi-api` | Commented out line 77: value: |
| `empi/csi-empi-api` | Commented out line 78: name: CSI_MODULE_NAME |
| `empi/csi-empi-api` | Commented out line 79: value: "csi-empi-api" |
| `empi/csi-empi-api` | Commented out line 80: - op: add |
| `empi/csi-empi-api` | Commented out line 81: path: /spec/template/spec/containers/0/env/- |
| `empi/csi-empi-api` | Commented out line 82: value: |
| `empi/csi-empi-api` | Commented out line 83: name: CSI_PARENT_MODULE_NAME |
| `empi/csi-empi-api` | Commented out line 84: value: "empi" |
| `empi/csi-empi-webui` | Replaced Sync reference with DM-Initiator |
| `empi/csi-empi-webui` | Added new sync-presync/sync-postsync Job patches |
| `empi/csi-empi-webui` | Commented out line 23: - target: |
| `empi/csi-empi-webui` | Commented out line 24: group: batch |
| `empi/csi-empi-webui` | Commented out line 25: version: v1 |
| `empi/csi-empi-webui` | Commented out line 26: kind: Job |
| `empi/csi-empi-webui` | Commented out line 27: name: .* |
| `empi/csi-empi-webui` | Commented out line 28: patch: |- |
| `empi/csi-empi-webui` | Commented out line 29: - op: replace |
| `empi/csi-empi-webui` | Commented out line 30: path: /metadata/name |
| `empi/csi-empi-webui` | Commented out line 31: value: before-csi-empi-ui |
| `empi/csi-empi-webui` | Commented out line 32: - op: add |
| `empi/csi-empi-webui` | Commented out line 33: path: /spec/template/spec/containers/0/env/- |
| `empi/csi-empi-webui` | Commented out line 34: value: |
| `empi/csi-empi-webui` | Commented out line 35: name: CSI_MODULENAME |
| `empi/csi-empi-webui` | Commented out line 36: value: "csi-empi-ui" |
| `empi/csi-empi-webui` | Commented out line 37: - op: add |
| `empi/csi-empi-webui` | Commented out line 38: path: /spec/template/spec/containers/0/env/- |
| `empi/csi-empi-webui` | Commented out line 39: value: |
| `empi/csi-empi-webui` | Commented out line 40: name: CSI_DATA_VERSION |
| `empi/csi-empi-webui` | Commented out line 41: value: "4.2.106.0" |
| `empi/csi-empi-webui` | Commented out line 42: - op: add |
| `empi/csi-empi-webui` | Commented out line 43: path: /spec/template/spec/containers/0/env/- |
| `empi/csi-empi-webui` | Commented out line 44: value: |
| `empi/csi-empi-webui` | Commented out line 45: name: CSI_PROJECT_NAME |
| `empi/csi-empi-webui` | Commented out line 46: value: "csi-empi-webui" |
| `empi/csi-empi-webui` | Commented out line 47: - op: add |
| `empi/csi-empi-webui` | Commented out line 48: path: /spec/template/spec/containers/0/env/- |
| `empi/csi-empi-webui` | Commented out line 49: value: |
| `empi/csi-empi-webui` | Commented out line 50: name: CSI_MODULE_NAME |
| `empi/csi-empi-webui` | Commented out line 51: value: "empiui" |
| `empi/csi-empi-webui` | Commented out line 52: - op: add |
| `empi/csi-empi-webui` | Commented out line 53: path: /spec/template/spec/containers/0/env/- |
| `empi/csi-empi-webui` | Commented out line 54: value: |
| `empi/csi-empi-webui` | Commented out line 55: name: CSI_PARENT_MODULE_NAME |
| `empi/csi-empi-webui` | Commented out line 56: value: "empi" |
| `integration/csi-ie-general` | Replaced Sync reference with DM-Initiator |
| `integration/csi-ie-general` | Added new sync-presync/sync-postsync Job patches |
| `integration/csi-ie-general` | Commented out line 29: - target: |
| `integration/csi-ie-general` | Commented out line 30: group: batch |
| `integration/csi-ie-general` | Commented out line 31: version: v1 |
| `integration/csi-ie-general` | Commented out line 32: kind: Job |
| `integration/csi-ie-general` | Commented out line 33: name: before |
| `integration/csi-ie-general` | Commented out line 34: patch: |- |
| `integration/csi-ie-general` | Commented out line 35: - op: replace |
| `integration/csi-ie-general` | Commented out line 36: path: /metadata/name |
| `integration/csi-ie-general` | Commented out line 37: value: before-csi-ie-general |
| `integration/csi-ie-general` | Commented out line 38: - op: add |
| `integration/csi-ie-general` | Commented out line 39: path: /spec/template/spec/containers/0/env/- |
| `integration/csi-ie-general` | Commented out line 40: value: |
| `integration/csi-ie-general` | Commented out line 41: name: CSI_PROJECT_NAME |
| `integration/csi-ie-general` | Commented out line 42: value: "csi-ie-general" |
| `integration/csi-ie-general` | Commented out line 43: - op: add |
| `integration/csi-ie-general` | Commented out line 44: path: /spec/template/spec/containers/0/env/- |
| `integration/csi-ie-general` | Commented out line 45: value: |
| `integration/csi-ie-general` | Commented out line 46: name: CSI_MODULE_NAME |
| `integration/csi-ie-general` | Commented out line 47: value: "csi-ie-general" |
| `integration/csi-ie-general` | Commented out line 48: - op: add |
| `integration/csi-ie-general` | Commented out line 49: path: /spec/template/spec/containers/0/env/- |
| `integration/csi-ie-general` | Commented out line 50: value: |
| `integration/csi-ie-general` | Commented out line 51: name: CSI_PARENT_MODULE_NAME |
| `integration/csi-ie-general` | Commented out line 52: value: "integration" |
| `pharmacy/phrbasebgjava` | Replaced Sync reference with DM-Initiator |
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
| `security/csi-master-data-management-service` | Commented out line 28: value: before-secmasterdata |
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
