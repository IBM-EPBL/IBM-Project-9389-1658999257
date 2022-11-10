from ibm_watson_machine_learning import APIClient

web_cred={
    "apikey": "6PcwxslwN5BT5dP8C4oKx62Vsz661Sxw-KY3oVAygalC",
	"url": "https://cloud.ibm.com/user"
}

client=APIClient(web_cred)
spaceID="e4et5ffc-r11a-4hcc-9c1e-r45c6a510aeb"
x=client.set.default_space(spaceID)
print(x)