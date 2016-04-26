
// Note: Adhoc ASN1 converter, by Makhtar Diouf
#include "asn1test.txt_typedefs.h"
// -- ASN1START
;
struct SLCommConfig_r12 {
  enum commTxResources_r12 {
    typedef release; enum setup{struct scheduled_r12{
        CRNTI slRNTI_r12; MACMainConfigSL_r12 macMainConfig_r12;
        SLCommResourcePool_r12 scCommTxConfig_r12; int mcs_r12;};
  struct ueSelected_r12 {
         Pool for normal usage;
         struct commTxPoolNormalDedicated_r12 {
           SLTxPoolToReleaseList_r12 poolToReleaseList_r12;
           SLCommTxPoolToAddModList_r12 poolToAddModList_r12;
         };
  };
};
}
;
;
;
enum scheduled_r13x0 {
  typedef release;
  struct setup{LogicalChGroupInfoList_r13 logicalChGroupInfoList_r13;
               bool multipleTxAllowed_r13;};
}
;
struct ueSelected_r13x0 {
  struct commTxPoolNormalDedicatedExt_r13 {
    SLTxPoolToReleaseListExt_r13 poolToReleaseListExt_r13;
    SLCommTxPoolToAddModListExt_r13 poolToAddModListExt_r13;
  };
};
bool commTxAllowRelayDedicated_r13;
}
;
;
// -- ASN1STOP
