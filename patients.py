import requests

baseUrl = "https://api.dev.onalabs.biot-med.com"

url = "https://api.dev.onalabs.biot-med.com/organization/v1/users/patients?searchRequest=%7B%22limit%22%3A30%2C%22filter%22%3A%7B%22_ownerOrganization.id%22%3A%7B%22in%22%3A%5B%22a416a889-8cc6-46d9-bbef-2c0df6bd78ea%22%5D%7D%7D%2C%22freeTextSearch%22%3A%22%22%7D"

headers = {
    "accept": "application/json",
    "authorization": "Bearer eyJhbGciOiJSUzUxMiJ9.eyJyZWZyZXNoVG9rZW5JZCI6ImQzZmJhMDc5LTg3MDgtNDAyYi1iM2FiLTJjMGQ3OTYzZjA0YSIsInRlbmFudElkIjoiYTQxNmE4ODktOGNjNi00NmQ5LWJiZWYtMmMwZGY2YmQ3OGVhIiwic2NvcGVzIjpbIlNFVFRJTkdTX01JTklNSVpFRF9TRUFSQ0hfVEVNUExBVEUiLCJQUk9URUNURURfQVBJIiwiU0VUVElOR1NfUE9SVEFMX0JVSUxERVJfR0VUX1ZJRVdfRlVMTF9BVFRSSUJVVEVTIiwiVU1TX1VTRVJTX1NFTEZfVVBEQVRFX1VTRVIiLCJTRVRUSU5HU19HRVRfVEVNUExBVEUiLCJVTVNfVVNFUlNfU0VMRl9ERUxFVEVfVVNFUiIsIk9SR0FOSVpBVElPTl9HRVRfQlVJTFRfSU5fVEVNUExBVEVTIiwiVU1TX1VTRVJTX1NFTEZfR0VUX1VTRVIiLCJTRVRUSU5HU19TRUFSQ0hfVEVNUExBVEUiXSwidG9rZW5UeXBlIjoiVVNFUiIsImp0aSI6Ijk1ZmUxZTIyLTliZTMtNDBkYS05MjgzLWM0ZjRlMzA5ZDI1MiIsInN1YiI6IjBhZDlkZjg2LTY2ZjYtNDEzNi04ZDEyLTJiNzI5OWRlNGQ4ZiIsImV4cCI6MTY5MTIyNzcyNn0.OUa5ifmActW9Sg-yGIz_hdIPLDEmA0FXjbodAYEz1vToI9BxE8AmOo_N8yI8sQbxmLHFIpAP5PgCdv3UgAnCLfRgPUEwUkjO59qi6tw3JZZ_AoIPW30VmFoGmN0rd0HQ9R3qFLhwRm_nxFWysAbyzgBkvlvc21Vk9gdGDaDdDZd3m78zT9QvGE6D00PSv6xFBHPsQlk0wRATEHCw0VocJVCBHRZ8-Is7zVaN6ZzcCzVuAzD9Ao1jJsEq9a79Y5m8uPSdNLIhsSSbTGdgQT8iHheBxaQ1NHtMLCMRDhilgLPc3cNPReS5yliY-HDYN9PCvAK3VWdoDmx11g-lfjaIDA"
}

response = requests.get(url, headers=headers)

print(response.text)