%%
%   COURSE: Master statistics and machine learning: intuition, math, code										
%      URL: udemy.com/course/statsml_x/?couponCode=202006 
% 
%  SECTION: Correlation
%    VIDEO: The subgroups correlation paradox
% 
%  TEACHER: Mike X Cohen, sincxpress.com
%

% Note: The official term is "Simpson's paradox"

%%

% a clear MATLAB workspace is a clear mental workspace
close all; clear; clc

%%

% initializations
n = 20; % sample points per group
offsets = [2 3.5 5]; % mean offsets
[x,y,l] = deal(cell(3,1));

% setup figure
figure(1), clf, hold on
c = 'rbk';

% generate and plot data
for datai=1:3
    
    % generate data
    x{datai} = linspace(offsets(datai)-1,offsets(datai)+1,n);
    y{datai} = mean(x{datai}) + randn(1,n)/2;
    
    % plot
    plot(x{datai},y{datai},[c(datai) 'o'],'markersize',12,'markerfacecolor',c(datai))
    
    % subgroup correlation
    [r,p] = corr(x{datai}',y{datai}');
    l{datai} = [ 'r = ' num2str(r,3) ', p = ' num2str(p,3) ];
end


% now correlate the groups
[r,p] = corr(cell2mat(x')',cell2mat(y')');
title([ 'r = ' num2str(r,3) ', p = ' num2str(p,3) ])

xlabel('X'), ylabel('Y')
axis([0 7 0 7])
legend(l,'Location','NorthWest')
set(gca,'fontsize',14)

%% done
