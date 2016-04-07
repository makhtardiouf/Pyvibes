   struct     SLCommConfigr12       { 
       enum        commTxResourcesr12     { 
           typedef         release; 
           enum           setup     { 
               struct        scheduledr12       { 
                   typedef CRNTI      slRNTIr12  ; 
                   typedef MACMainConfigSLr12    macMainConfigr12  ; 
                   typedef SLCommResourcePoolr12    scCommTxConfigr12  ; 
                   int  mcsr12; 
               }; ,      
               struct        ueSelectedr12       { 
                   
                   struct    commTxPoolNormalDedicatedr12        { 
                       typedef    SLTxPoolToReleaseListr12    poolToReleaseListr12; 
                       typedef    SLCommTxPoolToAddModListr12    poolToAddModListr12; 
                   };
               };
           }
       }
   };
       