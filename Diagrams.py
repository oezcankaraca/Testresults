import pandas as pd
import matplotlib.pyplot as plt

# Data from CSV file
df = pd.read_csv('/Users/ozcankaraca/Desktop/Testresults/5peers.csv', sep=";")

df.columns = df.columns.str.strip()
del df["TestID"]

#------------------------------------------------------------------------------------------------------------------
# 1 - Error rate for bandwidth with an increasing number of peers (with P2P) for a specific file size.

df['With Super-Peers'] = df['With Super-Peers'].astype(str)

df_filtered = df[(df['With Super-Peers'].str.upper() == 'TRUE') & (df['Total Received Bytes'] == 67108864)]

grouped_data = df_filtered.groupby('Number of Peers')[['Maximum Bandwidth Error Rate [%]', 
                                                       'Minimum Bandwidth Error Rate [%]', 
                                                       'Average Bandwidth Error Rate [%]']].mean().reset_index()

plt.figure(figsize=(10, 6), dpi=300) 

plt.plot(grouped_data['Number of Peers'], grouped_data['Maximum Bandwidth Error Rate [%]'], 
         label='Maximum', marker='o', linestyle='-', linewidth=2)
plt.plot(grouped_data['Number of Peers'], grouped_data['Minimum Bandwidth Error Rate [%]'], 
         label='Minimum', marker='s', linestyle='-', linewidth=2)
plt.plot(grouped_data['Number of Peers'], grouped_data['Average Bandwidth Error Rate [%]'], 
         label='Average', marker='^', linestyle='-', linewidth=2)

plt.xlabel('Number of Peers', fontsize=20)
plt.ylabel('Bandwidth Error Rate [%]', fontsize=20)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16) 

plt.legend(fontsize=18)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

plt.tight_layout()
plt.savefig('bandwidth_error_rate_with_p2p.png', format='png', dpi=300) 
plt.show()

#------------------------------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------------------------------
# 2 - Error rate for bandwidth with an increasing number of peers (without P2P) for a specific file size

df['With Super-Peers'] = df['With Super-Peers'].astype(str)

df_filtered = df[(df['With Super-Peers'].str.upper() == 'FALSE') & (df['Total Received Bytes'] == 67108864)]

grouped_data = df_filtered.groupby('Number of Peers')[['Maximum Bandwidth Error Rate [%]', 
                                                       'Minimum Bandwidth Error Rate [%]', 
                                                       'Average Bandwidth Error Rate [%]']].mean().reset_index()

plt.figure(figsize=(10, 6), dpi=300)

plt.plot(grouped_data['Number of Peers'], grouped_data['Maximum Bandwidth Error Rate [%]'], 
         label='Maximum', marker='o', linestyle='-', linewidth=2)
plt.plot(grouped_data['Number of Peers'], grouped_data['Minimum Bandwidth Error Rate [%]'], 
         label='Minimum', marker='s', linestyle='-', linewidth=2)
plt.plot(grouped_data['Number of Peers'], grouped_data['Average Bandwidth Error Rate [%]'], 
         label='Average', marker='^', linestyle='-', linewidth=2)

plt.xlabel('Number of Peers', fontsize=20)
plt.ylabel('Bandwidth Error Rate [%]', fontsize=20)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16) 

plt.legend(fontsize=18)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()

plt.savefig('bandwidth_error_rate_without_p2p.png', format='png', dpi=300)
plt.show()

#------------------------------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------------------------------
# 3 - Error rate for latency with an increasing number of peers (with P2P) for a specific file size.

df['With Super-Peers'] = df['With Super-Peers'].astype(str)

df_filtered = df[(df['With Super-Peers'].str.upper() == 'TRUE') & (df['Total Received Bytes'] == 67108864)]

grouped_data = df_filtered.groupby('Number of Peers')[['Maximum Latency Error Rate [%]', 
                                                       'Minimum Latency Error Rate [%]', 
                                                       'Average Latency Error Rate [%]']].mean().reset_index()

