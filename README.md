# Phishing detection AI from scratch.

Makes use of Phishtank online valid datasets and Cisco Umbrella top 1 million domains list, to train a recurrent neural network to classify domain names as phishing or not phishing.

Run the dataset_downloader.py to download one new sample from phishtank and merge any new urls into the combined dataset. Could be automated using crontab.


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
2020-10-30 17:49:46.485027: I tensorflow/stream_executor/platform/default/dso_loader.cc:49] Successfully opened dynamic library libcudart.so.11.0
Phishtank Online Valid Dataset
23736 rows
    Unnamed: 0                                                url  ...                                       domain_names in_whitelist
0            0  https://newproductsstore.com/oauth.paypal/myac...  ...                               newproductsstore.com        False
1            1                             http://dhj.wsaufan.cn/  ...                                     dhj.wsaufan.cn        False
2            2                               http://olivaspa.com/  ...                                       olivaspa.com        False
3            3                     https://olivaspa.com/index.php  ...                                       olivaspa.com        False
4            4                              https://olivaspa.com/  ...                                       olivaspa.com        False
5            5                    http://izacourier.com/index.php  ...                                     izacourier.com        False
6            6                   https://izacourier.com/index.php  ...                                     izacourier.com        False
7            7                            https://izacourier.com/  ...                                     izacourier.com        False
8            8                 https://www.msn.autheticathor.com/  ...                          www.msn.autheticathor.com        False
9            9  http://ftaqdxdsljuxbemvdgpkeoqhmmglnrscfsgz-do...  ...  ftaqdxdsljuxbemvdgpkeoqhmmglnrscfsgz-dot-cedar...        False
10          10  https://ftaqdxdsljuxbemvdgpkeoqhmmglnrscfsgz-d...  ...  ftaqdxdsljuxbemvdgpkeoqhmmglnrscfsgz-dot-cedar...        False
11          11  http://173.82.129.223/ap/signin?key=a@b.c&amp;...  ...                                     173.82.129.223        False
12          12  http://osh11.labour.go.th/language/overrides/A...  ...                                 osh11.labour.go.th        False
13          13  https://dreemhempoil.com/wp-content/secureNetf...  ...                                   dreemhempoil.com        False
14          14  https://squarenup.org/totalconfirm/index2.php?...  ...                                      squarenup.org        False
15          15  https://onlinesquare4.org/index2.php?cmd=login...  ...                                  onlinesquare4.org        False
16          16                         https://onlinesquare4.org/  ...                                  onlinesquare4.org        False
17          17                          http://onlinesquare4.net/  ...                                  onlinesquare4.net        False
18          18  http://www.gadalenterprises.com/wp-includes/za...  ...                           www.gadalenterprises.com        False
19          19  http://miansoft.com/images/_notes/w/we/wee/tra...  ...                                       miansoft.com        False

[20 rows x 10 columns]
             com   ru  net  org   br  xyz   uk  top  info   ph   in  link   id   cc   cn   ly   fr   io   de   it  OTHERS
TLD Count  13905  945  776  477  373  360  354  339   243  235  221   211  205  174  164  146  144  144  139  135    4046
Percentage of top 20 tlds: 82.95 %

Whitelist file: top-1m_umbrella.csv
1000000 rows
    rank                     domain_names
0      1                       google.com
1      2                   www.google.com
2      3                    microsoft.com
3      4                     facebook.com
4      5                      netflix.com
5      6                windowsupdate.com
6      7                  ftl.netflix.com
7      8             prod.ftl.netflix.com
8      9               data.microsoft.com
9     10           api-global.netflix.com
10    11          ctldl.windowsupdate.com
11    12        nrdp.prod.ftl.netflix.com
12    13                  doubleclick.net
13    14                g.doubleclick.net
14    15      safebrowsing.googleapis.com
15    16  settings-win.data.microsoft.com
16    17                      youtube.com
17    18      googleads.g.doubleclick.net
18    19        events.data.microsoft.com
19    20                         live.com

Number of urls that have domains which are in the whilelist: 1442

Selected Data Examples:
Phishing domains: ['newproductsstore.com' 'dhj.wsaufan.cn' 'olivaspa.com' ...
 '0992334.weebly.com' 'gruppwaa139.my03.com' 'bungaabeauty.com'] 22294
Benign domains: ['co.th.lan' 'ext.selected-search.com' 'visio.officeapps.live.com' ...
 'buy1.rcjitdd.com' 'agwu.rs' 'bla2hs.org'] 27867


Encoding Vocabulary (73) used:
[' ', 'z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a', '_', 'Z', 'Y', 'X', 'W', 'V', 'U', 'T', 'S', 'R', 'Q', 'P', 'O', 'N', 'M', 'L', 'K', 'J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A', '@', '?', '=', ';', ':', '9', '8', '7', '6', '5', '4', '3', '2', '1', '0', '.', '-', '&', '#']
Encoding example:
[13 22  4 11  9 12 23  6 24  7  8  8  7 12  9 22 69 24 12 14]
newproductsstore.com
[926, 179, 150, 150, 150, 122, 113, 113, 111, 105, 105, 104, 102, 102, 102, 100, 95, 95, 94, 93]
4300 URLs longer than the cutoff length 40

