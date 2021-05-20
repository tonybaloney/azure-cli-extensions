# Azure CLI Module Creation Report

## EXTENSION
|CLI Extension|Command Groups|
|---------|------------|
|az dataprotection|[groups](#CommandGroups)

## GROUPS
### <a name="CommandGroups">Command groups in `az dataprotection` extension </a>
|CLI Command Group|Group Swagger name|Commands|
|---------|------------|--------|
|az dataprotection||[commands](#CommandsIn)|
|az dataprotection backup-instance|BackupInstances|[commands](#CommandsInBackupInstances)|
|az dataprotection backup-policy|BackupPolicies|[commands](#CommandsInBackupPolicies)|
|az dataprotection backup-vault|BackupVaults|[commands](#CommandsInBackupVaults)|
|az dataprotection job|Jobs|[commands](#CommandsInJobs)|
|az dataprotection job|Job|[commands](#CommandsInJob)|
|az dataprotection recovery-point|RecoveryPoints|[commands](#CommandsInRecoveryPoints)|
|az dataprotection recovery-point|RecoveryPoint|[commands](#CommandsInRecoveryPoint)|

## COMMANDS
### <a name="CommandsIn">Commands in `az dataprotection` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az dataprotection check-feature-support](#CheckFeatureSupport)|CheckFeatureSupport|[Parameters](#ParametersCheckFeatureSupport)|[Example](#ExamplesCheckFeatureSupport)|
|[az dataprotection show-operation-result-patch](#GetOperationResultPatch)|GetOperationResultPatch|[Parameters](#ParametersGetOperationResultPatch)|[Example](#ExamplesGetOperationResultPatch)|
|[az dataprotection show-operation-status](#GetOperationStatus)|GetOperationStatus|[Parameters](#ParametersGetOperationStatus)|[Example](#ExamplesGetOperationStatus)|

### <a name="CommandsInBackupInstances">Commands in `az dataprotection backup-instance` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az dataprotection backup-instance list](#BackupInstancesList)|List|[Parameters](#ParametersBackupInstancesList)|[Example](#ExamplesBackupInstancesList)|
|[az dataprotection backup-instance show](#BackupInstancesGet)|Get|[Parameters](#ParametersBackupInstancesGet)|[Example](#ExamplesBackupInstancesGet)|
|[az dataprotection backup-instance create](#BackupInstancesCreateOrUpdate#Create)|CreateOrUpdate#Create|[Parameters](#ParametersBackupInstancesCreateOrUpdate#Create)|[Example](#ExamplesBackupInstancesCreateOrUpdate#Create)|
|[az dataprotection backup-instance update](#BackupInstancesCreateOrUpdate#Update)|CreateOrUpdate#Update|[Parameters](#ParametersBackupInstancesCreateOrUpdate#Update)|Not Found|
|[az dataprotection backup-instance delete](#BackupInstancesDelete)|Delete|[Parameters](#ParametersBackupInstancesDelete)|[Example](#ExamplesBackupInstancesDelete)|
|[az dataprotection backup-instance adhoc-backup](#BackupInstancesAdhocBackup)|AdhocBackup|[Parameters](#ParametersBackupInstancesAdhocBackup)|[Example](#ExamplesBackupInstancesAdhocBackup)|
|[az dataprotection backup-instance azure-backup-recovery-point-based-restore-request azure-backup-restore-with-rehydration-request item-level-restore-target-info trigger-restore](#BackupInstancesTriggerRestore#AzureBackupRecoveryPointBasedRestoreRequest#AzureBackupRestoreWithRehydrationRequest#ItemLevelRestoreTargetInfo)|TriggerRestore#AzureBackupRecoveryPointBasedRestoreRequest#AzureBackupRestoreWithRehydrationRequest#ItemLevelRestoreTargetInfo|[Parameters](#ParametersBackupInstancesTriggerRestore#AzureBackupRecoveryPointBasedRestoreRequest#AzureBackupRestoreWithRehydrationRequest#ItemLevelRestoreTargetInfo)|[Example](#ExamplesBackupInstancesTriggerRestore#AzureBackupRecoveryPointBasedRestoreRequest#AzureBackupRestoreWithRehydrationRequest#ItemLevelRestoreTargetInfo)|
|[az dataprotection backup-instance azure-backup-recovery-point-based-restore-request azure-backup-restore-with-rehydration-request restore-files-target-info trigger-restore](#BackupInstancesTriggerRestore#AzureBackupRecoveryPointBasedRestoreRequest#AzureBackupRestoreWithRehydrationRequest#RestoreFilesTargetInfo)|TriggerRestore#AzureBackupRecoveryPointBasedRestoreRequest#AzureBackupRestoreWithRehydrationRequest#RestoreFilesTargetInfo|[Parameters](#ParametersBackupInstancesTriggerRestore#AzureBackupRecoveryPointBasedRestoreRequest#AzureBackupRestoreWithRehydrationRequest#RestoreFilesTargetInfo)|[Example](#ExamplesBackupInstancesTriggerRestore#AzureBackupRecoveryPointBasedRestoreRequest#AzureBackupRestoreWithRehydrationRequest#RestoreFilesTargetInfo)|
|[az dataprotection backup-instance azure-backup-recovery-point-based-restore-request azure-backup-restore-with-rehydration-request restore-target-info trigger-restore](#BackupInstancesTriggerRestore#AzureBackupRecoveryPointBasedRestoreRequest#AzureBackupRestoreWithRehydrationRequest#RestoreTargetInfo)|TriggerRestore#AzureBackupRecoveryPointBasedRestoreRequest#AzureBackupRestoreWithRehydrationRequest#RestoreTargetInfo|[Parameters](#ParametersBackupInstancesTriggerRestore#AzureBackupRecoveryPointBasedRestoreRequest#AzureBackupRestoreWithRehydrationRequest#RestoreTargetInfo)|[Example](#ExamplesBackupInstancesTriggerRestore#AzureBackupRecoveryPointBasedRestoreRequest#AzureBackupRestoreWithRehydrationRequest#RestoreTargetInfo)|
|[az dataprotection backup-instance azure-backup-recovery-time-based-restore-request item-level-restore-target-info trigger-restore](#BackupInstancesTriggerRestore#AzureBackupRecoveryTimeBasedRestoreRequest#ItemLevelRestoreTargetInfo)|TriggerRestore#AzureBackupRecoveryTimeBasedRestoreRequest#ItemLevelRestoreTargetInfo|[Parameters](#ParametersBackupInstancesTriggerRestore#AzureBackupRecoveryTimeBasedRestoreRequest#ItemLevelRestoreTargetInfo)|[Example](#ExamplesBackupInstancesTriggerRestore#AzureBackupRecoveryTimeBasedRestoreRequest#ItemLevelRestoreTargetInfo)|
|[az dataprotection backup-instance azure-backup-recovery-time-based-restore-request restore-files-target-info trigger-restore](#BackupInstancesTriggerRestore#AzureBackupRecoveryTimeBasedRestoreRequest#RestoreFilesTargetInfo)|TriggerRestore#AzureBackupRecoveryTimeBasedRestoreRequest#RestoreFilesTargetInfo|[Parameters](#ParametersBackupInstancesTriggerRestore#AzureBackupRecoveryTimeBasedRestoreRequest#RestoreFilesTargetInfo)|[Example](#ExamplesBackupInstancesTriggerRestore#AzureBackupRecoveryTimeBasedRestoreRequest#RestoreFilesTargetInfo)|
|[az dataprotection backup-instance azure-backup-recovery-time-based-restore-request restore-target-info trigger-restore](#BackupInstancesTriggerRestore#AzureBackupRecoveryTimeBasedRestoreRequest#RestoreTargetInfo)|TriggerRestore#AzureBackupRecoveryTimeBasedRestoreRequest#RestoreTargetInfo|[Parameters](#ParametersBackupInstancesTriggerRestore#AzureBackupRecoveryTimeBasedRestoreRequest#RestoreTargetInfo)|[Example](#ExamplesBackupInstancesTriggerRestore#AzureBackupRecoveryTimeBasedRestoreRequest#RestoreTargetInfo)|
|[az dataprotection backup-instance azure-backup-restore-with-rehydration-request item-level-restore-target-info trigger-restore](#BackupInstancesTriggerRestore#AzureBackupRestoreWithRehydrationRequest#ItemLevelRestoreTargetInfo)|TriggerRestore#AzureBackupRestoreWithRehydrationRequest#ItemLevelRestoreTargetInfo|[Parameters](#ParametersBackupInstancesTriggerRestore#AzureBackupRestoreWithRehydrationRequest#ItemLevelRestoreTargetInfo)|[Example](#ExamplesBackupInstancesTriggerRestore#AzureBackupRestoreWithRehydrationRequest#ItemLevelRestoreTargetInfo)|
|[az dataprotection backup-instance azure-backup-restore-with-rehydration-request restore-files-target-info trigger-restore](#BackupInstancesTriggerRestore#AzureBackupRestoreWithRehydrationRequest#RestoreFilesTargetInfo)|TriggerRestore#AzureBackupRestoreWithRehydrationRequest#RestoreFilesTargetInfo|[Parameters](#ParametersBackupInstancesTriggerRestore#AzureBackupRestoreWithRehydrationRequest#RestoreFilesTargetInfo)|[Example](#ExamplesBackupInstancesTriggerRestore#AzureBackupRestoreWithRehydrationRequest#RestoreFilesTargetInfo)|
|[az dataprotection backup-instance azure-backup-restore-with-rehydration-request restore-target-info trigger-restore](#BackupInstancesTriggerRestore#AzureBackupRestoreWithRehydrationRequest#RestoreTargetInfo)|TriggerRestore#AzureBackupRestoreWithRehydrationRequest#RestoreTargetInfo|[Parameters](#ParametersBackupInstancesTriggerRestore#AzureBackupRestoreWithRehydrationRequest#RestoreTargetInfo)|[Example](#ExamplesBackupInstancesTriggerRestore#AzureBackupRestoreWithRehydrationRequest#RestoreTargetInfo)|
|[az dataprotection backup-instance trigger-rehydrate](#BackupInstancesTriggerRehydrate)|TriggerRehydrate|[Parameters](#ParametersBackupInstancesTriggerRehydrate)|[Example](#ExamplesBackupInstancesTriggerRehydrate)|

### <a name="CommandsInBackupPolicies">Commands in `az dataprotection backup-policy` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az dataprotection backup-policy list](#BackupPoliciesList)|List|[Parameters](#ParametersBackupPoliciesList)|[Example](#ExamplesBackupPoliciesList)|
|[az dataprotection backup-policy show](#BackupPoliciesGet)|Get|[Parameters](#ParametersBackupPoliciesGet)|[Example](#ExamplesBackupPoliciesGet)|
|[az dataprotection backup-policy create](#BackupPoliciesCreateOrUpdate#Create)|CreateOrUpdate#Create|[Parameters](#ParametersBackupPoliciesCreateOrUpdate#Create)|[Example](#ExamplesBackupPoliciesCreateOrUpdate#Create)|
|[az dataprotection backup-policy update](#BackupPoliciesCreateOrUpdate#Update)|CreateOrUpdate#Update|[Parameters](#ParametersBackupPoliciesCreateOrUpdate#Update)|Not Found|
|[az dataprotection backup-policy delete](#BackupPoliciesDelete)|Delete|[Parameters](#ParametersBackupPoliciesDelete)|[Example](#ExamplesBackupPoliciesDelete)|

### <a name="CommandsInBackupVaults">Commands in `az dataprotection backup-vault` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az dataprotection backup-vault show](#BackupVaultsGet)|Get|[Parameters](#ParametersBackupVaultsGet)|[Example](#ExamplesBackupVaultsGet)|
|[az dataprotection backup-vault create](#BackupVaultsCreateOrUpdate#Create)|CreateOrUpdate#Create|[Parameters](#ParametersBackupVaultsCreateOrUpdate#Create)|[Example](#ExamplesBackupVaultsCreateOrUpdate#Create)|
|[az dataprotection backup-vault update](#BackupVaultsCreateOrUpdate#Update)|CreateOrUpdate#Update|[Parameters](#ParametersBackupVaultsCreateOrUpdate#Update)|Not Found|
|[az dataprotection backup-vault delete](#BackupVaultsDelete)|Delete|[Parameters](#ParametersBackupVaultsDelete)|[Example](#ExamplesBackupVaultsDelete)|
|[az dataprotection backup-vault patch](#BackupVaultsPatch)|Patch|[Parameters](#ParametersBackupVaultsPatch)|[Example](#ExamplesBackupVaultsPatch)|
|[az dataprotection backup-vault show-resource-in-resource-group](#BackupVaultsGetResourcesInResourceGroup)|GetResourcesInResourceGroup|[Parameters](#ParametersBackupVaultsGetResourcesInResourceGroup)|[Example](#ExamplesBackupVaultsGetResourcesInResourceGroup)|
|[az dataprotection backup-vault show-resource-in-subscription](#BackupVaultsGetResourcesInSubscription)|GetResourcesInSubscription|[Parameters](#ParametersBackupVaultsGetResourcesInSubscription)|[Example](#ExamplesBackupVaultsGetResourcesInSubscription)|

### <a name="CommandsInJobs">Commands in `az dataprotection job` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az dataprotection job list](#JobsList)|List|[Parameters](#ParametersJobsList)|[Example](#ExamplesJobsList)|

### <a name="CommandsInJob">Commands in `az dataprotection job` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az dataprotection job show](#JobGet)|Get|[Parameters](#ParametersJobGet)|[Example](#ExamplesJobGet)|

### <a name="CommandsInRecoveryPoints">Commands in `az dataprotection recovery-point` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az dataprotection recovery-point show-list](#RecoveryPointsGetList)|GetList|[Parameters](#ParametersRecoveryPointsGetList)|[Example](#ExamplesRecoveryPointsGetList)|

### <a name="CommandsInRecoveryPoint">Commands in `az dataprotection recovery-point` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az dataprotection recovery-point show](#RecoveryPointGet)|Get|[Parameters](#ParametersRecoveryPointGet)|[Example](#ExamplesRecoveryPointGet)|


## COMMAND DETAILS
### group `az dataprotection`
#### <a name="CheckFeatureSupport">Command `az dataprotection check-feature-support`</a>

##### <a name="ExamplesCheckFeatureSupport">Example</a>
```
az dataprotection check-feature-support --location "WestUS" --feature-validation-request feature-type="DataSourceType"
```
##### <a name="ParametersCheckFeatureSupport">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--location**|string||location|location|
|**--feature-validation-request**|object|Base class for feature object|feature_validation_request|FeatureValidationRequest|

#### <a name="GetOperationResultPatch">Command `az dataprotection show-operation-result-patch`</a>

##### <a name="ExamplesGetOperationResultPatch">Example</a>
```
az dataprotection show-operation-result-patch --operation-id "YWUzNDFkMzQtZmM5OS00MmUyLWEzNDMtZGJkMDIxZjlmZjgzOzdmYzBiM\
zhmLTc2NmItNDM5NS05OWQ1LTVmOGEzNzg4MWQzNA==" --resource-group "SampleResourceGroup" --vault-name "swaggerExample"
```
##### <a name="ParametersGetOperationResultPatch">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--vault-name**|string|The name of the backup vault.|vault_name|vaultName|
|**--resource-group-name**|string|The name of the resource group where the backup vault is present.|resource_group_name|resourceGroupName|
|**--operation-id**|string||operation_id|operationId|

#### <a name="GetOperationStatus">Command `az dataprotection show-operation-status`</a>

##### <a name="ExamplesGetOperationStatus">Example</a>
```
az dataprotection show-operation-status --operation-id "MjkxOTMyODMtYTE3My00YzJjLTg5NjctN2E4MDIxNDA3NjA2OzdjNGE2ZWRjLWJ\
jMmItNDRkYi1hYzMzLWY1YzEwNzk5Y2EyOA==" --location "WestUS"
```
##### <a name="ParametersGetOperationStatus">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--location**|string||location|location|
|**--operation-id**|string||operation_id|operationId|

### group `az dataprotection backup-instance`
#### <a name="BackupInstancesList">Command `az dataprotection backup-instance list`</a>

##### <a name="ExamplesBackupInstancesList">Example</a>
```
az dataprotection backup-instance list --resource-group "000pikumar" --vault-name "PratikPrivatePreviewVault1"
```
##### <a name="ParametersBackupInstancesList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--vault-name**|string|The name of the backup vault.|vault_name|vaultName|
|**--resource-group-name**|string|The name of the resource group where the backup vault is present.|resource_group_name|resourceGroupName|

#### <a name="BackupInstancesGet">Command `az dataprotection backup-instance show`</a>

##### <a name="ExamplesBackupInstancesGet">Example</a>
```
az dataprotection backup-instance show --name "testInstance1" --resource-group "000pikumar" --vault-name \
"PratikPrivatePreviewVault1"
```
##### <a name="ParametersBackupInstancesGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--vault-name**|string|The name of the backup vault.|vault_name|vaultName|
|**--resource-group-name**|string|The name of the resource group where the backup vault is present.|resource_group_name|resourceGroupName|
|**--backup-instance-name**|string|The name of the backup instance|backup_instance_name|backupInstanceName|

#### <a name="BackupInstancesCreateOrUpdate#Create">Command `az dataprotection backup-instance create`</a>

##### <a name="ExamplesBackupInstancesCreateOrUpdate#Create">Example</a>
```
az dataprotection backup-instance create --name "testInstance1" --data-source-info datasource-type="OssDB" \
object-type="Datasource" resource-id="/subscriptions/f75d8d8b-6735-4697-82e1-1a7a3ff0d5d4/resourceGroups/viveksipgtest/\
providers/Microsoft.DBforPostgreSQL/servers/viveksipgtest/databases/testdb" resource-location="" \
resource-name="testdb" resource-type="Microsoft.DBforPostgreSQL/servers/databases" resource-uri="" \
--data-source-set-info datasource-type="OssDB" object-type="DatasourceSet" resource-id="/subscriptions/f75d8d8b-6735-46\
97-82e1-1a7a3ff0d5d4/resourceGroups/viveksipgtest/providers/Microsoft.DBforPostgreSQL/servers/viveksipgtest" \
resource-location="" resource-name="viveksipgtest" resource-type="Microsoft.DBforPostgreSQL/servers" resource-uri="" \
--friendly-name "harshitbi2" --object-type "BackupInstance" --policy-id "/subscriptions/04cf684a-d41f-4550-9f70-7708a3a\
2283b/resourceGroups/000pikumar/providers/Microsoft.DataProtection/Backupvaults/PratikPrivatePreviewVault1/backupPolici\
es/PratikPolicy1" --policy-parameters data-store-parameters-list={"dataStoreType":"OperationalStore","objectType":"Azur\
eOperationalStoreParameters","resourceGroupId":"/subscriptions/f75d8d8b-6735-4697-82e1-1a7a3ff0d5d4/resourceGroups/vive\
ksipgtest"} --resource-group "000pikumar" --vault-name "PratikPrivatePreviewVault1"
```
##### <a name="ParametersBackupInstancesCreateOrUpdate#Create">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--vault-name**|string|The name of the backup vault.|vault_name|vaultName|
|**--resource-group-name**|string|The name of the resource group where the backup vault is present.|resource_group_name|resourceGroupName|
|**--backup-instance-name**|string|The name of the backup instance|backup_instance_name|backupInstanceName|
|**--friendly-name**|string|Gets or sets the Backup Instance friendly name.|friendly_name|friendlyName|
|**--data-source-info**|object|Gets or sets the data source information.|data_source_info|dataSourceInfo|
|**--data-source-set-info**|object|Gets or sets the data source set information.|data_source_set_info|dataSourceSetInfo|
|**--object-type**|string||object_type|objectType|
|**--policy-id**|string||policy_id|policyId|
|**--policy-parameters**|object|Policy parameters for the backup instance|policy_parameters|policyParameters|

#### <a name="BackupInstancesCreateOrUpdate#Update">Command `az dataprotection backup-instance update`</a>


##### <a name="ParametersBackupInstancesCreateOrUpdate#Update">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--vault-name**|string|The name of the backup vault.|vault_name|vaultName|
|**--resource-group-name**|string|The name of the resource group where the backup vault is present.|resource_group_name|resourceGroupName|
|**--backup-instance-name**|string|The name of the backup instance|backup_instance_name|backupInstanceName|
|**--friendly-name**|string|Gets or sets the Backup Instance friendly name.|friendly_name|friendlyName|
|**--data-source-info**|object|Gets or sets the data source information.|data_source_info|dataSourceInfo|
|**--data-source-set-info**|object|Gets or sets the data source set information.|data_source_set_info|dataSourceSetInfo|
|**--object-type**|string||object_type|objectType|
|**--policy-id**|string||policy_id|policyId|
|**--policy-parameters**|object|Policy parameters for the backup instance|policy_parameters|policyParameters|

#### <a name="BackupInstancesDelete">Command `az dataprotection backup-instance delete`</a>

##### <a name="ExamplesBackupInstancesDelete">Example</a>
```
az dataprotection backup-instance delete --name "testInstance1" --resource-group "000pikumar" --vault-name \
"PratikPrivatePreviewVault1"
```
##### <a name="ParametersBackupInstancesDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--vault-name**|string|The name of the backup vault.|vault_name|vaultName|
|**--resource-group-name**|string|The name of the resource group where the backup vault is present.|resource_group_name|resourceGroupName|
|**--backup-instance-name**|string|The name of the backup instance|backup_instance_name|backupInstanceName|

#### <a name="BackupInstancesAdhocBackup">Command `az dataprotection backup-instance adhoc-backup`</a>

##### <a name="ExamplesBackupInstancesAdhocBackup">Example</a>
```
az dataprotection backup-instance adhoc-backup --name "testInstance1" --rule-name "BackupWeekly" \
--retention-tag-override "yearly" --resource-group "000pikumar" --vault-name "PratikPrivatePreviewVault1"
```
##### <a name="ParametersBackupInstancesAdhocBackup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--vault-name**|string|The name of the backup vault.|vault_name|vaultName|
|**--resource-group-name**|string|The name of the resource group where the backup vault is present.|resource_group_name|resourceGroupName|
|**--backup-instance-name**|string|The name of the backup instance|backup_instance_name|backupInstanceName|
|**--rule-name**|string||rule_name|ruleName|
|**--retention-tag-override**|string||retention_tag_override|retentionTagOverride|

#### <a name="BackupInstancesTriggerRestore#AzureBackupRecoveryPointBasedRestoreRequest#AzureBackupRestoreWithRehydrationRequest#ItemLevelRestoreTargetInfo">Command `az dataprotection backup-instance azure-backup-recovery-point-based-restore-request azure-backup-restore-with-rehydration-request item-level-restore-target-info trigger-restore`</a>

##### <a name="ExamplesBackupInstancesTriggerRestore#AzureBackupRecoveryPointBasedRestoreRequest#AzureBackupRestoreWithRehydrationRequest#ItemLevelRestoreTargetInfo">Example</a>
```
az dataprotection backup-instance azure-backup-recovery-point-based-restore-request azure-backup-restore-with-rehydrati\
on-request item-level-restore-target-info trigger-restore --name "testInstance1" --azurebackuprestorewithrehydrationreq\
uest-recovery-point-id "hardcodedRP" --azurebackuprestorewithrehydrationrequest-source-data-store-type "VaultStore" \
--resource-group "000pikumar" --vault-name "PratikPrivatePreviewVault1"
az dataprotection backup-instance azure-backup-recovery-point-based-restore-request azure-backup-restore-with-rehydrati\
on-request item-level-restore-target-info trigger-restore --name "testInstance1" --azurebackuprestorewithrehydrationreq\
uest-recovery-point-id "hardcodedRP" --azurebackuprestorewithrehydrationrequest-source-data-store-type "VaultStore" \
--resource-group "000pikumar" --vault-name "PrivatePreviewVault1"
az dataprotection backup-instance azure-backup-recovery-point-based-restore-request azure-backup-restore-with-rehydrati\
on-request item-level-restore-target-info trigger-restore --name "testInstance1" --azurebackuprestorewithrehydrationreq\
uest-recovery-point-id "hardcodedRP" --azurebackuprestorewithrehydrationrequest-rehydration-priority "High" \
--azurebackuprestorewithrehydrationrequest-rehydration-retention-duration "7D" --azurebackuprestorewithrehydrationreque\
st-source-data-store-type "VaultStore" --resource-group "000pikumar" --vault-name "PratikPrivatePreviewVault1"
```
##### <a name="ParametersBackupInstancesTriggerRestore#AzureBackupRecoveryPointBasedRestoreRequest#AzureBackupRestoreWithRehydrationRequest#ItemLevelRestoreTargetInfo">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--vault-name**|string|The name of the backup vault.|vault_name|vaultName|
|**--resource-group-name**|string|The name of the resource group where the backup vault is present.|resource_group_name|resourceGroupName|
|**--backup-instance-name**|string|The name of the backup instance|backup_instance_name|backupInstanceName|
|**--item-level-restore-target-info-restore-criteria**|array|Restore Criteria|item_level_restore_target_info_restore_criteria|restoreCriteria|
|**--item-level-restore-target-info-datasource-info**|object|Information of target DS|item_level_restore_target_info_datasource_info|datasourceInfo|
|**--azurebackuprestorewithrehydrationrequest-source-data-store-type**|choice|Gets or sets the type of the source data store.|azurebackuprestorewithrehydrationrequest_source_data_store_type|sourceDataStoreType|
|**--azurebackuprestorewithrehydrationrequest-recovery-point-id**|string||azurebackuprestorewithrehydrationrequest_recovery_point_id|recoveryPointId|
|**--azurebackuprestorewithrehydrationrequest-rehydration-priority**|choice|Priority to be used for rehydration. Values High or Standard|azurebackuprestorewithrehydrationrequest_rehydration_priority|rehydrationPriority|
|**--azurebackuprestorewithrehydrationrequest-rehydration-retention-duration**|string|Retention duration in ISO 8601 format i.e P10D .|azurebackuprestorewithrehydrationrequest_rehydration_retention_duration|rehydrationRetentionDuration|
|**--item-level-restore-target-info-restore-location**|string|Target Restore region|item_level_restore_target_info_restore_location|restoreLocation|
|**--item-level-restore-target-info-datasource-set-info**|object|Information of target DS Set|item_level_restore_target_info_datasource_set_info|datasourceSetInfo|

#### <a name="BackupInstancesTriggerRestore#AzureBackupRecoveryPointBasedRestoreRequest#AzureBackupRestoreWithRehydrationRequest#RestoreFilesTargetInfo">Command `az dataprotection backup-instance azure-backup-recovery-point-based-restore-request azure-backup-restore-with-rehydration-request restore-files-target-info trigger-restore`</a>

##### <a name="ExamplesBackupInstancesTriggerRestore#AzureBackupRecoveryPointBasedRestoreRequest#AzureBackupRestoreWithRehydrationRequest#RestoreFilesTargetInfo">Example</a>
```
az dataprotection backup-instance azure-backup-recovery-point-based-restore-request azure-backup-restore-with-rehydrati\
on-request restore-files-target-info trigger-restore --name "testInstance1" --azurebackuprestorewithrehydrationrequest-\
recovery-point-id "hardcodedRP" --azurebackuprestorewithrehydrationrequest-source-data-store-type "VaultStore" \
--resource-group "000pikumar" --vault-name "PratikPrivatePreviewVault1"
az dataprotection backup-instance azure-backup-recovery-point-based-restore-request azure-backup-restore-with-rehydrati\
on-request restore-files-target-info trigger-restore --name "testInstance1" --azurebackuprestorewithrehydrationrequest-\
recovery-point-id "hardcodedRP" --azurebackuprestorewithrehydrationrequest-source-data-store-type "VaultStore" \
--resource-group "000pikumar" --vault-name "PrivatePreviewVault1"
az dataprotection backup-instance azure-backup-recovery-point-based-restore-request azure-backup-restore-with-rehydrati\
on-request restore-files-target-info trigger-restore --name "testInstance1" --azurebackuprestorewithrehydrationrequest-\
recovery-point-id "hardcodedRP" --azurebackuprestorewithrehydrationrequest-rehydration-priority "High" \
--azurebackuprestorewithrehydrationrequest-rehydration-retention-duration "7D" --azurebackuprestorewithrehydrationreque\
st-source-data-store-type "VaultStore" --resource-group "000pikumar" --vault-name "PratikPrivatePreviewVault1"
```
##### <a name="ParametersBackupInstancesTriggerRestore#AzureBackupRecoveryPointBasedRestoreRequest#AzureBackupRestoreWithRehydrationRequest#RestoreFilesTargetInfo">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--vault-name**|string|The name of the backup vault.|vault_name|vaultName|
|**--resource-group-name**|string|The name of the resource group where the backup vault is present.|resource_group_name|resourceGroupName|
|**--backup-instance-name**|string|The name of the backup instance|backup_instance_name|backupInstanceName|
|**--restore-files-target-info-target-details**|object|Destination of RestoreAsFiles operation, when destination is not a datasource|restore_files_target_info_target_details|targetDetails|
|**--azurebackuprestorewithrehydrationrequest-source-data-store-type**|choice|Gets or sets the type of the source data store.|azurebackuprestorewithrehydrationrequest_source_data_store_type|sourceDataStoreType|
|**--azurebackuprestorewithrehydrationrequest-recovery-point-id**|string||azurebackuprestorewithrehydrationrequest_recovery_point_id|recoveryPointId|
|**--azurebackuprestorewithrehydrationrequest-rehydration-priority**|choice|Priority to be used for rehydration. Values High or Standard|azurebackuprestorewithrehydrationrequest_rehydration_priority|rehydrationPriority|
|**--azurebackuprestorewithrehydrationrequest-rehydration-retention-duration**|string|Retention duration in ISO 8601 format i.e P10D .|azurebackuprestorewithrehydrationrequest_rehydration_retention_duration|rehydrationRetentionDuration|
|**--restore-files-target-info-restore-location**|string|Target Restore region|restore_files_target_info_restore_location|restoreLocation|

#### <a name="BackupInstancesTriggerRestore#AzureBackupRecoveryPointBasedRestoreRequest#AzureBackupRestoreWithRehydrationRequest#RestoreTargetInfo">Command `az dataprotection backup-instance azure-backup-recovery-point-based-restore-request azure-backup-restore-with-rehydration-request restore-target-info trigger-restore`</a>

##### <a name="ExamplesBackupInstancesTriggerRestore#AzureBackupRecoveryPointBasedRestoreRequest#AzureBackupRestoreWithRehydrationRequest#RestoreTargetInfo">Example</a>
```
az dataprotection backup-instance azure-backup-recovery-point-based-restore-request azure-backup-restore-with-rehydrati\
on-request restore-target-info trigger-restore --name "testInstance1" --azurebackuprestorewithrehydrationrequest-recove\
ry-point-id "hardcodedRP" --azurebackuprestorewithrehydrationrequest-source-data-store-type "VaultStore" \
--resource-group "000pikumar" --vault-name "PratikPrivatePreviewVault1"
az dataprotection backup-instance azure-backup-recovery-point-based-restore-request azure-backup-restore-with-rehydrati\
on-request restore-target-info trigger-restore --name "testInstance1" --azurebackuprestorewithrehydrationrequest-recove\
ry-point-id "hardcodedRP" --azurebackuprestorewithrehydrationrequest-source-data-store-type "VaultStore" \
--resource-group "000pikumar" --vault-name "PrivatePreviewVault1"
az dataprotection backup-instance azure-backup-recovery-point-based-restore-request azure-backup-restore-with-rehydrati\
on-request restore-target-info trigger-restore --name "testInstance1" --azurebackuprestorewithrehydrationrequest-recove\
ry-point-id "hardcodedRP" --azurebackuprestorewithrehydrationrequest-rehydration-priority "High" \
--azurebackuprestorewithrehydrationrequest-rehydration-retention-duration "7D" --azurebackuprestorewithrehydrationreque\
st-source-data-store-type "VaultStore" --resource-group "000pikumar" --vault-name "PratikPrivatePreviewVault1"
```
##### <a name="ParametersBackupInstancesTriggerRestore#AzureBackupRecoveryPointBasedRestoreRequest#AzureBackupRestoreWithRehydrationRequest#RestoreTargetInfo">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--vault-name**|string|The name of the backup vault.|vault_name|vaultName|
|**--resource-group-name**|string|The name of the resource group where the backup vault is present.|resource_group_name|resourceGroupName|
|**--backup-instance-name**|string|The name of the backup instance|backup_instance_name|backupInstanceName|
|**--restore-target-info-datasource-info**|object|Information of target DS|restore_target_info_datasource_info|datasourceInfo|
|**--azurebackuprestorewithrehydrationrequest-source-data-store-type**|choice|Gets or sets the type of the source data store.|azurebackuprestorewithrehydrationrequest_source_data_store_type|sourceDataStoreType|
|**--azurebackuprestorewithrehydrationrequest-recovery-point-id**|string||azurebackuprestorewithrehydrationrequest_recovery_point_id|recoveryPointId|
|**--azurebackuprestorewithrehydrationrequest-rehydration-priority**|choice|Priority to be used for rehydration. Values High or Standard|azurebackuprestorewithrehydrationrequest_rehydration_priority|rehydrationPriority|
|**--azurebackuprestorewithrehydrationrequest-rehydration-retention-duration**|string|Retention duration in ISO 8601 format i.e P10D .|azurebackuprestorewithrehydrationrequest_rehydration_retention_duration|rehydrationRetentionDuration|
|**--restore-target-info-restore-location**|string|Target Restore region|restore_target_info_restore_location|restoreLocation|
|**--restore-target-info-datasource-set-info**|object|Information of target DS Set|restore_target_info_datasource_set_info|datasourceSetInfo|

#### <a name="BackupInstancesTriggerRestore#AzureBackupRecoveryTimeBasedRestoreRequest#ItemLevelRestoreTargetInfo">Command `az dataprotection backup-instance azure-backup-recovery-time-based-restore-request item-level-restore-target-info trigger-restore`</a>

##### <a name="ExamplesBackupInstancesTriggerRestore#AzureBackupRecoveryTimeBasedRestoreRequest#ItemLevelRestoreTargetInfo">Example</a>
```
az dataprotection backup-instance azure-backup-recovery-time-based-restore-request item-level-restore-target-info \
trigger-restore --name "testInstance1" --azurebackuprecoverytimebasedrestorerequest-source-data-store-type \
"VaultStore" --resource-group "000pikumar" --vault-name "PratikPrivatePreviewVault1"
az dataprotection backup-instance azure-backup-recovery-time-based-restore-request item-level-restore-target-info \
trigger-restore --name "testInstance1" --azurebackuprecoverytimebasedrestorerequest-source-data-store-type \
"VaultStore" --resource-group "000pikumar" --vault-name "PrivatePreviewVault1"
az dataprotection backup-instance azure-backup-recovery-time-based-restore-request item-level-restore-target-info \
trigger-restore --name "testInstance1" --azurebackuprecoverytimebasedrestorerequest-source-data-store-type \
"VaultStore" --resource-group "000pikumar" --vault-name "PratikPrivatePreviewVault1"
```
##### <a name="ParametersBackupInstancesTriggerRestore#AzureBackupRecoveryTimeBasedRestoreRequest#ItemLevelRestoreTargetInfo">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--vault-name**|string|The name of the backup vault.|vault_name|vaultName|
|**--resource-group-name**|string|The name of the resource group where the backup vault is present.|resource_group_name|resourceGroupName|
|**--backup-instance-name**|string|The name of the backup instance|backup_instance_name|backupInstanceName|
|**--item-level-restore-target-info-restore-criteria**|array|Restore Criteria|item_level_restore_target_info_restore_criteria|restoreCriteria|
|**--item-level-restore-target-info-datasource-info**|object|Information of target DS|item_level_restore_target_info_datasource_info|datasourceInfo|
|**--azurebackuprecoverytimebasedrestorerequest-source-data-store-type**|choice|Gets or sets the type of the source data store.|azurebackuprecoverytimebasedrestorerequest_source_data_store_type|sourceDataStoreType|
|**--azurebackuprecoverytimebasedrestorerequest-recovery-point-time**|string|The recovery time in ISO 8601 format example - 2020-08-14T17:30:00.0000000Z.|azurebackuprecoverytimebasedrestorerequest_recovery_point_time|recoveryPointTime|
|**--item-level-restore-target-info-restore-location**|string|Target Restore region|item_level_restore_target_info_restore_location|restoreLocation|
|**--item-level-restore-target-info-datasource-set-info**|object|Information of target DS Set|item_level_restore_target_info_datasource_set_info|datasourceSetInfo|

#### <a name="BackupInstancesTriggerRestore#AzureBackupRecoveryTimeBasedRestoreRequest#RestoreFilesTargetInfo">Command `az dataprotection backup-instance azure-backup-recovery-time-based-restore-request restore-files-target-info trigger-restore`</a>

##### <a name="ExamplesBackupInstancesTriggerRestore#AzureBackupRecoveryTimeBasedRestoreRequest#RestoreFilesTargetInfo">Example</a>
```
az dataprotection backup-instance azure-backup-recovery-time-based-restore-request restore-files-target-info \
trigger-restore --name "testInstance1" --azurebackuprecoverytimebasedrestorerequest-source-data-store-type \
"VaultStore" --resource-group "000pikumar" --vault-name "PratikPrivatePreviewVault1"
az dataprotection backup-instance azure-backup-recovery-time-based-restore-request restore-files-target-info \
trigger-restore --name "testInstance1" --azurebackuprecoverytimebasedrestorerequest-source-data-store-type \
"VaultStore" --resource-group "000pikumar" --vault-name "PrivatePreviewVault1"
az dataprotection backup-instance azure-backup-recovery-time-based-restore-request restore-files-target-info \
trigger-restore --name "testInstance1" --azurebackuprecoverytimebasedrestorerequest-source-data-store-type \
"VaultStore" --resource-group "000pikumar" --vault-name "PratikPrivatePreviewVault1"
```
##### <a name="ParametersBackupInstancesTriggerRestore#AzureBackupRecoveryTimeBasedRestoreRequest#RestoreFilesTargetInfo">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--vault-name**|string|The name of the backup vault.|vault_name|vaultName|
|**--resource-group-name**|string|The name of the resource group where the backup vault is present.|resource_group_name|resourceGroupName|
|**--backup-instance-name**|string|The name of the backup instance|backup_instance_name|backupInstanceName|
|**--restore-files-target-info-target-details**|object|Destination of RestoreAsFiles operation, when destination is not a datasource|restore_files_target_info_target_details|targetDetails|
|**--azurebackuprecoverytimebasedrestorerequest-source-data-store-type**|choice|Gets or sets the type of the source data store.|azurebackuprecoverytimebasedrestorerequest_source_data_store_type|sourceDataStoreType|
|**--azurebackuprecoverytimebasedrestorerequest-recovery-point-time**|string|The recovery time in ISO 8601 format example - 2020-08-14T17:30:00.0000000Z.|azurebackuprecoverytimebasedrestorerequest_recovery_point_time|recoveryPointTime|
|**--restore-files-target-info-restore-location**|string|Target Restore region|restore_files_target_info_restore_location|restoreLocation|

#### <a name="BackupInstancesTriggerRestore#AzureBackupRecoveryTimeBasedRestoreRequest#RestoreTargetInfo">Command `az dataprotection backup-instance azure-backup-recovery-time-based-restore-request restore-target-info trigger-restore`</a>

##### <a name="ExamplesBackupInstancesTriggerRestore#AzureBackupRecoveryTimeBasedRestoreRequest#RestoreTargetInfo">Example</a>
```
az dataprotection backup-instance azure-backup-recovery-time-based-restore-request restore-target-info trigger-restore \
--name "testInstance1" --azurebackuprecoverytimebasedrestorerequest-source-data-store-type "VaultStore" \
--resource-group "000pikumar" --vault-name "PratikPrivatePreviewVault1"
az dataprotection backup-instance azure-backup-recovery-time-based-restore-request restore-target-info trigger-restore \
--name "testInstance1" --azurebackuprecoverytimebasedrestorerequest-source-data-store-type "VaultStore" \
--resource-group "000pikumar" --vault-name "PrivatePreviewVault1"
az dataprotection backup-instance azure-backup-recovery-time-based-restore-request restore-target-info trigger-restore \
--name "testInstance1" --azurebackuprecoverytimebasedrestorerequest-source-data-store-type "VaultStore" \
--resource-group "000pikumar" --vault-name "PratikPrivatePreviewVault1"
```
##### <a name="ParametersBackupInstancesTriggerRestore#AzureBackupRecoveryTimeBasedRestoreRequest#RestoreTargetInfo">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--vault-name**|string|The name of the backup vault.|vault_name|vaultName|
|**--resource-group-name**|string|The name of the resource group where the backup vault is present.|resource_group_name|resourceGroupName|
|**--backup-instance-name**|string|The name of the backup instance|backup_instance_name|backupInstanceName|
|**--restore-target-info-datasource-info**|object|Information of target DS|restore_target_info_datasource_info|datasourceInfo|
|**--azurebackuprecoverytimebasedrestorerequest-source-data-store-type**|choice|Gets or sets the type of the source data store.|azurebackuprecoverytimebasedrestorerequest_source_data_store_type|sourceDataStoreType|
|**--azurebackuprecoverytimebasedrestorerequest-recovery-point-time**|string|The recovery time in ISO 8601 format example - 2020-08-14T17:30:00.0000000Z.|azurebackuprecoverytimebasedrestorerequest_recovery_point_time|recoveryPointTime|
|**--restore-target-info-restore-location**|string|Target Restore region|restore_target_info_restore_location|restoreLocation|
|**--restore-target-info-datasource-set-info**|object|Information of target DS Set|restore_target_info_datasource_set_info|datasourceSetInfo|

#### <a name="BackupInstancesTriggerRestore#AzureBackupRestoreWithRehydrationRequest#ItemLevelRestoreTargetInfo">Command `az dataprotection backup-instance azure-backup-restore-with-rehydration-request item-level-restore-target-info trigger-restore`</a>

##### <a name="ExamplesBackupInstancesTriggerRestore#AzureBackupRestoreWithRehydrationRequest#ItemLevelRestoreTargetInfo">Example</a>
```
az dataprotection backup-instance azure-backup-restore-with-rehydration-request item-level-restore-target-info \
trigger-restore --name "testInstance1" --azurebackuprestorewithrehydrationrequest-recovery-point-id "hardcodedRP" \
--azurebackuprestorewithrehydrationrequest-source-data-store-type "VaultStore" --resource-group "000pikumar" \
--vault-name "PratikPrivatePreviewVault1"
az dataprotection backup-instance azure-backup-restore-with-rehydration-request item-level-restore-target-info \
trigger-restore --name "testInstance1" --azurebackuprestorewithrehydrationrequest-recovery-point-id "hardcodedRP" \
--azurebackuprestorewithrehydrationrequest-source-data-store-type "VaultStore" --resource-group "000pikumar" \
--vault-name "PrivatePreviewVault1"
az dataprotection backup-instance azure-backup-restore-with-rehydration-request item-level-restore-target-info \
trigger-restore --name "testInstance1" --azurebackuprestorewithrehydrationrequest-recovery-point-id "hardcodedRP" \
--azurebackuprestorewithrehydrationrequest-rehydration-priority "High" --azurebackuprestorewithrehydrationrequest-rehyd\
ration-retention-duration "7D" --azurebackuprestorewithrehydrationrequest-source-data-store-type "VaultStore" \
--resource-group "000pikumar" --vault-name "PratikPrivatePreviewVault1"
```
##### <a name="ParametersBackupInstancesTriggerRestore#AzureBackupRestoreWithRehydrationRequest#ItemLevelRestoreTargetInfo">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--vault-name**|string|The name of the backup vault.|vault_name|vaultName|
|**--resource-group-name**|string|The name of the resource group where the backup vault is present.|resource_group_name|resourceGroupName|
|**--backup-instance-name**|string|The name of the backup instance|backup_instance_name|backupInstanceName|
|**--item-level-restore-target-info-restore-criteria**|array|Restore Criteria|item_level_restore_target_info_restore_criteria|restoreCriteria|
|**--item-level-restore-target-info-datasource-info**|object|Information of target DS|item_level_restore_target_info_datasource_info|datasourceInfo|
|**--azurebackuprestorewithrehydrationrequest-source-data-store-type**|choice|Gets or sets the type of the source data store.|azurebackuprestorewithrehydrationrequest_source_data_store_type|sourceDataStoreType|
|**--azurebackuprestorewithrehydrationrequest-recovery-point-id**|string||azurebackuprestorewithrehydrationrequest_recovery_point_id|recoveryPointId|
|**--azurebackuprestorewithrehydrationrequest-rehydration-priority**|choice|Priority to be used for rehydration. Values High or Standard|azurebackuprestorewithrehydrationrequest_rehydration_priority|rehydrationPriority|
|**--azurebackuprestorewithrehydrationrequest-rehydration-retention-duration**|string|Retention duration in ISO 8601 format i.e P10D .|azurebackuprestorewithrehydrationrequest_rehydration_retention_duration|rehydrationRetentionDuration|
|**--item-level-restore-target-info-restore-location**|string|Target Restore region|item_level_restore_target_info_restore_location|restoreLocation|
|**--item-level-restore-target-info-datasource-set-info**|object|Information of target DS Set|item_level_restore_target_info_datasource_set_info|datasourceSetInfo|

#### <a name="BackupInstancesTriggerRestore#AzureBackupRestoreWithRehydrationRequest#RestoreFilesTargetInfo">Command `az dataprotection backup-instance azure-backup-restore-with-rehydration-request restore-files-target-info trigger-restore`</a>

##### <a name="ExamplesBackupInstancesTriggerRestore#AzureBackupRestoreWithRehydrationRequest#RestoreFilesTargetInfo">Example</a>
```
az dataprotection backup-instance azure-backup-restore-with-rehydration-request restore-files-target-info \
trigger-restore --name "testInstance1" --azurebackuprestorewithrehydrationrequest-recovery-point-id "hardcodedRP" \
--azurebackuprestorewithrehydrationrequest-source-data-store-type "VaultStore" --resource-group "000pikumar" \
--vault-name "PratikPrivatePreviewVault1"
az dataprotection backup-instance azure-backup-restore-with-rehydration-request restore-files-target-info \
trigger-restore --name "testInstance1" --azurebackuprestorewithrehydrationrequest-recovery-point-id "hardcodedRP" \
--azurebackuprestorewithrehydrationrequest-source-data-store-type "VaultStore" --resource-group "000pikumar" \
--vault-name "PrivatePreviewVault1"
az dataprotection backup-instance azure-backup-restore-with-rehydration-request restore-files-target-info \
trigger-restore --name "testInstance1" --azurebackuprestorewithrehydrationrequest-recovery-point-id "hardcodedRP" \
--azurebackuprestorewithrehydrationrequest-rehydration-priority "High" --azurebackuprestorewithrehydrationrequest-rehyd\
ration-retention-duration "7D" --azurebackuprestorewithrehydrationrequest-source-data-store-type "VaultStore" \
--resource-group "000pikumar" --vault-name "PratikPrivatePreviewVault1"
```
##### <a name="ParametersBackupInstancesTriggerRestore#AzureBackupRestoreWithRehydrationRequest#RestoreFilesTargetInfo">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--vault-name**|string|The name of the backup vault.|vault_name|vaultName|
|**--resource-group-name**|string|The name of the resource group where the backup vault is present.|resource_group_name|resourceGroupName|
|**--backup-instance-name**|string|The name of the backup instance|backup_instance_name|backupInstanceName|
|**--restore-files-target-info-target-details**|object|Destination of RestoreAsFiles operation, when destination is not a datasource|restore_files_target_info_target_details|targetDetails|
|**--azurebackuprestorewithrehydrationrequest-source-data-store-type**|choice|Gets or sets the type of the source data store.|azurebackuprestorewithrehydrationrequest_source_data_store_type|sourceDataStoreType|
|**--azurebackuprestorewithrehydrationrequest-recovery-point-id**|string||azurebackuprestorewithrehydrationrequest_recovery_point_id|recoveryPointId|
|**--azurebackuprestorewithrehydrationrequest-rehydration-priority**|choice|Priority to be used for rehydration. Values High or Standard|azurebackuprestorewithrehydrationrequest_rehydration_priority|rehydrationPriority|
|**--azurebackuprestorewithrehydrationrequest-rehydration-retention-duration**|string|Retention duration in ISO 8601 format i.e P10D .|azurebackuprestorewithrehydrationrequest_rehydration_retention_duration|rehydrationRetentionDuration|
|**--restore-files-target-info-restore-location**|string|Target Restore region|restore_files_target_info_restore_location|restoreLocation|

#### <a name="BackupInstancesTriggerRestore#AzureBackupRestoreWithRehydrationRequest#RestoreTargetInfo">Command `az dataprotection backup-instance azure-backup-restore-with-rehydration-request restore-target-info trigger-restore`</a>

##### <a name="ExamplesBackupInstancesTriggerRestore#AzureBackupRestoreWithRehydrationRequest#RestoreTargetInfo">Example</a>
```
az dataprotection backup-instance azure-backup-restore-with-rehydration-request restore-target-info trigger-restore \
--name "testInstance1" --azurebackuprestorewithrehydrationrequest-recovery-point-id "hardcodedRP" \
--azurebackuprestorewithrehydrationrequest-source-data-store-type "VaultStore" --resource-group "000pikumar" \
--vault-name "PratikPrivatePreviewVault1"
az dataprotection backup-instance azure-backup-restore-with-rehydration-request restore-target-info trigger-restore \
--name "testInstance1" --azurebackuprestorewithrehydrationrequest-recovery-point-id "hardcodedRP" \
--azurebackuprestorewithrehydrationrequest-source-data-store-type "VaultStore" --resource-group "000pikumar" \
--vault-name "PrivatePreviewVault1"
az dataprotection backup-instance azure-backup-restore-with-rehydration-request restore-target-info trigger-restore \
--name "testInstance1" --azurebackuprestorewithrehydrationrequest-recovery-point-id "hardcodedRP" \
--azurebackuprestorewithrehydrationrequest-rehydration-priority "High" --azurebackuprestorewithrehydrationrequest-rehyd\
ration-retention-duration "7D" --azurebackuprestorewithrehydrationrequest-source-data-store-type "VaultStore" \
--resource-group "000pikumar" --vault-name "PratikPrivatePreviewVault1"
```
##### <a name="ParametersBackupInstancesTriggerRestore#AzureBackupRestoreWithRehydrationRequest#RestoreTargetInfo">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--vault-name**|string|The name of the backup vault.|vault_name|vaultName|
|**--resource-group-name**|string|The name of the resource group where the backup vault is present.|resource_group_name|resourceGroupName|
|**--backup-instance-name**|string|The name of the backup instance|backup_instance_name|backupInstanceName|
|**--restore-target-info-datasource-info**|object|Information of target DS|restore_target_info_datasource_info|datasourceInfo|
|**--azurebackuprestorewithrehydrationrequest-source-data-store-type**|choice|Gets or sets the type of the source data store.|azurebackuprestorewithrehydrationrequest_source_data_store_type|sourceDataStoreType|
|**--azurebackuprestorewithrehydrationrequest-recovery-point-id**|string||azurebackuprestorewithrehydrationrequest_recovery_point_id|recoveryPointId|
|**--azurebackuprestorewithrehydrationrequest-rehydration-priority**|choice|Priority to be used for rehydration. Values High or Standard|azurebackuprestorewithrehydrationrequest_rehydration_priority|rehydrationPriority|
|**--azurebackuprestorewithrehydrationrequest-rehydration-retention-duration**|string|Retention duration in ISO 8601 format i.e P10D .|azurebackuprestorewithrehydrationrequest_rehydration_retention_duration|rehydrationRetentionDuration|
|**--restore-target-info-restore-location**|string|Target Restore region|restore_target_info_restore_location|restoreLocation|
|**--restore-target-info-datasource-set-info**|object|Information of target DS Set|restore_target_info_datasource_set_info|datasourceSetInfo|

#### <a name="BackupInstancesTriggerRehydrate">Command `az dataprotection backup-instance trigger-rehydrate`</a>

##### <a name="ExamplesBackupInstancesTriggerRehydrate">Example</a>
```
az dataprotection backup-instance trigger-rehydrate --name "testInstance1" --recovery-point-id "hardcodedRP" \
--rehydration-priority "High" --rehydration-retention-duration "7D" --resource-group "000pikumar" --vault-name \
"PratikPrivatePreviewVault1"
```
##### <a name="ParametersBackupInstancesTriggerRehydrate">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group where the backup vault is present.|resource_group_name|resourceGroupName|
|**--vault-name**|string|The name of the backup vault.|vault_name|vaultName|
|**--backup-instance-name**|string||backup_instance_name|backupInstanceName|
|**--recovery-point-id**|string|Id of the recovery point to be recovered|recovery_point_id|recoveryPointId|
|**--rehydration-retention-duration**|string|Retention duration in ISO 8601 format i.e P10D .|rehydration_retention_duration|rehydrationRetentionDuration|
|**--rehydration-priority**|choice|Priority to be used for rehydration. Values High or Standard|rehydration_priority|rehydrationPriority|

### group `az dataprotection backup-policy`
#### <a name="BackupPoliciesList">Command `az dataprotection backup-policy list`</a>

##### <a name="ExamplesBackupPoliciesList">Example</a>
```
az dataprotection backup-policy list --resource-group "000pikumar" --vault-name "PrivatePreviewVault"
```
##### <a name="ParametersBackupPoliciesList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--vault-name**|string|The name of the backup vault.|vault_name|vaultName|
|**--resource-group-name**|string|The name of the resource group where the backup vault is present.|resource_group_name|resourceGroupName|

#### <a name="BackupPoliciesGet">Command `az dataprotection backup-policy show`</a>

##### <a name="ExamplesBackupPoliciesGet">Example</a>
```
az dataprotection backup-policy show --name "OSSDBPolicy" --resource-group "000pikumar" --vault-name \
"PrivatePreviewVault"
```
##### <a name="ParametersBackupPoliciesGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--vault-name**|string|The name of the backup vault.|vault_name|vaultName|
|**--resource-group-name**|string|The name of the resource group where the backup vault is present.|resource_group_name|resourceGroupName|
|**--backup-policy-name**|string||backup_policy_name|backupPolicyName|

#### <a name="BackupPoliciesCreateOrUpdate#Create">Command `az dataprotection backup-policy create`</a>

##### <a name="ExamplesBackupPoliciesCreateOrUpdate#Create">Example</a>
```
az dataprotection backup-policy create --name "OSSDBPolicy" --datasource-types "OssDB" --resource-group "000pikumar" \
--vault-name "PrivatePreviewVault"
```
##### <a name="ParametersBackupPoliciesCreateOrUpdate#Create">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--vault-name**|string|The name of the backup vault.|vault_name|vaultName|
|**--resource-group-name**|string|The name of the resource group where the backup vault is present.|resource_group_name|resourceGroupName|
|**--backup-policy-name**|string||backup_policy_name|backupPolicyName|
|**--datasource-types**|array|Type of datasource for the backup management|datasource_types|datasourceTypes|

#### <a name="BackupPoliciesCreateOrUpdate#Update">Command `az dataprotection backup-policy update`</a>


##### <a name="ParametersBackupPoliciesCreateOrUpdate#Update">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--vault-name**|string|The name of the backup vault.|vault_name|vaultName|
|**--resource-group-name**|string|The name of the resource group where the backup vault is present.|resource_group_name|resourceGroupName|
|**--backup-policy-name**|string||backup_policy_name|backupPolicyName|
|**--datasource-types**|array|Type of datasource for the backup management|datasource_types|datasourceTypes|

#### <a name="BackupPoliciesDelete">Command `az dataprotection backup-policy delete`</a>

##### <a name="ExamplesBackupPoliciesDelete">Example</a>
```
az dataprotection backup-policy delete --name "OSSDBPolicy" --resource-group "000pikumar" --vault-name \
"PrivatePreviewVault"
```
##### <a name="ParametersBackupPoliciesDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--vault-name**|string|The name of the backup vault.|vault_name|vaultName|
|**--resource-group-name**|string|The name of the resource group where the backup vault is present.|resource_group_name|resourceGroupName|
|**--backup-policy-name**|string||backup_policy_name|backupPolicyName|

### group `az dataprotection backup-vault`
#### <a name="BackupVaultsGet">Command `az dataprotection backup-vault show`</a>

##### <a name="ExamplesBackupVaultsGet">Example</a>
```
az dataprotection backup-vault show --resource-group "SampleResourceGroup" --vault-name "swaggerExample"
az dataprotection backup-vault show --resource-group "SampleResourceGroup" --vault-name "swaggerExample"
```
##### <a name="ParametersBackupVaultsGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--vault-name**|string|The name of the backup vault.|vault_name|vaultName|
|**--resource-group-name**|string|The name of the resource group where the backup vault is present.|resource_group_name|resourceGroupName|

#### <a name="BackupVaultsCreateOrUpdate#Create">Command `az dataprotection backup-vault create`</a>

##### <a name="ExamplesBackupVaultsCreateOrUpdate#Create">Example</a>
```
az dataprotection backup-vault create --type "None" --location "WestUS" --storage-settings type="LocallyRedundant" \
datastore-type="VaultStore" --tags key1="val1" --resource-group "SampleResourceGroup" --vault-name "swaggerExample"
az dataprotection backup-vault create --type "systemAssigned" --location "WestUS" --storage-settings \
type="LocallyRedundant" datastore-type="VaultStore" --tags key1="val1" --resource-group "SampleResourceGroup" \
--vault-name "swaggerExample"
```
##### <a name="ParametersBackupVaultsCreateOrUpdate#Create">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--vault-name**|string|The name of the backup vault.|vault_name|vaultName|
|**--resource-group-name**|string|The name of the resource group where the backup vault is present.|resource_group_name|resourceGroupName|
|**--e-tag**|string|Optional ETag.|e_tag|eTag|
|**--location**|string|Resource location.|location|location|
|**--tags**|dictionary|Resource tags.|tags|tags|
|**--type**|string|The identityType which can be either SystemAssigned or None|type|type|
|**--storage-settings**|array|Storage Settings|storage_settings|storageSettings|

#### <a name="BackupVaultsCreateOrUpdate#Update">Command `az dataprotection backup-vault update`</a>


##### <a name="ParametersBackupVaultsCreateOrUpdate#Update">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--vault-name**|string|The name of the backup vault.|vault_name|vaultName|
|**--resource-group-name**|string|The name of the resource group where the backup vault is present.|resource_group_name|resourceGroupName|
|**--e-tag**|string|Optional ETag.|e_tag|eTag|
|**--location**|string|Resource location.|location|location|
|**--tags**|dictionary|Resource tags.|tags|tags|
|**--type**|string|The identityType which can be either SystemAssigned or None|type|type|
|**--storage-settings**|array|Storage Settings|storage_settings|storageSettings|

#### <a name="BackupVaultsDelete">Command `az dataprotection backup-vault delete`</a>

##### <a name="ExamplesBackupVaultsDelete">Example</a>
```
az dataprotection backup-vault delete --resource-group "SampleResourceGroup" --vault-name "swaggerExample"
```
##### <a name="ParametersBackupVaultsDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--vault-name**|string|The name of the backup vault.|vault_name|vaultName|
|**--resource-group-name**|string|The name of the resource group where the backup vault is present.|resource_group_name|resourceGroupName|

#### <a name="BackupVaultsPatch">Command `az dataprotection backup-vault patch`</a>

##### <a name="ExamplesBackupVaultsPatch">Example</a>
```
az dataprotection backup-vault patch --tags newKey="newVal" --resource-group "SampleResourceGroup" --vault-name \
"swaggerExample"
```
##### <a name="ParametersBackupVaultsPatch">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--vault-name**|string|The name of the backup vault.|vault_name|vaultName|
|**--resource-group-name**|string|The name of the resource group where the backup vault is present.|resource_group_name|resourceGroupName|
|**--tags**|dictionary|Resource tags.|tags|tags|
|**--type**|string|The identityType which can be either SystemAssigned or None|type|type|

#### <a name="BackupVaultsGetResourcesInResourceGroup">Command `az dataprotection backup-vault show-resource-in-resource-group`</a>

##### <a name="ExamplesBackupVaultsGetResourcesInResourceGroup">Example</a>
```
az dataprotection backup-vault show-resource-in-resource-group --resource-group "SampleResourceGroup"
```
##### <a name="ParametersBackupVaultsGetResourcesInResourceGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group where the backup vault is present.|resource_group_name|resourceGroupName|

#### <a name="BackupVaultsGetResourcesInSubscription">Command `az dataprotection backup-vault show-resource-in-subscription`</a>

##### <a name="ExamplesBackupVaultsGetResourcesInSubscription">Example</a>
```
az dataprotection backup-vault show-resource-in-subscription
```
##### <a name="ParametersBackupVaultsGetResourcesInSubscription">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|

### group `az dataprotection job`
#### <a name="JobsList">Command `az dataprotection job list`</a>

##### <a name="ExamplesJobsList">Example</a>
```
az dataprotection job list --resource-group "BugBash1" --vault-name "BugBashVaultForCCYv11"
```
##### <a name="ParametersJobsList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group where the backup vault is present.|resource_group_name|resourceGroupName|
|**--vault-name**|string|The name of the backup vault.|vault_name|vaultName|

### group `az dataprotection job`
#### <a name="JobGet">Command `az dataprotection job show`</a>

##### <a name="ExamplesJobGet">Example</a>
```
az dataprotection job show --job-id "3c60cb49-63e8-4b21-b9bd-26277b3fdfae" --resource-group "BugBash1" --vault-name \
"BugBashVaultForCCYv11"
```
##### <a name="ParametersJobGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group where the backup vault is present.|resource_group_name|resourceGroupName|
|**--vault-name**|string|The name of the backup vault.|vault_name|vaultName|
|**--job-id**|string|The Job ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).|job_id|jobId|

### group `az dataprotection recovery-point`
#### <a name="RecoveryPointsGetList">Command `az dataprotection recovery-point show-list`</a>

##### <a name="ExamplesRecoveryPointsGetList">Example</a>
```
az dataprotection recovery-point show-list --backup-instance-name "testInstance1" --resource-group "000pikumar" \
--vault-name "PratikPrivatePreviewVault1"
```
##### <a name="ParametersRecoveryPointsGetList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--vault-name**|string|The name of the backup vault.|vault_name|vaultName|
|**--resource-group-name**|string|The name of the resource group where the backup vault is present.|resource_group_name|resourceGroupName|
|**--backup-instance-name**|string|The name of the backup instance|backup_instance_name|backupInstanceName|
|**--filter**|string|OData filter options.|filter|$filter|
|**--skip-token**|string|skipToken Filter.|skip_token|$skipToken|

### group `az dataprotection recovery-point`
#### <a name="RecoveryPointGet">Command `az dataprotection recovery-point show`</a>

##### <a name="ExamplesRecoveryPointGet">Example</a>
```
az dataprotection recovery-point show --backup-instance-name "testInstance1" --recovery-point-id \
"7fb2cddd-c5b3-44f6-a0d9-db3c4f9d5f25" --resource-group "000pikumar" --vault-name "PratikPrivatePreviewVault1"
```
##### <a name="ParametersRecoveryPointGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--vault-name**|string|The name of the backup vault.|vault_name|vaultName|
|**--resource-group-name**|string|The name of the resource group where the backup vault is present.|resource_group_name|resourceGroupName|
|**--backup-instance-name**|string|The name of the backup instance|backup_instance_name|backupInstanceName|
|**--recovery-point-id**|string||recovery_point_id|recoveryPointId|