plt.figure(figsize=(10, 6), dpi=300)

plt.plot(grouped_data['Number of Peers'], grouped_data['Maximum Latency Error Rate [%]'], 
         label='Maximum', marker='o', linestyle='-', linewidth=2)
plt.plot(grouped_data['Number of Peers'], grouped_data['Minimum Latency Error Rate [%]'], 
         label='Minimum', marker='s', linestyle='-', linewidth=2)
plt.plot(grouped_data['Number of Peers'], grouped_data['Average Latency Error Rate [%]'], 
         label='Average', marker='^', linestyle='-', linewidth=2)

plt.xlabel('Number of Peers', fontsize=20)
plt.ylabel('Latency Error Rate [%]', fontsize=20)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16) 

plt.legend(fontsize=18)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()

plt.savefig('latency_error_rate_with_p2p.png', format='png', dpi=300)
plt.show()

#------------------------------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------------------------------
# 4 - Error rate for latency with an increasing number of peers (without P2P) for a specific file size.

df['With Super-Peers'] = df['With Super-Peers'].astype(str)

df_filtered = df[(df['With Super-Peers'].str.upper() == 'FALSE') & (df['Total Received Bytes'] == 67108864)]

grouped_data = df_filtered.groupby('Number of Peers')[['Maximum Latency Error Rate [%]', 
                                                       'Minimum Latency Error Rate [%]', 
                                                       'Average Latency Error Rate [%]']].mean().reset_index()

plt.figure(figsize=(10, 6), dpi=300)

plt.plot(grouped_data['Number of Peers'], grouped_data['Maximum Latency Error Rate [%]'],
         label='Maximum', marker='o', linestyle='-', linewidth=2)
plt.plot(grouped_data['Number of Peers'], grouped_data['Minimum Latency Error Rate [%]'],
         label='Minimum', marker='s', linestyle='-', linewidth=2)
plt.plot(grouped_data['Number of Peers'], grouped_data['Average Latency Error Rate [%]'],
         label='Average', marker='^', linestyle='-', linewidth=2)

plt.xlabel('Number of Peers', fontsize=20)
plt.ylabel('Latency Error Rate [%]', fontsize=20)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16) 

plt.legend(fontsize=18)

plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()

plt.savefig('latency_error_rate_without_p2p.png', format='png', dpi=300)
plt.show()

#------------------------------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------------------------------
# 5 - Error rate for data transfer time with an increasing number of peers (with P2P) for a specific file size.

df['With Super-Peers'] = df['With Super-Peers'].astype(str)

df_filtered = df[(df['With Super-Peers'].str.upper() == 'TRUE') & (df['Total Received Bytes'] == 67108864)]

grouped_data = df_filtered.groupby('Number of Peers')[['Maximum Transfer Error Rate [%]', 
                                                       'Minimum Transfer Error Rate [%]', 
                                                       'Average Transfer Error Rate [%]']].mean().reset_index()

plt.figure(figsize=(10, 6), dpi=300)

plt.plot(grouped_data['Number of Peers'], grouped_data['Maximum Transfer Error Rate [%]'],
         label='Maximum', marker='o', linestyle='-', linewidth=2)
plt.plot(grouped_data['Number of Peers'], grouped_data['Minimum Transfer Error Rate [%]'],
         label='Minimum', marker='s', linestyle='-', linewidth=2)
plt.plot(grouped_data['Number of Peers'], grouped_data['Average Transfer Error Rate [%]'],
         label='Average', marker='^', linestyle='-', linewidth=2)

plt.xlabel('Number of Peers', fontsize=20)
plt.ylabel('Transfer Time Error Rate [%]', fontsize=20)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16) 

plt.legend(fontsize=18)

plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()

plt.savefig('transfer_error_rate_increasing_peers_with_p2p.png', format='png', dpi=300)
plt.show()

