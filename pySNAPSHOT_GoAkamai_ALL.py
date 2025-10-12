#####################################################################################################
# Script to save a snapshot from available GoAkamai (http://www.goakamai.org/) traffic cameras on Oahu, HI.
# Last Modified:    1/29/2025 Kayla Yamamoto
#                   		9/20/2025  Phoebe Chang
#
#####################################################################################################
import os, urllib, shutil, glob, requests, datetime
from PIL import Image, ImageFile

# print(zoneinfo.available_timezones())

ImageFile.LOAD_TRUNCATED_IMAGES = True
try:
    import zoneinfo  # The zoneinfo module is only available in Python 3.9+
except ImportError:
    from backports import zoneinfo  # Use backports.zoneinfo if necessary

key_timezone = 'Pacific/Honolulu'
timestamp = datetime.datetime.now(tz=zoneinfo.ZoneInfo(key=key_timezone))

url_parent = 'http://cctv.cdn.goakamai.org/SnapShot/320x240/'
url_child = {
    "TL-0007": "TL-0007.jpg",
    "TL-0008": "TL-0008.jpg",
#    "TL-0200": "TL-0200.jpg",
    "TL-0222": "TL-0222.jpg",
    "TL-0077": "TL-0077.jpg",
    "TL-0080": "TL-0080.jpg"
#    "TL-0001": "TL-0001.jpg",
#    "TL-0002": "TL-0002.jpg",
#   "TL-0226": "TL-0226.jpg",
#    "TL-0198": "TL-0198.jpg",
#   "TL-0004": "TL-0004.jpg",
#    "TL-0005": "TL-0005.jpg",
#    "TL-0006": "TL-0006.jpg",
#    "TL-0217": "TL-0217.jpg",
#    "TL-0193": "TL-0193.jpg",
#    "TL-0010": "TL-0010.jpg",
#    "TL-0011": "TL-0011.jpg",
#    "TL-0012": "TL-0012.jpg",
#    "TL-0013": "TL-0013.jpg",
#    "TL-0014": "TL-0014.jpg",
#    "TL-0015": "TL-0015.jpg",
#    "TL-0016": "TL-0016.jpg",
#    "TL-0017": "TL-0017.jpg",
#    "TL-0018": "TL-0018.jpg",
#    "TL-0019": "TL-0019.jpg",
#    "TL-0332": "TL-0332.jpg",
#    "TL-0306": "TL-0306.jpg",
#    "TL-0309": "TL-0309.jpg",
#    "TL-0255": "TL-0255.jpg",
#    "TL-0264": "TL-0264.jpg",
#    "TL-0256": "TL-0256.jpg",
#    "TL-0307": "TL-0307.jpg",
#    "TL-0308": "TL-0308.jpg",
#    "TL-0024": "TL-0024.jpg",
#    "TL-0026": "TL-0026.jpg",
#    "TL-0027": "TL-0027.jpg",
#    "TL-0029": "TL-0029.jpg",
#    "TL-0030": "TL-0030.jpg",
#    "TL-0031": "TL-0031.jpg",
#    "TL-0032": "TL-0032.jpg",
#    "TL-0033": "TL-0033.jpg",
#    "TL-0034": "TL-0034.jpg",
#    "TL-0322": "TL-0322.jpg",
#    "TL-0323": "TL-0323.jpg",
#    "TL-0232": "TL-0232.jpg",
#    "TL-0233": "TL-0233.jpg",
#    "TL-0057": "TL-0057.jpg",
#    "TL-0341": "TL-0341.jpg",
#    "TL-0348": "TL-0348.jpg",
#    "TL-0038": "TL-0038.jpg",
#    "TL-0039": "TL-0039.jpg",
#    "TL-0040": "TL-0040.jpg",
#    "TL-0227": "TL-0227.jpg",
#    "TL-0041": "TL-0041.jpg",
#    "TL-0042": "TL-0042.jpg",
#    "TL-0343": "TL-0343.jpg",
#    "TL-0326": "TL-0326.jpg",
#    "TL-0327": "TL-0327.jpg",
#    "TL-0320": "TL-0320.jpg",
#    "TL-0044": "TL-0044.jpg",
#    "TL-0328": "TL-0328.jpg",
#    "TL-0045": "TL-0045.jpg",
#    "TL-0325": "TL-0325.jpg",
#    "TL-0324": "TL-0324.jpg",
#    "TL-0331": "TL-0331.jpg",
#    "TL-0048": "TL-0048.jpg",
#    "TL-0228": "TL-0228.jpg",
#    "TL-0049": "TL-0049.jpg",
#    "TL-0314": "TL-0314.jpg",
#    "TL-0311": "TL-0311.jpg",
#    "TL-0051": "TL-0051.jpg",
#    "TL-0054": "TL-0054.jpg",
#    "TL-0058": "TL-0058.jpg",
#    "TL-0059": "TL-0059.jpg",
#    "TL-0060": "TL-0060.jpg",
#    "TL-0063": "TL-0063.jpg",
#    "TL-0062": "TL-0062.jpg",
#    "TL-0349": "TL-0349.jpg",
#    "TL-0350": "TL-0350.jpg",
#    "TL-0243": "TL-0243.jpg",
#    "TL-0302": "TL-0302.jpg",
#    "TL-0122": "TL-0122.jpg",
#    "TL-0188": "TL-0188.jpg",
#    "TL-0187": "TL-0187.jpg",
#    "TL-0300": "TL-0300.jpg",
#    "TL-0305": "TL-0305.jpg",
#    "TL-0168": "TL-0168.jpg",
#    "TL-0182": "TL-0182.jpg",
#    "TL-0175": "TL-0175.jpg",
#    "TL-0176": "TL-0176.jpg",
#    "TL-0177": "TL-0177.jpg",
#    "TL-0173": "TL-0173.jpg",
#    "TL-0174": "TL-0174.jpg",
#    "TL-0172": "TL-0172.jpg",
#    "TL-0178": "TL-0178.jpg",
#    "TL-0185": "TL-0185.jpg",
#    "TL-0184": "TL-0184.jpg",
#    "TL-0183": "TL-0183.jpg",
#    "TL-0170": "TL-0170.jpg",
#    "TL-0171": "TL-0171.jpg",
#    "TL-0181": "TL-0181.jpg",
#    "TL-0169": "TL-0169.jpg",
#    "TL-0180": "TL-0180.jpg",
#    "TL-0167": "TL-0167.jpg",
#    "TL-0186": "TL-0186.jpg",
#    "TL-0009": "TL-0009.jpg",
#    "TL-0801": "TL-0801.jpg",
#    "TL-0822": "TL-0822.jpg",
#    "TL-0804": "TL-0804.jpg",
#    "TL-0814": "TL-0814.jpg",
#    "TL-0803": "TL-0803.jpg",
#    "TL-0802": "TL-0802.jpg",
#    "TL-0064": "TL-0064.jpg",
#    "TL-0820": "TL-0820.jpg",
#    "TL-0806": "TL-0806.jpg",
#    "TL-0828": "TL-0828.jpg",
#    "TL-0241": "TL-0241.jpg",
#    "TL-0239": "TL-0239.jpg",
#    "TL-0240": "TL-0240.jpg",
#    "TL-0807": "TL-0807.jpg",
#    "TL-0066": "TL-0066.jpg",
#    "TL-0067": "TL-0067.jpg",
#    "TL-0068": "TL-0068.jpg",
#    "TL-0069": "TL-0069.jpg",
#    "TL-0070": "TL-0070.jpg",
#    "TL-0071": "TL-0071.jpg",
#    "TL-0072": "TL-0072.jpg",
#    "TL-0073": "TL-0073.jpg",
#    "TL-0074": "TL-0074.jpg",
#    "TL-0075": "TL-0075.jpg",
#    "TL-0076": "TL-0076.jpg",
#    "TL-0219": "TL-0219.jpg",
#    "TL-0218": "TL-0218.jpg",
#    "TL-0078": "TL-0078.jpg",
#    "TL-0079": "TL-0079.jpg",
#    "TL-0206": "TL-0206.jpg",
#    "TL-0093": "TL-0093.jpg",
#    "TL-0081": "TL-0081.jpg",
#    "TL-0094": "TL-0094.jpg",
#    "TL-0203": "TL-0203.jpg",
#    "TL-0095": "TL-0095.jpg",
#    "TL-0205": "TL-0205.jpg",
#    "TL-0155": "TL-0155.jpg",
#    "TL-0096": "TL-0096.jpg",
#    "TL-0082": "TL-0082.jpg",
#    "TL-0083": "TL-0083.jpg",
#    "TL-0084": "TL-0084.jpg",
#    "TL-0086": "TL-0086.jpg",
#    "TL-0087": "TL-0087.jpg",
#    "TL-0088": "TL-0088.jpg",
#    "TL-0089": "TL-0089.jpg",
#    "TL-0090": "TL-0090.jpg",
#    "TL-0207": "TL-0207.jpg",
#    "TL-0097": "TL-0097.jpg",
#    "TL-0189": "TL-0189.jpg",
#    "TL-0342": "TL-0342.jpg",
#    "TL-0270": "TL-0270.jpg",
#    "TL-0269": "TL-0269.jpg",
#    "TL-0340": "TL-0340.jpg",
#    "TL-0345": "TL-0345.jpg",
#    "TL-0346": "TL-0346.jpg",
#    "TL-0268": "TL-0268.jpg",
#    "TL-0271": "TL-0271.jpg",
#    "TL-0238": "TL-0238.jpg",
#    "TL-0258": "TL-0258.jpg",
#    "TL-0261": "TL-0261.jpg",
#    "TL-0260": "TL-0260.jpg",
#    "TL-0824": "TL-0824.jpg",
#    "TL-0021": "TL-0021.jpg",
#    "TL-0098": "TL-0098.jpg",
#    "TL-0208": "TL-0208.jpg",
#    "TL-0099": "TL-0099.jpg",
#    "TL-0100": "TL-0100.jpg",
#    "TL-0101": "TL-0101.jpg",
#    "TL-0102": "TL-0102.jpg",
#    "TL-0272": "TL-0272.jpg",
#    "TL-0103": "TL-0103.jpg",
#    "TL-0247": "TL-0247.jpg",
#    "TL-0262": "TL-0262.jpg",
#    "TL-0263": "TL-0263.jpg",
#    "TL-0246": "TL-0246.jpg",
#    "TL-0248": "TL-0248.jpg",
#    "TL-0231": "TL-0231.jpg",
#    "TL-0244": "TL-0244.jpg",
#    "TL-0104": "TL-0104.jpg",
#    "TL-0105": "TL-0105.jpg",
#    "TL-0815": "TL-0815.jpg",
#    "TL-0106": "TL-0106.jpg",
#    "TL-0107": "TL-0107.jpg",
#    "TL-0109": "TL-0109.jpg",
#    "TL-0110": "TL-0110.jpg",
#    "TL-0111": "TL-0111.jpg",
#    "TL-0112": "TL-0112.jpg",
#    "TL-0273": "TL-0273.jpg",
#    "TL-0113": "TL-0113.jpg",
#    "TL-0114": "TL-0114.jpg",
#    "TL-0115": "TL-0115.jpg",
#    "TL-0275": "TL-0275.jpg",
#    "TL-0195": "TL-0195.jpg",
#    "TL-0209": "TL-0209.jpg",
#    "TL-0197": "TL-0197.jpg",
#    "TL-0196": "TL-0196.jpg",
#    "TL-0265": "TL-0265.jpg",
#    "TL-0339": "TL-0339.jpg",
#    "TL-0116": "TL-0116.jpg",
#    "TL-0202": "TL-0202.jpg",
#    "TL-0338": "TL-0338.jpg",
#    "TL-0813": "TL-0813.jpg",
#    "TL-0819": "TL-0819.jpg",
#    "TL-0816": "TL-0816.jpg",
#    "TL-0811": "TL-0811.jpg",
#    "TL-0117": "TL-0117.jpg",
#    "TL-0118": "TL-0118.jpg",
#    "TL-0119": "TL-0119.jpg",
#    "TL-0120": "TL-0120.jpg",
#    "TL-0121": "TL-0121.jpg",
#    "TL-0237": "TL-0237.jpg",
#    "TL-0234": "TL-0234.jpg",
#    "TL-0236": "TL-0236.jpg",
#    "TL-0235": "TL-0235.jpg",
#    "TL-0827": "TL-0827.jpg",
#    "TL-0812": "TL-0812.jpg",
#    "TL-0279": "TL-0279.jpg",
#    "TL-0278": "TL-0278.jpg",
#    "TL-0281": "TL-0281.jpg",
#    "TL-0280": "TL-0280.jpg",
#    "TL-0277": "TL-0277.jpg",
#    "TL-0285": "TL-0285.jpg",
#    "TL-0284": "TL-0284.jpg",
#    "TL-0282": "TL-0282.jpg",
#    "TL-0283": "TL-0283.jpg",
#    "TL-0123": "TL-0123.jpg",
#    "TL-0124": "TL-0124.jpg",
#    "TL-0125": "TL-0125.jpg",
#    "TL-0129": "TL-0129.jpg",
#    "TL-0130": "TL-0130.jpg",
#    "TL-0131": "TL-0131.jpg",
#    "TL-0134": "TL-0134.jpg",
#    "TL-0276": "TL-0276.jpg",
#    "TL-0135": "TL-0135.jpg",
#    "TL-0136": "TL-0136.jpg",
#    "TL-0137": "TL-0137.jpg",
#    "TL-0138": "TL-0138.jpg",
#    "TL-0141": "TL-0141.jpg",
#    "TL-0144": "TL-0144.jpg",
#    "TL-0805": "TL-0805.jpg",
#    "TL-0145": "TL-0145.jpg",
#    "TL-0146": "TL-0146.jpg",
#    "TL-0147": "TL-0147.jpg",
#    "TL-0149": "TL-0149.jpg",
#    "TL-0148": "TL-0148.jpg",
#    "TL-0810": "TL-0810.jpg",
#    "TL-0808": "TL-0808.jpg",
#    "TL-0826": "TL-0826.jpg",
#    "TL-0809": "TL-0809.jpg",
#    "TL-0817": "TL-0817.jpg",
#    "TL-0150": "TL-0150.jpg",
#    "TL-0151": "TL-0151.jpg",
#    "TL-0152": "TL-0152.jpg",
#    "TL-0154": "TL-0154.jpg",
#    "TL-0157": "TL-0157.jpg",
#    "TL-0158": "TL-0158.jpg",
#    "TL-0159": "TL-0159.jpg",
#    "TL-0160": "TL-0160.jpg",
#    "TL-0161": "TL-0161.jpg",
#    "TL-0162": "TL-0162.jpg",
#    "TL-0823": "TL-0823.jpg",
#    "TL-0163": "TL-0163.jpg",
#    "TL-0164": "TL-0164.jpg",
#    "TL-0165": "TL-0165.jpg",
#    "TL-0825": "TL-0825.jpg",
#    "TL-0818": "TL-0818.jpg",
#    "TL-0166": "TL-0166.jpg"
}

