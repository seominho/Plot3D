import plotly.graph_objects as go
import numpy as np
import streamlit as st

# each axis value and position list
ticktxt_x = ["Ma", "Dt", "So"]
tickvals_x = [1, 3, 5]

ticktxt_y = ["Ag", "Mf", "Mn", "Co", "Co-Neo", "Co-Fold", "Hc", "Df", "Sp"]
tickvals_y = [1, 2, 3, 4, 4+2/3, 4+4/3, 6, 7, 8]

ticktxt_z = ["Sw", "Ro", "Ro-Serv", "Ro-Const", "Ro-AutoL", "AI", "3p", "Qt"]
tickvals_z = [1, 2, 2+2/4, 2+4/4, 2+6/4, 4, 5, 6]

# default origin axis line
line_x_lst = [[0,8],[0,0],[0,0]]
line_y_lst = [[0,0],[0,8],[0,0]]
line_z_lst = [[0,0],[0,0],[0,8]]

# combination plan
COMBINATION_LIST = [dict(x="Ma", y="Mf", z="Ro", n="AMR"),
                    dict(x="Ma", y="Mf", z="3p", n="CNT"),
                    dict(x="Dt", y="Co", z="Ro", n="PARKING"),
                    dict(x="Ma", y="Ag", z="AI", n="Dandelion"),
                    dict(x="Ma", y="Hc", z="Sw", n="Silicon")]

def points_lst2(x,y,z):
    temp_length = 0.15
    temp_point = np.array(x+y+z) # x,y,z should be list
    temp_xdir = np.array([temp_length, 0, 0])
    temp_ydir = np.array([0, temp_length, 0])
    temp_zdir = np.array([0, 0, temp_length])
    
    # above 4 points
    temp_1 = (temp_point + temp_xdir + temp_ydir + temp_zdir)[np.newaxis,:]
    temp_2 = (temp_point + temp_xdir - temp_ydir + temp_zdir)[np.newaxis,:]
    temp_3 = (temp_point - temp_xdir - temp_ydir + temp_zdir)[np.newaxis,:]
    temp_4 = (temp_point - temp_xdir + temp_ydir + temp_zdir)[np.newaxis,:]
    # below 4 points
    temp_5 = (temp_point + temp_xdir + temp_ydir - temp_zdir)[np.newaxis,:]
    temp_6 = (temp_point + temp_xdir - temp_ydir - temp_zdir)[np.newaxis,:]
    temp_7 = (temp_point - temp_xdir - temp_ydir - temp_zdir)[np.newaxis,:]
    temp_8 = (temp_point - temp_xdir + temp_ydir - temp_zdir)[np.newaxis,:]
    
    # line list
    line_list1 = np.concatenate((temp_1, temp_2, temp_3, temp_4, temp_1))
    line_list2 = np.concatenate((temp_5, temp_6, temp_7, temp_8, temp_5))
    line_list3 = np.concatenate((temp_1, temp_5))
    line_list4 = np.concatenate((temp_2, temp_6))
    line_list5 = np.concatenate((temp_3, temp_7))
    line_list6 = np.concatenate((temp_4, temp_8))
    
    return line_list1, line_list2, line_list3, line_list4, line_list5, line_list6


# Draw all
fig = go.Figure()

line_color_lst = ['blue', 'red', 'green']

# len(combination_list) == len(sc_color_lst)
sc_color_lst = ["green","yellow","lightgreen","lightblue","pink"] 

for tmp_x, tmp_y, tmp_z, tmp_c in zip(line_x_lst, line_y_lst, line_z_lst, line_color_lst):
    fig.add_trace(go.Scatter3d(
        x=tmp_x,
        y=tmp_y,
        z=tmp_z,
        mode='lines',
        line = dict(width=2, color=tmp_c),
        hoverinfo='skip'
    ))
    
