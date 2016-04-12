#include "RRC36331-EUTRA-Sidelink-Preconf.asn1_typedefs.h"
// 
// --
// -- ASN.1 module found by ./crfc2asn1.pl in EUTRA-RRC36331.txt at line 19307
// --
// 
// EUTRA-Sidelink-Preconf DEFINITIONS AUTOMATIC TAGS ::=
// 
// BEGIN
// 
// IMPORTS
// AdditionalSpectrumEmission,
// ARFCN-ValueEUTRA-r9,
// FilterCoefficient,
// maxSL-TxPool-r12,
// maxSL-CommRxPoolPreconf-v13x0,
// maxSL-CommTxPoolPreconf-v13x0,
// maxSL-DiscRxPoolPreconf-r13,
// maxSL-DiscTxPoolPreconf-r13,
// P-Max,
// ReselectionInfoRelay-r13,
// SL-CP-Len-r12,
// SL-HoppingConfigComm-r12,
// SL-OffsetIndicatorSync-r12,
// SL-PeriodComm-r12,
// RSRP-RangeSL3-r12,
// SL-PriorityList-r13,
// SL-TF-ResourceConfig-r12,
// SL-TRPT-Subset-r12,
// P0-SL-r12,
// TDD-ConfigSL-r12
// FROM EUTRA-RRC-Definitions;
// 
// -- ASN1STOP
// 
// 
// -	SL-Preconfiguration
// The IE SL-Preconfiguration includes the sidelink pre-configured parameters.
// SL-Preconfiguration information elements
// -- ASN1START
	 ;
	struct    SLPreconfigurationr12    {
	SLPreconfigGeneralr12     preconfigGeneralr12;
	SLPreconfigSyncr12      preconfigSyncr12;
	SLPreconfigCommPoolList4r12      preconfigCommr12;
	

;
	 struct      preconfigCommv13x0  
   {
	SLPreconfigCommRxPoolListExtr13    commRxPoolListExtr13;
	  SLPreconfigCommTxPoolListExtr13   commTxPoolListExtr13;
	                   };
	 struct      preconfigDiscr13    {
	SLPreconfigDiscRxPoolListr13     discRxPoolListr13;
	  SLPreconfigDiscTxPoolListr13    discTxPoolListr13;
	                   };
	    SLPreconfigRelayr13    preconfigRelayr13;
	 
;
	 ;
	};
	 ;
	struct    SLPreconfigGeneralr12    {
	 PDCP configuration;
	 struct       rohcProfilesr12   {
	 bool        profile0x0001r12;
	 bool        profile0x0002r12;
	 bool        profile0x0004r12;
	 bool        profile0x0006r12;
	 bool        profile0x0101r12;
	 bool        profile0x0102r12;
	 bool       profile0x0104r12;
	} ;
	 Physical configuration;
	ARFCNValueEUTRAr9       carrierFreqr12;
	PMax       maxTxPowerr12;
	AdditionalSpectrumEmission   additionalSpectrumEmissionr12;
	 enum       slbandwidthr12   { 
n6,  n15,  n25,  n50,  n75
	TDDConfigSLr12      tddConfigSLr12;
	std::bitset<1>       reservedr12;
	

;
	};
	 ;
	struct   SLPreconfigSyncr12    {
	SLCPLenr12       syncCPLenr12;
	SLOffsetIndicatorSyncr12    syncOffsetIndicator1r12;
	SLOffsetIndicatorSyncr12    syncOffsetIndicator2r12;
	P0SLr12     syncTxParametersr12;
	RSRPRangeSL3r12      syncTxThreshOoCr12;
	FilterCoefficient     filterCoefficientr12;
	 enum       syncRefMinHystr12   { 
dB0,  dB3,  dB6,  dB9
	 enum       syncRefDiffHystr12   { 
dB0,  dB3,  dB6,  dB9,  dB12
	

;
	Need OR     enum  true}     syncTxPeriodicr13  
   { 
true}     syncTxPeriodicr13  
  ,
	 
;
	};
	 ;
	SEQU SLPreconfigCommPoolList4r12  ;
	 ;
	SEQU SLPreconfigCommRxPoolListExtr13  ;
	 ;
	SEQU SLPreconfigCommTxPoolListExtr13  ;
	 ;
	struct    SLPreconfigCommPoolr12    {
	 This IE is same as SLCommResourcePool with rxParametersNCell absent;
	SLCPLenr12       scCPLenr12;
	SLPeriodCommr12       scPeriodr12;
	SLTFResourceConfigr12    scTFResourceConfigr12;
	P0SLr12      scTxParametersr12;
	SLCPLenr12       dataCPLenr12;
	SLTFResourceConfigr12    dataTFResourceConfigr12;
	SLHoppingConfigCommr12     dataHoppingConfigr12;
	P0SLr12     dataTxParametersr12;
	SLTRPTSubsetr12       trptSubsetr12;
	

;
	For Tx    SLPriorityListr13    priorityListr13  
;
	 
;
	};
	 ;
	SEQU SLPreconfigDiscRxPoolListr13  ;
	 ;
	SEQU SLPreconfigDiscTxPoolListr13  ;
	 ;
	struct    SLPreconfigDiscPoolr13    {
	 This IE is same as SLDiscResourcePool with rxParameters absent;
	SLCPLenr12       cpLenr13;
	 enum      discPeriodr13   { 
rf4,  rf7,  rf8,  rf14,  rf16,  rf28,  rf32
	rf128  rf256  rf512  rf1024  spare4  spare3 ;
	spare2  spare} ;
	 int      numRetxr13;
	 int     numRepetitionr13;
	SLTFResourceConfigr12    tfResourceConfigr13;
	 struct      txParametersr13   {
	P0SLr12   txParametersGeneralr13;
	 enum   p100}   txProbabilityr13    { 
p25,  p50
	                 };
	

;
	};
	 ;
	struct   SLPreconfigRelayr13    {
	ReselectionInfoRelayr13   reselectionInfoRemoteUEOoCr13;
	};
	 ;
	// END;
