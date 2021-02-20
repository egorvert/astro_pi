.. _output_format:

Output Format
=============

The data saved in ``data.csv`` must be kept in a uniform format to allow the large
collection of data to be easily sifted through afterwards by a program. The format is
upheld due to the protocol of merging the data into a ``MetricRecord`` object before
writing it to the file, as the class automatically formats the supplied data into
the shape expected by the csv writer.

The format of each line is as follows::

	timestamp,source,content,deviance,error

	Examples:
	2021-02-20 03:46:31.176709,log,Experiment beginning,0,
	2021-02-20 03:46:34.481528,camera,0.8539240536487881,1,
	2021-02-16 17:09:54.076496,log,Experiment ceased unexpectedly,0,NameError: name 'framcount' is not defined

Columns
*******

Timestamp
~~~~~~~~~

Every record is preceeded with the time at which the row was created. The time is given as
the standard ISO format including microseconds. These must be included not only for to allow
the resulting measurements to be modelled on a graph, but also the rows will not be in order.

As the ``OutputController`` handles logged messages in :ref:`a lazy style <output-controller>`,
some records that have been on the backlog for significant time could be added after new measurements.

Source
~~~~~~

The source column is present to make filtering data records easier. The source can be one of a few values
as listed below:

.. csv-table::
	:header: "Source", "Description"
	:widths: 15, 15

	"log", "A general message about the program's health and/or processes."
	"accelerometer", "Applied to records that either hold measurements from the accelerometer, or errors that occured when measuring it."
	"camera", "Applied to records that either hold measurements from the camera, or errors that occured when measuring it."
	"gyroscope", "Applied to records that either hold measurements from the gyroscope, or errors that occured when measuring it."

Content
~~~~~~~

This is the main body of the row. It is either the value(s) measured from a component or it
is the main message of the log.

Deviance
~~~~~~~~

This is only ever one of two values: 0 or 1. It is 0 in almost all cases including whenever the record
is not a measurement. However it is 1 when the record contains a measurement **and** calculated this/these
value(s) to be deviant compared to the previous values.

The first 3 recorded measurements will always have a deviance of 0, as it only begins checking deviation once
a history of records has been built up.

Error
~~~~~

Hopefully once the data is received back from the ISS, this column will be empty by all rows. However, in the
event that something goes wrong in the program, we will want to see when and where this error occured. This
is especially helpful during development as well.

It is given in the format ``<Type of Error>: <Error Message>``.