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
Best performance at threshold: 0.5972361809045227
Calculated 7630 predictions with a mean value of 0.4468480944633484
Evaluating using threshold 0.5972361809045227
Cut-off threshold: 0.5972
Evaluation counts: {'TN': 3850, 'FP': 429, 'FN': 430, 'TP': 2921}
+------------------+----------------+--------------------+
| Accuracy 88.742% | Predicted safe | Predicted phishing |
+------------------+----------------+--------------------+
|   Not phishing   |    TN: 3850    |      FP: 429       |
|                  |  NPV: 89.953%  |    FDR: 12.806%    |
|                  |  TNR: 89.974%  |    FPR: 10.026%    |
|   Is phishing    |    FN: 430     |      TP: 2921      |
|                  |  FOR: 10.047%  |    PPV: 87.194%    |
|                  |  FNR: 12.832%  |    TPR: 87.168%    |
+------------------+----------------+--------------------+

Examples for TN Bin range: 3.0172878e-05 - 0.11933063 , Num. Samples: 3556
                                  input  ground truth  prediction
0                    delahowe.k12.sc.us             0    0.011289
1                         ilomadntsi.cf             0    0.004563
2              dns1.digicelbarbados.net             0    0.000249
3                           mnpsk12.org             0    0.000160
4                          mail.aav.com             0    0.000087
5   r7---sn-ci5gup-qxak.googlevideo.com             0    0.000046
6                     mjgohoqsrwyiut.sx             0    0.000071
7       r5---sn-3u-u5xd.googlevideo.com             0    0.000053
8                       m16.obyhogh.biz             0    0.000034
9        r1.sn-5hne6n7l.googlevideo.com             0    0.000093
10             policy.cookiereports.com             0    0.000041
11                 outbrain-d.openx.net             0    0.000040
12                        events.air.tv             0    0.000081
13         external-sea1-1.xx.fbcdn.net             0    0.000032
14                     x36.xnimseon.com             0    0.000033

Examples for TN Bin range: 0.11933063 - 0.23863108 , Num. Samples: 124
                                input  ground truth  prediction
0                   job.supperpow.com             0    0.211935
1                 demo.goodlayers.com             0    0.201903
2                   www.lesschwab.com             0    0.221087
3                       macromill.com             0    0.147707
4                    canal2movies.com             0    0.180264
5      milestone.myfinanceservice.com             0    0.186852
6                          posist.org             0    0.133924
7                   packagecontrol.io             0    0.225168
8               discoverybenefits.com             0    0.212295
9                          wbho.co.za             0    0.162950
10                       taquanta.com             0    0.128921
11                     mp3juices.site             0    0.198850
12                         sheret.com             0    0.124487
13                 podcastio.app.link             0    0.202055
14  savewithwa.empower-retirement.com             0    0.139124

Examples for TN Bin range: 0.23863108 - 0.35793155 , Num. Samples: 66
                            input  ground truth  prediction
0                securifythis.com             0    0.288340
1   nonguu99fdoe.cloudmaestro.com             0    0.323198
2                    niloblog.com             0    0.300954
3                api.myskyapp.com             0    0.303832
4               ww2.cartoonhd.com             0    0.321170
5   secure.osla.myloanmanager.com             0    0.283964
6                   samhealth.org             0    0.338313
7               www.bolasport.com             0    0.318110
8             www.southlandcu.org             0    0.329205
9                      amm.org.br             0    0.329359
10                halliburton.com             0    0.267816
11                  areena.yle.fi             0    0.252053
12                    egaejjt.com             0    0.340614
13                   kendauer.com             0    0.275805
14     subscriber.pushcentric.com             0    0.311353

Examples for TN Bin range: 0.35793155 - 0.477232 , Num. Samples: 54
                      input  ground truth  prediction
