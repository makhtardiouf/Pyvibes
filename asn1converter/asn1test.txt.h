struct     SLCommConfigr12 {
    enum        commTxResourcesr12 {
        typedef         release;
        enum           setup {
            struct        scheduledr12 {
                typedef CRNTI      slRNTIr12;
                typedef MACMainConfigSLr12    macMainConfigr12;
                typedef SLCommResourcePoolr12    scCommTxConfigr12;
                typedef         int        mcsr12;
            }
            struct        ueSelectedr12 {
// -- Pool for normal usage {
                struct    commTxPoolNormalDedicatedr12 {
                    typedef SLTxPoolToReleaseListr12    poolToReleaseListr12;
                    typedef    SLCommTxPoolToAddModListr12    poolToAddModListr12;
                    typedef
                }     ;
                typedef
            }    ;
            typedef
        }   ;
    }
    typedef ;
}
enum         scheduledr13x0 {
    typedef         release;
    struct           setup {
        typedef LogicalChGroupInfoListr13   logicalChGroupInfoListr13;
        bool     multipleTxAllowedr13;
        typedef
    }    ;
}
struct        ueSelectedr13x0 {
    struct    commTxPoolNormalDedicatedExtr13 {
        typedef SLTxPoolToReleaseListExtr13    poolToReleaseListExtr13;
        typedef     SLCommTxPoolToAddModListExtr13    poolToAddModListExtr13;
        typedef
    }    ;
}
bool   commTxAllowRelayDedicatedr13;

}
}
