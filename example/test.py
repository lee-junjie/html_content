
from html_content import HtmlContent, Type
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


def create_df():
    """Create a pandas DataFrame"""
    df = pd.DataFrame(np.random.randn(10, 4), columns=['A', 'B', 'C', 'D'])
    df['Name'] = [f'x{i}' for i in range(0, 10)]
    df.iloc[0, 2] = np.nan
    return df


def create_matplotlib_fig():
    plt.clf()
    sns.lineplot(x=[1, 2, 3], y=[2, 3, 4])
    fig = plt.gcf()
    return fig


def create_plotly_fig():
    import plotly.express as px
    fig = px.scatter(x=range(10), y=range(10))
    return fig


def main():
    content = HtmlContent('Title of example')

    # markdown
    content.add_markdown('# Header')
    content.add_markdown('***')
    content.add_markdown('## success text', bg_color=Type.SUCCESS)
    content.add_markdown('## warning text', bg_color=Type.WARNING)
    content.add_markdown('## error text', bg_color=Type.ERROR)
    content.add_markdown('normal text')

    # add fig
    content.add_matplotlib_fig(create_matplotlib_fig())
    content.add_plotly_fig(create_plotly_fig())

    # add HTML
    content.add_html('<b>Bold font</b>')

    # add pandas
    df = create_df()
    content.add_df(df, caption='pandas table with diverging_gradient=False', diverging_gradient=False)
    content.add_df(df, caption='pandas table with diverging_gradient=True', diverging_gradient=True)

    # save content to HTML
    # content.get_html()
    content.save_html('example/content.html')


if __name__ == '__main__':
    main()
