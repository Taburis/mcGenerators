
#ifndef EVTINFO_H
#define EVTINFO_H
#include "TTree.h"

class evtInfo {
		public :
				evtInfo(){};
				void init(TTree* t);
				void addEvtInfo(double iweight, float ipthat){weight = iweight; ipthat = pthat;};

				TTree* ot;
				double weight;
			   	float pthat;
};

void evtInfo::init(TTree* t){
		ot = t;
//		ot->Branch("vz", &vz, "vz/F");
		ot->Branch("pthat", &pthat, "pthat/F");
		ot->Branch("weight", &weight, "weight/F");
}

#endif
