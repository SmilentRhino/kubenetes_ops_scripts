import json

KUBE_SWAGGER = ''
with open('swagger.json', 'r') as f:
    KUBE_SWAGGER = json.load(f)

def api_mapping(self, manifest):
    api_version = manifest['apiVersion'].split('/')
    api_func_name = ''
    list_func_name = ''
    manifest_type = ''
     if 'apps' == api_version[0]:
         api_func_name = ''.join(i.capitalize() for i in api_version) + 'Api'
     elif 'v1' == api_version[0]:
         api_func_name = 'CoreV1Api'
     elif 'extension' == api_version[0]:
         api_func_name = ''.join(i.capitalize() for i in api_version) + 'Api'
    if 'v1' == api_version[0]:
        api_func_name = 'CoreV1Api'
        if 'namespace' not in manifest['metadata']:
            list_func_path = '/api/' + manifest['apiVersion'].lower() + '/' + manifest['kind'].lower() + 's'
            logging.debug(list_func_path)
            list_func_operation = KUBE_SWAGGER['paths'][list_func_path]['get']['operationId']
            list_func_name = re.sub('([A-Z]+)', r'_\1', list_func_operation).lower()
            create_func_path = '/api/' + manifest['apiVersion'].lower() + '/' + manifest['kind'].lower() + 's'
            create_func_operation = KUBE_SWAGGER['paths'][create_func_path]['post']['operationId']
            create_func_name = re.sub('([A-Z]+)', r'_\1', create_func_operation).lower()
            read_func_path = '/api/' + manifest['apiVersion'].lower() + '/' + manifest['kind'].lower() + 's' + '/{name}'
            read_func_operation = KUBE_SWAGGER['paths'][read_func_path]['get']['operationId']
            read_func_name = re.sub('([A-Z]+)', r'_\1', read_func_operation).lower()
            update_func_path = '/api/' + manifest['apiVersion'].lower() + '/' + manifest['kind'].lower() + 's' + '/{name}'
            update_func_operation = KUBE_SWAGGER['paths'][update_func_path]['put']['operationId']
            update_func_name = re.sub('([A-Z]+)', r'_\1', update_func_operation).lower()

            my_ref = KUBE_SWAGGER['paths'][read_func_path]['get']['responses']['200']['schema']['$ref'].split('/')[-1]
            for i in my_ref.split('.'):
                manifest_type += i[0].upper() + i[1:]

        else:
            list_func_path = '/api/' + manifest['apiVersion'].lower() + '/namespaces/{namespace}/' + manifest['kind'].lower() + 's'
            logging.debug(list_func_path)
            list_func_operation = KUBE_SWAGGER['paths'][list_func_path]['get']['operationId']
            list_func_name = re.sub('([A-Z]+)', r'_\1', list_func_operation).lower()
            create_func_path = '/api/' + manifest['apiVersion'].lower() + '/namespaces/{namespace}/' + manifest['kind'].lower() + 's'
            create_func_operation = KUBE_SWAGGER['paths'][create_func_path]['post']['operationId']
            create_func_name = re.sub('([A-Z]+)', r'_\1', create_func_operation).lower()
            read_func_path = '/api/' + manifest['apiVersion'].lower() + '/namespaces/{namespace}/' + manifest['kind'].lower() + 's' + '/{name}'
            read_func_operation = KUBE_SWAGGER['paths'][read_func_path]['get']['operationId']
            read_func_name = re.sub('([A-Z]+)', r'_\1', read_func_operation).lower()
            update_func_path = '/api/' + manifest['apiVersion'].lower() + '/namespaces/{namespace}/' + manifest['kind'].lower() + 's' + '/{name}'
            update_func_operation = KUBE_SWAGGER['paths'][update_func_path]['put']['operationId']
            update_func_name = re.sub('([A-Z]+)', r'_\1', update_func_operation).lower()

            my_ref = KUBE_SWAGGER['paths'][read_func_path]['get']['responses']['200']['schema']['$ref'].split('/')[-1]
            for i in my_ref.split('.'):
                manifest_type += i[0].upper() + i[1:]


    else:
        api_func_path = '/apis/' + manifest['apiVersion'].lower() + '/'
        api_func_tags = KUBE_SWAGGER['paths'][api_func_path]['get']['tags']
        logging.info('%s', api_func_tags[0])
        for i in api_func_tags[0].split('_'):
            api_func_name += i[0].upper() + i[1:]
        api_func_name += 'Api'
        #api_func_name = ''.join(i.capitalize() for i in api_version) + 'Api'
        if 'namespace' not in manifest['metadata']:
            list_func_path = '/apis/' + manifest['apiVersion'].lower() + '/' + manifest['kind'].lower() + 's'
            logging.debug(list_func_path)
            list_func_operation = KUBE_SWAGGER['paths'][list_func_path]['get']['operationId']
            list_func_name = re.sub('([A-Z]+)', r'_\1', list_func_operation).lower()
            create_func_path = '/apis/' + manifest['apiVersion'].lower() + '/' + manifest['kind'].lower() + 's'
            create_func_operation = KUBE_SWAGGER['paths'][create_func_path]['post']['operationId']
            create_func_name = re.sub('([A-Z]+)', r'_\1', create_func_operation).lower()
            read_func_path = '/apis/' + manifest['apiVersion'].lower() + '/' + manifest['kind'].lower() + 's' + '/{name}'
            read_func_operation = KUBE_SWAGGER['paths'][read_func_path]['get']['operationId']
            read_func_name = re.sub('([A-Z]+)', r'_\1', read_func_operation).lower()
            update_func_path = '/apis/' + manifest['apiVersion'].lower() + '/' + manifest['kind'].lower() + 's' + '/{name}'
            update_func_operation = KUBE_SWAGGER['paths'][update_func_path]['put']['operationId']
            update_func_name = re.sub('([A-Z]+)', r'_\1', update_func_operation).lower()

            my_ref = KUBE_SWAGGER['paths'][read_func_path]['get']['responses']['200']['schema']['$ref'].split('/')[-1]
            for i in my_ref.split('.'):
                manifest_type += i[0].upper() + i[1:]
        else:
            list_func_path = '/apis/' + manifest['apiVersion'].lower() + '/namespaces/{namespace}/' + manifest['kind'].lower() + 's'
            logging.debug(list_func_path)
            list_func_operation = KUBE_SWAGGER['paths'][list_func_path]['get']['operationId']
            list_func_name = re.sub('([A-Z]+)', r'_\1', list_func_operation).lower()
            create_func_path = '/apis/' + manifest['apiVersion'].lower() + '/namespaces/{namespace}/' + manifest['kind'].lower() + 's'
            create_func_operation = KUBE_SWAGGER['paths'][create_func_path]['post']['operationId']
            create_func_name = re.sub('([A-Z]+)', r'_\1', create_func_operation).lower()
            read_func_path = '/apis/' + manifest['apiVersion'].lower() + '/namespaces/{namespace}/' + manifest['kind'].lower() + 's' + '/{name}'
            read_func_operation = KUBE_SWAGGER['paths'][read_func_path]['get']['operationId']
            read_func_name = re.sub('([A-Z]+)', r'_\1', read_func_operation).lower()
            update_func_path = '/apis/' + manifest['apiVersion'].lower() + '/namespaces/{namespace}/' + manifest['kind'].lower() + 's' + '/{name}'
            update_func_operation = KUBE_SWAGGER['paths'][update_func_path]['put']['operationId']
            update_func_name = re.sub('([A-Z]+)', r'_\1', update_func_operation).lower()

            my_ref = KUBE_SWAGGER['paths'][read_func_path]['get']['responses']['200']['schema']['$ref'].split('/')[-1]
            for i in my_ref.split('.'):
                manifest_type += i[0].upper() + i[1:]


    logging.info('Api func name %s', api_func_name)

    print(api_func_name, list_func_name, create_func_name, read_func_name, manifest_type,  update_func_name)
    return (api_func_name, list_func_name, create_func_name, read_func_name, manifest_type,  update_func_name)

def create_manifest(self, manifest):
    created = False
    my_api_name = self.api_mapping(manifest)
    api_func_name, list_func_name, create_func_name = my_api_name[0], my_api_name[1], my_api_name[2]
    api_instance = getattr(client,api_func_name)(self.cluster_client.api_client)
    logging.info(create_func_name)
    if 'namespace' not in manifest['metadata']:
        create_result = getattr(api_instance, create_func_name)(body=manifest)
    else:
        create_result = getattr(api_instance, create_func_name)(manifest['metadata']['namespace'], body=manifest)
    logging.info(create_result)
    return created