Training and testing data: (showing first 5)
Train data 42636 samples
[('aon-com.mail.protection.outlook.com', 0, 0.8), ('sultanbetgirisadresimiz1.blogspot.com', 1, 1.0), ('fwdproxy-atn-004.fbsv.net', 0, 0.8), ('robot.ba', 0, 0.8), ('rakuten.co.jp.rakutenlogin.best', 1, 1.0)]
Test data 7525 samples
[('m.bdnews24.com', 0, 0.8), ('pinnerx.com', 1, 1.0), ('www.otropuerto.com', 1, 1.0), ('52e4t.csb.app', 1, 1.0), ('wk.slack.com', 0, 0.8)]

Encoded data: (showing first 5)
Train data 42636 samples, encoded
[(array([26, 12, 13, 70, 24, 12, 14, 69, 14, 26, 18, 15, 69, 11,  9, 12,  7,
       22, 24,  7, 18, 12, 13, 69, 12,  6,  7, 15, 12, 12, 16, 69, 24, 12,
       14]), 0), (array([ 8,  6, 15,  7, 26, 13, 25, 22,  7, 20, 18,  9, 18,  8, 26, 23,  9,
       22,  8, 18, 14, 18,  1, 67, 69, 25, 15, 12, 20,  8, 11, 12,  7, 69,
       24, 12, 14]), 1), (array([21,  4, 23, 11,  9, 12,  3,  2, 70, 26,  7, 13, 70, 68, 68, 64, 69,
       21, 25,  8,  5, 69, 13, 22,  7]), 0), (array([ 9, 12, 25, 12,  7, 69, 25, 26]), 0), (array([ 9, 26, 16,  6,  7, 22, 13, 69, 24, 12, 69, 17, 11, 69,  9, 26, 16,
        6,  7, 22, 13, 15, 12, 20, 18, 13, 69, 25, 22,  8,  7]), 1)]
Test data 7525 samples, encoded
[(array([14, 69, 25, 23, 13, 22,  4,  8, 66, 64, 69, 24, 12, 14]), 0), (array([11, 18, 13, 13, 22,  9,  3, 69, 24, 12, 14]), 1), (array([ 4,  4,  4, 69, 12,  7,  9, 12, 11,  6, 22,  9,  7, 12, 69, 24, 12,
       14]), 1), (array([63, 66, 22, 64,  7, 69, 24,  8, 25, 69, 26, 11, 11]), 1), (array([ 4, 16, 69,  8, 15, 26, 24, 16, 69, 24, 12, 14]), 0)]

Encoded and padded data: (showing first 5)
Train data 42636 samples, encoded
[(array([ 0,  0,  0,  0,  0, 26, 12, 13, 70, 24, 12, 14, 69, 14, 26, 18, 15,
       69, 11,  9, 12,  7, 22, 24,  7, 18, 12, 13, 69, 12,  6,  7, 15, 12,
       12, 16, 69, 24, 12, 14], dtype=int32), 0), (array([ 0,  0,  0,  8,  6, 15,  7, 26, 13, 25, 22,  7, 20, 18,  9, 18,  8,
       26, 23,  9, 22,  8, 18, 14, 18,  1, 67, 69, 25, 15, 12, 20,  8, 11,
       12,  7, 69, 24, 12, 14], dtype=int32), 1), (array([ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 21,  4,
       23, 11,  9, 12,  3,  2, 70, 26,  7, 13, 70, 68, 68, 64, 69, 21, 25,
        8,  5, 69, 13, 22,  7], dtype=int32), 0), (array([ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
        0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  9, 12,
       25, 12,  7, 69, 25, 26], dtype=int32), 0), (array([ 0,  0,  0,  0,  0,  0,  0,  0,  0,  9, 26, 16,  6,  7, 22, 13, 69,
       24, 12, 69, 17, 11, 69,  9, 26, 16,  6,  7, 22, 13, 15, 12, 20, 18,
       13, 69, 25, 22,  8,  7], dtype=int32), 1)]
Test data 7525 samples, encoded
[(array([ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
        0,  0,  0,  0,  0,  0,  0,  0,  0, 14, 69, 25, 23, 13, 22,  4,  8,
       66, 64, 69, 24, 12, 14], dtype=int32), 0), (array([ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
        0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 11, 18, 13, 13, 22,
        9,  3, 69, 24, 12, 14], dtype=int32), 1), (array([ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
        0,  0,  0,  0,  0,  4,  4,  4, 69, 12,  7,  9, 12, 11,  6, 22,  9,
        7, 12, 69, 24, 12, 14], dtype=int32), 1), (array([ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
        0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 63, 66, 22, 64,  7, 69, 24,
        8, 25, 69, 26, 11, 11], dtype=int32), 1), (array([ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
        0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  4, 16, 69,  8, 15, 26,
       24, 16, 69, 24, 12, 14], dtype=int32), 0)]

