function H_YAW321 = calcH_YAW321(q0,q1,q2,q3,rotErr1,rotErr2,rotErr3)
%CALCH_YAW321
%    H_YAW321 = CALCH_YAW321(Q0,Q1,Q2,Q3,ROTERR1,ROTERR2,ROTERR3)

%    This function was generated by the Symbolic Math Toolbox version 6.2.
%    06-Mar-2016 14:23:58

t6 = q0.*2.0;
t7 = q1.*rotErr1;
t8 = q2.*rotErr2;
t9 = q3.*rotErr3;
t2 = -t6+t7+t8+t9;
t11 = q1.*2.0;
t12 = q0.*rotErr1;
t13 = q2.*rotErr3;
t14 = q3.*rotErr2;
t3 = t11+t12+t13-t14;
t16 = q2.*2.0;
t17 = q0.*rotErr2;
t18 = q1.*rotErr3;
t19 = q3.*rotErr1;
t4 = t16+t17-t18+t19;
t21 = q3.*2.0;
t22 = q0.*rotErr3;
t23 = q1.*rotErr2;
t24 = q2.*rotErr1;
t5 = t21+t22+t23-t24;
t10 = t2.^2;
t15 = t3.^2;
t20 = t4.^2;
t25 = t5.^2;
t26 = t10+t15-t20-t25;
t27 = q0.^2;
t28 = q1.^2;
t29 = q2.^2;
t30 = q3.^2;
t56 = t2.*t5;
t57 = t3.*t4;
t31 = t56-t57;
t32 = 1.0./t26.^2;
t33 = 1.0./t26;
t34 = rotErr1.*t27.*(1.0./2.0);
t35 = rotErr1.*t28.*(1.0./2.0);
t36 = q1.*q2.*rotErr2;
t37 = q0.*rotErr1.*(1.0./2.0);
t38 = q2.*rotErr3.*(1.0./2.0);
t62 = q3.*rotErr2.*(1.0./2.0);
t39 = q1+t37+t38-t62;
t40 = q0.*rotErr2.*(1.0./2.0);
t41 = q3.*rotErr1.*(1.0./2.0);
t63 = q1.*rotErr3.*(1.0./2.0);
t42 = q2+t40+t41-t63;
t43 = t39.*t42.*2.0;
t44 = q0.*rotErr3.*(1.0./2.0);
t45 = q1.*rotErr2.*(1.0./2.0);
t64 = q2.*rotErr1.*(1.0./2.0);
t46 = q3+t44+t45-t64;
t47 = q1.*rotErr1.*(1.0./2.0);
t48 = q2.*rotErr2.*(1.0./2.0);
t49 = q3.*rotErr3.*(1.0./2.0);
t50 = -q0+t47+t48+t49;
t65 = t46.*t50.*2.0;
t51 = t43-t65;
t52 = rotErr2.*t27.*(1.0./2.0);
t53 = rotErr2.*t29.*(1.0./2.0);
t54 = q0.*q3.*rotErr1;
t55 = q1.*q2.*rotErr1;
t58 = t31.^2;
t59 = t32.*t58.*4.0;
t60 = t59+1.0;
t61 = 1.0./t60;
H_YAW321 = [t61.*(t33.*(t52+t53+t54+t55-rotErr2.*t28.*(1.0./2.0)-rotErr2.*t30.*(1.0./2.0)-q0.*q1.*rotErr3+q2.*q3.*rotErr3).*4.0-t32.*t51.*(t34+t35+t36-rotErr1.*t29.*(1.0./2.0)-rotErr1.*t30.*(1.0./2.0)+q0.*q2.*rotErr3-q0.*q3.*rotErr2+q1.*q3.*rotErr3).*1.6e1),-t61.*(t33.*(-t34+t35+t36-q0.*q1.*2.0+q2.*q3.*2.0-rotErr1.*t29.*(1.0./2.0)+rotErr1.*t30.*(1.0./2.0)+q0.*q3.*rotErr2).*4.0-t32.*t51.*(t52-t53+t54-t55+q0.*q2.*2.0+q1.*q3.*2.0+rotErr2.*t28.*(1.0./2.0)-rotErr2.*t30.*(1.0./2.0)).*1.6e1),-t61.*(t33.*(-t27+t28-t29+t30+q0.*q1.*rotErr1+q0.*q3.*rotErr3+q1.*q2.*rotErr3-q2.*q3.*rotErr1).*4.0+t32.*t51.*(q0.*q3.*-2.0+q1.*q2.*2.0-rotErr3.*t27.*(1.0./2.0)-rotErr3.*t28.*(1.0./2.0)+rotErr3.*t29.*(1.0./2.0)+rotErr3.*t30.*(1.0./2.0)+q0.*q2.*rotErr1+q1.*q3.*rotErr1).*1.6e1),0.0,0.0,0.0,0.0,0.0,0.0];
