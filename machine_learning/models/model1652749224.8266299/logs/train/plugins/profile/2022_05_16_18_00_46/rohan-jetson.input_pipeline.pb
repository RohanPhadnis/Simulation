	=?U???*@=?U???*@!=?U???*@	????vK@????vK@!????vK@"{
=type.googleapis.com/tensorflow.profiler.PerGenericStepDetails:=?U???*@?_cD???A?ɨ2??@Y?9?踺@rEagerKernelExecute 0*	?A`??rk@2U
Iterator::Model::ParallelMapV2ҧU??f??!???+
;@)ҧU??f??1???+
;@:Preprocessing2l
5Iterator::Model::ParallelMapV2::Zip[1]::ForeverRepeat?i????!y?G?3<@)??qQ-"??1Dl???>7@:Preprocessing2f
/Iterator::Model::ParallelMapV2::Zip[0]::FlatMapB&9{??!??}??7@)??tޡ?1"? ???/@:Preprocessing2F
Iterator::Model&䃞ͪ??!??O E@)y ?H???1?????.@:Preprocessing2v
?Iterator::Model::ParallelMapV2::Zip[0]::FlatMap[0]::TensorSlicewMHk:??!_(???@)wMHk:??1_(???@:Preprocessing2Z
#Iterator::Model::ParallelMapV2::Zip?
?F??!X????L@)???&????18f`@Ò@:Preprocessing2x
AIterator::Model::ParallelMapV2::Zip[1]::ForeverRepeat::FromTensor???/fK??!?!?q?@)???/fK??1?!?q?@:Preprocessing:?
]Enqueuing data: you may want to combine small input data chunks into fewer but larger chunks.
?Data preprocessing: you may increase num_parallel_calls in <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map" target="_blank">Dataset map()</a> or preprocess the data OFFLINE.
?Reading data from files in advance: you may tune parameters in the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch size</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave cycle_length</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer_size</a>)
?Reading data from files on demand: you should read data IN ADVANCE using the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer</a>)
?Other data reading or processing: you may consider using the <a href="https://www.tensorflow.org/programmers_guide/datasets" target="_blank">tf.data API</a> (if you are not using it now)?
:type.googleapis.com/tensorflow.profiler.BottleneckAnalysis?
host?Your program is HIGHLY input-bound because 54.1% of the total step time sampled is waiting for input. Therefore, you should first focus on reducing the input time.no*no9????vK@IUgC??F@Zno>Look at Section 3 for the breakdown of input time on the host.B?
@type.googleapis.com/tensorflow.profiler.GenericStepTimeBreakdown?
	?_cD????_cD???!?_cD???      ?!       "      ?!       *      ?!       2	?ɨ2??@?ɨ2??@!?ɨ2??@:      ?!       B      ?!       J	?9?踺@?9?踺@!?9?踺@R      ?!       Z	?9?踺@?9?踺@!?9?踺@b      ?!       JCPU_ONLYY????vK@b qUgC??F@