---------------Tensorflow magic------------------

2020-10-30 17:49:52.516667: I tensorflow/compiler/jit/xla_cpu_device.cc:41] Not creating XLA devices, tf_xla_enable_xla_devices not set
2020-10-30 17:49:52.519108: I tensorflow/stream_executor/platform/default/dso_loader.cc:49] Successfully opened dynamic library libcuda.so.1
2020-10-30 17:49:52.539516: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:941] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2020-10-30 17:49:52.540066: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1720] Found device 0 with properties: 
pciBusID: 0000:00:08.0 name: EIZO Quadro MED-XN92 computeCapability: 7.5
coreClock: 1.545GHz coreCount: 36 deviceMemorySize: 7.79GiB deviceMemoryBandwidth: 387.49GiB/s
2020-10-30 17:49:52.540129: I tensorflow/stream_executor/platform/default/dso_loader.cc:49] Successfully opened dynamic library libcudart.so.11.0
2020-10-30 17:49:52.544990: I tensorflow/stream_executor/platform/default/dso_loader.cc:49] Successfully opened dynamic library libcublas.so.11
2020-10-30 17:49:52.545083: I tensorflow/stream_executor/platform/default/dso_loader.cc:49] Successfully opened dynamic library libcublasLt.so.11
2020-10-30 17:49:52.546355: I tensorflow/stream_executor/platform/default/dso_loader.cc:49] Successfully opened dynamic library libcufft.so.10
2020-10-30 17:49:52.547713: I tensorflow/stream_executor/platform/default/dso_loader.cc:49] Successfully opened dynamic library libcurand.so.10
2020-10-30 17:49:52.550908: I tensorflow/stream_executor/platform/default/dso_loader.cc:49] Successfully opened dynamic library libcusolver.so.10
2020-10-30 17:49:52.552210: I tensorflow/stream_executor/platform/default/dso_loader.cc:49] Successfully opened dynamic library libcusparse.so.11
2020-10-30 17:49:52.552672: I tensorflow/stream_executor/platform/default/dso_loader.cc:49] Successfully opened dynamic library libcudnn.so.8
2020-10-30 17:49:52.552804: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:941] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2020-10-30 17:49:52.553658: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:941] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2020-10-30 17:49:52.554074: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1862] Adding visible gpu devices: 0
gpu PhysicalDevice(name='/physical_device:GPU:0', device_type='GPU')
memory growth: True
2020-10-30 17:49:52.566294: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2020-10-30 17:49:52.566683: I tensorflow/compiler/jit/xla_gpu_device.cc:99] Not creating XLA devices, tf_xla_enable_xla_devices not set
2020-10-30 17:49:52.566874: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:941] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2020-10-30 17:49:52.567403: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1720] Found device 0 with properties: 
pciBusID: 0000:00:08.0 name: EIZO Quadro MED-XN92 computeCapability: 7.5
coreClock: 1.545GHz coreCount: 36 deviceMemorySize: 7.79GiB deviceMemoryBandwidth: 387.49GiB/s
2020-10-30 17:49:52.567458: I tensorflow/stream_executor/platform/default/dso_loader.cc:49] Successfully opened dynamic library libcudart.so.11.0
2020-10-30 17:49:52.567485: I tensorflow/stream_executor/platform/default/dso_loader.cc:49] Successfully opened dynamic library libcublas.so.11
2020-10-30 17:49:52.567504: I tensorflow/stream_executor/platform/default/dso_loader.cc:49] Successfully opened dynamic library libcublasLt.so.11
2020-10-30 17:49:52.567526: I tensorflow/stream_executor/platform/default/dso_loader.cc:49] Successfully opened dynamic library libcufft.so.10
2020-10-30 17:49:52.567543: I tensorflow/stream_executor/platform/default/dso_loader.cc:49] Successfully opened dynamic library libcurand.so.10
2020-10-30 17:49:52.567561: I tensorflow/stream_executor/platform/default/dso_loader.cc:49] Successfully opened dynamic library libcusolver.so.10
2020-10-30 17:49:52.567575: I tensorflow/stream_executor/platform/default/dso_loader.cc:49] Successfully opened dynamic library libcusparse.so.11
2020-10-30 17:49:52.567594: I tensorflow/stream_executor/platform/default/dso_loader.cc:49] Successfully opened dynamic library libcudnn.so.8
2020-10-30 17:49:52.567684: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:941] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2020-10-30 17:49:52.568042: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:941] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2020-10-30 17:49:52.568357: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1862] Adding visible gpu devices: 0
2020-10-30 17:49:52.568391: I tensorflow/stream_executor/platform/default/dso_loader.cc:49] Successfully opened dynamic library libcudart.so.11.0
2020-10-30 17:49:53.170188: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1261] Device interconnect StreamExecutor with strength 1 edge matrix:
2020-10-30 17:49:53.170215: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1267]      0 
2020-10-30 17:49:53.170242: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1280] 0:   N 
2020-10-30 17:49:53.170421: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:941] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2020-10-30 17:49:53.170821: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:941] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2020-10-30 17:49:53.171182: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:941] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2020-10-30 17:49:53.171562: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1406] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:0 with 6182 MB memory) -> physical GPU (device: 0, name: EIZO Quadro MED-XN92, pci bus id: 0000:00:08.0, compute capability: 7.5)
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
embedding (Embedding)        (None, None, 64)          4672      
_________________________________________________________________
lstm (LSTM)                  (None, 128)               98816     
_________________________________________________________________
dense (Dense)                (None, 128)               16512     
_________________________________________________________________
dense_1 (Dense)              (None, 1)                 129       
=================================================================
Total params: 120,129
Trainable params: 120,129
Non-trainable params: 0
_________________________________________________________________
None
Using the class weighting: {0: 0.4444444444444444, 1: 0.5555555555555556}
2020-10-30 17:49:56.995192: I tensorflow/compiler/mlir/mlir_graph_optimization_pass.cc:116] None of the MLIR optimization passes are enabled (registered 2)
2020-10-30 17:49:56.995550: I tensorflow/core/platform/profile_utils/cpu_utils.cc:108] CPU Frequency: 3696475000 Hz
Epoch 1/100
2020-10-30 17:49:58.136541: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:592] layout failed: Invalid argument: Size of values 2 does not match size of permutation 4 @ fanin shape insequential/dense/BiasAdd-0-TransposeNHWCToNCHW-LayoutOptimizer
2020-10-30 17:49:58.321330: I tensorflow/stream_executor/platform/default/dso_loader.cc:49] Successfully opened dynamic library libcublas.so.11
2020-10-30 17:49:58.830217: I tensorflow/stream_executor/platform/default/dso_loader.cc:49] Successfully opened dynamic library libcublasLt.so.11
2020-10-30 17:49:58.917439: I tensorflow/stream_executor/platform/default/dso_loader.cc:49] Successfully opened dynamic library libcudnn.so.8
1330/1333 [============================>.] - ETA: 0s - loss: 0.2418 - acc: 0.68852020-10-30 17:50:12.174596: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:592] layout failed: Invalid argument: Size of values 2 does not match size of permutation 4 @ fanin shape insequential/dense/BiasAdd-0-TransposeNHWCToNCHW-LayoutOptimizer
1333/1333 [==============================] - 16s 9ms/step - loss: 0.2417 - acc: 0.6886 - val_loss: 0.4471 - val_acc: 0.7751
Epoch 2/100
1333/1333 [==============================] - 11s 9ms/step - loss: 0.1911 - acc: 0.7768 - val_loss: 0.4404 - val_acc: 0.7847
Epoch 3/100
1333/1333 [==============================] - 12s 9ms/step - loss: 0.1792 - acc: 0.7961 - val_loss: 0.3821 - val_acc: 0.8101
Epoch 4/100
1333/1333 [==============================] - 12s 9ms/step - loss: 0.1678 - acc: 0.8102 - val_loss: 0.4049 - val_acc: 0.7934
Epoch 5/100
1333/1333 [==============================] - 12s 9ms/step - loss: 0.1609 - acc: 0.8155 - val_loss: 0.3738 - val_acc: 0.8189
Epoch 6/100
1333/1333 [==============================] - 12s 9ms/step - loss: 0.1532 - acc: 0.8283 - val_loss: 0.3472 - val_acc: 0.8342
Epoch 7/100
1333/1333 [==============================] - 11s 9ms/step - loss: 0.1397 - acc: 0.8454 - val_loss: 0.3404 - val_acc: 0.8397
Epoch 8/100
1333/1333 [==============================] - 11s 8ms/step - loss: 0.1311 - acc: 0.8586 - val_loss: 0.3169 - val_acc: 0.8533
Epoch 9/100
1333/1333 [==============================] - 12s 9ms/step - loss: 0.1214 - acc: 0.8670 - val_loss: 0.3090 - val_acc: 0.8623
Epoch 10/100
1333/1333 [==============================] - 12s 9ms/step - loss: 0.1119 - acc: 0.8790 - val_loss: 0.3214 - val_acc: 0.8569
Epoch 11/100
1333/1333 [==============================] - 12s 9ms/step - loss: 0.1003 - acc: 0.8911 - val_loss: 0.3133 - val_acc: 0.8690
Epoch 12/100
1333/1333 [==============================] - 12s 9ms/step - loss: 0.0897 - acc: 0.9061 - val_loss: 0.3262 - val_acc: 0.8642
Epoch 13/100
1333/1333 [==============================] - 12s 9ms/step - loss: 0.0784 - acc: 0.9189 - val_loss: 0.3467 - val_acc: 0.8638
236/236 [==============================] - 1s 4ms/step - loss: 0.3090 - acc: 0.8623
[0.30899688601493835, 0.8623256087303162]
2020-10-30 17:52:34.855446: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:592] layout failed: Invalid argument: Size of values 2 does not match size of permutation 4 @ fanin shape insequential/dense/BiasAdd-0-TransposeNHWCToNCHW-LayoutOptimizer
Best performance at threshold: 0.4796482412060301
Calculated 7525 predictions with a mean value of 0.4370075762271881
Evaluating using threshold 0.4796482412060301
Cut-off threshold: 0.4796
Evaluation counts: {'TN': 3661, 'FP': 583, 'FN': 449, 'TP': 2832}
+------------------+----------------+--------------------+
| Accuracy 86.286% | Predicted safe | Predicted phishing |
+------------------+----------------+--------------------+
|   Not phishing   |    TN: 3661    |      FP: 583       |
|                  |  NPV: 89.075%  |    FDR: 17.072%    |
|                  |  TNR: 86.263%  |    FPR: 13.737%    |
|   Is phishing    |    FN: 449     |      TP: 2832      |
|                  |  FOR: 10.925%  |    PPV: 82.928%    |
|                  |  FNR: 13.685%  |    TPR: 86.315%    |
+------------------+----------------+--------------------+