path_unavailable = 'UNAVAILABLE.jpg'

def compare_snapshots(imageA, imageB):
    A = list(Image.open(imageA, 'r').convert('RGB').getdata())
    B = list(Image.open(imageB, 'r').convert('RGB').getdata())
    if len(A) != len(B):
        return -1
    
    diff = [A[i][0] != B[i][0] or A[i][1] != B[i][1] or A[i][2] != B[i][2] for i in range(len(A))]
    return sum(diff) / len(diff)

def download_snapshots(url_parent, url_child, path_unavailable, timestamp=None, threshold=0.05):
    if timestamp is None:
        timestamp = datetime.datetime.now(tz=zoneinfo.ZoneInfo(key=key_timezone))
    
    res = 0
    for key, elem in url_child.items():
#        key = "livestream-snapshots" + key
        base_save_path = "/media/volume/test_Data"
        camera_folder = os.path.join(base_save_path, key)
        os.makedirs(camera_folder, exist_ok=True)

        
        # Try the URL without query parameters first
        url = f"{url_parent}{elem}"
        path = os.path.join(camera_folder, os.path.basename(elem))
        files = glob.glob(os.path.splitext(path)[0] + '-*' + os.path.splitext(path)[1])
        files.sort()
        
        n = 0
        while n < 10:
            try:
                req = requests.get(url, stream=True)
                if req.status_code == 200:
                    break
            except:
                n += 1
        
        # If the first request fails, try again with the dynamic query parameter
        if req.status_code != 200:
            query_param = int(datetime.datetime.now().timestamp() * 1000)
            url = f"{url_parent}{elem}?icx={query_param}"
            n = 0
            while n < 10:
                try:
                    req = requests.get(url, stream=True)
                    if req.status_code == 200:
                        break
                except:
                    n += 1
        
        if n == 10 or req.status_code != 200:
            print(f'ERROR at download_snapshots: Unable to retrieve {key}')
            continue
        
        with open(path, 'wb') as f:
            for chunk in req.iter_content():
                f.write(chunk)
        
        if path_unavailable is not None:
            if compare_snapshots(path, path_unavailable) == 0:
                continue
        
        dest_path = f"{os.path.splitext(path)[0]}-{timestamp.strftime('%Y%m%dT%H%M%S')}{os.path.splitext(path)[1]}"
        
        if os.path.exists(path):
            try:
                shutil.copyfile(path, dest_path)  # Avoids permission issues
            except PermissionError:
                print(f"ERROR: Unable to copy {path} to {dest_path}. Check file system permissions.")
        else:
            print(f"WARNING: File {path} not found, skipping.")
    
    return res


res = download_snapshots(url_parent, url_child, path_unavailable=path_unavailable, timestamp=timestamp, threshold=0.05)

