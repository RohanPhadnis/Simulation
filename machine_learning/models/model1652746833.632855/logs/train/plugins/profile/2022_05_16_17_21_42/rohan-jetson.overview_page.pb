?	?B=}?X@?B=}?X@!?B=}?X@	??QY????QY??!??QY??"{
=type.googleapis.com/tensorflow.profiler.PerGenericStepDetails:?B=}?X@VDM??(??AJ`s??X@Y,)w?????rEagerKernelExecute 0*	Q???c@2x
AIterator::Model::ParallelMapV2::Zip[1]::ForeverRepeat::FromTensorw?ِf??!?\7??G@)w?ِf??1?\7??G@:Preprocessing2l
5Iterator::Model::ParallelMapV2::Zip[1]::ForeverRepeat???????!TKkWO@)Ĵo????1??<Tý-@:Preprocessing2U
Iterator::Model::ParallelMapV2:??)??!?3?$u'@):??)??1?3?$u'@:Preprocessing2F
Iterator::Model????}ɺ?!g ?w?4@)?d?,?i??1u?5"@:Preprocessing2v
?Iterator::Model::ParallelMapV2::Zip[0]::FlatMap[0]::TensorSlice<???ܴ??!?N????@)<???ܴ??1?N????@:Preprocessing2f
/Iterator::Model::ParallelMapV2::Zip[0]::FlatMapE?[??b??!C2?Ci(@)0??9\??1??wm?G@:Preprocessing2Z
#Iterator::Model::ParallelMapV2::Zip?0(?hr??!&???S@)??=]ݱ??1@AH?4@:Preprocessing:?
]Enqueuing data: you may want to combine small input data chunks into fewer but larger chunks.
?Data preprocessing: you may increase num_parallel_calls in <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map" target="_blank">Dataset map()</a> or preprocess the data OFFLINE.
?Reading data from files in advance: you may tune parameters in the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch size</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave cycle_length</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer_size</a>)
?Reading data from files on demand: you should read data IN ADVANCE using the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer</a>)
?Other data reading or processing: you may consider using the <a href="https://www.tensorflow.org/programmers_guide/datasets" target="_blank">tf.data API</a> (if you are not using it now)?
:type.googleapis.com/tensorflow.profiler.BottleneckAnalysis?
device?Your program is NOT input-bound because only 0.3% of the total step time sampled is waiting for input. Therefore, you should focus on reducing other time.no*no9??QY??Iv'????X@Zno#You may skip the rest of this page.B?
@type.googleapis.com/tensorflow.profiler.GenericStepTimeBreakdown?
	VDM??(??VDM??(??!VDM??(??      ?!       "      ?!       *      ?!       2	J`s??X@J`s??X@!J`s??X@:      ?!       B      ?!       J	,)w?????,)w?????!,)w?????R      ?!       Z	,)w?????,)w?????!,)w?????b      ?!       JCPU_ONLYY??QY??b qv'????X@Y      Y@q??9??@?@"?	
device?Your program is NOT input-bound because only 0.3% of the total step time sampled is waiting for input. Therefore, you should focus on reducing other time.b
`input_pipeline_analyzer (especially Section 3 for the breakdown of input operations on the Host)Q
Otf_data_bottleneck_analysis (find the bottleneck in the tf.data input pipeline)m
ktrace_viewer (look at the activities on the timeline of each Host Thread near the bottom of the trace view)"T
Rtensorflow_stats (identify the time-consuming operations executed on the CPU_ONLY)"Z
Xtrace_viewer (look at the activities on the timeline of each CPU_ONLY in the trace view)*?
?<a href="https://www.tensorflow.org/guide/data_performance_analysis" target="_blank">Analyze tf.data performance with the TF Profiler</a>*y
w<a href="https://www.tensorflow.org/guide/data_performance" target="_blank">Better performance with the tf.data API</a>2M
=type.googleapis.com/tensorflow.profiler.GenericRecommendation
nono2no:
Refer to the TF2 Profiler FAQb?31.3% of Op time on the host used eager execution. Performance could be improved with <a href="https://www.tensorflow.org/guide/function" target="_blank">tf.function.</a>2"CPU: B 