Examples for TN Bin range: 0.00073767104 - 0.09641512 , Num. Samples: 2680
                               input  ground truth  prediction
0     external.frgn2-1.fna.fbcdn.net             0    0.001826
1                     m17.zmlxaqo.me             0    0.002751
2                     m1.pjdzmis.com             0    0.001309
3                    nl.zazaplay.com             0    0.034415
4            static.securedtouch.com             0    0.009018
5                    08.bgp.m565m.cn             0    0.007713
6                       mc.yandex.ua             0    0.038544
7                images.meesho.co.id             0    0.094320
8         e6449.dsce2.akamaiedge.net             0    0.003591
9                           csub.edu             0    0.023387
10                      1g.synr.asia             0    0.046314
11                         open8.com             0    0.065576
12                   m28.gzankeb.com             0    0.001823
13    speedtest.mediantbroadband.com             0    0.012560
14  scontent-lax3-1.cdninstagram.com             0    0.006103

Examples for TN Bin range: 0.09641512 - 0.19209257 , Num. Samples: 338
                                       input  ground truth  prediction
0                               batworld.com             0    0.189741
1                                   meimo.cc             0    0.162660
2                               ja-tukuba.jp             0    0.181687
3                                doceree.com             0    0.174871
4                     webmail.roulemabos.com             0    0.107781
5                                  uvenco.ru             0    0.135885
6                                 firmex.com             0    0.180981
7                                   icldc.ae             0    0.122841
8   wfqqreader-1252317822.image.myqcloud.com             0    0.156188
9                                vahblyw.org             0    0.164897
10                           mitraduta.co.id             0    0.167558
11                             saglik.gov.tr             0    0.130029
12                                pfizer.com             0    0.191651
13                         cantonfair.org.cn             0    0.098778
14                                oklink.com             0    0.105598

