BUILD_CONF='workflows/cloudbuild_template.yaml'
REPO_NAME="voice"
REPO_OWNER="vik-vok"

# cloud-func-name | py_func_name | dir
array=(
  'voice-original-get-all':'original_voice_get_all':'functions/original/all'
  'voice-original-create':'original_voice_create':'functions/original/create'
  'voice-original-delete':'original_voice_delete':'functions/original/id/delete'
  'voice-original-get':'original_voice_get':'functions/original/id/get'
  'voice-original-update':'original_voice_update':'functions/original/id/update'

  'voice-recorded-get-all':'recorded_voice_get_all':'functions/recorded/all'
  'voice-recorded-create':'recorded_voice_create':'functions/recorded/create'
  'voice-recorded-delete':'recorded_voice_delete':'functions/recorded/id/delete'
  'voice-recorded-get':'recorded_voice_get':'functions/recorded/id/get'
)

for i in "${array[@]}"; do
  IFS=":"
  set -- ${i}

  CLOUD_FUNC_NAME=${1}
  PY_FUNC_NAME=${2}
  DIR=${3}
  TRIGGER_NAME="${CLOUD_FUNC_NAME}-trigger"
  echo "#### Generating Trigger ${TRIGGER_NAME}"

  gcloud alpha builds triggers delete "${TRIGGER_NAME}" --quiet
  gcloud beta builds triggers create github \
    --repo-name="${REPO_NAME}" \
    --repo-owner="${REPO_OWNER}" \
    --included-files="${DIR}/*" \
    --name="${TRIGGER_NAME}" \
    --branch-pattern="^master$" \
    --build-config=${BUILD_CONF} \
    --substitutions _CLOUD_FUNC_NAME="${CLOUD_FUNC_NAME}",_PY_FUNC_NAME="${PY_FUNC_NAME}",_DIR="${DIR}"
done