#------------------------------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------------------------------
# 6 - Error rate for data transfer time with an increasing number of peers (without P2P) for a specific file size.

df['With Super-Peers'] = df['With Super-Peers'].astype(str)

df_filtered = df[(df['With Super-Peers'].str.upper() == 'FALSE') & (df['Total Received Bytes'] == 67108864)]

grouped_data = df_filtered.groupby('Number of Peers')[['Maximum Transfer Error Rate [%]', 
                                                       'Minimum Transfer Error Rate [%]', 
                                                       'Average Transfer Error Rate [%]']].mean().reset_index()

plt.figure(figsize=(10, 6), dpi=300)

plt.plot(grouped_data['Number of Peers'], grouped_data['Maximum Transfer Error Rate [%]'],
         label='Maximum', marker='o', linestyle='-', linewidth=2)
plt.plot(grouped_data['Number of Peers'], grouped_data['Minimum Transfer Error Rate [%]'],
         label='Minimum', marker='s', linestyle='-', linewidth=2)
plt.plot(grouped_data['Number of Peers'], grouped_data['Average Transfer Error Rate [%]'],
         label='Average', marker='^', linestyle='-', linewidth=2)

plt.xlabel('Number of Peers', fontsize=20)
plt.ylabel('Transfer Time Error Rate [%]', fontsize=20)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16) 

plt.legend(fontsize=18)

plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()

plt.savefig('transfer_error_rate_increasing_peers_without_p2p.png', format='png', dpi=300)
plt.show()

#------------------------------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------------------------------
# 7 - Error rate for data transfer time with an increasing size of file (with P2P) for a specific number of peers.

df['With Super-Peers'] = df['With Super-Peers'].astype(str)


df_filtered = df[(df['With Super-Peers'].str.upper() == 'TRUE') & (df['Number of Peers'] == 5)]

grouped_data = df_filtered.groupby('Total Received Bytes')[['Maximum Transfer Time Error Rate [%]', 
                                                            'Minimum Transfer Time Error Rate [%]', 
                                                            'Average Transfer Time Error Rate [%]']].mean().reset_index()

plt.figure(figsize=(10, 6), dpi=300)

plt.plot(grouped_data['Total Received Bytes'], grouped_data['Maximum Transfer Time Error Rate [%]'],
         label='Maximum', marker='o', linestyle='-', linewidth=2)
plt.plot(grouped_data['Total Received Bytes'], grouped_data['Minimum Transfer Time Error Rate [%]'],
         label='Minimum', marker='s', linestyle='-', linewidth=2)
plt.plot(grouped_data['Total Received Bytes'], grouped_data['Average Transfer Time Error Rate [%]'],
         label='Average', marker='^', linestyle='-', linewidth=2)

plt.xlabel('File Size (Total Received Bytes)', fontsize=20)
plt.ylabel('Transfer Time Error Rate [%]', fontsize=20)
plt.xscale('log')
plt.xticks(fontsize=16)
plt.yticks(fontsize=16) 

plt.legend(fontsize=18)

plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()

plt.savefig('transfer_error_rate_increasing_size_file_with_p2p.png', format='png', dpi=300)
plt.show()

#------------------------------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------------------------------
# 8 - Error rate for data transfer time with an increasing size of file (without P2P) for a specific number of peers.

df['With Super-Peers'] = df['With Super-Peers'].astype(str)


df_filtered = df[(df['With Super-Peers'].str.upper() == 'FALSE') & (df['Number of Peers'] == 5)]

grouped_data = df_filtered.groupby('Total Received Bytes')[['Maximum Transfer Time Error Rate [%]', 
                                                            'Minimum Transfer Time Error Rate [%]', 
                                                            'Average Transfer Time Error Rate [%]']].mean().reset_index()

plt.figure(figsize=(10, 6), dpi=300)

