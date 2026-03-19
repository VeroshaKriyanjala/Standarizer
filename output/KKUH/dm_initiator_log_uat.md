# DM-Initiator Update Log - KKUH

Mode: LIVE

## Version Check

- base-utility-service-java-sev: `V4.0.2512_W4-174_prod`
  - Threshold: `V4.0.2510_W1-4893_prod`
- csi-iam-service: `V4.0.2602_W2_108_prod`
  - Threshold: `V4.0.2510_W4_14_prod`
- **Conditions met: YES**

## Changes (2618 total)

| Service | Change |
|---------|--------|
| `base/base-utility-service-java-sev` | Replaced Sync reference with DM-Initiator |
| `base/base-utility-service-java-sev` | Added new sync-presync/sync-postsync Job patches |
| `base/base-utility-service-java-sev` | Commented out line 19: - target: |
| `base/base-utility-service-java-sev` | Commented out line 20: group: batch |
| `base/base-utility-service-java-sev` | Commented out line 21: version: v1 |
| `base/base-utility-service-java-sev` | Commented out line 22: kind: Job |
| `base/base-utility-service-java-sev` | Commented out line 23: name: .* |
| `base/base-utility-service-java-sev` | Commented out line 24: patch: |- |
| `base/base-utility-service-java-sev` | Commented out line 25: - op: replace |
| `base/base-utility-service-java-sev` | Commented out line 26: path: /metadata/name |
| `base/base-utility-service-java-sev` | Commented out line 27: value: before-csi-base-utility |
| `base/base-utility-service-java-sev` | Commented out line 28: namespace: moh-uat |
| `base/base-utility-service-java-sev` | Commented out line 29: - op: add |
| `base/base-utility-service-java-sev` | Commented out line 30: path: /spec/template/spec/containers/0/env/- |
| `base/base-utility-service-java-sev` | Commented out line 31: value: |
| `base/base-utility-service-java-sev` | Commented out line 32: name: CSI_MODULENAME |
| `base/base-utility-service-java-sev` | Commented out line 33: value: "csi-base-utility" |
| `base/base-utility-service-java-sev` | Commented out line 34: - op: add |
| `base/base-utility-service-java-sev` | Commented out line 35: path: /spec/template/spec/containers/0/env/- |
| `base/base-utility-service-java-sev` | Commented out line 36: value: |
| `base/base-utility-service-java-sev` | Commented out line 37: name: CSI_DATA_VERSION |
| `base/base-utility-service-java-sev` | Commented out line 38: value: "4.0.161.0" |
| `base/base-utility-service-java-sev` | Commented out line 39: - op: add |
| `base/base-utility-service-java-sev` | Commented out line 40: path: /spec/template/spec/containers/0/env/- |
| `base/base-utility-service-java-sev` | Commented out line 41: value: |
| `base/base-utility-service-java-sev` | Commented out line 42: name: CSI_PROJECT_NAME |
| `base/base-utility-service-java-sev` | Commented out line 43: value: "base-utility-service-java-sev" |
| `base/base-utility-service-java-sev` | Commented out line 44: - op: add |
| `base/base-utility-service-java-sev` | Commented out line 45: path: /spec/template/spec/containers/0/env/- |
| `base/base-utility-service-java-sev` | Commented out line 46: value: |
| `base/base-utility-service-java-sev` | Commented out line 47: name: CSI_MODULE_NAME |
| `base/base-utility-service-java-sev` | Commented out line 48: value: "base-utility-service-java-sev" |
| `base/base-utility-service-java-sev` | Commented out line 49: - op: add |
| `base/base-utility-service-java-sev` | Commented out line 50: path: /spec/template/spec/containers/0/env/- |
| `base/base-utility-service-java-sev` | Commented out line 51: value: |
| `base/base-utility-service-java-sev` | Commented out line 52: name: CSI_PARENT_MODULE_NAME |
| `base/base-utility-service-java-sev` | Commented out line 53: value: "base" |
| `base/csi-uif-settings` | Replaced Sync reference with DM-Initiator |
| `base/csi-uif-settings` | Added new sync-presync/sync-postsync Job patches |
| `base/csi-uif-settings` | Commented out line 58: - target: |
| `base/csi-uif-settings` | Commented out line 59: group: batch |
| `base/csi-uif-settings` | Commented out line 60: version: v1 |
| `base/csi-uif-settings` | Commented out line 61: kind: Job |
| `base/csi-uif-settings` | Commented out line 62: name: before |
| `base/csi-uif-settings` | Commented out line 63: patch: |- |
| `base/csi-uif-settings` | Commented out line 64: - op: replace |
| `base/csi-uif-settings` | Commented out line 65: path: /metadata/name |
| `base/csi-uif-settings` | Commented out line 66: value: before-csi-config-ui |
| `base/csi-uif-settings` | Commented out line 67: namespace: moh-uat |
| `base/csi-uif-settings` | Commented out line 68: - op: add |
| `base/csi-uif-settings` | Commented out line 69: path: /spec/template/spec/containers/0/env/- |
| `base/csi-uif-settings` | Commented out line 70: value: |
| `base/csi-uif-settings` | Commented out line 71: name: CSI_MODULENAME |
| `base/csi-uif-settings` | Commented out line 72: value: "csi-config-ui" |
| `base/csi-uif-settings` | Commented out line 73: - op: add |
| `base/csi-uif-settings` | Commented out line 74: path: /spec/template/spec/containers/0/env/- |
| `base/csi-uif-settings` | Commented out line 75: value: |
| `base/csi-uif-settings` | Commented out line 76: name: CSI_DATA_VERSION |
| `base/csi-uif-settings` | Commented out line 77: value: "4.1.170.0" |
| `base/csi-uif-settings` | Commented out line 78: - op: add |
| `base/csi-uif-settings` | Commented out line 79: path: /spec/template/spec/containers/0/env/- |
| `base/csi-uif-settings` | Commented out line 80: value: |
| `base/csi-uif-settings` | Commented out line 81: name: CSI_PROJECT_NAME |
| `base/csi-uif-settings` | Commented out line 82: value: "csi.uif.settings" |
| `base/csi-uif-settings` | Commented out line 83: - op: add |
| `base/csi-uif-settings` | Commented out line 84: path: /spec/template/spec/containers/0/env/- |
| `base/csi-uif-settings` | Commented out line 85: value: |
| `base/csi-uif-settings` | Commented out line 86: name: CSI_MODULE_NAME |
| `base/csi-uif-settings` | Commented out line 87: value: "csi-uif-settings" |
| `base/csi-uif-settings` | Commented out line 88: - op: add |
| `base/csi-uif-settings` | Commented out line 89: path: /spec/template/spec/containers/0/env/- |
| `base/csi-uif-settings` | Commented out line 90: value: |
| `base/csi-uif-settings` | Commented out line 91: name: CSI_PARENT_MODULE_NAME |
| `base/csi-uif-settings` | Commented out line 92: value: "base" |
| `base/facadpatientsnapshot` | Updated Deployment target name: csi-patient-snapshot-java-sev -> facadpatientsnapshot |
| `base/medispan` | Updated Deployment target name: csi-net-medispan -> medispan |
| `base/medispan/overlays/PROD` | Updated Deployment target name: csi-net-medispan -> PROD |
| `base/medispan/overlays/UAT` | Updated Deployment target name: csi-net-medispan -> UAT |
| `billing/csi-bm-approval-java-service` | Replaced Sync reference with DM-Initiator |
| `billing/csi-bm-approval-java-service` | Added new sync-presync/sync-postsync Job patches |
| `billing/csi-bm-approval-java-service` | Commented out line 23: - target: |
| `billing/csi-bm-approval-java-service` | Commented out line 24: group: batch |
| `billing/csi-bm-approval-java-service` | Commented out line 25: version: v1 |
| `billing/csi-bm-approval-java-service` | Commented out line 26: kind: Job |
| `billing/csi-bm-approval-java-service` | Commented out line 27: name: .* |
| `billing/csi-bm-approval-java-service` | Commented out line 28: patch: |- |
| `billing/csi-bm-approval-java-service` | Commented out line 29: - op: replace |
| `billing/csi-bm-approval-java-service` | Commented out line 30: path: /metadata/name |
| `billing/csi-bm-approval-java-service` | Commented out line 31: value: before-bmbillingapprovaljava |
| `billing/csi-bm-approval-java-service` | Commented out line 32: namespace: moh-uat |
| `billing/csi-bm-approval-java-service` | Commented out line 33: - op: add |
| `billing/csi-bm-approval-java-service` | Commented out line 34: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-approval-java-service` | Commented out line 35: value: |
| `billing/csi-bm-approval-java-service` | Commented out line 36: name: CSI_MODULENAME |
| `billing/csi-bm-approval-java-service` | Commented out line 37: value: "csi-bm-approval-java-service" |
| `billing/csi-bm-approval-java-service` | Commented out line 38: - op: add |
| `billing/csi-bm-approval-java-service` | Commented out line 39: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-approval-java-service` | Commented out line 40: value: |
| `billing/csi-bm-approval-java-service` | Commented out line 41: name: CSI_DATA_VERSION |
| `billing/csi-bm-approval-java-service` | Commented out line 42: value: "4.3.234.0" |
| `billing/csi-bm-approval-java-service` | Commented out line 43: - op: add |
| `billing/csi-bm-approval-java-service` | Commented out line 44: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-approval-java-service` | Commented out line 45: value: |
| `billing/csi-bm-approval-java-service` | Commented out line 46: name: CSI_PROJECT_NAME |
| `billing/csi-bm-approval-java-service` | Commented out line 47: value: "csi-bm-approval-java-service" |
| `billing/csi-bm-approval-java-service` | Commented out line 48: - op: add |
| `billing/csi-bm-approval-java-service` | Commented out line 49: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-approval-java-service` | Commented out line 50: value: |
| `billing/csi-bm-approval-java-service` | Commented out line 51: name: CSI_MODULE_NAME |
| `billing/csi-bm-approval-java-service` | Commented out line 52: value: "csi-bm-approval-java-service" |
| `billing/csi-bm-approval-java-service` | Commented out line 53: - op: add |
| `billing/csi-bm-approval-java-service` | Commented out line 54: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-approval-java-service` | Commented out line 55: value: |
| `billing/csi-bm-approval-java-service` | Commented out line 56: name: CSI_PARENT_MODULE_NAME |
| `billing/csi-bm-approval-java-service` | Commented out line 57: value: "billing" |
| `billing/csi-bm-approval-ui` | Replaced Sync reference with DM-Initiator |
| `billing/csi-bm-approval-ui` | Added new sync-presync/sync-postsync Job patches |
| `billing/csi-bm-approval-ui` | Commented out line 23: - target: |
| `billing/csi-bm-approval-ui` | Commented out line 24: group: batch |
| `billing/csi-bm-approval-ui` | Commented out line 25: version: v1 |
| `billing/csi-bm-approval-ui` | Commented out line 26: kind: Job |
| `billing/csi-bm-approval-ui` | Commented out line 27: name: .* |
| `billing/csi-bm-approval-ui` | Commented out line 28: patch: |- |
| `billing/csi-bm-approval-ui` | Commented out line 29: - op: replace |
| `billing/csi-bm-approval-ui` | Commented out line 30: path: /metadata/name |
| `billing/csi-bm-approval-ui` | Commented out line 31: value: before-bmapprovalui |
| `billing/csi-bm-approval-ui` | Commented out line 32: namespace: moh-uat |
| `billing/csi-bm-approval-ui` | Commented out line 33: - op: add |
| `billing/csi-bm-approval-ui` | Commented out line 34: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-approval-ui` | Commented out line 35: value: |
| `billing/csi-bm-approval-ui` | Commented out line 36: name: CSI_MODULENAME |
| `billing/csi-bm-approval-ui` | Commented out line 37: value: "csi-bm-approval-ui" |
| `billing/csi-bm-approval-ui` | Commented out line 38: - op: add |
| `billing/csi-bm-approval-ui` | Commented out line 39: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-approval-ui` | Commented out line 40: value: |
| `billing/csi-bm-approval-ui` | Commented out line 41: name: CSI_DATA_VERSION |
| `billing/csi-bm-approval-ui` | Commented out line 42: value: "4.5.252.0" |
| `billing/csi-bm-approval-ui` | Commented out line 43: - op: add |
| `billing/csi-bm-approval-ui` | Commented out line 44: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-approval-ui` | Commented out line 45: value: |
| `billing/csi-bm-approval-ui` | Commented out line 46: name: CSI_PROJECT_NAME |
| `billing/csi-bm-approval-ui` | Commented out line 47: value: "csi-approval-ui" |
| `billing/csi-bm-approval-ui` | Commented out line 48: - op: add |
| `billing/csi-bm-approval-ui` | Commented out line 49: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-approval-ui` | Commented out line 50: value: |
| `billing/csi-bm-approval-ui` | Commented out line 51: name: CSI_MODULE_NAME |
| `billing/csi-bm-approval-ui` | Commented out line 52: value: "csi-bm-approval-ui" |
| `billing/csi-bm-approval-ui` | Commented out line 53: - op: add |
| `billing/csi-bm-approval-ui` | Commented out line 54: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-approval-ui` | Commented out line 55: value: |
| `billing/csi-bm-approval-ui` | Commented out line 56: name: CSI_PARENT_MODULE_NAME |
| `billing/csi-bm-approval-ui` | Commented out line 57: value: "billing" |
| `billing/csi-bm-billing-java-service` | Replaced Sync reference with DM-Initiator |
| `billing/csi-bm-billing-java-service` | Added new sync-presync/sync-postsync Job patches |
| `billing/csi-bm-billing-java-service` | Commented out line 23: - target: |
| `billing/csi-bm-billing-java-service` | Commented out line 24: group: batch |
| `billing/csi-bm-billing-java-service` | Commented out line 25: version: v1 |
| `billing/csi-bm-billing-java-service` | Commented out line 26: kind: Job |
| `billing/csi-bm-billing-java-service` | Commented out line 27: name: .* |
| `billing/csi-bm-billing-java-service` | Commented out line 28: patch: |- |
| `billing/csi-bm-billing-java-service` | Commented out line 29: - op: replace |
| `billing/csi-bm-billing-java-service` | Commented out line 30: path: /metadata/name |
| `billing/csi-bm-billing-java-service` | Commented out line 31: value: before-bmbillingjava |
| `billing/csi-bm-billing-java-service` | Commented out line 32: namespace: moh-uat |
| `billing/csi-bm-billing-java-service` | Commented out line 33: - op: add |
| `billing/csi-bm-billing-java-service` | Commented out line 34: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-billing-java-service` | Commented out line 35: value: |
| `billing/csi-bm-billing-java-service` | Commented out line 36: name: CSI_MODULENAME |
| `billing/csi-bm-billing-java-service` | Commented out line 37: value: "csi-bm-billing-java-service" |
| `billing/csi-bm-billing-java-service` | Commented out line 38: - op: add |
| `billing/csi-bm-billing-java-service` | Commented out line 39: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-billing-java-service` | Commented out line 40: value: |
| `billing/csi-bm-billing-java-service` | Commented out line 41: name: CSI_DATA_VERSION |
| `billing/csi-bm-billing-java-service` | Commented out line 42: value: "4.5.502.0" |
| `billing/csi-bm-billing-java-service` | Commented out line 43: - op: add |
| `billing/csi-bm-billing-java-service` | Commented out line 44: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-billing-java-service` | Commented out line 45: value: |
| `billing/csi-bm-billing-java-service` | Commented out line 46: name: CSI_PROJECT_NAME |
| `billing/csi-bm-billing-java-service` | Commented out line 47: value: "csi-bm-billing-java-service" |
| `billing/csi-bm-billing-java-service` | Commented out line 48: - op: add |
| `billing/csi-bm-billing-java-service` | Commented out line 49: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-billing-java-service` | Commented out line 50: value: |
| `billing/csi-bm-billing-java-service` | Commented out line 51: name: CSI_MODULE_NAME |
| `billing/csi-bm-billing-java-service` | Commented out line 52: value: "csi-bm-billing-java-service" |
| `billing/csi-bm-billing-java-service` | Commented out line 53: - op: add |
| `billing/csi-bm-billing-java-service` | Commented out line 54: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-billing-java-service` | Commented out line 55: value: |
| `billing/csi-bm-billing-java-service` | Commented out line 56: name: CSI_PARENT_MODULE_NAME |
| `billing/csi-bm-billing-java-service` | Commented out line 57: value: "billing" |
| `billing/csi-bm-billing-ui` | Replaced Sync reference with DM-Initiator |
| `billing/csi-bm-billing-ui` | Added new sync-presync/sync-postsync Job patches |
| `billing/csi-bm-billing-ui` | Commented out line 23: - target: |
| `billing/csi-bm-billing-ui` | Commented out line 24: group: batch |
| `billing/csi-bm-billing-ui` | Commented out line 25: version: v1 |
| `billing/csi-bm-billing-ui` | Commented out line 26: kind: Job |
| `billing/csi-bm-billing-ui` | Commented out line 27: name: .* |
| `billing/csi-bm-billing-ui` | Commented out line 28: patch: |- |
| `billing/csi-bm-billing-ui` | Commented out line 29: - op: replace |
| `billing/csi-bm-billing-ui` | Commented out line 30: path: /metadata/name |
| `billing/csi-bm-billing-ui` | Commented out line 31: value: before-billingmasterui |
| `billing/csi-bm-billing-ui` | Commented out line 32: namespace: moh-uat |
| `billing/csi-bm-billing-ui` | Commented out line 33: - op: add |
| `billing/csi-bm-billing-ui` | Commented out line 34: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-billing-ui` | Commented out line 35: value: |
| `billing/csi-bm-billing-ui` | Commented out line 36: name: CSI_MODULENAME |
| `billing/csi-bm-billing-ui` | Commented out line 37: value: "csi-bm-billing-ui" |
| `billing/csi-bm-billing-ui` | Commented out line 38: - op: add |
| `billing/csi-bm-billing-ui` | Commented out line 39: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-billing-ui` | Commented out line 40: value: |
| `billing/csi-bm-billing-ui` | Commented out line 41: name: CSI_DATA_VERSION |
| `billing/csi-bm-billing-ui` | Commented out line 42: value: "4.5.252.0" |
| `billing/csi-bm-billing-ui` | Commented out line 43: - op: add |
| `billing/csi-bm-billing-ui` | Commented out line 44: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-billing-ui` | Commented out line 45: value: |
| `billing/csi-bm-billing-ui` | Commented out line 46: name: CSI_PROJECT_NAME |
| `billing/csi-bm-billing-ui` | Commented out line 47: value: "csi-billing-ui" |
| `billing/csi-bm-billing-ui` | Commented out line 48: - op: add |
| `billing/csi-bm-billing-ui` | Commented out line 49: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-billing-ui` | Commented out line 50: value: |
| `billing/csi-bm-billing-ui` | Commented out line 51: name: CSI_MODULE_NAME |
| `billing/csi-bm-billing-ui` | Commented out line 52: value: "csi-bm-billing-ui" |
| `billing/csi-bm-billing-ui` | Commented out line 53: - op: add |
| `billing/csi-bm-billing-ui` | Commented out line 54: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-billing-ui` | Commented out line 55: value: |
| `billing/csi-bm-billing-ui` | Commented out line 56: name: CSI_PARENT_MODULE_NAME |
| `billing/csi-bm-billing-ui` | Commented out line 57: value: "billing" |
| `billing/csi-bm-inte-bridge-java-service` | Replaced Sync reference with DM-Initiator |
| `billing/csi-bm-inte-bridge-java-service` | Added new sync-presync/sync-postsync Job patches |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 27: - target: |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 28: group: batch |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 29: version: v1 |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 30: kind: Job |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 31: name: .* |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 32: patch: |- |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 33: - op: replace |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 34: path: /metadata/name |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 35: value: before-csi-bm-inte-bridge-java-service |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 36: namespace: moh-uat |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 37: - op: add |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 38: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 39: value: |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 40: name: CSI_MODULENAME |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 41: value: "csi-bm-invoice-java-service" |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 42: - op: add |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 43: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 44: value: |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 45: name: CSI_DATA_VERSION |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 46: value: "4.2.502.0" |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 47: - op: add |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 48: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 49: value: |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 50: name: CSI_PROJECT_NAME |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 51: value: "csi-bm-inte-bridge-java-service" |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 52: - op: add |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 53: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 54: value: |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 55: name: CSI_MODULE_NAME |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 56: value: "csi-bm-inte-bridge-java-service" |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 57: - op: add |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 58: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 59: value: |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 60: name: CSI_PARENT_MODULE_NAME |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 61: value: "billing" |
| `billing/csi-bm-invoice-java-service` | Replaced Sync reference with DM-Initiator |
| `billing/csi-bm-invoice-java-service` | Added new sync-presync/sync-postsync Job patches |
| `billing/csi-bm-invoice-java-service` | Commented out line 23: - target: |
| `billing/csi-bm-invoice-java-service` | Commented out line 24: group: batch |
| `billing/csi-bm-invoice-java-service` | Commented out line 25: version: v1 |
| `billing/csi-bm-invoice-java-service` | Commented out line 26: kind: Job |
| `billing/csi-bm-invoice-java-service` | Commented out line 27: name: .* |
| `billing/csi-bm-invoice-java-service` | Commented out line 28: patch: |- |
| `billing/csi-bm-invoice-java-service` | Commented out line 29: - op: replace |
| `billing/csi-bm-invoice-java-service` | Commented out line 30: path: /metadata/name |
| `billing/csi-bm-invoice-java-service` | Commented out line 31: value: before-bmbillinginvoicejava |
| `billing/csi-bm-invoice-java-service` | Commented out line 32: namespace: moh-uat |
| `billing/csi-bm-invoice-java-service` | Commented out line 33: - op: add |
| `billing/csi-bm-invoice-java-service` | Commented out line 34: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-invoice-java-service` | Commented out line 35: value: |
| `billing/csi-bm-invoice-java-service` | Commented out line 36: name: CSI_MODULENAME |
| `billing/csi-bm-invoice-java-service` | Commented out line 37: value: "csi-bm-invoice-java-service" |
| `billing/csi-bm-invoice-java-service` | Commented out line 38: - op: add |
| `billing/csi-bm-invoice-java-service` | Commented out line 39: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-invoice-java-service` | Commented out line 40: value: |
| `billing/csi-bm-invoice-java-service` | Commented out line 41: name: CSI_DATA_VERSION |
| `billing/csi-bm-invoice-java-service` | Commented out line 42: value: "4.2.1298.0" |
| `billing/csi-bm-invoice-java-service` | Commented out line 43: - op: add |
| `billing/csi-bm-invoice-java-service` | Commented out line 44: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-invoice-java-service` | Commented out line 45: value: |
| `billing/csi-bm-invoice-java-service` | Commented out line 46: name: CSI_PROJECT_NAME |
| `billing/csi-bm-invoice-java-service` | Commented out line 47: value: "csi-bm-invoice-java-service" |
| `billing/csi-bm-invoice-java-service` | Commented out line 48: - op: add |
| `billing/csi-bm-invoice-java-service` | Commented out line 49: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-invoice-java-service` | Commented out line 50: value: |
| `billing/csi-bm-invoice-java-service` | Commented out line 51: name: CSI_MODULE_NAME |
| `billing/csi-bm-invoice-java-service` | Commented out line 52: value: "csi-bm-invoice-java-service" |
| `billing/csi-bm-invoice-java-service` | Commented out line 53: - op: add |
| `billing/csi-bm-invoice-java-service` | Commented out line 54: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-invoice-java-service` | Commented out line 55: value: |
| `billing/csi-bm-invoice-java-service` | Commented out line 56: name: CSI_PARENT_MODULE_NAME |
| `billing/csi-bm-invoice-java-service` | Commented out line 57: value: "billing" |
| `billing/csi-bm-invoice-ui` | Replaced Sync reference with DM-Initiator |
| `billing/csi-bm-invoice-ui` | Added new sync-presync/sync-postsync Job patches |
| `billing/csi-bm-invoice-ui` | Commented out line 24: - target: |
| `billing/csi-bm-invoice-ui` | Commented out line 25: group: batch |
| `billing/csi-bm-invoice-ui` | Commented out line 26: version: v1 |
| `billing/csi-bm-invoice-ui` | Commented out line 27: kind: Job |
| `billing/csi-bm-invoice-ui` | Commented out line 28: name: .* |
| `billing/csi-bm-invoice-ui` | Commented out line 29: patch: |- |
| `billing/csi-bm-invoice-ui` | Commented out line 30: - op: replace |
| `billing/csi-bm-invoice-ui` | Commented out line 31: path: /metadata/name |
| `billing/csi-bm-invoice-ui` | Commented out line 32: value: before-csi-bm-invoice-ui |
| `billing/csi-bm-invoice-ui` | Commented out line 33: namespace: moh-uat |
| `billing/csi-bm-invoice-ui` | Commented out line 34: - op: add |
| `billing/csi-bm-invoice-ui` | Commented out line 35: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-invoice-ui` | Commented out line 36: value: |
| `billing/csi-bm-invoice-ui` | Commented out line 37: name: CSI_PROJECT_NAME |
| `billing/csi-bm-invoice-ui` | Commented out line 38: value: "csi-bm-invoice-ui" |
| `billing/csi-bm-invoice-ui` | Commented out line 39: - op: add |
| `billing/csi-bm-invoice-ui` | Commented out line 40: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-invoice-ui` | Commented out line 41: value: |
| `billing/csi-bm-invoice-ui` | Commented out line 42: name: CSI_PROJECT_NAME |
| `billing/csi-bm-invoice-ui` | Commented out line 43: value: "csi-bm-invoice-ui" |
| `billing/csi-bm-invoice-ui` | Commented out line 44: - op: add |
| `billing/csi-bm-invoice-ui` | Commented out line 45: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-invoice-ui` | Commented out line 46: value: |
| `billing/csi-bm-invoice-ui` | Commented out line 47: name: CSI_MODULE_NAME |
| `billing/csi-bm-invoice-ui` | Commented out line 48: value: "csi-bm-invoice-ui" |
| `billing/csi-bm-invoice-ui` | Commented out line 49: - op: add |
| `billing/csi-bm-invoice-ui` | Commented out line 50: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-invoice-ui` | Commented out line 51: value: |
| `billing/csi-bm-invoice-ui` | Commented out line 52: name: CSI_PARENT_MODULE_NAME |
| `billing/csi-bm-invoice-ui` | Commented out line 53: value: "billing" |
| `billing/csi-bm-promotion-java-service` | Replaced Sync reference with DM-Initiator |
| `billing/csi-bm-promotion-java-service` | Added new sync-presync/sync-postsync Job patches |
| `billing/csi-bm-promotion-java-service` | Commented out line 25: - target: |
| `billing/csi-bm-promotion-java-service` | Commented out line 26: group: batch |
| `billing/csi-bm-promotion-java-service` | Commented out line 27: version: v1 |
| `billing/csi-bm-promotion-java-service` | Commented out line 28: kind: Job |
| `billing/csi-bm-promotion-java-service` | Commented out line 29: name: .* |
| `billing/csi-bm-promotion-java-service` | Commented out line 30: patch: |- |
| `billing/csi-bm-promotion-java-service` | Commented out line 31: - op: replace |
| `billing/csi-bm-promotion-java-service` | Commented out line 32: path: /metadata/name |
| `billing/csi-bm-promotion-java-service` | Commented out line 33: value: before-csi-bm-promotion-java-service |
| `billing/csi-bm-promotion-java-service` | Commented out line 34: - op: add |
| `billing/csi-bm-promotion-java-service` | Commented out line 35: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-promotion-java-service` | Commented out line 36: value: |
| `billing/csi-bm-promotion-java-service` | Commented out line 37: name: CSI_MODULENAME |
| `billing/csi-bm-promotion-java-service` | Commented out line 38: value: "csi-bm-promotion-java-service" |
| `billing/csi-bm-promotion-java-service` | Commented out line 39: - op: add |
| `billing/csi-bm-promotion-java-service` | Commented out line 40: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-promotion-java-service` | Commented out line 41: value: |
| `billing/csi-bm-promotion-java-service` | Commented out line 42: name: CSI_DATA_VERSION |
| `billing/csi-bm-promotion-java-service` | Commented out line 43: value: "4.2.502.0" |
| `billing/csi-bm-promotion-java-service` | Commented out line 44: - op: add |
| `billing/csi-bm-promotion-java-service` | Commented out line 45: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-promotion-java-service` | Commented out line 46: value: |
| `billing/csi-bm-promotion-java-service` | Commented out line 47: name: CSI_PROJECT_NAME |
| `billing/csi-bm-promotion-java-service` | Commented out line 48: value: "csi-bm-promotion-java-service" |
| `billing/csi-bm-promotion-java-service` | Commented out line 49: - op: add |
| `billing/csi-bm-promotion-java-service` | Commented out line 50: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-promotion-java-service` | Commented out line 51: value: |
| `billing/csi-bm-promotion-java-service` | Commented out line 52: name: CSI_MODULE_NAME |
| `billing/csi-bm-promotion-java-service` | Commented out line 53: value: "csi-bm-promotion-java-service" |
| `billing/csi-bm-promotion-java-service` | Commented out line 54: - op: add |
| `billing/csi-bm-promotion-java-service` | Commented out line 55: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-promotion-java-service` | Commented out line 56: value: |
| `billing/csi-bm-promotion-java-service` | Commented out line 57: name: CSI_PARENT_MODULE_NAME |
| `billing/csi-bm-promotion-java-service` | Commented out line 58: value: "billing" |
| `bloodbank/bb-bloodbankgui` | Replaced commented Sync reference with commented DM-Initiator |
| `bloodbank/bb-bloodbankgui` | Added new sync-presync/sync-postsync Job patches |
| `bloodbank/bb-bloodbankgui` | Commented out line 23: - target: |
| `bloodbank/bb-bloodbankgui` | Commented out line 24: group: batch |
| `bloodbank/bb-bloodbankgui` | Commented out line 25: version: v1 |
| `bloodbank/bb-bloodbankgui` | Commented out line 26: kind: Job |
| `bloodbank/bb-bloodbankgui` | Commented out line 27: name: .* |
| `bloodbank/bb-bloodbankgui` | Commented out line 28: patch: |- |
| `bloodbank/bb-bloodbankgui` | Commented out line 29: - op: replace |
| `bloodbank/bb-bloodbankgui` | Commented out line 30: path: /metadata/name |
| `bloodbank/bb-bloodbankgui` | Commented out line 31: value: before-bloodbankui |
| `bloodbank/bb-bloodbankgui` | Commented out line 32: namespace: moh-uat |
| `bloodbank/bb-bloodbankgui` | Commented out line 33: - op: add |
| `bloodbank/bb-bloodbankgui` | Commented out line 34: path: /spec/template/spec/containers/0/env/- |
| `bloodbank/bb-bloodbankgui` | Commented out line 35: value: |
| `bloodbank/bb-bloodbankgui` | Commented out line 36: name: CSI_MODULENAME |
| `bloodbank/bb-bloodbankgui` | Commented out line 37: value: "bb-bloodbankgui" |
| `bloodbank/bb-bloodbankgui` | Commented out line 38: - op: add |
| `bloodbank/bb-bloodbankgui` | Commented out line 39: path: /spec/template/spec/containers/0/env/- |
| `bloodbank/bb-bloodbankgui` | Commented out line 40: value: |
| `bloodbank/bb-bloodbankgui` | Commented out line 41: name: CSI_DATA_VERSION |
| `bloodbank/bb-bloodbankgui` | Commented out line 42: value: "4.1.56.0" |
| `bloodbank/bb-bloodbankgui` | Commented out line 43: - op: add |
| `bloodbank/bb-bloodbankgui` | Commented out line 44: path: /spec/template/spec/containers/0/env/- |
| `bloodbank/bb-bloodbankgui` | Commented out line 45: value: |
| `bloodbank/bb-bloodbankgui` | Commented out line 46: name: CSI_PROJECT_NAME |
| `bloodbank/bb-bloodbankgui` | Commented out line 47: value: "bb-bloodbankgui" |
| `bloodbank/bb-bloodbankgui` | Commented out line 48: - op: add |
| `bloodbank/bb-bloodbankgui` | Commented out line 49: path: /spec/template/spec/containers/0/env/- |
| `bloodbank/bb-bloodbankgui` | Commented out line 50: value: |
| `bloodbank/bb-bloodbankgui` | Commented out line 51: name: CSI_MODULE_NAME |
| `bloodbank/bb-bloodbankgui` | Commented out line 52: value: "bb-bloodbankgui" |
| `bloodbank/bb-bloodbankgui` | Commented out line 53: - op: add |
| `bloodbank/bb-bloodbankgui` | Commented out line 54: path: /spec/template/spec/containers/0/env/- |
| `bloodbank/bb-bloodbankgui` | Commented out line 55: value: |
| `bloodbank/bb-bloodbankgui` | Commented out line 56: name: CSI_PARENT_MODULE_NAME |
| `bloodbank/bb-bloodbankgui` | Commented out line 57: value: "bloodbank" |
| `bloodbank/bb-donation-srv` | Replaced Sync reference with DM-Initiator |
| `bloodbank/bb-donation-srv` | Removed extra Sync reference: # - ../../../Sync-DM/ |
| `bloodbank/bb-donation-srv` | Added new sync-presync/sync-postsync Job patches |
| `bloodbank/bb-donation-srv` | Commented out line 24: - target: |
| `bloodbank/bb-donation-srv` | Commented out line 25: group: batch |
| `bloodbank/bb-donation-srv` | Commented out line 26: version: v1 |
| `bloodbank/bb-donation-srv` | Commented out line 27: kind: Job |
| `bloodbank/bb-donation-srv` | Commented out line 28: name: before |
| `bloodbank/bb-donation-srv` | Commented out line 29: patch: |- |
| `bloodbank/bb-donation-srv` | Commented out line 30: - op: replace |
| `bloodbank/bb-donation-srv` | Commented out line 31: path: /metadata/name |
| `bloodbank/bb-donation-srv` | Commented out line 32: value: before-bloodbanknet |
| `bloodbank/bb-donation-srv` | Commented out line 33: namespace: moh-uat |
| `bloodbank/bb-donation-srv` | Commented out line 34: - op: add |
| `bloodbank/bb-donation-srv` | Commented out line 35: path: /spec/template/spec/containers/0/env/- |
| `bloodbank/bb-donation-srv` | Commented out line 36: value: |
| `bloodbank/bb-donation-srv` | Commented out line 37: name: CSI_DATA_VERSION |
| `bloodbank/bb-donation-srv` | Commented out line 38: value: "4.2.106.0" |
| `bloodbank/bb-donation-srv` | Commented out line 39: - op: add |
| `bloodbank/bb-donation-srv` | Commented out line 40: path: /spec/template/spec/containers/0/env/- |
| `bloodbank/bb-donation-srv` | Commented out line 41: value: |
| `bloodbank/bb-donation-srv` | Commented out line 42: name: CSI_PROJECT_NAME |
| `bloodbank/bb-donation-srv` | Commented out line 43: value: "bb-donation_srv" |
| `bloodbank/bb-donation-srv` | Commented out line 44: - op: add |
| `bloodbank/bb-donation-srv` | Commented out line 45: path: /spec/template/spec/containers/0/env/- |
| `bloodbank/bb-donation-srv` | Commented out line 46: value: |
| `bloodbank/bb-donation-srv` | Commented out line 47: name: CSI_MODULE_NAME |
| `bloodbank/bb-donation-srv` | Commented out line 48: value: "bb-donation-srv" |
| `bloodbank/bb-donation-srv` | Commented out line 49: - op: add |
| `bloodbank/bb-donation-srv` | Commented out line 50: path: /spec/template/spec/containers/0/env/- |
| `bloodbank/bb-donation-srv` | Commented out line 51: value: |
| `bloodbank/bb-donation-srv` | Commented out line 52: name: CSI_PARENT_MODULE_NAME |
| `bloodbank/bb-donation-srv` | Commented out line 53: value: "bloodbank" |
| `bloodbank/bb-donation-srv` | Commented out line 54: - op: add |
| `bloodbank/bb-donation-srv` | Commented out line 55: path: /spec/template/spec/containers/0/env/- |
| `bloodbank/bb-donation-srv` | Commented out line 56: value: |
| `bloodbank/bb-donation-srv` | Commented out line 57: name: isDropValidationDisabled |
| `bloodbank/bb-donation-srv` | Commented out line 58: value: "true" |
| `bloodbank/csi-blood-transfusion-java` | Replaced Sync reference with DM-Initiator |
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
| `bloodbank/csi-java-bb-service` | Commented out line 32: namespace: moh-uat |
| `bloodbank/csi-java-bb-service` | Commented out line 33: - op: add |
| `bloodbank/csi-java-bb-service` | Commented out line 34: path: /spec/template/spec/containers/0/env/- |
| `bloodbank/csi-java-bb-service` | Commented out line 35: value: |
| `bloodbank/csi-java-bb-service` | Commented out line 36: name: CSI_MODULENAME |
| `bloodbank/csi-java-bb-service` | Commented out line 37: value: "csi-java-bb-service" |
| `bloodbank/csi-java-bb-service` | Commented out line 38: - op: add |
| `bloodbank/csi-java-bb-service` | Commented out line 39: path: /spec/template/spec/containers/0/env/- |
| `bloodbank/csi-java-bb-service` | Commented out line 40: value: |
| `bloodbank/csi-java-bb-service` | Commented out line 41: name: CSI_DATA_VERSION |
| `bloodbank/csi-java-bb-service` | Commented out line 42: value: "4.2.106.0" |
| `bloodbank/csi-java-bb-service` | Commented out line 43: - op: add |
| `bloodbank/csi-java-bb-service` | Commented out line 44: path: /spec/template/spec/containers/0/env/- |
| `bloodbank/csi-java-bb-service` | Commented out line 45: value: |
| `bloodbank/csi-java-bb-service` | Commented out line 46: name: CSI_PROJECT_NAME |
| `bloodbank/csi-java-bb-service` | Commented out line 47: value: "csi-java-bb-service" |
| `bloodbank/csi-java-bb-service` | Commented out line 48: - op: add |
| `bloodbank/csi-java-bb-service` | Commented out line 49: path: /spec/template/spec/containers/0/env/- |
| `bloodbank/csi-java-bb-service` | Commented out line 50: value: |
| `bloodbank/csi-java-bb-service` | Commented out line 51: name: CSI_MODULE_NAME |
| `bloodbank/csi-java-bb-service` | Commented out line 52: value: "csi-java-bb-service" |
| `bloodbank/csi-java-bb-service` | Commented out line 53: - op: add |
| `bloodbank/csi-java-bb-service` | Commented out line 54: path: /spec/template/spec/containers/0/env/- |
| `bloodbank/csi-java-bb-service` | Commented out line 55: value: |
| `bloodbank/csi-java-bb-service` | Commented out line 56: name: CSI_PARENT_MODULE_NAME |
| `bloodbank/csi-java-bb-service` | Commented out line 57: value: "bloodbank" |
| `cssd/csi-cssd-java-sev` | Replaced Sync reference with DM-Initiator |
| `cssd/csi-cssd-java-sev` | Added new sync-presync/sync-postsync Job patches |
| `cssd/csi-cssd-java-sev` | Commented out line 24: - target: |
| `cssd/csi-cssd-java-sev` | Commented out line 25: group: batch |
| `cssd/csi-cssd-java-sev` | Commented out line 26: version: v1 |
| `cssd/csi-cssd-java-sev` | Commented out line 27: kind: Job |
| `cssd/csi-cssd-java-sev` | Commented out line 28: name: before |
| `cssd/csi-cssd-java-sev` | Commented out line 29: patch: |- |
| `cssd/csi-cssd-java-sev` | Commented out line 30: - op: replace |
| `cssd/csi-cssd-java-sev` | Commented out line 31: path: /metadata/name |
| `cssd/csi-cssd-java-sev` | Commented out line 32: value: before-csi-cssd-java-sev |
| `cssd/csi-cssd-java-sev` | Commented out line 33: - op: add |
| `cssd/csi-cssd-java-sev` | Commented out line 34: path: /spec/template/spec/containers/0/env/- |
| `cssd/csi-cssd-java-sev` | Commented out line 35: value: |
| `cssd/csi-cssd-java-sev` | Commented out line 36: name: CSI_MODULENAME |
| `cssd/csi-cssd-java-sev` | Commented out line 37: value: "csi-cssd-java-sev" |
| `cssd/csi-cssd-java-sev` | Commented out line 38: - op: add |
| `cssd/csi-cssd-java-sev` | Commented out line 39: path: /spec/template/spec/containers/0/env/- |
| `cssd/csi-cssd-java-sev` | Commented out line 40: value: |
| `cssd/csi-cssd-java-sev` | Commented out line 41: name: CSI_DATA_VERSION |
| `cssd/csi-cssd-java-sev` | Commented out line 42: value: "4.2.106.0" |
| `cssd/csi-cssd-java-sev` | Commented out line 43: - op: add |
| `cssd/csi-cssd-java-sev` | Commented out line 44: path: /spec/template/spec/containers/0/env/- |
| `cssd/csi-cssd-java-sev` | Commented out line 45: value: |
| `cssd/csi-cssd-java-sev` | Commented out line 46: name: CSI_PROJECT_NAME |
| `cssd/csi-cssd-java-sev` | Commented out line 47: value: "csi-cssd-java-sev" |
| `cssd/csi-cssd-java-sev` | Commented out line 48: - op: add |
| `cssd/csi-cssd-java-sev` | Commented out line 49: path: /spec/template/spec/containers/0/env/- |
| `cssd/csi-cssd-java-sev` | Commented out line 50: value: |
| `cssd/csi-cssd-java-sev` | Commented out line 51: name: CSI_MODULE_NAME |
| `cssd/csi-cssd-java-sev` | Commented out line 52: value: "csi-cssd-java-sev" |
| `cssd/csi-cssd-java-sev` | Commented out line 53: - op: add |
| `cssd/csi-cssd-java-sev` | Commented out line 54: path: /spec/template/spec/containers/0/env/- |
| `cssd/csi-cssd-java-sev` | Commented out line 55: value: |
| `cssd/csi-cssd-java-sev` | Commented out line 56: name: CSI_PARENT_MODULE_NAME |
| `cssd/csi-cssd-java-sev` | Commented out line 57: value: "cssd" |
| `cssd/csi-cssd-java-sev` | Commented out line 58: - target: |
| `cssd/csi-cssd-java-sev` | Commented out line 59: group: batch |
| `cssd/csi-cssd-java-sev` | Commented out line 60: version: v1 |
| `cssd/csi-cssd-java-sev` | Commented out line 61: kind: Job |
| `cssd/csi-cssd-java-sev` | Commented out line 62: name: data-migration_presync |
| `cssd/csi-cssd-java-sev` | Commented out line 63: patch: |- |
| `cssd/csi-cssd-java-sev` | Commented out line 64: - op: replace |
| `cssd/csi-cssd-java-sev` | Commented out line 65: path: /metadata/name |
| `cssd/csi-cssd-java-sev` | Commented out line 66: value: datamigrations-pre-csi-cssd-java-sev |
| `cssd/csi-cssd-java-sev` | Commented out line 67: - op: add |
| `cssd/csi-cssd-java-sev` | Commented out line 68: path: /spec/template/spec/containers/0/env/- |
| `cssd/csi-cssd-java-sev` | Commented out line 69: value: |
| `cssd/csi-cssd-java-sev` | Commented out line 70: name: CSI_MODULENAME |
| `cssd/csi-cssd-java-sev` | Commented out line 71: value: "csi-cssd-java-sev" |
| `cssd/csi-cssd-java-sev` | Commented out line 72: - op: add |
| `cssd/csi-cssd-java-sev` | Commented out line 73: path: /spec/template/spec/containers/0/env/- |
| `cssd/csi-cssd-java-sev` | Commented out line 74: value: |
| `cssd/csi-cssd-java-sev` | Commented out line 75: name: CSI_DATA_VERSION |
| `cssd/csi-cssd-java-sev` | Commented out line 76: value: "4.2.106.0" |
| `cssd/csi-cssd-java-sev` | Commented out line 77: - op: add |
| `cssd/csi-cssd-java-sev` | Commented out line 78: path: /spec/template/spec/containers/0/env/- |
| `cssd/csi-cssd-java-sev` | Commented out line 79: value: |
| `cssd/csi-cssd-java-sev` | Commented out line 80: name: CSI_PROJECT_NAME |
| `cssd/csi-cssd-java-sev` | Commented out line 81: value: "csi-cssd-java-sev" |
| `cssd/csi-cssd-java-sev` | Commented out line 82: - op: add |
| `cssd/csi-cssd-java-sev` | Commented out line 83: path: /spec/template/spec/containers/0/env/- |
| `cssd/csi-cssd-java-sev` | Commented out line 84: value: |
| `cssd/csi-cssd-java-sev` | Commented out line 85: name: CSI_MODULE_NAME |
| `cssd/csi-cssd-java-sev` | Commented out line 86: value: "csi-cssd-java-sev" |
| `cssd/csi-cssd-java-sev` | Commented out line 87: - op: add |
| `cssd/csi-cssd-java-sev` | Commented out line 88: path: /spec/template/spec/containers/0/env/- |
| `cssd/csi-cssd-java-sev` | Commented out line 89: value: |
| `cssd/csi-cssd-java-sev` | Commented out line 90: name: CSI_PARENT_MODULE_NAME |
| `cssd/csi-cssd-java-sev` | Commented out line 91: value: "cssd" |
| `cssd/csi-cssd-node-sev/overlays` | Updated Deployment target name: csi-cssd-node-sev -> overlays |
| `cssd/csi-cssd-ui` | Replaced Sync reference with DM-Initiator |
| `cssd/csi-cssd-ui` | Added new sync-presync/sync-postsync Job patches |
| `cssd/csi-cssd-ui` | Commented out line 25: - target: |
| `cssd/csi-cssd-ui` | Commented out line 26: group: batch |
| `cssd/csi-cssd-ui` | Commented out line 27: version: v1 |
| `cssd/csi-cssd-ui` | Commented out line 28: kind: Job |
| `cssd/csi-cssd-ui` | Commented out line 29: name: before |
| `cssd/csi-cssd-ui` | Commented out line 30: patch: |- |
| `cssd/csi-cssd-ui` | Commented out line 31: - op: replace |
| `cssd/csi-cssd-ui` | Commented out line 32: path: /metadata/name |
| `cssd/csi-cssd-ui` | Commented out line 33: value: before-csi-cssd-ui |
| `cssd/csi-cssd-ui` | Commented out line 34: - op: add |
| `cssd/csi-cssd-ui` | Commented out line 35: path: /spec/template/spec/containers/0/env/- |
| `cssd/csi-cssd-ui` | Commented out line 36: value: |
| `cssd/csi-cssd-ui` | Commented out line 37: name: CSI_MODULENAME |
| `cssd/csi-cssd-ui` | Commented out line 38: value: "csi-cssd-ui" |
| `cssd/csi-cssd-ui` | Commented out line 39: - op: add |
| `cssd/csi-cssd-ui` | Commented out line 40: path: /spec/template/spec/containers/0/env/- |
| `cssd/csi-cssd-ui` | Commented out line 41: value: |
| `cssd/csi-cssd-ui` | Commented out line 42: name: CSI_DATA_VERSION |
| `cssd/csi-cssd-ui` | Commented out line 43: value: "4.2.106.0" |
| `cssd/csi-cssd-ui` | Commented out line 44: - op: add |
| `cssd/csi-cssd-ui` | Commented out line 45: path: /spec/template/spec/containers/0/env/- |
| `cssd/csi-cssd-ui` | Commented out line 46: value: |
| `cssd/csi-cssd-ui` | Commented out line 47: name: CSI_PROJECT_NAME |
| `cssd/csi-cssd-ui` | Commented out line 48: value: "csi-cssd-ui" |
| `cssd/csi-cssd-ui` | Commented out line 49: - op: add |
| `cssd/csi-cssd-ui` | Commented out line 50: path: /spec/template/spec/containers/0/env/- |
| `cssd/csi-cssd-ui` | Commented out line 51: value: |
| `cssd/csi-cssd-ui` | Commented out line 52: name: CSI_MODULE_NAME |
| `cssd/csi-cssd-ui` | Commented out line 53: value: "csi-cssd-ui" |
| `cssd/csi-cssd-ui` | Commented out line 54: - op: add |
| `cssd/csi-cssd-ui` | Commented out line 55: path: /spec/template/spec/containers/0/env/- |
| `cssd/csi-cssd-ui` | Commented out line 56: value: |
| `cssd/csi-cssd-ui` | Commented out line 57: name: CSI_PARENT_MODULE_NAME |
| `cssd/csi-cssd-ui` | Commented out line 58: value: "cssd" |
| `dms/csi-document-management-service` | Replaced Sync reference with DM-Initiator |
| `dms/csi-document-management-service` | Added new sync-presync/sync-postsync Job patches |
| `dms/csi-document-management-service` | Commented out line 23: - target: |
| `dms/csi-document-management-service` | Commented out line 24: group: batch |
| `dms/csi-document-management-service` | Commented out line 25: version: v1 |
| `dms/csi-document-management-service` | Commented out line 26: kind: Job |
| `dms/csi-document-management-service` | Commented out line 27: name: before |
| `dms/csi-document-management-service` | Commented out line 28: patch: |- |
| `dms/csi-document-management-service` | Commented out line 29: - op: replace |
| `dms/csi-document-management-service` | Commented out line 30: path: /metadata/name |
| `dms/csi-document-management-service` | Commented out line 31: value: before-dms |
| `dms/csi-document-management-service` | Commented out line 32: namespace: moh-uat |
| `dms/csi-document-management-service` | Commented out line 33: - op: add |
| `dms/csi-document-management-service` | Commented out line 34: path: /spec/template/spec/containers/0/env/- |
| `dms/csi-document-management-service` | Commented out line 35: value: |
| `dms/csi-document-management-service` | Commented out line 36: name: CSI_MODULENAME |
| `dms/csi-document-management-service` | Commented out line 37: value: "csi-java-bb-service" |
| `dms/csi-document-management-service` | Commented out line 38: - op: add |
| `dms/csi-document-management-service` | Commented out line 39: path: /spec/template/spec/containers/0/env/- |
| `dms/csi-document-management-service` | Commented out line 40: value: |
| `dms/csi-document-management-service` | Commented out line 41: name: CSI_DATA_VERSION |
| `dms/csi-document-management-service` | Commented out line 42: value: "4.2.106.0" |
| `dms/csi-document-management-service` | Commented out line 43: - op: add |
| `dms/csi-document-management-service` | Commented out line 44: path: /spec/template/spec/containers/0/env/- |
| `dms/csi-document-management-service` | Commented out line 45: value: |
| `dms/csi-document-management-service` | Commented out line 46: name: CSI_PROJECT_NAME |
| `dms/csi-document-management-service` | Commented out line 47: value: "csi-document-management-service" |
| `dms/csi-document-management-service` | Commented out line 48: - op: add |
| `dms/csi-document-management-service` | Commented out line 49: path: /spec/template/spec/containers/0/env/- |
| `dms/csi-document-management-service` | Commented out line 50: value: |
| `dms/csi-document-management-service` | Commented out line 51: name: CSI_MODULE_NAME |
| `dms/csi-document-management-service` | Commented out line 52: value: "csi-document-management-service" |
| `dms/csi-document-management-service` | Commented out line 53: - op: add |
| `dms/csi-document-management-service` | Commented out line 54: path: /spec/template/spec/containers/0/env/- |
| `dms/csi-document-management-service` | Commented out line 55: value: |
| `dms/csi-document-management-service` | Commented out line 56: name: CSI_PARENT_MODULE_NAME |
| `dms/csi-document-management-service` | Commented out line 57: value: "dms" |
| `dms/dmsstorageengine` | Updated Deployment target name: document-storage-engine-service -> dmsstorageengine |
| `econsent/e-consent` | Updated Deployment target name: cs-net-econsent -> e-consent |
| `econsent/e-consent-ui` | Updated Deployment target name: cs-net-econsentui -> e-consent-ui |
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Replaced Sync reference with DM-Initiator |
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Added new sync-presync/sync-postsync Job patches |
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Commented out line 21: - target: |
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Commented out line 22: group: batch |
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Commented out line 23: version: v1 |
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Commented out line 24: kind: Job |
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Commented out line 25: name: .* |
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Commented out line 26: patch: |- |
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Commented out line 27: - op: replace |
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Commented out line 28: path: /metadata/name |
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Commented out line 29: value: before-csi-ehr-com-ip-dashboardwidget-dotnet-sev |
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Commented out line 30: - op: add |
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Commented out line 31: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Commented out line 32: value: |
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Commented out line 33: name: CSI_MODULENAME |
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Commented out line 34: value: "csi-ehr-opd" |
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Commented out line 35: - op: add |
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Commented out line 36: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Commented out line 37: value: |
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Commented out line 38: name: CSI_DATA_VERSION |
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Commented out line 39: value: "4.0.127.0" |
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Commented out line 40: - op: add |
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Commented out line 41: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Commented out line 42: value: |
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Commented out line 43: name: CSI_PROJECT_NAME |
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Commented out line 44: value: "csi-ehr-com-ip-dashboardwidget-dotnet-sev" |
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Commented out line 45: - op: add |
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Commented out line 46: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Commented out line 47: value: |
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Commented out line 48: name: CSI_MODULE_NAME |
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Commented out line 49: value: "csi-ehr-com-ip-dashboardwidget-dotnet-sev" |
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Commented out line 50: - op: add |
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Commented out line 51: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Commented out line 52: value: |
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Commented out line 53: name: CSI_PARENT_MODULE_NAME |
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Commented out line 54: value: "ehr" |
| `ehr/csi-ehr-com-ip-discharge-dotnet-sev` | Replaced commented Sync reference with commented DM-Initiator |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Replaced Sync reference with DM-Initiator |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Added new sync-presync/sync-postsync Job patches |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 23: - target: |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 24: group: batch |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 25: version: v1 |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 26: kind: Job |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 27: name: .* |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 28: patch: |- |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 29: - op: replace |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 30: path: /metadata/name |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 31: value: before-ehropdmasterdotnet |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 32: - op: add |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 33: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 34: value: |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 35: name: CSI_MODULENAME |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 36: value: "csi-ehr-opd" |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 37: - op: add |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 38: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 39: value: |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 40: name: CSI_DATA_VERSION |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 41: value: "4.0.127.0" |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 42: - op: add |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 43: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 44: value: |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 45: name: CSI_PROJECT_NAME |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 46: value: "csi-ehr-com-opd-master-dotnet-sev" |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 47: - op: add |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 48: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 49: value: |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 50: name: CSI_MODULE_NAME |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 51: value: "csi-ehr-com-opd-master-dotnet-sev" |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 52: - op: add |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 53: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 54: value: |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 55: name: CSI_PARENT_MODULE_NAME |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 56: value: "ehr" |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Replaced Sync reference with DM-Initiator |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Added new sync-presync/sync-postsync Job patches |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 23: - target: |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 24: group: batch |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 25: version: v1 |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 26: kind: Job |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 27: name: .* |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 28: patch: |- |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 29: - op: replace |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 30: path: /metadata/name |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 31: value: before-ehropdpatientdotnet |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 32: - op: add |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 33: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 34: value: |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 35: name: CSI_MODULENAME |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 36: value: "csi-opd-patient-pomr" |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 37: - op: add |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 38: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 39: value: |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 40: name: CSI_DATA_VERSION |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 41: value: "4.0.127.0" |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 42: - op: add |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 43: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 44: value: |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 45: name: CSI_PROJECT_NAME |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 46: value: "csi-ehr-com-opd-patient-dotnet-sev" |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 47: - op: add |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 48: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 49: value: |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 50: name: CSI_MODULE_NAME |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 51: value: "csi-ehr-com-opd-patient-dotnet-sev" |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 52: - op: add |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 53: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 54: value: |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 55: name: CSI_PARENT_MODULE_NAME |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 56: value: "ehr" |
| `ehr/csi-ehr-common-java-sev` | Replaced Sync reference with DM-Initiator |
| `ehr/csi-ehr-common-java-sev` | Added new sync-presync/sync-postsync Job patches |
| `ehr/csi-ehr-common-java-sev` | Commented out line 19: - target: |
| `ehr/csi-ehr-common-java-sev` | Commented out line 20: group: batch |
| `ehr/csi-ehr-common-java-sev` | Commented out line 21: version: v1 |
| `ehr/csi-ehr-common-java-sev` | Commented out line 22: kind: Job |
| `ehr/csi-ehr-common-java-sev` | Commented out line 23: name: .* |
| `ehr/csi-ehr-common-java-sev` | Commented out line 24: patch: |- |
| `ehr/csi-ehr-common-java-sev` | Commented out line 25: - op: replace |
| `ehr/csi-ehr-common-java-sev` | Commented out line 26: path: /metadata/name |
| `ehr/csi-ehr-common-java-sev` | Commented out line 27: value: before-csi-ehr-common |
| `ehr/csi-ehr-common-java-sev` | Commented out line 28: namespace: moh-uat |
| `ehr/csi-ehr-common-java-sev` | Commented out line 29: - op: add |
| `ehr/csi-ehr-common-java-sev` | Commented out line 30: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-common-java-sev` | Commented out line 31: value: |
| `ehr/csi-ehr-common-java-sev` | Commented out line 32: name: CSI_MODULENAME |
| `ehr/csi-ehr-common-java-sev` | Commented out line 33: value: "csi-ehr-common" |
| `ehr/csi-ehr-common-java-sev` | Commented out line 34: - op: add |
| `ehr/csi-ehr-common-java-sev` | Commented out line 35: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-common-java-sev` | Commented out line 36: value: |
| `ehr/csi-ehr-common-java-sev` | Commented out line 37: name: CSI_DATA_VERSION |
| `ehr/csi-ehr-common-java-sev` | Commented out line 38: value: "4.1.170.0" |
| `ehr/csi-ehr-common-java-sev` | Commented out line 39: - op: add |
| `ehr/csi-ehr-common-java-sev` | Commented out line 40: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-common-java-sev` | Commented out line 41: value: |
| `ehr/csi-ehr-common-java-sev` | Commented out line 42: name: CSI_PROJECT_NAME |
| `ehr/csi-ehr-common-java-sev` | Commented out line 43: value: "csi-ehr-common-java-sev" |
| `ehr/csi-ehr-common-java-sev` | Commented out line 44: - op: add |
| `ehr/csi-ehr-common-java-sev` | Commented out line 45: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-common-java-sev` | Commented out line 46: value: |
| `ehr/csi-ehr-common-java-sev` | Commented out line 47: name: CSI_MODULE_NAME |
| `ehr/csi-ehr-common-java-sev` | Commented out line 48: value: "csi-ehr-common-java-sev" |
| `ehr/csi-ehr-common-java-sev` | Commented out line 49: - op: add |
| `ehr/csi-ehr-common-java-sev` | Commented out line 50: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-common-java-sev` | Commented out line 51: value: |
| `ehr/csi-ehr-common-java-sev` | Commented out line 52: name: CSI_PARENT_MODULE_NAME |
| `ehr/csi-ehr-common-java-sev` | Commented out line 53: value: "ehr" |
| `ehr/csi-ehr-common-scheduler-java-sev` | Replaced Sync reference with DM-Initiator |
| `ehr/csi-ehr-common-scheduler-java-sev` | Added new sync-presync/sync-postsync Job patches |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 24: - target: |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 25: group: batch |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 26: version: v1 |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 27: kind: Job |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 28: name: .* |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 29: patch: |- |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 30: - op: replace |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 31: path: /metadata/name |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 32: value: before-ehrschedulerjava |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 33: - op: add |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 34: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 35: value: |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 36: name: CSI_MODULENAME |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 37: value: "csi-ehr-common-java-sev" |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 38: - op: add |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 39: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 40: value: |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 41: name: CSI_DATA_VERSION |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 42: value: "4.0.127.0" |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 43: - op: add |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 44: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 45: value: |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 46: name: CSI_PROJECT_NAME |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 47: value: "csi-ehr-common-scheduler-java-sev" |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 48: - op: add |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 49: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 50: value: |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 51: name: CSI_MODULE_NAME |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 52: value: "csi-ehr-common-scheduler-java-sev" |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 53: - op: add |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 54: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 55: value: |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 56: name: CSI_PARENT_MODULE_NAME |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 57: value: "ehr" |
| `ehr/csi-ehr-config-java-sev` | Replaced Sync reference with DM-Initiator |
| `ehr/csi-ehr-config-java-sev` | Added new sync-presync/sync-postsync Job patches |
| `ehr/csi-ehr-config-java-sev` | Commented out line 19: - target: |
| `ehr/csi-ehr-config-java-sev` | Commented out line 20: group: batch |
| `ehr/csi-ehr-config-java-sev` | Commented out line 21: version: v1 |
| `ehr/csi-ehr-config-java-sev` | Commented out line 22: kind: Job |
| `ehr/csi-ehr-config-java-sev` | Commented out line 23: name: .* |
| `ehr/csi-ehr-config-java-sev` | Commented out line 24: patch: |- |
| `ehr/csi-ehr-config-java-sev` | Commented out line 25: - op: replace |
| `ehr/csi-ehr-config-java-sev` | Commented out line 26: path: /metadata/name |
| `ehr/csi-ehr-config-java-sev` | Commented out line 27: value: before-ehrconfigjava |
| `ehr/csi-ehr-config-java-sev` | Commented out line 28: namespace: moh-uat |
| `ehr/csi-ehr-config-java-sev` | Commented out line 29: - op: add |
| `ehr/csi-ehr-config-java-sev` | Commented out line 30: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-config-java-sev` | Commented out line 31: value: |
| `ehr/csi-ehr-config-java-sev` | Commented out line 32: name: CSI_MODULENAME |
| `ehr/csi-ehr-config-java-sev` | Commented out line 33: value: "csi-ehr-opd" |
| `ehr/csi-ehr-config-java-sev` | Commented out line 34: - op: add |
| `ehr/csi-ehr-config-java-sev` | Commented out line 35: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-config-java-sev` | Commented out line 36: value: |
| `ehr/csi-ehr-config-java-sev` | Commented out line 37: name: CSI_DATA_VERSION |
| `ehr/csi-ehr-config-java-sev` | Commented out line 38: value: "4.0.125.0" |
| `ehr/csi-ehr-config-java-sev` | Commented out line 39: - op: add |
| `ehr/csi-ehr-config-java-sev` | Commented out line 40: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-config-java-sev` | Commented out line 41: value: |
| `ehr/csi-ehr-config-java-sev` | Commented out line 42: name: CSI_PROJECT_NAME |
| `ehr/csi-ehr-config-java-sev` | Commented out line 43: value: "csi-ehr-config-java-sev" |
| `ehr/csi-ehr-config-java-sev` | Commented out line 44: - op: add |
| `ehr/csi-ehr-config-java-sev` | Commented out line 45: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-config-java-sev` | Commented out line 46: value: |
| `ehr/csi-ehr-config-java-sev` | Commented out line 47: name: CSI_MODULE_NAME |
| `ehr/csi-ehr-config-java-sev` | Commented out line 48: value: "csi-ehr-config-java-sev" |
| `ehr/csi-ehr-config-java-sev` | Commented out line 49: - op: add |
| `ehr/csi-ehr-config-java-sev` | Commented out line 50: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-config-java-sev` | Commented out line 51: value: |
| `ehr/csi-ehr-config-java-sev` | Commented out line 52: name: CSI_PARENT_MODULE_NAME |
| `ehr/csi-ehr-config-java-sev` | Commented out line 53: value: "ehr" |
| `ehr/csi-ehr-ic-bundle-java-sev` | Replaced Sync reference with DM-Initiator |
| `ehr/csi-ehr-ic-bundle-java-sev` | Added new sync-presync/sync-postsync Job patches |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 26: - target: |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 27: group: batch |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 28: version: v1 |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 29: kind: Job |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 30: name: .* |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 31: patch: |- |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 32: - op: replace |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 33: path: /metadata/name |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 34: value: before-ehricbundlejava |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 35: - op: add |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 36: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 37: value: |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 38: name: CSI_MODULENAME |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 39: value: "csi-ehr-ic-bundle-java-sev" |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 40: - op: add |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 41: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 42: value: |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 43: name: CSI_DATA_VERSION |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 44: value: "4.2.464.0" |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 45: - op: add |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 46: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 47: value: |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 48: name: CSI_PROJECT_NAME |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 49: value: "csi-ehr-ic-bundle-java-sev" |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 50: - op: add |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 51: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 52: value: |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 53: name: CSI_MODULE_NAME |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 54: value: "csi-ehr-ic-bundle-java-sev" |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 55: - op: add |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 56: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 57: value: |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 58: name: CSI_PARENT_MODULE_NAME |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 59: value: "ehr" |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Replaced Sync reference with DM-Initiator |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Added new sync-presync/sync-postsync Job patches |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 26: - target: |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 27: group: batch |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 28: version: v1 |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 29: kind: Job |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 30: name: .* |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 31: patch: |- |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 32: - op: replace |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 33: path: /metadata/name |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 34: value: before-ehricdashboardjava |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 35: - op: add |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 36: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 37: value: |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 38: name: CSI_MODULENAME |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 39: value: "csi-ehr-ic-dashboard" |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 40: - op: add |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 41: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 42: value: |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 43: name: CSI_DATA_VERSION |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 44: value: "4.0.127.0" |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 45: - op: add |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 46: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 47: value: |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 48: name: CSI_PROJECT_NAME |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 49: value: "csi-ehr-ic-dashboard-java-sev" |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 50: - op: add |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 51: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 52: value: |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 53: name: CSI_MODULE_NAME |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 54: value: "csi-ehr-ic-dashboard-java-sev" |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 55: - op: add |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 56: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 57: value: |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 58: name: CSI_PARENT_MODULE_NAME |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 59: value: "ehr" |
| `ehr/csi-ehr-initialassessment-java-sev` | Replaced Sync reference with DM-Initiator |
| `ehr/csi-ehr-initialassessment-java-sev` | Added new sync-presync/sync-postsync Job patches |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 26: - target: |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 27: group: batch |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 28: version: v1 |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 29: kind: Job |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 30: name: .* |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 31: patch: |- |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 32: - op: replace |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 33: path: /metadata/name |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 34: value: before-ehrintitialassessjava |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 35: - op: add |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 36: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 37: value: |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 38: name: CSI_MODULENAME |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 39: value: "csi-ehr-specialized-clinic-java-sev" |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 40: - op: add |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 41: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 42: value: |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 43: name: CSI_DATA_VERSION |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 44: value: "4.0.161.0" |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 45: - op: add |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 46: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 47: value: |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 48: name: CSI_PROJECT_NAME |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 49: value: "csi-ehr-initialassessment-java-sev" |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 50: - op: add |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 51: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 52: value: |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 53: name: CSI_MODULE_NAME |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 54: value: "csi-ehr-initialassessment-java-sev" |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 55: - op: add |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 56: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 57: value: |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 58: name: CSI_PARENT_MODULE_NAME |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 59: value: "ehr" |
| `ehr/csi-ehr-ip-java-sev` | Replaced Sync reference with DM-Initiator |
| `ehr/csi-ehr-ip-java-sev` | Added new sync-presync/sync-postsync Job patches |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 19: - target: |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 20: group: batch |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 21: version: v1 |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 22: kind: Job |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 23: name: .* |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 24: patch: |- |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 25: - op: replace |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 26: path: /metadata/name |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 27: value: before-ehripjava |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 28: - op: add |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 29: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 30: value: |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 31: name: CSI_MODULENAME |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 32: value: "csi-ehr-ip-java-sev" |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 33: - op: add |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 34: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 35: value: |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 36: name: CSI_DATA_VERSION |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 37: value: "4.0.127.0" |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 38: - op: add |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 39: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 40: value: |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 41: name: CSI_PROJECT_NAME |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 42: value: "csi-ehr-ip-java-sev" |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 43: - op: add |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 44: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 45: value: |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 46: name: CSI_MODULE_NAME |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 47: value: "csi-ehr-ip-java-sev" |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 48: - op: add |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 49: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 50: value: |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 51: name: CSI_PARENT_MODULE_NAME |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 52: value: "ehr" |
| `ehr/csi-ehr-ldr-java-sev` | Replaced Sync reference with DM-Initiator |
| `ehr/csi-ehr-ldr-java-sev` | Added new sync-presync/sync-postsync Job patches |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 23: - target: |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 24: group: batch |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 25: version: v1 |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 26: kind: Job |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 27: name: .* |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 28: patch: |- |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 29: - op: replace |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 30: path: /metadata/name |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 31: value: before-ehrldrjava |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 32: - op: add |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 33: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 34: value: |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 35: name: CSI_MODULENAME |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 36: value: "csi-ehr-ldr-java-sev" |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 37: - op: add |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 38: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 39: value: |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 40: name: CSI_DATA_VERSION |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 41: value: "4.0.127.0" |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 42: - op: add |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 43: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 44: value: |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 45: name: CSI_PROJECT_NAME |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 46: value: "csi-ehr-ldr-java-sev" |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 47: - op: add |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 48: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 49: value: |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 50: name: CSI_MODULE_NAME |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 51: value: "csi-ehr-ldr-java-sev" |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 52: - op: add |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 53: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 54: value: |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 55: name: CSI_PARENT_MODULE_NAME |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 56: value: "ehr" |
| `ehr/csi-ehr-listener-java-sev` | Replaced Sync reference with DM-Initiator |
| `ehr/csi-ehr-opd-java-sev` | Replaced Sync reference with DM-Initiator |
| `ehr/csi-ehr-opd-java-sev` | Removed extra Sync reference: # - ../../../Sync-DM/ |
| `ehr/csi-ehr-opd-java-sev` | Added new sync-presync/sync-postsync Job patches |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 19: - target: |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 20: group: batch |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 21: version: v1 |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 22: kind: Job |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 23: name: .* |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 24: patch: |- |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 25: - op: replace |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 26: path: /metadata/name |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 27: value: before-ehropdjava |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 28: - op: add |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 29: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 30: value: |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 31: name: CSI_MODULENAME |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 32: value: "csi-ehr-opd" |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 33: - op: add |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 34: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 35: value: |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 36: name: CSI_DATA_VERSION |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 37: value: "4.0.127.0" |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 38: - op: add |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 39: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 40: value: |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 41: name: CSI_PROJECT_NAME |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 42: value: "csi-ehr-opd-java-sev" |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 43: - op: add |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 44: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 45: value: |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 46: name: CSI_MODULE_NAME |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 47: value: "csi-ehr-opd-java-sev" |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 48: - op: add |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 49: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 50: value: |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 51: name: CSI_PARENT_MODULE_NAME |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 52: value: "ehr" |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 54: - target: |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 55: group: batch |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 56: version: v1 |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 57: kind: Job |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 58: name: data-migration-presync |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 59: patch: |- |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 60: - op: replace |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 61: path: /metadata/name |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 62: value: data-migration-presync-ehropdjava |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 63: - op: add |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 64: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 65: value: |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 66: name: CSI_DATA_VERSION |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 67: value: "4.0.127.0" |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 68: - op: add |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 69: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 70: value: |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 71: name: CSI_PROJECT_NAME |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 72: value: "csi-ehr-opd-java-sev" |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 73: - op: add |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 74: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 75: value: |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 76: name: CSI_MODULE_NAME |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 77: value: "ehropdjava" |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 78: - op: add |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 79: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 80: value: |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 81: name: CSI_PARENT_MODULE_NAME |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 82: value: "ehr" |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 84: - target: |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 85: group: batch |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 86: version: v1 |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 87: kind: Job |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 88: name: data-migration-postsync |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 89: patch: |- |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 90: - op: replace |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 91: path: /metadata/name |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 92: value: data-migration-postsync-ehropdjava |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 93: - op: add |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 94: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 95: value: |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 96: name: CSI_DATA_VERSION |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 97: value: "4.0.127.0" |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 98: - op: add |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 99: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 100: value: |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 101: name: CSI_PROJECT_NAME |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 102: value: "csi-ehr-opd-java-sev" |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 103: - op: add |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 104: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 105: value: |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 106: name: CSI_MODULE_NAME |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 107: value: "ehropdjava" |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 108: - op: add |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 109: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 110: value: |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 111: name: CSI_PARENT_MODULE_NAME |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 112: value: "ehr" |
| `ehr/csi-ehr-opd-patient-pomr-java-sev` | Replaced Sync reference with DM-Initiator |
| `ehr/csi-ehr-opd-patient-pomr-java-sev` | Added new sync-presync/sync-postsync Job patches |
| `ehr/csi-ehr-opd-patient-pomr-java-sev` | Commented out line 19: - target: |
| `ehr/csi-ehr-opd-patient-pomr-java-sev` | Commented out line 20: group: batch |
| `ehr/csi-ehr-opd-patient-pomr-java-sev` | Commented out line 21: version: v1 |
| `ehr/csi-ehr-opd-patient-pomr-java-sev` | Commented out line 22: kind: Job |
| `ehr/csi-ehr-opd-patient-pomr-java-sev` | Commented out line 23: name: .* |
| `ehr/csi-ehr-opd-patient-pomr-java-sev` | Commented out line 24: patch: |- |
| `ehr/csi-ehr-opd-patient-pomr-java-sev` | Commented out line 25: - op: replace |
| `ehr/csi-ehr-opd-patient-pomr-java-sev` | Commented out line 26: path: /metadata/name |
| `ehr/csi-ehr-opd-patient-pomr-java-sev` | Commented out line 27: value: before-ehrpomrjava |
| `ehr/csi-ehr-opd-patient-pomr-java-sev` | Commented out line 28: namespace: moh-uat |
| `ehr/csi-ehr-opd-patient-pomr-java-sev` | Commented out line 29: - op: add |
| `ehr/csi-ehr-opd-patient-pomr-java-sev` | Commented out line 30: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-opd-patient-pomr-java-sev` | Commented out line 31: value: |
| `ehr/csi-ehr-opd-patient-pomr-java-sev` | Commented out line 32: name: CSI_MODULENAME |
| `ehr/csi-ehr-opd-patient-pomr-java-sev` | Commented out line 33: value: "csi-opd-patient-pomr" |
| `ehr/csi-ehr-opd-patient-pomr-java-sev` | Commented out line 34: - op: add |
| `ehr/csi-ehr-opd-patient-pomr-java-sev` | Commented out line 35: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-opd-patient-pomr-java-sev` | Commented out line 36: value: |
| `ehr/csi-ehr-opd-patient-pomr-java-sev` | Commented out line 37: name: CSI_DATA_VERSION |
| `ehr/csi-ehr-opd-patient-pomr-java-sev` | Commented out line 38: value: "4.0.125.0" |
| `ehr/csi-ehr-opd-patient-pomr-java-sev` | Commented out line 39: - op: add |
| `ehr/csi-ehr-opd-patient-pomr-java-sev` | Commented out line 40: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-opd-patient-pomr-java-sev` | Commented out line 41: value: |
| `ehr/csi-ehr-opd-patient-pomr-java-sev` | Commented out line 42: name: CSI_PROJECT_NAME |
| `ehr/csi-ehr-opd-patient-pomr-java-sev` | Commented out line 43: value: "csi-ehr-opd-patient-pomr-java-sev" |
| `ehr/csi-ehr-opd-patient-pomr-java-sev` | Commented out line 44: - op: add |
| `ehr/csi-ehr-opd-patient-pomr-java-sev` | Commented out line 45: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-opd-patient-pomr-java-sev` | Commented out line 46: value: |
| `ehr/csi-ehr-opd-patient-pomr-java-sev` | Commented out line 47: name: CSI_MODULE_NAME |
| `ehr/csi-ehr-opd-patient-pomr-java-sev` | Commented out line 48: value: "csi-ehr-opd-patient-pomr-java-sev" |
| `ehr/csi-ehr-opd-patient-pomr-java-sev` | Commented out line 49: - op: add |
| `ehr/csi-ehr-opd-patient-pomr-java-sev` | Commented out line 50: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-opd-patient-pomr-java-sev` | Commented out line 51: value: |
| `ehr/csi-ehr-opd-patient-pomr-java-sev` | Commented out line 52: name: CSI_PARENT_MODULE_NAME |
| `ehr/csi-ehr-opd-patient-pomr-java-sev` | Commented out line 53: value: "ehr" |
| `ehr/csi-ehr-opd-ui` | Replaced Sync reference with DM-Initiator |
| `ehr/csi-ehr-opd-ui` | Added new sync-presync/sync-postsync Job patches |
| `ehr/csi-ehr-opd-ui` | Commented out line 23: - target: |
| `ehr/csi-ehr-opd-ui` | Commented out line 24: group: batch |
| `ehr/csi-ehr-opd-ui` | Commented out line 25: version: v1 |
| `ehr/csi-ehr-opd-ui` | Commented out line 26: kind: Job |
| `ehr/csi-ehr-opd-ui` | Commented out line 27: name: .* |
| `ehr/csi-ehr-opd-ui` | Commented out line 28: patch: |- |
| `ehr/csi-ehr-opd-ui` | Commented out line 29: - op: replace |
| `ehr/csi-ehr-opd-ui` | Commented out line 30: path: /metadata/name |
| `ehr/csi-ehr-opd-ui` | Commented out line 31: value: before-csi-ehr-opd-ui |
| `ehr/csi-ehr-opd-ui` | Commented out line 32: namespace: moh-uat |
| `ehr/csi-ehr-opd-ui` | Commented out line 33: - op: add |
| `ehr/csi-ehr-opd-ui` | Commented out line 34: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-opd-ui` | Commented out line 35: value: |
| `ehr/csi-ehr-opd-ui` | Commented out line 36: name: CSI_MODULENAME |
| `ehr/csi-ehr-opd-ui` | Commented out line 37: value: "csi-ehr-opd-ui" |
| `ehr/csi-ehr-opd-ui` | Commented out line 38: - op: add |
| `ehr/csi-ehr-opd-ui` | Commented out line 39: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-opd-ui` | Commented out line 40: value: |
| `ehr/csi-ehr-opd-ui` | Commented out line 41: name: CSI_DATA_VERSION |
| `ehr/csi-ehr-opd-ui` | Commented out line 42: value: "AMD-10802" |
| `ehr/csi-ehr-opd-ui` | Commented out line 43: - op: add |
| `ehr/csi-ehr-opd-ui` | Commented out line 44: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-opd-ui` | Commented out line 45: value: |
| `ehr/csi-ehr-opd-ui` | Commented out line 46: name: CSI_PROJECT_NAME |
| `ehr/csi-ehr-opd-ui` | Commented out line 47: value: "csi-ehr-opd-ui" |
| `ehr/csi-ehr-opd-ui` | Commented out line 48: - op: add |
| `ehr/csi-ehr-opd-ui` | Commented out line 49: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-opd-ui` | Commented out line 50: value: |
| `ehr/csi-ehr-opd-ui` | Commented out line 51: name: CSI_MODULE_NAME |
| `ehr/csi-ehr-opd-ui` | Commented out line 52: value: "csi-ehr-opd-ui" |
| `ehr/csi-ehr-opd-ui` | Commented out line 53: - op: add |
| `ehr/csi-ehr-opd-ui` | Commented out line 54: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-opd-ui` | Commented out line 55: value: |
| `ehr/csi-ehr-opd-ui` | Commented out line 56: name: CSI_PARENT_MODULE_NAME |
| `ehr/csi-ehr-opd-ui` | Commented out line 57: value: "ehr" |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Replaced Sync reference with DM-Initiator |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Added new sync-presync/sync-postsync Job patches |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 23: - target: |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 24: group: batch |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 25: version: v1 |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 26: kind: Job |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 27: name: .* |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 28: patch: |- |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 29: - op: replace |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 30: path: /metadata/name |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 31: value: before-ehroranesthesiajava |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 32: - op: add |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 33: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 34: value: |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 35: name: CSI_MODULENAME |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 36: value: "csi-ehr-or-anesthesia-java-sev" |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 37: - op: add |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 38: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 39: value: |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 40: name: CSI_DATA_VERSION |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 41: value: "4.0.127.0" |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 42: - op: add |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 43: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 44: value: |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 45: name: CSI_PROJECT_NAME |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 46: value: "csi-ehr-or-anesthesia-java-sev" |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 47: - op: add |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 48: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 49: value: |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 50: name: CSI_MODULE_NAME |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 51: value: "csi-ehr-or-anesthesia-java-sev" |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 52: - op: add |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 53: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 54: value: |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 55: name: CSI_PARENT_MODULE_NAME |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 56: value: "ehr" |
| `ehr/csi-ehr-or-book-java-sev` | Replaced Sync reference with DM-Initiator |
| `ehr/csi-ehr-or-book-java-sev` | Added new sync-presync/sync-postsync Job patches |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 23: - target: |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 24: group: batch |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 25: version: v1 |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 26: kind: Job |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 27: name: .* |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 28: patch: |- |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 29: - op: replace |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 30: path: /metadata/name |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 31: value: before-ehrorbookjava |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 32: - op: add |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 33: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 34: value: |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 35: name: CSI_MODULENAME |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 36: value: "csi-ehr-or-book-java-sev" |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 37: - op: add |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 38: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 39: value: |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 40: name: CSI_DATA_VERSION |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 41: value: "4.0.127.0" |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 42: - op: add |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 43: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 44: value: |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 45: name: CSI_PROJECT_NAME |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 46: value: "csi-ehr-or-book-java-sev" |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 47: - op: add |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 48: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 49: value: |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 50: name: CSI_MODULE_NAME |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 51: value: "csi-ehr-or-book-java-sev" |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 52: - op: add |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 53: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 54: value: |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 55: name: CSI_PARENT_MODULE_NAME |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 56: value: "ehr" |
| `ehr/csi-ehr-or-booking-java-sev` | Replaced Sync reference with DM-Initiator |
| `ehr/csi-ehr-or-booking-java-sev` | Added new sync-presync/sync-postsync Job patches |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 23: - target: |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 24: group: batch |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 25: version: v1 |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 26: kind: Job |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 27: name: .* |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 28: patch: |- |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 29: - op: replace |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 30: path: /metadata/name |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 31: value: before-ehrorbookingjava |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 32: - op: add |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 33: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 34: value: |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 35: name: CSI_MODULENAME |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 36: value: "csi-ehr-or-booking-java-sev" |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 37: - op: add |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 38: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 39: value: |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 40: name: CSI_DATA_VERSION |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 41: value: "4.0.127.0" |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 42: - op: add |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 43: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 44: value: |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 45: name: CSI_PROJECT_NAME |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 46: value: "csi-ehr-or-booking-java-sev" |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 47: - op: add |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 48: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 49: value: |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 50: name: CSI_MODULE_NAME |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 51: value: "csi-ehr-or-booking-java-sev" |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 52: - op: add |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 53: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 54: value: |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 55: name: CSI_PARENT_MODULE_NAME |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 56: value: "ehr" |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Replaced Sync reference with DM-Initiator |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Added new sync-presync/sync-postsync Job patches |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 23: - target: |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 24: group: batch |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 25: version: v1 |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 26: kind: Job |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 27: name: .* |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 28: patch: |- |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 29: - op: replace |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 30: path: /metadata/name |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 31: value: before-ehrspecializedclinicjava |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 32: namespace: moh-prod |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 33: - op: add |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 34: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 35: value: |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 36: name: CSI_MODULENAME |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 37: value: "csi-ehr-specialized-clinic-java-sev" |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 38: - op: add |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 39: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 40: value: |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 41: name: CSI_DATA_VERSION |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 42: value: "4.0.161.0" |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 43: - op: add |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 44: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 45: value: |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 46: name: CSI_PROJECT_NAME |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 47: value: "csi-ehr-specialized-clinic-java-sev" |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 48: - op: add |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 49: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 50: value: |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 51: name: CSI_MODULE_NAME |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 52: value: "csi-ehr-specialized-clinic-java-sev" |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 53: - op: add |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 54: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 55: value: |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 56: name: CSI_PARENT_MODULE_NAME |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 57: value: "ehr" |
| `ehr/csi-ehr-template-java-sev` | Replaced Sync reference with DM-Initiator |
| `ehr/csi-ehr-template-java-sev` | Added new sync-presync/sync-postsync Job patches |
| `ehr/csi-ehr-template-java-sev` | Commented out line 23: - target: |
| `ehr/csi-ehr-template-java-sev` | Commented out line 24: group: batch |
| `ehr/csi-ehr-template-java-sev` | Commented out line 25: version: v1 |
| `ehr/csi-ehr-template-java-sev` | Commented out line 26: kind: Job |
| `ehr/csi-ehr-template-java-sev` | Commented out line 27: name: .* |
| `ehr/csi-ehr-template-java-sev` | Commented out line 28: patch: |- |
| `ehr/csi-ehr-template-java-sev` | Commented out line 29: - op: replace |
| `ehr/csi-ehr-template-java-sev` | Commented out line 30: path: /metadata/name |
| `ehr/csi-ehr-template-java-sev` | Commented out line 31: value: before-ehrtemplatejava |
| `ehr/csi-ehr-template-java-sev` | Commented out line 32: - op: add |
| `ehr/csi-ehr-template-java-sev` | Commented out line 33: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-template-java-sev` | Commented out line 34: value: |
| `ehr/csi-ehr-template-java-sev` | Commented out line 35: name: CSI_MODULENAME |
| `ehr/csi-ehr-template-java-sev` | Commented out line 36: value: "csi-ehr-opd" |
| `ehr/csi-ehr-template-java-sev` | Commented out line 37: - op: add |
| `ehr/csi-ehr-template-java-sev` | Commented out line 38: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-template-java-sev` | Commented out line 39: value: |
| `ehr/csi-ehr-template-java-sev` | Commented out line 40: name: CSI_DATA_VERSION |
| `ehr/csi-ehr-template-java-sev` | Commented out line 41: value: "4.0.127.0" |
| `ehr/csi-ehr-template-java-sev` | Commented out line 42: - op: add |
| `ehr/csi-ehr-template-java-sev` | Commented out line 43: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-template-java-sev` | Commented out line 44: value: |
| `ehr/csi-ehr-template-java-sev` | Commented out line 45: name: CSI_PROJECT_NAME |
| `ehr/csi-ehr-template-java-sev` | Commented out line 46: value: "csi-ehr-template-java-sev" |
| `ehr/csi-ehr-template-java-sev` | Commented out line 47: - op: add |
| `ehr/csi-ehr-template-java-sev` | Commented out line 48: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-template-java-sev` | Commented out line 49: value: |
| `ehr/csi-ehr-template-java-sev` | Commented out line 50: name: CSI_MODULE_NAME |
| `ehr/csi-ehr-template-java-sev` | Commented out line 51: value: "csi-ehr-template-java-sev" |
| `ehr/csi-ehr-template-java-sev` | Commented out line 52: - op: add |
| `ehr/csi-ehr-template-java-sev` | Commented out line 53: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-template-java-sev` | Commented out line 54: value: |
| `ehr/csi-ehr-template-java-sev` | Commented out line 55: name: CSI_PARENT_MODULE_NAME |
| `ehr/csi-ehr-template-java-sev` | Commented out line 56: value: "ehr" |
| `ehr/csi-workflow-automation-service-java-sev` | Replaced commented Sync reference with commented DM-Initiator |
| `ehr/ehr-ic-ui` | Replaced Sync reference with DM-Initiator |
| `ehr/ehr-ic-ui` | Added new sync-presync/sync-postsync Job patches |
| `ehr/ehr-ic-ui` | Commented out line 26: - target: |
| `ehr/ehr-ic-ui` | Commented out line 27: group: batch |
| `ehr/ehr-ic-ui` | Commented out line 28: version: v1 |
| `ehr/ehr-ic-ui` | Commented out line 29: kind: Job |
| `ehr/ehr-ic-ui` | Commented out line 30: name: .* |
| `ehr/ehr-ic-ui` | Commented out line 31: patch: |- |
| `ehr/ehr-ic-ui` | Commented out line 32: - op: replace |
| `ehr/ehr-ic-ui` | Commented out line 33: path: /metadata/name |
| `ehr/ehr-ic-ui` | Commented out line 34: value: before-ehricui |
| `ehr/ehr-ic-ui` | Commented out line 35: - op: add |
| `ehr/ehr-ic-ui` | Commented out line 36: path: /spec/template/spec/containers/0/env/- |
| `ehr/ehr-ic-ui` | Commented out line 37: value: |
| `ehr/ehr-ic-ui` | Commented out line 38: name: CSI_MODULENAME |
| `ehr/ehr-ic-ui` | Commented out line 39: value: "csi-ehr-ic-ui" |
| `ehr/ehr-ic-ui` | Commented out line 40: - op: add |
| `ehr/ehr-ic-ui` | Commented out line 41: path: /spec/template/spec/containers/0/env/- |
| `ehr/ehr-ic-ui` | Commented out line 42: value: |
| `ehr/ehr-ic-ui` | Commented out line 43: name: CSI_DATA_VERSION |
| `ehr/ehr-ic-ui` | Commented out line 44: value: "4.2.464.0" |
| `ehr/ehr-ic-ui` | Commented out line 45: - op: add |
| `ehr/ehr-ic-ui` | Commented out line 46: path: /spec/template/spec/containers/0/env/- |
| `ehr/ehr-ic-ui` | Commented out line 47: value: |
| `ehr/ehr-ic-ui` | Commented out line 48: name: CSI_PROJECT_NAME |
| `ehr/ehr-ic-ui` | Commented out line 49: value: "ehr-ic-ui" |
| `ehr/ehr-ic-ui` | Commented out line 50: - op: add |
| `ehr/ehr-ic-ui` | Commented out line 51: path: /spec/template/spec/containers/0/env/- |
| `ehr/ehr-ic-ui` | Commented out line 52: value: |
| `ehr/ehr-ic-ui` | Commented out line 53: name: CSI_MODULE_NAME |
| `ehr/ehr-ic-ui` | Commented out line 54: value: "ehr-ic-ui" |
| `ehr/ehr-ic-ui` | Commented out line 55: - op: add |
| `ehr/ehr-ic-ui` | Commented out line 56: path: /spec/template/spec/containers/0/env/- |
| `ehr/ehr-ic-ui` | Commented out line 57: value: |
| `ehr/ehr-ic-ui` | Commented out line 58: name: CSI_PARENT_MODULE_NAME |
| `ehr/ehr-ic-ui` | Commented out line 59: value: "ehr" |
| `empi/csi-empi-api` | Replaced Sync reference with DM-Initiator |
| `empi/csi-empi-api` | Added new sync-presync/sync-postsync Job patches |
| `empi/csi-empi-api` | Commented out line 20: - target: |
| `empi/csi-empi-api` | Commented out line 21: group: batch |
| `empi/csi-empi-api` | Commented out line 22: version: v1 |
| `empi/csi-empi-api` | Commented out line 23: kind: Job |
| `empi/csi-empi-api` | Commented out line 24: name: .* |
| `empi/csi-empi-api` | Commented out line 25: patch: |- |
| `empi/csi-empi-api` | Commented out line 26: - op: replace |
| `empi/csi-empi-api` | Commented out line 27: path: /metadata/name |
| `empi/csi-empi-api` | Commented out line 28: value: before-csi-empi-api |
| `empi/csi-empi-api` | Commented out line 29: namespace: moh-uat |
| `empi/csi-empi-api` | Commented out line 30: - op: add |
| `empi/csi-empi-api` | Commented out line 31: path: /spec/template/spec/containers/0/env/- |
| `empi/csi-empi-api` | Commented out line 32: value: |
| `empi/csi-empi-api` | Commented out line 33: name: CSI_MODULENAME |
| `empi/csi-empi-api` | Commented out line 34: value: "csi-empi-api" |
| `empi/csi-empi-api` | Commented out line 35: - op: add |
| `empi/csi-empi-api` | Commented out line 36: path: /spec/template/spec/containers/0/env/- |
| `empi/csi-empi-api` | Commented out line 37: value: |
| `empi/csi-empi-api` | Commented out line 38: name: CSI_DATA_VERSION |
| `empi/csi-empi-api` | Commented out line 39: value: "4.1.170.0" |
| `empi/csi-empi-api` | Commented out line 40: - op: add |
| `empi/csi-empi-api` | Commented out line 41: path: /spec/template/spec/containers/0/env/- |
| `empi/csi-empi-api` | Commented out line 42: value: |
| `empi/csi-empi-api` | Commented out line 43: name: CSI_PROJECT_NAME |
| `empi/csi-empi-api` | Commented out line 44: value: "csi-empi-api" |
| `empi/csi-empi-api` | Commented out line 45: - op: add |
| `empi/csi-empi-api` | Commented out line 46: path: /spec/template/spec/containers/0/env/- |
| `empi/csi-empi-api` | Commented out line 47: value: |
| `empi/csi-empi-api` | Commented out line 48: name: CSI_MODULE_NAME |
| `empi/csi-empi-api` | Commented out line 49: value: "csi-empi-api" |
| `empi/csi-empi-api` | Commented out line 50: - op: add |
| `empi/csi-empi-api` | Commented out line 51: path: /spec/template/spec/containers/0/env/- |
| `empi/csi-empi-api` | Commented out line 52: value: |
| `empi/csi-empi-api` | Commented out line 53: name: CSI_PARENT_MODULE_NAME |
| `empi/csi-empi-api` | Commented out line 54: value: "empi" |
| `empi/csi-empi-webui` | Replaced commented Sync reference with commented DM-Initiator |
| `empi/csi-empi-webui` | Added new sync-presync/sync-postsync Job patches |
| `empi/csi-empi-webui` | Commented out line 22: - target: |
| `empi/csi-empi-webui` | Commented out line 23: group: batch |
| `empi/csi-empi-webui` | Commented out line 24: version: v1 |
| `empi/csi-empi-webui` | Commented out line 25: kind: Job |
| `empi/csi-empi-webui` | Commented out line 26: name: .* |
| `empi/csi-empi-webui` | Commented out line 27: patch: |- |
| `empi/csi-empi-webui` | Commented out line 28: - op: replace |
| `empi/csi-empi-webui` | Commented out line 29: path: /metadata/name |
| `empi/csi-empi-webui` | Commented out line 30: value: before-csi-empi-ui |
| `empi/csi-empi-webui` | Commented out line 31: namespace: moh-uat |
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
| `empi/csi-empi-webui` | Commented out line 51: value: "csi-empi-webui" |
| `empi/csi-empi-webui` | Commented out line 52: - op: add |
| `empi/csi-empi-webui` | Commented out line 53: path: /spec/template/spec/containers/0/env/- |
| `empi/csi-empi-webui` | Commented out line 54: value: |
| `empi/csi-empi-webui` | Commented out line 55: name: CSI_PARENT_MODULE_NAME |
| `empi/csi-empi-webui` | Commented out line 56: value: "empi" |
| `er/csi-ehr-er-functions-dotnet-sev` | Replaced Sync reference with DM-Initiator |
| `er/csi-ehr-er-functions-dotnet-sev` | Added new sync-presync/sync-postsync Job patches |
| `er/csi-ehr-er-functions-dotnet-sev` | Commented out line 26: - target: |
| `er/csi-ehr-er-functions-dotnet-sev` | Commented out line 27: group: batch |
| `er/csi-ehr-er-functions-dotnet-sev` | Commented out line 28: version: v1 |
| `er/csi-ehr-er-functions-dotnet-sev` | Commented out line 29: kind: Job |
| `er/csi-ehr-er-functions-dotnet-sev` | Commented out line 30: name: before |
| `er/csi-ehr-er-functions-dotnet-sev` | Commented out line 31: patch: |- |
| `er/csi-ehr-er-functions-dotnet-sev` | Commented out line 32: - op: replace |
| `er/csi-ehr-er-functions-dotnet-sev` | Commented out line 33: path: /metadata/name |
| `er/csi-ehr-er-functions-dotnet-sev` | Commented out line 34: value: before-erfunctiondotnet |
| `er/csi-ehr-er-functions-dotnet-sev` | Commented out line 35: - op: add |
| `er/csi-ehr-er-functions-dotnet-sev` | Commented out line 36: path: /spec/template/spec/containers/0/env/- |
| `er/csi-ehr-er-functions-dotnet-sev` | Commented out line 37: value: |
| `er/csi-ehr-er-functions-dotnet-sev` | Commented out line 38: name: CSI_DATA_VERSION |
| `er/csi-ehr-er-functions-dotnet-sev` | Commented out line 39: value: "4.1.28.20" |
| `er/csi-ehr-er-functions-dotnet-sev` | Commented out line 40: - op: add |
| `er/csi-ehr-er-functions-dotnet-sev` | Commented out line 41: path: /spec/template/spec/containers/0/env/- |
| `er/csi-ehr-er-functions-dotnet-sev` | Commented out line 42: value: |
| `er/csi-ehr-er-functions-dotnet-sev` | Commented out line 43: name: CSI_PROJECT_NAME |
| `er/csi-ehr-er-functions-dotnet-sev` | Commented out line 44: value: "csi-ehr-er-functions-dotnet-sev" |
| `er/csi-ehr-er-functions-dotnet-sev` | Commented out line 45: - op: add |
| `er/csi-ehr-er-functions-dotnet-sev` | Commented out line 46: path: /spec/template/spec/containers/0/env/- |
| `er/csi-ehr-er-functions-dotnet-sev` | Commented out line 47: value: |
| `er/csi-ehr-er-functions-dotnet-sev` | Commented out line 48: name: CSI_MODULE_NAME |
| `er/csi-ehr-er-functions-dotnet-sev` | Commented out line 49: value: "csi-ehr-er-functions-dotnet-sev" |
| `er/csi-ehr-er-functions-dotnet-sev` | Commented out line 50: - op: add |
| `er/csi-ehr-er-functions-dotnet-sev` | Commented out line 51: path: /spec/template/spec/containers/0/env/- |
| `er/csi-ehr-er-functions-dotnet-sev` | Commented out line 52: value: |
| `er/csi-ehr-er-functions-dotnet-sev` | Commented out line 53: name: CSI_PARENT_MODULE_NAME |
| `er/csi-ehr-er-functions-dotnet-sev` | Commented out line 54: value: "er" |
| `er/csi-ehr-er-functions-dotnet-sev` | Commented out line 55: - op: add |
| `er/csi-ehr-er-functions-dotnet-sev` | Commented out line 56: path: /spec/template/spec/containers/0/env/- |
| `er/csi-ehr-er-functions-dotnet-sev` | Commented out line 57: value: |
| `er/csi-ehr-er-functions-dotnet-sev` | Commented out line 58: name: isDropValidationDisabled |
| `er/csi-ehr-er-functions-dotnet-sev` | Commented out line 59: value: "true" |
| `er/csi-ehr-er-ui` | Replaced Sync reference with DM-Initiator |
| `er/csi-ehr-er-ui` | Added new sync-presync/sync-postsync Job patches |
| `er/csi-ehr-er-ui` | Commented out line 23: - target: |
| `er/csi-ehr-er-ui` | Commented out line 24: group: batch |
| `er/csi-ehr-er-ui` | Commented out line 25: version: v1 |
| `er/csi-ehr-er-ui` | Commented out line 26: kind: Job |
| `er/csi-ehr-er-ui` | Commented out line 27: name: .* |
| `er/csi-ehr-er-ui` | Commented out line 28: patch: |- |
| `er/csi-ehr-er-ui` | Commented out line 29: - op: replace |
| `er/csi-ehr-er-ui` | Commented out line 30: path: /metadata/name |
| `er/csi-ehr-er-ui` | Commented out line 31: value: before-ehrerui |
| `er/csi-ehr-er-ui` | Commented out line 32: namespace: moh-uat |
| `er/csi-ehr-er-ui` | Commented out line 33: - op: add |
| `er/csi-ehr-er-ui` | Commented out line 34: path: /spec/template/spec/containers/0/env/- |
| `er/csi-ehr-er-ui` | Commented out line 35: value: |
| `er/csi-ehr-er-ui` | Commented out line 36: name: CSI_MODULENAME |
| `er/csi-ehr-er-ui` | Commented out line 37: value: "csi-ehr-er-ui" |
| `er/csi-ehr-er-ui` | Commented out line 38: - op: add |
| `er/csi-ehr-er-ui` | Commented out line 39: path: /spec/template/spec/containers/0/env/- |
| `er/csi-ehr-er-ui` | Commented out line 40: value: |
| `er/csi-ehr-er-ui` | Commented out line 41: name: CSI_DATA_VERSION |
| `er/csi-ehr-er-ui` | Commented out line 42: value: "4.1.19.22-hf2" |
| `er/csi-ehr-er-ui` | Commented out line 43: - op: add |
| `er/csi-ehr-er-ui` | Commented out line 44: path: /spec/template/spec/containers/0/env/- |
| `er/csi-ehr-er-ui` | Commented out line 45: value: |
| `er/csi-ehr-er-ui` | Commented out line 46: name: CSI_PROJECT_NAME |
| `er/csi-ehr-er-ui` | Commented out line 47: value: "csi-ehr-er-ui" |
| `er/csi-ehr-er-ui` | Commented out line 48: - op: add |
| `er/csi-ehr-er-ui` | Commented out line 49: path: /spec/template/spec/containers/0/env/- |
| `er/csi-ehr-er-ui` | Commented out line 50: value: |
| `er/csi-ehr-er-ui` | Commented out line 51: name: CSI_MODULE_NAME |
| `er/csi-ehr-er-ui` | Commented out line 52: value: "csi-ehr-er-ui" |
| `er/csi-ehr-er-ui` | Commented out line 53: - op: add |
| `er/csi-ehr-er-ui` | Commented out line 54: path: /spec/template/spec/containers/0/env/- |
| `er/csi-ehr-er-ui` | Commented out line 55: value: |
| `er/csi-ehr-er-ui` | Commented out line 56: name: CSI_PARENT_MODULE_NAME |
| `er/csi-ehr-er-ui` | Commented out line 57: value: "er" |
| `him/csi-health-information-srv` | Replaced Sync reference with DM-Initiator |
| `him/csi-health-information-srv` | Added new sync-presync/sync-postsync Job patches |
| `him/csi-health-information-srv` | Commented out line 23: - target: |
| `him/csi-health-information-srv` | Commented out line 24: group: batch |
| `him/csi-health-information-srv` | Commented out line 25: version: v1 |
| `him/csi-health-information-srv` | Commented out line 26: kind: Job |
| `him/csi-health-information-srv` | Commented out line 27: name: .* |
| `him/csi-health-information-srv` | Commented out line 28: patch: | |
| `him/csi-health-information-srv` | Commented out line 29: - op: replace |
| `him/csi-health-information-srv` | Commented out line 30: path: /metadata/name |
| `him/csi-health-information-srv` | Commented out line 31: value: before-csi-net-himservi |
| `him/csi-health-information-srv` | Commented out line 32: namespace: moh-uat |
| `him/csi-health-information-srv` | Commented out line 33: - op: add |
| `him/csi-health-information-srv` | Commented out line 34: path: /spec/template/spec/containers/0/env/- |
| `him/csi-health-information-srv` | Commented out line 35: value: |
| `him/csi-health-information-srv` | Commented out line 36: name: CSI_MODULENAME |
| `him/csi-health-information-srv` | Commented out line 37: value: "csi-health-information-srv" |
| `him/csi-health-information-srv` | Commented out line 38: - op: add |
| `him/csi-health-information-srv` | Commented out line 39: path: /spec/template/spec/containers/0/env/- |
| `him/csi-health-information-srv` | Commented out line 40: value: |
| `him/csi-health-information-srv` | Commented out line 41: name: CSI_DATA_VERSION |
| `him/csi-health-information-srv` | Commented out line 42: value: "4.1.28.20" |
| `him/csi-health-information-srv` | Commented out line 43: - op: add |
| `him/csi-health-information-srv` | Commented out line 44: path: /spec/template/spec/containers/0/env/- |
| `him/csi-health-information-srv` | Commented out line 45: value: |
| `him/csi-health-information-srv` | Commented out line 46: name: CSI_PROJECT_NAME |
| `him/csi-health-information-srv` | Commented out line 47: value: "csi-health-information-srv" |
| `him/csi-health-information-srv` | Commented out line 48: - op: add |
| `him/csi-health-information-srv` | Commented out line 49: path: /spec/template/spec/containers/0/env/- |
| `him/csi-health-information-srv` | Commented out line 50: value: |
| `him/csi-health-information-srv` | Commented out line 51: name: CSI_MODULE_NAME |
| `him/csi-health-information-srv` | Commented out line 52: value: "csi-health-information-srv" |
| `him/csi-health-information-srv` | Commented out line 53: - op: add |
| `him/csi-health-information-srv` | Commented out line 54: path: /spec/template/spec/containers/0/env/- |
| `him/csi-health-information-srv` | Commented out line 55: value: |
| `him/csi-health-information-srv` | Commented out line 56: name: CSI_PARENT_MODULE_NAME |
| `him/csi-health-information-srv` | Commented out line 57: value: "him" |
| `him/csi-him-ui` | Replaced Sync reference with DM-Initiator |
| `him/csi-him-ui` | Added new sync-presync/sync-postsync Job patches |
| `him/csi-him-ui` | Commented out line 24: - target: |
| `him/csi-him-ui` | Commented out line 25: group: batch |
| `him/csi-him-ui` | Commented out line 26: version: v1 |
| `him/csi-him-ui` | Commented out line 27: kind: Job |
| `him/csi-him-ui` | Commented out line 28: name: .* |
| `him/csi-him-ui` | Commented out line 29: patch: |- |
| `him/csi-him-ui` | Commented out line 30: - op: replace |
| `him/csi-him-ui` | Commented out line 31: path: /metadata/name |
| `him/csi-him-ui` | Commented out line 32: value: before-csi-him-ui |
| `him/csi-him-ui` | Commented out line 33: namespace: moh-uat |
| `him/csi-him-ui` | Commented out line 34: - op: add |
| `him/csi-him-ui` | Commented out line 35: path: /spec/template/spec/containers/0/env/- |
| `him/csi-him-ui` | Commented out line 36: value: |
| `him/csi-him-ui` | Commented out line 37: name: CSI_MODULENAME |
| `him/csi-him-ui` | Commented out line 38: value: "csi-him-ui" |
| `him/csi-him-ui` | Commented out line 39: - op: add |
| `him/csi-him-ui` | Commented out line 40: path: /spec/template/spec/containers/0/env/- |
| `him/csi-him-ui` | Commented out line 41: value: |
| `him/csi-him-ui` | Commented out line 42: name: CSI_DATA_VERSION |
| `him/csi-him-ui` | Commented out line 43: value: "4.3.234.0" |
| `him/csi-him-ui` | Commented out line 44: - op: add |
| `him/csi-him-ui` | Commented out line 45: path: /spec/template/spec/containers/0/env/- |
| `him/csi-him-ui` | Commented out line 46: value: |
| `him/csi-him-ui` | Commented out line 47: name: CSI_PROJECT_NAME |
| `him/csi-him-ui` | Commented out line 48: value: "csi-him-ui" |
| `him/csi-him-ui` | Commented out line 49: - op: add |
| `him/csi-him-ui` | Commented out line 50: path: /spec/template/spec/containers/0/env/- |
| `him/csi-him-ui` | Commented out line 51: value: |
| `him/csi-him-ui` | Commented out line 52: name: CSI_MODULE_NAME |
| `him/csi-him-ui` | Commented out line 53: value: "csi-him-ui" |
| `him/csi-him-ui` | Commented out line 54: - op: add |
| `him/csi-him-ui` | Commented out line 55: path: /spec/template/spec/containers/0/env/- |
| `him/csi-him-ui` | Commented out line 56: value: |
| `him/csi-him-ui` | Commented out line 57: name: CSI_PARENT_MODULE_NAME |
| `him/csi-him-ui` | Commented out line 58: value: "him" |
| `integration/csi-ie-general` | Replaced Sync reference with DM-Initiator |
| `integration/csi-ie-general` | Added new sync-presync/sync-postsync Job patches |
| `integration/csi-ie-general` | Commented out line 25: - target: |
| `integration/csi-ie-general` | Commented out line 26: group: batch |
| `integration/csi-ie-general` | Commented out line 27: version: v1 |
| `integration/csi-ie-general` | Commented out line 28: kind: Job |
| `integration/csi-ie-general` | Commented out line 29: name: before |
| `integration/csi-ie-general` | Commented out line 30: patch: | |
| `integration/csi-ie-general` | Commented out line 31: - op: replace |
| `integration/csi-ie-general` | Commented out line 32: path: /metadata/name |
| `integration/csi-ie-general` | Commented out line 33: value: before-csi-ie-general |
| `integration/csi-ie-general` | Commented out line 34: - op: add |
| `integration/csi-ie-general` | Commented out line 35: path: /spec/template/spec/containers/0/env/- |
| `integration/csi-ie-general` | Commented out line 36: value: |
| `integration/csi-ie-general` | Commented out line 37: name: CSI_MODULENAME |
| `integration/csi-ie-general` | Commented out line 38: value: "csi-ie-general" |
| `integration/csi-ie-general` | Commented out line 39: - op: add |
| `integration/csi-ie-general` | Commented out line 40: path: /spec/template/spec/containers/0/env/- |
| `integration/csi-ie-general` | Commented out line 41: value: |
| `integration/csi-ie-general` | Commented out line 42: name: CSI_DATA_VERSION |
| `integration/csi-ie-general` | Commented out line 43: value: "4.2.502.0" |
| `integration/csi-ie-general` | Commented out line 44: - op: add |
| `integration/csi-ie-general` | Commented out line 45: path: /spec/template/spec/containers/0/env/- |
| `integration/csi-ie-general` | Commented out line 46: value: |
| `integration/csi-ie-general` | Commented out line 47: name: CSI_PROJECT_NAME |
| `integration/csi-ie-general` | Commented out line 48: value: "csi-ie-general" |
| `integration/csi-ie-general` | Commented out line 49: - op: add |
| `integration/csi-ie-general` | Commented out line 50: path: /spec/template/spec/containers/0/env/- |
| `integration/csi-ie-general` | Commented out line 51: value: |
| `integration/csi-ie-general` | Commented out line 52: name: CSI_MODULE_NAME |
| `integration/csi-ie-general` | Commented out line 53: value: "csi-ie-general" |
| `integration/csi-ie-general` | Commented out line 54: - op: add |
| `integration/csi-ie-general` | Commented out line 55: path: /spec/template/spec/containers/0/env/- |
| `integration/csi-ie-general` | Commented out line 56: value: |
| `integration/csi-ie-general` | Commented out line 57: name: CSI_PARENT_MODULE_NAME |
| `integration/csi-ie-general` | Commented out line 58: value: "integration" |
| `integration/csi-ie-general` | Commented out line 59: - op: add |
| `integration/csi-ie-general` | Commented out line 60: path: /spec/template/spec/containers/0/env/- |
| `integration/csi-ie-general` | Commented out line 61: value: |
| `integration/csi-ie-general` | Commented out line 62: name: isDropValidationDisabled |
| `integration/csi-ie-general` | Commented out line 63: value: "true" |
| `integration/csi-ie-mobile` | Replaced Sync reference with DM-Initiator |
| `integration/csi-ie-mobile` | Added new sync-presync/sync-postsync Job patches |
| `integration/csi-ie-mobile` | Commented out line 21: - target: |
| `integration/csi-ie-mobile` | Commented out line 22: group: batch |
| `integration/csi-ie-mobile` | Commented out line 23: version: v1 |
| `integration/csi-ie-mobile` | Commented out line 24: kind: Job |
| `integration/csi-ie-mobile` | Commented out line 25: name: before |
| `integration/csi-ie-mobile` | Commented out line 26: patch: | |
| `integration/csi-ie-mobile` | Commented out line 27: - op: replace |
| `integration/csi-ie-mobile` | Commented out line 28: path: /metadata/name |
| `integration/csi-ie-mobile` | Commented out line 29: value: before-csi-ie-mobile |
| `integration/csi-ie-mobile` | Commented out line 30: - op: add |
| `integration/csi-ie-mobile` | Commented out line 31: path: /spec/template/spec/containers/0/env/- |
| `integration/csi-ie-mobile` | Commented out line 32: value: |
| `integration/csi-ie-mobile` | Commented out line 33: name: CSI_MODULENAME |
| `integration/csi-ie-mobile` | Commented out line 34: value: "csi-ie-mobile" |
| `integration/csi-ie-mobile` | Commented out line 35: - op: add |
| `integration/csi-ie-mobile` | Commented out line 36: path: /spec/template/spec/containers/0/env/- |
| `integration/csi-ie-mobile` | Commented out line 37: value: |
| `integration/csi-ie-mobile` | Commented out line 38: name: CSI_DATA_VERSION |
| `integration/csi-ie-mobile` | Commented out line 39: value: "4.2.502.0" |
| `integration/csi-ie-mobile` | Commented out line 40: - op: add |
| `integration/csi-ie-mobile` | Commented out line 41: path: /spec/template/spec/containers/0/env/- |
| `integration/csi-ie-mobile` | Commented out line 42: value: |
| `integration/csi-ie-mobile` | Commented out line 43: name: CSI_PROJECT_NAME |
| `integration/csi-ie-mobile` | Commented out line 44: value: "csi-ie-mobile" |
| `integration/csi-ie-mobile` | Commented out line 45: - op: add |
| `integration/csi-ie-mobile` | Commented out line 46: path: /spec/template/spec/containers/0/env/- |
| `integration/csi-ie-mobile` | Commented out line 47: value: |
| `integration/csi-ie-mobile` | Commented out line 48: name: CSI_MODULE_NAME |
| `integration/csi-ie-mobile` | Commented out line 49: value: "csi-ie-mobile" |
| `integration/csi-ie-mobile` | Commented out line 50: - op: add |
| `integration/csi-ie-mobile` | Commented out line 51: path: /spec/template/spec/containers/0/env/- |
| `integration/csi-ie-mobile` | Commented out line 52: value: |
| `integration/csi-ie-mobile` | Commented out line 53: name: CSI_PARENT_MODULE_NAME |
| `integration/csi-ie-mobile` | Commented out line 54: value: "integration" |
| `lab/lab-labgui` | Replaced Sync reference with DM-Initiator |
| `lab/lab-labgui` | Added new sync-presync/sync-postsync Job patches |
| `lab/lab-labgui` | Commented out line 23: - target: |
| `lab/lab-labgui` | Commented out line 24: group: batch |
| `lab/lab-labgui` | Commented out line 25: version: v1 |
| `lab/lab-labgui` | Commented out line 26: kind: Job |
| `lab/lab-labgui` | Commented out line 27: name: .* |
| `lab/lab-labgui` | Commented out line 28: patch: |- |
| `lab/lab-labgui` | Commented out line 29: - op: replace |
| `lab/lab-labgui` | Commented out line 30: path: /metadata/name |
| `lab/lab-labgui` | Commented out line 31: value: before-labui |
| `lab/lab-labgui` | Commented out line 32: - op: add |
| `lab/lab-labgui` | Commented out line 33: path: /spec/template/spec/containers/0/env/- |
| `lab/lab-labgui` | Commented out line 34: value: |
| `lab/lab-labgui` | Commented out line 35: name: CSI_MODULENAME |
| `lab/lab-labgui` | Commented out line 36: value: "lab-labgui" |
| `lab/lab-labgui` | Commented out line 37: - op: add |
| `lab/lab-labgui` | Commented out line 38: path: /spec/template/spec/containers/0/env/- |
| `lab/lab-labgui` | Commented out line 39: value: |
| `lab/lab-labgui` | Commented out line 40: name: CSI_DATA_VERSION |
| `lab/lab-labgui` | Commented out line 41: value: "4.0.127.0" |
| `lab/lab-labgui` | Commented out line 42: - op: add |
| `lab/lab-labgui` | Commented out line 43: path: /spec/template/spec/containers/0/env/- |
| `lab/lab-labgui` | Commented out line 44: value: |
| `lab/lab-labgui` | Commented out line 45: name: CSI_PROJECT_NAME |
| `lab/lab-labgui` | Commented out line 46: value: "lab-labgui" |
| `lab/lab-labgui` | Commented out line 47: - op: add |
| `lab/lab-labgui` | Commented out line 48: path: /spec/template/spec/containers/0/env/- |
| `lab/lab-labgui` | Commented out line 49: value: |
| `lab/lab-labgui` | Commented out line 50: name: CSI_MODULE_NAME |
| `lab/lab-labgui` | Commented out line 51: value: "lab-labgui" |
| `lab/lab-labgui` | Commented out line 52: - op: add |
| `lab/lab-labgui` | Commented out line 53: path: /spec/template/spec/containers/0/env/- |
| `lab/lab-labgui` | Commented out line 54: value: |
| `lab/lab-labgui` | Commented out line 55: name: CSI_PARENT_MODULE_NAME |
| `lab/lab-labgui` | Commented out line 56: value: "lab" |
| `lab/lab-labmgt-srv` | Replaced Sync reference with DM-Initiator |
| `lab/lab-labmgt-srv` | Added new sync-presync/sync-postsync Job patches |
| `lab/lab-labmgt-srv` | Commented out line 25: - target: |
| `lab/lab-labmgt-srv` | Commented out line 26: group: batch |
| `lab/lab-labmgt-srv` | Commented out line 27: version: v1 |
| `lab/lab-labmgt-srv` | Commented out line 28: kind: Job |
| `lab/lab-labmgt-srv` | Commented out line 29: name: data-migration-presync |
| `lab/lab-labmgt-srv` | Commented out line 30: patch: |- |
| `lab/lab-labmgt-srv` | Commented out line 31: - op: replace |
| `lab/lab-labmgt-srv` | Commented out line 32: path: /metadata/name |
| `lab/lab-labmgt-srv` | Commented out line 33: value: data-migration-presync-labmgmtdotnet |
| `lab/lab-labmgt-srv` | Commented out line 34: - op: add |
| `lab/lab-labmgt-srv` | Commented out line 35: path: /spec/template/spec/containers/0/env/- |
| `lab/lab-labmgt-srv` | Commented out line 36: value: |
| `lab/lab-labmgt-srv` | Commented out line 37: name: CSI_MODULENAME |
| `lab/lab-labmgt-srv` | Commented out line 38: value: "lab-labmgt_srv" |
| `lab/lab-labmgt-srv` | Commented out line 39: - op: add |
| `lab/lab-labmgt-srv` | Commented out line 40: path: /spec/template/spec/containers/0/env/- |
| `lab/lab-labmgt-srv` | Commented out line 41: value: |
| `lab/lab-labmgt-srv` | Commented out line 42: name: CSI_DATA_VERSION |
| `lab/lab-labmgt-srv` | Commented out line 43: value: "4.1.28.20" |
| `lab/lab-labmgt-srv` | Commented out line 44: - op: add |
| `lab/lab-labmgt-srv` | Commented out line 45: path: /spec/template/spec/containers/0/env/- |
| `lab/lab-labmgt-srv` | Commented out line 46: value: |
| `lab/lab-labmgt-srv` | Commented out line 47: name: CSI_PROJECT_NAME |
| `lab/lab-labmgt-srv` | Commented out line 48: value: "lab-labmgt_srv" |
| `lab/lab-labmgt-srv` | Commented out line 49: - op: add |
| `lab/lab-labmgt-srv` | Commented out line 50: path: /spec/template/spec/containers/0/env/- |
| `lab/lab-labmgt-srv` | Commented out line 51: value: |
| `lab/lab-labmgt-srv` | Commented out line 52: name: CSI_MODULE_NAME |
| `lab/lab-labmgt-srv` | Commented out line 53: value: "lab-labmgt-srv" |
| `lab/lab-labmgt-srv` | Commented out line 54: - op: add |
| `lab/lab-labmgt-srv` | Commented out line 55: path: /spec/template/spec/containers/0/env/- |
| `lab/lab-labmgt-srv` | Commented out line 56: value: |
| `lab/lab-labmgt-srv` | Commented out line 57: name: CSI_PARENT_MODULE_NAME |
| `lab/lab-labmgt-srv` | Commented out line 58: value: "lab" |
| `lab/lab-labmgt-srv` | Commented out line 59: - op: add |
| `lab/lab-labmgt-srv` | Commented out line 60: path: /spec/template/spec/containers/0/env/- |
| `lab/lab-labmgt-srv` | Commented out line 61: value: |
| `lab/lab-labmgt-srv` | Commented out line 62: name: isDropValidationDisabled |
| `lab/lab-labmgt-srv` | Commented out line 63: value: "true" |
| `lab/lab-labmgt-srv` | Commented out line 65: - target: |
| `lab/lab-labmgt-srv` | Commented out line 66: group: batch |
| `lab/lab-labmgt-srv` | Commented out line 67: version: v1 |
| `lab/lab-labmgt-srv` | Commented out line 68: kind: Job |
| `lab/lab-labmgt-srv` | Commented out line 69: name: data-migration-postsync |
| `lab/lab-labmgt-srv` | Commented out line 70: patch: |- |
| `lab/lab-labmgt-srv` | Commented out line 71: - op: replace |
| `lab/lab-labmgt-srv` | Commented out line 72: path: /metadata/name |
| `lab/lab-labmgt-srv` | Commented out line 73: value: data-migration-postsync-labmgmtdotnet |
| `lab/lab-labmgt-srv` | Commented out line 74: - op: add |
| `lab/lab-labmgt-srv` | Commented out line 75: path: /spec/template/spec/containers/0/env/- |
| `lab/lab-labmgt-srv` | Commented out line 76: value: |
| `lab/lab-labmgt-srv` | Commented out line 77: name: CSI_MODULENAME |
| `lab/lab-labmgt-srv` | Commented out line 78: value: "lab-labmgt_srv" |
| `lab/lab-labmgt-srv` | Commented out line 79: - op: add |
| `lab/lab-labmgt-srv` | Commented out line 80: path: /spec/template/spec/containers/0/env/- |
| `lab/lab-labmgt-srv` | Commented out line 81: value: |
| `lab/lab-labmgt-srv` | Commented out line 82: name: CSI_DATA_VERSION |
| `lab/lab-labmgt-srv` | Commented out line 83: value: "4.1.28.20" |
| `lab/lab-labmgt-srv` | Commented out line 84: - op: add |
| `lab/lab-labmgt-srv` | Commented out line 85: path: /spec/template/spec/containers/0/env/- |
| `lab/lab-labmgt-srv` | Commented out line 86: value: |
| `lab/lab-labmgt-srv` | Commented out line 87: name: CSI_PROJECT_NAME |
| `lab/lab-labmgt-srv` | Commented out line 88: value: "lab-labmgt_srv" |
| `lab/lab-labmgt-srv` | Commented out line 89: - op: add |
| `lab/lab-labmgt-srv` | Commented out line 90: path: /spec/template/spec/containers/0/env/- |
| `lab/lab-labmgt-srv` | Commented out line 91: value: |
| `lab/lab-labmgt-srv` | Commented out line 92: name: CSI_MODULE_NAME |
| `lab/lab-labmgt-srv` | Commented out line 93: value: "lab-labmgt-srv" |
| `lab/lab-labmgt-srv` | Commented out line 94: - op: add |
| `lab/lab-labmgt-srv` | Commented out line 95: path: /spec/template/spec/containers/0/env/- |
| `lab/lab-labmgt-srv` | Commented out line 96: value: |
| `lab/lab-labmgt-srv` | Commented out line 97: name: CSI_PARENT_MODULE_NAME |
| `lab/lab-labmgt-srv` | Commented out line 98: value: "lab" |
| `lab/lab-labmgt-srv` | Commented out line 99: - op: add |
| `lab/lab-labmgt-srv` | Commented out line 100: path: /spec/template/spec/containers/0/env/- |
| `lab/lab-labmgt-srv` | Commented out line 101: value: |
| `lab/lab-labmgt-srv` | Commented out line 102: name: isDropValidationDisabled |
| `lab/lab-labmgt-srv` | Commented out line 103: value: "true" |
| `lab/lab-scheduled` | Replaced Sync reference with DM-Initiator |
| `lab/lab-scheduled` | Added new sync-presync/sync-postsync Job patches |
| `lab/lab-scheduled` | Commented out line 24: - target: |
| `lab/lab-scheduled` | Commented out line 25: group: batch |
| `lab/lab-scheduled` | Commented out line 26: version: v1 |
| `lab/lab-scheduled` | Commented out line 27: kind: Job |
| `lab/lab-scheduled` | Commented out line 28: name: .* |
| `lab/lab-scheduled` | Commented out line 29: patch: |- |
| `lab/lab-scheduled` | Commented out line 30: - op: replace |
| `lab/lab-scheduled` | Commented out line 31: path: /metadata/name |
| `lab/lab-scheduled` | Commented out line 32: value: before-labscheduled |
| `lab/lab-scheduled` | Commented out line 33: - op: add |
| `lab/lab-scheduled` | Commented out line 34: path: /metadata/namespace |
| `lab/lab-scheduled` | Commented out line 35: value: moh-uat |
| `lab/lab-scheduled` | Commented out line 36: - op: add |
| `lab/lab-scheduled` | Commented out line 37: path: /spec/template/spec/containers/0/env/- |
| `lab/lab-scheduled` | Commented out line 38: value: |
| `lab/lab-scheduled` | Commented out line 39: name: CSI_MODULENAME |
| `lab/lab-scheduled` | Commented out line 40: value: "lab-scheduled" |
| `lab/lab-scheduled` | Commented out line 41: - op: add |
| `lab/lab-scheduled` | Commented out line 42: path: /spec/template/spec/containers/0/env/- |
| `lab/lab-scheduled` | Commented out line 43: value: |
| `lab/lab-scheduled` | Commented out line 44: name: CSI_DATA_VERSION |
| `lab/lab-scheduled` | Commented out line 45: value: "4.0.127.0" |
| `lab/lab-scheduled` | Commented out line 46: - op: add |
| `lab/lab-scheduled` | Commented out line 47: path: /spec/template/spec/containers/0/env/- |
| `lab/lab-scheduled` | Commented out line 48: value: |
| `lab/lab-scheduled` | Commented out line 49: name: CSI_PROJECT_NAME |
| `lab/lab-scheduled` | Commented out line 50: value: "csi-net-lab-scheduled" |
| `lab/lab-scheduled` | Commented out line 51: - op: add |
| `lab/lab-scheduled` | Commented out line 52: path: /spec/template/spec/containers/0/env/- |
| `lab/lab-scheduled` | Commented out line 53: value: |
| `lab/lab-scheduled` | Commented out line 54: name: CSI_MODULE_NAME |
| `lab/lab-scheduled` | Commented out line 55: value: "lab-scheduled" |
| `lab/lab-scheduled` | Commented out line 56: - op: add |
| `lab/lab-scheduled` | Commented out line 57: path: /spec/template/spec/containers/0/env/- |
| `lab/lab-scheduled` | Commented out line 58: value: |
| `lab/lab-scheduled` | Commented out line 59: name: CSI_PARENT_MODULE_NAME |
| `lab/lab-scheduled` | Commented out line 60: value: "lab" |
| `lab/lab-vidaptor-integration` | Replaced commented Sync reference with commented DM-Initiator |
| `lab/lab-vidaptor-integration` | Added new sync-presync/sync-postsync Job patches |
| `lab/lab-vidaptor-integration` | Commented out line 24: - target: |
| `lab/lab-vidaptor-integration` | Commented out line 25: group: batch |
| `lab/lab-vidaptor-integration` | Commented out line 26: version: v1 |
| `lab/lab-vidaptor-integration` | Commented out line 27: kind: Job |
| `lab/lab-vidaptor-integration` | Commented out line 28: name: .* |
| `lab/lab-vidaptor-integration` | Commented out line 29: patch: |- |
| `lab/lab-vidaptor-integration` | Commented out line 30: - op: replace |
| `lab/lab-vidaptor-integration` | Commented out line 31: path: /metadata/name |
| `lab/lab-vidaptor-integration` | Commented out line 32: value: before-labvidaptor |
| `lab/lab-vidaptor-integration` | Commented out line 33: - op: add |
| `lab/lab-vidaptor-integration` | Commented out line 34: path: /metadata/namespace |
| `lab/lab-vidaptor-integration` | Commented out line 35: value: moh-uat |
| `lab/lab-vidaptor-integration` | Commented out line 36: - op: add |
| `lab/lab-vidaptor-integration` | Commented out line 37: path: /spec/template/spec/containers/0/env/- |
| `lab/lab-vidaptor-integration` | Commented out line 38: value: |
| `lab/lab-vidaptor-integration` | Commented out line 39: name: CSI_MODULENAME |
| `lab/lab-vidaptor-integration` | Commented out line 40: value: "lab-vidaptorIntegration" |
| `lab/lab-vidaptor-integration` | Commented out line 41: - op: add |
| `lab/lab-vidaptor-integration` | Commented out line 42: path: /spec/template/spec/containers/0/env/- |
| `lab/lab-vidaptor-integration` | Commented out line 43: value: |
| `lab/lab-vidaptor-integration` | Commented out line 44: name: CSI_DATA_VERSION |
| `lab/lab-vidaptor-integration` | Commented out line 45: value: "4.0.127.0" |
| `notification/csi-vidaplus-external` | Updated Deployment target name: csi-net-ext -> csi-vidaplus-external |
| `notification/csi-vidaplus-external` | Updated Deployment target name: csi-net-ext -> csi-vidaplus-external |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Replaced Sync reference with DM-Initiator |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Added new sync-presync/sync-postsync Job patches |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 23: - target: |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 24: group: batch |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 25: version: v1 |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 26: kind: Job |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 27: name: .* |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 28: patch: | |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 29: - op: replace |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 30: path: /metadata/name |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 31: value: before-ehripprescriptionjava |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 32: namespace: moh-uat |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 33: - op: add |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 34: path: /spec/template/spec/containers/0/env/- |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 35: value: |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 36: name: CSI_MODULENAME |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 37: value: "csi-java-ehr-ip-doctor-prescription" |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 38: - op: add |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 39: path: /spec/template/spec/containers/0/env/- |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 40: value: |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 41: name: CSI_DATA_VERSION |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 42: value: "4.0.127.0" |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 43: - op: add |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 44: path: /spec/template/spec/containers/0/env/- |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 45: value: |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 46: name: CSI_PROJECT_NAME |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 47: value: "csi-java-ehr-ip-doctor-prescription" |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 48: - op: add |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 49: path: /spec/template/spec/containers/0/env/- |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 50: value: |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 51: name: CSI_MODULE_NAME |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 52: value: "csi-java-ehr-ip-doctor-prescription" |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 53: - op: add |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 54: path: /spec/template/spec/containers/0/env/- |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 55: value: |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 56: name: CSI_PARENT_MODULE_NAME |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 57: value: "pharmacy" |
| `pharmacy/csi-phr-base` | Replaced Sync reference with DM-Initiator |
| `pharmacy/csi-phr-base` | Added new sync-presync/sync-postsync Job patches |
| `pharmacy/csi-phr-base` | Commented out line 23: - target: |
| `pharmacy/csi-phr-base` | Commented out line 24: group: batch |
| `pharmacy/csi-phr-base` | Commented out line 25: version: v1 |
| `pharmacy/csi-phr-base` | Commented out line 26: kind: Job |
| `pharmacy/csi-phr-base` | Commented out line 27: name: .* |
| `pharmacy/csi-phr-base` | Commented out line 28: patch: | |
| `pharmacy/csi-phr-base` | Commented out line 29: - op: replace |
| `pharmacy/csi-phr-base` | Commented out line 30: path: /metadata/name |
| `pharmacy/csi-phr-base` | Commented out line 31: value: before-phrbasejava |
| `pharmacy/csi-phr-base` | Commented out line 32: namespace: moh-uat |
| `pharmacy/csi-phr-base` | Commented out line 33: - op: add |
| `pharmacy/csi-phr-base` | Commented out line 34: path: /spec/template/spec/containers/0/env/- |
| `pharmacy/csi-phr-base` | Commented out line 35: value: |
| `pharmacy/csi-phr-base` | Commented out line 36: name: CSI_MODULENAME |
| `pharmacy/csi-phr-base` | Commented out line 37: value: "csi-phr-base" |
| `pharmacy/csi-phr-base` | Commented out line 38: - op: add |
| `pharmacy/csi-phr-base` | Commented out line 39: path: /spec/template/spec/containers/0/env/- |
| `pharmacy/csi-phr-base` | Commented out line 40: value: |
| `pharmacy/csi-phr-base` | Commented out line 41: name: CSI_DATA_VERSION |
| `pharmacy/csi-phr-base` | Commented out line 42: value: "4.2.15.0" |
| `pharmacy/csi-phr-base` | Commented out line 43: - op: add |
| `pharmacy/csi-phr-base` | Commented out line 44: path: /spec/template/spec/containers/0/env/- |
| `pharmacy/csi-phr-base` | Commented out line 45: value: |
| `pharmacy/csi-phr-base` | Commented out line 46: name: CSI_PROJECT_NAME |
| `pharmacy/csi-phr-base` | Commented out line 47: value: "csi-phr-base" |
| `pharmacy/csi-phr-base` | Commented out line 48: - op: add |
| `pharmacy/csi-phr-base` | Commented out line 49: path: /spec/template/spec/containers/0/env/- |
| `pharmacy/csi-phr-base` | Commented out line 50: value: |
| `pharmacy/csi-phr-base` | Commented out line 51: name: CSI_MODULE_NAME |
| `pharmacy/csi-phr-base` | Commented out line 52: value: "csi-phr-base" |
| `pharmacy/csi-phr-base` | Commented out line 53: - op: add |
| `pharmacy/csi-phr-base` | Commented out line 54: path: /spec/template/spec/containers/0/env/- |
| `pharmacy/csi-phr-base` | Commented out line 55: value: |
| `pharmacy/csi-phr-base` | Commented out line 56: name: CSI_PARENT_MODULE_NAME |
| `pharmacy/csi-phr-base` | Commented out line 57: value: "pharmacy" |
| `pharmacy/csi-phr-cron` | Replaced commented Sync reference with commented DM-Initiator |
| `pharmacy/medispan` | Replaced Sync reference with DM-Initiator |
| `pharmacy/medispan` | Updated Deployment target name: csi-net-medispan -> medispan |
| `pharmacy/medispan` | Added new sync-presync/sync-postsync Job patches |
| `pharmacy/medispan` | Commented out line 23: - target: |
| `pharmacy/medispan` | Commented out line 24: group: batch |
| `pharmacy/medispan` | Commented out line 25: version: v1 |
| `pharmacy/medispan` | Commented out line 26: kind: Job |
| `pharmacy/medispan` | Commented out line 27: name: .* |
| `pharmacy/medispan` | Commented out line 28: patch: | |
| `pharmacy/medispan` | Commented out line 29: - op: replace |
| `pharmacy/medispan` | Commented out line 30: path: /metadata/name |
| `pharmacy/medispan` | Commented out line 31: value: before-medispan |
| `pharmacy/medispan` | Commented out line 32: namespace: moh-uat |
| `pharmacy/medispan` | Commented out line 33: - op: add |
| `pharmacy/medispan` | Commented out line 34: path: /spec/template/spec/containers/0/env/- |
| `pharmacy/medispan` | Commented out line 35: value: |
| `pharmacy/medispan` | Commented out line 36: name: CSI_MODULENAME |
| `pharmacy/medispan` | Commented out line 37: value: "csi-bm-invoice-java-service" |
| `pharmacy/medispan` | Commented out line 38: - op: add |
| `pharmacy/medispan` | Commented out line 39: path: /spec/template/spec/containers/0/env/- |
| `pharmacy/medispan` | Commented out line 40: value: |
| `pharmacy/medispan` | Commented out line 41: name: CSI_DATA_VERSION |
| `pharmacy/medispan` | Commented out line 42: value: "4.2.502.0" |
| `pharmacy/medispan` | Commented out line 43: - op: add |
| `pharmacy/medispan` | Commented out line 44: path: /spec/template/spec/containers/0/env/- |
| `pharmacy/medispan` | Commented out line 45: value: |
| `pharmacy/medispan` | Commented out line 46: name: CSI_PROJECT_NAME |
| `pharmacy/medispan` | Commented out line 47: value: "csi-net-medispan" |
| `pharmacy/medispan` | Commented out line 48: - op: add |
| `pharmacy/medispan` | Commented out line 49: path: /spec/template/spec/containers/0/env/- |
| `pharmacy/medispan` | Commented out line 50: value: |
| `pharmacy/medispan` | Commented out line 51: name: CSI_MODULE_NAME |
| `pharmacy/medispan` | Commented out line 52: value: "medispan" |
| `pharmacy/medispan` | Commented out line 53: - op: add |
| `pharmacy/medispan` | Commented out line 54: path: /spec/template/spec/containers/0/env/- |
| `pharmacy/medispan` | Commented out line 55: value: |
| `pharmacy/medispan` | Commented out line 56: name: CSI_PARENT_MODULE_NAME |
| `pharmacy/medispan` | Commented out line 57: value: "pharmacy" |
| `pharmacy/medispan-wrapper` | Replaced commented Sync reference with commented DM-Initiator |
| `pharmacy/phr-bff` | Replaced commented Sync reference with commented DM-Initiator |
| `pharmacy/phr-pharmacygui` | Replaced Sync reference with DM-Initiator |
| `pharmacy/phr-pharmacygui` | Added new sync-presync/sync-postsync Job patches |
| `pharmacy/phr-pharmacygui` | Commented out line 23: - target: |
| `pharmacy/phr-pharmacygui` | Commented out line 24: group: batch |
| `pharmacy/phr-pharmacygui` | Commented out line 25: version: v1 |
| `pharmacy/phr-pharmacygui` | Commented out line 26: kind: Job |
| `pharmacy/phr-pharmacygui` | Commented out line 27: name: before |
| `pharmacy/phr-pharmacygui` | Commented out line 28: patch: | |
| `pharmacy/phr-pharmacygui` | Commented out line 29: - op: replace |
| `pharmacy/phr-pharmacygui` | Commented out line 30: path: /metadata/name |
| `pharmacy/phr-pharmacygui` | Commented out line 31: value: before-csi-pharmacy-ui |
| `pharmacy/phr-pharmacygui` | Commented out line 32: - op: add |
| `pharmacy/phr-pharmacygui` | Commented out line 33: path: /spec/template/spec/containers/0/env/- |
| `pharmacy/phr-pharmacygui` | Commented out line 34: value: |
| `pharmacy/phr-pharmacygui` | Commented out line 35: name: CSI_MODULENAME |
| `pharmacy/phr-pharmacygui` | Commented out line 36: value: "csi-pharmacy-ui" |
| `pharmacy/phr-pharmacygui` | Commented out line 37: - op: add |
| `pharmacy/phr-pharmacygui` | Commented out line 38: path: /spec/template/spec/containers/0/env/- |
| `pharmacy/phr-pharmacygui` | Commented out line 39: value: |
| `pharmacy/phr-pharmacygui` | Commented out line 40: name: CSI_DATA_VERSION |
| `pharmacy/phr-pharmacygui` | Commented out line 41: value: "4.2.15.0" |
| `pharmacy/phr-pharmacygui` | Commented out line 42: - op: add |
| `pharmacy/phr-pharmacygui` | Commented out line 43: path: /spec/template/spec/containers/0/env/- |
| `pharmacy/phr-pharmacygui` | Commented out line 44: value: |
| `pharmacy/phr-pharmacygui` | Commented out line 45: name: CSI_PROJECT_NAME |
| `pharmacy/phr-pharmacygui` | Commented out line 46: value: "phr-pharmacygui" |
| `pharmacy/phr-pharmacygui` | Commented out line 47: - op: add |
| `pharmacy/phr-pharmacygui` | Commented out line 48: path: /spec/template/spec/containers/0/env/- |
| `pharmacy/phr-pharmacygui` | Commented out line 49: value: |
| `pharmacy/phr-pharmacygui` | Commented out line 50: name: CSI_MODULE_NAME |
| `pharmacy/phr-pharmacygui` | Commented out line 51: value: "phr-pharmacygui" |
| `pharmacy/phr-pharmacygui` | Commented out line 52: - op: add |
| `pharmacy/phr-pharmacygui` | Commented out line 53: path: /spec/template/spec/containers/0/env/- |
| `pharmacy/phr-pharmacygui` | Commented out line 54: value: |
| `pharmacy/phr-pharmacygui` | Commented out line 55: name: CSI_PARENT_MODULE_NAME |
| `pharmacy/phr-pharmacygui` | Commented out line 56: value: "pharmacy" |
| `pharmacy/phr-ui-v2` | Replaced commented Sync reference with commented DM-Initiator |
| `pharmacy/phr-ui-v2` | Updated Deployment target name: csi-phr-ui-v2 -> phr-ui-v2 |
| `pharmacy/phr-ui-v2` | Added new sync-presync/sync-postsync Job patches |
| `pharmacy/phr-ui-v2` | Commented out line 24: - target: |
| `pharmacy/phr-ui-v2` | Commented out line 25: group: batch |
| `pharmacy/phr-ui-v2` | Commented out line 26: version: v1 |
| `pharmacy/phr-ui-v2` | Commented out line 27: kind: Job |
| `pharmacy/phr-ui-v2` | Commented out line 28: name: before |
| `pharmacy/phr-ui-v2` | Commented out line 29: patch: |- |
| `pharmacy/phr-ui-v2` | Commented out line 30: - op: replace |
| `pharmacy/phr-ui-v2` | Commented out line 31: path: /metadata/name |
| `pharmacy/phr-ui-v2` | Commented out line 32: value: before-phr-ui-v2 |
| `pharmacy/phr-ui-v2` | Commented out line 33: namespace: moh-uat |
| `pharmacy/phr-ui-v2` | Commented out line 34: - op: add |
| `pharmacy/phr-ui-v2` | Commented out line 35: path: /spec/template/spec/containers/0/env/- |
| `pharmacy/phr-ui-v2` | Commented out line 36: value: |
| `pharmacy/phr-ui-v2` | Commented out line 37: name: CSI_MODULENAME |
| `pharmacy/phr-ui-v2` | Commented out line 38: value: "phr-ui-v2" |
| `pharmacy/phr-ui-v2` | Commented out line 39: - op: add |
| `pharmacy/phr-ui-v2` | Commented out line 40: path: /spec/template/spec/containers/0/env/- |
| `pharmacy/phr-ui-v2` | Commented out line 41: value: |
| `pharmacy/phr-ui-v2` | Commented out line 42: name: CSI_DATA_VERSION |
| `pharmacy/phr-ui-v2` | Commented out line 43: value: "4.5.252.0" |
| `pharmacy/phr-ui-v2` | Commented out line 44: - op: add |
| `pharmacy/phr-ui-v2` | Commented out line 45: path: /spec/template/spec/containers/0/env/- |
| `pharmacy/phr-ui-v2` | Commented out line 46: value: |
| `pharmacy/phr-ui-v2` | Commented out line 47: name: CSI_PROJECT_NAME |
| `pharmacy/phr-ui-v2` | Commented out line 48: value: "phr-ui-v2" |
| `pharmacy/phr-ui-v2` | Commented out line 49: - op: add |
| `pharmacy/phr-ui-v2` | Commented out line 50: path: /spec/template/spec/containers/0/env/- |
| `pharmacy/phr-ui-v2` | Commented out line 51: value: |
| `pharmacy/phr-ui-v2` | Commented out line 52: name: CSI_MODULE_NAME |
| `pharmacy/phr-ui-v2` | Commented out line 53: value: "phr-ui-v2" |
| `pharmacy/phr-ui-v2` | Commented out line 54: - op: add |
| `pharmacy/phr-ui-v2` | Commented out line 55: path: /spec/template/spec/containers/0/env/- |
| `pharmacy/phr-ui-v2` | Commented out line 56: value: |
| `pharmacy/phr-ui-v2` | Commented out line 57: name: CSI_PARENT_MODULE_NAME |
| `pharmacy/phr-ui-v2` | Commented out line 58: value: "pharmacy" |
| `pharmacy/phrbasebgjava` | Replaced Sync reference with DM-Initiator |
| `pharmacy/phrbasebgjava` | Updated Deployment target name: csi-phr-base-bgservice -> phrbasebgjava |
| `renal/ren-hemodialysis-srv` | Replaced Sync reference with DM-Initiator |
| `renal/ren-hemodialysis-srv` | Added new sync-presync/sync-postsync Job patches |
| `renal/ren-hemodialysis-srv` | Commented out line 24: - target: |
| `renal/ren-hemodialysis-srv` | Commented out line 25: group: batch |
| `renal/ren-hemodialysis-srv` | Commented out line 26: version: v1 |
| `renal/ren-hemodialysis-srv` | Commented out line 27: kind: Job |
| `renal/ren-hemodialysis-srv` | Commented out line 28: name: .* |
| `renal/ren-hemodialysis-srv` | Commented out line 29: patch: |- |
| `renal/ren-hemodialysis-srv` | Commented out line 30: - op: replace |
| `renal/ren-hemodialysis-srv` | Commented out line 31: path: /metadata/name |
| `renal/ren-hemodialysis-srv` | Commented out line 32: value: before-csi-net-hemdialy |
| `renal/ren-hemodialysis-srv` | Commented out line 33: namespace: moh-uat |
| `renal/ren-hemodialysis-srv` | Commented out line 34: - op: add |
| `renal/ren-hemodialysis-srv` | Commented out line 35: path: /spec/template/spec/containers/0/env/- |
| `renal/ren-hemodialysis-srv` | Commented out line 36: value: |
| `renal/ren-hemodialysis-srv` | Commented out line 37: name: CSI_DATA_VERSION |
| `renal/ren-hemodialysis-srv` | Commented out line 38: value: "4.0.127.0" |
| `renal/ren-hemodialysis-srv` | Commented out line 39: - op: add |
| `renal/ren-hemodialysis-srv` | Commented out line 40: path: /spec/template/spec/containers/0/env/- |
| `renal/ren-hemodialysis-srv` | Commented out line 41: value: |
| `renal/ren-hemodialysis-srv` | Commented out line 42: name: CSI_PROJECT_NAME |
| `renal/ren-hemodialysis-srv` | Commented out line 43: value: "ren-hemodialysis-srv" |
| `renal/ren-hemodialysis-srv` | Commented out line 44: - op: add |
| `renal/ren-hemodialysis-srv` | Commented out line 45: path: /spec/template/spec/containers/0/env/- |
| `renal/ren-hemodialysis-srv` | Commented out line 46: value: |
| `renal/ren-hemodialysis-srv` | Commented out line 47: name: CSI_MODULE_NAME |
| `renal/ren-hemodialysis-srv` | Commented out line 48: value: "ren-hemodialysis-srv" |
| `renal/ren-hemodialysis-srv` | Commented out line 49: - op: add |
| `renal/ren-hemodialysis-srv` | Commented out line 50: path: /spec/template/spec/containers/0/env/- |
| `renal/ren-hemodialysis-srv` | Commented out line 51: value: |
| `renal/ren-hemodialysis-srv` | Commented out line 52: name: CSI_PARENT_MODULE_NAME |
| `renal/ren-hemodialysis-srv` | Commented out line 53: value: "renal" |
| `rms/csi-ds-dental-core-java-sev` | Added new sync-presync/sync-postsync Job patches |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 23: - target: |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 24: group: batch |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 25: version: v1 |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 26: kind: Job |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 27: name: .* |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 28: patch: |- |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 29: - op: replace |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 30: path: /metadata/name |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 31: value: before-csi-java-ds-dental-core |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 32: - op: add |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 33: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 34: value: |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 35: name: CSI_MODULENAME |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 36: value: "csi-java-ds-dental-core" |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 37: - op: add |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 38: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 39: value: |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 40: name: CSI_DATA_VERSION |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 41: value: "4.0.127.0" |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 42: - op: add |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 43: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 44: value: |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 45: name: CSI_PROJECT_NAME |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 46: value: "csi-ds-dental-core-java-sev" |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 47: - op: add |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 48: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 49: value: |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 50: name: CSI_MODULE_NAME |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 51: value: "csi-ds-dental-core-java-sev" |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 52: - op: add |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 53: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 54: value: |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 55: name: CSI_PARENT_MODULE_NAME |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 56: value: "rms" |
| `rms/csi-mlm-ui` | Added new sync-presync/sync-postsync Job patches |
| `rms/csi-mlm-ui` | Commented out line 20: - target: |
| `rms/csi-mlm-ui` | Commented out line 21: group: batch |
| `rms/csi-mlm-ui` | Commented out line 22: version: v1 |
| `rms/csi-mlm-ui` | Commented out line 23: kind: Job |
| `rms/csi-mlm-ui` | Commented out line 24: name: .* |
| `rms/csi-mlm-ui` | Commented out line 25: patch: |- |
| `rms/csi-mlm-ui` | Commented out line 26: - op: replace |
| `rms/csi-mlm-ui` | Commented out line 27: path: /metadata/name |
| `rms/csi-mlm-ui` | Commented out line 28: value: before-csi-mlm-ui |
| `rms/csi-mlm-ui` | Commented out line 29: namespace: moh-uat |
| `rms/csi-mlm-ui` | Commented out line 30: - op: add |
| `rms/csi-mlm-ui` | Commented out line 31: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-mlm-ui` | Commented out line 32: value: |
| `rms/csi-mlm-ui` | Commented out line 33: name: CSI_MODULENAME |
| `rms/csi-mlm-ui` | Commented out line 34: value: "csi-mlm-ui" |
| `rms/csi-mlm-ui` | Commented out line 35: - op: add |
| `rms/csi-mlm-ui` | Commented out line 36: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-mlm-ui` | Commented out line 37: value: |
| `rms/csi-mlm-ui` | Commented out line 38: name: CSI_DATA_VERSION |
| `rms/csi-mlm-ui` | Commented out line 39: value: "4.0.127.0" |
| `rms/csi-mlm-ui` | Commented out line 40: - op: add |
| `rms/csi-mlm-ui` | Commented out line 41: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-mlm-ui` | Commented out line 42: value: |
| `rms/csi-mlm-ui` | Commented out line 43: name: CSI_PROJECT_NAME |
| `rms/csi-mlm-ui` | Commented out line 44: value: "csi-mlm-ui" |
| `rms/csi-mlm-ui` | Commented out line 45: - op: add |
| `rms/csi-mlm-ui` | Commented out line 46: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-mlm-ui` | Commented out line 47: value: |
| `rms/csi-mlm-ui` | Commented out line 48: name: CSI_MODULE_NAME |
| `rms/csi-mlm-ui` | Commented out line 49: value: "csi-mlm-ui" |
| `rms/csi-mlm-ui` | Commented out line 50: - op: add |
| `rms/csi-mlm-ui` | Commented out line 51: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-mlm-ui` | Commented out line 52: value: |
| `rms/csi-mlm-ui` | Commented out line 53: name: CSI_PARENT_MODULE_NAME |
| `rms/csi-mlm-ui` | Commented out line 54: value: "rms" |
| `rms/csi-morgue-ui` | Replaced Sync reference with DM-Initiator |
| `rms/csi-morgue-ui` | Added new sync-presync/sync-postsync Job patches |
| `rms/csi-morgue-ui` | Commented out line 20: - target: |
| `rms/csi-morgue-ui` | Commented out line 21: group: batch |
| `rms/csi-morgue-ui` | Commented out line 22: version: v1 |
| `rms/csi-morgue-ui` | Commented out line 23: kind: Job |
| `rms/csi-morgue-ui` | Commented out line 24: name: .* |
| `rms/csi-morgue-ui` | Commented out line 25: patch: |- |
| `rms/csi-morgue-ui` | Commented out line 26: - op: replace |
| `rms/csi-morgue-ui` | Commented out line 27: path: /metadata/name |
| `rms/csi-morgue-ui` | Commented out line 28: value: before-csi-morgue-ui |
| `rms/csi-morgue-ui` | Commented out line 29: - op: add |
| `rms/csi-morgue-ui` | Commented out line 30: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-morgue-ui` | Commented out line 31: value: |
| `rms/csi-morgue-ui` | Commented out line 32: name: CSI_MODULENAME |
| `rms/csi-morgue-ui` | Commented out line 33: value: "csi-morgue-ui" |
| `rms/csi-morgue-ui` | Commented out line 34: - op: add |
| `rms/csi-morgue-ui` | Commented out line 35: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-morgue-ui` | Commented out line 36: value: |
| `rms/csi-morgue-ui` | Commented out line 37: name: CSI_DATA_VERSION |
| `rms/csi-morgue-ui` | Commented out line 38: value: "4.0.127.0" |
| `rms/csi-morgue-ui` | Commented out line 39: - op: add |
| `rms/csi-morgue-ui` | Commented out line 40: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-morgue-ui` | Commented out line 41: value: |
| `rms/csi-morgue-ui` | Commented out line 42: name: CSI_PROJECT_NAME |
| `rms/csi-morgue-ui` | Commented out line 43: value: "csi-morgue-ui" |
| `rms/csi-morgue-ui` | Commented out line 44: - op: add |
| `rms/csi-morgue-ui` | Commented out line 45: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-morgue-ui` | Commented out line 46: value: |
| `rms/csi-morgue-ui` | Commented out line 47: name: CSI_MODULE_NAME |
| `rms/csi-morgue-ui` | Commented out line 48: value: "csi-morgue-ui" |
| `rms/csi-morgue-ui` | Commented out line 49: - op: add |
| `rms/csi-morgue-ui` | Commented out line 50: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-morgue-ui` | Commented out line 51: value: |
| `rms/csi-morgue-ui` | Commented out line 52: name: CSI_PARENT_MODULE_NAME |
| `rms/csi-morgue-ui` | Commented out line 53: value: "rms" |
| `rms/csi-pms-adt-request-java-sev` | Added new sync-presync/sync-postsync Job patches |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 23: - target: |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 24: group: batch |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 25: version: v1 |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 26: kind: Job |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 27: name: .* |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 28: patch: |- |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 29: - op: replace |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 30: path: /metadata/name |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 31: value: before-csi-pms-adt-request |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 32: namespace: moh-uat |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 33: - op: add |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 34: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 35: value: |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 36: name: CSI_MODULENAME |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 37: value: "csi-pms-adt-request" |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 38: - op: add |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 39: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 40: value: |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 41: name: CSI_DATA_VERSION |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 42: value: "4.0.127.0" |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 43: - op: add |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 44: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 45: value: |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 46: name: CSI_PROJECT_NAME |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 47: value: "csi-pms-adt-request-java-sev" |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 48: - op: add |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 49: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 50: value: |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 51: name: CSI_MODULE_NAME |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 52: value: "csi-pms-adt-request-java-sev" |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 53: - op: add |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 54: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 55: value: |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 56: name: CSI_PARENT_MODULE_NAME |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 57: value: "rms" |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 58: - op: add |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 59: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 60: value: |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 61: name: isDropValidationDisabled |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 62: value: "true" |
| `rms/csi-pms-adt-ui` | Replaced Sync reference with DM-Initiator |
| `rms/csi-pms-adt-ui` | Added new sync-presync/sync-postsync Job patches |
| `rms/csi-pms-adt-ui` | Commented out line 25: - target: |
| `rms/csi-pms-adt-ui` | Commented out line 26: group: batch |
| `rms/csi-pms-adt-ui` | Commented out line 27: version: v1 |
| `rms/csi-pms-adt-ui` | Commented out line 28: kind: Job |
| `rms/csi-pms-adt-ui` | Commented out line 29: name: .* |
| `rms/csi-pms-adt-ui` | Commented out line 30: patch: | |
| `rms/csi-pms-adt-ui` | Commented out line 31: - op: replace |
| `rms/csi-pms-adt-ui` | Commented out line 32: path: /metadata/name |
| `rms/csi-pms-adt-ui` | Commented out line 33: value: before-csi-adt-ui |
| `rms/csi-pms-adt-ui` | Commented out line 34: - op: add |
| `rms/csi-pms-adt-ui` | Commented out line 35: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-pms-adt-ui` | Commented out line 36: value: |
| `rms/csi-pms-adt-ui` | Commented out line 37: name: CSI_MODULENAME |
| `rms/csi-pms-adt-ui` | Commented out line 38: value: "csi-adt-ui" |
| `rms/csi-pms-adt-ui` | Commented out line 39: - op: add |
| `rms/csi-pms-adt-ui` | Commented out line 40: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-pms-adt-ui` | Commented out line 41: value: |
| `rms/csi-pms-adt-ui` | Commented out line 42: name: CSI_DATA_VERSION |
| `rms/csi-pms-adt-ui` | Commented out line 43: value: "4.1.28.20" |
| `rms/csi-pms-adt-ui` | Commented out line 44: - op: add |
| `rms/csi-pms-adt-ui` | Commented out line 45: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-pms-adt-ui` | Commented out line 46: value: |
| `rms/csi-pms-adt-ui` | Commented out line 47: name: CSI_PROJECT_NAME |
| `rms/csi-pms-adt-ui` | Commented out line 48: value: "csi-pms-adt-ui" |
| `rms/csi-pms-adt-ui` | Commented out line 49: - op: add |
| `rms/csi-pms-adt-ui` | Commented out line 50: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-pms-adt-ui` | Commented out line 51: value: |
| `rms/csi-pms-adt-ui` | Commented out line 52: name: CSI_MODULE_NAME |
| `rms/csi-pms-adt-ui` | Commented out line 53: value: "csi-pms-adt-ui" |
| `rms/csi-pms-adt-ui` | Commented out line 54: - op: add |
| `rms/csi-pms-adt-ui` | Commented out line 55: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-pms-adt-ui` | Commented out line 56: value: |
| `rms/csi-pms-adt-ui` | Commented out line 57: name: CSI_PARENT_MODULE_NAME |
| `rms/csi-pms-adt-ui` | Commented out line 58: value: "rms" |
| `rms/csi-pms-adt-ui` | Commented out line 59: - target: |
| `rms/csi-pms-adt-ui` | Commented out line 60: group: batch |
| `rms/csi-pms-adt-ui` | Commented out line 61: version: v1 |
| `rms/csi-pms-adt-ui` | Commented out line 62: kind: Job |
| `rms/csi-pms-adt-ui` | Commented out line 63: name: data-migration_presync |
| `rms/csi-pms-adt-ui` | Commented out line 64: patch: |- |
| `rms/csi-pms-adt-ui` | Commented out line 65: - op: replace |
| `rms/csi-pms-adt-ui` | Commented out line 66: path: /metadata/name |
| `rms/csi-pms-adt-ui` | Commented out line 67: value: datamigration-csi-adt-ui |
| `rms/csi-pms-adt-ui` | Commented out line 68: namespace: moh-uat |
| `rms/csi-rms-masterdata-java-sev` | Replaced Sync reference with DM-Initiator |
| `rms/csi-rms-masterdata-java-sev` | Removed extra Sync reference: - ../../../Sync-DM/ |
| `rms/csi-rms-masterdata-java-sev` | Added new sync-presync/sync-postsync Job patches |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 46: - target: |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 47: group: batch |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 48: version: v1 |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 49: kind: Job |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 50: name: before |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 51: patch: |- |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 52: - op: replace |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 53: path: /metadata/name |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 54: value: before-rmsmasterdata |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 55: namespace: moh-uat |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 56: - op: add |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 57: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 58: value: |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 59: name: CSI_MODULENAME |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 60: value: "csi-rms-masterdata" |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 61: - op: add |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 62: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 63: value: |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 64: name: CSI_DATA_VERSION |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 65: value: "4.1.196.0" |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 66: - op: add |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 67: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 68: value: |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 69: name: CSI_PROJECT_NAME |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 70: value: "csi-rms-masterdata-java-sev" |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 71: - op: add |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 72: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 73: value: |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 74: name: CSI_MODULE_NAME |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 75: value: "csi-rms-masterdata-java-sev" |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 76: - op: add |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 77: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 78: value: |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 79: name: CSI_PARENT_MODULE_NAME |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 80: value: "rms" |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 81: - op: add |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 82: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 83: value: |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 84: name: isDropValidationDisabled |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 85: value: "true" |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 87: - target: |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 88: group: batch |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 89: version: v1 |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 90: kind: Job |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 91: name: data-migration-presync |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 92: patch: | |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 93: - op: replace |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 94: path: /metadata/name |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 95: value: datamigrations-pre-csi-rms-masterdata |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 96: - op: add |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 97: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 98: value: |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 99: name: CSI_MODULENAME |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 100: value: "csi-rms-masterdata" |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 101: - op: add |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 102: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 103: value: |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 104: name: CSI_DATA_VERSION |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 105: value: "4.1.28.20" |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 106: - op: add |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 107: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 108: value: |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 109: name: CSI_PROJECT_NAME |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 110: value: "csi-rms-masterdata-java-sev" |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 111: - op: add |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 112: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 113: value: |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 114: name: CSI_MODULE_NAME |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 115: value: "csi-rms-masterdata-java-sev" |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 116: - op: add |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 117: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 118: value: |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 119: name: CSI_PARENT_MODULE_NAME |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 120: value: "rms" |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 122: - target: |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 123: group: batch |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 124: version: v1 |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 125: kind: Job |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 126: name: data-migration-postsync |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 127: patch: | |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 128: - op: replace |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 129: path: /metadata/name |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 130: value: datamigrations-post-csi-rms-masterdata |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 131: - op: add |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 132: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 133: value: |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 134: name: CSI_MODULENAME |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 135: value: "csi-rms-masterdata" |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 136: - op: add |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 137: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 138: value: |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 139: name: CSI_DATA_VERSION |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 140: value: "4.1.28.20" |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 141: - op: add |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 142: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 143: value: |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 144: name: CSI_PROJECT_NAME |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 145: value: "csi-rms-masterdata-java-sev" |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 146: - op: add |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 147: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 148: value: |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 149: name: CSI_MODULE_NAME |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 150: value: "csi-rms-masterdata-java-sev" |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 151: - op: add |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 152: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 153: value: |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 154: name: CSI_PARENT_MODULE_NAME |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 155: value: "rms" |
| `rms/csi-rms-morgue-java-service` | Added new sync-presync/sync-postsync Job patches |
| `rms/csi-rms-morgue-java-service` | Commented out line 23: - target: |
| `rms/csi-rms-morgue-java-service` | Commented out line 24: group: batch |
| `rms/csi-rms-morgue-java-service` | Commented out line 25: version: v1 |
| `rms/csi-rms-morgue-java-service` | Commented out line 26: kind: Job |
| `rms/csi-rms-morgue-java-service` | Commented out line 27: name: .* |
| `rms/csi-rms-morgue-java-service` | Commented out line 28: patch: |- |
| `rms/csi-rms-morgue-java-service` | Commented out line 29: - op: replace |
| `rms/csi-rms-morgue-java-service` | Commented out line 30: path: /metadata/name |
| `rms/csi-rms-morgue-java-service` | Commented out line 31: value: before-csi-rms-morgue |
| `rms/csi-rms-morgue-java-service` | Commented out line 32: - op: add |
| `rms/csi-rms-morgue-java-service` | Commented out line 33: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-morgue-java-service` | Commented out line 34: value: |
| `rms/csi-rms-morgue-java-service` | Commented out line 35: name: CSI_MODULE_NAME |
| `rms/csi-rms-morgue-java-service` | Commented out line 36: value: "csi-rms-morgue-java-service" |
| `rms/csi-rms-morgue-java-service` | Commented out line 37: - op: add |
| `rms/csi-rms-morgue-java-service` | Commented out line 38: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-morgue-java-service` | Commented out line 39: value: |
| `rms/csi-rms-morgue-java-service` | Commented out line 40: name: CSI_PARENT_MODULE_NAME |
| `rms/csi-rms-morgue-java-service` | Commented out line 41: value: "rms" |
| `rms/csi-rms-morgue-java-service` | Commented out line 42: - op: add |
| `rms/csi-rms-morgue-java-service` | Commented out line 43: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-morgue-java-service` | Commented out line 44: value: |
| `rms/csi-rms-morgue-java-service` | Commented out line 45: name: CSI_DATA_VERSION |
| `rms/csi-rms-morgue-java-service` | Commented out line 46: value: "4.0.127.0" |
| `rms/csi-rms-morgue-java-service` | Commented out line 47: - op: add |
| `rms/csi-rms-morgue-java-service` | Commented out line 48: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-morgue-java-service` | Commented out line 49: value: |
| `rms/csi-rms-morgue-java-service` | Commented out line 50: name: filePath |
| `rms/csi-rms-morgue-java-service` | Commented out line 51: value: "kustomization.yaml" |
| `rms/csi-rms-morgue-java-service` | Commented out line 52: - op: add |
| `rms/csi-rms-morgue-java-service` | Commented out line 53: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-morgue-java-service` | Commented out line 54: value: |
| `rms/csi-rms-morgue-java-service` | Commented out line 55: name: CSI_PROJECT_NAME |
| `rms/csi-rms-morgue-java-service` | Commented out line 56: value: "csi-rms-morgue-java-service" |
| `rms/csi-rms-morgue-java-service` | Commented out line 57: - op: add |
| `rms/csi-rms-morgue-java-service` | Commented out line 58: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-morgue-java-service` | Commented out line 59: value: |
| `rms/csi-rms-morgue-java-service` | Commented out line 60: name: MODULE_NAME |
| `rms/csi-rms-morgue-java-service` | Commented out line 61: value: "csi-rms-morgue-java-service" |
| `rms/csi-rms-morgue-java-service` | Commented out line 62: - op: add |
| `rms/csi-rms-morgue-java-service` | Commented out line 63: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-morgue-java-service` | Commented out line 64: value: |
| `rms/csi-rms-morgue-java-service` | Commented out line 65: name: isDropValidationDisabled |
| `rms/csi-rms-morgue-java-service` | Commented out line 66: value: "true" |
| `rms/csi-rms-reservation-java-sev` | Added new sync-presync/sync-postsync Job patches |
| `rms/csi-rms-reservation-java-sev` | Commented out line 23: - target: |
| `rms/csi-rms-reservation-java-sev` | Commented out line 24: group: batch |
| `rms/csi-rms-reservation-java-sev` | Commented out line 25: version: v1 |
| `rms/csi-rms-reservation-java-sev` | Commented out line 26: kind: Job |
| `rms/csi-rms-reservation-java-sev` | Commented out line 27: name: .* |
| `rms/csi-rms-reservation-java-sev` | Commented out line 28: patch: |- |
| `rms/csi-rms-reservation-java-sev` | Commented out line 29: - op: replace |
| `rms/csi-rms-reservation-java-sev` | Commented out line 30: path: /metadata/name |
| `rms/csi-rms-reservation-java-sev` | Commented out line 31: value: before-rmsreservation |
| `rms/csi-rms-reservation-java-sev` | Commented out line 32: namespace: moh-uat |
| `rms/csi-rms-reservation-java-sev` | Commented out line 33: - op: add |
| `rms/csi-rms-reservation-java-sev` | Commented out line 34: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-reservation-java-sev` | Commented out line 35: value: |
| `rms/csi-rms-reservation-java-sev` | Commented out line 36: name: CSI_MODULENAME |
| `rms/csi-rms-reservation-java-sev` | Commented out line 37: value: "csi-rms-reservation-java-sev" |
| `rms/csi-rms-reservation-java-sev` | Commented out line 38: - op: add |
| `rms/csi-rms-reservation-java-sev` | Commented out line 39: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-reservation-java-sev` | Commented out line 40: value: |
| `rms/csi-rms-reservation-java-sev` | Commented out line 41: name: CSI_DATA_VERSION |
| `rms/csi-rms-reservation-java-sev` | Commented out line 42: value: "V4-785" |
| `rms/csi-rms-reservation-java-sev` | Commented out line 43: - op: add |
| `rms/csi-rms-reservation-java-sev` | Commented out line 44: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-reservation-java-sev` | Commented out line 45: value: |
| `rms/csi-rms-reservation-java-sev` | Commented out line 46: name: CSI_PROJECT_NAME |
| `rms/csi-rms-reservation-java-sev` | Commented out line 47: value: "csi-rms-reservation-java-sev" |
| `rms/csi-rms-reservation-java-sev` | Commented out line 48: - op: add |
| `rms/csi-rms-reservation-java-sev` | Commented out line 49: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-reservation-java-sev` | Commented out line 50: value: |
| `rms/csi-rms-reservation-java-sev` | Commented out line 51: name: CSI_MODULE_NAME |
| `rms/csi-rms-reservation-java-sev` | Commented out line 52: value: "csi-rms-reservation-java-sev" |
| `rms/csi-rms-reservation-java-sev` | Commented out line 53: - op: add |
| `rms/csi-rms-reservation-java-sev` | Commented out line 54: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-reservation-java-sev` | Commented out line 55: value: |
| `rms/csi-rms-reservation-java-sev` | Commented out line 56: name: CSI_PARENT_MODULE_NAME |
| `rms/csi-rms-reservation-java-sev` | Commented out line 57: value: "rms" |
| `rms/csi-rms-resource-registry-java-sev` | Added new sync-presync/sync-postsync Job patches |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 56: - target: |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 57: group: batch |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 58: version: v1 |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 59: kind: Job |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 60: name: .* |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 61: patch: |- |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 62: - op: replace |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 63: path: /metadata/name |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 64: value: before-csi-rms-resource-registry-java-sev |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 65: namespace: moh-uat |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 66: - op: add |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 67: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 68: value: |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 69: name: CSI_MODULENAME |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 70: value: "csi-rms-resource-registry-java-sev" |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 71: - op: add |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 72: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 73: value: |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 74: name: CSI_DATA_VERSION |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 75: value: "4.0.127.0" |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 76: - op: add |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 77: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 78: value: |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 79: name: CSI_PROJECT_NAME |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 80: value: "csi-rms-resource-registry-java-sev" |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 81: - op: add |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 82: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 83: value: |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 84: name: CSI_MODULE_NAME |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 85: value: "csi-rms-resource-registry-java-sev" |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 86: - op: add |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 87: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 88: value: |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 89: name: CSI_PARENT_MODULE_NAME |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 90: value: "rms" |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 91: - op: add |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 92: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 93: value: |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 94: name: isDropValidationDisabled |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 95: value: "true" |
| `rms/csi-rms-ui` | Added new sync-presync/sync-postsync Job patches |
| `rms/csi-rms-ui` | Commented out line 20: - target: |
| `rms/csi-rms-ui` | Commented out line 21: group: batch |
| `rms/csi-rms-ui` | Commented out line 22: version: v1 |
| `rms/csi-rms-ui` | Commented out line 23: kind: Job |
| `rms/csi-rms-ui` | Commented out line 24: name: .* |
| `rms/csi-rms-ui` | Commented out line 25: patch: |- |
| `rms/csi-rms-ui` | Commented out line 26: - op: replace |
| `rms/csi-rms-ui` | Commented out line 27: path: /metadata/name |
| `rms/csi-rms-ui` | Commented out line 28: value: before-csi-rms-ui |
| `rms/csi-rms-ui` | Commented out line 29: namespace: moh-uat |
| `rms/csi-rms-ui` | Commented out line 30: - op: add |
| `rms/csi-rms-ui` | Commented out line 31: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-ui` | Commented out line 32: value: |
| `rms/csi-rms-ui` | Commented out line 33: name: CSI_MODULENAME |
| `rms/csi-rms-ui` | Commented out line 34: value: "csi-rms-ui" |
| `rms/csi-rms-ui` | Commented out line 35: - op: add |
| `rms/csi-rms-ui` | Commented out line 36: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-ui` | Commented out line 37: value: |
| `rms/csi-rms-ui` | Commented out line 38: name: CSI_DATA_VERSION |
| `rms/csi-rms-ui` | Commented out line 39: value: "AMD-11685" |
| `rms/csi-rms-ui` | Commented out line 40: - op: add |
| `rms/csi-rms-ui` | Commented out line 41: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-ui` | Commented out line 42: value: |
| `rms/csi-rms-ui` | Commented out line 43: name: CSI_PROJECT_NAME |
| `rms/csi-rms-ui` | Commented out line 44: value: "csi-rms-ui" |
| `rms/csi-rms-ui` | Commented out line 45: - op: add |
| `rms/csi-rms-ui` | Commented out line 46: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-ui` | Commented out line 47: value: |
| `rms/csi-rms-ui` | Commented out line 48: name: CSI_MODULE_NAME |
| `rms/csi-rms-ui` | Commented out line 49: value: "csi-rms-ui" |
| `rms/csi-rms-ui` | Commented out line 50: - op: add |
| `rms/csi-rms-ui` | Commented out line 51: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-ui` | Commented out line 52: value: |
| `rms/csi-rms-ui` | Commented out line 53: name: CSI_PARENT_MODULE_NAME |
| `rms/csi-rms-ui` | Commented out line 54: value: "rms" |
| `rms/csi-setup-ui` | Added new sync-presync/sync-postsync Job patches |
| `rms/csi-setup-ui` | Commented out line 20: - target: |
| `rms/csi-setup-ui` | Commented out line 21: group: batch |
| `rms/csi-setup-ui` | Commented out line 22: version: v1 |
| `rms/csi-setup-ui` | Commented out line 23: kind: Job |
| `rms/csi-setup-ui` | Commented out line 24: name: .* |
| `rms/csi-setup-ui` | Commented out line 25: patch: |- |
| `rms/csi-setup-ui` | Commented out line 26: - op: replace |
| `rms/csi-setup-ui` | Commented out line 27: path: /metadata/name |
| `rms/csi-setup-ui` | Commented out line 28: value: before-setupui |
| `rms/csi-setup-ui` | Commented out line 29: namespace: moh-uat |
| `rms/csi-setup-ui` | Commented out line 30: - op: add |
| `rms/csi-setup-ui` | Commented out line 31: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-setup-ui` | Commented out line 32: value: |
| `rms/csi-setup-ui` | Commented out line 33: name: CSI_MODULENAME |
| `rms/csi-setup-ui` | Commented out line 34: value: "csi-setup-ui" |
| `rms/csi-setup-ui` | Commented out line 35: - op: add |
| `rms/csi-setup-ui` | Commented out line 36: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-setup-ui` | Commented out line 37: value: |
| `rms/csi-setup-ui` | Commented out line 38: name: CSI_DATA_VERSION |
| `rms/csi-setup-ui` | Commented out line 39: value: "V4-785" |
| `rms/csi-setup-ui` | Commented out line 40: - op: add |
| `rms/csi-setup-ui` | Commented out line 41: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-setup-ui` | Commented out line 42: value: |
| `rms/csi-setup-ui` | Commented out line 43: name: CSI_PROJECT_NAME |
| `rms/csi-setup-ui` | Commented out line 44: value: "csi-setup-ui" |
| `rms/csi-setup-ui` | Commented out line 45: - op: add |
| `rms/csi-setup-ui` | Commented out line 46: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-setup-ui` | Commented out line 47: value: |
| `rms/csi-setup-ui` | Commented out line 48: name: CSI_MODULE_NAME |
| `rms/csi-setup-ui` | Commented out line 49: value: "csi-setup-ui" |
| `rms/csi-setup-ui` | Commented out line 50: - op: add |
| `rms/csi-setup-ui` | Commented out line 51: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-setup-ui` | Commented out line 52: value: |
| `rms/csi-setup-ui` | Commented out line 53: name: CSI_PARENT_MODULE_NAME |
| `rms/csi-setup-ui` | Commented out line 54: value: "rms" |
| `security/securitycentralauth` | Updated Deployment target name: csi-central-authentication-service -> securitycentralauth |
| `security/securityiamcache` | Updated Deployment target name: infinispan-server -> securityiamcache |
