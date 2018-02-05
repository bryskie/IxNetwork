params = {
    "trafficItems": [
        {
	    "name": "Port1 to Port2",
            "enabled": True,
            "bidirectional": True,
	    "trackBy": ["flowGroup0"],
	    "endpoints": {
		"srcPort": ["192.168.70.11", "1", "1"],
		"dstPort": ["192.168.70.11", "2", "1"]
	    },
	    "configElement": {
		"transmissionType": "fixedPacketCount",
		"frameCount": 2000000,
		"frameRate": 100,
		"frameRateType": "percentLineRate",
		"frameSize": 64,
		"stack": {
		    "mac": {
			"src": {"start": "00:0c:29:aa:86:e0", "step": "00:00:00:00:00:01", "direction": "increment", "count": 1},
			"dst": {"start": "00:0c:29:84:37:16", "step": "00:00:00:00:00:01", "direction": "increment", "count": 1}
		    },
		    "mpls": [
			{"start": 16, "step": 1, "direction": "increment", "count": 2},
			{"start": 18, "step": 1, "direction": "increment", "count": 2}
		    ],
		    "ipv4": {
			"src": {"start": "1.1.1.1", "step": "0.0.0.1", "direction": "increment", "count": 2},
			"dst": {"start": "1.1.1.2", "step": "0.0.0.1", "direction": "increment", "count": 2}
		    }
		}
	    }
	},
        {
	    "name": "Port3 to Port4",
            "enabled": True,
            "bidirectional": True,
	    "trackBy": ["flowGroup0"],
	    "endpoints": {
		"srcEndpoint": ["192.168.70.11", "1", "1"],
		"dstEndpoint": ["192.168.70.11", "2", "1"]
	    },
	    "configElement": {
		"transmissionType": "fixedPacketCount",
		"frameCount": 2000000,
		"frameRate": 100,
		"frameRateType": "percentLineRate",
		"frameSize": 64,
		"stack": {
		    "mac": {
			"src": {"start": "00:0c:29:aa:86:e0", "step": "00:00:00:00:00:01", "direction": "increment", "count": 1},
			"dst": {"start": "00:0c:29:84:37:16", "step": "00:00:00:00:00:01", "direction": "increment", "count": 1}
		    },
		    "mpls": [
			{"start": 20, "step": 1, "direction": "increment", "count": 2},
			{"start": 22, "step": 1, "direction": "increment", "count": 2}
		    ],
		    "ipv4": {
			"src": {"start": "1.1.1.1", "step": "0.0.0.1", "direction": "increment", "count": 2},
			"dst": {"start": "1.1.1.2", "step": "0.0.0.1", "direction": "increment", "count": 2}
		    }
		}
	    }
	}
    ]
}