Examples for TN Bin range: 0.19209257 - 0.28777 , Num. Samples: 270
                           input  ground truth  prediction
0                    qubiqle.com             0    0.281636
1                 www.labays.com             0    0.234597
2                   nfhvkdp.info             0    0.226117
3                 realgain.co.kr             0    0.228534
4                    conbase.top             0    0.251976
5     cwu-vanity.instructure.com             0    0.210433
6                     enter5.com             0    0.211571
7                   reachplc.com             0    0.216619
8   crow-wpengine.netdna-ssl.com             0    0.207189
9                 www.careem.com             0    0.269816
10              www.nanovisor.io             0    0.287554
11                 www.fun2u.biz             0    0.254512
12                gkinvest.co.id             0    0.249888
13                  www.3799.com             0    0.208607
14                   daekong.com             0    0.273093

Examples for TN Bin range: 0.28777 - 0.38344747 , Num. Samples: 203
                     input  ground truth  prediction
0            utahtutor.com             0    0.371420
1           mikrosimage.eu             0    0.309477
2             smzdmimg.com             0    0.349975
3            coldreams.com             0    0.313818
4              sdnbhv.info             0    0.379307
5           xiexingnet.com             0    0.365675
6              cabralsk.cf             0    0.347865
7   pdw-adf.userreport.com             0    0.372328
8             jet-porda.de             0    0.311209
9            sjgroup.local             0    0.370204
10              nol.com.br             0    0.315714
11         www.porntry.com             0    0.374096
12             dgxinda.com             0    0.325559
13          np-tokumei.net             0    0.336091
14             pepsico.com             0    0.303395

Examples for TN Bin range: 0.38344747 - 0.4791249 , Num. Samples: 169
                              input  ground truth  prediction