plt.plot(grouped_data['Total Received Bytes'], grouped_data['Maximum Transfer Time Error Rate [%]'],
         label='Maximum', marker='o', linestyle='-', linewidth=2)
plt.plot(grouped_data['Total Received Bytes'], grouped_data['Minimum Transfer Time Error Rate [%]'],
         label='Minimum', marker='s', linestyle='-', linewidth=2)
plt.plot(grouped_data['Total Received Bytes'], grouped_data['Average Transfer Time Error Rate [%]'],
         label='Average', marker='^', linestyle='-', linewidth=2)

plt.xlabel('File Size (Total Received Bytes)', fontsize=20)
plt.ylabel('Transfer Time Error Rate [%]', fontsize=20)
plt.xscale('log')  
plt.xticks(fontsize=16)
plt.yticks(fontsize=16) 

plt.legend(fontsize=18)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()

plt.savefig('transfer_error_rate_increasing_size_file_without_p2p.png', format='png', dpi=300)
plt.show()

#------------------------------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------------------------------
# 9 - Connection time for a connection between two container with an increasing number of peers (with P2P) for a specific file size.

df['With Super-Peers'] = df['With Super-Peers'].astype(str)

df_filtered = df[(df['With Super-Peers'].str.upper() == 'TRUE') & (df['Total Received Bytes'] == 2239815)]

grouped_data = df_filtered.groupby('Number of Peers')[['Maximum Connection Time [s]', 
                                                       'Minimum Connection Time [s]', 
                                                       'Average Connection Time [s]']].mean().reset_index()

plt.figure(figsize=(10, 6), dpi=300)

plt.plot(grouped_data['Number of Peers'], grouped_data['Maximum Connection Time [s]'],
         label='Max', marker='o', linestyle='-', linewidth=2)
plt.plot(grouped_data['Number of Peers'], grouped_data['Minimum Connection Time [s]'],
         label='Min', marker='s', linestyle='-', linewidth=2)
plt.plot(grouped_data['Number of Peers'], grouped_data['Average Connection Time [s]'],
         label='Avg ', marker='^', linestyle='-', linewidth=2)

plt.xlabel('Number of Peers', fontsize=20)
plt.ylabel('Connection Time [s]', fontsize=20)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16) 

plt.legend(fontsize=18)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()

plt.savefig('connection_time_increasing_number_peers_with_p2p.png', format='png', dpi=300)
plt.show()

#------------------------------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------------------------------
# 10 - Connection time for a connection between two container with an increasing number of peers (without P2P) for a specific file size.

df['With Super-Peers'] = df['With Super-Peers'].astype(str)

df_filtered = df[(df['With Super-Peers'].str.upper() == 'FALSE') & (df['Total Received Bytes'] == 2239815)]

grouped_data = df_filtered.groupby('Number of Peers')[['Maximum Connection Time [s]', 
                                                       'Minimum Connection Time [s]', 
                                                       'Average Connection Time [s]']].mean().reset_index()

plt.figure(figsize=(10, 6), dpi=300)

plt.plot(grouped_data['Number of Peers'], grouped_data['Maximum Connection Time [s]'],
         label='Max', marker='o', linestyle='-', linewidth=2)
plt.plot(grouped_data['Number of Peers'], grouped_data['Minimum Connection Time [s]'],
         label='Min', marker='s', linestyle='-', linewidth=2)
plt.plot(grouped_data['Number of Peers'], grouped_data['Average Connection Time [s]'],
         label='Avg', marker='^', linestyle='-', linewidth=2)

plt.xlabel('Number of Peers', fontsize=20)
plt.ylabel('Connection Time [s]', fontsize=20)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16) 

plt.legend(fontsize=18)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()

plt.savefig('connection_time_increasing_number_peers_without_p2p.png', format='png', dpi=300)
plt.show()

#------------------------------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------------------------------
# 11 - Transfer time of two container with an increasing number of peers (with P2P) for a specific file size.

