from ncclient import manager

m = manager.connect(
         host="10.10.20.48",
         port=830,
         username="developer",
         password="C1sco12345",
         hostkey_verify= False
    
    )

print("#Supported Capabilities (YANG models):")
for capability in m.server_capabilities:
    print(capability)