0               saviola.com             0    0.397828
1        allisonmoffett.com             0    0.370027
2   wyndhamgrandcamranh.com             0    0.402791
3                nrru.ac.th             0    0.376657
4            www.ehenho.com             0    0.403307
5           kindle-boot.com             0    0.456016
6            mcdanielfg.com             0    0.432687
7    experiencecherwell.com             0    0.413031
8           premiumspace.gr             0    0.385199
9        www.tonymacx86.com             0    0.432605
10             utande.co.zw             0    0.399428
11               appvtv.com             0    0.463649
12           warpportal.com             0    0.383542
13      www.loginangkah.com             0    0.424406
14        nanjingchenxi.com             0    0.456118

Examples for TN Bin range: 0.477232 - 0.59653246 , Num. Samples: 49
                                input  ground truth  prediction
0              mailderef.g-ha-gmx.com             0    0.486849
1                  blackmanfamily.com             0    0.481157
2                       ilegkenya.org             0    0.508360
3                     parcelforce.com             0    0.508580
4                         madonna.org             0    0.580892
5                  unimednatal.com.br             0    0.494837
6                         bt.okmp3.ru             0    0.587899
7              www.redtubepremium.com             0    0.528888
8   bagalkot1.supersonicbroadband.com             0    0.557537
9                  monitor-eqatec.com             0    0.501735
10                      bongdasao.com             0    0.539638
11                          atlax.com             0    0.531772
12                    www.newwide.com             0    0.492133
13                  skyscanner.com.my             0    0.481562
14                    jeff-beaman.com             0    0.570212

Examples for FP Bin range: 0.59776086 - 0.6782012 , Num. Samples: 31
                          input  ground truth  prediction
0             www.crismatec.com             0    0.614148
1          o3.ptr7117.now1.site             0    0.615988
2                 sjgroup.local             0    0.676225
3          animenewsnetwork.com             0    0.623854
4                   hostigr.com             0    0.617599
5                  ltqqnoob.com             0    0.641287
6               www.otoflik.com             0    0.665595
7                    mdlinx.com             0    0.625648
8                onfluencer.net             0    0.651579
9   mirror.oxfordnanoportal.com             0    0.614395
10                   sm-usa.org             0    0.606733
11                   apizza.net             0    0.656295
12            mail.arhidasrl.it             0    0.664505
13                   wanmei.com             0    0.670492
14                 ooshahwa.biz             0    0.636655

Examples for FP Bin range: 0.6782012 - 0.7586416 , Num. Samples: 26
                                   input  ground truth  prediction
0                               majoo.id             0    0.688085
1                              rebm.work             0    0.745737
2                www.adcenterexpress.com             0    0.709357
3                    letslearnkidz.co.za             0    0.718207
4                           shoplife.pro             0    0.732617
5                              c-stat.eu             0    0.713418
6                     animalonplanet.com             0    0.700922
7                          wizardsbd.com             0    0.737219
8               metcashautomotive.com.au             0    0.757068
9                       grouperubuye.com             0    0.747778
10                          bitmovin.com             0    0.699946
11                          interjet.com             0    0.737858
12                        www.petmart.ro             0    0.747681
13  blooming-springs-10369.herokuapp.com             0    0.705731
14                  www.co.lincoln.or.us             0    0.693781

Examples for FP Bin range: 0.7586416 - 0.83908194 , Num. Samples: 43
                      input  ground truth  prediction
0               7-eleven.ca             0    0.795190
1             uscategui.com             0    0.774827
2             rppbreexwr.ug             0    0.825306
3              pspindia.net             0    0.759786
4              hogegypt.com             0    0.785405
5   testwww.starbucks.co.uk             0    0.816987
6              seahawks.com             0    0.786492
7           error.youjyi.cn             0    0.829183
8          generalassemb.ly             0    0.829913
9          gaypornhdfree.to             0    0.818294
10        flywheelsites.com             0    0.809150
11                doqcl.top             0    0.825850
12         www.allbirds.com             0    0.827875
13          www.linksys.com             0    0.817023
14                    uv.ro             0    0.811801