tmp_f_lst = zip(COMBINATION_LIST, sc_color_lst)    
for ind, tmp_value in enumerate(tmp_f_lst):
    temp_text = f"{tmp_value[0]['n']}"
    
    if type(tmp_value[0]['x']) is str:
        temp_x = [tickvals_x[ticktxt_x.index(tmp_value[0]['x'])]]
    else:
        temp_x = [0]
        
    if type(tmp_value[0]['y']) is str:
        temp_y = [tickvals_y[ticktxt_y.index(tmp_value[0]['y'])]]
    else:
        temp_y = [0]
        
    if type(tmp_value[0]['z']) is str:
        temp_z = [tickvals_z[ticktxt_z.index(tmp_value[0]['z'])]]
    else:
        temp_z = [0]
        
    temp_line_1, temp_line_2, temp_line_3, temp_line_4, temp_line_5, temp_line_6 = points_lst2(temp_x, temp_y, temp_z)    
    
    # Draw 3D points    
    fig.add_trace(go.Scatter3d(
        x=temp_x,
        y=temp_y,
        z=temp_z,
        mode = "markers+text",
        text = temp_text,
        marker = dict(size=5, color=tmp_value[1], symbol="circle", line_color="black", line_width=10)
    ))
    # Draw 3D line #1
    fig.add_trace(go.Scatter3d(
        x=temp_line_1[:,0],
        y=temp_line_1[:,1],
        z=temp_line_1[:,2],
        mode='lines',
        line=dict(width=2, color="white"),
        hoverinfo='skip'
    ))
    # Draw 3D line #2
    fig.add_trace(go.Scatter3d(
        x=temp_line_2[:,0],
        y=temp_line_2[:,1],
        z=temp_line_2[:,2],
        mode='lines',
        line=dict(width=2, color="white"),
        hoverinfo='skip'
    ))
    # Draw 3D line #3
    fig.add_trace(go.Scatter3d(
        x=temp_line_3[:,0],
        y=temp_line_3[:,1],
        z=temp_line_3[:,2],
        mode='lines',
        line=dict(width=2, color="white"),
        hoverinfo='skip'
    ))
    # Draw 3D line #4
    fig.add_trace(go.Scatter3d(
        x=temp_line_4[:,0],
        y=temp_line_4[:,1],
        z=temp_line_4[:,2],
        mode='lines',
        line=dict(width=2, color="white"),
        hoverinfo='skip'
    ))
    # Draw 3D line #5
    fig.add_trace(go.Scatter3d(
        x=temp_line_5[:,0],
        y=temp_line_5[:,1],
        z=temp_line_5[:,2],
        mode='lines',
        line=dict(width=2, color="white"),
        hoverinfo='skip'
    ))
    # Draw 3D line #6
    fig.add_trace(go.Scatter3d(
        x=temp_line_6[:,0],
        y=temp_line_6[:,1],
        z=temp_line_6[:,2],
        mode='lines',
        line=dict(width=2, color="white"),
        hoverinfo='skip'
    ))

fig.update_layout(
    showlegend=False,
    width = 1200,
    height = 1200,
)

fig.update_layout(scene = dict(
    xaxis = dict(
        title_text = "Substance",
        title_font = dict(color='blue', size=20),
        backgroundcolor = "rgb(153, 153, 153)",
        # backgroundcolor = "gray",
        showbackground = True,
        ticktext = ticktxt_x,
        tickvals = tickvals_x,
        tickfont = dict(color='blue', size=11)
    ),
    yaxis = dict(
        title_text = "Field",
        title_font = dict(color="red", size=20),
        backgroundcolor = "rgb(153, 153, 153)",
        # backgroundcolor = "gray",
        showbackground = True,
        ticktext = ticktxt_y,
        tickvals = tickvals_y,
        tickfont = dict(color='red', size=11)
    ),
    zaxis = dict(
        title_text = "Method",
        title_font = dict(color="green", size=20),
        backgroundcolor = "rgb(153, 153, 153)",
        # backgroundcolor = "gray",
        showbackground = True,
        ticktext = ticktxt_z,
        tickvals = tickvals_z,
        tickfont = dict(color='green', size=11)
    ),
))

# Plot on streamlit
st.plotly_chart(fig, use_container_width=False)
# fig.show()