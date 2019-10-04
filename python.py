import numpy as np

def project_vectors(vx, vy, onto_x, onto_y, eps = 1e-6):
    # projected = dot(v,onto/mag(onto))
    mag_onto = np.sqrt(onto_x*onto_x+onto_y*onto_y)
    sel_valid = np.abs(mag_onto) > eps
    vx = vx[sel_valid]
    vy = vy[sel_valid]
    onto_x = onto_x[sel_valid]
    onto_y = onto_y[sel_valid]
    mag_onto = mag_onto[sel_valid]
    projected_length = (vx*onto_x/mag_onto)+(vy*onto_y/mag_onto)
    onto_x_norm = onto_x / mag_onto
    onto_y_norm = onto_y / mag_onto
    projected_v_x = projected_length*onto_x_norm
    projected_v_y = projected_length*onto_y_norm
    orthogonal_v_x = vx-projected_v_x
    orthogonal_v_y = vy-projected_v_y
    return sel_valid, (projected_v_x, projected_v_y), (orthogonal_v_x, orthogonal_v_y)
    
    
