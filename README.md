# Phishing detection AI from scratch.

Makes use of Phishtank online valid datasets and Cisco Umbrella top 1 million domains list, to train a recurrent neural network to classify domain names as phishing or not phishing.

Run the dataset_downloader.py to download one new sample from phishtank and merge any new urls into the combined dataset. Could be automated using crontab.

### Youtube video walthrough of the code:

[![](http://img.youtube.com/vi/ak10IUlVsvA/0.jpg)](http://www.youtube.com/watch?v=ak10IUlVsvA "")

# Results

### Accuracy vs decision threshold:
The neural network outputs values between 0 and 1. The threshold where the decision is made determines the various detection rates.

[![](https://github.com/maximsachs/phishing_classification_recurrent_nn/raw/master/threshold_statistics_sweep.png)](https://github.com/maximsachs/phishing_classification_recurrent_nn/raw/master/threshold_statistics_sweep.pdf "")

### Sample prediction distribution for the best threshold:
The distribution of samples with their prediction outputs visualised to see TN, FP, FN and TP:

[![](https://github.com/maximsachs/phishing_classification_recurrent_nn/raw/master/outcome_distributions.png)](https://github.com/maximsachs/phishing_classification_recurrent_nn/raw/master/outcome_distributions.pdf "")

### Example output

```
Best performance at threshold: 0.5655778894472362
Calculated 7876 predictions with a mean value of 0.4562220573425293
Evaluating using threshold 0.5655778894472362
Cut-off threshold: 0.5656
Evaluation counts: {'TN': 3891, 'FP': 506, 'FN': 435, 'TP': 3044}
+------------------+----------------+--------------------+
| Accuracy 88.052% | Predicted safe | Predicted phishing |
+------------------+----------------+--------------------+
|   Not phishing   |    TN: 3891    |      FP: 506       |
|                  |  NPV: 89.945%  |    FDR: 14.254%    |
|                  |  TNR: 88.492%  |    FPR: 11.508%    |
|   Is phishing    |    FN: 435     |      TP: 3044      |
|                  |  FOR: 10.055%  |    PPV: 85.746%    |
|                  |  FNR: 12.504%  |    TPR: 87.496%    |
+------------------+----------------+--------------------+

Examples for TN Bin range: 7.317396e-06 - 0.11298742 , Num. Samples: 3462
                                input  ground truth  prediction
0                llnw.daps.nbcuni.com             0    0.000118
1              speedtest.wispwest.net             0    0.000050
2                     m13.rsefukf.com             0    0.000032
3                     m15.dcbxlrj.org             0    0.000008
4   edge-091.sgsin.icloud-content.com             0    0.000015
5                   mail.novuscom.net             0    0.000012
6                          xghelp.com             0    0.005918
7                linuxfromscratch.org             0    0.024444
8      r1.sn-5ualdn7y.googlevideo.com             0    0.000011
9                     m40.dyopshw.com             0    0.000246
10        gaplecdn.aliyun.joyours.com             0    0.000438
11                       cdn.epica.ai             0    0.000028
12                  siorc.xfinity.com             0    0.000428
13                   110.mimilcnf.pro             0    0.000041
14                        aslroma1.it             0    0.004463

Examples for TN Bin range: 0.11298742 - 0.22596753 , Num. Samples: 157
                         input  ground truth  prediction
0                   reamaze.io             0    0.188346
1               www.wisksl.com             0    0.134943
2             pollosgar.com.co             0    0.183440
3           hm.vuicungdafa.com             0    0.161075
4      mail.guoceratile.com.my             0    0.133046
5                      ggwp.id             0    0.191724
6             oceans-nadia.com             0    0.149921
7               jieqinwang.com             0    0.148553
8               v.lsttnews.com             0    0.141278
9   liveme.zgsgllive.linkv.fun             0    0.191640
10         nws.etemavrajoip.fr             0    0.136429
11             portforward.com             0    0.122953
12     98kz-alternate.app.link             0    0.186109
13               emailsrvr.com             0    0.213246
14           static.f-list.net             0    0.124085

Examples for TN Bin range: 0.22596753 - 0.33894762 , Num. Samples: 105
                       input  ground truth  prediction
0           fastcomments.com             0    0.324313
1             elsenbruch.com             0    0.231270
2                 zahori.com             0    0.272963
3             alex.kakao.com             0    0.263239
4   www.svfree.svgame168.com             0    0.228486
5          kashra-server.com             0    0.301930
6      mail.elcharcutero.com             0    0.326268
7           stratoserver.net             0    0.256581
8          votesouthwell.com             0    0.320887
9             www.amboss.com             0    0.275090
10             mx.interia.pl             0    0.274614
11             myconvene.com             0    0.240418
12                pchouse.gr             0    0.324463
13          intraplanner.com             0    0.272231
14         elnacional.com.do             0    0.330957

Examples for TN Bin range: 0.33894762 - 0.45192775 , Num. Samples: 73
                     input  ground truth  prediction
0   acdevelopmentgroup.com             0    0.353133
1              aaronsw.com             0    0.406117
2              gazt.gov.sa             0    0.386374
3              yhcgift.com             0    0.418845
4                javdb.com             0    0.354495
5     www.trainenquiry.com             0    0.419734
6       www.devexpress.com             0    0.373720
7      anferingenieria.com             0    0.438848
8       fusion-manager.com             0    0.374282
9               mqnrqbl.in             0    0.432225
10    citi.bridgetrack.com             0    0.439842
11     xlog-va.tiktokv.com             0    0.445081
12                 ghnd.fr             0    0.371937
13   billing.oknotify2.com             0    0.382837
14              300400.net             0    0.353102

Examples for TN Bin range: 0.45192775 - 0.56490785 , Num. Samples: 93
                                       input  ground truth  prediction
0                  sfd.et0978.epichosted.com             0    0.529685
1                        surgicalscience.com             0    0.559815
2                            privatemail.com             0    0.485508
3                          asemanfredonia.it             0    0.474472
4                                  mevris.io             0    0.474573
5                         xianghuanzhang.com             0    0.546445
6                         www.madridhifi.com             0    0.490822
7                mail.motivedynamicsmgmt.com             0    0.465295
8         user-media-upload.renderforest.com             0    0.538933
9                                 ffquan.com             0    0.551031
10                   kaptivoapi.kaptivo.live             0    0.515401
11                         scipublisherj.com             0    0.494632
12  08c374edcb87ab5cbdab24dc9.js.ubembed.com             0    0.462961
13                     fashioneditorials.com             0    0.486268
14                             shoplazza.com             0    0.484051

Examples for FP Bin range: 0.5741874 - 0.6593455 , Num. Samples: 58
                      input  ground truth  prediction
0        delta-searches.com             0    0.610190
1         luckyqueenpro.com             0    0.612061
2               pollmann.at             0    0.628621
3                   zbj.com             0    0.642035
4              zastatic.com             0    0.598736
5   freeonlineconverter.net             0    0.639440
6     freemalaysiatoday.com             0    0.634647
7            www.silive.com             0    0.574187
8       ariannelingerie.com             0    0.605711
9     go.publisher-news.com             0    0.636007
10      seancodynetwork.com             0    0.637383
11           indihome.co.id             0    0.583247
12            hortimail.com             0    0.647075
13          ljlpeinture.com             0    0.586821
14       hiddencamstube.com             0    0.614998

Examples for FP Bin range: 0.6593455 - 0.74450356 , Num. Samples: 60
                        input  ground truth  prediction
0            www.senate.go.th             0    0.682710
1           blackhole9999.com             0    0.671924
2            xnxx.tubekek.com             0    0.682402
3                   nasoe.org             0    0.725112
4               local.bark.us             0    0.684137
5              www.netapp.com             0    0.741023
6           www.molottery.com             0    0.689571
7              satismeter.com             0    0.736355
8           mqsrkvcpyzvnw.com             0    0.742406
9          bbbbbbbb.846846.de             0    0.680710
10              bsh-group.com             0    0.696653
11               dlr-hatc.com             0    0.683883
12          bibliotecasma.com             0    0.731776
13  bollingplasticsurgery.com             0    0.733331
14            ystrationa.info             0    0.741842

Examples for FP Bin range: 0.74450356 - 0.82966167 , Num. Samples: 68
                                input  ground truth  prediction
0   studyinsweden.easyvirtualfair.com             0    0.801279
1        mail.veiligheidsbeleving.com             0    0.751713
2                       fotoaziti.com             0    0.805599
3                         nettv4u.com             0    0.813323
4             live.outplaygamekit.com             0    0.824369
5                uiprxlbgfrxaxrwnh.in             0    0.746816
6            recaptcha.bittorrent.com             0    0.823070
7                       www.fun2u.biz             0    0.762361
8                 freightinvestor.com             0    0.747800
9                    servizioemail.it             0    0.809356
10         kaiserswerther-diakonie.de             0    0.824186
11                   www.europcar.com             0    0.800409
12                   www.pulsapay.com             0    0.809266
13                     ecoserveis.net             0    0.778508
14                         lkr5k85.cn             0    0.769014

Examples for FP Bin range: 0.82966167 - 0.9148197 , Num. Samples: 97
                          input  ground truth  prediction
0              b6b4rhsbdawj.com             0    0.901391
1    incrediblerugsanddecor.com             0    0.838826
2                  ramweb.co.za             0    0.874516
3            cbt-charpentier.fr             0    0.841216
4              beerrightnow.com             0    0.859271
5                 bdtsales.best             0    0.857589
6      boehringer-ingelheim.com             0    0.872133
7       www.dernieredemeure.com             0    0.908550
8                  reco.wynk.in             0    0.863313
9             acielcolombia.com             0    0.873488
10     www.alaskaredkitchen.com             0    0.911707
11  lyncdiscover.wellsfargo.com             0    0.832653
12         www.jobdiagnosis.com             0    0.890343
13         zh-hk.guitarians.com             0    0.898340
14  mail.kontaktlinsen-radar.de             0    0.882129

Examples for FP Bin range: 0.9148197 - 0.9999778 , Num. Samples: 222
                              input  ground truth  prediction
0                  gampangcod.my.id             0    0.998248
1             kath-dekanat-alzey.de             0    0.987271
2                www.jdsports.co.uk             0    0.997600
3                    delightfull.eu             0    0.966502
4           bipolaraustralia.org.au             0    0.924600
5                  essentialhome.eu             0    0.999747
6   consentmanager.mgr.consensu.org             0    0.967583
7         koodomobile.telus.digital             0    0.997511
8             bomenservice-zuid.com             0    0.916765
9                  virtuallawyer.se             0    0.988618
10                     redcalfs.com             0    0.986578
11                          baua.fr             0    0.983905
12     www.childsplayclothing.co.uk             0    0.999968
13                           wdm.pl             0    0.940031
14                    cimtav.com.tr             0    0.997630

Examples for FN Bin range: 8.67373e-06 - 0.112897925 , Num. Samples: 238
                                   input  ground truth  prediction
0                             moxisq.com             1    0.001682
1                      mail-generali.com             1    0.000243
2                    stearncommunily.com             1    0.029782
3                            newmy-3.com             1    0.007560
4                                shrt.es             1    0.012051
5                         elgabalawy.com             1    0.008782
6                                 hmp.me             1    0.043992
7          nice.constantcontactsites.com             1    0.000962
8             dubailuxurypropertiess.com             1    0.020251
9                          unnobzava.net             1    0.009643
10       selfish-cheese.aerobaticapp.com             1    0.005296
11  claro-controle-downloader.m4u.com.br             1    0.011110
12                        arcomindia.com             1    0.059921
13             e.t.s.interac.ca-app.club             1    0.000054
14                          donghuong.uk             1    0.002262

Examples for FN Bin range: 0.112897925 - 0.22578716 , Num. Samples: 44
                                       input  ground truth  prediction
0                      binarybenliveload.com             1    0.213511
1                             mtfirewood.com             1    0.186709
2                             propress.co.uk             1    0.173334
3          www.videosoy.reachhealthylife.com             1    0.135371
4                       axiomatickidneys.org             1    0.179086
5               codedrop.thevisionpoints.com             1    0.201330
6                            zinextworld.com             1    0.148280
7                          getyourtx-tdy.com             1    0.147874
8                             mtfirewood.com             1    0.186709
9   ge-id-7819108955.sycoexportimportltd.com             1    0.145995
10                www.scuolascigressoney.net             1    0.196822
11                         losmentirosos.com             1    0.160719
12                               ipp-inc.com             1    0.125211
13                              wikiform.org             1    0.116855
14                            careplayit.vip             1    0.129922

Examples for FN Bin range: 0.22578716 - 0.33867642 , Num. Samples: 50
                       input  ground truth  prediction
0          mackanthem.com.pe             1    0.306885
1             365playing.com             1    0.301153
2      elhogarproperties.com             1    0.264287
3             pandaimath.com             1    0.276507
4      playfirstoftheday.com             1    0.312422
5          expertcarzone.com             1    0.282245
6   sexeducation.atspace.com             1    0.239057
7         techsysnigeria.com             1    0.235290
8            jeffreybcam.net             1    0.230963
9          www.coderllci.com             1    0.299572
10            galvarburg.com             1    0.226562
11        contraprova.com.br             1    0.292125
12            pubgmdaily.com             1    0.299808
13            pkwmobilede.de             1    0.320379
14            7colours.co.za             1    0.230266

Examples for FN Bin range: 0.33867642 - 0.45156565 , Num. Samples: 52
                                       input  ground truth  prediction
0                             lassolinks.com             1    0.368287
1               marie02zue.azurewebsites.net             1    0.381409
2                          tomeigosto.com.br             1    0.363083
3                                   gradi.ba             1    0.434554
4                              foamnflow.com             1    0.395296
5                                  kisa.link             1    0.339635
6                      bizbizeturkiyenim.com             1    0.359583
7   asecure-messagesystem.thenailcabin.co.uk             1    0.372895
8                     autodiscover.gre.ac.uk             1    0.429600
9                             snarkysoap.com             1    0.350943
10                         aegisredmedia.com             1    0.438507
11                   freey-joingrub.otzo.com             1    0.381696
12                   graphicommunication.com             1    0.410395
13                              gold-mail.ru             1    0.409111
14          redirectlyoseven.firebaseapp.com             1    0.444133

Examples for FN Bin range: 0.45156565 - 0.5644549 , Num. Samples: 50
                                       input  ground truth  prediction
0   NvbQ==Memberservices&amp;legalshieldcorp             1    0.473352
1                       backyarddelivery.com             1    0.559786
2                        kbstitchdesigns.com             1    0.457322
3                     orthodoxresearcher.com             1    0.519094
4                           fedexvoyager.com             1    0.479571
5                         woodysportsbar.com             1    0.510820
6                  globaldoctorshospital.com             1    0.525911
7                        akannitoyegbola.com             1    0.454716
8                                fdriqtbt.cn             1    0.523340
9                     kellijophotography.com             1    0.502783
10                         plasticmonkey.com             1    0.487777
11                        www.bayernlbuk.net             1    0.563618
12                   www.ktplasmachinery.com             1    0.476686
13                            pochegroup.com             1    0.528044
14                            modesuites.com             1    0.471518

Examples for TP Bin range: 0.5688994 - 0.65511745 , Num. Samples: 66
                          input  ground truth  prediction
0            remnegocios.com.br             1    0.584870
1   neighbourhoodwatchcasey.com             1    0.569869
2      find-yourprofithere.life             1    0.633644
3               www.jfteabd.com             1    0.592988
4                www.mktbtk.com             1    0.579223
5         austinbeautyguide.com             1    0.646723
6              www.hoomokef.com             1    0.653069
7              essexminibus.com             1    0.588611
8                  olivaspa.com             1    0.624943
9              www.denartcc.org             1    0.572421
10                 tarelka67.ru             1    0.607841
11                   jagex.club             1    0.638270
12  www.tinavegaphotography.com             1    0.631984
13                  v-upd.co.uk             1    0.586614
14                  byoko.co.kr             1    0.603089

Examples for TP Bin range: 0.65511745 - 0.7413355 , Num. Samples: 65
                          input  ground truth  prediction
0            www.wonderstore.it             1    0.688639
1               pp-giftcard.com             1    0.715353
2                      ehan.org             1    0.718887
3            bonamourmarket.com             1    0.726458
4                mansdragon.com             1    0.686235
5   ded5441.inmotionhosting.com             1    0.706312
6                  dasktake.com             1    0.672902
7               patchcracks.com             1    0.663025
8                tierretyr.live             1    0.659768
9                   pubgner.com             1    0.700133
10                viewfbapp.com             1    0.721883
11                profalsam.com             1    0.730803
12           alealtaseguros.com             1    0.725690
13            limited-verify.me             1    0.681457
14                pubgmyace.com             1    0.711182

Examples for TP Bin range: 0.7413355 - 0.8275535 , Num. Samples: 110
                                  input  ground truth  prediction
0                     www.arrowcase.com             1    0.777720
1                          brighant.com             1    0.746563
2                      amazerpresce.com             1    0.813245
3             essentialshoppingmall.com             1    0.824800
4          privateinvestigatormilan.com             1    0.819198
5                    markareklamevi.com             1    0.814238
6                       epay-paxful.com             1    0.762931
7                  sakkiswonderland.com             1    0.787093
8                        hutoknepper.de             1    0.807550
9                       epay-paxful.com             1    0.762931
10                       ddotamoney.com             1    0.796305
11                      www.payinur.com             1    0.783428
12                     valeexpressa.com             1    0.742105
13  m.facebok-item-84372.vattrustbd.com             1    0.812274
14                      zeebracross.com             1    0.788122

Examples for TP Bin range: 0.8275535 - 0.91377157 , Num. Samples: 185
                         input  ground truth  prediction
0                   net-eco.fr             1    0.841986
1          ecscreditrepair.com             1    0.881374
2              www.rehrlbau.de             1    0.842446
3            destructoring.com             1    0.879459
4                    ucxuc.com             1    0.872591
5   unionheightsresidental.com             1    0.841180
6    liberbankos-prestades.com             1    0.908444
7          chirhoprecision.com             1    0.908011
8         gandjministorage.com             1    0.866434
9      ebay-payment-issues.com             1    0.847162
10       ruakunten.kadnanu.top             1    0.831892
11             boconceptla.com             1    0.883810
12       bahankuliahonline.com             1    0.851976
13      corewellnesshawaii.com             1    0.848730
14            fghjh.uioiuo.xyz             1    0.850209

Examples for TP Bin range: 0.91377157 - 0.9999896 , Num. Samples: 2613
                                       input  ground truth  prediction
0   u-dot-cedar-code-289917.nn.r.appspot.com             1    0.999989
1             netflix.error-with-billing.com             1    0.999882
2                         psych-k-online.com             1    0.999736
3                                pubg-as.com             1    0.915831
4                    unknowninfo-online.link             1    0.998208
5                 www.academiafleming.com.pe             1    0.984846
6                llojas-americanas.ezyro.com             1    0.999285
7               windowinstallationtoronto.ca             1    0.994219
8   leappsecurehalifacxappsecure.wikiamuz.ir             1    0.999947
9                  raokuten.co.jp.amozj.buzz             1    0.999732
10                     truenorthstrength.com             1    0.947873
11              services.runescape.com-zx.ru             1    0.999986
12                   www.bp-atualiza-app.com             1    0.997780
13                 fbcom-32601355.chekkos.mx             1    0.999840
14                                 hatac.net             1    0.994230

Phishing ULR examples:
Prediction on url: frgcxtmjawefgrthdcusge.dab 0.0037203317
Prediction on url: evilmadeupurl.phish 0.633814
Prediction on url: evil.madeupurl.phish 0.00034718902

Safe URL examples:
Prediction on url: google.com 0.4695877
Prediction on url: www.google.com 0.23997158
Prediction on url: gmail.google.com 6.3069674e-05
Prediction on url: mail.google.com 0.00013527935
Prediction on url: tudelft.nl 0.031315554
Prediction on url: brightspace.tudelft.nl 0.9944102
Prediction on url: colab.research.google.com 0.0001981094
Prediction on url: 00-gayrettepe-t3-8---00-gayrettepe-xrs-t2-1.statik.turktelekom.com.tr 0.0064572464
```