0                    www.wrcbtv.com             0    0.441002
1                   alumnos.upla.cl             0    0.429029
2                  www.mobil123.com             0    0.435025
3                      dataminr.com             0    0.441780
4                   www.frachri.com             0    0.406250
5                        pkcoieh.ga             0    0.477031
6   secure07a.amer.gslbjpmchase.com             0    0.385407
7                     uscategui.com             0    0.414396
8                  palcomonline.com             0    0.470491
9                     zuishidai.com             0    0.436745
10                     daveking.com             0    0.424506
11                 diariodesign.com             0    0.462537
12                      liwrnskz.ru             0    0.468292
13                  www.e-go.com.au             0    0.430346
14                    felgueres.com             0    0.441377

Examples for FP Bin range: 0.47989374 - 0.5836909 , Num. Samples: 162
                             input  ground truth  prediction
0               city-furniture.com             0    0.508803
1                      opensrs.net             0    0.563031
2                    travelagu.com             0    0.509845
3                    zapaka.com.au             0    0.528178
4   hhscovid19portal.azureedge.net             0    0.499109
5                   abrankings.com             0    0.481347
6                     huajindp.com             0    0.557127
7             offingervipolof.club             0    0.548674
8                         irinn.ir             0    0.561199
9                 ntp-sop.inria.fr             0    0.526376
10                    fj133165.com             0    0.542226
11                sunny-portal.com             0    0.492807
12                 kfedisbroke.com             0    0.531020
13               www.mytestcom.net             0    0.521992
14                 upc-g.chello.nl             0    0.539581

Examples for FP Bin range: 0.5836909 - 0.687488 , Num. Samples: 150
                                       input  ground truth  prediction
0                  support.solarwindsmsp.com             0    0.661952
1                  ale.yingshidaquan0304.com             0    0.628479
2   prod.message-broker.last-mile.amazon.dev             0    0.610678
3                           greerlawfirm.com             0    0.597153
4                           khartoumbank.com             0    0.633720
5                         paltalkconnect.com             0    0.635018
6                               live-hub.net             0    0.594316
7                             studyfinds.org             0    0.661915
8                           lzaudholding.com             0    0.623820
9                                uffs.edu.br             0    0.682886
10                       michaelnugent.co.uk             0    0.631068
11  irginia-db5.us-east-1.lb.campuspress.com             0    0.613418
12                       www.centbrowser.com             0    0.598979
13                          buhajargroup.com             0    0.676785
14                              tirumala.org             0    0.630036

Examples for FP Bin range: 0.687488 - 0.7912852 , Num. Samples: 138
                              input  ground truth  prediction
0                     montelimar.fr             0    0.787795
1                          bban.top             0    0.746404
2                       mail.dmp.re             0    0.736635
3             nvhfonkbvdekjcwvrt.us             0    0.717489
4           selangorbusinesshub.com             0    0.743502
5                   todayxsgpoz.com             0    0.740515
6                   krebergroup.com             0    0.718761
7                  tagihanpulsa.com             0    0.723181
8            www.penookinfotech.com             0    0.707833
9              livingscriptures.com             0    0.701407
10  dc-83c8c2e84a76.donate-2020.com             0    0.708266
11               requentlyfths.club             0    0.752670
12                 ursoftdns.com.br             0    0.698403
13           scrabblewordfinder.org             0    0.789190
14                 naviglandgps.com             0    0.692196

Examples for FP Bin range: 0.7912852 - 0.89508235 , Num. Samples: 77
                                       input  ground truth  prediction
0                            freeproxy.world             0    0.891221
1                 jardindecocagneafrique.com             0    0.809826
2                     amazingfilehosting.com             0    0.878496
3                              true-apk.info             0    0.882408
4                      bluecubecreatives.com             0    0.817033
5                         stephanecottin.com             0    0.862456
6                   vibracoustic-cvas.com.tr             0    0.839400
7   accb.ap-northeast-2.elasticbeanstalk.com             0    0.893960
8                      tract-old-engines.net             0    0.894969
9                     teleperformanceusa.com             0    0.859106
10                   prefabrikyapimarket.com             0    0.867551
11                org.whois.rfc-clueless.org             0    0.858679
12                            poetikatour.lv             0    0.876996
13                 staplescanada.zendesk.com             0    0.799101
14                           thaidevhost.com             0    0.807563

Examples for FP Bin range: 0.89508235 - 0.9988795 , Num. Samples: 55
                                       input  ground truth  prediction
0                        listener.ecp123.com             0    0.897503
1            www.eus-www.sway-extensions.com             0    0.958327
2                 sup.app-bang-dream-gbp.com             0    0.931483
3                      authns1.webpartner.dk             0    0.966933
4                        movable-ink-601.com             0    0.988290
5                    www.mercadolibre.com.ar             0    0.914418
6   ns8.aaafc94b3a37b75ae9cb60afc42e86fe.org             0    0.996585
7              image.harryanddavid-email.com             0    0.965513
8                     nationalparksite.co.uk             0    0.942953
9                       puppet.securealm.net             0    0.923198
10         hadiahfreefireindonesia.go1.my.id             0    0.996508
11                     unithese-resteven.icu             0    0.951225
12   unitevous-transedufudom-enusomozent.net             0    0.963450
13                  upos-sz-static.hdslb.com             0    0.897458
14                                2095101.ru             0    0.932946