Examples for FP Bin range: 0.83908194 - 0.91952235 , Num. Samples: 70
                           input  ground truth  prediction
0               cinnamylife.info             0    0.918139
1            www.omahasteaks.com             0    0.874224
2                      com.cn314             0    0.868870
3                 pengpengla.com             0    0.875235
4              laughingsquid.com             0    0.859094
5               fnsdk.4399sy.com             0    0.853729
6          dutedu.sharepoint.com             0    0.895549
7                grupoceltis.com             0    0.839715
8                      tellas.gr             0    0.900057
9               fieradidacta.com             0    0.915717
10              www.goapotik.com             0    0.898373
11     suggestqueries.google.com             0    0.888391
12  emfmediaresize.azureedge.net             0    0.869302
13                     vfsite.cz             0    0.911232
14                     idcsrl.it             0    0.897139

Examples for FP Bin range: 0.91952235 - 0.9999627 , Num. Samples: 258
                               input  ground truth  prediction
0                   subtitlebank.net             0    0.965914
1            ufcnouvellecaledonie.nc             0    0.943053
2                movable-ink-601.com             0    0.999940
3          appartamentiexcelsior.com             0    0.994583
4   playlist-nonlive-central.fubo.tv             0    0.999733
5                 emailsenderk79.com             0    0.957429
6             expert-batiment-63.com             0    0.999724
7        orion1772.startdedicated.de             0    0.985480
8                  viaggiosvaghi.com             0    0.967028
9                   evanzo-server.de             0    0.984985
10                   dpsstsdhaka.org             0    0.999744
11                      desirulez.cc             0    0.999112
12         www.associazionehombre.it             0    0.999906
13                 breakingbarta.com             0    0.993755
14               privacypolicies.com             0    0.980872

Examples for FN Bin range: 3.3519635e-05 - 0.114939705 , Num. Samples: 273
                               input  ground truth  prediction
0                          smbcc.top             1    0.106517
1                    divinetrack.com             1    0.107551
2                     tilamaito.info             1    0.002725
3                        fdriqtbt.cn             1    0.002293
4                        fdriqtbt.cn             1    0.002293
5                    actionfilmz.com             1    0.077150
6                  rakvtunm-mqsz.ooo             1    0.015849
7                     o3clean.com.co             1    0.001577
8                   assets.cdnxz.com             1    0.000042
9                     arcomindia.com             1    0.000687
10                      protenfo.com             1    0.007933
11                     betqiuqiu.com             1    0.002747
12                     oclodging.com             1    0.063708
13                        ucmpun.com             1    0.002734
14  correos-cliente-spain.koncil.com             1    0.001256

Examples for FN Bin range: 0.114939705 - 0.2298459 , Num. Samples: 40
                                input  ground truth  prediction
0                          avucan.com             1    0.226981
1                  newdetails-3.world             1    0.168099
2           mijn.ing.nl.r3lja3mxea.cf             1    0.150226
3                      bahadarpur.org             1    0.120667
4                  o2.uk.5ghtml02.com             1    0.118060
5           www.themooregroupofsc.com             1    0.125079
6    www.indepthlaurencefishburne.org             1    0.202768
7    www.indepthlaurencefishburne.org             1    0.202768
8                        printkea.com             1    0.130417
9    www.indepthlaurencefishburne.org             1    0.202768
10                  www.eset-store.gr             1    0.155028
11  www.videosoy.reachhealthylife.com             1    0.225230
12            subscribers.shhxpe.wang             1    0.204844
13          www.quickezweightloss.com             1    0.133729
14                   themkdiaries.com             1    0.227057

Examples for FN Bin range: 0.2298459 - 0.34475207 , Num. Samples: 34
                      input  ground truth  prediction
