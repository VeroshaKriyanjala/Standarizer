# DM-Initiator Update Log - HMG

Mode: LIVE

## Version Check

- base-utility-service-java-sev: `V4.0.2512_W4-174_prod`
  - Threshold: `V4.0.2510_W1-4893_prod`
- csi-iam-service: `V4.0.2602_W2_108_prod`
  - Threshold: `V4.0.2510_W4_14_prod`
- **Conditions met: YES**

## Changes (2656 total)

| Service | Change |
|---------|--------|
| `base/base-utility-service-java-sev` | Replaced Sync reference with DM-Initiator |
| `base/base-utility-service-java-sev` | Removed extra Sync reference: - ../../../Sync-DM/ |
| `base/base-utility-service-java-sev` | Added new sync-presync/sync-postsync Job patches |
| `base/base-utility-service-java-sev` | Commented out line 20: - target: |
| `base/base-utility-service-java-sev` | Commented out line 21: group: batch |
| `base/base-utility-service-java-sev` | Commented out line 22: version: v1 |
| `base/base-utility-service-java-sev` | Commented out line 23: kind: Job |
| `base/base-utility-service-java-sev` | Commented out line 24: name: before |
| `base/base-utility-service-java-sev` | Commented out line 25: patch: |- |
| `base/base-utility-service-java-sev` | Commented out line 26: - op: replace |
| `base/base-utility-service-java-sev` | Commented out line 27: path: /metadata/name |
| `base/base-utility-service-java-sev` | Commented out line 28: value: before-csi-base-utility |
| `base/base-utility-service-java-sev` | Commented out line 29: - op: add |
| `base/base-utility-service-java-sev` | Commented out line 30: path: /spec/template/spec/containers/0/env/- |
| `base/base-utility-service-java-sev` | Commented out line 31: value: |
| `base/base-utility-service-java-sev` | Commented out line 32: name: CSI_MODULENAME |
| `base/base-utility-service-java-sev` | Commented out line 33: value: "csi-base-utility" |
| `base/base-utility-service-java-sev` | Commented out line 34: - op: add |
| `base/base-utility-service-java-sev` | Commented out line 35: path: /spec/template/spec/containers/0/env/- |
| `base/base-utility-service-java-sev` | Commented out line 36: value: |
| `base/base-utility-service-java-sev` | Commented out line 37: name: CSI_DATA_VERSION |
| `base/base-utility-service-java-sev` | Commented out line 38: value: "4.1.28.20" |
| `base/base-utility-service-java-sev` | Commented out line 39: - op: add |
| `base/base-utility-service-java-sev` | Commented out line 40: path: /spec/template/spec/containers/0/env/- |
| `base/base-utility-service-java-sev` | Commented out line 41: value: |
| `base/base-utility-service-java-sev` | Commented out line 42: name: CSI_PROJECT_NAME |
| `base/base-utility-service-java-sev` | Commented out line 43: value: "base-utility-service-java-sev" |
| `base/base-utility-service-java-sev` | Commented out line 44: - op: add |
| `base/base-utility-service-java-sev` | Commented out line 45: path: /spec/template/spec/containers/0/env/- |
| `base/base-utility-service-java-sev` | Commented out line 46: value: |
| `base/base-utility-service-java-sev` | Commented out line 47: name: CSI_MODULE_NAME |
| `base/base-utility-service-java-sev` | Commented out line 48: value: "baseutilityservicejava" |
| `base/base-utility-service-java-sev` | Commented out line 49: - op: add |
| `base/base-utility-service-java-sev` | Commented out line 50: path: /spec/template/spec/containers/0/env/- |
| `base/base-utility-service-java-sev` | Commented out line 51: value: |
| `base/base-utility-service-java-sev` | Commented out line 52: name: CSI_PARENT_MODULE_NAME |
| `base/base-utility-service-java-sev` | Commented out line 53: value: "base" |
| `base/base-utility-service-java-sev` | Commented out line 55: - target: |
| `base/base-utility-service-java-sev` | Commented out line 56: group: batch |
| `base/base-utility-service-java-sev` | Commented out line 57: version: v1 |
| `base/base-utility-service-java-sev` | Commented out line 58: kind: Job |
| `base/base-utility-service-java-sev` | Commented out line 59: name: data-migration-presync |
| `base/base-utility-service-java-sev` | Commented out line 60: patch: |- |
| `base/base-utility-service-java-sev` | Commented out line 61: - op: replace |
| `base/base-utility-service-java-sev` | Commented out line 62: path: /metadata/name |
| `base/base-utility-service-java-sev` | Commented out line 63: value: data-migration-presync-csi-base-utility |
| `base/base-utility-service-java-sev` | Commented out line 64: - op: add |
| `base/base-utility-service-java-sev` | Commented out line 65: path: /spec/template/spec/containers/0/env/- |
| `base/base-utility-service-java-sev` | Commented out line 66: value: |
| `base/base-utility-service-java-sev` | Commented out line 67: name: CSI_MODULENAME |
| `base/base-utility-service-java-sev` | Commented out line 68: value: "baseutilityservicejava" |
| `base/base-utility-service-java-sev` | Commented out line 69: - op: add |
| `base/base-utility-service-java-sev` | Commented out line 70: path: /spec/template/spec/containers/0/env/- |
| `base/base-utility-service-java-sev` | Commented out line 71: value: |
| `base/base-utility-service-java-sev` | Commented out line 72: name: CSI_DATA_VERSION |
| `base/base-utility-service-java-sev` | Commented out line 73: value: "4.1.28.20" |
| `base/base-utility-service-java-sev` | Commented out line 74: - op: add |
| `base/base-utility-service-java-sev` | Commented out line 75: path: /spec/template/spec/containers/0/env/- |
| `base/base-utility-service-java-sev` | Commented out line 76: value: |
| `base/base-utility-service-java-sev` | Commented out line 77: name: CSI_PROJECT_NAME |
| `base/base-utility-service-java-sev` | Commented out line 78: value: "base-utility-service-java-sev" |
| `base/base-utility-service-java-sev` | Commented out line 79: - op: add |
| `base/base-utility-service-java-sev` | Commented out line 80: path: /spec/template/spec/containers/0/env/- |
| `base/base-utility-service-java-sev` | Commented out line 81: value: |
| `base/base-utility-service-java-sev` | Commented out line 82: name: CSI_MODULE_NAME |
| `base/base-utility-service-java-sev` | Commented out line 83: value: "baseutilityservicejava" |
| `base/base-utility-service-java-sev` | Commented out line 84: - op: add |
| `base/base-utility-service-java-sev` | Commented out line 85: path: /spec/template/spec/containers/0/env/- |
| `base/base-utility-service-java-sev` | Commented out line 86: value: |
| `base/base-utility-service-java-sev` | Commented out line 87: name: CSI_PARENT_MODULE_NAME |
| `base/base-utility-service-java-sev` | Commented out line 88: value: "base" |
| `base/base-utility-service-java-sev` | Commented out line 90: - target: |
| `base/base-utility-service-java-sev` | Commented out line 91: group: batch |
| `base/base-utility-service-java-sev` | Commented out line 92: version: v1 |
| `base/base-utility-service-java-sev` | Commented out line 93: kind: Job |
| `base/base-utility-service-java-sev` | Commented out line 94: name: data-migration-postsync |
| `base/base-utility-service-java-sev` | Commented out line 95: patch: |- |
| `base/base-utility-service-java-sev` | Commented out line 96: - op: replace |
| `base/base-utility-service-java-sev` | Commented out line 97: path: /metadata/name |
| `base/base-utility-service-java-sev` | Commented out line 98: value: data-migration-postsync-csi-base-utility |
| `base/base-utility-service-java-sev` | Commented out line 99: - op: add |
| `base/base-utility-service-java-sev` | Commented out line 100: path: /spec/template/spec/containers/0/env/- |
| `base/base-utility-service-java-sev` | Commented out line 101: value: |
| `base/base-utility-service-java-sev` | Commented out line 102: name: CSI_MODULENAME |
| `base/base-utility-service-java-sev` | Commented out line 103: value: "baseutilityservicejava" |
| `base/base-utility-service-java-sev` | Commented out line 104: - op: add |
| `base/base-utility-service-java-sev` | Commented out line 105: path: /spec/template/spec/containers/0/env/- |
| `base/base-utility-service-java-sev` | Commented out line 106: value: |
| `base/base-utility-service-java-sev` | Commented out line 107: name: CSI_DATA_VERSION |
| `base/base-utility-service-java-sev` | Commented out line 108: value: "4.1.28.20" |
| `base/base-utility-service-java-sev` | Commented out line 109: - op: add |
| `base/base-utility-service-java-sev` | Commented out line 110: path: /spec/template/spec/containers/0/env/- |
| `base/base-utility-service-java-sev` | Commented out line 111: value: |
| `base/base-utility-service-java-sev` | Commented out line 112: name: CSI_PROJECT_NAME |
| `base/base-utility-service-java-sev` | Commented out line 113: value: "base-utility-service-java-sev" |
| `base/base-utility-service-java-sev` | Commented out line 114: - op: add |
| `base/base-utility-service-java-sev` | Commented out line 115: path: /spec/template/spec/containers/0/env/- |
| `base/base-utility-service-java-sev` | Commented out line 116: value: |
| `base/base-utility-service-java-sev` | Commented out line 117: name: CSI_MODULE_NAME |
| `base/base-utility-service-java-sev` | Commented out line 118: value: "baseutilityservicejava" |
| `base/base-utility-service-java-sev` | Commented out line 119: - op: add |
| `base/base-utility-service-java-sev` | Commented out line 120: path: /spec/template/spec/containers/0/env/- |
| `base/base-utility-service-java-sev` | Commented out line 121: value: |
| `base/base-utility-service-java-sev` | Commented out line 122: name: CSI_PARENT_MODULE_NAME |
| `base/base-utility-service-java-sev` | Commented out line 123: value: "base" |
| `base/csi-uif-admin-ui` | Replaced Sync reference with DM-Initiator |
| `base/csi-uif-settings` | Replaced Sync reference with DM-Initiator |
| `base/csi-uif-settings` | Added new sync-presync/sync-postsync Job patches |
| `base/csi-uif-settings` | Commented out line 20: - target: |
| `base/csi-uif-settings` | Commented out line 21: group: batch |
| `base/csi-uif-settings` | Commented out line 22: version: v1 |
| `base/csi-uif-settings` | Commented out line 23: kind: Job |
| `base/csi-uif-settings` | Commented out line 24: name: before |
| `base/csi-uif-settings` | Commented out line 25: patch: |- |
| `base/csi-uif-settings` | Commented out line 26: - op: replace |
| `base/csi-uif-settings` | Commented out line 27: path: /metadata/name |
| `base/csi-uif-settings` | Commented out line 28: value: before-csi-config-ui |
| `base/csi-uif-settings` | Commented out line 29: namespace: moh-uat |
| `base/csi-uif-settings` | Commented out line 30: - op: add |
| `base/csi-uif-settings` | Commented out line 31: path: /spec/template/spec/containers/0/env/- |
| `base/csi-uif-settings` | Commented out line 32: value: |
| `base/csi-uif-settings` | Commented out line 33: name: CSI_MODULENAME |
| `base/csi-uif-settings` | Commented out line 34: value: "csi-config-ui" |
| `base/csi-uif-settings` | Commented out line 35: - op: add |
| `base/csi-uif-settings` | Commented out line 36: path: /spec/template/spec/containers/0/env/- |
| `base/csi-uif-settings` | Commented out line 37: value: |
| `base/csi-uif-settings` | Commented out line 38: name: CSI_DATA_VERSION |
| `base/csi-uif-settings` | Commented out line 39: value: "4.1.170.0" |
| `base/csi-uif-settings` | Commented out line 40: - op: add |
| `base/csi-uif-settings` | Commented out line 41: path: /spec/template/spec/containers/0/env/- |
| `base/csi-uif-settings` | Commented out line 42: value: |
| `base/csi-uif-settings` | Commented out line 43: name: CSI_PROJECT_NAME |
| `base/csi-uif-settings` | Commented out line 44: value: "csi.uif.settings" |
| `base/csi-uif-settings` | Commented out line 45: - op: add |
| `base/csi-uif-settings` | Commented out line 46: path: /spec/template/spec/containers/0/env/- |
| `base/csi-uif-settings` | Commented out line 47: value: |
| `base/csi-uif-settings` | Commented out line 48: name: CSI_MODULE_NAME |
| `base/csi-uif-settings` | Commented out line 49: value: "configui" |
| `base/csi-uif-settings` | Commented out line 50: - op: add |
| `base/csi-uif-settings` | Commented out line 51: path: /spec/template/spec/containers/0/env/- |
| `base/csi-uif-settings` | Commented out line 52: value: |
| `base/csi-uif-settings` | Commented out line 53: name: CSI_PARENT_MODULE_NAME |
| `base/csi-uif-settings` | Commented out line 54: value: "base" |
| `billing/csi-bm-approval-java-service` | Replaced Sync reference with DM-Initiator |
| `billing/csi-bm-approval-java-service` | Added new sync-presync/sync-postsync Job patches |
| `billing/csi-bm-approval-java-service` | Commented out line 18: - target: |
| `billing/csi-bm-approval-java-service` | Commented out line 19: group: batch |
| `billing/csi-bm-approval-java-service` | Commented out line 20: version: v1 |
| `billing/csi-bm-approval-java-service` | Commented out line 21: kind: Job |
| `billing/csi-bm-approval-java-service` | Commented out line 22: name: .* |
| `billing/csi-bm-approval-java-service` | Commented out line 23: patch: |- |
| `billing/csi-bm-approval-java-service` | Commented out line 24: - op: replace |
| `billing/csi-bm-approval-java-service` | Commented out line 25: path: /metadata/name |
| `billing/csi-bm-approval-java-service` | Commented out line 26: value: before-bmbillingapprovaljava |
| `billing/csi-bm-approval-java-service` | Commented out line 27: - op: add |
| `billing/csi-bm-approval-java-service` | Commented out line 28: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-approval-java-service` | Commented out line 29: value: |
| `billing/csi-bm-approval-java-service` | Commented out line 30: name: CSI_MODULENAME |
| `billing/csi-bm-approval-java-service` | Commented out line 31: value: "csi-bm-approval-java-service" |
| `billing/csi-bm-approval-java-service` | Commented out line 32: - op: add |
| `billing/csi-bm-approval-java-service` | Commented out line 33: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-approval-java-service` | Commented out line 34: value: |
| `billing/csi-bm-approval-java-service` | Commented out line 35: name: CSI_DATA_VERSION |
| `billing/csi-bm-approval-java-service` | Commented out line 36: value: "4.3.234.0" |
| `billing/csi-bm-approval-java-service` | Commented out line 37: - op: add |
| `billing/csi-bm-approval-java-service` | Commented out line 38: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-approval-java-service` | Commented out line 39: value: |
| `billing/csi-bm-approval-java-service` | Commented out line 40: name: CSI_PROJECT_NAME |
| `billing/csi-bm-approval-java-service` | Commented out line 41: value: "csi-bm-approval-java-service" |
| `billing/csi-bm-approval-java-service` | Commented out line 42: - op: add |
| `billing/csi-bm-approval-java-service` | Commented out line 43: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-approval-java-service` | Commented out line 44: value: |
| `billing/csi-bm-approval-java-service` | Commented out line 45: name: CSI_MODULE_NAME |
| `billing/csi-bm-approval-java-service` | Commented out line 46: value: "bmbillingapprovaljava" |
| `billing/csi-bm-approval-java-service` | Commented out line 47: - op: add |
| `billing/csi-bm-approval-java-service` | Commented out line 48: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-approval-java-service` | Commented out line 49: value: |
| `billing/csi-bm-approval-java-service` | Commented out line 50: name: CSI_PARENT_MODULE_NAME |
| `billing/csi-bm-approval-java-service` | Commented out line 51: value: "billing" |
| `billing/csi-bm-approval-ui` | Replaced Sync reference with DM-Initiator |
| `billing/csi-bm-approval-ui` | Added new sync-presync/sync-postsync Job patches |
| `billing/csi-bm-approval-ui` | Commented out line 20: - target: |
| `billing/csi-bm-approval-ui` | Commented out line 21: group: batch |
| `billing/csi-bm-approval-ui` | Commented out line 22: version: v1 |
| `billing/csi-bm-approval-ui` | Commented out line 23: kind: Job |
| `billing/csi-bm-approval-ui` | Commented out line 24: name: .* |
| `billing/csi-bm-approval-ui` | Commented out line 25: patch: |- |
| `billing/csi-bm-approval-ui` | Commented out line 26: - op: replace |
| `billing/csi-bm-approval-ui` | Commented out line 27: path: /metadata/name |
| `billing/csi-bm-approval-ui` | Commented out line 28: value: before-bmapprovalui |
| `billing/csi-bm-approval-ui` | Commented out line 29: - op: add |
| `billing/csi-bm-approval-ui` | Commented out line 30: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-approval-ui` | Commented out line 31: value: |
| `billing/csi-bm-approval-ui` | Commented out line 32: name: CSI_MODULENAME |
| `billing/csi-bm-approval-ui` | Commented out line 33: value: "csi-bm-approval-ui" |
| `billing/csi-bm-approval-ui` | Commented out line 34: - op: add |
| `billing/csi-bm-approval-ui` | Commented out line 35: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-approval-ui` | Commented out line 36: value: |
| `billing/csi-bm-approval-ui` | Commented out line 37: name: CSI_DATA_VERSION |
| `billing/csi-bm-approval-ui` | Commented out line 38: value: "4.3.146.0" |
| `billing/csi-bm-approval-ui` | Commented out line 39: - op: add |
| `billing/csi-bm-approval-ui` | Commented out line 40: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-approval-ui` | Commented out line 41: value: |
| `billing/csi-bm-approval-ui` | Commented out line 42: name: CSI_PROJECT_NAME |
| `billing/csi-bm-approval-ui` | Commented out line 43: value: "csi-bm-approval-ui" |
| `billing/csi-bm-approval-ui` | Commented out line 44: - op: add |
| `billing/csi-bm-approval-ui` | Commented out line 45: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-approval-ui` | Commented out line 46: value: |
| `billing/csi-bm-approval-ui` | Commented out line 47: name: CSI_MODULE_NAME |
| `billing/csi-bm-approval-ui` | Commented out line 48: value: "bmapprovalui" |
| `billing/csi-bm-approval-ui` | Commented out line 49: - op: add |
| `billing/csi-bm-approval-ui` | Commented out line 50: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-approval-ui` | Commented out line 51: value: |
| `billing/csi-bm-approval-ui` | Commented out line 52: name: CSI_PARENT_MODULE_NAME |
| `billing/csi-bm-approval-ui` | Commented out line 53: value: "billing" |
| `billing/csi-bm-billing-java-service` | Replaced Sync reference with DM-Initiator |
| `billing/csi-bm-billing-java-service` | Added new sync-presync/sync-postsync Job patches |
| `billing/csi-bm-billing-java-service` | Commented out line 20: - target: |
| `billing/csi-bm-billing-java-service` | Commented out line 21: group: batch |
| `billing/csi-bm-billing-java-service` | Commented out line 22: version: v1 |
| `billing/csi-bm-billing-java-service` | Commented out line 23: kind: Job |
| `billing/csi-bm-billing-java-service` | Commented out line 24: name: before |
| `billing/csi-bm-billing-java-service` | Commented out line 25: patch: |- |
| `billing/csi-bm-billing-java-service` | Commented out line 26: - op: replace |
| `billing/csi-bm-billing-java-service` | Commented out line 27: path: /metadata/name |
| `billing/csi-bm-billing-java-service` | Commented out line 28: value: before-csi-bm-billing-java-service |
| `billing/csi-bm-billing-java-service` | Commented out line 29: - op: add |
| `billing/csi-bm-billing-java-service` | Commented out line 30: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-billing-java-service` | Commented out line 31: value: |
| `billing/csi-bm-billing-java-service` | Commented out line 32: name: CSI_MODULENAME |
| `billing/csi-bm-billing-java-service` | Commented out line 33: value: "csi-bm-billing-java-service" |
| `billing/csi-bm-billing-java-service` | Commented out line 34: - op: add |
| `billing/csi-bm-billing-java-service` | Commented out line 35: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-billing-java-service` | Commented out line 36: value: |
| `billing/csi-bm-billing-java-service` | Commented out line 37: name: CSI_DATA_VERSION |
| `billing/csi-bm-billing-java-service` | Commented out line 38: value: "4.5.154.0" |
| `billing/csi-bm-billing-java-service` | Commented out line 39: - op: add |
| `billing/csi-bm-billing-java-service` | Commented out line 40: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-billing-java-service` | Commented out line 41: value: |
| `billing/csi-bm-billing-java-service` | Commented out line 42: name: CSI_PROJECT_NAME |
| `billing/csi-bm-billing-java-service` | Commented out line 43: value: "csi-bm-billing-java-service" |
| `billing/csi-bm-billing-java-service` | Commented out line 44: - op: add |
| `billing/csi-bm-billing-java-service` | Commented out line 45: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-billing-java-service` | Commented out line 46: value: |
| `billing/csi-bm-billing-java-service` | Commented out line 47: name: CSI_MODULE_NAME |
| `billing/csi-bm-billing-java-service` | Commented out line 48: value: "bmbillingjava" |
| `billing/csi-bm-billing-java-service` | Commented out line 49: - op: add |
| `billing/csi-bm-billing-java-service` | Commented out line 50: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-billing-java-service` | Commented out line 51: value: |
| `billing/csi-bm-billing-java-service` | Commented out line 52: name: CSI_PARENT_MODULE_NAME |
| `billing/csi-bm-billing-java-service` | Commented out line 53: value: "billing" |
| `billing/csi-bm-billing-ui` | Replaced Sync reference with DM-Initiator |
| `billing/csi-bm-billing-ui` | Added new sync-presync/sync-postsync Job patches |
| `billing/csi-bm-billing-ui` | Commented out line 22: - target: |
| `billing/csi-bm-billing-ui` | Commented out line 23: group: batch |
| `billing/csi-bm-billing-ui` | Commented out line 24: version: v1 |
| `billing/csi-bm-billing-ui` | Commented out line 25: kind: Job |
| `billing/csi-bm-billing-ui` | Commented out line 26: name: .* |
| `billing/csi-bm-billing-ui` | Commented out line 27: patch: |- |
| `billing/csi-bm-billing-ui` | Commented out line 28: - op: replace |
| `billing/csi-bm-billing-ui` | Commented out line 29: path: /metadata/name |
| `billing/csi-bm-billing-ui` | Commented out line 30: value: before-billingmasterui |
| `billing/csi-bm-billing-ui` | Commented out line 31: - op: add |
| `billing/csi-bm-billing-ui` | Commented out line 32: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-billing-ui` | Commented out line 33: value: |
| `billing/csi-bm-billing-ui` | Commented out line 34: name: CSI_MODULENAME |
| `billing/csi-bm-billing-ui` | Commented out line 35: value: "csi-bm-billing-ui" |
| `billing/csi-bm-billing-ui` | Commented out line 36: - op: add |
| `billing/csi-bm-billing-ui` | Commented out line 37: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-billing-ui` | Commented out line 38: value: |
| `billing/csi-bm-billing-ui` | Commented out line 39: name: CSI_DATA_VERSION |
| `billing/csi-bm-billing-ui` | Commented out line 40: value: "4.5.252.0" |
| `billing/csi-bm-billing-ui` | Commented out line 41: - op: add |
| `billing/csi-bm-billing-ui` | Commented out line 42: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-billing-ui` | Commented out line 43: value: |
| `billing/csi-bm-billing-ui` | Commented out line 44: name: CSI_PROJECT_NAME |
| `billing/csi-bm-billing-ui` | Commented out line 45: value: "csi-bm-billing-ui" |
| `billing/csi-bm-billing-ui` | Commented out line 46: - op: add |
| `billing/csi-bm-billing-ui` | Commented out line 47: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-billing-ui` | Commented out line 48: value: |
| `billing/csi-bm-billing-ui` | Commented out line 49: name: CSI_MODULE_NAME |
| `billing/csi-bm-billing-ui` | Commented out line 50: value: "billingmasterui" |
| `billing/csi-bm-billing-ui` | Commented out line 51: - op: add |
| `billing/csi-bm-billing-ui` | Commented out line 52: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-billing-ui` | Commented out line 53: value: |
| `billing/csi-bm-billing-ui` | Commented out line 54: name: CSI_PARENT_MODULE_NAME |
| `billing/csi-bm-billing-ui` | Commented out line 55: value: "billing" |
| `billing/csi-bm-inte-bridge-java-service` | Replaced Sync reference with DM-Initiator |
| `billing/csi-bm-inte-bridge-java-service` | Added new sync-presync/sync-postsync Job patches |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 20: - target: |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 21: group: batch |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 22: version: v1 |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 23: kind: Job |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 24: name: .* |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 25: patch: |- |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 26: - op: replace |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 27: path: /metadata/name |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 28: value: before-csi-bm-inte-bridge-java-service |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 29: namespace: moh-uat |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 30: - op: add |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 31: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 32: value: |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 33: name: CSI_MODULENAME |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 34: value: "csi-bm-invoice-java-service" |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 35: - op: add |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 36: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 37: value: |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 38: name: CSI_DATA_VERSION |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 39: value: "4.2.502.0" |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 40: - op: add |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 41: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 42: value: |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 43: name: CSI_PROJECT_NAME |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 44: value: "csi-bm-inte-bridge-java-service" |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 45: - op: add |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 46: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 47: value: |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 48: name: CSI_MODULE_NAME |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 49: value: "csi-bm-inte-bridge-java-service" |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 50: - op: add |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 51: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 52: value: |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 53: name: CSI_PARENT_MODULE_NAME |
| `billing/csi-bm-inte-bridge-java-service` | Commented out line 54: value: "billing" |
| `billing/csi-bm-invoice-java-service` | Replaced Sync reference with DM-Initiator |
| `billing/csi-bm-invoice-java-service` | Added new sync-presync/sync-postsync Job patches |
| `billing/csi-bm-invoice-java-service` | Commented out line 56: - target: |
| `billing/csi-bm-invoice-java-service` | Commented out line 57: group: batch |
| `billing/csi-bm-invoice-java-service` | Commented out line 58: version: v1 |
| `billing/csi-bm-invoice-java-service` | Commented out line 59: kind: Job |
| `billing/csi-bm-invoice-java-service` | Commented out line 60: name: .* |
| `billing/csi-bm-invoice-java-service` | Commented out line 61: patch: |- |
| `billing/csi-bm-invoice-java-service` | Commented out line 62: - op: replace |
| `billing/csi-bm-invoice-java-service` | Commented out line 63: path: /metadata/name |
| `billing/csi-bm-invoice-java-service` | Commented out line 64: value: before-bmbillinginvoicejava |
| `billing/csi-bm-invoice-java-service` | Commented out line 65: - op: add |
| `billing/csi-bm-invoice-java-service` | Commented out line 66: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-invoice-java-service` | Commented out line 67: value: |
| `billing/csi-bm-invoice-java-service` | Commented out line 68: name: CSI_MODULENAME |
| `billing/csi-bm-invoice-java-service` | Commented out line 69: value: "csi-bm-invoice-java-service" |
| `billing/csi-bm-invoice-java-service` | Commented out line 70: - op: add |
| `billing/csi-bm-invoice-java-service` | Commented out line 71: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-invoice-java-service` | Commented out line 72: value: |
| `billing/csi-bm-invoice-java-service` | Commented out line 73: name: CSI_DATA_VERSION |
| `billing/csi-bm-invoice-java-service` | Commented out line 74: value: "4.2.502.0" |
| `billing/csi-bm-invoice-java-service` | Commented out line 75: - op: add |
| `billing/csi-bm-invoice-java-service` | Commented out line 76: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-invoice-java-service` | Commented out line 77: value: |
| `billing/csi-bm-invoice-java-service` | Commented out line 78: name: CSI_PROJECT_NAME |
| `billing/csi-bm-invoice-java-service` | Commented out line 79: value: "csi-bm-invoice-java-service" |
| `billing/csi-bm-invoice-java-service` | Commented out line 80: - op: add |
| `billing/csi-bm-invoice-java-service` | Commented out line 81: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-invoice-java-service` | Commented out line 82: value: |
| `billing/csi-bm-invoice-java-service` | Commented out line 83: name: CSI_MODULE_NAME |
| `billing/csi-bm-invoice-java-service` | Commented out line 84: value: "bmbillinginvoicejava" |
| `billing/csi-bm-invoice-java-service` | Commented out line 85: - op: add |
| `billing/csi-bm-invoice-java-service` | Commented out line 86: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-invoice-java-service` | Commented out line 87: value: |
| `billing/csi-bm-invoice-java-service` | Commented out line 88: name: CSI_PARENT_MODULE_NAME |
| `billing/csi-bm-invoice-java-service` | Commented out line 89: value: "billing" |
| `billing/csi-bm-invoice-ui` | Replaced Sync reference with DM-Initiator |
| `billing/csi-bm-invoice-ui` | Added new sync-presync/sync-postsync Job patches |
| `billing/csi-bm-invoice-ui` | Commented out line 21: - target: |
| `billing/csi-bm-invoice-ui` | Commented out line 22: group: batch |
| `billing/csi-bm-invoice-ui` | Commented out line 23: version: v1 |
| `billing/csi-bm-invoice-ui` | Commented out line 24: kind: Job |
| `billing/csi-bm-invoice-ui` | Commented out line 25: name: .* |
| `billing/csi-bm-invoice-ui` | Commented out line 26: patch: |- |
| `billing/csi-bm-invoice-ui` | Commented out line 27: - op: replace |
| `billing/csi-bm-invoice-ui` | Commented out line 28: path: /metadata/name |
| `billing/csi-bm-invoice-ui` | Commented out line 29: value: before-bminvoiceui |
| `billing/csi-bm-invoice-ui` | Commented out line 30: - op: add |
| `billing/csi-bm-invoice-ui` | Commented out line 31: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-invoice-ui` | Commented out line 32: value: |
| `billing/csi-bm-invoice-ui` | Commented out line 33: name: CSI_MODULENAME |
| `billing/csi-bm-invoice-ui` | Commented out line 34: value: "csi-bm-invoice-ui" |
| `billing/csi-bm-invoice-ui` | Commented out line 35: - op: add |
| `billing/csi-bm-invoice-ui` | Commented out line 36: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-invoice-ui` | Commented out line 37: value: |
| `billing/csi-bm-invoice-ui` | Commented out line 38: name: CSI_DATA_VERSION |
| `billing/csi-bm-invoice-ui` | Commented out line 39: value: "4.2.1298.0" |
| `billing/csi-bm-invoice-ui` | Commented out line 40: - op: add |
| `billing/csi-bm-invoice-ui` | Commented out line 41: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-invoice-ui` | Commented out line 42: value: |
| `billing/csi-bm-invoice-ui` | Commented out line 43: name: CSI_PROJECT_NAME |
| `billing/csi-bm-invoice-ui` | Commented out line 44: value: "csi-bm-invoice-ui" |
| `billing/csi-bm-invoice-ui` | Commented out line 45: - op: add |
| `billing/csi-bm-invoice-ui` | Commented out line 46: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-invoice-ui` | Commented out line 47: value: |
| `billing/csi-bm-invoice-ui` | Commented out line 48: name: CSI_MODULE_NAME |
| `billing/csi-bm-invoice-ui` | Commented out line 49: value: "bminvoiceui" |
| `billing/csi-bm-invoice-ui` | Commented out line 50: - op: add |
| `billing/csi-bm-invoice-ui` | Commented out line 51: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-invoice-ui` | Commented out line 52: value: |
| `billing/csi-bm-invoice-ui` | Commented out line 53: name: CSI_PARENT_MODULE_NAME |
| `billing/csi-bm-invoice-ui` | Commented out line 54: value: "billing" |
| `billing/csi-bm-promotion-java-service` | Replaced Sync reference with DM-Initiator |
| `billing/csi-bm-promotion-java-service` | Added new sync-presync/sync-postsync Job patches |
| `billing/csi-bm-promotion-java-service` | Commented out line 21: - target: |
| `billing/csi-bm-promotion-java-service` | Commented out line 22: group: batch |
| `billing/csi-bm-promotion-java-service` | Commented out line 23: version: v1 |
| `billing/csi-bm-promotion-java-service` | Commented out line 24: kind: Job |
| `billing/csi-bm-promotion-java-service` | Commented out line 25: name: .* |
| `billing/csi-bm-promotion-java-service` | Commented out line 26: patch: |- |
| `billing/csi-bm-promotion-java-service` | Commented out line 27: - op: replace |
| `billing/csi-bm-promotion-java-service` | Commented out line 28: path: /metadata/name |
| `billing/csi-bm-promotion-java-service` | Commented out line 29: value: before-csi-bm-promotion-java-service |
| `billing/csi-bm-promotion-java-service` | Commented out line 30: - op: add |
| `billing/csi-bm-promotion-java-service` | Commented out line 31: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-promotion-java-service` | Commented out line 32: value: |
| `billing/csi-bm-promotion-java-service` | Commented out line 33: name: CSI_MODULENAME |
| `billing/csi-bm-promotion-java-service` | Commented out line 34: value: "csi-bm-promotion-java-service" |
| `billing/csi-bm-promotion-java-service` | Commented out line 35: - op: add |
| `billing/csi-bm-promotion-java-service` | Commented out line 36: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-promotion-java-service` | Commented out line 37: value: |
| `billing/csi-bm-promotion-java-service` | Commented out line 38: name: CSI_DATA_VERSION |
| `billing/csi-bm-promotion-java-service` | Commented out line 39: value: "4.2.502.0" |
| `billing/csi-bm-promotion-java-service` | Commented out line 40: - op: add |
| `billing/csi-bm-promotion-java-service` | Commented out line 41: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-promotion-java-service` | Commented out line 42: value: |
| `billing/csi-bm-promotion-java-service` | Commented out line 43: name: CSI_PROJECT_NAME |
| `billing/csi-bm-promotion-java-service` | Commented out line 44: value: "csi-bm-promotion-java-service" |
| `billing/csi-bm-promotion-java-service` | Commented out line 45: - op: add |
| `billing/csi-bm-promotion-java-service` | Commented out line 46: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-promotion-java-service` | Commented out line 47: value: |
| `billing/csi-bm-promotion-java-service` | Commented out line 48: name: CSI_MODULE_NAME |
| `billing/csi-bm-promotion-java-service` | Commented out line 49: value: "csi-bm-promotion-java-service" |
| `billing/csi-bm-promotion-java-service` | Commented out line 50: - op: add |
| `billing/csi-bm-promotion-java-service` | Commented out line 51: path: /spec/template/spec/containers/0/env/- |
| `billing/csi-bm-promotion-java-service` | Commented out line 52: value: |
| `billing/csi-bm-promotion-java-service` | Commented out line 53: name: CSI_PARENT_MODULE_NAME |
| `billing/csi-bm-promotion-java-service` | Commented out line 54: value: "billing" |
| `bloodbank/bb-bloodbankgui` | Replaced Sync reference with DM-Initiator |
| `bloodbank/bb-bloodbankgui` | Added new sync-presync/sync-postsync Job patches |
| `bloodbank/bb-bloodbankgui` | Commented out line 21: - target: |
| `bloodbank/bb-bloodbankgui` | Commented out line 22: group: batch |
| `bloodbank/bb-bloodbankgui` | Commented out line 23: version: v1 |
| `bloodbank/bb-bloodbankgui` | Commented out line 24: kind: Job |
| `bloodbank/bb-bloodbankgui` | Commented out line 25: name: .* |
| `bloodbank/bb-bloodbankgui` | Commented out line 26: patch: |- |
| `bloodbank/bb-bloodbankgui` | Commented out line 27: - op: replace |
| `bloodbank/bb-bloodbankgui` | Commented out line 28: path: /metadata/name |
| `bloodbank/bb-bloodbankgui` | Commented out line 29: value: before-bloodbankui |
| `bloodbank/bb-bloodbankgui` | Commented out line 30: - op: add |
| `bloodbank/bb-bloodbankgui` | Commented out line 31: path: /spec/template/spec/containers/0/env/- |
| `bloodbank/bb-bloodbankgui` | Commented out line 32: value: |
| `bloodbank/bb-bloodbankgui` | Commented out line 33: name: CSI_MODULENAME |
| `bloodbank/bb-bloodbankgui` | Commented out line 34: value: "bb-bloodbankgui" |
| `bloodbank/bb-bloodbankgui` | Commented out line 35: - op: add |
| `bloodbank/bb-bloodbankgui` | Commented out line 36: path: /spec/template/spec/containers/0/env/- |
| `bloodbank/bb-bloodbankgui` | Commented out line 37: value: |
| `bloodbank/bb-bloodbankgui` | Commented out line 38: name: CSI_DATA_VERSION |
| `bloodbank/bb-bloodbankgui` | Commented out line 39: value: "4.1.56.0" |
| `bloodbank/bb-bloodbankgui` | Commented out line 40: - op: add |
| `bloodbank/bb-bloodbankgui` | Commented out line 41: path: /spec/template/spec/containers/0/env/- |
| `bloodbank/bb-bloodbankgui` | Commented out line 42: value: |
| `bloodbank/bb-bloodbankgui` | Commented out line 43: name: CSI_PROJECT_NAME |
| `bloodbank/bb-bloodbankgui` | Commented out line 44: value: "bb-bloodbankgui" |
| `bloodbank/bb-bloodbankgui` | Commented out line 45: - op: add |
| `bloodbank/bb-bloodbankgui` | Commented out line 46: path: /spec/template/spec/containers/0/env/- |
| `bloodbank/bb-bloodbankgui` | Commented out line 47: value: |
| `bloodbank/bb-bloodbankgui` | Commented out line 48: name: CSI_MODULE_NAME |
| `bloodbank/bb-bloodbankgui` | Commented out line 49: value: "bloodbankui" |
| `bloodbank/bb-bloodbankgui` | Commented out line 50: - op: add |
| `bloodbank/bb-bloodbankgui` | Commented out line 51: path: /spec/template/spec/containers/0/env/- |
| `bloodbank/bb-bloodbankgui` | Commented out line 52: value: |
| `bloodbank/bb-bloodbankgui` | Commented out line 53: name: CSI_PARENT_MODULE_NAME |
| `bloodbank/bb-bloodbankgui` | Commented out line 54: value: "bloodbank" |
| `bloodbank/bb-donation-srv` | Replaced Sync reference with DM-Initiator |
| `bloodbank/bb-donation-srv` | Removed extra Sync reference: - ../../../Sync-DM/ |
| `bloodbank/bb-donation-srv` | Added new sync-presync/sync-postsync Job patches |
| `bloodbank/bb-donation-srv` | Commented out line 20: - target: |
| `bloodbank/bb-donation-srv` | Commented out line 21: group: batch |
| `bloodbank/bb-donation-srv` | Commented out line 22: version: v1 |
| `bloodbank/bb-donation-srv` | Commented out line 23: kind: Job |
| `bloodbank/bb-donation-srv` | Commented out line 24: name: before |
| `bloodbank/bb-donation-srv` | Commented out line 25: patch: |- |
| `bloodbank/bb-donation-srv` | Commented out line 26: - op: replace |
| `bloodbank/bb-donation-srv` | Commented out line 27: path: /metadata/name |
| `bloodbank/bb-donation-srv` | Commented out line 28: value: before-bloodbanknet |
| `bloodbank/bb-donation-srv` | Commented out line 29: - op: add |
| `bloodbank/bb-donation-srv` | Commented out line 30: path: /spec/template/spec/containers/0/env/- |
| `bloodbank/bb-donation-srv` | Commented out line 31: value: |
| `bloodbank/bb-donation-srv` | Commented out line 32: name: CSI_MODULENAME |
| `bloodbank/bb-donation-srv` | Commented out line 33: value: "bb-donation_srv" |
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
| `bloodbank/bb-donation-srv` | Commented out line 48: value: "bloodbanknet" |
| `bloodbank/bb-donation-srv` | Commented out line 49: - op: add |
| `bloodbank/bb-donation-srv` | Commented out line 50: path: /spec/template/spec/containers/0/env/- |
| `bloodbank/bb-donation-srv` | Commented out line 51: value: |
| `bloodbank/bb-donation-srv` | Commented out line 52: name: CSI_PARENT_MODULE_NAME |
| `bloodbank/bb-donation-srv` | Commented out line 53: value: "bloodbank" |
| `bloodbank/bb-donation-srv` | Commented out line 55: - target: |
| `bloodbank/bb-donation-srv` | Commented out line 56: group: batch |
| `bloodbank/bb-donation-srv` | Commented out line 57: version: v1 |
| `bloodbank/bb-donation-srv` | Commented out line 58: kind: Job |
| `bloodbank/bb-donation-srv` | Commented out line 59: name: data-migration-presync |
| `bloodbank/bb-donation-srv` | Commented out line 60: patch: |- |
| `bloodbank/bb-donation-srv` | Commented out line 61: - op: replace |
| `bloodbank/bb-donation-srv` | Commented out line 62: path: /metadata/name |
| `bloodbank/bb-donation-srv` | Commented out line 63: value: data-migration-presync-bloodbanknet |
| `bloodbank/bb-donation-srv` | Commented out line 64: - op: add |
| `bloodbank/bb-donation-srv` | Commented out line 65: path: /spec/template/spec/containers/0/env/- |
| `bloodbank/bb-donation-srv` | Commented out line 66: value: |
| `bloodbank/bb-donation-srv` | Commented out line 67: name: CSI_DATA_VERSION |
| `bloodbank/bb-donation-srv` | Commented out line 68: value: "4.0.127.0" |
| `bloodbank/bb-donation-srv` | Commented out line 69: - op: add |
| `bloodbank/bb-donation-srv` | Commented out line 70: path: /spec/template/spec/containers/0/env/- |
| `bloodbank/bb-donation-srv` | Commented out line 71: value: |
| `bloodbank/bb-donation-srv` | Commented out line 72: name: CSI_PROJECT_NAME |
| `bloodbank/bb-donation-srv` | Commented out line 73: value: "bb-donation_srv" |
| `bloodbank/bb-donation-srv` | Commented out line 74: - op: add |
| `bloodbank/bb-donation-srv` | Commented out line 75: path: /spec/template/spec/containers/0/env/- |
| `bloodbank/bb-donation-srv` | Commented out line 76: value: |
| `bloodbank/bb-donation-srv` | Commented out line 77: name: CSI_MODULE_NAME |
| `bloodbank/bb-donation-srv` | Commented out line 78: value: "bloodbanknet" |
| `bloodbank/bb-donation-srv` | Commented out line 79: - op: add |
| `bloodbank/bb-donation-srv` | Commented out line 80: path: /spec/template/spec/containers/0/env/- |
| `bloodbank/bb-donation-srv` | Commented out line 81: value: |
| `bloodbank/bb-donation-srv` | Commented out line 82: name: CSI_PARENT_MODULE_NAME |
| `bloodbank/bb-donation-srv` | Commented out line 83: value: "bloodbank" |
| `bloodbank/bb-donation-srv` | Commented out line 86: - target: |
| `bloodbank/bb-donation-srv` | Commented out line 87: group: batch |
| `bloodbank/bb-donation-srv` | Commented out line 88: version: v1 |
| `bloodbank/bb-donation-srv` | Commented out line 89: kind: Job |
| `bloodbank/bb-donation-srv` | Commented out line 90: name: data-migration-postsync |
| `bloodbank/bb-donation-srv` | Commented out line 91: patch: |- |
| `bloodbank/bb-donation-srv` | Commented out line 92: - op: replace |
| `bloodbank/bb-donation-srv` | Commented out line 93: path: /metadata/name |
| `bloodbank/bb-donation-srv` | Commented out line 94: value: data-migration-postsync-bloodbanknet |
| `bloodbank/bb-donation-srv` | Commented out line 95: - op: add |
| `bloodbank/bb-donation-srv` | Commented out line 96: path: /spec/template/spec/containers/0/env/- |
| `bloodbank/bb-donation-srv` | Commented out line 97: value: |
| `bloodbank/bb-donation-srv` | Commented out line 98: name: CSI_DATA_VERSION |
| `bloodbank/bb-donation-srv` | Commented out line 99: value: "4.0.127.0" |
| `bloodbank/bb-donation-srv` | Commented out line 100: - op: add |
| `bloodbank/bb-donation-srv` | Commented out line 101: path: /spec/template/spec/containers/0/env/- |
| `bloodbank/bb-donation-srv` | Commented out line 102: value: |
| `bloodbank/bb-donation-srv` | Commented out line 103: name: CSI_PROJECT_NAME |
| `bloodbank/bb-donation-srv` | Commented out line 104: value: "bb-donation_srv" |
| `bloodbank/bb-donation-srv` | Commented out line 105: - op: add |
| `bloodbank/bb-donation-srv` | Commented out line 106: path: /spec/template/spec/containers/0/env/- |
| `bloodbank/bb-donation-srv` | Commented out line 107: value: |
| `bloodbank/bb-donation-srv` | Commented out line 108: name: CSI_MODULE_NAME |
| `bloodbank/bb-donation-srv` | Commented out line 109: value: "bloodbanknet" |
| `bloodbank/bb-donation-srv` | Commented out line 110: - op: add |
| `bloodbank/bb-donation-srv` | Commented out line 111: path: /spec/template/spec/containers/0/env/- |
| `bloodbank/bb-donation-srv` | Commented out line 112: value: |
| `bloodbank/bb-donation-srv` | Commented out line 113: name: CSI_PARENT_MODULE_NAME |
| `bloodbank/bb-donation-srv` | Commented out line 114: value: "bloodbank" |
| `cssd/csi-cssd-java-sev` | Replaced Sync reference with DM-Initiator |
| `cssd/csi-cssd-java-sev` | Added new sync-presync/sync-postsync Job patches |
| `cssd/csi-cssd-java-sev` | Commented out line 25: - target: |
| `cssd/csi-cssd-java-sev` | Commented out line 26: group: batch |
| `cssd/csi-cssd-java-sev` | Commented out line 27: version: v1 |
| `cssd/csi-cssd-java-sev` | Commented out line 28: kind: Job |
| `cssd/csi-cssd-java-sev` | Commented out line 29: name: before |
| `cssd/csi-cssd-java-sev` | Commented out line 30: patch: |- |
| `cssd/csi-cssd-java-sev` | Commented out line 31: - op: replace |
| `cssd/csi-cssd-java-sev` | Commented out line 32: path: /metadata/name |
| `cssd/csi-cssd-java-sev` | Commented out line 33: value: before-csi-cssd-java-sev |
| `cssd/csi-cssd-java-sev` | Commented out line 34: namespace: moh-uat |
| `cssd/csi-cssd-java-sev` | Commented out line 35: - op: add |
| `cssd/csi-cssd-java-sev` | Commented out line 36: path: /spec/template/spec/containers/0/env/- |
| `cssd/csi-cssd-java-sev` | Commented out line 37: value: |
| `cssd/csi-cssd-java-sev` | Commented out line 38: name: CSI_MODULENAME |
| `cssd/csi-cssd-java-sev` | Commented out line 39: value: "csi-cssd-java-sev" |
| `cssd/csi-cssd-java-sev` | Commented out line 40: - op: add |
| `cssd/csi-cssd-java-sev` | Commented out line 41: path: /spec/template/spec/containers/0/env/- |
| `cssd/csi-cssd-java-sev` | Commented out line 42: value: |
| `cssd/csi-cssd-java-sev` | Commented out line 43: name: CSI_DATA_VERSION |
| `cssd/csi-cssd-java-sev` | Commented out line 44: value: "4.2.106.0" |
| `cssd/csi-cssd-java-sev` | Commented out line 45: - op: add |
| `cssd/csi-cssd-java-sev` | Commented out line 46: path: /spec/template/spec/containers/0/env/- |
| `cssd/csi-cssd-java-sev` | Commented out line 47: value: |
| `cssd/csi-cssd-java-sev` | Commented out line 48: name: CSI_PROJECT_NAME |
| `cssd/csi-cssd-java-sev` | Commented out line 49: value: "csi-cssd-java-sev" |
| `cssd/csi-cssd-java-sev` | Commented out line 50: - op: add |
| `cssd/csi-cssd-java-sev` | Commented out line 51: path: /spec/template/spec/containers/0/env/- |
| `cssd/csi-cssd-java-sev` | Commented out line 52: value: |
| `cssd/csi-cssd-java-sev` | Commented out line 53: name: CSI_MODULE_NAME |
| `cssd/csi-cssd-java-sev` | Commented out line 54: value: "csi-cssd-java-sev" |
| `cssd/csi-cssd-java-sev` | Commented out line 55: - op: add |
| `cssd/csi-cssd-java-sev` | Commented out line 56: path: /spec/template/spec/containers/0/env/- |
| `cssd/csi-cssd-java-sev` | Commented out line 57: value: |
| `cssd/csi-cssd-java-sev` | Commented out line 58: name: CSI_PARENT_MODULE_NAME |
| `cssd/csi-cssd-java-sev` | Commented out line 59: value: "cssd" |
| `cssd/csi-cssd-java-sev` | Commented out line 60: - target: |
| `cssd/csi-cssd-java-sev` | Commented out line 61: group: batch |
| `cssd/csi-cssd-java-sev` | Commented out line 62: version: v1 |
| `cssd/csi-cssd-java-sev` | Commented out line 63: kind: Job |
| `cssd/csi-cssd-java-sev` | Commented out line 64: name: data-migration-presync |
| `cssd/csi-cssd-java-sev` | Commented out line 65: patch: |- |
| `cssd/csi-cssd-java-sev` | Commented out line 66: - op: replace |
| `cssd/csi-cssd-java-sev` | Commented out line 67: path: /metadata/name |
| `cssd/csi-cssd-java-sev` | Commented out line 68: value: datamigrations-pre-csi-cssd-java-sev |
| `cssd/csi-cssd-java-sev` | Commented out line 69: - op: add |
| `cssd/csi-cssd-java-sev` | Commented out line 70: path: /spec/template/spec/containers/0/env/- |
| `cssd/csi-cssd-java-sev` | Commented out line 71: value: |
| `cssd/csi-cssd-java-sev` | Commented out line 72: name: CSI_MODULENAME |
| `cssd/csi-cssd-java-sev` | Commented out line 73: value: "csi-cssd-java-sev" |
| `cssd/csi-cssd-java-sev` | Commented out line 74: - op: add |
| `cssd/csi-cssd-java-sev` | Commented out line 75: path: /spec/template/spec/containers/0/env/- |
| `cssd/csi-cssd-java-sev` | Commented out line 76: value: |
| `cssd/csi-cssd-java-sev` | Commented out line 77: name: CSI_DATA_VERSION |
| `cssd/csi-cssd-java-sev` | Commented out line 78: value: "4.2.106.0" |
| `cssd/csi-cssd-java-sev` | Commented out line 79: - op: add |
| `cssd/csi-cssd-java-sev` | Commented out line 80: path: /spec/template/spec/containers/0/env/- |
| `cssd/csi-cssd-java-sev` | Commented out line 81: value: |
| `cssd/csi-cssd-java-sev` | Commented out line 82: name: CSI_PROJECT_NAME |
| `cssd/csi-cssd-java-sev` | Commented out line 83: value: "csi-cssd-java-sev" |
| `cssd/csi-cssd-java-sev` | Commented out line 84: - op: add |
| `cssd/csi-cssd-java-sev` | Commented out line 85: path: /spec/template/spec/containers/0/env/- |
| `cssd/csi-cssd-java-sev` | Commented out line 86: value: |
| `cssd/csi-cssd-java-sev` | Commented out line 87: name: CSI_MODULE_NAME |
| `cssd/csi-cssd-java-sev` | Commented out line 88: value: "csi-cssd-java-sev" |
| `cssd/csi-cssd-java-sev` | Commented out line 89: - op: add |
| `cssd/csi-cssd-java-sev` | Commented out line 90: path: /spec/template/spec/containers/0/env/- |
| `cssd/csi-cssd-java-sev` | Commented out line 91: value: |
| `cssd/csi-cssd-java-sev` | Commented out line 92: name: CSI_PARENT_MODULE_NAME |
| `cssd/csi-cssd-java-sev` | Commented out line 93: value: "cssd" |
| `dms/csi-document-management-service` | Replaced Sync reference with DM-Initiator |
| `dms/csi-document-management-service` | Added new sync-presync/sync-postsync Job patches |
| `dms/csi-document-management-service` | Commented out line 19: - target: |
| `dms/csi-document-management-service` | Commented out line 20: group: batch |
| `dms/csi-document-management-service` | Commented out line 21: version: v1 |
| `dms/csi-document-management-service` | Commented out line 22: kind: Job |
| `dms/csi-document-management-service` | Commented out line 23: name: before |
| `dms/csi-document-management-service` | Commented out line 24: patch: |- |
| `dms/csi-document-management-service` | Commented out line 25: - op: replace |
| `dms/csi-document-management-service` | Commented out line 26: path: /metadata/name |
| `dms/csi-document-management-service` | Commented out line 27: value: before-dms |
| `dms/csi-document-management-service` | Commented out line 28: namespace: moh-uat |
| `dms/csi-document-management-service` | Commented out line 29: - op: add |
| `dms/csi-document-management-service` | Commented out line 30: path: /spec/template/spec/containers/0/env/- |
| `dms/csi-document-management-service` | Commented out line 31: value: |
| `dms/csi-document-management-service` | Commented out line 32: name: CSI_MODULENAME |
| `dms/csi-document-management-service` | Commented out line 33: value: "csi-java-bb-service" |
| `dms/csi-document-management-service` | Commented out line 34: - op: add |
| `dms/csi-document-management-service` | Commented out line 35: path: /spec/template/spec/containers/0/env/- |
| `dms/csi-document-management-service` | Commented out line 36: value: |
| `dms/csi-document-management-service` | Commented out line 37: name: CSI_DATA_VERSION |
| `dms/csi-document-management-service` | Commented out line 38: value: "4.2.106.0" |
| `dms/csi-document-management-service` | Commented out line 39: - op: add |
| `dms/csi-document-management-service` | Commented out line 40: path: /spec/template/spec/containers/0/env/- |
| `dms/csi-document-management-service` | Commented out line 41: value: |
| `dms/csi-document-management-service` | Commented out line 42: name: CSI_PROJECT_NAME |
| `dms/csi-document-management-service` | Commented out line 43: value: "csi-document-management-service" |
| `dms/csi-document-management-service` | Commented out line 44: - op: add |
| `dms/csi-document-management-service` | Commented out line 45: path: /spec/template/spec/containers/0/env/- |
| `dms/csi-document-management-service` | Commented out line 46: value: |
| `dms/csi-document-management-service` | Commented out line 47: name: CSI_MODULE_NAME |
| `dms/csi-document-management-service` | Commented out line 48: value: "csi-document-management-service" |
| `dms/csi-document-management-service` | Commented out line 49: - op: add |
| `dms/csi-document-management-service` | Commented out line 50: path: /spec/template/spec/containers/0/env/- |
| `dms/csi-document-management-service` | Commented out line 51: value: |
| `dms/csi-document-management-service` | Commented out line 52: name: CSI_PARENT_MODULE_NAME |
| `dms/csi-document-management-service` | Commented out line 53: value: "dms" |
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
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Commented out line 29: value: before-ehripdashboardwiddotnet |
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Commented out line 30: - op: add |
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Commented out line 31: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Commented out line 32: value: |
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Commented out line 33: name: CSI_MODULENAME |
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Commented out line 34: value: "ehripdashboardwiddotnet" |
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Commented out line 35: - op: add |
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Commented out line 36: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Commented out line 37: value: |
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Commented out line 38: name: CSI_DATA_VERSION |
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Commented out line 39: value: "4.0.161.0" |
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Commented out line 40: - op: add |
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Commented out line 41: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Commented out line 42: value: |
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Commented out line 43: name: CSI_PROJECT_NAME |
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Commented out line 44: value: "csi-ehr-com-ip-dashboardwidget-dotnet-sev" |
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Commented out line 45: - op: add |
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Commented out line 46: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Commented out line 47: value: |
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Commented out line 48: name: CSI_MODULE_NAME |
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Commented out line 49: value: "ehripdashboardwiddotnet" |
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Commented out line 50: - op: add |
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Commented out line 51: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Commented out line 52: value: |
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Commented out line 53: name: CSI_PARENT_MODULE_NAME |
| `ehr/csi-ehr-com-ip-dashboardwidget-dotnet-sev` | Commented out line 54: value: "ehr" |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Replaced commented Sync reference with commented DM-Initiator |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Added new sync-presync/sync-postsync Job patches |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 20: - target: |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 21: group: batch |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 22: version: v1 |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 23: kind: Job |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 24: name: .* |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 25: patch: |- |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 26: - op: replace |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 27: path: /metadata/name |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 28: value: before-ehropdmasterdotnet |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 29: - op: add |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 30: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 31: value: |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 32: name: CSI_MODULENAME |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 33: value: "csi-ehr-opd" |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 34: - op: add |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 35: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 36: value: |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 37: name: CSI_DATA_VERSION |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 38: value: "4.0.127.0" |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 39: - op: add |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 40: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 41: value: |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 42: name: CSI_PROJECT_NAME |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 43: value: "csi-ehr-com-opd-master-dotnet-sev" |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 44: - op: add |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 45: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 46: value: |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 47: name: CSI_MODULE_NAME |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 48: value: "ehropdmasterdotnet" |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 49: - op: add |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 50: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 51: value: |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 52: name: CSI_PARENT_MODULE_NAME |
| `ehr/csi-ehr-com-opd-master-dotnet-sev` | Commented out line 53: value: "ehr" |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Replaced Sync reference with DM-Initiator |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Added new sync-presync/sync-postsync Job patches |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 21: - target: |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 22: group: batch |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 23: version: v1 |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 24: kind: Job |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 25: name: .* |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 26: patch: |- |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 27: - op: replace |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 28: path: /metadata/name |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 29: value: before-ehropdpatientdotnet |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 30: - op: add |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 31: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 32: value: |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 33: name: CSI_MODULENAME |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 34: value: "csi-opd-patient-pomr" |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 35: - op: add |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 36: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 37: value: |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 38: name: CSI_DATA_VERSION |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 39: value: "4.0.127.0" |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 40: - op: add |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 41: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 42: value: |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 43: name: CSI_PROJECT_NAME |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 44: value: "csi-ehr-com-opd-patient-dotnet-sev" |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 45: - op: add |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 46: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 47: value: |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 48: name: CSI_MODULE_NAME |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 49: value: "ehropdpatientdotnet" |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 50: - op: add |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 51: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 52: value: |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 53: name: CSI_PARENT_MODULE_NAME |
| `ehr/csi-ehr-com-opd-patient-dotnet-sev` | Commented out line 54: value: "ehr" |
| `ehr/csi-ehr-common-java-sev` | Replaced Sync reference with DM-Initiator |
| `ehr/csi-ehr-common-java-sev` | Added new sync-presync/sync-postsync Job patches |
| `ehr/csi-ehr-common-java-sev` | Commented out line 20: - target: |
| `ehr/csi-ehr-common-java-sev` | Commented out line 21: group: batch |
| `ehr/csi-ehr-common-java-sev` | Commented out line 22: version: v1 |
| `ehr/csi-ehr-common-java-sev` | Commented out line 23: kind: Job |
| `ehr/csi-ehr-common-java-sev` | Commented out line 24: name: before |
| `ehr/csi-ehr-common-java-sev` | Commented out line 25: patch: |- |
| `ehr/csi-ehr-common-java-sev` | Commented out line 26: - op: replace |
| `ehr/csi-ehr-common-java-sev` | Commented out line 27: path: /metadata/name |
| `ehr/csi-ehr-common-java-sev` | Commented out line 28: value: before-csi-ehr-common |
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
| `ehr/csi-ehr-common-java-sev` | Commented out line 48: value: "ehrcommonjava" |
| `ehr/csi-ehr-common-java-sev` | Commented out line 49: - op: add |
| `ehr/csi-ehr-common-java-sev` | Commented out line 50: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-common-java-sev` | Commented out line 51: value: |
| `ehr/csi-ehr-common-java-sev` | Commented out line 52: name: CSI_PARENT_MODULE_NAME |
| `ehr/csi-ehr-common-java-sev` | Commented out line 53: value: "ehr" |
| `ehr/csi-ehr-common-scheduler-java-sev` | Replaced Sync reference with DM-Initiator |
| `ehr/csi-ehr-common-scheduler-java-sev` | Added new sync-presync/sync-postsync Job patches |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 20: - target: |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 21: group: batch |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 22: version: v1 |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 23: kind: Job |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 24: name: .* |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 25: patch: |- |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 26: - op: replace |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 27: path: /metadata/name |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 28: value: before-ehrschedulerjava |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 29: namespace: moh-uat |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 30: - op: add |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 31: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 32: value: |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 33: name: CSI_MODULENAME |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 34: value: "csi-ehr-common-scheduler" |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 35: - op: add |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 36: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 37: value: |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 38: name: CSI_DATA_VERSION |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 39: value: "4.0.127.0" |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 40: - op: add |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 41: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 42: value: |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 43: name: CSI_PROJECT_NAME |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 44: value: "csi-ehr-common-scheduler-java-sev" |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 45: - op: add |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 46: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 47: value: |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 48: name: CSI_MODULE_NAME |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 49: value: "ehrschedulerjava" |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 50: - op: add |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 51: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 52: value: |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 53: name: CSI_PARENT_MODULE_NAME |
| `ehr/csi-ehr-common-scheduler-java-sev` | Commented out line 54: value: "ehr" |
| `ehr/csi-ehr-config-java-sev` | Replaced Sync reference with DM-Initiator |
| `ehr/csi-ehr-config-java-sev` | Added new sync-presync/sync-postsync Job patches |
| `ehr/csi-ehr-config-java-sev` | Commented out line 20: - target: |
| `ehr/csi-ehr-config-java-sev` | Commented out line 21: group: batch |
| `ehr/csi-ehr-config-java-sev` | Commented out line 22: version: v1 |
| `ehr/csi-ehr-config-java-sev` | Commented out line 23: kind: Job |
| `ehr/csi-ehr-config-java-sev` | Commented out line 24: name: .* |
| `ehr/csi-ehr-config-java-sev` | Commented out line 25: patch: |- |
| `ehr/csi-ehr-config-java-sev` | Commented out line 26: - op: replace |
| `ehr/csi-ehr-config-java-sev` | Commented out line 27: path: /metadata/name |
| `ehr/csi-ehr-config-java-sev` | Commented out line 28: value: before-ehrconfigjava |
| `ehr/csi-ehr-config-java-sev` | Commented out line 29: - op: add |
| `ehr/csi-ehr-config-java-sev` | Commented out line 30: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-config-java-sev` | Commented out line 31: value: |
| `ehr/csi-ehr-config-java-sev` | Commented out line 32: name: CSI_MODULENAME |
| `ehr/csi-ehr-config-java-sev` | Commented out line 33: value: "csi-ehr-config" |
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
| `ehr/csi-ehr-config-java-sev` | Commented out line 48: value: "ehrconfigjava" |
| `ehr/csi-ehr-config-java-sev` | Commented out line 49: - op: add |
| `ehr/csi-ehr-config-java-sev` | Commented out line 50: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-config-java-sev` | Commented out line 51: value: |
| `ehr/csi-ehr-config-java-sev` | Commented out line 52: name: CSI_PARENT_MODULE_NAME |
| `ehr/csi-ehr-config-java-sev` | Commented out line 53: value: "ehr" |
| `ehr/csi-ehr-ic-bundle-java-sev` | Replaced Sync reference with DM-Initiator |
| `ehr/csi-ehr-ic-bundle-java-sev` | Added new sync-presync/sync-postsync Job patches |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 20: - target: |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 21: group: batch |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 22: version: v1 |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 23: kind: Job |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 24: name: .* |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 25: patch: |- |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 26: - op: replace |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 27: path: /metadata/name |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 28: value: before-ehricbundlejava |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 29: - op: add |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 30: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 31: value: |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 32: name: CSI_MODULENAME |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 33: value: "csi-ehr-ic-bundle-java-sev" |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 34: - op: add |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 35: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 36: value: |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 37: name: CSI_DATA_VERSION |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 38: value: "4.2.464.0" |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 39: - op: add |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 40: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 41: value: |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 42: name: CSI_PROJECT_NAME |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 43: value: "csi-ehr-ic-bundle-java-sev" |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 44: - op: add |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 45: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 46: value: |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 47: name: CSI_MODULE_NAME |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 48: value: "ehricbundlejava" |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 49: - op: add |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 50: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 51: value: |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 52: name: CSI_PARENT_MODULE_NAME |
| `ehr/csi-ehr-ic-bundle-java-sev` | Commented out line 53: value: "ehr" |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Replaced Sync reference with DM-Initiator |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Added new sync-presync/sync-postsync Job patches |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 20: - target: |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 21: group: batch |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 22: version: v1 |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 23: kind: Job |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 24: name: .* |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 25: patch: |- |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 26: - op: replace |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 27: path: /metadata/name |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 28: value: before-ehricdashboardjava |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 29: - op: add |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 30: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 31: value: |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 32: name: CSI_MODULENAME |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 33: value: "csi-ehr-ic-dashboard" |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 34: - op: add |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 35: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 36: value: |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 37: name: CSI_DATA_VERSION |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 38: value: "4.0.127.0" |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 39: - op: add |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 40: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 41: value: |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 42: name: CSI_PROJECT_NAME |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 43: value: "csi-ehr-ic-dashboard-java-sev" |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 44: - op: add |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 45: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 46: value: |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 47: name: CSI_MODULE_NAME |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 48: value: "ehricdashboardjava" |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 49: - op: add |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 50: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 51: value: |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 52: name: CSI_PARENT_MODULE_NAME |
| `ehr/csi-ehr-ic-dashboard-java-sev` | Commented out line 53: value: "ehr" |
| `ehr/csi-ehr-initialassessment-java-sev` | Replaced Sync reference with DM-Initiator |
| `ehr/csi-ehr-initialassessment-java-sev` | Added new sync-presync/sync-postsync Job patches |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 21: - target: |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 22: group: batch |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 23: version: v1 |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 24: kind: Job |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 25: name: .* |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 26: patch: |- |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 27: - op: replace |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 28: path: /metadata/name |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 29: value: before-ehrintitialassessjava |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 30: - op: add |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 31: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 32: value: |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 33: name: CSI_MODULENAME |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 34: value: "csi-ehr-initialassessment" |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 35: - op: add |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 36: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 37: value: |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 38: name: CSI_DATA_VERSION |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 39: value: "4.0.161.0" |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 40: - op: add |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 41: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 42: value: |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 43: name: CSI_PROJECT_NAME |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 44: value: "csi-ehr-initialassessment-java-sev" |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 45: - op: add |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 46: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 47: value: |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 48: name: CSI_MODULE_NAME |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 49: value: "ehrintitialassessjava" |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 50: - op: add |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 51: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 52: value: |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 53: name: CSI_PARENT_MODULE_NAME |
| `ehr/csi-ehr-initialassessment-java-sev` | Commented out line 54: value: "ehr" |
| `ehr/csi-ehr-ip-java-sev` | Replaced Sync reference with DM-Initiator |
| `ehr/csi-ehr-ip-java-sev` | Added new sync-presync/sync-postsync Job patches |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 20: - target: |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 21: group: batch |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 22: version: v1 |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 23: kind: Job |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 24: name: .* |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 25: patch: |- |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 26: - op: replace |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 27: path: /metadata/name |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 28: value: before-ehripjava |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 29: - op: add |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 30: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 31: value: |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 32: name: CSI_MODULENAME |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 33: value: "csi-ehr-ip-java-sev" |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 34: - op: add |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 35: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 36: value: |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 37: name: CSI_DATA_VERSION |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 38: value: "4.0.127.0" |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 39: - op: add |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 40: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 41: value: |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 42: name: CSI_PROJECT_NAME |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 43: value: "csi-ehr-ip-java-sev" |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 44: - op: add |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 45: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 46: value: |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 47: name: CSI_MODULE_NAME |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 48: value: "ehripjava" |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 49: - op: add |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 50: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 51: value: |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 52: name: CSI_PARENT_MODULE_NAME |
| `ehr/csi-ehr-ip-java-sev` | Commented out line 53: value: "ehr" |
| `ehr/csi-ehr-ldr-java-sev` | Replaced Sync reference with DM-Initiator |
| `ehr/csi-ehr-ldr-java-sev` | Added new sync-presync/sync-postsync Job patches |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 21: - target: |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 22: group: batch |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 23: version: v1 |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 24: kind: Job |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 25: name: .* |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 26: patch: |- |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 27: - op: replace |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 28: path: /metadata/name |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 29: value: before-ehrldrjava |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 30: - op: add |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 31: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 32: value: |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 33: name: CSI_MODULENAME |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 34: value: "csi-ehr-ldr-java-sev" |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 35: - op: add |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 36: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 37: value: |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 38: name: CSI_DATA_VERSION |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 39: value: "4.0.127.0" |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 40: - op: add |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 41: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 42: value: |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 43: name: CSI_PROJECT_NAME |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 44: value: "csi-ehr-ldr-java-sev" |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 45: - op: add |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 46: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 47: value: |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 48: name: CSI_MODULE_NAME |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 49: value: "ehrldrjava" |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 50: - op: add |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 51: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 52: value: |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 53: name: CSI_PARENT_MODULE_NAME |
| `ehr/csi-ehr-ldr-java-sev` | Commented out line 54: value: "ehr" |
| `ehr/csi-ehr-opd-java-sev` | Replaced Sync reference with DM-Initiator |
| `ehr/csi-ehr-opd-java-sev` | Added new sync-presync/sync-postsync Job patches |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 20: - target: |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 21: group: batch |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 22: version: v1 |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 23: kind: Job |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 24: name: .* |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 25: patch: |- |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 26: - op: replace |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 27: path: /metadata/name |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 28: value: before-ehropdjava |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 29: - op: add |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 30: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 31: value: |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 32: name: CSI_MODULENAME |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 33: value: "csi-ehr-opd" |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 34: - op: add |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 35: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 36: value: |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 37: name: CSI_DATA_VERSION |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 38: value: "4.0.127.0" |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 39: - op: add |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 40: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 41: value: |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 42: name: CSI_PROJECT_NAME |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 43: value: "csi-ehr-opd-java-sev" |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 44: - op: add |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 45: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 46: value: |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 47: name: CSI_MODULE_NAME |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 48: value: "ehropdjava" |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 49: - op: add |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 50: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 51: value: |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 52: name: CSI_PARENT_MODULE_NAME |
| `ehr/csi-ehr-opd-java-sev` | Commented out line 53: value: "ehr" |
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
| `ehr/csi-ehr-opd-patient-pomr-java-sev` | Commented out line 28: - op: add |
| `ehr/csi-ehr-opd-patient-pomr-java-sev` | Commented out line 29: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-opd-patient-pomr-java-sev` | Commented out line 30: value: |
| `ehr/csi-ehr-opd-patient-pomr-java-sev` | Commented out line 31: name: CSI_MODULENAME |
| `ehr/csi-ehr-opd-patient-pomr-java-sev` | Commented out line 32: value: "csi-opd-patient-pomr" |
| `ehr/csi-ehr-opd-patient-pomr-java-sev` | Commented out line 33: - op: add |
| `ehr/csi-ehr-opd-patient-pomr-java-sev` | Commented out line 34: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-opd-patient-pomr-java-sev` | Commented out line 35: value: |
| `ehr/csi-ehr-opd-patient-pomr-java-sev` | Commented out line 36: name: CSI_DATA_VERSION |
| `ehr/csi-ehr-opd-patient-pomr-java-sev` | Commented out line 37: value: "4.0.125.0" |
| `ehr/csi-ehr-opd-patient-pomr-java-sev` | Commented out line 38: - op: add |
| `ehr/csi-ehr-opd-patient-pomr-java-sev` | Commented out line 39: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-opd-patient-pomr-java-sev` | Commented out line 40: value: |
| `ehr/csi-ehr-opd-patient-pomr-java-sev` | Commented out line 41: name: CSI_PROJECT_NAME |
| `ehr/csi-ehr-opd-patient-pomr-java-sev` | Commented out line 42: value: "csi-ehr-opd-patient-pomr-java-sev" |
| `ehr/csi-ehr-opd-patient-pomr-java-sev` | Commented out line 43: - op: add |
| `ehr/csi-ehr-opd-patient-pomr-java-sev` | Commented out line 44: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-opd-patient-pomr-java-sev` | Commented out line 45: value: |
| `ehr/csi-ehr-opd-patient-pomr-java-sev` | Commented out line 46: name: CSI_MODULE_NAME |
| `ehr/csi-ehr-opd-patient-pomr-java-sev` | Commented out line 47: value: "ehrpomrjava" |
| `ehr/csi-ehr-opd-patient-pomr-java-sev` | Commented out line 48: - op: add |
| `ehr/csi-ehr-opd-patient-pomr-java-sev` | Commented out line 49: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-opd-patient-pomr-java-sev` | Commented out line 50: value: |
| `ehr/csi-ehr-opd-patient-pomr-java-sev` | Commented out line 51: name: CSI_PARENT_MODULE_NAME |
| `ehr/csi-ehr-opd-patient-pomr-java-sev` | Commented out line 52: value: "ehr" |
| `ehr/csi-ehr-opd-ui` | Replaced Sync reference with DM-Initiator |
| `ehr/csi-ehr-opd-ui` | Added new sync-presync/sync-postsync Job patches |
| `ehr/csi-ehr-opd-ui` | Commented out line 20: - target: |
| `ehr/csi-ehr-opd-ui` | Commented out line 21: group: batch |
| `ehr/csi-ehr-opd-ui` | Commented out line 22: version: v1 |
| `ehr/csi-ehr-opd-ui` | Commented out line 23: kind: Job |
| `ehr/csi-ehr-opd-ui` | Commented out line 24: name: .* |
| `ehr/csi-ehr-opd-ui` | Commented out line 25: patch: |- |
| `ehr/csi-ehr-opd-ui` | Commented out line 26: - op: replace |
| `ehr/csi-ehr-opd-ui` | Commented out line 27: path: /metadata/name |
| `ehr/csi-ehr-opd-ui` | Commented out line 28: value: before-ehropdui |
| `ehr/csi-ehr-opd-ui` | Commented out line 29: - op: add |
| `ehr/csi-ehr-opd-ui` | Commented out line 30: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-opd-ui` | Commented out line 31: value: |
| `ehr/csi-ehr-opd-ui` | Commented out line 32: name: CSI_MODULENAME |
| `ehr/csi-ehr-opd-ui` | Commented out line 33: value: "csi-ehr-opd-ui" |
| `ehr/csi-ehr-opd-ui` | Commented out line 34: - op: add |
| `ehr/csi-ehr-opd-ui` | Commented out line 35: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-opd-ui` | Commented out line 36: value: |
| `ehr/csi-ehr-opd-ui` | Commented out line 37: name: CSI_DATA_VERSION |
| `ehr/csi-ehr-opd-ui` | Commented out line 38: value: "AMD-10802" |
| `ehr/csi-ehr-opd-ui` | Commented out line 39: - op: add |
| `ehr/csi-ehr-opd-ui` | Commented out line 40: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-opd-ui` | Commented out line 41: value: |
| `ehr/csi-ehr-opd-ui` | Commented out line 42: name: CSI_PROJECT_NAME |
| `ehr/csi-ehr-opd-ui` | Commented out line 43: value: "csi-ehr-opd-ui" |
| `ehr/csi-ehr-opd-ui` | Commented out line 44: - op: add |
| `ehr/csi-ehr-opd-ui` | Commented out line 45: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-opd-ui` | Commented out line 46: value: |
| `ehr/csi-ehr-opd-ui` | Commented out line 47: name: CSI_MODULE_NAME |
| `ehr/csi-ehr-opd-ui` | Commented out line 48: value: "ehropdui" |
| `ehr/csi-ehr-opd-ui` | Commented out line 49: - op: add |
| `ehr/csi-ehr-opd-ui` | Commented out line 50: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-opd-ui` | Commented out line 51: value: |
| `ehr/csi-ehr-opd-ui` | Commented out line 52: name: CSI_PARENT_MODULE_NAME |
| `ehr/csi-ehr-opd-ui` | Commented out line 53: value: "ehr" |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Replaced Sync reference with DM-Initiator |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Added new sync-presync/sync-postsync Job patches |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 21: - target: |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 22: group: batch |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 23: version: v1 |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 24: kind: Job |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 25: name: .* |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 26: patch: |- |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 27: - op: replace |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 28: path: /metadata/name |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 29: value: before-ehroranesthesiajava |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 30: - op: add |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 31: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 32: value: |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 33: name: CSI_MODULENAME |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 34: value: "csi-ehr-or-anesthesia-java-sev" |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 35: - op: add |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 36: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 37: value: |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 38: name: CSI_DATA_VERSION |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 39: value: "4.0.127.0" |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 40: - op: add |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 41: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 42: value: |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 43: name: CSI_PROJECT_NAME |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 44: value: "csi-ehr-or-anesthesia-java-sev" |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 45: - op: add |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 46: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 47: value: |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 48: name: CSI_MODULE_NAME |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 49: value: "ehroranesthesiajava" |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 50: - op: add |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 51: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 52: value: |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 53: name: CSI_PARENT_MODULE_NAME |
| `ehr/csi-ehr-or-anesthesia-java-sev` | Commented out line 54: value: "ehr" |
| `ehr/csi-ehr-or-book-java-sev` | Replaced Sync reference with DM-Initiator |
| `ehr/csi-ehr-or-book-java-sev` | Added new sync-presync/sync-postsync Job patches |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 20: - target: |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 21: group: batch |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 22: version: v1 |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 23: kind: Job |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 24: name: .* |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 25: patch: |- |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 26: - op: replace |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 27: path: /metadata/name |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 28: value: before-ehrorbookjava |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 29: namespace: moh-uat |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 30: - op: add |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 31: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 32: value: |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 33: name: CSI_MODULENAME |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 34: value: "csi-ehr-or-book-java-sev" |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 35: - op: add |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 36: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 37: value: |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 38: name: CSI_DATA_VERSION |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 39: value: "4.0.127.0" |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 40: - op: add |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 41: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 42: value: |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 43: name: CSI_PROJECT_NAME |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 44: value: "csi-ehr-or-book-java-sev" |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 45: - op: add |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 46: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 47: value: |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 48: name: CSI_MODULE_NAME |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 49: value: "ehrorbookjava" |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 50: - op: add |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 51: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 52: value: |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 53: name: CSI_PARENT_MODULE_NAME |
| `ehr/csi-ehr-or-book-java-sev` | Commented out line 54: value: "ehr" |
| `ehr/csi-ehr-or-booking-java-sev` | Replaced Sync reference with DM-Initiator |
| `ehr/csi-ehr-or-booking-java-sev` | Added new sync-presync/sync-postsync Job patches |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 21: - target: |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 22: group: batch |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 23: version: v1 |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 24: kind: Job |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 25: name: .* |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 26: patch: |- |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 27: - op: replace |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 28: path: /metadata/name |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 29: value: before-ehrorbookingjava |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 30: - op: add |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 31: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 32: value: |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 33: name: CSI_MODULENAME |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 34: value: "csi-ehr-or-booking-java-sev" |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 35: - op: add |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 36: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 37: value: |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 38: name: CSI_DATA_VERSION |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 39: value: "4.0.127.0" |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 40: - op: add |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 41: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 42: value: |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 43: name: CSI_PROJECT_NAME |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 44: value: "csi-ehr-or-booking-java-sev" |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 45: - op: add |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 46: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 47: value: |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 48: name: CSI_MODULE_NAME |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 49: value: "ehrorbookingjava" |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 50: - op: add |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 51: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 52: value: |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 53: name: CSI_PARENT_MODULE_NAME |
| `ehr/csi-ehr-or-booking-java-sev` | Commented out line 54: value: "ehr" |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Replaced Sync reference with DM-Initiator |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Added new sync-presync/sync-postsync Job patches |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 20: - target: |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 21: group: batch |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 22: version: v1 |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 23: kind: Job |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 24: name: .* |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 25: patch: |- |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 26: - op: replace |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 27: path: /metadata/name |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 28: value: before-ehrspecializedclinicjava |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 29: namespace: moh-prod |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 30: - op: add |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 31: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 32: value: |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 33: name: CSI_MODULENAME |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 34: value: "csi-ehr-specialized-clinic-java-sev" |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 35: - op: add |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 36: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 37: value: |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 38: name: CSI_DATA_VERSION |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 39: value: "4.0.161.0" |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 40: - op: add |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 41: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 42: value: |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 43: name: CSI_PROJECT_NAME |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 44: value: "csi-ehr-specialized-clinic-java-sev" |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 45: - op: add |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 46: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 47: value: |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 48: name: CSI_MODULE_NAME |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 49: value: "ehrspecializedclinicjava" |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 50: - op: add |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 51: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 52: value: |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 53: name: CSI_PARENT_MODULE_NAME |
| `ehr/csi-ehr-specialized-clinic-java-sev` | Commented out line 54: value: "ehr" |
| `ehr/csi-ehr-template-java-sev` | Replaced Sync reference with DM-Initiator |
| `ehr/csi-ehr-template-java-sev` | Added new sync-presync/sync-postsync Job patches |
| `ehr/csi-ehr-template-java-sev` | Commented out line 20: - target: |
| `ehr/csi-ehr-template-java-sev` | Commented out line 21: group: batch |
| `ehr/csi-ehr-template-java-sev` | Commented out line 22: version: v1 |
| `ehr/csi-ehr-template-java-sev` | Commented out line 23: kind: Job |
| `ehr/csi-ehr-template-java-sev` | Commented out line 24: name: .* |
| `ehr/csi-ehr-template-java-sev` | Commented out line 25: patch: |- |
| `ehr/csi-ehr-template-java-sev` | Commented out line 26: - op: replace |
| `ehr/csi-ehr-template-java-sev` | Commented out line 27: path: /metadata/name |
| `ehr/csi-ehr-template-java-sev` | Commented out line 28: value: before-ehrtemplatejava |
| `ehr/csi-ehr-template-java-sev` | Commented out line 29: namespace: moh-uat |
| `ehr/csi-ehr-template-java-sev` | Commented out line 30: - op: add |
| `ehr/csi-ehr-template-java-sev` | Commented out line 31: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-template-java-sev` | Commented out line 32: value: |
| `ehr/csi-ehr-template-java-sev` | Commented out line 33: name: CSI_MODULENAME |
| `ehr/csi-ehr-template-java-sev` | Commented out line 34: value: "csi-ehr-template" |
| `ehr/csi-ehr-template-java-sev` | Commented out line 35: - op: add |
| `ehr/csi-ehr-template-java-sev` | Commented out line 36: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-template-java-sev` | Commented out line 37: value: |
| `ehr/csi-ehr-template-java-sev` | Commented out line 38: name: CSI_DATA_VERSION |
| `ehr/csi-ehr-template-java-sev` | Commented out line 39: value: "4.0.127.0" |
| `ehr/csi-ehr-template-java-sev` | Commented out line 40: - op: add |
| `ehr/csi-ehr-template-java-sev` | Commented out line 41: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-template-java-sev` | Commented out line 42: value: |
| `ehr/csi-ehr-template-java-sev` | Commented out line 43: name: CSI_PROJECT_NAME |
| `ehr/csi-ehr-template-java-sev` | Commented out line 44: value: "csi-ehr-template-java-sev" |
| `ehr/csi-ehr-template-java-sev` | Commented out line 45: - op: add |
| `ehr/csi-ehr-template-java-sev` | Commented out line 46: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-template-java-sev` | Commented out line 47: value: |
| `ehr/csi-ehr-template-java-sev` | Commented out line 48: name: CSI_MODULE_NAME |
| `ehr/csi-ehr-template-java-sev` | Commented out line 49: value: "ehrtemplatejava" |
| `ehr/csi-ehr-template-java-sev` | Commented out line 50: - op: add |
| `ehr/csi-ehr-template-java-sev` | Commented out line 51: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-template-java-sev` | Commented out line 52: value: |
| `ehr/csi-ehr-template-java-sev` | Commented out line 53: name: CSI_PARENT_MODULE_NAME |
| `ehr/csi-ehr-template-java-sev` | Commented out line 54: value: "ehr" |
| `ehr/csi-ehr-template-java-sev` | Commented out line 55: - target: |
| `ehr/csi-ehr-template-java-sev` | Commented out line 56: group: batch |
| `ehr/csi-ehr-template-java-sev` | Commented out line 57: version: v1 |
| `ehr/csi-ehr-template-java-sev` | Commented out line 58: kind: Job |
| `ehr/csi-ehr-template-java-sev` | Commented out line 59: name: data-migration_presync |
| `ehr/csi-ehr-template-java-sev` | Commented out line 60: patch: |- |
| `ehr/csi-ehr-template-java-sev` | Commented out line 61: - op: replace |
| `ehr/csi-ehr-template-java-sev` | Commented out line 62: path: /metadata/name |
| `ehr/csi-ehr-template-java-sev` | Commented out line 63: value: datamigrations-pre-ehrtemplatejava |
| `ehr/csi-ehr-template-java-sev` | Commented out line 64: namespace: moh-uat |
| `ehr/csi-ehr-template-java-sev` | Commented out line 65: - op: add |
| `ehr/csi-ehr-template-java-sev` | Commented out line 66: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-template-java-sev` | Commented out line 67: value: |
| `ehr/csi-ehr-template-java-sev` | Commented out line 68: name: CSI_MODULENAME |
| `ehr/csi-ehr-template-java-sev` | Commented out line 69: value: "csi-ehr-template-java-service" |
| `ehr/csi-ehr-template-java-sev` | Commented out line 70: - op: add |
| `ehr/csi-ehr-template-java-sev` | Commented out line 71: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-template-java-sev` | Commented out line 72: value: |
| `ehr/csi-ehr-template-java-sev` | Commented out line 73: name: CSI_DATA_VERSION |
| `ehr/csi-ehr-template-java-sev` | Commented out line 74: value: "4.2.502.0" |
| `ehr/csi-ehr-template-java-sev` | Commented out line 75: - op: add |
| `ehr/csi-ehr-template-java-sev` | Commented out line 76: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-template-java-sev` | Commented out line 77: value: |
| `ehr/csi-ehr-template-java-sev` | Commented out line 78: name: CSI_PROJECT_NAME |
| `ehr/csi-ehr-template-java-sev` | Commented out line 79: value: "csi-ehr-template-java-sev" |
| `ehr/csi-ehr-template-java-sev` | Commented out line 80: - op: add |
| `ehr/csi-ehr-template-java-sev` | Commented out line 81: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-template-java-sev` | Commented out line 82: value: |
| `ehr/csi-ehr-template-java-sev` | Commented out line 83: name: CSI_MODULE_NAME |
| `ehr/csi-ehr-template-java-sev` | Commented out line 84: value: "ehrtemplatejava" |
| `ehr/csi-ehr-template-java-sev` | Commented out line 85: - op: add |
| `ehr/csi-ehr-template-java-sev` | Commented out line 86: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-ehr-template-java-sev` | Commented out line 87: value: |
| `ehr/csi-ehr-template-java-sev` | Commented out line 88: name: CSI_PARENT_MODULE_NAME |
| `ehr/csi-ehr-template-java-sev` | Commented out line 89: value: "ehr" |
| `ehr/csi-workflow-automation-service-java-sev` | Replaced commented Sync reference with commented DM-Initiator |
| `ehr/csi-workflow-automation-service-java-sev` | Added new sync-presync/sync-postsync Job patches |
| `ehr/csi-workflow-automation-service-java-sev` | Commented out line 21: - target: |
| `ehr/csi-workflow-automation-service-java-sev` | Commented out line 22: group: batch |
| `ehr/csi-workflow-automation-service-java-sev` | Commented out line 23: version: v1 |
| `ehr/csi-workflow-automation-service-java-sev` | Commented out line 24: kind: Job |
| `ehr/csi-workflow-automation-service-java-sev` | Commented out line 25: name: .* |
| `ehr/csi-workflow-automation-service-java-sev` | Commented out line 26: patch: |- |
| `ehr/csi-workflow-automation-service-java-sev` | Commented out line 27: - op: replace |
| `ehr/csi-workflow-automation-service-java-sev` | Commented out line 28: path: /metadata/name |
| `ehr/csi-workflow-automation-service-java-sev` | Commented out line 29: value: before-workflow |
| `ehr/csi-workflow-automation-service-java-sev` | Commented out line 30: namespace: moh-uat |
| `ehr/csi-workflow-automation-service-java-sev` | Commented out line 31: - op: add |
| `ehr/csi-workflow-automation-service-java-sev` | Commented out line 32: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-workflow-automation-service-java-sev` | Commented out line 33: value: |
| `ehr/csi-workflow-automation-service-java-sev` | Commented out line 34: name: CSI_MODULENAME |
| `ehr/csi-workflow-automation-service-java-sev` | Commented out line 35: value: "csi-workflow-automation" |
| `ehr/csi-workflow-automation-service-java-sev` | Commented out line 36: - op: add |
| `ehr/csi-workflow-automation-service-java-sev` | Commented out line 37: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-workflow-automation-service-java-sev` | Commented out line 38: value: |
| `ehr/csi-workflow-automation-service-java-sev` | Commented out line 39: name: CSI_DATA_VERSION |
| `ehr/csi-workflow-automation-service-java-sev` | Commented out line 40: value: "4.0.127.0" |
| `ehr/csi-workflow-automation-service-java-sev` | Commented out line 41: - op: add |
| `ehr/csi-workflow-automation-service-java-sev` | Commented out line 42: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-workflow-automation-service-java-sev` | Commented out line 43: value: |
| `ehr/csi-workflow-automation-service-java-sev` | Commented out line 44: name: CSI_PROJECT_NAME |
| `ehr/csi-workflow-automation-service-java-sev` | Commented out line 45: value: "csi-workflow-automation-service-java-sev" |
| `ehr/csi-workflow-automation-service-java-sev` | Commented out line 46: - op: add |
| `ehr/csi-workflow-automation-service-java-sev` | Commented out line 47: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-workflow-automation-service-java-sev` | Commented out line 48: value: |
| `ehr/csi-workflow-automation-service-java-sev` | Commented out line 49: name: CSI_MODULE_NAME |
| `ehr/csi-workflow-automation-service-java-sev` | Commented out line 50: value: "workflow" |
| `ehr/csi-workflow-automation-service-java-sev` | Commented out line 51: - op: add |
| `ehr/csi-workflow-automation-service-java-sev` | Commented out line 52: path: /spec/template/spec/containers/0/env/- |
| `ehr/csi-workflow-automation-service-java-sev` | Commented out line 53: value: |
| `ehr/csi-workflow-automation-service-java-sev` | Commented out line 54: name: CSI_PARENT_MODULE_NAME |
| `ehr/csi-workflow-automation-service-java-sev` | Commented out line 55: value: "ehr" |
| `ehr/ehr-data-strem-core` | Replaced commented Sync reference with commented DM-Initiator |
| `ehr/ehr-data-strem-core` | Updated Deployment target name: ehr-data-stream-core -> ehr-data-strem-core |
| `ehr/ehr-data-strem-core` | Updated Deployment target name: ehr-data-stream-core -> ehr-data-strem-core |
| `ehr/ehr-ic-ui` | Replaced Sync reference with DM-Initiator |
| `ehr/ehr-ic-ui` | Added new sync-presync/sync-postsync Job patches |
| `ehr/ehr-ic-ui` | Commented out line 21: - target: |
| `ehr/ehr-ic-ui` | Commented out line 22: group: batch |
| `ehr/ehr-ic-ui` | Commented out line 23: version: v1 |
| `ehr/ehr-ic-ui` | Commented out line 24: kind: Job |
| `ehr/ehr-ic-ui` | Commented out line 25: name: .* |
| `ehr/ehr-ic-ui` | Commented out line 26: patch: |- |
| `ehr/ehr-ic-ui` | Commented out line 27: - op: replace |
| `ehr/ehr-ic-ui` | Commented out line 28: path: /metadata/name |
| `ehr/ehr-ic-ui` | Commented out line 29: value: before-ehricui |
| `ehr/ehr-ic-ui` | Commented out line 30: - op: add |
| `ehr/ehr-ic-ui` | Commented out line 31: path: /spec/template/spec/containers/0/env/- |
| `ehr/ehr-ic-ui` | Commented out line 32: value: |
| `ehr/ehr-ic-ui` | Commented out line 33: name: CSI_MODULENAME |
| `ehr/ehr-ic-ui` | Commented out line 34: value: "csi-ehr-ic-ui" |
| `ehr/ehr-ic-ui` | Commented out line 35: - op: add |
| `ehr/ehr-ic-ui` | Commented out line 36: path: /spec/template/spec/containers/0/env/- |
| `ehr/ehr-ic-ui` | Commented out line 37: value: |
| `ehr/ehr-ic-ui` | Commented out line 38: name: CSI_DATA_VERSION |
| `ehr/ehr-ic-ui` | Commented out line 39: value: "4.2.464.0" |
| `ehr/ehr-ic-ui` | Commented out line 40: - op: add |
| `ehr/ehr-ic-ui` | Commented out line 41: path: /spec/template/spec/containers/0/env/- |
| `ehr/ehr-ic-ui` | Commented out line 42: value: |
| `ehr/ehr-ic-ui` | Commented out line 43: name: CSI_PROJECT_NAME |
| `ehr/ehr-ic-ui` | Commented out line 44: value: "csi-ehr-ic-ui" |
| `ehr/ehr-ic-ui` | Commented out line 45: - op: add |
| `ehr/ehr-ic-ui` | Commented out line 46: path: /spec/template/spec/containers/0/env/- |
| `ehr/ehr-ic-ui` | Commented out line 47: value: |
| `ehr/ehr-ic-ui` | Commented out line 48: name: CSI_MODULE_NAME |
| `ehr/ehr-ic-ui` | Commented out line 49: value: "ehricui" |
| `ehr/ehr-ic-ui` | Commented out line 50: - op: add |
| `ehr/ehr-ic-ui` | Commented out line 51: path: /spec/template/spec/containers/0/env/- |
| `ehr/ehr-ic-ui` | Commented out line 52: value: |
| `ehr/ehr-ic-ui` | Commented out line 53: name: CSI_PARENT_MODULE_NAME |
| `ehr/ehr-ic-ui` | Commented out line 54: value: "ehr" |
| `empi/csi-empi-webui` | Replaced Sync reference with DM-Initiator |
| `empi/csi-empi-webui` | Added new sync-presync/sync-postsync Job patches |
| `empi/csi-empi-webui` | Commented out line 20: - target: |
| `empi/csi-empi-webui` | Commented out line 21: group: batch |
| `empi/csi-empi-webui` | Commented out line 22: version: v1 |
| `empi/csi-empi-webui` | Commented out line 23: kind: Job |
| `empi/csi-empi-webui` | Commented out line 24: name: .* |
| `empi/csi-empi-webui` | Commented out line 25: patch: |- |
| `empi/csi-empi-webui` | Commented out line 26: - op: replace |
| `empi/csi-empi-webui` | Commented out line 27: path: /metadata/name |
| `empi/csi-empi-webui` | Commented out line 28: value: before-csi-empi-ui |
| `empi/csi-empi-webui` | Commented out line 29: - op: add |
| `empi/csi-empi-webui` | Commented out line 30: path: /spec/template/spec/containers/0/env/- |
| `empi/csi-empi-webui` | Commented out line 31: value: |
| `empi/csi-empi-webui` | Commented out line 32: name: CSI_MODULENAME |
| `empi/csi-empi-webui` | Commented out line 33: value: "csi-empi-ui" |
| `empi/csi-empi-webui` | Commented out line 34: - op: add |
| `empi/csi-empi-webui` | Commented out line 35: path: /spec/template/spec/containers/0/env/- |
| `empi/csi-empi-webui` | Commented out line 36: value: |
| `empi/csi-empi-webui` | Commented out line 37: name: CSI_DATA_VERSION |
| `empi/csi-empi-webui` | Commented out line 38: value: "4.2.106.0" |
| `empi/csi-empi-webui` | Commented out line 39: - op: add |
| `empi/csi-empi-webui` | Commented out line 40: path: /spec/template/spec/containers/0/env/- |
| `empi/csi-empi-webui` | Commented out line 41: value: |
| `empi/csi-empi-webui` | Commented out line 42: name: CSI_PROJECT_NAME |
| `empi/csi-empi-webui` | Commented out line 43: value: "csi-empi-webui" |
| `empi/csi-empi-webui` | Commented out line 44: - op: add |
| `empi/csi-empi-webui` | Commented out line 45: path: /spec/template/spec/containers/0/env/- |
| `empi/csi-empi-webui` | Commented out line 46: value: |
| `empi/csi-empi-webui` | Commented out line 47: name: CSI_MODULE_NAME |
| `empi/csi-empi-webui` | Commented out line 48: value: "empiui" |
| `empi/csi-empi-webui` | Commented out line 49: - op: add |
| `empi/csi-empi-webui` | Commented out line 50: path: /spec/template/spec/containers/0/env/- |
| `empi/csi-empi-webui` | Commented out line 51: value: |
| `empi/csi-empi-webui` | Commented out line 52: name: CSI_PARENT_MODULE_NAME |
| `empi/csi-empi-webui` | Commented out line 53: value: "empi" |
| `er/csi-ehr-er-functions-dotnet-sev` | Replaced Sync reference with DM-Initiator |
| `er/csi-ehr-er-functions-dotnet-sev` | Added new sync-presync/sync-postsync Job patches |
| `er/csi-ehr-er-functions-dotnet-sev` | Commented out line 21: - target: |
| `er/csi-ehr-er-functions-dotnet-sev` | Commented out line 22: group: batch |
| `er/csi-ehr-er-functions-dotnet-sev` | Commented out line 23: version: v1 |
| `er/csi-ehr-er-functions-dotnet-sev` | Commented out line 24: kind: Job |
| `er/csi-ehr-er-functions-dotnet-sev` | Commented out line 25: name: before |
| `er/csi-ehr-er-functions-dotnet-sev` | Commented out line 26: patch: |- |
| `er/csi-ehr-er-functions-dotnet-sev` | Commented out line 27: - op: replace |
| `er/csi-ehr-er-functions-dotnet-sev` | Commented out line 28: path: /metadata/name |
| `er/csi-ehr-er-functions-dotnet-sev` | Commented out line 29: value: before-erfunctiondotnet |
| `er/csi-ehr-er-functions-dotnet-sev` | Commented out line 30: - op: add |
| `er/csi-ehr-er-functions-dotnet-sev` | Commented out line 31: path: /spec/template/spec/containers/0/env/- |
| `er/csi-ehr-er-functions-dotnet-sev` | Commented out line 32: value: |
| `er/csi-ehr-er-functions-dotnet-sev` | Commented out line 33: name: CSI_MODULENAME |
| `er/csi-ehr-er-functions-dotnet-sev` | Commented out line 34: value: "csi-ehr-er-functions-dotnet-sev" |
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
| `er/csi-ehr-er-functions-dotnet-sev` | Commented out line 49: value: "erfunctiondotnet" |
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
| `er/csi-ehr-er-ui` | Commented out line 35: - target: |
| `er/csi-ehr-er-ui` | Commented out line 36: group: batch |
| `er/csi-ehr-er-ui` | Commented out line 37: version: v1 |
| `er/csi-ehr-er-ui` | Commented out line 38: kind: Job |
| `er/csi-ehr-er-ui` | Commented out line 39: name: .* |
| `er/csi-ehr-er-ui` | Commented out line 40: patch: |- |
| `er/csi-ehr-er-ui` | Commented out line 41: - op: replace |
| `er/csi-ehr-er-ui` | Commented out line 42: path: /metadata/name |
| `er/csi-ehr-er-ui` | Commented out line 43: value: before-ehrerui |
| `er/csi-ehr-er-ui` | Commented out line 44: namespace: moh-uat |
| `er/csi-ehr-er-ui` | Commented out line 45: - op: add |
| `er/csi-ehr-er-ui` | Commented out line 46: path: /spec/template/spec/containers/0/env/- |
| `er/csi-ehr-er-ui` | Commented out line 47: value: |
| `er/csi-ehr-er-ui` | Commented out line 48: name: CSI_MODULENAME |
| `er/csi-ehr-er-ui` | Commented out line 49: value: "csi-ehr-er-ui" |
| `er/csi-ehr-er-ui` | Commented out line 50: - op: add |
| `er/csi-ehr-er-ui` | Commented out line 51: path: /spec/template/spec/containers/0/env/- |
| `er/csi-ehr-er-ui` | Commented out line 52: value: |
| `er/csi-ehr-er-ui` | Commented out line 53: name: CSI_DATA_VERSION |
| `er/csi-ehr-er-ui` | Commented out line 54: value: "4.1.19.22-hf2" |
| `er/csi-ehr-er-ui` | Commented out line 55: - op: add |
| `er/csi-ehr-er-ui` | Commented out line 56: path: /spec/template/spec/containers/0/env/- |
| `er/csi-ehr-er-ui` | Commented out line 57: value: |
| `er/csi-ehr-er-ui` | Commented out line 58: name: CSI_PROJECT_NAME |
| `er/csi-ehr-er-ui` | Commented out line 59: value: "csi-ehr-er-ui" |
| `er/csi-ehr-er-ui` | Commented out line 60: - op: add |
| `er/csi-ehr-er-ui` | Commented out line 61: path: /spec/template/spec/containers/0/env/- |
| `er/csi-ehr-er-ui` | Commented out line 62: value: |
| `er/csi-ehr-er-ui` | Commented out line 63: name: CSI_MODULE_NAME |
| `er/csi-ehr-er-ui` | Commented out line 64: value: "ehrerui" |
| `er/csi-ehr-er-ui` | Commented out line 65: - op: add |
| `er/csi-ehr-er-ui` | Commented out line 66: path: /spec/template/spec/containers/0/env/- |
| `er/csi-ehr-er-ui` | Commented out line 67: value: |
| `er/csi-ehr-er-ui` | Commented out line 68: name: CSI_PARENT_MODULE_NAME |
| `er/csi-ehr-er-ui` | Commented out line 69: value: "er" |
| `hhc/hhc-service` | Replaced Sync reference with DM-Initiator |
| `hhc/hhc-ui` | Replaced Sync reference with DM-Initiator |
| `him/csi-health-information-srv` | Replaced Sync reference with DM-Initiator |
| `him/csi-health-information-srv` | Added new sync-presync/sync-postsync Job patches |
| `him/csi-health-information-srv` | Commented out line 20: - target: |
| `him/csi-health-information-srv` | Commented out line 21: group: batch |
| `him/csi-health-information-srv` | Commented out line 22: version: v1 |
| `him/csi-health-information-srv` | Commented out line 23: kind: Job |
| `him/csi-health-information-srv` | Commented out line 24: name: .* |
| `him/csi-health-information-srv` | Commented out line 25: patch: |- |
| `him/csi-health-information-srv` | Commented out line 26: - op: replace |
| `him/csi-health-information-srv` | Commented out line 27: path: /metadata/name |
| `him/csi-health-information-srv` | Commented out line 28: value: before-csi-net-himservi |
| `him/csi-health-information-srv` | Commented out line 29: - op: add |
| `him/csi-health-information-srv` | Commented out line 30: path: /spec/template/spec/containers/0/env/- |
| `him/csi-health-information-srv` | Commented out line 31: value: |
| `him/csi-health-information-srv` | Commented out line 32: name: CSI_MODULENAME |
| `him/csi-health-information-srv` | Commented out line 33: value: "csi-health-information-srv" |
| `him/csi-health-information-srv` | Commented out line 34: - op: add |
| `him/csi-health-information-srv` | Commented out line 35: path: /spec/template/spec/containers/0/env/- |
| `him/csi-health-information-srv` | Commented out line 36: value: |
| `him/csi-health-information-srv` | Commented out line 37: name: CSI_DATA_VERSION |
| `him/csi-health-information-srv` | Commented out line 38: value: "4.1.28.20" |
| `him/csi-health-information-srv` | Commented out line 39: - op: add |
| `him/csi-health-information-srv` | Commented out line 40: path: /spec/template/spec/containers/0/env/- |
| `him/csi-health-information-srv` | Commented out line 41: value: |
| `him/csi-health-information-srv` | Commented out line 42: name: CSI_PROJECT_NAME |
| `him/csi-health-information-srv` | Commented out line 43: value: "csi-health-information-srv" |
| `him/csi-health-information-srv` | Commented out line 44: - op: add |
| `him/csi-health-information-srv` | Commented out line 45: path: /spec/template/spec/containers/0/env/- |
| `him/csi-health-information-srv` | Commented out line 46: value: |
| `him/csi-health-information-srv` | Commented out line 47: name: CSI_MODULE_NAME |
| `him/csi-health-information-srv` | Commented out line 48: value: "csinethimservi" |
| `him/csi-health-information-srv` | Commented out line 49: - op: add |
| `him/csi-health-information-srv` | Commented out line 50: path: /spec/template/spec/containers/0/env/- |
| `him/csi-health-information-srv` | Commented out line 51: value: |
| `him/csi-health-information-srv` | Commented out line 52: name: CSI_PARENT_MODULE_NAME |
| `him/csi-health-information-srv` | Commented out line 53: value: "him" |
| `him/csi-him-ui` | Replaced commented Sync reference with commented DM-Initiator |
| `him/csi-him-ui` | Added new sync-presync/sync-postsync Job patches |
| `him/csi-him-ui` | Commented out line 21: - target: |
| `him/csi-him-ui` | Commented out line 22: group: batch |
| `him/csi-him-ui` | Commented out line 23: version: v1 |
| `him/csi-him-ui` | Commented out line 24: kind: Job |
| `him/csi-him-ui` | Commented out line 25: name: .* |
| `him/csi-him-ui` | Commented out line 26: patch: |- |
| `him/csi-him-ui` | Commented out line 27: - op: replace |
| `him/csi-him-ui` | Commented out line 28: path: /metadata/name |
| `him/csi-him-ui` | Commented out line 29: value: before-csi-him-ui |
| `him/csi-him-ui` | Commented out line 30: namespace: moh-uat |
| `him/csi-him-ui` | Commented out line 31: - op: add |
| `him/csi-him-ui` | Commented out line 32: path: /spec/template/spec/containers/0/env/- |
| `him/csi-him-ui` | Commented out line 33: value: |
| `him/csi-him-ui` | Commented out line 34: name: CSI_MODULENAME |
| `him/csi-him-ui` | Commented out line 35: value: "csi-him-ui" |
| `him/csi-him-ui` | Commented out line 36: - op: add |
| `him/csi-him-ui` | Commented out line 37: path: /spec/template/spec/containers/0/env/- |
| `him/csi-him-ui` | Commented out line 38: value: |
| `him/csi-him-ui` | Commented out line 39: name: CSI_DATA_VERSION |
| `him/csi-him-ui` | Commented out line 40: value: "4.3.234.0" |
| `him/csi-him-ui` | Commented out line 41: - op: add |
| `him/csi-him-ui` | Commented out line 42: path: /spec/template/spec/containers/0/env/- |
| `him/csi-him-ui` | Commented out line 43: value: |
| `him/csi-him-ui` | Commented out line 44: name: CSI_PROJECT_NAME |
| `him/csi-him-ui` | Commented out line 45: value: "csi-him-ui" |
| `him/csi-him-ui` | Commented out line 46: - op: add |
| `him/csi-him-ui` | Commented out line 47: path: /spec/template/spec/containers/0/env/- |
| `him/csi-him-ui` | Commented out line 48: value: |
| `him/csi-him-ui` | Commented out line 49: name: CSI_MODULE_NAME |
| `him/csi-him-ui` | Commented out line 50: value: "csi-him-ui" |
| `him/csi-him-ui` | Commented out line 51: - op: add |
| `him/csi-him-ui` | Commented out line 52: path: /spec/template/spec/containers/0/env/- |
| `him/csi-him-ui` | Commented out line 53: value: |
| `him/csi-him-ui` | Commented out line 54: name: CSI_PARENT_MODULE_NAME |
| `him/csi-him-ui` | Commented out line 55: value: "him" |
| `integration/csi-ie-general` | Replaced Sync reference with DM-Initiator |
| `integration/csi-ie-general` | Removed extra Sync reference: - ../../../Sync-DM/ |
| `integration/csi-ie-general` | Added new sync-presync/sync-postsync Job patches |
| `integration/csi-ie-general` | Commented out line 20: - target: |
| `integration/csi-ie-general` | Commented out line 21: group: batch |
| `integration/csi-ie-general` | Commented out line 22: version: v1 |
| `integration/csi-ie-general` | Commented out line 23: kind: Job |
| `integration/csi-ie-general` | Commented out line 24: name: before |
| `integration/csi-ie-general` | Commented out line 25: patch: | |
| `integration/csi-ie-general` | Commented out line 26: - op: replace |
| `integration/csi-ie-general` | Commented out line 27: path: /metadata/name |
| `integration/csi-ie-general` | Commented out line 28: value: before-csi-ie-general |
| `integration/csi-ie-general` | Commented out line 29: - op: add |
| `integration/csi-ie-general` | Commented out line 30: path: /spec/template/spec/containers/0/env/- |
| `integration/csi-ie-general` | Commented out line 31: value: |
| `integration/csi-ie-general` | Commented out line 32: name: CSI_MODULENAME |
| `integration/csi-ie-general` | Commented out line 33: value: "csi-ie-general" |
| `integration/csi-ie-general` | Commented out line 34: - op: add |
| `integration/csi-ie-general` | Commented out line 35: path: /spec/template/spec/containers/0/env/- |
| `integration/csi-ie-general` | Commented out line 36: value: |
| `integration/csi-ie-general` | Commented out line 37: name: CSI_DATA_VERSION |
| `integration/csi-ie-general` | Commented out line 38: value: "4.2.502.0" |
| `integration/csi-ie-general` | Commented out line 39: - op: add |
| `integration/csi-ie-general` | Commented out line 40: path: /spec/template/spec/containers/0/env/- |
| `integration/csi-ie-general` | Commented out line 41: value: |
| `integration/csi-ie-general` | Commented out line 42: name: CSI_PROJECT_NAME |
| `integration/csi-ie-general` | Commented out line 43: value: "csi-ie-general" |
| `integration/csi-ie-general` | Commented out line 44: - op: add |
| `integration/csi-ie-general` | Commented out line 45: path: /spec/template/spec/containers/0/env/- |
| `integration/csi-ie-general` | Commented out line 46: value: |
| `integration/csi-ie-general` | Commented out line 47: name: CSI_MODULE_NAME |
| `integration/csi-ie-general` | Commented out line 48: value: "csiiegeneral" |
| `integration/csi-ie-general` | Commented out line 49: - op: add |
| `integration/csi-ie-general` | Commented out line 50: path: /spec/template/spec/containers/0/env/- |
| `integration/csi-ie-general` | Commented out line 51: value: |
| `integration/csi-ie-general` | Commented out line 52: name: CSI_PARENT_MODULE_NAME |
| `integration/csi-ie-general` | Commented out line 53: value: "integration" |
| `integration/csi-ie-general` | Commented out line 79: - target: |
| `integration/csi-ie-general` | Commented out line 80: group: batch |
| `integration/csi-ie-general` | Commented out line 81: version: v1 |
| `integration/csi-ie-general` | Commented out line 82: kind: Job |
| `integration/csi-ie-general` | Commented out line 83: name: data-migration-presync |
| `integration/csi-ie-general` | Commented out line 84: patch: |- |
| `integration/csi-ie-general` | Commented out line 85: - op: replace |
| `integration/csi-ie-general` | Commented out line 86: path: /metadata/name |
| `integration/csi-ie-general` | Commented out line 87: value: data-migration-presync-ie-general |
| `integration/csi-ie-general` | Commented out line 88: - op: add |
| `integration/csi-ie-general` | Commented out line 89: path: /spec/template/spec/containers/0/env/- |
| `integration/csi-ie-general` | Commented out line 90: value: |
| `integration/csi-ie-general` | Commented out line 91: name: CSI_DATA_VERSION |
| `integration/csi-ie-general` | Commented out line 92: value: "4.2.502.0" |
| `integration/csi-ie-general` | Commented out line 93: - op: add |
| `integration/csi-ie-general` | Commented out line 94: path: /spec/template/spec/containers/0/env/- |
| `integration/csi-ie-general` | Commented out line 95: value: |
| `integration/csi-ie-general` | Commented out line 96: name: CSI_PROJECT_NAME |
| `integration/csi-ie-general` | Commented out line 97: value: "csi-ie-general" |
| `integration/csi-ie-general` | Commented out line 98: - op: add |
| `integration/csi-ie-general` | Commented out line 99: path: /spec/template/spec/containers/0/env/- |
| `integration/csi-ie-general` | Commented out line 100: value: |
| `integration/csi-ie-general` | Commented out line 101: name: CSI_MODULE_NAME |
| `integration/csi-ie-general` | Commented out line 102: value: "csiiegeneral" |
| `integration/csi-ie-general` | Commented out line 103: - op: add |
| `integration/csi-ie-general` | Commented out line 104: path: /spec/template/spec/containers/0/env/- |
| `integration/csi-ie-general` | Commented out line 105: value: |
| `integration/csi-ie-general` | Commented out line 106: name: CSI_PARENT_MODULE_NAME |
| `integration/csi-ie-general` | Commented out line 107: value: "integration" |
| `integration/csi-ie-general` | Commented out line 109: - target: |
| `integration/csi-ie-general` | Commented out line 110: group: batch |
| `integration/csi-ie-general` | Commented out line 111: version: v1 |
| `integration/csi-ie-general` | Commented out line 112: kind: Job |
| `integration/csi-ie-general` | Commented out line 113: name: data-migration-postsync |
| `integration/csi-ie-general` | Commented out line 114: patch: |- |
| `integration/csi-ie-general` | Commented out line 115: - op: replace |
| `integration/csi-ie-general` | Commented out line 116: path: /metadata/name |
| `integration/csi-ie-general` | Commented out line 117: value: data-migration-postsync-ie-general |
| `integration/csi-ie-general` | Commented out line 118: - op: add |
| `integration/csi-ie-general` | Commented out line 119: path: /spec/template/spec/containers/0/env/- |
| `integration/csi-ie-general` | Commented out line 120: value: |
| `integration/csi-ie-general` | Commented out line 121: name: CSI_DATA_VERSION |
| `integration/csi-ie-general` | Commented out line 122: value: "4.2.502.0" |
| `integration/csi-ie-general` | Commented out line 123: - op: add |
| `integration/csi-ie-general` | Commented out line 124: path: /spec/template/spec/containers/0/env/- |
| `integration/csi-ie-general` | Commented out line 125: value: |
| `integration/csi-ie-general` | Commented out line 126: name: CSI_PROJECT_NAME |
| `integration/csi-ie-general` | Commented out line 127: value: "csi-ie-general" |
| `integration/csi-ie-general` | Commented out line 128: - op: add |
| `integration/csi-ie-general` | Commented out line 129: path: /spec/template/spec/containers/0/env/- |
| `integration/csi-ie-general` | Commented out line 130: value: |
| `integration/csi-ie-general` | Commented out line 131: name: CSI_MODULE_NAME |
| `integration/csi-ie-general` | Commented out line 132: value: "csiiegeneral" |
| `integration/csi-ie-general` | Commented out line 133: - op: add |
| `integration/csi-ie-general` | Commented out line 134: path: /spec/template/spec/containers/0/env/- |
| `integration/csi-ie-general` | Commented out line 135: value: |
| `integration/csi-ie-general` | Commented out line 136: name: CSI_PARENT_MODULE_NAME |
| `integration/csi-ie-general` | Commented out line 137: value: "integration" |
| `integration/csi-ie-mobile` | Replaced Sync reference with DM-Initiator |
| `integration/csi-ie-mobile` | Added new sync-presync/sync-postsync Job patches |
| `integration/csi-ie-mobile` | Commented out line 19: - target: |
| `integration/csi-ie-mobile` | Commented out line 20: group: batch |
| `integration/csi-ie-mobile` | Commented out line 21: version: v1 |
| `integration/csi-ie-mobile` | Commented out line 22: kind: Job |
| `integration/csi-ie-mobile` | Commented out line 23: name: before |
| `integration/csi-ie-mobile` | Commented out line 24: patch: |- |
| `integration/csi-ie-mobile` | Commented out line 25: - op: replace |
| `integration/csi-ie-mobile` | Commented out line 26: path: /metadata/name |
| `integration/csi-ie-mobile` | Commented out line 27: value: before-csi-ie-mobile |
| `integration/csi-ie-mobile` | Commented out line 28: - op: add |
| `integration/csi-ie-mobile` | Commented out line 29: path: /spec/template/spec/containers/0/env/- |
| `integration/csi-ie-mobile` | Commented out line 30: value: |
| `integration/csi-ie-mobile` | Commented out line 31: name: CSI_MODULENAME |
| `integration/csi-ie-mobile` | Commented out line 32: value: "csi-ie-mobile" |
| `integration/csi-ie-mobile` | Commented out line 33: - op: add |
| `integration/csi-ie-mobile` | Commented out line 34: path: /spec/template/spec/containers/0/env/- |
| `integration/csi-ie-mobile` | Commented out line 35: value: |
| `integration/csi-ie-mobile` | Commented out line 36: name: CSI_DATA_VERSION |
| `integration/csi-ie-mobile` | Commented out line 37: value: "4.2.502.0" |
| `integration/csi-ie-mobile` | Commented out line 38: - op: add |
| `integration/csi-ie-mobile` | Commented out line 39: path: /spec/template/spec/containers/0/env/- |
| `integration/csi-ie-mobile` | Commented out line 40: value: |
| `integration/csi-ie-mobile` | Commented out line 41: name: CSI_PROJECT_NAME |
| `integration/csi-ie-mobile` | Commented out line 42: value: "csi-ie-mobile" |
| `integration/csi-ie-mobile` | Commented out line 43: - op: add |
| `integration/csi-ie-mobile` | Commented out line 44: path: /spec/template/spec/containers/0/env/- |
| `integration/csi-ie-mobile` | Commented out line 45: value: |
| `integration/csi-ie-mobile` | Commented out line 46: name: CSI_MODULE_NAME |
| `integration/csi-ie-mobile` | Commented out line 47: value: "csiiemobile" |
| `integration/csi-ie-mobile` | Commented out line 48: - op: add |
| `integration/csi-ie-mobile` | Commented out line 49: path: /spec/template/spec/containers/0/env/- |
| `integration/csi-ie-mobile` | Commented out line 50: value: |
| `integration/csi-ie-mobile` | Commented out line 51: name: CSI_PARENT_MODULE_NAME |
| `integration/csi-ie-mobile` | Commented out line 52: value: "integration" |
| `integration/csiiemobile-v2` | Replaced Sync reference with DM-Initiator |
| `integration/csiiemobile-v2` | Added new sync-presync/sync-postsync Job patches |
| `integration/csiiemobile-v2` | Commented out line 19: - target: |
| `integration/csiiemobile-v2` | Commented out line 20: group: batch |
| `integration/csiiemobile-v2` | Commented out line 21: version: v1 |
| `integration/csiiemobile-v2` | Commented out line 22: kind: Job |
| `integration/csiiemobile-v2` | Commented out line 23: name: before |
| `integration/csiiemobile-v2` | Commented out line 24: patch: |- |
| `integration/csiiemobile-v2` | Commented out line 25: - op: replace |
| `integration/csiiemobile-v2` | Commented out line 26: path: /metadata/name |
| `integration/csiiemobile-v2` | Commented out line 27: value: before-csi-ie-mobile-v2 |
| `integration/csiiemobile-v2` | Commented out line 28: - op: add |
| `integration/csiiemobile-v2` | Commented out line 29: path: /spec/template/spec/containers/0/env/- |
| `integration/csiiemobile-v2` | Commented out line 30: value: |
| `integration/csiiemobile-v2` | Commented out line 31: name: CSI_MODULENAME |
| `integration/csiiemobile-v2` | Commented out line 32: value: "csi-ie-mobile" |
| `integration/csiiemobile-v2` | Commented out line 33: - op: add |
| `integration/csiiemobile-v2` | Commented out line 34: path: /spec/template/spec/containers/0/env/- |
| `integration/csiiemobile-v2` | Commented out line 35: value: |
| `integration/csiiemobile-v2` | Commented out line 36: name: CSI_DATA_VERSION |
| `integration/csiiemobile-v2` | Commented out line 37: value: "4.2.502.0" |
| `integration/csiiemobile-v2` | Commented out line 38: - op: add |
| `integration/csiiemobile-v2` | Commented out line 39: path: /spec/template/spec/containers/0/env/- |
| `integration/csiiemobile-v2` | Commented out line 40: value: |
| `integration/csiiemobile-v2` | Commented out line 41: name: CSI_PROJECT_NAME |
| `integration/csiiemobile-v2` | Commented out line 42: value: "csi-ie-mobile" |
| `integration/csiiemobile-v2` | Commented out line 43: - op: add |
| `integration/csiiemobile-v2` | Commented out line 44: path: /spec/template/spec/containers/0/env/- |
| `integration/csiiemobile-v2` | Commented out line 45: value: |
| `integration/csiiemobile-v2` | Commented out line 46: name: CSI_MODULE_NAME |
| `integration/csiiemobile-v2` | Commented out line 47: value: "csiiemobile-v2" |
| `integration/csiiemobile-v2` | Commented out line 48: - op: add |
| `integration/csiiemobile-v2` | Commented out line 49: path: /spec/template/spec/containers/0/env/- |
| `integration/csiiemobile-v2` | Commented out line 50: value: |
| `integration/csiiemobile-v2` | Commented out line 51: name: CSI_PARENT_MODULE_NAME |
| `integration/csiiemobile-v2` | Commented out line 52: value: "integration" |
| `lab/lab-labgui` | Replaced Sync reference with DM-Initiator |
| `lab/lab-labgui` | Added new sync-presync/sync-postsync Job patches |
| `lab/lab-labgui` | Commented out line 20: - target: |
| `lab/lab-labgui` | Commented out line 21: group: batch |
| `lab/lab-labgui` | Commented out line 22: version: v1 |
| `lab/lab-labgui` | Commented out line 23: kind: Job |
| `lab/lab-labgui` | Commented out line 24: name: .* |
| `lab/lab-labgui` | Commented out line 25: patch: |- |
| `lab/lab-labgui` | Commented out line 26: - op: replace |
| `lab/lab-labgui` | Commented out line 27: path: /metadata/name |
| `lab/lab-labgui` | Commented out line 28: value: before-labui |
| `lab/lab-labgui` | Commented out line 29: - op: add |
| `lab/lab-labgui` | Commented out line 30: path: /spec/template/spec/containers/0/env/- |
| `lab/lab-labgui` | Commented out line 31: value: |
| `lab/lab-labgui` | Commented out line 32: name: CSI_MODULENAME |
| `lab/lab-labgui` | Commented out line 33: value: "lab-labgui" |
| `lab/lab-labgui` | Commented out line 34: - op: add |
| `lab/lab-labgui` | Commented out line 35: path: /spec/template/spec/containers/0/env/- |
| `lab/lab-labgui` | Commented out line 36: value: |
| `lab/lab-labgui` | Commented out line 37: name: CSI_DATA_VERSION |
| `lab/lab-labgui` | Commented out line 38: value: "4.0.127.0" |
| `lab/lab-labgui` | Commented out line 39: - op: add |
| `lab/lab-labgui` | Commented out line 40: path: /spec/template/spec/containers/0/env/- |
| `lab/lab-labgui` | Commented out line 41: value: |
| `lab/lab-labgui` | Commented out line 42: name: CSI_PROJECT_NAME |
| `lab/lab-labgui` | Commented out line 43: value: "lab-labgui" |
| `lab/lab-labgui` | Commented out line 44: - op: add |
| `lab/lab-labgui` | Commented out line 45: path: /spec/template/spec/containers/0/env/- |
| `lab/lab-labgui` | Commented out line 46: value: |
| `lab/lab-labgui` | Commented out line 47: name: CSI_MODULE_NAME |
| `lab/lab-labgui` | Commented out line 48: value: "labui" |
| `lab/lab-labgui` | Commented out line 49: - op: add |
| `lab/lab-labgui` | Commented out line 50: path: /spec/template/spec/containers/0/env/- |
| `lab/lab-labgui` | Commented out line 51: value: |
| `lab/lab-labgui` | Commented out line 52: name: CSI_PARENT_MODULE_NAME |
| `lab/lab-labgui` | Commented out line 53: value: "lab" |
| `lab/lab-labmgt-srv` | Replaced Sync reference with DM-Initiator |
| `lab/lab-labmgt-srv` | Removed extra Sync reference: - ../../../Sync-DM/ |
| `lab/lab-labmgt-srv` | Added new sync-presync/sync-postsync Job patches |
| `lab/lab-labmgt-srv` | Commented out line 25: - target: |
| `lab/lab-labmgt-srv` | Commented out line 26: group: batch |
| `lab/lab-labmgt-srv` | Commented out line 27: version: v1 |
| `lab/lab-labmgt-srv` | Commented out line 28: kind: Job |
| `lab/lab-labmgt-srv` | Commented out line 29: name: before |
| `lab/lab-labmgt-srv` | Commented out line 30: patch: |- |
| `lab/lab-labmgt-srv` | Commented out line 31: - op: replace |
| `lab/lab-labmgt-srv` | Commented out line 32: path: /metadata/name |
| `lab/lab-labmgt-srv` | Commented out line 33: value: before-labmgmtdotnet |
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
| `lab/lab-labmgt-srv` | Commented out line 53: value: "labmgmtdotnet" |
| `lab/lab-labmgt-srv` | Commented out line 54: - op: add |
| `lab/lab-labmgt-srv` | Commented out line 55: path: /spec/template/spec/containers/0/env/- |
| `lab/lab-labmgt-srv` | Commented out line 56: value: |
| `lab/lab-labmgt-srv` | Commented out line 57: name: CSI_PARENT_MODULE_NAME |
| `lab/lab-labmgt-srv` | Commented out line 58: value: "lab" |
| `lab/lab-labmgt-srv` | Commented out line 60: - target: |
| `lab/lab-labmgt-srv` | Commented out line 61: group: batch |
| `lab/lab-labmgt-srv` | Commented out line 62: version: v1 |
| `lab/lab-labmgt-srv` | Commented out line 63: kind: Job |
| `lab/lab-labmgt-srv` | Commented out line 64: name: data-migration-presync |
| `lab/lab-labmgt-srv` | Commented out line 65: patch: |- |
| `lab/lab-labmgt-srv` | Commented out line 66: - op: replace |
| `lab/lab-labmgt-srv` | Commented out line 67: path: /metadata/name |
| `lab/lab-labmgt-srv` | Commented out line 68: value: data-migration-presync-labmgmtdotnet |
| `lab/lab-labmgt-srv` | Commented out line 69: - op: add |
| `lab/lab-labmgt-srv` | Commented out line 70: path: /spec/template/spec/containers/0/env/- |
| `lab/lab-labmgt-srv` | Commented out line 71: value: |
| `lab/lab-labmgt-srv` | Commented out line 72: name: CSI_MODULENAME |
| `lab/lab-labmgt-srv` | Commented out line 73: value: "lab-labmgt_srv" |
| `lab/lab-labmgt-srv` | Commented out line 74: - op: add |
| `lab/lab-labmgt-srv` | Commented out line 75: path: /spec/template/spec/containers/0/env/- |
| `lab/lab-labmgt-srv` | Commented out line 76: value: |
| `lab/lab-labmgt-srv` | Commented out line 77: name: CSI_DATA_VERSION |
| `lab/lab-labmgt-srv` | Commented out line 78: value: "4.1.28.20" |
| `lab/lab-labmgt-srv` | Commented out line 79: - op: add |
| `lab/lab-labmgt-srv` | Commented out line 80: path: /spec/template/spec/containers/0/env/- |
| `lab/lab-labmgt-srv` | Commented out line 81: value: |
| `lab/lab-labmgt-srv` | Commented out line 82: name: CSI_PROJECT_NAME |
| `lab/lab-labmgt-srv` | Commented out line 83: value: "lab-labmgt_srv" |
| `lab/lab-labmgt-srv` | Commented out line 84: - op: add |
| `lab/lab-labmgt-srv` | Commented out line 85: path: /spec/template/spec/containers/0/env/- |
| `lab/lab-labmgt-srv` | Commented out line 86: value: |
| `lab/lab-labmgt-srv` | Commented out line 87: name: CSI_MODULE_NAME |
| `lab/lab-labmgt-srv` | Commented out line 88: value: "labmgmtdotnet" |
| `lab/lab-labmgt-srv` | Commented out line 89: - op: add |
| `lab/lab-labmgt-srv` | Commented out line 90: path: /spec/template/spec/containers/0/env/- |
| `lab/lab-labmgt-srv` | Commented out line 91: value: |
| `lab/lab-labmgt-srv` | Commented out line 92: name: CSI_PARENT_MODULE_NAME |
| `lab/lab-labmgt-srv` | Commented out line 93: value: "lab" |
| `lab/lab-labmgt-srv` | Commented out line 95: - target: |
| `lab/lab-labmgt-srv` | Commented out line 96: group: batch |
| `lab/lab-labmgt-srv` | Commented out line 97: version: v1 |
| `lab/lab-labmgt-srv` | Commented out line 98: kind: Job |
| `lab/lab-labmgt-srv` | Commented out line 99: name: data-migration-postsync |
| `lab/lab-labmgt-srv` | Commented out line 100: patch: |- |
| `lab/lab-labmgt-srv` | Commented out line 101: - op: replace |
| `lab/lab-labmgt-srv` | Commented out line 102: path: /metadata/name |
| `lab/lab-labmgt-srv` | Commented out line 103: value: data-migration-postsync-labmgmtdotnet |
| `lab/lab-labmgt-srv` | Commented out line 104: - op: add |
| `lab/lab-labmgt-srv` | Commented out line 105: path: /spec/template/spec/containers/0/env/- |
| `lab/lab-labmgt-srv` | Commented out line 106: value: |
| `lab/lab-labmgt-srv` | Commented out line 107: name: CSI_MODULENAME |
| `lab/lab-labmgt-srv` | Commented out line 108: value: "lab-labmgt_srv" |
| `lab/lab-labmgt-srv` | Commented out line 109: - op: add |
| `lab/lab-labmgt-srv` | Commented out line 110: path: /spec/template/spec/containers/0/env/- |
| `lab/lab-labmgt-srv` | Commented out line 111: value: |
| `lab/lab-labmgt-srv` | Commented out line 112: name: CSI_DATA_VERSION |
| `lab/lab-labmgt-srv` | Commented out line 113: value: "4.1.28.20" |
| `lab/lab-labmgt-srv` | Commented out line 114: - op: add |
| `lab/lab-labmgt-srv` | Commented out line 115: path: /spec/template/spec/containers/0/env/- |
| `lab/lab-labmgt-srv` | Commented out line 116: value: |
| `lab/lab-labmgt-srv` | Commented out line 117: name: CSI_PROJECT_NAME |
| `lab/lab-labmgt-srv` | Commented out line 118: value: "lab-labmgt_srv" |
| `lab/lab-labmgt-srv` | Commented out line 119: - op: add |
| `lab/lab-labmgt-srv` | Commented out line 120: path: /spec/template/spec/containers/0/env/- |
| `lab/lab-labmgt-srv` | Commented out line 121: value: |
| `lab/lab-labmgt-srv` | Commented out line 122: name: CSI_MODULE_NAME |
| `lab/lab-labmgt-srv` | Commented out line 123: value: "labmgmtdotnet" |
| `lab/lab-labmgt-srv` | Commented out line 124: - op: add |
| `lab/lab-labmgt-srv` | Commented out line 125: path: /spec/template/spec/containers/0/env/- |
| `lab/lab-labmgt-srv` | Commented out line 126: value: |
| `lab/lab-labmgt-srv` | Commented out line 127: name: CSI_PARENT_MODULE_NAME |
| `lab/lab-labmgt-srv` | Commented out line 128: value: "lab" |
| `notification/csi-net-base-sms` | Replaced commented Sync reference with commented DM-Initiator |
| `notification/csi-net-base-sms` | Added new sync-presync/sync-postsync Job patches |
| `notification/csi-net-base-sms` | Commented out line 19: - target: |
| `notification/csi-net-base-sms` | Commented out line 20: group: batch |
| `notification/csi-net-base-sms` | Commented out line 21: version: v1 |
| `notification/csi-net-base-sms` | Commented out line 22: kind: Job |
| `notification/csi-net-base-sms` | Commented out line 23: name: .* |
| `notification/csi-net-base-sms` | Commented out line 24: patch: |- |
| `notification/csi-net-base-sms` | Commented out line 25: - op: replace |
| `notification/csi-net-base-sms` | Commented out line 26: path: /metadata/name |
| `notification/csi-net-base-sms` | Commented out line 27: value: before-notynetbasesms |
| `notification/csi-net-base-sms` | Commented out line 28: - op: add |
| `notification/csi-net-base-sms` | Commented out line 29: path: /spec/template/spec/containers/0/env/- |
| `notification/csi-net-base-sms` | Commented out line 30: value: |
| `notification/csi-net-base-sms` | Commented out line 31: name: CSI_MODULENAME |
| `notification/csi-net-base-sms` | Commented out line 32: value: "csi-net-base-sms" |
| `notification/csi-net-base-sms` | Commented out line 33: - op: add |
| `notification/csi-net-base-sms` | Commented out line 34: path: /spec/template/spec/containers/0/env/- |
| `notification/csi-net-base-sms` | Commented out line 35: value: |
| `notification/csi-net-base-sms` | Commented out line 36: name: CSI_DATA_VERSION |
| `notification/csi-net-base-sms` | Commented out line 37: value: "4.3.234.0" |
| `notification/csi-net-base-sms` | Commented out line 38: - op: add |
| `notification/csi-net-base-sms` | Commented out line 39: path: /spec/template/spec/containers/0/env/- |
| `notification/csi-net-base-sms` | Commented out line 40: value: |
| `notification/csi-net-base-sms` | Commented out line 41: name: CSI_PROJECT_NAME |
| `notification/csi-net-base-sms` | Commented out line 42: value: "csi-net-base-sms" |
| `notification/csi-net-base-sms` | Commented out line 43: - op: add |
| `notification/csi-net-base-sms` | Commented out line 44: path: /spec/template/spec/containers/0/env/- |
| `notification/csi-net-base-sms` | Commented out line 45: value: |
| `notification/csi-net-base-sms` | Commented out line 46: name: CSI_MODULE_NAME |
| `notification/csi-net-base-sms` | Commented out line 47: value: "notynetbasesms" |
| `notification/csi-net-base-sms` | Commented out line 48: - op: add |
| `notification/csi-net-base-sms` | Commented out line 49: path: /spec/template/spec/containers/0/env/- |
| `notification/csi-net-base-sms` | Commented out line 50: value: |
| `notification/csi-net-base-sms` | Commented out line 51: name: CSI_PARENT_MODULE_NAME |
| `notification/csi-net-base-sms` | Commented out line 52: value: "notification" |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Replaced Sync reference with DM-Initiator |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Added new sync-presync/sync-postsync Job patches |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 21: - target: |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 22: group: batch |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 23: version: v1 |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 24: kind: Job |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 25: name: .* |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 26: patch: |- |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 27: - op: replace |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 28: path: /metadata/name |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 29: value: before-ehripprescriptionjava |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 30: - op: add |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 31: path: /spec/template/spec/containers/0/env/- |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 32: value: |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 33: name: CSI_MODULENAME |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 34: value: "csi-java-ehr-ip-doctor-prescription" |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 35: - op: add |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 36: path: /spec/template/spec/containers/0/env/- |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 37: value: |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 38: name: CSI_DATA_VERSION |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 39: value: "4.0.127.0" |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 40: - op: add |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 41: path: /spec/template/spec/containers/0/env/- |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 42: value: |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 43: name: CSI_PROJECT_NAME |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 44: value: "csi-java-ehr-ip-doctor-prescription" |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 45: - op: add |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 46: path: /spec/template/spec/containers/0/env/- |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 47: value: |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 48: name: CSI_MODULE_NAME |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 49: value: "ehripprescriptionjava" |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 50: - op: add |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 51: path: /spec/template/spec/containers/0/env/- |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 52: value: |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 53: name: CSI_PARENT_MODULE_NAME |
| `pharmacy/csi-java-ehr-ip-doctor-prescription` | Commented out line 54: value: "pharmacy" |
| `pharmacy/csi-phr-base` | Replaced Sync reference with DM-Initiator |
| `pharmacy/csi-phr-base` | Added new sync-presync/sync-postsync Job patches |
| `pharmacy/csi-phr-base` | Commented out line 19: - target: |
| `pharmacy/csi-phr-base` | Commented out line 20: group: batch |
| `pharmacy/csi-phr-base` | Commented out line 21: version: v1 |
| `pharmacy/csi-phr-base` | Commented out line 22: kind: Job |
| `pharmacy/csi-phr-base` | Commented out line 23: name: .* |
| `pharmacy/csi-phr-base` | Commented out line 24: patch: | |
| `pharmacy/csi-phr-base` | Commented out line 25: - op: replace |
| `pharmacy/csi-phr-base` | Commented out line 26: path: /metadata/name |
| `pharmacy/csi-phr-base` | Commented out line 27: value: before-phrbasejava |
| `pharmacy/csi-phr-base` | Commented out line 28: - op: add |
| `pharmacy/csi-phr-base` | Commented out line 29: path: /spec/template/spec/containers/0/env/- |
| `pharmacy/csi-phr-base` | Commented out line 30: value: |
| `pharmacy/csi-phr-base` | Commented out line 31: name: CSI_MODULENAME |
| `pharmacy/csi-phr-base` | Commented out line 32: value: "csi-phr-base" |
| `pharmacy/csi-phr-base` | Commented out line 33: - op: add |
| `pharmacy/csi-phr-base` | Commented out line 34: path: /spec/template/spec/containers/0/env/- |
| `pharmacy/csi-phr-base` | Commented out line 35: value: |
| `pharmacy/csi-phr-base` | Commented out line 36: name: CSI_DATA_VERSION |
| `pharmacy/csi-phr-base` | Commented out line 37: value: "4.2.15.0" |
| `pharmacy/csi-phr-base` | Commented out line 38: - op: add |
| `pharmacy/csi-phr-base` | Commented out line 39: path: /spec/template/spec/containers/0/env/- |
| `pharmacy/csi-phr-base` | Commented out line 40: value: |
| `pharmacy/csi-phr-base` | Commented out line 41: name: CSI_PROJECT_NAME |
| `pharmacy/csi-phr-base` | Commented out line 42: value: "csi-phr-base" |
| `pharmacy/csi-phr-base` | Commented out line 43: - op: add |
| `pharmacy/csi-phr-base` | Commented out line 44: path: /spec/template/spec/containers/0/env/- |
| `pharmacy/csi-phr-base` | Commented out line 45: value: |
| `pharmacy/csi-phr-base` | Commented out line 46: name: CSI_MODULE_NAME |
| `pharmacy/csi-phr-base` | Commented out line 47: value: "phrbasejava" |
| `pharmacy/csi-phr-base` | Commented out line 48: - op: add |
| `pharmacy/csi-phr-base` | Commented out line 49: path: /spec/template/spec/containers/0/env/- |
| `pharmacy/csi-phr-base` | Commented out line 50: value: |
| `pharmacy/csi-phr-base` | Commented out line 51: name: CSI_PARENT_MODULE_NAME |
| `pharmacy/csi-phr-base` | Commented out line 52: value: "pharmacy" |
| `pharmacy/phr-pharmacygui` | Replaced Sync reference with DM-Initiator |
| `pharmacy/phr-pharmacygui` | Added new sync-presync/sync-postsync Job patches |
| `pharmacy/phr-pharmacygui` | Commented out line 29: - target: |
| `pharmacy/phr-pharmacygui` | Commented out line 30: group: batch |
| `pharmacy/phr-pharmacygui` | Commented out line 31: version: v1 |
| `pharmacy/phr-pharmacygui` | Commented out line 32: kind: Job |
| `pharmacy/phr-pharmacygui` | Commented out line 33: name: .* |
| `pharmacy/phr-pharmacygui` | Commented out line 34: patch: |- |
| `pharmacy/phr-pharmacygui` | Commented out line 35: - op: replace |
| `pharmacy/phr-pharmacygui` | Commented out line 36: path: /metadata/name |
| `pharmacy/phr-pharmacygui` | Commented out line 37: value: before-pharmacyui |
| `pharmacy/phr-pharmacygui` | Commented out line 38: - op: add |
| `pharmacy/phr-pharmacygui` | Commented out line 39: path: /spec/template/spec/containers/0/env/- |
| `pharmacy/phr-pharmacygui` | Commented out line 40: value: |
| `pharmacy/phr-pharmacygui` | Commented out line 41: name: CSI_MODULENAME |
| `pharmacy/phr-pharmacygui` | Commented out line 42: value: "phr-pharmacygui" |
| `pharmacy/phr-pharmacygui` | Commented out line 43: - op: add |
| `pharmacy/phr-pharmacygui` | Commented out line 44: path: /spec/template/spec/containers/0/env/- |
| `pharmacy/phr-pharmacygui` | Commented out line 45: value: |
| `pharmacy/phr-pharmacygui` | Commented out line 46: name: CSI_DATA_VERSION |
| `pharmacy/phr-pharmacygui` | Commented out line 47: value: "4.0.127.0" |
| `pharmacy/phr-pharmacygui` | Commented out line 48: - op: add |
| `pharmacy/phr-pharmacygui` | Commented out line 49: path: /spec/template/spec/containers/0/env/- |
| `pharmacy/phr-pharmacygui` | Commented out line 50: value: |
| `pharmacy/phr-pharmacygui` | Commented out line 51: name: CSI_PROJECT_NAME |
| `pharmacy/phr-pharmacygui` | Commented out line 52: value: "phr-pharmacygui" |
| `pharmacy/phr-pharmacygui` | Commented out line 53: - op: add |
| `pharmacy/phr-pharmacygui` | Commented out line 54: path: /spec/template/spec/containers/0/env/- |
| `pharmacy/phr-pharmacygui` | Commented out line 55: value: |
| `pharmacy/phr-pharmacygui` | Commented out line 56: name: CSI_MODULE_NAME |
| `pharmacy/phr-pharmacygui` | Commented out line 57: value: "pharmacyui" |
| `pharmacy/phr-pharmacygui` | Commented out line 58: - op: add |
| `pharmacy/phr-pharmacygui` | Commented out line 59: path: /spec/template/spec/containers/0/env/- |
| `pharmacy/phr-pharmacygui` | Commented out line 60: value: |
| `pharmacy/phr-pharmacygui` | Commented out line 61: name: CSI_PARENT_MODULE_NAME |
| `pharmacy/phr-pharmacygui` | Commented out line 62: value: "pharmacy" |
| `pharmacy/phr-ui-v2` | Replaced Sync reference with DM-Initiator |
| `pharmacy/phr-ui-v2` | Added new sync-presync/sync-postsync Job patches |
| `pharmacy/phr-ui-v2` | Commented out line 24: - target: |
| `pharmacy/phr-ui-v2` | Commented out line 25: group: batch |
| `pharmacy/phr-ui-v2` | Commented out line 26: version: v1 |
| `pharmacy/phr-ui-v2` | Commented out line 27: kind: Job |
| `pharmacy/phr-ui-v2` | Commented out line 28: name: before |
| `pharmacy/phr-ui-v2` | Commented out line 29: patch: |- |
| `pharmacy/phr-ui-v2` | Commented out line 30: - op: replace |
| `pharmacy/phr-ui-v2` | Commented out line 31: path: /metadata/name |
| `pharmacy/phr-ui-v2` | Commented out line 32: value: before-csi-phr-ui-v2 |
| `pharmacy/phr-ui-v2` | Commented out line 33: namespace: moh-uat |
| `pharmacy/phr-ui-v2` | Commented out line 34: - op: add |
| `pharmacy/phr-ui-v2` | Commented out line 35: path: /spec/template/spec/containers/0/env/- |
| `pharmacy/phr-ui-v2` | Commented out line 36: value: |
| `pharmacy/phr-ui-v2` | Commented out line 37: name: CSI_MODULENAME |
| `pharmacy/phr-ui-v2` | Commented out line 38: value: "csi-phr-ui-v2" |
| `pharmacy/phr-ui-v2` | Commented out line 39: - op: add |
| `pharmacy/phr-ui-v2` | Commented out line 40: path: /spec/template/spec/containers/0/env/- |
| `pharmacy/phr-ui-v2` | Commented out line 41: value: |
| `pharmacy/phr-ui-v2` | Commented out line 42: name: CSI_DATA_VERSION |
| `pharmacy/phr-ui-v2` | Commented out line 43: value: "4.2.15.0" |
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
| `renal/ren-hemodialysis-srv` | Replaced Sync reference with DM-Initiator |
| `renal/ren-hemodialysis-srv` | Added new sync-presync/sync-postsync Job patches |
| `renal/ren-hemodialysis-srv` | Commented out line 20: - target: |
| `renal/ren-hemodialysis-srv` | Commented out line 21: group: batch |
| `renal/ren-hemodialysis-srv` | Commented out line 22: version: v1 |
| `renal/ren-hemodialysis-srv` | Commented out line 23: kind: Job |
| `renal/ren-hemodialysis-srv` | Commented out line 24: name: .* |
| `renal/ren-hemodialysis-srv` | Commented out line 25: patch: |- |
| `renal/ren-hemodialysis-srv` | Commented out line 26: - op: replace |
| `renal/ren-hemodialysis-srv` | Commented out line 27: path: /metadata/name |
| `renal/ren-hemodialysis-srv` | Commented out line 28: value: before-csi-net-hemdialy |
| `renal/ren-hemodialysis-srv` | Commented out line 29: namespace: vida-uat |
| `renal/ren-hemodialysis-srv` | Commented out line 30: - op: add |
| `renal/ren-hemodialysis-srv` | Commented out line 31: path: /spec/template/spec/containers/0/env/- |
| `renal/ren-hemodialysis-srv` | Commented out line 32: value: |
| `renal/ren-hemodialysis-srv` | Commented out line 33: name: CSI_MODULENAME |
| `renal/ren-hemodialysis-srv` | Commented out line 34: value: "csi-net-hemdialy" |
| `renal/ren-hemodialysis-srv` | Commented out line 35: - op: add |
| `renal/ren-hemodialysis-srv` | Commented out line 36: path: /spec/template/spec/containers/0/env/- |
| `renal/ren-hemodialysis-srv` | Commented out line 37: value: |
| `renal/ren-hemodialysis-srv` | Commented out line 38: name: CSI_DATA_VERSION |
| `renal/ren-hemodialysis-srv` | Commented out line 39: value: "4.0.127.0" |
| `renal/ren-hemodialysis-srv` | Commented out line 40: - op: add |
| `renal/ren-hemodialysis-srv` | Commented out line 41: path: /spec/template/spec/containers/0/env/- |
| `renal/ren-hemodialysis-srv` | Commented out line 42: value: |
| `renal/ren-hemodialysis-srv` | Commented out line 43: name: CSI_PROJECT_NAME |
| `renal/ren-hemodialysis-srv` | Commented out line 44: value: "ren-hemodialysis-srv" |
| `renal/ren-hemodialysis-srv` | Commented out line 45: - op: add |
| `renal/ren-hemodialysis-srv` | Commented out line 46: path: /spec/template/spec/containers/0/env/- |
| `renal/ren-hemodialysis-srv` | Commented out line 47: value: |
| `renal/ren-hemodialysis-srv` | Commented out line 48: name: CSI_MODULE_NAME |
| `renal/ren-hemodialysis-srv` | Commented out line 49: value: "renalnet" |
| `renal/ren-hemodialysis-srv` | Commented out line 50: - op: add |
| `renal/ren-hemodialysis-srv` | Commented out line 51: path: /spec/template/spec/containers/0/env/- |
| `renal/ren-hemodialysis-srv` | Commented out line 52: value: |
| `renal/ren-hemodialysis-srv` | Commented out line 53: name: CSI_PARENT_MODULE_NAME |
| `renal/ren-hemodialysis-srv` | Commented out line 54: value: "renal" |
| `rms/csi-ds-dental-core-java-sev` | Replaced Sync reference with DM-Initiator |
| `rms/csi-ds-dental-core-java-sev` | Added new sync-presync/sync-postsync Job patches |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 20: - target: |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 21: group: batch |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 22: version: v1 |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 23: kind: Job |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 24: name: .* |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 25: patch: |- |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 26: - op: replace |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 27: path: /metadata/name |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 28: value: before-csi-java-ds-dental-core |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 29: - op: add |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 30: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 31: value: |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 32: name: CSI_MODULENAME |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 33: value: "csi-java-ds-dental-core" |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 34: - op: add |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 35: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 36: value: |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 37: name: CSI_DATA_VERSION |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 38: value: "4.0.127.0" |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 39: - op: add |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 40: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 41: value: |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 42: name: CSI_PROJECT_NAME |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 43: value: "csi-ds-dental-core-java-sev" |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 44: - op: add |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 45: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 46: value: |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 47: name: CSI_MODULE_NAME |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 48: value: "dsdental" |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 49: - op: add |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 50: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 51: value: |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 52: name: CSI_PARENT_MODULE_NAME |
| `rms/csi-ds-dental-core-java-sev` | Commented out line 53: value: "rms" |
| `rms/csi-mlm-ui` | Replaced Sync reference with DM-Initiator |
| `rms/csi-mlm-ui` | Added new sync-presync/sync-postsync Job patches |
| `rms/csi-mlm-ui` | Commented out line 21: - target: |
| `rms/csi-mlm-ui` | Commented out line 22: group: batch |
| `rms/csi-mlm-ui` | Commented out line 23: version: v1 |
| `rms/csi-mlm-ui` | Commented out line 24: kind: Job |
| `rms/csi-mlm-ui` | Commented out line 25: name: .* |
| `rms/csi-mlm-ui` | Commented out line 26: patch: | |
| `rms/csi-mlm-ui` | Commented out line 27: - op: replace |
| `rms/csi-mlm-ui` | Commented out line 28: path: /metadata/name |
| `rms/csi-mlm-ui` | Commented out line 29: value: before-csi-mlm-ui |
| `rms/csi-mlm-ui` | Commented out line 30: - op: add |
| `rms/csi-mlm-ui` | Commented out line 31: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-mlm-ui` | Commented out line 32: value: |
| `rms/csi-mlm-ui` | Commented out line 33: name: CSI_MODULENAME |
| `rms/csi-mlm-ui` | Commented out line 34: value: "csi-mlm-ui" |
| `rms/csi-mlm-ui` | Commented out line 35: - op: add |
| `rms/csi-mlm-ui` | Commented out line 36: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-mlm-ui` | Commented out line 37: value: |
| `rms/csi-mlm-ui` | Commented out line 38: name: CSI_DATA_VERSION |
| `rms/csi-mlm-ui` | Commented out line 39: value: "AMD-11685" |
| `rms/csi-mlm-ui` | Commented out line 40: - op: add |
| `rms/csi-mlm-ui` | Commented out line 41: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-mlm-ui` | Commented out line 42: value: |
| `rms/csi-mlm-ui` | Commented out line 43: name: CSI_PROJECT_NAME |
| `rms/csi-mlm-ui` | Commented out line 44: value: "csi-mlm-ui" |
| `rms/csi-mlm-ui` | Commented out line 45: - op: add |
| `rms/csi-mlm-ui` | Commented out line 46: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-mlm-ui` | Commented out line 47: value: |
| `rms/csi-mlm-ui` | Commented out line 48: name: CSI_MODULE_NAME |
| `rms/csi-mlm-ui` | Commented out line 49: value: "mlmui" |
| `rms/csi-mlm-ui` | Commented out line 50: - op: add |
| `rms/csi-mlm-ui` | Commented out line 51: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-mlm-ui` | Commented out line 52: value: |
| `rms/csi-mlm-ui` | Commented out line 53: name: CSI_PARENT_MODULE_NAME |
| `rms/csi-mlm-ui` | Commented out line 54: value: "rms" |
| `rms/csi-morgue-ui` | Replaced Sync reference with DM-Initiator |
| `rms/csi-morgue-ui` | Added new sync-presync/sync-postsync Job patches |
| `rms/csi-morgue-ui` | Commented out line 21: - target: |
| `rms/csi-morgue-ui` | Commented out line 22: group: batch |
| `rms/csi-morgue-ui` | Commented out line 23: version: v1 |
| `rms/csi-morgue-ui` | Commented out line 24: kind: Job |
| `rms/csi-morgue-ui` | Commented out line 25: name: .* |
| `rms/csi-morgue-ui` | Commented out line 26: patch: |- |
| `rms/csi-morgue-ui` | Commented out line 27: - op: replace |
| `rms/csi-morgue-ui` | Commented out line 28: path: /metadata/name |
| `rms/csi-morgue-ui` | Commented out line 29: value: before-csi-morgue-ui |
| `rms/csi-morgue-ui` | Commented out line 30: - op: add |
| `rms/csi-morgue-ui` | Commented out line 31: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-morgue-ui` | Commented out line 32: value: |
| `rms/csi-morgue-ui` | Commented out line 33: name: CSI_MODULENAME |
| `rms/csi-morgue-ui` | Commented out line 34: value: "csi-morgue-ui" |
| `rms/csi-morgue-ui` | Commented out line 35: - op: add |
| `rms/csi-morgue-ui` | Commented out line 36: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-morgue-ui` | Commented out line 37: value: |
| `rms/csi-morgue-ui` | Commented out line 38: name: CSI_DATA_VERSION |
| `rms/csi-morgue-ui` | Commented out line 39: value: "4.0.127.0" |
| `rms/csi-morgue-ui` | Commented out line 40: - op: add |
| `rms/csi-morgue-ui` | Commented out line 41: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-morgue-ui` | Commented out line 42: value: |
| `rms/csi-morgue-ui` | Commented out line 43: name: CSI_PROJECT_NAME |
| `rms/csi-morgue-ui` | Commented out line 44: value: "csi-morgue-ui" |
| `rms/csi-morgue-ui` | Commented out line 45: - op: add |
| `rms/csi-morgue-ui` | Commented out line 46: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-morgue-ui` | Commented out line 47: value: |
| `rms/csi-morgue-ui` | Commented out line 48: name: CSI_MODULE_NAME |
| `rms/csi-morgue-ui` | Commented out line 49: value: "rmsmorgueui" |
| `rms/csi-morgue-ui` | Commented out line 50: - op: add |
| `rms/csi-morgue-ui` | Commented out line 51: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-morgue-ui` | Commented out line 52: value: |
| `rms/csi-morgue-ui` | Commented out line 53: name: CSI_PARENT_MODULE_NAME |
| `rms/csi-morgue-ui` | Commented out line 54: value: "rms" |
| `rms/csi-pms-adt-request-java-sev` | Replaced Sync reference with DM-Initiator |
| `rms/csi-pms-adt-request-java-sev` | Added new sync-presync/sync-postsync Job patches |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 21: - target: |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 22: group: batch |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 23: version: v1 |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 24: kind: Job |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 25: name: .* |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 26: patch: |- |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 27: - op: replace |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 28: path: /metadata/name |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 29: value: before-csi-pms-adt-request |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 30: - op: add |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 31: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 32: value: |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 33: name: CSI_MODULENAME |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 34: value: "csi-pms-adt-request" |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 35: - op: add |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 36: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 37: value: |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 38: name: CSI_DATA_VERSION |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 39: value: "4.0.127.0" |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 40: - op: add |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 41: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 42: value: |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 43: name: CSI_PROJECT_NAME |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 44: value: "csi-pms-adt-request-java-sev" |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 45: - op: add |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 46: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 47: value: |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 48: name: CSI_MODULE_NAME |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 49: value: "pmsadtrequest" |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 50: - op: add |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 51: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 52: value: |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 53: name: CSI_PARENT_MODULE_NAME |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 54: value: "rms" |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 55: - op: add |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 56: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 57: value: |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 58: name: isDropValidationDisabled |
| `rms/csi-pms-adt-request-java-sev` | Commented out line 59: value: "true" |
| `rms/csi-pms-adt-ui` | Replaced Sync reference with DM-Initiator |
| `rms/csi-pms-adt-ui` | Added new sync-presync/sync-postsync Job patches |
| `rms/csi-pms-adt-ui` | Commented out line 21: - target: |
| `rms/csi-pms-adt-ui` | Commented out line 22: group: batch |
| `rms/csi-pms-adt-ui` | Commented out line 23: version: v1 |
| `rms/csi-pms-adt-ui` | Commented out line 24: kind: Job |
| `rms/csi-pms-adt-ui` | Commented out line 25: name: .* |
| `rms/csi-pms-adt-ui` | Commented out line 26: patch: |- |
| `rms/csi-pms-adt-ui` | Commented out line 27: - op: replace |
| `rms/csi-pms-adt-ui` | Commented out line 28: path: /metadata/name |
| `rms/csi-pms-adt-ui` | Commented out line 29: value: before-csi-adt-ui |
| `rms/csi-pms-adt-ui` | Commented out line 30: - op: add |
| `rms/csi-pms-adt-ui` | Commented out line 31: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-pms-adt-ui` | Commented out line 32: value: |
| `rms/csi-pms-adt-ui` | Commented out line 33: name: CSI_MODULENAME |
| `rms/csi-pms-adt-ui` | Commented out line 34: value: "csi-adt-ui" |
| `rms/csi-pms-adt-ui` | Commented out line 35: - op: add |
| `rms/csi-pms-adt-ui` | Commented out line 36: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-pms-adt-ui` | Commented out line 37: value: |
| `rms/csi-pms-adt-ui` | Commented out line 38: name: CSI_DATA_VERSION |
| `rms/csi-pms-adt-ui` | Commented out line 39: value: "4.1.28.20" |
| `rms/csi-pms-adt-ui` | Commented out line 40: - op: add |
| `rms/csi-pms-adt-ui` | Commented out line 41: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-pms-adt-ui` | Commented out line 42: value: |
| `rms/csi-pms-adt-ui` | Commented out line 43: name: CSI_PROJECT_NAME |
| `rms/csi-pms-adt-ui` | Commented out line 44: value: "csi-pms-adt-ui" |
| `rms/csi-pms-adt-ui` | Commented out line 45: - op: add |
| `rms/csi-pms-adt-ui` | Commented out line 46: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-pms-adt-ui` | Commented out line 47: value: |
| `rms/csi-pms-adt-ui` | Commented out line 48: name: CSI_MODULE_NAME |
| `rms/csi-pms-adt-ui` | Commented out line 49: value: "adtui" |
| `rms/csi-pms-adt-ui` | Commented out line 50: - op: add |
| `rms/csi-pms-adt-ui` | Commented out line 51: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-pms-adt-ui` | Commented out line 52: value: |
| `rms/csi-pms-adt-ui` | Commented out line 53: name: CSI_PARENT_MODULE_NAME |
| `rms/csi-pms-adt-ui` | Commented out line 54: value: "rms" |
| `rms/csi-rms-masterdata-java-sev` | Replaced Sync reference with DM-Initiator |
| `rms/csi-rms-masterdata-java-sev` | Removed extra Sync reference: # - ../../../Sync-DM/ |
| `rms/csi-rms-masterdata-java-sev` | Added new sync-presync/sync-postsync Job patches |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 20: - target: |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 21: group: batch |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 22: version: v1 |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 23: kind: Job |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 24: name: .* |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 25: patch: |- |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 26: - op: replace |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 27: path: /metadata/name |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 28: value: before-csi-rms-masterdata |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 29: - op: add |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 30: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 31: value: |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 32: name: CSI_MODULENAME |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 33: value: "csi-rms-masterdata" |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 34: - op: add |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 35: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 36: value: |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 37: name: CSI_DATA_VERSION |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 38: value: "4.1.28.20" |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 39: - op: add |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 40: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 41: value: |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 42: name: CSI_PROJECT_NAME |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 43: value: "csi-rms-masterdata-java-sev" |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 44: - op: add |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 45: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 46: value: |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 47: name: CSI_MODULE_NAME |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 48: value: "rmsmasterdata" |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 49: - op: add |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 50: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 51: value: |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 52: name: CSI_PARENT_MODULE_NAME |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 53: value: "rms" |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 55: - target: |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 56: group: batch |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 57: version: v1 |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 58: kind: Job |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 59: name: data-migration-presync |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 60: patch: |- |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 61: - op: replace |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 62: path: /metadata/name |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 63: value: data-migration-presync-csi-rms-masterdata |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 64: - op: add |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 65: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 66: value: |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 67: name: CSI_MODULENAME |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 68: value: "csi-rms-masterdata" |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 69: - op: add |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 70: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 71: value: |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 72: name: CSI_DATA_VERSION |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 73: value: "4.1.28.20" |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 74: - op: add |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 75: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 76: value: |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 77: name: CSI_PROJECT_NAME |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 78: value: "csi-rms-masterdata-java-sev" |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 79: - op: add |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 80: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 81: value: |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 82: name: CSI_MODULE_NAME |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 83: value: "rmsmasterdata" |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 84: - op: add |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 85: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 86: value: |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 87: name: CSI_PARENT_MODULE_NAME |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 88: value: "rms" |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 90: - target: |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 91: group: batch |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 92: version: v1 |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 93: kind: Job |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 94: name: data-migration-postsync |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 95: patch: |- |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 96: - op: replace |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 97: path: /metadata/name |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 98: value: data-migration-postsync-csi-rms-masterdata |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 99: - op: add |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 100: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 101: value: |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 102: name: CSI_MODULENAME |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 103: value: "csi-rms-masterdata" |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 104: - op: add |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 105: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 106: value: |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 107: name: CSI_DATA_VERSION |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 108: value: "4.1.28.20" |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 109: - op: add |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 110: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 111: value: |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 112: name: CSI_PROJECT_NAME |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 113: value: "csi-rms-masterdata" |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 114: - op: add |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 115: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 116: value: |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 117: name: CSI_MODULE_NAME |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 118: value: "rmsmasterdata" |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 119: - op: add |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 120: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 121: value: |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 122: name: CSI_PARENT_MODULE_NAME |
| `rms/csi-rms-masterdata-java-sev` | Commented out line 123: value: "rms" |
| `rms/csi-rms-morgue-java-service` | Replaced Sync reference with DM-Initiator |
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
| `rms/csi-rms-morgue-java-service` | Commented out line 32: namespace: moh-uat |
| `rms/csi-rms-morgue-java-service` | Commented out line 33: - op: add |
| `rms/csi-rms-morgue-java-service` | Commented out line 34: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-morgue-java-service` | Commented out line 35: value: |
| `rms/csi-rms-morgue-java-service` | Commented out line 36: name: CSI_DATA_VERSION |
| `rms/csi-rms-morgue-java-service` | Commented out line 37: value: "4.0.127.0" |
| `rms/csi-rms-morgue-java-service` | Commented out line 38: - op: add |
| `rms/csi-rms-morgue-java-service` | Commented out line 39: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-morgue-java-service` | Commented out line 40: value: |
| `rms/csi-rms-morgue-java-service` | Commented out line 41: name: CSI_PROJECT_NAME |
| `rms/csi-rms-morgue-java-service` | Commented out line 42: value: "csi-rms-morgue-java-service" |
| `rms/csi-rms-morgue-java-service` | Commented out line 43: - op: add |
| `rms/csi-rms-morgue-java-service` | Commented out line 44: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-morgue-java-service` | Commented out line 45: value: |
| `rms/csi-rms-morgue-java-service` | Commented out line 46: name: CSI_MODULE_NAME |
| `rms/csi-rms-morgue-java-service` | Commented out line 47: value: "rmsmorgue" |
| `rms/csi-rms-morgue-java-service` | Commented out line 48: - op: add |
| `rms/csi-rms-morgue-java-service` | Commented out line 49: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-morgue-java-service` | Commented out line 50: value: |
| `rms/csi-rms-morgue-java-service` | Commented out line 51: name: CSI_PARENT_MODULE_NAME |
| `rms/csi-rms-morgue-java-service` | Commented out line 52: value: "rms" |
| `rms/csi-rms-reservation-java-sev` | Replaced Sync reference with DM-Initiator |
| `rms/csi-rms-reservation-java-sev` | Added new sync-presync/sync-postsync Job patches |
| `rms/csi-rms-reservation-java-sev` | Commented out line 28: - target: |
| `rms/csi-rms-reservation-java-sev` | Commented out line 29: group: batch |
| `rms/csi-rms-reservation-java-sev` | Commented out line 30: version: v1 |
| `rms/csi-rms-reservation-java-sev` | Commented out line 31: kind: Job |
| `rms/csi-rms-reservation-java-sev` | Commented out line 32: name: .* |
| `rms/csi-rms-reservation-java-sev` | Commented out line 33: patch: |- |
| `rms/csi-rms-reservation-java-sev` | Commented out line 34: - op: replace |
| `rms/csi-rms-reservation-java-sev` | Commented out line 35: path: /metadata/name |
| `rms/csi-rms-reservation-java-sev` | Commented out line 36: value: before-csi-rms-reservation-java-sev |
| `rms/csi-rms-reservation-java-sev` | Commented out line 37: namespace: vida-prod |
| `rms/csi-rms-reservation-java-sev` | Commented out line 38: - op: add |
| `rms/csi-rms-reservation-java-sev` | Commented out line 39: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-reservation-java-sev` | Commented out line 40: value: |
| `rms/csi-rms-reservation-java-sev` | Commented out line 41: name: CSI_MODULENAME |
| `rms/csi-rms-reservation-java-sev` | Commented out line 42: value: "csi-rms-reservation-java-sev" |
| `rms/csi-rms-reservation-java-sev` | Commented out line 43: - op: add |
| `rms/csi-rms-reservation-java-sev` | Commented out line 44: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-reservation-java-sev` | Commented out line 45: value: |
| `rms/csi-rms-reservation-java-sev` | Commented out line 46: name: CSI_DATA_VERSION |
| `rms/csi-rms-reservation-java-sev` | Commented out line 47: value: "AMD-11685" |
| `rms/csi-rms-reservation-java-sev` | Commented out line 48: - op: add |
| `rms/csi-rms-reservation-java-sev` | Commented out line 49: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-reservation-java-sev` | Commented out line 50: value: |
| `rms/csi-rms-reservation-java-sev` | Commented out line 51: name: CSI_PROJECT_NAME |
| `rms/csi-rms-reservation-java-sev` | Commented out line 52: value: "csi-rms-reservation-java-sev" |
| `rms/csi-rms-reservation-java-sev` | Commented out line 53: - op: add |
| `rms/csi-rms-reservation-java-sev` | Commented out line 54: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-reservation-java-sev` | Commented out line 55: value: |
| `rms/csi-rms-reservation-java-sev` | Commented out line 56: name: CSI_MODULE_NAME |
| `rms/csi-rms-reservation-java-sev` | Commented out line 57: value: "rmsreservation" |
| `rms/csi-rms-reservation-java-sev` | Commented out line 58: - op: add |
| `rms/csi-rms-reservation-java-sev` | Commented out line 59: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-reservation-java-sev` | Commented out line 60: value: |
| `rms/csi-rms-reservation-java-sev` | Commented out line 61: name: CSI_PARENT_MODULE_NAME |
| `rms/csi-rms-reservation-java-sev` | Commented out line 62: value: "rms" |
| `rms/csi-rms-resource-registry-java-sev` | Replaced Sync reference with DM-Initiator |
| `rms/csi-rms-resource-registry-java-sev` | Added new sync-presync/sync-postsync Job patches |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 48: - target: |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 49: group: batch |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 50: version: v1 |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 51: kind: Job |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 52: name: .* |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 53: patch: |- |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 54: - op: replace |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 55: path: /metadata/name |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 56: value: before-csi-rms-resource-registry |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 57: namespace: moh-uat |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 58: - op: add |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 59: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 60: value: |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 61: name: CSI_MODULENAME |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 62: value: "csi-rms-resource-registry" |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 63: - op: add |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 64: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 65: value: |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 66: name: CSI_DATA_VERSION |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 67: value: "4.0.161.0" |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 68: - op: add |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 69: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 70: value: |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 71: name: CSI_PROJECT_NAME |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 72: value: "csi-rms-resource-registry-java-sev" |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 73: - op: add |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 74: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 75: value: |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 76: name: CSI_MODULE_NAME |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 77: value: "rmsresourceregistry" |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 78: - op: add |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 79: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 80: value: |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 81: name: CSI_PARENT_MODULE_NAME |
| `rms/csi-rms-resource-registry-java-sev` | Commented out line 82: value: "rms" |
| `rms/csi-rms-ui` | Replaced Sync reference with DM-Initiator |
| `rms/csi-rms-ui` | Added new sync-presync/sync-postsync Job patches |
| `rms/csi-rms-ui` | Commented out line 21: - target: |
| `rms/csi-rms-ui` | Commented out line 22: group: batch |
| `rms/csi-rms-ui` | Commented out line 23: version: v1 |
| `rms/csi-rms-ui` | Commented out line 24: kind: Job |
| `rms/csi-rms-ui` | Commented out line 25: name: .* |
| `rms/csi-rms-ui` | Commented out line 26: patch: |- |
| `rms/csi-rms-ui` | Commented out line 27: - op: replace |
| `rms/csi-rms-ui` | Commented out line 28: path: /metadata/name |
| `rms/csi-rms-ui` | Commented out line 29: value: before-rmsui |
| `rms/csi-rms-ui` | Commented out line 30: - op: add |
| `rms/csi-rms-ui` | Commented out line 31: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-ui` | Commented out line 32: value: |
| `rms/csi-rms-ui` | Commented out line 33: name: CSI_MODULENAME |
| `rms/csi-rms-ui` | Commented out line 34: value: "csi-rms-ui" |
| `rms/csi-rms-ui` | Commented out line 35: - op: add |
| `rms/csi-rms-ui` | Commented out line 36: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-ui` | Commented out line 37: value: |
| `rms/csi-rms-ui` | Commented out line 38: name: CSI_DATA_VERSION |
| `rms/csi-rms-ui` | Commented out line 39: value: "AMD-10410" |
| `rms/csi-rms-ui` | Commented out line 40: - op: add |
| `rms/csi-rms-ui` | Commented out line 41: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-ui` | Commented out line 42: value: |
| `rms/csi-rms-ui` | Commented out line 43: name: CSI_PROJECT_NAME |
| `rms/csi-rms-ui` | Commented out line 44: value: "csi-rms-ui" |
| `rms/csi-rms-ui` | Commented out line 45: - op: add |
| `rms/csi-rms-ui` | Commented out line 46: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-ui` | Commented out line 47: value: |
| `rms/csi-rms-ui` | Commented out line 48: name: CSI_MODULE_NAME |
| `rms/csi-rms-ui` | Commented out line 49: value: "rmsui" |
| `rms/csi-rms-ui` | Commented out line 50: - op: add |
| `rms/csi-rms-ui` | Commented out line 51: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-rms-ui` | Commented out line 52: value: |
| `rms/csi-rms-ui` | Commented out line 53: name: CSI_PARENT_MODULE_NAME |
| `rms/csi-rms-ui` | Commented out line 54: value: "rms" |
| `rms/csi-setup-ui` | Replaced Sync reference with DM-Initiator |
| `rms/csi-setup-ui` | Added new sync-presync/sync-postsync Job patches |
| `rms/csi-setup-ui` | Commented out line 21: - target: |
| `rms/csi-setup-ui` | Commented out line 22: group: batch |
| `rms/csi-setup-ui` | Commented out line 23: version: v1 |
| `rms/csi-setup-ui` | Commented out line 24: kind: Job |
| `rms/csi-setup-ui` | Commented out line 25: name: .* |
| `rms/csi-setup-ui` | Commented out line 26: patch: |- |
| `rms/csi-setup-ui` | Commented out line 27: - op: replace |
| `rms/csi-setup-ui` | Commented out line 28: path: /metadata/name |
| `rms/csi-setup-ui` | Commented out line 29: value: before-csi-setup-ui |
| `rms/csi-setup-ui` | Commented out line 30: - op: add |
| `rms/csi-setup-ui` | Commented out line 31: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-setup-ui` | Commented out line 32: value: |
| `rms/csi-setup-ui` | Commented out line 33: name: CSI_MODULENAME |
| `rms/csi-setup-ui` | Commented out line 34: value: "csi-setup-ui" |
| `rms/csi-setup-ui` | Commented out line 35: - op: add |
| `rms/csi-setup-ui` | Commented out line 36: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-setup-ui` | Commented out line 37: value: |
| `rms/csi-setup-ui` | Commented out line 38: name: CSI_DATA_VERSION |
| `rms/csi-setup-ui` | Commented out line 39: value: "4.0.127.0" |
| `rms/csi-setup-ui` | Commented out line 40: - op: add |
| `rms/csi-setup-ui` | Commented out line 41: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-setup-ui` | Commented out line 42: value: |
| `rms/csi-setup-ui` | Commented out line 43: name: CSI_PROJECT_NAME |
| `rms/csi-setup-ui` | Commented out line 44: value: "csi-setup-ui" |
| `rms/csi-setup-ui` | Commented out line 45: - op: add |
| `rms/csi-setup-ui` | Commented out line 46: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-setup-ui` | Commented out line 47: value: |
| `rms/csi-setup-ui` | Commented out line 48: name: CSI_MODULE_NAME |
| `rms/csi-setup-ui` | Commented out line 49: value: "setupui" |
| `rms/csi-setup-ui` | Commented out line 50: - op: add |
| `rms/csi-setup-ui` | Commented out line 51: path: /spec/template/spec/containers/0/env/- |
| `rms/csi-setup-ui` | Commented out line 52: value: |
| `rms/csi-setup-ui` | Commented out line 53: name: CSI_PARENT_MODULE_NAME |
| `rms/csi-setup-ui` | Commented out line 54: value: "rms" |
| `rms/rmsreservation-360` | Updated Deployment target name: csi-rms-reservation-360 -> rmsreservation-360 |
