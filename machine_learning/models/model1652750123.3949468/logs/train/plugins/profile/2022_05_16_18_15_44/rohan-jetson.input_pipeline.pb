	L?uT?@L?uT?@!L?uT?@	?奺l#@?奺l#@!?奺l#@"{
=type.googleapis.com/tensorflow.profiler.PerGenericStepDetails:L?uT?@??O???A]ݱ?&?@Y??:?f???rEagerKernelExecute 0*	Q???_t@2U
Iterator::Model::ParallelMapV2???죻?!>?Z?`?@@)???죻?1>?Z?`?@@:Preprocessing2v
?Iterator::Model::ParallelMapV2::Zip[0]::FlatMap[0]::TensorSlice?Nt??!5?'4??9@)?Nt??15?'4??9@:Preprocessing2l
5Iterator::Model::ParallelMapV2::Zip[1]::ForeverRepeat?J???!M?F??P3@)P6?
???1???#0@:Preprocessing2F
Iterator::ModelH??'????!$?????E@)?,?????1??????#@:Preprocessing2f
/Iterator::Model::ParallelMapV2::Zip[0]::FlatMap1?74e???!?ǧ{u?@@)Z??? ͘?1??߷@:Preprocessing2Z
#Iterator::Model::ParallelMapV2::Zip??O@???!?+Y}tL@)W?9?m?1????h?@:Preprocessing2x
AIterator::Model::ParallelMapV2::Zip[1]::ForeverRepeat::FromTensor?//?>:??!?B??o	@)?//?>:??1?B??o	@:Preprocessing:?
]Enqueuing data: you may want to combine small input data chunks into fewer but larger chunks.
?Data preprocessing: you may increase num_parallel_calls in <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map" target="_blank">Dataset map()</a> or preprocess the data OFFLINE.
?Reading data from files in advance: you may tune parameters in the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch size</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave cycle_length</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer_size</a>)
?Reading data from files on demand: you should read data IN ADVANCE using the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer</a>)
?Other data reading or processing: you may consider using the <a href="https://www.tensorflow.org/programmers_guide/datasets" target="_blank">tf.data API</a> (if you are not using it now)?
:type.googleapis.com/tensorflow.profiler.BottleneckAnalysis?
both?Your program is MODERATELY input-bound because 9.7% of the total step time sampled is waiting for input. Therefore, you would need to reduce both the input time and other time.no*moderate2s8.8 % of the total step time sampled is spent on 'All Others' time. This could be due to Python execution overhead.9?奺l#@IPC??~?V@Zno>Look at Section 3 for the breakdown of input time on the host.B?
@type.googleapis.com/tensorflow.profiler.GenericStepTimeBreakdown?
	??O?????O???!??O???      ?!       "      ?!       *      ?!       2	]ݱ?&?@]ݱ?&?@!]ݱ?&?@:      ?!       B      ?!       J	??:?f?????:?f???!??:?f???R      ?!       Z	??:?f?????:?f???!??:?f???b      ?!       JCPU_ONLYY?奺l#@b qPC??~?V@