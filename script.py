from mitmproxy import http
import logging

# 로그 설정
logging.basicConfig(filename='packets.log', level=logging.INFO)

def request(flow: http.HTTPFlow) -> None:
    # # 특정 도메인 필터링 (예: example.com)
    # target_domain = "example.com"
    # if target_domain in flow.request.pretty_host:
        logging.info(f"Request to {flow.request.pretty_url}")
        print(f"Request: {flow.request.method} {flow.request.pretty_url}")
        print(f"Headers: {flow.request.headers}")
        print(f"Content: {flow.request.content}")

def response(flow: http.HTTPFlow) -> None:
    # # 특정 도메인 필터링
    # target_domain = "example.com"
    # if target_domain in flow.request.pretty_host:
    #     logging.info(f"Response from {flow.request.pretty_url}")
        print(f"Response: {flow.response.status_code}")
        print(f"Headers: {flow.response.headers}")
        print(f"Content: {flow.response.content}")