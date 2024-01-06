import numpy as np
import streamlit as st
import time



st.title('Ma The Matic')
st.subheader("In every exercise, the matrix(s) will be shown, you have to copy it then work on a paper and only at the end"
             " read the result, good luck mf!")
# Matrix Inverse
if st.button('3x3 Matrix Determinant'):
    x = np.random.randint(0, 4, (3, 3))
    st.write('Matrix:')
    st.write(x)
    st.write("In 15 seconds it will show the results down here (do not read it bro)")
    time.sleep(15)
    determinant = round(np.linalg.det(x))
    st.write(f"The Determinant is: {determinant}")


if st.button('4x4 Matrix Determinant'):
    x = np.random.randint(0, 4, (4, 4))
    st.write('Matrix:')
    st.write(x)
    st.write("In 30 seconds it will show the results down here copy the matrix (do not read it bro)")
    time.sleep(30)
    determinant = round(np.linalg.det(x))
    st.write(f"The Determinant is: {determinant}")

# Matrix Inverse
if st.button('3x3 Matrix Inverse Calculation'):
    x = np.random.randint(0, 4, (3, 3))
    st.write('Matrix:')
    st.write(x)
    x_1 = np.linalg.inv(x)
    st.write("In 10 seconds it will show the results down here (do not read it bro)")
    time.sleep(10)
    determinant = round(np.linalg.det(x))
    st.write(f"The Determinant is: {determinant}")
    st.write("Here the Inverse Matrix Multiplied by the determinant (to make things prettier)")
    st.write(x_1 * determinant, determinant)

# Matrix Multiplication / dot Product
if st.button('3x3 Matrix Dot product Calculation (prodotto scalare)'):
    x = np.random.randint(0, 4, (3, 3))
    x2 = np.random.randint(0, 4, (3, 3))
    st.write(x)
    st.write('x')
    st.write(x2)
    # print('\n')
    st.write("In 10 seconds it will show the results down here (do not read it bro)")
    time.sleep(10)
    st.write(np.dot(x, x2))

if st.button('4x4 Matrix Inverse Calculation'):
    x = np.random.randint(0, 4, (4, 4))
    st.write('Matrix:')
    st.write(x)
    x_1 = np.linalg.inv(x)
    st.write("In 10 seconds it will show the results down here (do not read it bro)")
    time.sleep(10)
    determinant = round(np.linalg.det(x))
    st.write(f"The Determinant is: {determinant}")
    st.write("Here the Inverse Matrix Multiplied by the determinant (to make things prettier)")
    st.write(x_1 * determinant, determinant)

# Matrix Multiplication / dot Product
if st.button('4x4 Matrix Dot product Calculation (prodotto scalare)'):
    x = np.random.randint(0, 4, (4, 4))
    x2 = np.random.randint(0, 4, (4, 4))
    st.write(x)
    st.write('x')
    st.write(x2)
    # print('\n')
    st.write("In 10 seconds it will show the results down here (do not read it bro)")
    time.sleep(10)
    st.write(np.dot(x, x2))
