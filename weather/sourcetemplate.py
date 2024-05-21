def sourcetemplate(url: str):
    """Returns function that connects given params"""
    def get_query(**params) -> str:
        """Properly connects given parameters into a URL"""
        if params:
            data = []
            for key in params:
                if isinstance(params[key], (tuple, list)):
                    data.append(f'{key}={",".join(params[key])}')
                else:
                    data.append(f'{key}={params[key]}')
            return f'{url}?{"&".join(data)}'
        return url
    return get_query
