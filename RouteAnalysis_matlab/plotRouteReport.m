tiledlayout(2,2)
nexttile([1,1])
plot(data.Gps_Distance,data.SpdLimKPH)
title('Speed Limit in KPH')
text(10000,40,'Number of SL events: ~80','color','blue')

nexttile([1,1])
plot(data.Gps_Distance,data.SpdLimKPH);
hold on
data.CornerTgtSpdCmf_KPH(data.CornerTgtSpdCmf_KPH == 0) = NaN;
data.CornerTgtSpdCmf_KPH(data.CornerTgtSpdCmf_KPH > data.SpdLimKPH) = NaN;
scatter(data.Gps_Distance,data.CornerTgtSpdCmf_KPH,'+')
title('Corner target speed in KPH - Comfort')
text(10000,40,'Number of CSA events - Comfort: ~237','color','blue')


nexttile([1,1])
plot(data.Gps_Distance,data.SpdLimKPH);
hold on
data.CornerTgtSpdEco_KPH(data.CornerTgtSpdEco_KPH == 0) = NaN;
data.CornerTgtSpdEco_KPH(data.CornerTgtSpdEco_KPH > data.SpdLimKPH) = NaN;
scatter(data.Gps_Distance,data.CornerTgtSpdEco_KPH,'+')
title('Corner target speed in KPH - Eco')
text(10000,40,'Number of CSA events - Comfort: ~252','color','blue')

nexttile([1,1])
plot(data.Gps_Distance,data.SpdLimKPH);
hold on
data.CornerTgtSpdDyn_KPH(data.CornerTgtSpdDyn_KPH == 0) = NaN;
data.CornerTgtSpdDyn_KPH(data.CornerTgtSpdDyn_KPH > data.SpdLimKPH) = NaN;
scatter(data.Gps_Distance,data.CornerTgtSpdDyn_KPH,'+')
title('Corner target speed in KPH - Eco')
text(10000,40,'Number of CSA events - Comfort: ~217','color','blue')
