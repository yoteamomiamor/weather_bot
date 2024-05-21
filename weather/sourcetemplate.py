def sourcetemplate(url: str):
    """Returns function that connects given params"""
    def get_query(**params) -> str:
        """Properly connects given parameters into a URL"""
        if params:
            data = [f'{key}={params[key]}' for key in params]
            return f'{url}?{"&".join(data)}'
        return url
    return get_query
