'''
Created on Dec 5, 2012

@author: inekar
'''

#result = [[133747.3, 138046.6, 131550.8, 127115.1, 139616.99999999997, 136272.69999999998, 137124.19999999998, 136718.4, 133234.6, 135549.89999999997, 135447.80000000002, 135443.69999999998, 137581.80000000002, 140884.6, 132677.1, 138015.1, 134061.3, 136315.4, 136919.19999999998, 140083.40000000002, 137665.0, 137399.1, 144249.69999999998, 142011.8, 132875.9, 136104.9, 137391.2, 139008.19999999998, 143260.1, 140927.1, 136824.7, 136272.69999999998, 137915.69999999998, 136130.40000000002, 138702.2, 140793.80000000002, 139330.89999999997, 136717.89999999997, 136980.09999999998, 136289.59999999998, 139545.8, 132651.40000000002, 142783.19999999998, 131819.3, 136928.1, 139470.5, 137445.5, 140113.5, 125881.50000000001, 139594.0, 137401.90000000002, 127413.09999999999, 132233.19999999998, 135645.4, 137938.69999999998, 136345.8, 137043.79999999996, 132338.8, 134925.7, 137621.3, 136759.40000000002, 140066.9, 128432.50000000001, 131129.3, 136846.59999999998, 137211.3, 137706.59999999998, 135044.39999999997, 133187.3, 133937.7, 138522.9, 138030.4, 137886.09999999998, 127464.59999999999, 136685.8, 137715.50000000003, 137591.50000000003, 119367.4, 133349.49999999997, 141054.9, 135328.0, 132637.59999999998, 132914.89999999997, 137940.8, 136346.4, 133119.5, 132120.0, 135987.1, 138653.1, 133417.59999999998, 134224.99999999997, 135391.9, 131338.8, 140927.1, 126165.90000000001, 144402.69999999998, 135241.2, 136284.4, 131657.59999999998, 142110.69999999998],
#          [133747.3, 140959.1, 137052.1, 140930.99999999997, 135171.8, 139223.3, 129330.20000000001, 136904.90000000002, 139054.8, 131290.69999999998, 136243.9, 139802.7, 127782.5, 132246.49999999997, 138858.7, 138537.2, 134079.69999999998, 131201.3, 133747.30000000002, 139144.3, 132010.9, 142093.9, 136980.1, 132689.39999999997, 139429.5, 139033.00000000003, 127031.4, 143674.2, 142828.3, 133342.7, 135577.0, 136284.4, 133231.4, 138041.40000000002, 131338.8, 139394.69999999998, 136414.6, 136536.6, 135366.3, 131756.19999999998, 135563.3, 130829.59999999999, 135079.9, 137119.5, 135422.4, 134671.5, 135203.2, 135399.0, 136710.3, 133303.00000000003, 135952.1, 140276.6, 134883.49999999997, 135391.9, 138915.0, 139594.0, 136331.1, 144293.69999999998, 139568.19999999998, 129756.40000000001, 132858.49999999997, 134702.5, 131639.09999999998, 137940.8, 127988.29999999999, 138186.5, 133252.19999999998, 130311.6, 135780.5, 140102.3, 130572.2, 127847.50000000001, 138736.99999999997, 132704.09999999998, 137159.99999999997, 127545.40000000001, 134397.30000000002, 134491.3, 133521.4, 129838.90000000001, 135461.40000000002, 133924.1, 138213.2, 135444.3, 129656.7, 134625.30000000002, 131869.5, 133607.30000000002, 136278.9, 129838.90000000001, 138949.3, 133189.30000000002, 139123.8, 130366.3, 132194.1, 136283.3, 138571.3, 137819.99999999997, 123308.1, 127545.40000000001],
#          [133747.3, 138862.8, 135126.7, 136564.89999999997, 135952.1, 138188.19999999998, 139862.90000000002, 141975.69999999998, 133021.9, 139580.6, 137938.5, 133607.30000000002, 140921.0, 137059.4, 136464.0, 142785.4, 130956.79999999999, 139235.09999999998, 138510.7, 143107.19999999998, 137011.2, 135902.1, 136209.19999999998, 140839.6, 134704.6, 129134.59999999998, 136422.1, 133927.1, 134167.90000000002, 131270.19999999998, 136046.8, 135812.7, 136483.1, 125323.50000000001, 137824.69999999998, 129899.5, 137387.0, 135899.9, 137618.69999999998, 140653.9, 141769.49999999997, 136029.9, 140786.4, 137331.9, 138096.2, 132637.59999999998, 134945.6, 132047.9, 137910.29999999996, 129276.79999999999, 129528.29999999999, 134353.1, 141454.1, 132856.0, 138931.8, 139190.3, 134755.2, 135384.59999999998, 134794.0, 135391.9, 132677.1, 135416.09999999998, 125976.79999999999, 137305.39999999997, 136774.8, 133924.1, 135880.2, 142967.0, 139213.59999999998, 136139.2, 127826.2, 136604.5, 137900.1, 143779.7, 137432.69999999998, 141102.20000000004, 134516.6, 137084.19999999998, 132802.1, 132758.09999999998, 140432.4, 138349.2, 134504.40000000002, 138349.2, 139944.9, 137090.19999999998, 139429.5, 138510.7, 133096.6, 141342.2, 133768.5, 136817.00000000003, 138108.4, 139119.4, 134762.0, 128380.1, 137070.9, 131129.3, 138653.1, 141988.3],
#          [133747.3, 141520.6, 138268.69999999998, 138504.5, 135335.50000000003, 128183.70000000001, 129436.00000000001, 142355.0, 132726.40000000002, 136489.7, 141609.9, 140140.9, 132010.9, 134169.19999999998, 133031.4, 143674.2, 134712.69999999998, 137763.0, 138213.2, 135782.3, 135084.4, 126391.9, 135588.59999999998, 143050.09999999998, 139603.9, 124277.5, 139196.6, 127297.1, 125881.50000000001, 136900.59999999998, 136349.7, 139865.4, 139616.99999999997, 134075.9, 135468.9, 126960.49999999999, 134764.3, 137016.39999999997, 142783.19999999998, 134768.5, 128831.09999999999, 142923.9, 137540.00000000003, 138051.5, 138286.4, 134767.30000000002, 140780.50000000003, 140164.59999999998, 136464.8, 132865.3, 139655.49999999997, 136718.4, 137445.5, 129276.79999999999, 132512.5, 130358.40000000001, 134964.19999999998, 137035.8, 136723.0, 138432.1, 129436.00000000001, 139076.4, 136082.4, 137736.19999999998, 137824.69999999998, 128959.0, 135388.2, 135809.1, 137581.80000000002, 136938.8, 136304.90000000002, 136681.99999999997, 134261.5, 137809.5, 138928.19999999998, 129715.09999999999, 138203.09999999998, 136489.7, 140800.8, 134207.80000000002, 136273.8, 139960.19999999998, 130941.29999999999, 136934.69999999998, 136005.8, 134166.80000000002, 139413.89999999997, 140435.3, 136937.39999999997, 135635.1, 135442.09999999998, 135160.3, 134974.69999999998, 136673.39999999997, 141194.3, 129134.59999999998, 134061.3, 137341.09999999998, 135485.9, 134466.90000000002],
#          [133747.3, 130373.10000000002, 134022.5, 131207.0, 136464.8, 139572.80000000002, 131559.5, 135658.0, 134938.19999999998, 138080.4, 138048.60000000003, 134969.59999999998, 132083.89999999997, 134762.0, 141054.4, 135729.6, 138454.0, 139547.9, 139067.3, 129461.39999999998, 135202.30000000005, 130133.7, 136672.69999999998, 138014.30000000002, 132290.4, 141927.69999999998, 139730.30000000002, 139425.69999999998, 137715.09999999998, 135748.80000000002, 137391.2, 140768.8, 135972.2, 126544.19999999998, 136820.8, 140881.3, 139655.99999999997, 134334.4, 136845.2, 139008.19999999998, 136965.09999999998, 128380.1, 137881.80000000002, 137162.69999999998, 138676.69999999998, 127917.00000000001, 136611.9, 129715.09999999999, 137430.8, 142888.5, 137387.0, 140157.69999999998, 143142.6, 135812.7, 134979.7, 130295.6, 141194.3, 138768.0, 135462.4, 136869.3, 136666.1, 143107.19999999998, 135476.19999999998, 146649.4, 139628.59999999998, 143396.9, 134536.9, 136407.3, 132785.99999999997, 132152.4, 141059.69999999998, 139761.4, 140432.4, 132272.19999999998, 140507.4, 135231.0, 136760.80000000002, 132274.5, 135207.1, 135160.3, 134267.69999999998, 136457.5, 141692.4, 130761.90000000001, 135151.0, 142065.6, 136187.59999999998, 142021.00000000003, 139708.8, 135896.5, 134855.7, 136465.80000000002, 135468.9, 134281.5, 141742.19999999998, 138420.9, 130626.2, 139276.69999999998, 137421.0, 130134.4]
#        ]
result = [[133747.3, 121170.40000000001, 111528.80000000003, 103749.40000000004, 98494.40000000004, 93315.40000000004, 88181.60000000003, 84301.00000000003, 79527.50000000001, 77407.20000000001, 75374.3, 73411.0, 70537.5, 68723.59999999999, 66288.19999999998, 63704.0, 61075.7, 60124.0, 58273.0, 57139.4, 55650.4, 54534.90000000001, 53762.600000000006, 52885.9, 50847.899999999994, 50327.6, 48959.6, 48628.700000000004, 48074.2, 47698.799999999996, 47432.19999999999, 47230.09999999999, 46276.99999999999, 45986.59999999999, 45798.6, 45659.799999999996, 45681.7, 45714.899999999994, 45681.7, 45261.09999999999, 45042.999999999985, 44808.79999999999, 44776.89999999999, 44711.09999999999, 44623.799999999996, 44601.899999999994, 44472.49999999999, 44559.09999999999, 44405.69999999999, 44319.09999999999, 44305.59999999999, 44213.09999999999, 44212.3, 44254.799999999996, 44212.3, 43362.80000000001, 42742.30000000001, 42681.90000000001, 42724.4, 42602.2, 42264.2, 41636.8, 41814.3, 41383.0, 41205.5, 41344.3, 41309.5, 41170.700000000004, 41309.5, 41324.0, 41309.5, 41324.0, 41185.2, 41362.7, 41185.2, 41212.3, 41351.1, 41324.0, 41185.2, 40682.7, 40668.200000000004, 40196.700000000004, 40211.2, 40388.7, 40655.3, 40682.40000000001, 40831.40000000001, 40564.8, 40537.7, 40564.8, 40537.7, 40564.8, 40415.8, 40564.8, 40641.5, 40546.7, 40470.0, 40546.7, 40723.7, 40623.99999999999],
          [133747.3, 118946.0, 111788.49999999999, 100287.4, 93251.79999999999, 87994.5, 85157.3, 82645.49999999999, 78170.7, 75962.90000000001, 73792.40000000001, 71978.90000000001, 70601.00000000001, 68167.40000000001, 66887.80000000002, 64388.20000000001, 62013.10000000001, 61210.70000000001, 60305.20000000002, 59645.900000000016, 57642.50000000001, 56240.90000000001, 55292.50000000001, 54592.100000000006, 53977.200000000004, 52355.0, 51920.899999999994, 51001.0, 50371.399999999994, 49764.9, 48615.5, 47777.799999999996, 47767.59999999999, 47565.7, 47260.799999999996, 47245.6, 47074.2, 46972.6, 45994.9, 46005.1, 45682.5, 45260.7, 44983.399999999994, 44973.2, 44781.899999999994, 44806.899999999994, 44682.09999999999, 44692.299999999996, 44624.09999999999, 44556.89999999999, 44537.899999999994, 44701.1, 44537.899999999994, 44331.59999999999, 44321.399999999994, 43938.2, 44059.899999999994, 44178.799999999996, 43975.19999999999, 42733.59999999999, 42642.19999999999, 42400.19999999999, 42263.09999999999, 42138.299999999996, 42131.299999999996, 42139.299999999996, 41219.7, 41129.9, 41099.5, 41130.3, 39661.9, 39673.700000000004, 39661.9, 39528.7, 39540.5, 39677.600000000006, 39251.200000000004, 39455.0, 39277.5, 39455.0, 39606.2, 39388.299999999996, 39607.69999999999, 39606.79999999999, 39330.399999999994, 39071.2, 39330.399999999994, 39331.299999999996, 39042.6, 39265.299999999996, 39471.399999999994, 39252.0, 39315.3, 39397.9, 39426.5, 39397.9, 39273.100000000006, 39301.700000000004, 39508.700000000004, 38780.100000000006],
          [133747.3, 117108.70000000001, 111081.00000000001, 98504.10000000003, 91683.10000000002, 87616.60000000002, 83497.90000000002, 79440.90000000002, 76870.70000000003, 73039.9, 70987.5, 68438.79999999999, 65905.0, 61805.0, 60474.5, 59548.200000000004, 58759.1, 57884.19999999999, 57106.499999999985, 56495.19999999999, 55265.99999999999, 54734.999999999985, 53641.29999999999, 52504.99999999999, 52034.59999999999, 50757.79999999999, 49809.29999999999, 49317.799999999996, 48872.6, 48187.3, 47837.09999999999, 47560.7, 47252.1, 46390.7, 45135.2, 44957.0, 44822.600000000006, 44532.3, 44159.4, 43867.6, 43673.200000000004, 43548.4, 43482.1, 43298.5, 43212.1, 43208.3, 43333.1, 42009.799999999996, 42050.899999999994, 42117.2, 42228.2, 42242.29999999999, 42131.29999999999, 42242.29999999999, 42333.69999999999, 42222.69999999999, 41965.399999999994, 42044.59999999999, 42155.59999999999, 41991.59999999999, 41726.09999999999, 41615.09999999999, 41471.19999999999, 41580.899999999994, 41048.79999999999, 41034.7, 40968.399999999994, 41093.2, 41134.299999999996, 41211.8, 40968.399999999994, 40551.1, 40802.6, 41046.0, 41236.1, 41433.5, 41145.299999999996, 40992.7, 41145.299999999996, 41411.9, 41259.3, 41497.8, 41700.100000000006, 42059.200000000004, 42075.40000000001, 41697.20000000001, 41755.30000000001, 41473.1, 41809.600000000006, 41473.1, 41350.0, 41566.2, 41708.4, 42003.2, 41906.600000000006, 41655.100000000006, 41744.00000000001, 41477.4, 41195.3, 41281.200000000004],
          [133747.3, 121170.40000000001, 114029.30000000003, 104207.20000000003, 98290.30000000003, 94171.60000000002, 90807.50000000001, 86712.00000000001, 83511.50000000001, 78376.30000000002, 75806.10000000002, 73356.50000000001, 71300.30000000002, 68363.3, 66876.8, 64750.5, 63271.50000000001, 61964.000000000015, 60848.70000000001, 58310.60000000001, 57555.50000000001, 55132.50000000001, 54174.3, 53515.600000000006, 52799.7, 52316.399999999994, 51296.299999999996, 50495.49999999999, 49808.99999999999, 49190.5, 48630.3, 48153.399999999994, 46461.69999999999, 45273.29999999999, 44464.89999999999, 44363.29999999999, 44168.499999999985, 43125.89999999999, 43166.19999999999, 43257.899999999994, 42242.69999999999, 42121.69999999999, 41804.899999999994, 41464.299999999996, 41468.899999999994, 40933.2, 41016.399999999994, 41055.1, 39754.9, 39590.799999999996, 39694.1, 39584.8, 39694.1, 39584.8, 39481.5, 39584.8, 39479.3, 39504.3, 39613.6, 39767.0, 39957.1, 39847.8, 39957.1, 39847.8, 39657.700000000004, 39767.0, 39738.700000000004, 39585.3, 39538.6, 39681.1, 39577.799999999996, 39537.9, 39584.6, 39238.2, 39191.49999999999, 39238.2, 39362.99999999999, 39582.39999999999, 39362.99999999999, 39316.299999999996, 39199.1, 39239.0, 39324.9, 39231.399999999994, 39324.9, 39490.7, 39367.6, 39490.7, 39367.6, 39490.7, 39259.899999999994, 39136.799999999996, 39204.4, 39293.3, 39253.4, 39073.8, 39214.200000000004, 38992.100000000006, 38788.3, 38940.9],
          [133747.3, 124105.70000000001, 116948.2, 109168.80000000002, 94367.50000000001, 90460.00000000001, 86579.40000000001, 81322.1, 77453.9, 73608.59999999999, 71872.9, 70447.1, 68236.9, 66938.2, 65745.29999999999, 64596.59999999999, 63939.0, 62200.00000000001, 61050.8, 60366.3, 59916.2, 57689.1, 57386.6, 56711.1, 55621.00000000001, 53961.8, 51856.1, 51556.5, 49942.80000000001, 49525.600000000006, 47638.9, 46982.80000000001, 46911.80000000001, 46267.80000000001, 45964.50000000001, 45886.9, 45388.3, 45144.1, 44985.799999999996, 44504.0, 44411.5, 44584.5, 44020.4, 43788.600000000006, 43913.40000000001, 43788.600000000006, 43737.100000000006, 43639.3, 43690.8, 43111.8, 43060.3, 43176.80000000001, 43172.3, 43167.200000000004, 42468.700000000004, 42334.4, 42217.3, 42252.3, 41908.200000000004, 41959.700000000004, 42084.5, 41862.100000000006, 41684.200000000004, 41496.3, 41674.200000000004, 41255.100000000006, 41466.70000000001, 41415.20000000001, 41237.3, 41025.700000000004, 41203.600000000006, 41025.700000000004, 41237.3, 41001.700000000004, 41053.200000000004, 40992.40000000001, 40940.90000000001, 40729.3, 40780.8, 40965.30000000001, 40448.6, 40294.8, 40482.7, 40211.6, 40160.1, 40130.3, 39869.5, 39421.5, 39461.4, 39512.9, 39461.4, 39491.2, 39370.899999999994, 39345.899999999994, 39507.1, 39077.4, 38995.700000000004, 39252.5, 38995.700000000004, 39077.4]

          ]
mean = []
for i in range(len(result[0])):
    item = 0
    for j in range(5):
        item += result[j][i]
    mean += [item/5]
    
print(mean)