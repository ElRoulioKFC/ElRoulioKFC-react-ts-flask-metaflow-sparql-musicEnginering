from metaflow import FlowSpec, step, Parameter,conda,conda_base


class GetArtistFlow(FlowSpec):
    """
    A flow where Metaflow prints 'Hi'.

    Run this flow to validate that Metaflow is installed correctly.

    """

    @conda_base(libraries={'numpy':'1.15.4'}, python='3.6.5')
    @step
    def start(self):
        """
        This is the 'start' step. All flows must have a step named 'start' that
        is the first step in the fif __name__ == "__main__":
    HelloFlow()low.

        """
        print("HelloFlow is starting.")
        self.next(self.hello)

    @step
    def hello(self):
        """
        A step for metaflow to introduce itself.

        """
        print("Metaflow says: Hi!")
        self.next(self.end)

    @step
    def end(self):
        """
        This is the 'end' step. All flows must have an 'end' step, which is the
        last step in the flow.

        """
        print("HelloFlow is all done.")
if __name__ == "__main__":
    HelloFlow()