0               ghorana.com             1    0.330231
1     www.kiana-leather.com             1    0.280618
2   whatsapps.instanthq.com             1    0.337591
3       kbstitchdesigns.com             1    0.323251
4    www.airy-directory.com             1    0.312206
5        savethedate.com.hr             1    0.275456
6         brianhuntblog.com             1    0.269412
7         osh2.labour.go.th             1    0.259121
8          organicmanure.in             1    0.294464
9         iceyouroffice.com             1    0.246719
10           pkwmobilede.de             1    0.302874
11               icodex.org             1    0.316362
12             squaksre.com             1    0.318579
13        avestafinance.com             1    0.340175
14    suchen.de-mobille.com             1    0.271637

Examples for FN Bin range: 0.34475207 - 0.45965827 , Num. Samples: 40
                                       input  ground truth  prediction
0                               vmoremlm.com             1    0.452679
1                               funpeguy.com             1    0.386935
2                        3mvirugambakkam.com             1    0.393048
3         internetbanking.ninetysbankasi.com             1    0.396618
4              blog.venouslaserclinic.com.br             1    0.423525
5                            wwwfacebook.org             1    0.398083
6                whatshappeninghighlands.com             1    0.394724
7                        www.elsacampini.com             1    0.435217
8                           villaflor.edu.mx             1    0.446791
9                        www.bangbusheai.com             1    0.364459
10                         gerenciadorpj.net             1    0.425528
11  jonkwowa.fra1.cdn.digitaloceanspaces.com             1    0.421220
12                          www.maayadal.com             1    0.348724
13                           tuliving.com.ar             1    0.359025
14                         www.via-india.com             1    0.457765

Examples for FN Bin range: 0.45965827 - 0.57456446 , Num. Samples: 42
                        input  ground truth  prediction
0     www.cottoncandybros.com             1    0.485077
1                dasktake.com             1    0.539341
2              www.navic7.net             1    0.466916
3          gamingdominion.com             1    0.511847
4                   cvacca.ca             1    0.534316
5            ktychemicals.com             1    0.498314
6            ktychemicals.com             1    0.498314
7           www.coderllci.com             1    0.537806
8            www.hoomokef.com             1    0.509717
9         www.vashtrainer.com             1    0.490914
10       panthera-medical.com             1    0.487382
11        rrthulasi.unaux.com             1    0.502706
12  www.therootfoundation.org             1    0.546045
13        scalextricman.co.uk             1    0.475573
14              careeresl.com             1    0.478702

Examples for TP Bin range: 0.59801906 - 0.6784087 , Num. Samples: 38
                          input  ground truth  prediction
0     naturalhormonetherapy.biz             1    0.604839
1        ayushayurvedagroup.com             1    0.672764
2                   loneail.com             1    0.600407
3   card-mail-center.bribhvi.cn             1    0.677979
4                  uzbekart.com             1    0.629176
5             evensfreepubg.com             1    0.667894
6              isabellacano.com             1    0.637639
7                truckargue.com             1    0.656847
8               metallist-nk.ru             1    0.598019
9                    piponi.com             1    0.669874
10          solobuenasideas.com             1    0.614413
11               truckargue.com             1    0.656847
12         heritagehomeindia.in             1    0.632249
13      www.jcomforthomes.co.ke             1    0.614173
14            osmantraining.com             1    0.614198

Examples for TP Bin range: 0.6784087 - 0.7587983 , Num. Samples: 50
                                       input  ground truth  prediction
0                       backyarddelivery.com             1    0.684160
1                           www.brighant.com             1    0.707692
2                        pixelbenchmarks.com             1    0.714688
3                        www.masterdrive.com             1    0.705495
4                                go4steel.in             1    0.699073
5                      southernlagranite.com             1    0.747723
6                wpcorporate.sfdevserver.com             1    0.754215
7                         www.budgetbots.com             1    0.742864
8                         secure-updform.com             1    0.741747
9                    lloyds.bank-confirm.com             1    0.727995
10                       personalbravery.com             1    0.749598
11                            219betasus.com             1    0.706293
12                             mailcarry.com             1    0.712842
13  doc.google.share.pressurecookerindia.com             1    0.710382
14                         janatatvnepal.com             1    0.678944

