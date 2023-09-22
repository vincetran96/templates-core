'''ClickHouse utils
'''
import requests
import http.client
from requests import Response

from utils.configs import CLICKHOUSE_USER, CLICKHOUSE_PASSWORD, CH_PROD_HOST
from utils.datetime import str_to_date, generate_dates


# Http max headers must be set for connection to ClickHouse
http.client._MAXHEADERS = 1000
DATABASE = 'default'
TIMEOUT = 6000

def execute_clickhouse_query(
    query,
    user = CLICKHOUSE_USER,
    password = CLICKHOUSE_PASSWORD,
    host = CH_PROD_HOST,
    database = DATABASE,
    connection_timeout = TIMEOUT,
    external_file: str = None,
    external_file_cols: dict = None,
    stream: bool = False
):
    '''
    Experimental feature: external file

    Resources:
    - https://clickhouse.com/docs/en/engines/table-engines/special/external-data
    - https://stackoverflow.com/questions/10859374/curl-f-what-does-it-mean-php-instagram
    - https://requests.readthedocs.io/en/latest/user/quickstart/#post-a-multipart-encoded-file

    **Query with external file can be like so:**
    ```
    select
        cc.query, ad_urls
    from
        (select lowerUTF8(query) as query, `ads.url` as ad_urls
        from coccoc_search.serp
        where event_date = yesterday()) cc
    inner join (select query from external_file) gg on cc.query = gg.query
    ```

    The file must:
    - **Not** contain a header row
    - Not contain quotes
    - Be tab-separated

    ---
    :params:
    ---
        - external_file: path to file
        - external_file_cols: dict of cols and ClickHouse dtype for each
            For example: `external_file_cols = {'domain': 'String', 'traffic': 'UInt32'}`
        - stream: whether to stream response
    '''
    params = {
        'query': query,
        'database': database,
        'user': user,
        'password': password
    }
    files = None    

    # Change file-related variables if `external_file` is provided
    if external_file:
        files = {'external_file': open(external_file, 'r', encoding="utf-8")}
        structure = ",".join([f"{col} {dtype}" for col, dtype in external_file_cols.items()])
        params = {
            'query': query,
            'database': database,
            'user': user,
            'password': password,
            'external_file_structure': structure
        }

    request = requests.post(
        host,
        params = params,
        timeout = connection_timeout,
        files = files,
        stream = stream
    )

    return request

def get_clickhouse_data(
        query, external_file: str = None, external_file_cols: dict = None, stream: bool = False
    ) -> Response:
    '''Gets data from ClickHouse as text

    Returns a Response object (in case you need to stream it)
    '''
    resp = execute_clickhouse_query(
        query, CLICKHOUSE_USER, CLICKHOUSE_PASSWORD, CH_PROD_HOST, DATABASE, TIMEOUT,
        external_file=external_file, external_file_cols=external_file_cols,
        stream=stream
    )
    resp.raise_for_status()
    if resp.status_code == 200:
        return resp
    raise ValueError(resp.text)

def gen_dates_back(ddate: str, n_dates: int):
    '''Generates dates from ddate going back n_dates;

    Returns a list of strings representing dates
    sorted ascendingly
    '''
    check_ddate = True
    if ddate != "yesterday":
        try:
            str_to_date(ddate)
        except Exception:
            check_ddate = False
    if not check_ddate:
        raise ValueError("Check the value of param `ddate`")
    
    ddate_str = "yesterday()" if ddate == "yesterday" else f"toDate('{ddate}')"
    data_dd = get_clickhouse_data(f"select {ddate_str} - {n_dates}, {ddate_str}").text
    start, end = data_dd.strip().split("\t")
    dates_arr = generate_dates(start, end)
    return sorted(set(dates_arr))

def get_yesterday():
    '''Gets the date representing yesterday() in CH
    '''
    data = get_clickhouse_data("select yesterday()").text
    return data.strip()
