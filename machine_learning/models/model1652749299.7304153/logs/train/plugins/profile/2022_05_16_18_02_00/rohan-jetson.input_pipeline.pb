	v?1<@v?1<@!v?1<@	v?!?D?"@v?!?D?"@!v?!?D?"@"{
=type.googleapis.com/tensorflow.profiler.PerGenericStepDetails:v?1<@???h>??Arjg??@Y??r??{??rEagerKernelExecute 0*	??C?l?p@2U
Iterator::Model::ParallelMapV2V?`????!P>?sE@)V?`????1P>?sE@:Preprocessing2l
5Iterator::Model::ParallelMapV2::Zip[1]::ForeverRepeat???????!?۶ r5@)???}r??1&?????1@:Preprocessing2v
?Iterator::Model::ParallelMapV2::Zip[0]::FlatMap[0]::TensorSlicev??^
??!?Wx???&@)v??^
??1?Wx???&@:Preprocessing2F
Iterator::ModelQ?i>"??!?)M"h?J@)2??Y?Ӟ?1f=<?ѳ&@:Preprocessing2f
/Iterator::Model::ParallelMapV2::Zip[0]::FlatMap??qo~??!?w\W?4@)???????1ؗ@???!@:Preprocessing2Z
#Iterator::Model::ParallelMapV2::ZipI??_????!WֲݗJG@)???}???1A???_?@:Preprocessing2x
AIterator::Model::ParallelMapV2::Zip[1]::ForeverRepeat::FromTensorD?;??)??!{??_?@)D?;??)??1{??_?@:Preprocessing:?
]Enqueuing data: you may want to combine small input data chunks into fewer but larger chunks.
?Data preprocessing: you may increase num_parallel_calls in <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map" target="_blank">Dataset map()</a> or preprocess the data OFFLINE.
?Reading data from files in advance: you may tune parameters in the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch size</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave cycle_length</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer_size</a>)
?Reading data from files on demand: you should read data IN ADVANCE using the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer</a>)
?Other data reading or processing: you may consider using the <a href="https://www.tensorflow.org/programmers_guide/datasets" target="_blank">tf.data API</a> (if you are not using it now)?
:type.googleapis.com/tensorflow.profiler.BottleneckAnalysis?
both?Your program is MODERATELY input-bound because 9.3% of the total step time sampled is waiting for input. Therefore, you would need to reduce both the input time and other time.no*moderate2s4.6 % of the total step time sampled is spent on 'All Others' time. This could be due to Python execution overhead.9v?!?D?"@I?ǻhׯV@Zno>Look at Section 3 for the breakdown of input time on the host.B?
@type.googleapis.com/tensorflow.profiler.GenericStepTimeBreakdown?
	???h>?????h>??!???h>??      ?!       "      ?!       *      ?!       2	rjg??@rjg??@!rjg??@:      ?!       B      ?!       J	??r??{????r??{??!??r??{??R      ?!       Z	??r??{????r??{??!??r??{??b      ?!       JCPU_ONLYYv?!?D?"@b q?ǻhׯV@