import streamlit as st

st.title("Mad Libs Generator")

st.write("Fill in the blanks and generate an inspiring and educational story!")

# User inputs
boy_name = st.text_input("Enter a boy's name:")
friend_name = st.text_input("Enter a friend's name:")

if st.button("Generate Story"):
    if boy_name and friend_name:
        story = (f"One bright morning, {boy_name} and {friend_name} were walking to school, discussing their dreams. "
                 f"{boy_name} wanted to become a scientist, and {friend_name} dreamed of being an astronaut. "
                 f"On their way, they met an old professor who shared a fascinating book about space exploration. "
                 f"Excited, they spent the whole day reading about planets, stars, and the wonders of science. "
                 f"Inspired, {boy_name} and {friend_name} promised to study hard and never give up on their dreams. "
                 f"Years later, {boy_name} became a brilliant scientist, and {friend_name} traveled to space! "
                 f"Their childhood dream had come true because they believed in learning and perseverance. "
                 f"In the end, they realized that knowledge and determination could turn any dream into reality, and they continued to inspire future generations with their incredible journey.")
        st.success(story)
    else:
        st.error("Please enter both names to generate the story.")
