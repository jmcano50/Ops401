from graphviz import Digraph

# Create a new directed graph
dot = Digraph(comment='Threat Model')

# Add nodes for the different components
dot.node('E', 'Employees', shape='ellipse')
dot.node('WAF', 'WAF', shape='shield')
dot.node('GWA', 'Genisys Web App\n(Ubuntu Server)', shape='component')
dot.node('DB', 'SQL Server DB\n(Windows Server 2019)', shape='cylinder')
dot.node('DBA', 'DBA\n(VPN Connection)', shape='ellipse')
dot.node('SA', 'Sys Admin\n(Teamviewer)', shape='ellipse')

# Add edges to represent the data flows
dot.edge('E', 'WAF', label=' HTTPS Traffic In/Out')
dot.edge('WAF', 'GWA', label=' HTTP Traffic')
dot.edge('GWA', 'DB', label=' SQL Transactions')
dot.edge('DBA', 'DB', label=' SQL Management')
dot.edge('SA', 'DB', label=' Remote Management')

# Define subgraphs for trust boundaries
with dot.subgraph(name='cluster_public') as c:
    c.attr(color='blue')
    c.node_attr['style'] = 'filled'
    c.edges([('WAF', 'GWA')])
    c.attr(label='Public Subnet')

with dot.subgraph(name='cluster_private') as c:
    c.attr(color='red')
    c.node_attr['style'] = 'filled'
    c.edges([('GWA', 'DB')])
    c.attr(label='Private Subnet')

# Print the source code of the graph for debugging
print(dot.source)

# Render the graph to a file (the render command returns the filename)
file_path = dot.render('/mnt/data/threat_model_diagram', format='png', cleanup=True)

file_path
