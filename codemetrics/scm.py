#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Factor things common to git and svn."""

import abc
import collections
import datetime as dt

import pandas as pd

from . import pbar
from .internals import get_now


LogEntry = collections.namedtuple('LogEntry',
                                  'revision author date textmods kind action '
                                  'propmods path message added removed'.split())


def _to_dataframe(records):
    """Convert log entries to a pandas DataFrame.

    :param iter(LogEntry) records: records generated by the SCM log command.
    :rtype pandas.DataFrame:

    """
    columns = LogEntry._fields
    result = pd.DataFrame.from_records(records, columns=columns)
    result['date'] = pd.to_datetime(result['date'], utc=True)
    # FIXME categorize columns that should be categorized.
    return result


class _ScmLogCollector(abc.ABC):
    """Base class for svn and git.

    def get_log(self) is to be implemented in subclasses.

    """

    def __init__(self, after=None, before=None, path='.', progress_bar=None):
        """Initialize.

        Args:
            after: start date of log entries.
            before: end date of log entries (default to latest).
            path: location of local source repository.
            progress_bar: implements tqdm.tqdm interface.

        """
        self.path = path
        assert after is None or after.tzinfo is not None
        self.after = after or get_now() - dt.timedelta(365)
        assert before is None or before.tzinfo is not None
        self.before = before
        self.progress_bar = progress_bar
        if self.progress_bar is not None and self.after is None:
            raise ValueError("progress_bar requires 'after' parameter")

    def process_output_to_df(self, cmd_output):
        """Factor creation of dataframe from output of command.

        Args:
            cmd_output: generator returning lines of output from the cmd line.

        Returns:
              pandas.DataFrame

        """
        log_entries = []
        with pbar.ProgressBarAdapter(self.progress_bar,
                                     self.after) as progress_bar:
            for entry in self.get_log_entries(cmd_output):
                log_entries.append(entry)
                progress_bar.update(entry.date)
        df = _to_dataframe(log_entries)
        return df

    @abc.abstractmethod
    def get_log(self):
        """Call git log and return the log entries as a DataFrame.

        Returns:
            pandas.DataFrame.

        """
        pass

    @abc.abstractmethod
    def get_log_entries(self, cmd_output):
        """Convert output of git log --xml -v to a csv.

        Args:
            text: iterable of string (one for each line).

        Yields:
            tuple of :class:`codemetrics.scm.LogEntry`.

        """
        pass