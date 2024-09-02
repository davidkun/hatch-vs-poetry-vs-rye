from uv_demo.demo import dataframe_from


def test_dataframe_from():
    df = dataframe_from(
        """A,B,C
    0.0,10.0,200.1"""
    )
    assert len(df.count()) == 1
