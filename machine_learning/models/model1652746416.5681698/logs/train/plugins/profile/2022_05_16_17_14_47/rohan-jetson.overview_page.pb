?	O崧??d@O崧??d@!O崧??d@	? )а?H@? )а?H@!? )а?H@"{
=type.googleapis.com/tensorflow.profiler.PerGenericStepDetails:O崧??d@?n?KS??A62;?U@Y????9bT@rEagerKernelExecute 0*	??v??H?@2x
AIterator::Model::ParallelMapV2::Zip[1]::ForeverRepeat::FromTensorE?e????!s????lB@)E?e????1s????lB@:Preprocessing2F
Iterator::ModelR}?%???!?????>@)???(\???1H?NI7?2@:Preprocessing2l
5Iterator::Model::ParallelMapV2::Zip[1]::ForeverRepeat?Rx?????!k???uJ@)W	?3???1??ݝ?0@:Preprocessing2U
Iterator::Model::ParallelMapV28??@??!}?T?!_(@)8??@??1}?T?!_(@:Preprocessing2f
/Iterator::Model::ParallelMapV2::Zip[0]::FlatMapu?8F?G??!?yx??&@)??Ӻ??1v???k?@:Preprocessing2v
?Iterator::Model::ParallelMapV2::Zip[0]::FlatMap[0]::TensorSlice?qS??!?kl??}@)?qS??1?kl??}@:Preprocessing2Z
#Iterator::Model::ParallelMapV2::Zipd???q??!????CQ@)? ?hUK??1:?V?+?@:Preprocessing:?
]Enqueuing data: you may want to combine small input data chunks into fewer but larger chunks.
?Data preprocessing: you may increase num_parallel_calls in <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map" target="_blank">Dataset map()</a> or preprocess the data OFFLINE.
?Reading data from files in advance: you may tune parameters in the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch size</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave cycle_length</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer_size</a>)
?Reading data from files on demand: you should read data IN ADVANCE using the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer</a>)
?Other data reading or processing: you may consider using the <a href="https://www.tensorflow.org/programmers_guide/datasets" target="_blank">tf.data API</a> (if you are not using it now)?
:type.googleapis.com/tensorflow.profiler.BottleneckAnalysis?
host?Your program is HIGHLY input-bound because 49.0% of the total step time sampled is waiting for input. Therefore, you should first focus on reducing the input time.no*no9? )а?H@I&??/OzI@Zno>Look at Section 3 for the breakdown of input time on the host.B?
@type.googleapis.com/tensorflow.profiler.GenericStepTimeBreakdown?
	?n?KS???n?KS??!?n?KS??      ?!       "      ?!       *      ?!       2	62;?U@62;?U@!62;?U@:      ?!       B      ?!       J	????9bT@????9bT@!????9bT@R      ?!       Z	????9bT@????9bT@!????9bT@b      ?!       JCPU_ONLYY? )а?H@b q&??/OzI@Y      Y@q?9j*,???"?
host?Your program is HIGHLY input-bound because 49.0% of the total step time sampled is waiting for input. Therefore, you should first focus on reducing the input time.b
`input_pipeline_analyzer (especially Section 3 for the breakdown of input operations on the Host)Q
Otf_data_bottleneck_analysis (find the bottleneck in the tf.data input pipeline)m
ktrace_viewer (look at the activities on the timeline of each Host Thread near the bottom of the trace view)"T
Rtensorflow_stats (identify the time-consuming operations executed on the CPU_ONLY)"Z
Xtrace_viewer (look at the activities on the timeline of each CPU_ONLY in the trace view)*?
?<a href="https://www.tensorflow.org/guide/data_performance_analysis" target="_blank">Analyze tf.data performance with the TF Profiler</a>*y
w<a href="https://www.tensorflow.org/guide/data_performance" target="_blank">Better performance with the tf.data API</a>2M
=type.googleapis.com/tensorflow.profiler.GenericRecommendation
nono2no:
Refer to the TF2 Profiler FAQ2"CPU: B 