df['With Super-Peers'] = df['With Super-Peers'].astype(str)

df_filtered = df[(df['With Super-Peers'].str.upper() == 'TRUE') & (df['Total Received Bytes'] == 2239815)]

grouped_data = df_filtered.groupby('Number of Peers')[['Maximum Transfer Time [s]', 
                                                       'Minimum Transfer Time [s]', 
                                                       'Average Transfer Time [s]']].mean().reset_index()

plt.figure(figsize=(10, 6), dpi=300)

plt.plot(grouped_data['Number of Peers'], grouped_data['Maximum Transfer Time [s]'],
         label='Max', marker='o', linestyle='-', linewidth=2)
plt.plot(grouped_data['Number of Peers'], grouped_data['Minimum Transfer Time [s]'],
         label='Min', marker='s', linestyle='-', linewidth=2)
plt.plot(grouped_data['Number of Peers'], grouped_data['Average Transfer Time [s]'],
         label='Avg', marker='^', linestyle='-', linewidth=2)

plt.xlabel('Number of Peers', fontsize=20)
plt.ylabel('Transfer Time [s]', fontsize=20)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16) 

plt.legend(fontsize=18)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()

plt.savefig('transfer_time_increasing_number_peers_with_p2p.png', format='png', dpi=300)
plt.show()

#------------------------------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------------------------------
# 12 - Transfer time of two container with an increasing number of peers (without P2P) for a specific file size.

df['With Super-Peers'] = df['With Super-Peers'].astype(str)

df_filtered = df[(df['With Super-Peers'].str.upper() == 'FALSE') & (df['Total Received Bytes'] == 2239815)]

grouped_data = df_filtered.groupby('Number of Peers')[['Maximum Transfer Time [s]', 
                                                       'Minimum Transfer Time [s]', 
                                                       'Average Transfer Time [s]']].mean().reset_index()

plt.figure(figsize=(10, 6), dpi=300)

plt.plot(grouped_data['Number of Peers'], grouped_data['Maximum Transfer Time [s]'],
         label='Max', marker='o', linestyle='-', linewidth=2)
plt.plot(grouped_data['Number of Peers'], grouped_data['Minimum Transfer Time [s]'],
         label='Min', marker='s', linestyle='-', linewidth=2)
plt.plot(grouped_data['Number of Peers'], grouped_data['Average Transfer Time [s]'],
         label='Avg', marker='^', linestyle='-', linewidth=2)

plt.xlabel('Number of Peers', fontsize=20)
plt.ylabel('Transfer Time [s]', fontsize=20)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16) 

plt.legend(fontsize=18)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()

plt.savefig('transfer_time_increasing_number_peers_without_p2p.png', format='png', dpi=300)
plt.show()

#------------------------------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------------------------------
# 13 - Total time of two container with an increasing number of peers (with P2P) for a specific file size.

df['With Super-Peers'] = df['With Super-Peers'].astype(str)

df_filtered = df[(df['With Super-Peers'].str.upper() == 'TRUE') & (df['Total Received Bytes'] == 2239815)]

grouped_data = df_filtered.groupby('Number of Peers')[['Maximum Total Time [s]', 
                                                       'Minimum Total Time [s]', 
                                                       'Average Total Time [s]']].mean().reset_index()

plt.figure(figsize=(10, 6), dpi=300)

plt.plot(grouped_data['Number of Peers'], grouped_data['Maximum Total Time [s]'],
         label='Maximum', marker='o', linestyle='-', linewidth=2)
plt.plot(grouped_data['Number of Peers'], grouped_data['Minimum Total Time [s]'],
         label='Minimum', marker='s', linestyle='-', linewidth=2)
plt.plot(grouped_data['Number of Peers'], grouped_data['Average Total Time [s]'],
         label='Average', marker='^', linestyle='-', linewidth=2)

plt.xlabel('Number of Peers', fontsize=20)
plt.ylabel('Total Time [s]', fontsize=20)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16) 

