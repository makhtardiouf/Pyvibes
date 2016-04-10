#include "asn1test.txt_typedefs.h"
// -- ASN1START

struct     SLCommConfigr12    {
  enum        commTxResourcesr12   {
    typedef          release;
    enum           setup    {
      struct        scheduledr12     {
        CRNTI       slRNTIr12;
        MACMainConfigSLr12     macMainConfigr12;
        SLCommResourcePoolr12     scCommTxConfigr12;
        int        mcsr12;
      } ;
      struct        ueSelectedr12     {
        // Pool for normal usage;
        struct    commTxPoolNormalDedicatedr12      {
          SLTxPoolToReleaseListr12     poolToReleaseListr12;
          SLCommTxPoolToAddModListr12    poolToAddModListr12;
        };
      };
    };
  };

  enum         scheduledr13x0
    {
      typedef  release;
      struct           setup     {
        LogicalChGroupInfoListr13    logicalChGroupInfoListr13;
        bool     multipleTxAllowedr13;
      };
    };
  struct        ueSelectedr13x0    {
    struct    commTxPoolNormalDedicatedExtr13     {
      SLTxPoolToReleaseListExtr13     poolToReleaseListExtr13;
      SLCommTxPoolToAddModListExtr13    poolToAddModListExtr13;
    };
  };
  bool   commTxAllowRelayDedicatedr13;

};
;
// -- ASN1STOP