Examples for FN Bin range: 0.0015901173 - 0.09708761 , Num. Samples: 86
                                       input  ground truth  prediction
0                      old.gotyoufloored.com             1    0.015478
1   doc.google.share.pressurecookerindia.com             1    0.014898
2                       senat.poltekba.ac.id             1    0.089448
3                      winerspot.mikecrm.com             1    0.030749
4                                newmy-3.com             1    0.018185
5                                apptuts.bio             1    0.086695
6                               wifreight.cf             1    0.008036
7                     takipci.sosyalkedi.com             1    0.010906
8                              ligatokens.io             1    0.080280
9                                 igoh2o.net             1    0.028993
10                      top.chasingtheid.com             1    0.002966
11              bayanicgiyimsitesi.somee.com             1    0.037803
12                            www.navic7.net             1    0.036665
13                   redirectbdp.totispa.com             1    0.021853
14                                  sovve.nl             1    0.092889

Examples for FN Bin range: 0.09708761 - 0.1925851 , Num. Samples: 58
                                       input  ground truth  prediction
0                             www.control.pw             1    0.102346
1                                  ibn36.com             1    0.144847
2                   sexeducation.atspace.com             1    0.175864
3                                 atbpro.com             1    0.143024
4                                 moatia.com             1    0.131405
5                         faleupas.kissr.com             1    0.177808
6                            tantiengiang.vn             1    0.102041
7                          forum.sexabout.ru             1    0.104568
8                    webmail.jomolufarms.com             1    0.099579
9                            events-sa.co.za             1    0.155235
10      americanas.app.seuatendimento.credit             1    0.139100
11                        sh1493982.a.had.su             1    0.142146
12                                boclog.com             1    0.158257
13  n.securedupgradeaccess.com.mgccampus.com             1    0.109232
14                                 tu762.com             1    0.123681

Examples for FN Bin range: 0.1925851 - 0.2880826 , Num. Samples: 98
                           input  ground truth  prediction
0              www.coderllci.com             1    0.266152
1                    suelunn.com             1    0.276253
2                    irporel.com             1    0.192658
3                  eagle-its.com             1    0.232300
4                shop-sports.biz             1    0.229206
5                        anon.to             1    0.205724
6                    s-venmo.com             1    0.201042
7                www.agfmanu.com             1    0.199795
8              assicuriamoci.net             1    0.282765
9   www.one.file.xclusivehit.net             1    0.207554
10                  medicalbi.it             1    0.249609
11                    shleta.com             1    0.230437
12                    iaak12.org             1    0.214448
13                    suxury.com             1    0.228365
14          wagrup-new.qhigh.com             1    0.276561

Examples for FN Bin range: 0.2880826 - 0.3835801 , Num. Samples: 79
                      input  ground truth  prediction
0            whatssappp.top             1    0.366372
1           nalgsovetnyk.ru             1    0.295397
2             updtowa.xf.cz             1    0.370194
3         csgomagic-win.com             1    0.308319
4   mail.mohdnourshahen.com             1    0.365940
5             kartam.com.au             1    0.352101
6           rhodvillecu.com             1    0.340045
7                272101.com             1    0.351776
8             rollaries.com             1    0.322299
9            tierretyr.live             1    0.319244
10        www.sfs-group.net             1    0.345325
11             iphonexn.com             1    0.339238
12              govdvla.com             1    0.304174
13               myeeuk.com             1    0.297938
14          licogi18.com.vn             1    0.303316

Examples for FN Bin range: 0.3835801 - 0.47907758 , Num. Samples: 127
                          input  ground truth  prediction
0               misrschools.com             1    0.462270
1                  ciet-itac.ca             1    0.472288
2                   immb.com.au             1    0.405964
3               actionfilmz.com             1    0.400122
4   corptoduct4.shockbyte.games             1    0.458000
5          www.littekencreme.nl             1    0.426483
6                 careeresl.com             1    0.417289
7                www.bmisec.com             1    0.416548
8                 area53.com.br             1    0.469472
9                ajaxfrance.com             1    0.459782
10             crestlesunny.com             1    0.472927
11              ecosolarion.com             1    0.421531
12              www.landpage.co             1    0.445673
13                gaughrith.com             1    0.455162
14             creativegigs.net             1    0.420851

Examples for TP Bin range: 0.4797831 - 0.58368903 , Num. Samples: 183
                           input  ground truth  prediction