plt.legend(fontsize=18)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()

plt.savefig('total_time_increasing_number_peers_with_p2p.png', format='png', dpi=300)
plt.show()

#------------------------------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------------------------------
# 14 - Total time of two container with an increasing number of peers (without P2P) for a specific file size.

df['With Super-Peers'] = df['With Super-Peers'].astype(str)

df_filtered = df[(df['With Super-Peers'].str.upper() == 'FALSE') & (df['Total Received Bytes'] == 2239815)]

grouped_data = df_filtered.groupby('Number of Peers')[['Maximum Total Time [s]', 
                                                       'Minimum Total Time [s]', 
                                                       'Average Total Time [s]']].mean().reset_index()

plt.figure(figsize=(10, 6), dpi=300)

plt.plot(grouped_data['Number of Peers'], grouped_data['Maximum Total Time [s]'],
         label='Maximum', marker='o', linestyle='-', linewidth=2)
plt.plot(grouped_data['Number of Peers'], grouped_data['Minimum Total Time [s]'],
         label='Minimum', marker='s', linestyle='-', linewidth=2)
plt.plot(grouped_data['Number of Peers'], grouped_data['Average Total Time [s]'],
         label='Average', marker='^', linestyle='-', linewidth=2)

plt.xlabel('Number of Peers', fontsize=20)
plt.ylabel('Total Time [s]', fontsize=20)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16) 

plt.legend(fontsize=18)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()

plt.savefig('total_time_increasing_number_peers_without_p2p.png', format='png', dpi=300)
plt.show()

#------------------------------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------------------------------
# 15 - Total duration of the whole process with 20 peers and an increasing size of file with and without P2P

df['With Super-Peers'] = df['With Super-Peers'].astype(str)

df_with_super_peer = df[(df['With Super-Peers'].str.upper() == 'TRUE') & (df['Number of Peers'] == 20)]

df_without_super_peer = df[(df['With Super-Peers'].str.upper() == 'FALSE') & (df['Number of Peers'] == 20)]

grouped_data_with = df_with_super_peer.groupby('Total Received Bytes')['Total Duration [s]'].mean().reset_index()
grouped_data_without = df_without_super_peer.groupby('Total Received Bytes')['Total Duration [s]'].mean().reset_index()

plt.figure(figsize=(12, 7), dpi=300)

plt.plot(grouped_data_with['Total Received Bytes'], grouped_data_with['Total Duration [s]'],
         label='With P2P', marker='o', linestyle='-', linewidth=2)
plt.plot(grouped_data_without['Total Received Bytes'], grouped_data_without['Total Duration [s]'],
         label='Without P2P', marker='s', linestyle='-', linewidth=2)

plt.xlabel('File Size (Total Received Bytes)', fontsize=20)
plt.ylabel('Total Duration [s]', fontsize=20)
plt.xscale('log')
plt.xticks(fontsize=16)
plt.yticks(fontsize=16) 

plt.legend(fontsize=18)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()

plt.savefig('total_duration_with_20_peers_with_and_without_p2p.png', format='png', dpi=300)
plt.show()

#------------------------------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------------------------------
# 16 - Total duration of the whole process with 35 peers and an increasing size of file with and without P2P

df['With Super-Peers'] = df['With Super-Peers'].astype(str)

df_with_super_peer = df[(df['With Super-Peers'].str.upper() == 'TRUE') & (df['Number of Peers'] == 35)]

df_without_super_peer = df[(df['With Super-Peers'].str.upper() == 'FALSE') & (df['Number of Peers'] == 35)]

grouped_data_with = df_with_super_peer.groupby('Total Received Bytes')['Total Duration [s]'].mean().reset_index()
grouped_data_without = df_without_super_peer.groupby('Total Received Bytes')['Total Duration [s]'].mean().reset_index()

plt.figure(figsize=(12, 7), dpi=300)

