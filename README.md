# Phishing detection AI from scratch.

Makes use of Phishtank online valid datasets and Cisco Umbrella top 1 million domains list, to train a recurrent neural network to classify domain names as phishing or not phishing.

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

```
Best performance at threshold: 0.8233668341708543
Calculated 7482 predictions with a mean value of 0.45260921120643616
Evaluating using threshold 0.8233668341708543
Cut-off threshold: 0.8234
Evaluation counts: {'TN': 3840, 'FP': 411, 'FN': 474, 'TP': 2757}
+------------------+----------------+--------------------+
| Accuracy 88.172% | Predicted safe | Predicted phishing |
+------------------+----------------+--------------------+
|   Not phishing   |    TN: 3840    |      FP: 411       |
|                  |  NPV: 89.013%  |    FDR: 12.973%    |
|                  |  TNR: 90.332%  |    FPR: 9.668%     |
|   Is phishing    |    FN: 474     |      TP: 2757      |
|                  |  FOR: 10.987%  |    PPV: 87.027%    |
|                  |  FNR: 14.67%   |    TPR: 85.33%     |
+------------------+----------------+--------------------+

Examples for TN Bin range: 4.2038914e-06 - 0.1645833 , Num. Samples: 3546
                               input  ground truth  prediction
0                             uff.br             0    0.000074
1                       kgridhub.net             0    0.000071
2                          i.tfag.de             0    0.000049
3               speed.sng.host.co.ug             0    0.000041
4   r1---sn-4g5ednsk.googlevideo.com             0    0.000006
5                        metrilo.com             0    0.000688
6                  minikube.internal             0    0.081473
7            duplex.snapchat.com.lan             0    0.000722
8                  baidu.gcs-web.com             0    0.018649
9                   artix.aqw.aq.com             0    0.000013
10             eofihsishihiursgu.biz             0    0.000017
11            fcai21-2.fna.fbcdn.net             0    0.000006
12                 logs1412.xiti.com             0    0.000007
13                 dw32.uptodown.com             0    0.000112
14    acs.m.taobao.com.itotolink.net             0    0.000006

Examples for TN Bin range: 0.1645833 - 0.3291624 , Num. Samples: 101
                             input  ground truth  prediction
0                   prospam.pro.dk             0    0.291461
1         webmail.sakuraexpress.cl             0    0.166276
2                   mail.lauka.org             0    0.270554
3                   luckfriend.com             0    0.269514
4               messagecloud.co.uk             0    0.318155
5   ksn-url-geo.kaspersky-labs.com             0    0.200115
6                          htl.bid             0    0.257485
7              wa.cdn-surfline.com             0    0.311028
8                 irishmeadows.net             0    0.282818
9                     aventi.co.uk             0    0.178727
10                    ip-adress.eu             0    0.310365
11                  nis-jeddah.com             0    0.218548
12                learnbook.com.au             0    0.324814
13                       ubu.ac.th             0    0.206307
14                   sompocare.com             0    0.229599

Examples for TN Bin range: 0.3291624 - 0.4937415 , Num. Samples: 68
                              input  ground truth  prediction
0                      flowonly.com             0    0.356909
1                      tosejuna.com             0    0.417197
2                            edu.bd             0    0.444738
3                        heatmap.vn             0    0.404180
4          autodiscover.myrp.edu.sg             0    0.329448
5        www.davitahelpinghands.com             0    0.403792
6                       rmazywr.org             0    0.424882
7                      nic-bank.com             0    0.356714
8                      moreradio.ru             0    0.436693
9                       ituqqwd.com             0    0.329223
10                    tapjoyads.com             0    0.457778
11  expert-comptable-paris-2eme.com             0    0.420038
12                 alexscott.com.au             0    0.424583
13                   luckypushh.com             0    0.404293
14                      daarvag.com             0    0.420969

Examples for TN Bin range: 0.4937415 - 0.6583206 , Num. Samples: 58
                 input  ground truth  prediction
0     server.kwh.co.id             0    0.631592
1     livesupporti.com             0    0.543329
2      credisur.com.ar             0    0.615295
3   www.nodemanage.com             0    0.571279
4     ao-neandertal.fr             0    0.571206
5         tamsonvn.com             0    0.637497
6            ahtea.com             0    0.606500
7          everset.com             0    0.510987
8       gluon.opngr.in             0    0.625919
9           meteor.com             0    0.633929
10             poki.by             0    0.588951
11     lenovopress.com             0    0.522174
12    transauer.com.ar             0    0.597781
13          manasco.be             0    0.550624
14       supermsav.com             0    0.580832

Examples for TN Bin range: 0.6583206 - 0.8228997 , Num. Samples: 66
                  input  ground truth  prediction
0     www.workfront.com             0    0.778051
1             skift.com             0    0.673103
2    www.ecdc.europa.eu             0    0.667001
3   wcproject.so-net.tw             0    0.793860
4             yoyou.com             0    0.814273
5     spineuniverse.com             0    0.788195
6        api5137.d41.co             0    0.802097
7   comm.mywellness.com             0    0.725134
8      mbf3g.coccoc.com             0    0.821054
9           phos.com.cy             0    0.743115
10     www.macaubet.com             0    0.699770
11        bimnsaft.info             0    0.747835
12       enecprogram.ae             0    0.746568
13         www.dogia.ml             0    0.779521
14       jahwijrkkyr.cx             0    0.800437

Examples for FP Bin range: 0.8346011 - 0.8676798 , Num. Samples: 23
                     input  ground truth  prediction
0              firehol.org             0    0.839287
1         trumarkmedia.com             0    0.841028
2   quickdriverupdater.com             0    0.851080
3              iogame.zone             0    0.842212
4         mcritiskilo.info             0    0.865129
5             allianzsp.sk             0    0.844906
6        epochtimes.com.br             0    0.846198
7             doylo.com.au             0    0.855685
8         icocpanutrdeb.cf             0    0.849629
9         comeconcausa.com             0    0.838330
10        qbkrecaptcha.com             0    0.867649
11          mediamanbu.com             0    0.836004
12   greenweddingshoes.com             0    0.864043
13       negociosjordi.com             0    0.853819
14       www.boomlings.com             0    0.834601

Examples for FP Bin range: 0.8676798 - 0.90075845 , Num. Samples: 15
                       input  ground truth  prediction
0                    chat.ru             0    0.890686
1        api.hikestickers.in             0    0.886232
2               onlycable.es             0    0.882747
3   mail.hickorypark-bbq.com             0    0.898491
4            bmbabbage.co.uk             0    0.871446
5             magnet.kiev.ua             0    0.883989
6          midas-network.com             0    0.893381
7                 lanecc.edu             0    0.896558
8            metatrader4.com             0    0.894400
9        hottubcoverpros.com             0    0.872151
10              hanoi.edu.vn             0    0.872082
11    heartsfireleathers.com             0    0.881630
12             capi-ombre.ch             0    0.884095
13             jlsmzsss.info             0    0.892742
14           www.wayixia.com             0    0.885290

Examples for FP Bin range: 0.90075845 - 0.93383706 , Num. Samples: 31
                                 input  ground truth  prediction
0                    evergreensame.com             0    0.906636
1   autologon.microsoftazuread-sso.com             0    0.906080
2                     brandedgirls.com             0    0.932306
3                        shabakaty.com             0    0.916243
4                    naturalcycles.com             0    0.913313
5                   hk.af7f.linkit.dev             0    0.900904
6                    galaxydigital.com             0    0.919322
7                           ole711.com             0    0.917215
8                           lawyer.com             0    0.928246
9                   hanbalmasstech.com             0    0.918848
10                    gamemonetize.com             0    0.913623
11                  morningconsult.com             0    0.921385
12                     jpniaocsydt.org             0    0.901721
13                   rainbowelec.co.kr             0    0.918791
14                        creaders.net             0    0.926909

Examples for FP Bin range: 0.93383706 - 0.9669157 , Num. Samples: 45
                                    input  ground truth  prediction
0                   www.indiangaysite.com             0    0.949830
1                        cq5yofna3emz.com             0    0.961039
2              imarketing.smadvantage.com             0    0.936440
3                        prizehoarder.com             0    0.943814
4                     www.radio-polska.pl             0    0.952098
5                      track.wrktrack.xyz             0    0.934386
6                      saveeditonline.com             0    0.949220
7                   performance-click.com             0    0.964512
8                     message.zhulong.com             0    0.942824
9                         eyefeelfree.com             0    0.965426
10                        com-t-iqiyi.com             0    0.939032
11                   concur.ais-vidnt.com             0    0.959422
12                             hkstar.com             0    0.964927
13  com.xi.zwtianshangm.com.n.num1dns.com             0    0.958984
14                www.rivendellschool.org             0    0.952425

Examples for FP Bin range: 0.9669157 - 0.9999944 , Num. Samples: 296
                                   input  ground truth  prediction
0                        www.sicepat.com             0    0.994377
1                          boingo.events             0    0.998023
2    mail.info.virtualization-online.org             0    0.974096
3                       bk.madamebuzz.fr             0    0.998491
4                       sahabatnesia.com             0    0.992564
5             images-origin.wallwiz.link             0    0.998445
6              www.joyfulhealthyeats.com             0    0.994789
7                            yqit.com.gu             0    0.999963
8           southeastasia1-mediap.svc.ms             0    0.979225
9           www.auduboninternational.org             0    0.999933
10            mail.yukseliskoleji.com.tr             0    0.999993
11                  oce.myworkaccess.com             0    0.982829
12                   www.bostonglobe.com             0    0.999549
13                             uwe.ac.uk             0    0.996843
14  performancemanager.successfactors.eu             0    0.999963

Examples for FN Bin range: 5.7383745e-06 - 0.16260472 , Num. Samples: 313
                                       input  ground truth  prediction
0                        www.elsacampini.com             1    0.071840
1         internetbanking.ninetysbankasi.com             1    0.000523
2                              csgoequal.com             1    0.000059
3                         laaksik1.emlnk.com             1    0.000007
4                              mmp.zaridi.to             1    0.000007
5                                  sjafc.com             1    0.006155
6                  mijn.ing.nl.r3lja3mxea.cf             1    0.000085
7                                 dotilo.com             1    0.000158
8                         www.bayernlbuk.net             1    0.002987
9                   sexeducation.atspace.com             1    0.015100
10                               depgrup.com             1    0.000090
11                      g8consultores.com.ar             1    0.000374
12                             ukdvlatax.com             1    0.000595
13  -371481629042.s3-us-west-2.amazonaws.com             1    0.005684
14                            o2accounts.com             1    0.008778

Examples for FN Bin range: 0.16260472 - 0.3252037 , Num. Samples: 34
                                 input  ground truth  prediction
0            hernandeztreeservices.com             1    0.228097
1                        lwsovetnyk.ru             1    0.276620
2             www.todosprodutos.com.br             1    0.270474
3                    www.washpucks.com             1    0.287281
4                     www.smspoint.biz             1    0.252704
5                    info.lionnets.com             1    0.208567
6                       bahadarpur.org             1    0.187675
7                    carrytheskull.com             1    0.288351
8          neighbourhoodwatchcasey.com             1    0.186946
9                 undeadthreads.com.au             1    0.286252
10                   aucoindesrues.com             1    0.168562
11            www.cashflowfxonline.com             1    0.172259
12  bodegalatinacorp-my.sharepoint.com             1    0.281606
13                   galeano-store.com             1    0.319252
14                   emasresources.com             1    0.322427

Examples for FN Bin range: 0.3252037 - 0.48780265 , Num. Samples: 33
                           input  ground truth  prediction
0                movemycouch.com             1    0.483017
1    littleblackdresskingdom.com             1    0.440833
2      smartenergyinitiative.com             1    0.421929
3                 autoscurt24.de             1    0.361222
4             anantaglobal.co.in             1    0.467341
5           himanshusofttech.com             1    0.421861
6              mackanthem.com.pe             1    0.458732
7   undesmaro1937.blogspot.co.uk             1    0.355714
8               amazerpresce.com             1    0.353877
9          wybierajmy-wygrana.eu             1    0.415280
10                   infobcp.com             1    0.434311
11            www.attemplate.com             1    0.410304
12                galvarburg.com             1    0.417515
13          returnsuktax-reb.com             1    0.483303
14       mobileandmacpoint.co.uk             1    0.479876

Examples for FN Bin range: 0.48780265 - 0.65040165 , Num. Samples: 37
                         input  ground truth  prediction
0        bahankuliahonline.com             1    0.613407
1         www.vjdisplay.com.cn             1    0.489598
2                 dasktake.com             1    0.541082
3                   boclog.com             1    0.552461
4               installusd.com             1    0.619007
5            dgte.hyperphp.com             1    0.617228
6             ourevolution.com             1    0.575264
7             corfuproperty.gr             1    0.507206
8            iwatchsystems.com             1    0.504257
9         www.ecotaskforce.com             1    0.617794
10     kayakthefloridakeys.com             1    0.548003
11  regulariac.sslblindado.com             1    0.579141
12               www.ne-pok.hr             1    0.562615
13              snarkysoap.com             1    0.530398
14    wg1386611.virtualuser.de             1    0.634511

Examples for FN Bin range: 0.65040165 - 0.8130006 , Num. Samples: 56
                                     input  ground truth  prediction
0                          webextractz.com             1    0.812275
1                     roadtax-overpaid.com             1    0.690235
2                       perucreartebtl.com             1    0.660292
3                                 auv95.ru             1    0.666613
4                 tscit3-my.sharepoint.com             1    0.756394
5                 servicosnet-prime.online             1    0.797019
6   accountchckecker-update-now.drpiza.com             1    0.707069
7                    dynamicdesignsinc.net             1    0.773909
8                   www19.vemdeofertas.com             1    0.733960
9              fotografodebodasbolivia.com             1    0.664201
10      accounts.sanpchat.com.ghasalah.com             1    0.734386
11                             vhmrics.com             1    0.752213
12                     kishblackdolphin.ir             1    0.728020
13                         www.payinur.com             1    0.806341
14                      glaserpartners.com             1    0.737612

Examples for TP Bin range: 0.8244931 - 0.8595935 , Num. Samples: 17
                       input  ground truth  prediction
0           www.rusikona.pro             1    0.841892
1           nuovaapp2021.com             1    0.828084
2    www.financialone.com.hk             1    0.833767
3        taxrebate-ukgov.com             1    0.826855
4         www.mitadmas11.net             1    0.840091
5       threecustomers.co.uk             1    0.832363
6             amezon-fuui.cc             1    0.847114
7         arkitektonline.com             1    0.824786
8                galen.co.ke             1    0.857913
9          www.formbuddy.com             1    0.841383
10   www.tamircimuslukcu.com             1    0.838979
11           kokoalets.dx.am             1    0.838399
12  www.khabargozarisaba.com             1    0.851899
13                 foliar.pl             1    0.834544
14           ecosolarion.com             1    0.824493

Examples for TP Bin range: 0.8595935 - 0.89469385 , Num. Samples: 28
                           input  ground truth  prediction
0            sn.4yamarketing.com             1    0.883737
1     jagexbondclaim-rewards.com             1    0.887546
2    afectadostrustinvesting.com             1    0.877798
3        modaprivatelabel.com.br             1    0.891466
4                  3mileride.com             1    0.883470
5           panthera-medical.com             1    0.877320
6        mail.mohdnourshahen.com             1    0.870165
7    afectadostrustinvesting.com             1    0.877798
8         corewellnesshawaii.com             1    0.870114
9                      cvacca.ca             1    0.872188
10           masterenfunnels.com             1    0.860963
11                    meetme.run             1    0.867648
12  gz.realestateinkatytexas.com             1    0.876292
13                    meditur.ro             1    0.875157
14             evensfreepubg.com             1    0.891941

Examples for TP Bin range: 0.89469385 - 0.92979425 , Num. Samples: 57
                                   input  ground truth  prediction
0                          bombi-yarn.ru             1    0.904719
1                    gov-onlineclaim.com             1    0.911427
2                    h5r4-accsecnode.com             1    0.896938
3       royalbank.com.xtudocapela.com.br             1    0.909660
4                dfshkqbzt.holopokor.com             1    0.919802
5                    harpiaadventure.com             1    0.913415
6                      www.faxitalia.com             1    0.921273
7              tamericans-melhorando.com             1    0.924349
8                    chirhoprecision.com             1    0.922330
9                     regularizar-app.tk             1    0.908537
10  bungjakatingkir.dosesesfacesopio.com             1    0.920813
11                          margarita.md             1    0.904043
12                        otropuerto.com             1    0.927858
13                flourishnetwork.org.za             1    0.897290
14                       clublazilio.com             1    0.928594

Examples for TP Bin range: 0.92979425 - 0.9648946 , Num. Samples: 89
                                       input  ground truth  prediction
0                            go-midasbuy.com             1    0.940949
1                        thundersoftball.org             1    0.957733
2               themarbleshop.sharepoint.com             1    0.959678
3                              anatkumar.com             1    0.942024
4                            aladdinstar.com             1    0.954259
5                      myhealthinsquotes.com             1    0.956690
6              commercialinvestingcenter.com             1    0.961896
7              blog.venouslaserclinic.com.br             1    0.938522
8                                 suxury.com             1    0.964564
9   ww.chatgrupwhatsappjoinkanyuk.wikaba.com             1    0.963315
10                       kbstitchdesigns.com             1    0.948136
11                                mxhlbrt.de             1    0.956871
12                       rotorflygklubben.se             1    0.950931
13                        vodafonenotice.com             1    0.945711
14                               voipoid.com             1    0.934430

Examples for TP Bin range: 0.9648946 - 0.999995 , Num. Samples: 2563
                                       input  ground truth  prediction
0                                jmcnoack.cl             1    0.999400
1   -e-w-me-ss-age-po-rt-al.wl.r.appspot.com             1    0.999970
2                        rosenbloomphoto.com             1    0.997969
3                  globaldoctorshospital.com             1    0.999965
4                        lbk-consulta760.com             1    0.997620
5                     afrotechfoundation.org             1    0.999844
6                        smcc-cacc.apqcf.com             1    0.999684
7                                bietgi.info             1    0.999959
8                        smcc-cacc.cjnyd.com             1    0.999983
9                         www.nixtechnix.com             1    0.999262
10                        tmsneurohealth.net             1    0.973825
11                      netflixloginhelp.com             1    0.999931
12  p-dot-cedar-code-289917.nn.r.appspot.com             1    0.999992
13  -dot-cryptic-now-290917.ey.r.appspot.com             1    0.999993
14  k-dot-cedar-code-289917.nn.r.appspot.com             1    0.999993

Phishing ULR examples:
Prediction on url: frgcxtmjzfjpdcusge.top 0.9999919
Prediction on url: evilmadeupurl.phish 2.8354718e-05
Prediction on url: evil.madeupurl.phish 4.8922248e-06

Safe URL examples:
Prediction on url: sharelatex.cryptobro.eu 0.0003382023
Prediction on url: sharelatex.cryptobro.eu:5000 0.9999814
Prediction on url: google.com 2.0498774e-05
Prediction on url: www.google.com 0.000113828835
Prediction on url: gmail.google.com 6.681633e-06
Prediction on url: mail.google.com 5.736596e-06
Prediction on url: tudelft.nl 0.0001385505
Prediction on url: brightspace.tudelft.nl 0.99950314
Prediction on url: colab.research.google.com 6.3205575e-06
Prediction on url: 00-gayrettepe-t3-8---00-gayrettepe-xrs-t2-1.statik.turktelekom.com.tr 0.91619027
```