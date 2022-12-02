import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Performa Model", page_icon=":bar_chart:", layout="wide")
st.title('Performa Model - HaloFILKOM')

st.header('Model Machine Learning')

df_report_onehot_rf = pd.read_csv('df_report_ml/report_onehot_rf.csv')
df_report_label_rf = pd.read_csv('df_report_ml/report_label_rf.csv')
df_report_label_nb = pd.read_csv('df_report_ml/report_label_nb.csv')
df_report_onehot_knn = pd.read_csv('df_report_ml/report_onehot_knn.csv')
df_report_label_knn = pd.read_csv('df_report_ml/report_label_knn.csv')
df_report_onehot_svm = pd.read_csv('df_report_ml/report_onehot_svm.csv')

classes = ['alur_get_nim_mahasiswa_filkom_ub','alur_pasca_ujian_skripsi','angsur_sap','banding_ukt_mahasiswa','bantuan_kemendikbud_tidak_terverifikasi','bantuan_ukt','bantuan_ukt_dan_ukt_kemendikbud_ristek','batas_akhir_pendaftaran_semhas_ujian_skripsi','batas_konversi_nilai_ke_huruf','batas_sks_beban_mhs','bebas_pustaka_ub','bebas_tanggungan_laboratorium_filkom_ub','cara_daftar_bantuan_kemendikbud_ristek','cek_siam_untuk_tagihan','crisis_centre_uas_filkom_20211','daftar_ulang','dosen_pembimbing_ujian_skripsi_tidak_hadir_salah_satu','edaran_skripsi','faq_perkuliahan_hybrid_filkom_ub','form_pasca_ujian_skripsi','foto_yudisium','foto_yudisium_sc218','ijazah','jadwal_bantuan','kip_k','kip_kuliah','kkn_2020','kontak_hp_daring_kps_tif__tekom','konversi_mk_perpindahan_prodi','kriteria_50','ktm_tersedia','kuliah_hybrid','kuota_paket_data','layanan','layanan_ruang_baca_filkom_ub','legalisir_ijazah','legalisir_khs_dll_dtif','link_data_uji','list_dosen_minat_skripsi','mahasiswa_kritis_sudah_ujian__status_do','mhs_kritis_ujian_sblm_21072022_yudisium','nilai_mbkm_belum_keluar_20212','nilai_pkm__kkn','nip_khajur_kps_tif','no_response','pembatalan_mk_pkl_skripsi','pembayaran_diluar_jadwal_registrasi','peminjaman_fasilitas_lab','peminjaman_ijazah','penambahan_sks_melebihi_batas_maksimum_mk_dari_ip_beban_jtif','pencairan_beasiswa_kemendikbud','pencairan_saldo_ukt','pendaftaran_seminar_hasil_ujian_skripsi_filkom_ub','pendaftaran_yudisium_filkom_ub','pendataan_kelas_penuh','pengajuan_bantuan','pengajuan_nilai_praktikum','pengajuan_praproposal_terkendala','pengajuan_proposal_skripsi_di_luar_jadwal_jtif','pengajuan_st_dosen_pembimbing_lomba','pengajuan_st_dospem_dan_reward_prestasi','pengajuan_transkrip_keperluan_beasiswa_mhs_do_semhas_validasi_kps_dll','pengajuan_transkrip_validasi_kps__jtif','pengambilan_ijazah_non_prosesi','pengambilan_ktm','pengambilan_sertifikat_toefl','penutup','perihal_kehilangan_transkrip_nilai_kuliah','perkuliahan_hybrid','perkuliahan_hybrid_wajib_hadir','permasalahan_sibaku','permohonan_perpanjangan_mahasiswa_do_diluar_skripsi','perpanjangan_masa_studi_filkom_2022_2023_ganjil','perpanjangan_skripsi','perpindahan_prodi_akreditasi_b_ke_a','persyaratan_semhas__ujian_skripsi_filkom','perubahan_judul_skripsi','perubahan_judul_skripsi_filkom_apps','perubahan_jurnal_jtiik_ke_luar_jtiik','pin','pkl__mbkm','prasyarat_perpindahan_stream_keminatan','presensi_perkuliahan','proposal_skripsi_di_luar_jadwal_jtif','prosedur_buka_blokir_telat_pembayaran__pengajuan_validasi_di_luar_jadwal','proses_sertifikasi_it_belum_ada_jawaban','psik__permasalahan_telah_diproses_tiket_ditutup','registrasi_mahasiswa_lama','rekomendasi_magang_dan_mbkm','rekomendasi_magang_mandiri_dan_mbkm','revisi_skripsi','sapaan','sertifikasi_it','sisa_tagihan_50','skl__transkrip','skl_dan_transkrip_sementara','status_wisuda_belum_valid','surat_aktif_kuliah','surat_pengantar_penelitian_skripsi','surat_rekomendasi_beasiswa','syarat_menempuh_mk_lintas_prodi','tagihan_ukt_potongan_50_muncul_kembali','tahapan_pendaftaran_wisuda','tata_cara_pembayaran','templates_dtif','terlambat_pengajuan_bantuan','tidak_bisa_masuk_link_uas','tidak_bisa_mengikuti_perkuliahan_luring_hybrid','tidak_bisa_mengikuti_uas_luring_dan_terpadu','tidak_dapat_upload_berkas_yudisium','toefl','tombol_revisi_proposal_skripsi_pada_filkom_apps','transkrip_final_validasi_rektor_dan_dekan','transkrip_legalisir','turnitin','turnitin_prasyarat_sd_melihat_hasil_turnitin','ujian_khusus_filkom_ub','ujian_skripsi_20212__pendaftaran_yudisium_non_kritis_20212_20221','ukt_mhs_ujian_skripsi_belum_yudisium_selain_kritis','validasi_dosen_pa_pada_krs_siam_mahasiswa_masih_dalam_jadwal','validasi_krs_jtif_terlambat','validasi_wisuda__jurnal_toefl_ti','verifikasi_skm','yudisium','sapaan','penutup','terima_kasih','no_response']

