import streamlit as st
import yfinance as yf


from  utilities.utlis import set_page

set_page('News','📰') 



stock_curr = st.session_state['selected_stock']


news_articles =yf.Search(stock_curr, news_count=5).news






if news_articles:
    for i, article in enumerate(news_articles):
        title = article.get('title', 'No title available')
        publisher = article.get('publisher', 'No publisher available')
        link = article.get('link', '#')  # Default to '#' if no link is available
        thumbnail_url = article.get('thumbnail', {}).get('resolutions', [{}])[0].get('url', 'No thumbnail available')

        st.subheader(f"{i+1}. {title}")
        
        st.write(f" [Read More]({link})")

        if thumbnail_url != 'No thumbnail available':
            st.image(thumbnail_url, width=500)

        st.markdown("---")
else:
    st.write("No news available for this stock.")