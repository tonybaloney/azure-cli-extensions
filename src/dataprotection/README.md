# Azure CLI dataprotection Extension #
This is the extension for dataprotection

### How to use ###
Install this extension using the below CLI command
```
az extension add --name dataprotection
```

### Included Features ###
#### dataprotection backup-vault ####
##### Create #####
```
az dataprotection backup-vault create --type "None" --location "WestUS" \
    --storage-settings type="LocallyRedundant" datastore-type="VaultStore" --tags key1="val1" \
    --resource-group "SampleResourceGroup" --vault-name "swaggerExample" 
```
##### Create #####
```
az dataprotection backup-vault create --type "systemAssigned" --location "WestUS" \
    --storage-settings type="LocallyRedundant" datastore-type="VaultStore" --tags key1="val1" \
    --resource-group "SampleResourceGroup" --vault-name "swaggerExample" 
```
##### Show #####
```
az dataprotection backup-vault show --resource-group "SampleResourceGroup" --vault-name "swaggerExample"
```
##### Show #####
```
az dataprotection backup-vault show --resource-group "SampleResourceGroup" --vault-name "swaggerExample"
```
##### Patch #####
```
az dataprotection backup-vault patch --tags newKey="newVal" --resource-group "SampleResourceGroup" \
    --vault-name "swaggerExample" 
```
##### Show-resource-in-resource-group #####
```
az dataprotection backup-vault show-resource-in-resource-group --resource-group "SampleResourceGroup"
```
##### Show-resource-in-subscription #####
```
az dataprotection backup-vault show-resource-in-subscription
```
##### Delete #####
```
az dataprotection backup-vault delete --resource-group "SampleResourceGroup" --vault-name "swaggerExample"
```
#### dataprotection ####
##### Check-feature-support #####
```
az dataprotection check-feature-support --location "WestUS" --feature-validation-request feature-type="DataSourceType"
```
##### Show-operation-result-patch #####
```
az dataprotection show-operation-result-patch \
    --operation-id "YWUzNDFkMzQtZmM5OS00MmUyLWEzNDMtZGJkMDIxZjlmZjgzOzdmYzBiMzhmLTc2NmItNDM5NS05OWQ1LTVmOGEzNzg4MWQzNA==" \
    --resource-group "SampleResourceGroup" --vault-name "swaggerExample" 
```
##### Show-operation-status #####
```
az dataprotection show-operation-status \
    --operation-id "MjkxOTMyODMtYTE3My00YzJjLTg5NjctN2E4MDIxNDA3NjA2OzdjNGE2ZWRjLWJjMmItNDRkYi1hYzMzLWY1YzEwNzk5Y2EyOA==" \
    --location "WestUS" 
```
#### dataprotection backup-policy ####
##### Create #####
```
az dataprotection backup-policy create --name "OSSDBPolicy" --datasource-types "OssDB" --resource-group "000pikumar" \
    --vault-name "PrivatePreviewVault" 
```
##### Show #####
```
az dataprotection backup-policy show --name "OSSDBPolicy" --resource-group "000pikumar" \
    --vault-name "PrivatePreviewVault" 
```
##### List #####
```
az dataprotection backup-policy list --resource-group "000pikumar" --vault-name "PrivatePreviewVault"
```
##### Delete #####
```
az dataprotection backup-policy delete --name "OSSDBPolicy" --resource-group "000pikumar" \
    --vault-name "PrivatePreviewVault" 
```
#### dataprotection backup-instance ####
##### Create #####
```
az dataprotection backup-instance create --name "testInstance1" \
    --data-source-info datasource-type="OssDB" object-type="Datasource" resource-id="/subscriptions/f75d8d8b-6735-4697-82e1-1a7a3ff0d5d4/resourceGroups/viveksipgtest/providers/Microsoft.DBforPostgreSQL/servers/viveksipgtest/databases/testdb" resource-location="" resource-name="testdb" resource-type="Microsoft.DBforPostgreSQL/servers/databases" resource-uri="" \
    --data-source-set-info datasource-type="OssDB" object-type="DatasourceSet" resource-id="/subscriptions/f75d8d8b-6735-4697-82e1-1a7a3ff0d5d4/resourceGroups/viveksipgtest/providers/Microsoft.DBforPostgreSQL/servers/viveksipgtest" resource-location="" resource-name="viveksipgtest" resource-type="Microsoft.DBforPostgreSQL/servers" resource-uri="" \
    --friendly-name "harshitbi2" --object-type "BackupInstance" \
    --policy-id "/subscriptions/04cf684a-d41f-4550-9f70-7708a3a2283b/resourceGroups/000pikumar/providers/Microsoft.DataProtection/Backupvaults/PratikPrivatePreviewVault1/backupPolicies/PratikPolicy1" \
    --policy-parameters data-store-parameters-list={"dataStoreType":"OperationalStore","objectType":"AzureOperationalStoreParameters","resourceGroupId":"/subscriptions/f75d8d8b-6735-4697-82e1-1a7a3ff0d5d4/resourceGroups/viveksipgtest"} \
    --resource-group "000pikumar" --vault-name "PratikPrivatePreviewVault1" 

az dataprotection backup-instance wait --created --name "{myBackupInstance}" --resource-group "{rg_2}" \
    --vault-name "{myBackupVault}" 
```
##### Show #####
```
az dataprotection backup-instance show --name "testInstance1" --resource-group "000pikumar" \
    --vault-name "PratikPrivatePreviewVault1" 
```
##### List #####
```
az dataprotection backup-instance list --resource-group "000pikumar" --vault-name "PratikPrivatePreviewVault1"
```
##### Adhoc-backup #####
```
az dataprotection backup-instance adhoc-backup --name "testInstance1" --rule-name "BackupWeekly" \
    --retention-tag-override "yearly" --resource-group "000pikumar" --vault-name "PratikPrivatePreviewVault1" 
```
##### Azure-backup-recovery-point-based-restore-request azure-backup-restore-with-rehydration-request trigger-restore #####
```
\
    az dataprotection backup-instance azure-backup-recovery-point-based-restore-request azure-backup-restore-with-rehydration-request trigger-restore \
    --name "testInstance1" --azurebackuprecoverypointbasedrestorerequest-recovery-point-id "hardcodedRP" \
    --azurebackuprecoverypointbasedrestorerequest-restore-target-info "{\\"datasourceInfo\\":{\\"datasourceType\\":\\"OssDB\\",\\"objectType\\":\\"Datasource\\",\\"resourceID\\":\\"/subscriptions/f75d8d8b-6735-4697-82e1-1a7a3ff0d5d4/resourceGroups/viveksipgtest/providers/Microsoft.DBforPostgreSQL/servers/viveksipgtest/databases/testdb\\",\\"resourceLocation\\":\\"\\",\\"resourceName\\":\\"testdb\\",\\"resourceType\\":\\"Microsoft.DBforPostgreSQL/servers/databases\\",\\"resourceUri\\":\\"\\"},\\"datasourceSetInfo\\":{\\"datasourceType\\":\\"OssDB\\",\\"objectType\\":\\"DatasourceSet\\",\\"resourceID\\":\\"/subscriptions/f75d8d8b-6735-4697-82e1-1a7a3ff0d5d4/resourceGroups/viveksipgtest/providers/Microsoft.DBforPostgreSQL/servers/viveksipgtest\\",\\"resourceLocation\\":\\"\\",\\"resourceName\\":\\"viveksipgtest\\",\\"resourceType\\":\\"Microsoft.DBforPostgreSQL/servers\\",\\"resourceUri\\":\\"\\"},\\"objectType\\":\\"RestoreTargetInfo\\",\\"recoveryOption\\":\\"FailIfExists\\",\\"restoreLocation\\":\\"southeastasia\\"}" \
    --azurebackuprecoverypointbasedrestorerequest-source-data-store-type "VaultStore" --resource-group "000pikumar" \
    --vault-name "PratikPrivatePreviewVault1" 
```
##### Azure-backup-recovery-point-based-restore-request azure-backup-restore-with-rehydration-request trigger-restore #####
```
\
    az dataprotection backup-instance azure-backup-recovery-point-based-restore-request azure-backup-restore-with-rehydration-request trigger-restore \
    --name "testInstance1" --azurebackuprecoverypointbasedrestorerequest-recovery-point-id "hardcodedRP" \
    --azurebackuprecoverypointbasedrestorerequest-restore-target-info "{\\"objectType\\":\\"RestoreFilesTargetInfo\\",\\"recoveryOption\\":\\"FailIfExists\\",\\"restoreLocation\\":\\"southeastasia\\",\\"targetDetails\\":{\\"filePrefix\\":\\"restoredblob\\",\\"restoreTargetLocationType\\":\\"AzureBlobs\\",\\"url\\":\\"https://teststorage.blob.core.windows.net/restoretest\\"}}" \
    --azurebackuprecoverypointbasedrestorerequest-source-data-store-type "VaultStore" --resource-group "000pikumar" \
    --vault-name "PrivatePreviewVault1" 
```
##### Azure-backup-recovery-point-based-restore-request azure-backup-restore-with-rehydration-request trigger-restore #####
```
\
    az dataprotection backup-instance azure-backup-recovery-point-based-restore-request azure-backup-restore-with-rehydration-request trigger-restore \
    --name "testInstance1" --azurebackuprecoverypointbasedrestorerequest-recovery-point-id "hardcodedRP" \
    --azurebackuprecoverypointbasedrestorerequest-restore-target-info "{\\"datasourceInfo\\":{\\"datasourceType\\":\\"OssDB\\",\\"objectType\\":\\"Datasource\\",\\"resourceID\\":\\"/subscriptions/f75d8d8b-6735-4697-82e1-1a7a3ff0d5d4/resourceGroups/viveksipgtest/providers/Microsoft.DBforPostgreSQL/servers/viveksipgtest/databases/testdb\\",\\"resourceLocation\\":\\"\\",\\"resourceName\\":\\"testdb\\",\\"resourceType\\":\\"Microsoft.DBforPostgreSQL/servers/databases\\",\\"resourceUri\\":\\"\\"},\\"datasourceSetInfo\\":{\\"datasourceType\\":\\"OssDB\\",\\"objectType\\":\\"DatasourceSet\\",\\"resourceID\\":\\"/subscriptions/f75d8d8b-6735-4697-82e1-1a7a3ff0d5d4/resourceGroups/viveksipgtest/providers/Microsoft.DBforPostgreSQL/servers/viveksipgtest\\",\\"resourceLocation\\":\\"\\",\\"resourceName\\":\\"viveksipgtest\\",\\"resourceType\\":\\"Microsoft.DBforPostgreSQL/servers\\",\\"resourceUri\\":\\"\\"},\\"objectType\\":\\"RestoreTargetInfo\\",\\"recoveryOption\\":\\"FailIfExists\\",\\"restoreLocation\\":\\"southeastasia\\"}" \
    --azurebackuprecoverypointbasedrestorerequest-source-data-store-type "VaultStore" --resource-group "000pikumar" \
    --vault-name "PratikPrivatePreviewVault1" 
```
##### Azure-backup-recovery-time-based-restore-request item-level-restore-target-info trigger-restore #####
```
\
    az dataprotection backup-instance azure-backup-recovery-time-based-restore-request item-level-restore-target-info trigger-restore \
    --name "testInstance1" --azurebackuprecoverytimebasedrestorerequest-source-data-store-type "VaultStore" \
    --resource-group "000pikumar" --vault-name "PratikPrivatePreviewVault1" 
```
##### Azure-backup-recovery-time-based-restore-request item-level-restore-target-info trigger-restore #####
```
\
    az dataprotection backup-instance azure-backup-recovery-time-based-restore-request item-level-restore-target-info trigger-restore \
    --name "testInstance1" --azurebackuprecoverytimebasedrestorerequest-source-data-store-type "VaultStore" \
    --resource-group "000pikumar" --vault-name "PrivatePreviewVault1" 
```
##### Azure-backup-recovery-time-based-restore-request item-level-restore-target-info trigger-restore #####
```
\
    az dataprotection backup-instance azure-backup-recovery-time-based-restore-request item-level-restore-target-info trigger-restore \
    --name "testInstance1" --azurebackuprecoverytimebasedrestorerequest-source-data-store-type "VaultStore" \
    --resource-group "000pikumar" --vault-name "PratikPrivatePreviewVault1" 
```
##### Azure-backup-recovery-time-based-restore-request restore-files-target-info trigger-restore #####
```
\
    az dataprotection backup-instance azure-backup-recovery-time-based-restore-request restore-files-target-info trigger-restore \
    --name "testInstance1" --azurebackuprecoverytimebasedrestorerequest-source-data-store-type "VaultStore" \
    --resource-group "000pikumar" --vault-name "PratikPrivatePreviewVault1" 
```
##### Azure-backup-recovery-time-based-restore-request restore-files-target-info trigger-restore #####
```
\
    az dataprotection backup-instance azure-backup-recovery-time-based-restore-request restore-files-target-info trigger-restore \
    --name "testInstance1" --azurebackuprecoverytimebasedrestorerequest-source-data-store-type "VaultStore" \
    --resource-group "000pikumar" --vault-name "PrivatePreviewVault1" 
```
##### Azure-backup-recovery-time-based-restore-request restore-files-target-info trigger-restore #####
```
\
    az dataprotection backup-instance azure-backup-recovery-time-based-restore-request restore-files-target-info trigger-restore \
    --name "testInstance1" --azurebackuprecoverytimebasedrestorerequest-source-data-store-type "VaultStore" \
    --resource-group "000pikumar" --vault-name "PratikPrivatePreviewVault1" 
```
##### Azure-backup-recovery-time-based-restore-request restore-target-info trigger-restore #####
```
az dataprotection backup-instance azure-backup-recovery-time-based-restore-request restore-target-info trigger-restore \
    --name "testInstance1" --azurebackuprecoverytimebasedrestorerequest-source-data-store-type "VaultStore" \
    --resource-group "000pikumar" --vault-name "PratikPrivatePreviewVault1" 
```
##### Azure-backup-recovery-time-based-restore-request restore-target-info trigger-restore #####
```
az dataprotection backup-instance azure-backup-recovery-time-based-restore-request restore-target-info trigger-restore \
    --name "testInstance1" --azurebackuprecoverytimebasedrestorerequest-source-data-store-type "VaultStore" \
    --resource-group "000pikumar" --vault-name "PrivatePreviewVault1" 
```
##### Azure-backup-recovery-time-based-restore-request restore-target-info trigger-restore #####
```
az dataprotection backup-instance azure-backup-recovery-time-based-restore-request restore-target-info trigger-restore \
    --name "testInstance1" --azurebackuprecoverytimebasedrestorerequest-source-data-store-type "VaultStore" \
    --resource-group "000pikumar" --vault-name "PratikPrivatePreviewVault1" 
```
##### Azure-backup-restore-with-rehydration-request trigger-restore #####
```
az dataprotection backup-instance azure-backup-restore-with-rehydration-request trigger-restore --name "testInstance1" \
    --recovery-point-id "hardcodedRP" \
    --restore-target-info "{\\"datasourceInfo\\":{\\"datasourceType\\":\\"OssDB\\",\\"objectType\\":\\"Datasource\\",\\"resourceID\\":\\"/subscriptions/f75d8d8b-6735-4697-82e1-1a7a3ff0d5d4/resourceGroups/viveksipgtest/providers/Microsoft.DBforPostgreSQL/servers/viveksipgtest/databases/testdb\\",\\"resourceLocation\\":\\"\\",\\"resourceName\\":\\"testdb\\",\\"resourceType\\":\\"Microsoft.DBforPostgreSQL/servers/databases\\",\\"resourceUri\\":\\"\\"},\\"datasourceSetInfo\\":{\\"datasourceType\\":\\"OssDB\\",\\"objectType\\":\\"DatasourceSet\\",\\"resourceID\\":\\"/subscriptions/f75d8d8b-6735-4697-82e1-1a7a3ff0d5d4/resourceGroups/viveksipgtest/providers/Microsoft.DBforPostgreSQL/servers/viveksipgtest\\",\\"resourceLocation\\":\\"\\",\\"resourceName\\":\\"viveksipgtest\\",\\"resourceType\\":\\"Microsoft.DBforPostgreSQL/servers\\",\\"resourceUri\\":\\"\\"},\\"objectType\\":\\"RestoreTargetInfo\\",\\"recoveryOption\\":\\"FailIfExists\\",\\"restoreLocation\\":\\"southeastasia\\"}" \
    --source-data-store-type "VaultStore" --resource-group "000pikumar" --vault-name "PratikPrivatePreviewVault1" 
```
##### Azure-backup-restore-with-rehydration-request trigger-restore #####
```
az dataprotection backup-instance azure-backup-restore-with-rehydration-request trigger-restore --name "testInstance1" \
    --recovery-point-id "hardcodedRP" \
    --restore-target-info "{\\"objectType\\":\\"RestoreFilesTargetInfo\\",\\"recoveryOption\\":\\"FailIfExists\\",\\"restoreLocation\\":\\"southeastasia\\",\\"targetDetails\\":{\\"filePrefix\\":\\"restoredblob\\",\\"restoreTargetLocationType\\":\\"AzureBlobs\\",\\"url\\":\\"https://teststorage.blob.core.windows.net/restoretest\\"}}" \
    --source-data-store-type "VaultStore" --resource-group "000pikumar" --vault-name "PrivatePreviewVault1" 
```
##### Azure-backup-restore-with-rehydration-request trigger-restore #####
```
az dataprotection backup-instance azure-backup-restore-with-rehydration-request trigger-restore --name "testInstance1" \
    --recovery-point-id "hardcodedRP" --rehydration-priority "High" --rehydration-retention-duration "7D" \
    --restore-target-info "{\\"datasourceInfo\\":{\\"datasourceType\\":\\"OssDB\\",\\"objectType\\":\\"Datasource\\",\\"resourceID\\":\\"/subscriptions/f75d8d8b-6735-4697-82e1-1a7a3ff0d5d4/resourceGroups/viveksipgtest/providers/Microsoft.DBforPostgreSQL/servers/viveksipgtest/databases/testdb\\",\\"resourceLocation\\":\\"\\",\\"resourceName\\":\\"testdb\\",\\"resourceType\\":\\"Microsoft.DBforPostgreSQL/servers/databases\\",\\"resourceUri\\":\\"\\"},\\"datasourceSetInfo\\":{\\"datasourceType\\":\\"OssDB\\",\\"objectType\\":\\"DatasourceSet\\",\\"resourceID\\":\\"/subscriptions/f75d8d8b-6735-4697-82e1-1a7a3ff0d5d4/resourceGroups/viveksipgtest/providers/Microsoft.DBforPostgreSQL/servers/viveksipgtest\\",\\"resourceLocation\\":\\"\\",\\"resourceName\\":\\"viveksipgtest\\",\\"resourceType\\":\\"Microsoft.DBforPostgreSQL/servers\\",\\"resourceUri\\":\\"\\"},\\"objectType\\":\\"RestoreTargetInfo\\",\\"recoveryOption\\":\\"FailIfExists\\",\\"restoreLocation\\":\\"southeastasia\\"}" \
    --source-data-store-type "VaultStore" --resource-group "000pikumar" --vault-name "PratikPrivatePreviewVault1" 
```
##### Trigger-rehydrate #####
```
az dataprotection backup-instance trigger-rehydrate --name "testInstance1" --recovery-point-id "hardcodedRP" \
    --rehydration-priority "High" --rehydration-retention-duration "7D" --resource-group "000pikumar" \
    --vault-name "PratikPrivatePreviewVault1" 
```
##### Delete #####
```
az dataprotection backup-instance delete --name "testInstance1" --resource-group "000pikumar" \
    --vault-name "PratikPrivatePreviewVault1" 
```
#### dataprotection recovery-point ####
##### Show-list #####
```
az dataprotection recovery-point show-list --backup-instance-name "testInstance1" --resource-group "000pikumar" \
    --vault-name "PratikPrivatePreviewVault1" 
```
#### dataprotection recovery-point ####
##### Show #####
```
az dataprotection recovery-point show --backup-instance-name "testInstance1" \
    --recovery-point-id "7fb2cddd-c5b3-44f6-a0d9-db3c4f9d5f25" --resource-group "000pikumar" \
    --vault-name "PratikPrivatePreviewVault1" 
```
#### dataprotection job ####
##### List #####
```
az dataprotection job list --resource-group "BugBash1" --vault-name "BugBashVaultForCCYv11"
```
#### dataprotection job ####
##### Show #####
```
az dataprotection job show --job-id "3c60cb49-63e8-4b21-b9bd-26277b3fdfae" --resource-group "BugBash1" \
    --vault-name "BugBashVaultForCCYv11" 
```