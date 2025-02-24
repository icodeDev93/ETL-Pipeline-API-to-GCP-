from googleapiclient.discovery import build

def trigger_df_job(cloud_event,environment):

    service = build('dataflow', 'v1b3')
    project = "data-pipeline-1-437112"

    template_path = 'gs://dataflow-templates-us-central1/latest/GCS_Text_to_BigQuery'

    template_body = {
        "jobName" : "bq-load", # Provide a unique name for the job
        "parameters": {
            "javascriptTextTransformGcsPath": "gs://bucket-dataflow-metadata-1/udf.js",
            "JSONPath": "gs://bucket-dataflow-metadata-1/bq.json",
            "javascriptTextTransformFunctionName": "transform",
            "outputTable": "data-pipeline-1-437112:cricket_dataset.icc_odi_batsman_ranking",
            "inputFilePattern": "gs://bucket-cricket/batsmen_ranking.csv",
            "bigQueryLoadingTemporaryDirectory": "gs://bucket-dataflow-metadata-1"
        }
    }

    request = service.projects().templates().launch(projectId=project, gcsPath=template_path, body=template_body)
    response = request.execute()
    print(response)