Examples for TP Bin range: 0.7587983 - 0.839188 , Num. Samples: 68
                                 input  ground truth  prediction
0                    wuteh.a100.com.pl             1    0.810533
1                          bietgi.info             1    0.766141
2               mapper.terra-drone.net             1    0.795500
3                    refundlnterac.com             1    0.764800
4                  clientesdigital.xyz             1    0.766737
5                    smartubemedia.com             1    0.784708
6              sayeedinternational.com             1    0.766233
7                             gradi.ba             1    0.836420
8   info-kyufukinsoumusoumu.eefnnrl.cn             1    0.814390
9                     corfuproperty.gr             1    0.788099
10                    bestrapbeats.com             1    0.813633
11                   rapinafanzine.com             1    0.783293
12              frgcxtmjzfjpdcusge.top             1    0.786150
13                     pignoseamps.com             1    0.838261
14                     b2bprints.co.uk             1    0.821473

Examples for TP Bin range: 0.839188 - 0.9195776 , Num. Samples: 114
                                       input  ground truth  prediction
0                         vodafonenotice.com             1    0.896264
1                                 moatia.com             1    0.873030
2              153284594738391.statictab.com             1    0.878149
3                        princessmarlene.com             1    0.912236
4                                  rooyan.in             1    0.891730
5                joeypmemorialfoundation.com             1    0.848792
6   -online-zonasegura.plantascarnivoras.com             1    0.870558
7                  greenbirdtechnologies.com             1    0.878551
8                            toenailecare.ru             1    0.862664
9                      paxful.epayment.trade             1    0.898151
10                      stearncommurnity.com             1    0.882519
11                 grottedisaledesenzano.com             1    0.891977
12  dauthowa.fra1.cdn.digitaloceanspaces.com             1    0.911096
13                              kaher.edu.in             1    0.911662
14                        poligrafiapias.com             1    0.915044

Examples for TP Bin range: 0.9195776 - 0.9999672 , Num. Samples: 2650
                                       input  ground truth  prediction
0                  accorservorg.yolasite.com             1    0.999926
1                             103.45.103.207             1    0.999961
2   p-dot-cedar-code-289917.nn.r.appspot.com             1    0.999939
3                       scientificerevna.com             1    0.981638
4                   handsonbeautysalon.co.uk             1    0.994450
5                          www.storstart.com             1    0.997019
6   -dot-cryptic-now-290917.ey.r.appspot.com             1    0.999955
7        halifax.secureonline-helpcenter.com             1    0.999938
8                web6910.cweb03.gamingweb.de             1    0.999649
9                            gpmohammadi.com             1    0.987925
10                               pinnerx.com             1    0.998637
11                            macjakarta.com             1    0.966443
12                www.hplc-remove-device.com             1    0.999932
13                              techbells.in             1    0.999934
14        groupbokepwhatsapp.grub-wa23.my.id             1    0.999964

Phishing ULR examples:
Prediction on url: frgcxtmjawefgrthdcusge.dab 0.00019756198
Prediction on url: evilmadeupurl.phish 0.90739095
Prediction on url: evil.madeupurl.phish 0.10410794

Safe URL examples:
Prediction on url: google.com 0.0003748567
Prediction on url: www.google.com 0.4357896
Prediction on url: gmail.google.com 5.1141105e-05
Prediction on url: mail.google.com 4.7062753e-05
Prediction on url: tudelft.nl 0.00018236713
Prediction on url: brightspace.tudelft.nl 0.9994887
Prediction on url: colab.research.google.com 8.626908e-05
Prediction on url: 00-gayrettepe-t3-8---00-gayrettepe-xrs-t2-1.statik.turktelekom.com.tr 0.047438875
```