plt.plot(grouped_data_with['Total Received Bytes'], grouped_data_with['Total Duration [s]'],
         label='With P2P', marker='o', linestyle='-', linewidth=2)
plt.plot(grouped_data_without['Total Received Bytes'], grouped_data_without['Total Duration [s]'],
         label='Without P2P', marker='s', linestyle='-', linewidth=2)

plt.xlabel('File Size (Total Received Bytes)', fontsize=20)
plt.ylabel('Total Duration [s]', fontsize=20)
plt.xscale('log')
plt.xticks(fontsize=16)
plt.yticks(fontsize=16) 

plt.legend(fontsize=18)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()

plt.savefig('total_duration_with_35_peers_with_and_without_p2p.png', format='png', dpi=300)
plt.show()

#------------------------------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------------------------------
# 17 - Total duration of the whole process with 50 peers and an increasing size of file with and without P2P

df['With Super-Peers'] = df['With Super-Peers'].astype(str)

df_with_super_peer = df[(df['With Super-Peers'].str.upper() == 'TRUE') & (df['Number of Peers'] == 50)]

df_without_super_peer = df[(df['With Super-Peers'].str.upper() == 'FALSE') & (df['Number of Peers'] == 50)]

grouped_data_with = df_with_super_peer.groupby('Total Received Bytes')['Total Duration [s]'].mean().reset_index()
grouped_data_without = df_without_super_peer.groupby('Total Received Bytes')['Total Duration [s]'].mean().reset_index()

plt.figure(figsize=(12, 7), dpi=300)

plt.plot(grouped_data_with['Total Received Bytes'], grouped_data_with['Total Duration [s]'],
         label='With P2P', marker='o', linestyle='-', linewidth=2)
plt.plot(grouped_data_without['Total Received Bytes'], grouped_data_without['Total Duration [s]'],
         label='Without P2P', marker='s', linestyle='-', linewidth=2)

plt.xlabel('File Size (Total Received Bytes)', fontsize=20)
plt.ylabel('Total Duration [s]', fontsize=20)
plt.xscale('log')
plt.xticks(fontsize=16)
plt.yticks(fontsize=16) 

plt.legend(fontsize=18)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()

plt.savefig('total_duration_with_50_peers_with_and_without_p2p.png', format='png', dpi=300)
plt.show()

#------------------------------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------------------------------
# 18 - Total duration of the whole process with 75 peers and an increasing size of file with and without P2P

df['With Super-Peers'] = df['With Super-Peers'].astype(str)

df_with_super_peer = df[(df['With Super-Peers'].str.upper() == 'TRUE') & (df['Number of Peers'] == 75)]

df_without_super_peer = df[(df['With Super-Peers'].str.upper() == 'FALSE') & (df['Number of Peers'] == 75)]

grouped_data_with = df_with_super_peer.groupby('Total Received Bytes')['Total Duration [s]'].mean().reset_index()
grouped_data_without = df_without_super_peer.groupby('Total Received Bytes')['Total Duration [s]'].mean().reset_index()

plt.figure(figsize=(12, 7), dpi=300)

plt.plot(grouped_data_with['Total Received Bytes'], grouped_data_with['Total Duration [s]'],
         label='With P2P', marker='o', linestyle='-', linewidth=2)
plt.plot(grouped_data_without['Total Received Bytes'], grouped_data_without['Total Duration [s]'],
         label='Without P2P', marker='s', linestyle='-', linewidth=2)

plt.xlabel('File Size (Total Received Bytes)', fontsize=20)
plt.ylabel('Total Duration [s]', fontsize=20)
plt.xscale('log')
plt.xticks(fontsize=16)
plt.yticks(fontsize=16) 

plt.legend(fontsize=18)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()

plt.savefig('total_duration_with_75_peers_with_and_without_p2p.png', format='png', dpi=300)
plt.show()

#------------------------------------------------------------------------------------------------------------------