0               isabellacano.com             1    0.505505
1                 caviarkelp.com             1    0.495798
2                   kuberavc.com             1    0.515785
3                   smartmco.com             1    0.545397
4                   sa-samba.com             1    0.499236
5                     qanfin.com             1    0.505225
6              redacrecenter.org             1    0.555332
7                 mawcompany.com             1    0.488395
8               www.estiklal.com             1    0.548034
9   polrul-85240581.alsalhaj.com             1    0.482257
10          www.expresstravel.it             1    0.542184
11           ecscreditrepair.com             1    0.496471
12                  uzbekart.com             1    0.487085
13    www.laforestaincantata.dog             1    0.549389
14              domosmartllc.com             1    0.521439

Examples for TP Bin range: 0.58368903 - 0.68759495 , Num. Samples: 281
                       input  ground truth  prediction
0        allthishappened.com             1    0.604911
1    daotaoquoctedhxd.edu.vn             1    0.623096
2       www.tesosubastas.org             1    0.644371
3          www.storstart.com             1    0.677649
4             www.inbioma.pe             1    0.612063
5             gb-revolut.com             1    0.653655
6   meriamstuurfotografie.nl             1    0.667239
7           tacticalhvac.net             1    0.603656
8              moqsocial.com             1    0.686818
9              moqsocial.com             1    0.686818
10               m42club.com             1    0.594287
11           wishnquotes.com             1    0.663337
12          osohealthful.com             1    0.646076
13               shophgi.com             1    0.602334
14           aladdinstar.com             1    0.632148

Examples for TP Bin range: 0.68759495 - 0.79150087 , Num. Samples: 314
                                    input  ground truth  prediction
0                   therootfoundation.org             1    0.709868
1                   www.theroyalaegis.com             1    0.696106
2                          www.zjgsyds.cn             1    0.765590
3                 graphicommunication.com             1    0.719345
4                           osrsgames.com             1    0.742855
5                www.indivisibleheart.com             1    0.723827
6               rrqeventmobilelegends.com             1    0.721633
7                        managedevices.cc             1    0.730796
8                          liderkuota.com             1    0.790152
9                    ketoneswithmindy.com             1    0.776659
10                 www.shannonebeling.com             1    0.734715
11                   o2supportbilling.com             1    0.776781
12                       remove-device.cc             1    0.764982
13                     www.nixtechnix.com             1    0.786221
14  cebuphonly.jrzoutsourcingservices.com             1    0.749541

Examples for TP Bin range: 0.79150087 - 0.89540684 , Num. Samples: 334
                               input  ground truth  prediction
0             www.hydrolyzeultra.com             1    0.849653
1   hotelpousadadasaraucarias.com.br             1    0.887290
2        www.3dsignsmelbourne.com.au             1    0.884936
3                          hatac.net             1    0.877164
4                 thescrapescape.com             1    0.807780
5                       gold-mail.ru             1    0.815649
6         wilsonparrotfoundation.org             1    0.856035
7          www.themooregroupofsc.com             1    0.832021
8                  e-stat-co-jp.info             1    0.886373
9                     nixtechnix.com             1    0.815634
10            marketinghelper.com.au             1    0.870068
11            mytaxreturns-govuk.com             1    0.844636
12             beautifulattendee.com             1    0.806628
13              paytouch-free.online             1    0.843577
14              netflixloginhelp.com             1    0.830842

Examples for TP Bin range: 0.89540684 - 0.99931276 , Num. Samples: 1668
                                       input  ground truth  prediction
0              secure234.inmotionhosting.com             1    0.988558
1                              amazon-cg.xyz             1    0.974676
2          publictvirtusupott.atwebpages.com             1    0.985855
3         groupbokepwhatsapp.grub-wa23.my.id             1    0.997745
4                             173.82.129.237             1    0.999034
5                              csytravels.in             1    0.916754
6   -e-w-me-ss-age-po-rt-al.wl.r.appspot.com             1    0.999150
7   update-system-update.esenbogashuttle.com             1    0.991657
8   .marketplace-item382472.highshark.com.ng             1    0.971108
9                         xn--tequeon-8za.pe             1    0.983672
10  ww.secure07statementxx3mnd48.duckdns.org             1    0.992536
11  dot-solar-vertex-285913.rj.r.appspot.com             1    0.999304
12                secure.oldschool.com-gf.ru             1    0.979880
13  aaa7739a2b6d3e596335723b856a435a431db.ph             1    0.997664
14        halifax.co.uk.app-review-2067.info             1    0.995147

Phishing ULR examples:
Prediction on url: frgcxtmjawefgrthdcusge.dab 0.10695601
Prediction on url: evilmadeupurl.phish 0.14836672
Prediction on url: evil.madeupurl.phish 0.084076315

Safe URL examples:
Prediction on url: google.com 0.093087696
Prediction on url: www.google.com 0.32636034
Prediction on url: gmail.google.com 0.003183104
Prediction on url: mail.google.com 0.0030769757
Prediction on url: tudelft.nl 0.055145584
Prediction on url: brightspace.tudelft.nl 0.4495974
Prediction on url: colab.research.google.com 0.002710549
Prediction on url: 00-gayrettepe-t3-8---00-gayrettepe-xrs-t2-1.statik.turktelekom.com.tr 0.012957305
```