# Phishing detection AI from scratch.

Makes use of Phishtank online valid datasets and Cisco Umbrella top 1 million domains list, to train a recurrent neural network to classify domain names as phishing or not phishing.

Run the dataset_downloader.py to download one new sample from phishtank and merge any new urls into the combined dataset. Could be automated using crontab.

### Youtube video walthrough of the code:

[![](http://img.youtube.com/vi/ak10IUlVsvA/0.jpg)](http://www.youtube.com/watch?v=ak10IUlVsvA "")

# Results

### Accuracy vs decision threshold:
The neural network outputs values between 0 and 1. The threshold where the decision is made determines the various detection rates.

<object data="https://github.com/maximsachs/phishing_classification_recurrent_nn/raw/master/threshold_statistics_sweep.pdf" type="application/pdf" width="700px" height="700px">
    <embed src="https://github.com/maximsachs/phishing_classification_recurrent_nn/raw/master/threshold_statistics_sweep.pdf">
        <p>The detection rates for various thresholds: <a href="https://github.com/maximsachs/phishing_classification_recurrent_nn/raw/master/threshold_statistics_sweep.pdf">Download PDF</a>.</p>
    </embed>
</object>

### Sample prediction distribution for the best threshold:

<object data="https://github.com/maximsachs/phishing_classification_recurrent_nn/raw/master/outcome_distributions.pdf" type="application/pdf" width="700px" height="700px">
    <embed src="https://github.com/maximsachs/phishing_classification_recurrent_nn/raw/master/outcome_distributions.pdf">
        <p>The distribution of samples with their prediction outputs visualised to see TN, FP, FN and TP: <a href="https://github.com/maximsachs/phishing_classification_recurrent_nn/raw/master/outcome_distributions.pdf">Download PDF</a>.</p>
    </embed>
</object>

### Example output

```
Best performance at threshold: 0.7555276381909548
Calculated 7695 predictions with a mean value of 0.4602312743663788
Evaluating using threshold 0.7555276381909548
Cut-off threshold: 0.7555
Evaluation counts: {'TN': 3902, 'FP': 463, 'FN': 395, 'TP': 2935}
+-----------------+----------------+--------------------+
| Accuracy 88.85% | Predicted safe | Predicted phishing |
+-----------------+----------------+--------------------+
|   Not phishing  |    TN: 3902    |      FP: 463       |
|                 |  NPV: 90.808%  |    FDR: 13.626%    |
|                 |  TNR: 89.393%  |    FPR: 10.607%    |
|   Is phishing   |    FN: 395     |      TP: 2935      |
|                 |  FOR: 9.192%   |    PPV: 86.374%    |
|                 |  FNR: 11.862%  |    TPR: 88.138%    |
+-----------------+----------------+--------------------+

Examples for TN Bin range: 6.6296548e-06 - 0.15104796 , Num. Samples: 3620
                                       input  ground truth  prediction
0                                dlogixs.com             0    0.002675
1               fairprice.api.useinsider.com             0    0.000032
2                           datafield-hk.com             0    0.022040
3   -odc.samsungapps.com.gslb.cdnetworks.net             0    0.000026
4                          en.touhouwiki.net             0    0.111190
5                              v1.ayjpalf.ru             0    0.000008
6                           konnectodial.com             0    0.051903
7                                     kdo.de             0    0.000515
8                           vra.outbrain.com             0    0.000021
9                               oodleimg.com             0    0.085622
10                        mail.valorunico.cl             0    0.000055
11                            m24.kjecppw.cc             0    0.000008
12                            concent.com.br             0    0.000011
13                           shop.jisuapp.cn             0    0.000031
14               identity.ciam.refinitiv.net             0    0.000007

Examples for TN Bin range: 0.15104796 - 0.30208927 , Num. Samples: 102
                       input  ground truth  prediction
0                zdwcxfe.com             0    0.183455
1               labo-team.fr             0    0.160546
2             interthinx.com             0    0.157220
3                 datanet.iq             0    0.219580
4       mail.asiaertebat.com             0    0.194294
5              cookiepro.com             0    0.256896
6         theedgemarkets.com             0    0.165590
7         www.fednetbank.com             0    0.186842
8              www.msq88.com             0    0.254356
9   www.downiestatistics.com             0    0.196170
10           produitlive.com             0    0.178915
11          euemazure.ey.com             0    0.283395
12           hotelrunner.com             0    0.291902
13                 abramo.it             0    0.176437
14           newcampaigns.pl             0    0.283066

Examples for TN Bin range: 0.30208927 - 0.4531306 , Num. Samples: 68
                                       input  ground truth  prediction
0                             alahmadani.com             0    0.442474
1                            cdcservices.com             0    0.405938
2                                 xialwqe.ru             0    0.372986
3                             hon-win.com.cn             0    0.341402
4                                zuowen8.com             0    0.428328
5             credleaderboard.firebaseio.com             0    0.365162
6                           cujonevilofe.com             0    0.397637
7                        bokormas.dyndns.biz             0    0.314557
8                        estes-equipment.com             0    0.448628
9                       yasamboyuogrenim.com             0    0.321593
10                       locke.neobright.net             0    0.305679
11                         edge.udmserve.net             0    0.359595
12                                   udmr.ru             0    0.406787
13                         www.tagserve.asia             0    0.407259
14  pr1m08phcga89.s3.us-west-2.amazonaws.com             0    0.441766

Examples for TN Bin range: 0.4531306 - 0.60417193 , Num. Samples: 45
                            input  ground truth  prediction
0                   uhcarcade.com             0    0.543132
1      medidor.turbonetssp.com.br             0    0.576397
2           candy.jp-brothers.com             0    0.502245
3                lingtianmold.com             0    0.562866
4                     sothuchi.vn             0    0.455938
5                  mvhospital.net             0    0.518542
6         denbtiepd2.de.aosrv.com             0    0.525436
7       c2r7b7xk.v1d.pkoplink.com             0    0.548341
8             pendleton.sspinc.io             0    0.597321
9   examnet-176208.firebaseio.com             0    0.531097
10          appliedbiosystems.com             0    0.602869
11       podcastfeeds.nbcnews.com             0    0.564579
12              firsatlarshop.com             0    0.507331
13             isdschoolsmail.org             0    0.496355
14       mail.helairporttaksi.com             0    0.496934

Examples for TN Bin range: 0.60417193 - 0.75521326 , Num. Samples: 66
                                       input  ground truth  prediction
0                      www.thelivemirror.com             0    0.607597
1      uswstorage.oss-us-west-1.aliyuncs.com             0    0.730624
2                           tintucketoan.com             0    0.735861
3                                 gyrxttt.su             0    0.616638
4                               aermacchi.it             0    0.611230
5                                   oliac.pk             0    0.642718
6                            adextelecom.com             0    0.651698
7                             tuviglobal.com             0    0.677120
8                        freightinvestor.com             0    0.697711
9                           thefilmstage.com             0    0.731003
10                             rmbenasse.com             0    0.653530
11                               first-mg.de             0    0.700918
12  esumesearchstorage.blob.core.windows.net             0    0.747432
13                            sclubeuropa.it             0    0.648071
14                                ins.com.tr             0    0.752853

Examples for FP Bin range: 0.7574164 - 0.8059311 , Num. Samples: 14
                             input  ground truth  prediction
0                        koryu.com             0    0.777464
1                report.365you.com             0    0.797975
2       webmail.anforaformacion.es             0    0.790950
3                       mfydunx.ru             0    0.763983
4                mailout.ns01.info             0    0.794748
5                        cncrk.com             0    0.766324
6                     tir2bolt.xyz             0    0.760481
7             dpmailbu.doteasy.com             0    0.767257
8   ep-us-west-wa-02.flowroute.com             0    0.758322
9                     digopaul.com             0    0.757416
10                 www.acompli.com             0    0.780901
11                    mamalisa.com             0    0.803154
12                    gearhost.com             0    0.786216
13                ozerparkotel.com             0    0.779360

Examples for FP Bin range: 0.8059311 - 0.8544458 , Num. Samples: 28
                              input  ground truth  prediction
0   languagelearningwithnetflix.com             0    0.842674
1                        telecom.mu             0    0.813443
2           bigmooseproductions.com             0    0.836675
3                hogwartsishere.com             0    0.819805
4                 rateyourmusic.com             0    0.840521
5                     huflit.edu.vn             0    0.836330
6                 johnhenrymahr.com             0    0.811060
7          teamobjectifaventure.com             0    0.829121
8                   global-roam.com             0    0.851315
9               amateurgayclips.com             0    0.841719
10                 amctextil.com.br             0    0.810374
11                   zenshin.com.ph             0    0.843911
12       www.hangchinhhanggiare.com             0    0.839857
13                www.desir-cam.com             0    0.837189
14        amandabeautycenter.com.br             0    0.838762

Examples for FP Bin range: 0.8544458 - 0.9029605 , Num. Samples: 31
                        input  ground truth  prediction
0                    flair.co             0    0.859403
1   playstationexperience.net             0    0.868899
2             www.yjcf360.com             0    0.871511
3    ookla.fastxbroadband.com             0    0.870116
4           www.areafokus.com             0    0.876992
5              optimalbux.com             0    0.874091
6                  ak-ort.com             0    0.879341
7        brisbanetimes.com.au             0    0.864254
8              oaeeckakci.com             0    0.891409
9         stonks.widgetbot.io             0    0.879586
10              baicizhan.org             0    0.890082
11     down.zhilingshidai.com             0    0.870641
12                  cicese.mx             0    0.855197
13        weimiaocaishang.com             0    0.884302
14                wakemed.org             0    0.865121

Examples for FP Bin range: 0.9029605 - 0.9514752 , Num. Samples: 63
                         input  ground truth  prediction
0                  espalais.fr             0    0.951184
1          trimun.lagivado.com             0    0.932640
2         theforanexchange.com             0    0.937796
3                turdayma.info             0    0.945138
4                hostcenter.dk             0    0.933696
5                  america.net             0    0.916790
6              mail.pyramis.fi             0    0.931681
7                amazonpmi.com             0    0.947179
8   domainsregistrationapi.com             0    0.929311
9               resdingtone.me             0    0.949165
10                    youla.io             0    0.913650
11                 aerostar.ro             0    0.909746
12          www.extremeplus.it             0    0.949173
13            affinbank.com.my             0    0.927267
14               stockstar.com             0    0.936368

Examples for FP Bin range: 0.9514752 - 0.99998987 , Num. Samples: 326
                           input  ground truth  prediction
0                majadahonda.org             0    0.999375
1      clientfiles.tmpwebeng.com             0    0.999911
2          www.orientfreight.com             0    0.994013
3                    panduit.com             0    0.999745
4          bomenservice-zuid.com             0    0.999684
5              salfamontajes.com             0    0.998994
6       essays-termpapers2go.com             0    0.987707
7            first-resources.com             0    0.964477
8   whatchristianswanttoknow.com             0    0.999529
9                     alimc3.top             0    0.999864
10              storeimaging.com             0    0.999724
11               securelinks.net             0    0.998143
12            files.keyreply.com             0    0.994470
13                     goaaa.com             0    0.973565
14     redhillchurchofchrist.org             0    0.999557

Examples for FN Bin range: 8.355906e-06 - 0.14803024 , Num. Samples: 275
                         input  ground truth  prediction
0        www.man1bantul.sch.id             1    0.002277
1   mysite.plexusworldwide.com             1    0.000027
2              accesso-mps.com             1    0.000083
3                betqiuqiu.com             1    0.001756
4                medhermes.net             1    0.003648
5              wwwfacebook.org             1    0.021296
6                 taengball.co             1    0.056845
7                 iokainle.fun             1    0.057070
8              vki.vipcentr.ru             1    0.014383
9               fusionfitn.com             1    0.004113
10           www.34.miktd7.com             1    0.001106
11                   cornia.in             1    0.028525
12           battlegrownds.com             1    0.003919
13         baltijosloto.opo.lt             1    0.012160
14   e.t.s.interac.ca-app.club             1    0.015846

Examples for FN Bin range: 0.14803024 - 0.2960521 , Num. Samples: 36
                                       input  ground truth  prediction
0                          amazonm-thtru.pro             1    0.212129
1                                 734231.com             1    0.206223
2                          jamupasakbumi.com             1    0.159967
3                               laserland.by             1    0.165746
4                            rsrsurprise.com             1    0.185366
5                             techinfobd.net             1    0.193354
6                          techasteroids.com             1    0.268435
7              billingsmontanarealestate.com             1    0.194124
8   dauthowa.fra1.cdn.digitaloceanspaces.com             1    0.158757
9                  dvla-vehicletaxrefund.com             1    0.251008
10                               kent.com.bd             1    0.158588
11                       pixelbenchmarks.com             1    0.174780
12                          baanlaesuans.com             1    0.262554
13                              pranavida.cl             1    0.158021
14                                734231.com             1    0.206223

Examples for FN Bin range: 0.2960521 - 0.44407398 , Num. Samples: 24
                            input  ground truth  prediction
0          www.quantumfitness.com             1    0.361186
1                 aladdinstar.com             1    0.424780
2                     rubysoap.hk             1    0.352645
3            ketoneswithmindy.com             1    0.413272
4                securenet-pp.com             1    0.347048
5             harpiaadventure.com             1    0.307106
6   microsoft-excel.kr.jaleco.com             1    0.305564
7           havantsurveyors.co.uk             1    0.307383
8       www.cr.mnfg.shwxtfood.com             1    0.310780
9       emsi-lobo.firebaseapp.com             1    0.416162
10                   smartmco.com             1    0.354033
11       www.duffywholesalers.com             1    0.438219
12           cesta-americanas.com             1    0.388964
13                jeffreybcam.net             1    0.394956
14              www.faxitalia.com             1    0.347434

Examples for FN Bin range: 0.44407398 - 0.59209585 , Num. Samples: 28
                               input  ground truth  prediction
0                       uzbekart.com             1    0.533469
1                          ucxuc.com             1    0.550148
2                org-nr.yolasite.com             1    0.552236
3                  emasresources.com             1    0.590512
4                 newdetails-3.world             1    0.462371
5             ronhommelfotografie.nl             1    0.584028
6                correiopaulista.com             1    0.496955
7                       sistemhr.com             1    0.591904
8                     crisisomar.net             1    0.475834
9                org-nr.yolasite.com             1    0.552236
10               help-0024511457.xyz             1    0.488397
11  review01-supportapple.xyxxon.com             1    0.455973
12         nuevoamanecercolombia.com             1    0.557255
13                    amezglobal.com             1    0.535588
14           www.getmefranchise.info             1    0.504285

Examples for FN Bin range: 0.59209585 - 0.7401177 , Num. Samples: 31
                                       input  ground truth  prediction
0                         www.secure.mwwi.pl             1    0.646337
1                           skins-casino.com             1    0.617467
2                       londonshortstays.com             1    0.641500
3                        katherinegesell.com             1    0.654144
4                      www.vindanamobile.com             1    0.717523
5                      dynamicdesignsinc.net             1    0.707900
6   w.invite-grub-whatsappsex-chat.2waky.com             1    0.662419
7                           www.jetcraft.com             1    0.642037
8                                   aurix.ro             1    0.668920
9                     www.serviziappbank.com             1    0.685895
10                   dbs.rewardgateway.co.uk             1    0.719831
11                              alumdecor.ru             1    0.676338
12                                    hap.io             1    0.638569
13                      www.toancaupumps.com             1    0.727888
14                         www.taxiample.com             1    0.684279

Examples for TP Bin range: 0.7569905 - 0.805591 , Num. Samples: 27
                           input  ground truth  prediction
0                  ukdvlatax.com             1    0.800841
1                      satkom.id             1    0.756990
2                   welasyia.com             1    0.786966
3                      satkom.id             1    0.756990
4                  turkstore.net             1    0.780650
5               aurickhotels.com             1    0.774534
6   bayanicgiyimsitesi.somee.com             1    0.764003
7         uofc-my.sharepoint.com             1    0.774488
8             lavienailscorp.com             1    0.802538
9                      aflbd.net             1    0.797983
10             deviceattempt.com             1    0.775647
11               zeebracross.com             1    0.796079
12          backyarddelivery.com             1    0.779522
13         www.alqurancampus.com             1    0.760257
14             stephaneledro.com             1    0.772025

Examples for TP Bin range: 0.805591 - 0.8541914 , Num. Samples: 33
                                       input  ground truth  prediction
0                                 paipale.ml             1    0.824391
1                            rabosafetyy.xyz             1    0.840437
2                      lu9-my.sharepoint.com             1    0.842121
3                             baobulksms.com             1    0.853588
4   .bancodebogota.com.co.aceitesymas.com.mx             1    0.816174
5                                 suxury.com             1    0.830553
6                           in-medias-res.it             1    0.817654
7                             ajaxfrance.com             1    0.811190
8                                   ehan.org             1    0.845986
9                    www.ktplasmachinery.com             1    0.810302
10                 timetravel.mementoweb.org             1    0.842011
11                   congressoagrotec.com.br             1    0.825719
12  fspsv7.k9l7d5k8uutps498.rebelyell.agency             1    0.841047
13                         ellasuniforms.com             1    0.841626
14                                  kjsa.com             1    0.853723

Examples for TP Bin range: 0.8541914 - 0.9027919 , Num. Samples: 45
                                       input  ground truth  prediction
0                        www.mokshshanti.com             1    0.874623
1                                 meetme.run             1    0.863964
2                                vhmrics.com             1    0.865939
3                              mybill-o2.com             1    0.862201
4                               mulnored.com             1    0.873008
5   NvbQ==Memberservices&amp;legalshieldcorp             1    0.858713
6                                 jagex.club             1    0.864284
7                        www.lovetheedit.com             1    0.875986
8   983499-secondary.z6.web.core.windows.net             1    0.863342
9                              hisyo.main.jp             1    0.867997
10  jonkwowa.fra1.cdn.digitaloceanspaces.com             1    0.863365
11                            squamfreup.com             1    0.896652
12                              nartsokb.com             1    0.899637
13                          isabellacano.com             1    0.858607
14                        updatefbsecure.com             1    0.895199

Examples for TP Bin range: 0.9027919 - 0.95139235 , Num. Samples: 90
                             input  ground truth  prediction
0                           lmy.de             1    0.932130
1               cancelnewdevice.cc             1    0.951213
2        pendingreview-account.com             1    0.949510
3                     ctamedia.net             1    0.924627
4                rekvtanm-eoivf.cc             1    0.940937
5          luckyspin20.pubgm.co.in             1    0.906129
6                    nirmalind.com             1    0.950144
7                   www.nabacc.com             1    0.923543
8   umconnectumt-my.sharepoint.com             1    0.936156
9                urbanmeisters.ovh             1    0.947217
10          joinngrubwa.itsaol.com             1    0.947602
11                 patchcracks.com             1    0.944506
12               o2-my-account.com             1    0.944245
13                    sentraco.com             1    0.934767
14                     jmcnoack.cl             1    0.914810

Examples for TP Bin range: 0.95139235 - 0.99999285 , Num. Samples: 2739
                                       input  ground truth  prediction
0                   www.vadodaramarathon.com             1    0.997816
1            halifax-deviceauthenticator.com             1    0.999815
2                              52e4t.csb.app             1    0.999971
3                          aomuabinhtien.com             1    0.991657
4                                    i-ta.cc             1    0.999882
5          fistgradekhjwdmjhfemfe.weebly.com             1    0.999985
6           halifax.fraudalerts-payments.com             1    0.999990
7           www.lloyds.fraudpaymentalert.com             1    0.998945
8                       lnk.pmlti-etai-2.ovh             1    0.994699
9    onlineyahoo-vericationcenter.weebly.com             1    0.999982
10                     cirodentalperu.online             1    0.999927
11                        firmaadicional.com             1    0.997154
12                              garionac.com             1    0.967664
13                    ladycavendishdiary.com             1    0.974894
14  rket-place-item-723465123.achsnmlion.win             1    0.989723

Phishing ULR examples:
Prediction on url: frgcxtmjawefgrthdcusge.dab 0.9682055
Prediction on url: evilmadeupurl.phish 0.929837
Prediction on url: evil.madeupurl.phish 0.0158896

Safe URL examples:
Prediction on url: google.com 0.00012256467
Prediction on url: www.google.com 0.00025575052
Prediction on url: gmail.google.com 8.538672e-06
Prediction on url: mail.google.com 8.285025e-06
Prediction on url: tudelft.nl 0.00022523031
Prediction on url: brightspace.tudelft.nl 0.9749136
Prediction on url: colab.research.google.com 7.819281e-06
Prediction on url: 00-gayrettepe-t3-8---00-gayrettepe-xrs-t2-1.statik.turktelekom.com.tr 3.510749e-05
```