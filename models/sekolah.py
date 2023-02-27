from odoo import models, fields, api


class Kelas(models.Model):
    _name = 'kelas.kelas'
    _description = ''

    nm_kelas_id = fields.Char(string='Nama Kelas')
    wali_kelas_id = fields.Char(string='Wali Kelas')
    nm_siswa = fields.Char(string='Nama Siswa')
    
    


class Siswa(models.Model):
    _name = 'siswa.siswa'
    
    nis = fields.Integer(string='Nis')
    jenis_kelamin = fields.Char(string='Jenis Kelamin')
    tgl_lahir = fields.Integer(string='Tanggal Lahir')
    agama = fields.Char(string='Agama')
    nm_ayah = fields.Char(string='Nama Ayah')
    nm_ibu = fields.Char(string='Nama Ibu')
    usia = fields.Integer(string='Usia')
    alamat = fields.Char(string='Alamat')
    
    

class Guru(models.Model):
    _name = 'guru.guru'
    
    nip = fields.Integer(string='Nip')
    nm_guru = fields.Char(string='Nama Guru')
    jenis_kelamin = fields.Char(string='Jenis Kelamin')
    mata_pelajaran = fields.Char(string='Mata Pelajaran')
    usia_guru = fields.Integer(string='Usia Guru')
    no_telp = fields.Integer(string='No Telepon')
    alamat = fields.Char(string='Alamat')



class Jadwal(models.Model):
    _name = 'jadwal.jadwal'
    
    hari = fields.Char(string='hari')
    kelas = fields.Char(string='Kelas')
    jam = fields.Integer(string='Jam')
    mata_pelajaran = fields.Char(string='Mata Pelajaran')
        
    
    
class MataPelajaran(models.Model):
    _name = 'mata.pelajaran'
    
    nama_mata_pelajaran = fields.Char(string='Nama Mata Pelajaran')
    jurusan = fields.Char(string='Jurusan')
    
    
    
    
    
    
    
    
    