st.write('Model Machine Learning yang digunakan adalah Random Forest Classifier, Naive Bayes, K-Nearest Neighbor, dan Support Vector Machine')

st.subheader('Random Forest Classifier - One Hot encoding')
df_presentation_onehot_rf = df_report_onehot_rf.tail(4).reset_index().drop('index',axis=1).rename(columns={'Unnamed: 0':'Metrics'})
st.dataframe(df_presentation_onehot_rf,use_container_width=True)
# df_report_onehot_rf['Unnamed: 0'] = classes
# st.dataframe(df_report_onehot_rf[:-4].reset_index().drop('index',axis=1).rename(columns={'Unnamed: 0':'Class'}),use_container_width=True)

st.subheader('Random Forest Classifier - Label encoding')
df_presentation_label_rf = df_report_label_rf.tail(3).reset_index().drop('index',axis=1).rename(columns={'Unnamed: 0':'Metrics'})
st.dataframe(df_presentation_label_rf,use_container_width=True)
# df_report_label_rf['Unnamed: 0'] = classes
# st.dataframe(df_report_label_rf[:-3].reset_index().drop('index',axis=1).rename(columns={'Unnamed: 0':'Class'}),use_container_width=True)

st.subheader('Naive Bayes - Label encoding')
df_presentation_label_nb = df_report_label_nb.tail(3).reset_index().drop('index',axis=1).rename(columns={'Unnamed: 0':'Metrics'})
st.dataframe(df_presentation_label_nb,use_container_width=True)

st.subheader('K-Nearest Neighbor - One Hot encoding')
df_presentation_onehot_knn = df_report_onehot_knn.tail(4).reset_index().drop('index',axis=1).rename(columns={'Unnamed: 0':'Metrics'})
st.dataframe(df_presentation_onehot_knn,use_container_width=True)

st.subheader('K-Nearest Neighbor - Label encoding')
df_presentation_label_knn = df_report_label_knn.tail(3).reset_index().drop('index',axis=1).rename(columns={'Unnamed: 0':'Metrics'})
st.dataframe(df_presentation_label_knn,use_container_width=True)

st.subheader('Support Vector Machine - Label encoding')
df_presentation_label_svm = df_report_onehot_svm.tail(3).reset_index().drop('index',axis=1).rename(columns={'Unnamed: 0':'Metrics'})
st.dataframe(df_presentation_label_svm,use_container_width=True)


st.header('Model Deep Neural Network')
st.subheader('Plot Akurasi')
st.image('images/model_akurasi.png')
st.subheader('Plot Loss')
st.image('images/model_loss.png')
st.subheader('Plot Confusion Matrix')
df_confusion_matrix = pd.read_csv('confusion_matrix_dl.csv').rename(columns={'Unnamed: 0':'Class'})
st.dataframe(df_confusion_matrix,use_container_width=True)
