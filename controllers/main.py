from odoo import http
from odoo.http import request
from odoo.addons.web.controllers.main import content_disposition #,serialize_exception
import base64
import logging
logger = logging.getLogger(__name__)

class pendaftaran(http.Controller):
    @http.route('/pendaftaran', type='http', auth='public', website=True)
    def pasar(self , **kw):
        propinsi = request.env['simpasar.propinsi'].sudo().search([('name','=ilike','Jawa Timur')])
        kota = request.env['simpasar.kota'].sudo().search([('propinsi_id','in',propinsi.mapped('id'))])
        kota_lahir = request.env['simpasar.kota'].sudo().search([])
        kecamatan = request.env['simpasar.kecamatan'].sudo().search([('kota_id','in',kota.mapped('id'))])
        desa = request.env['simpasar.desa'].sudo().search([])
        jenis_jualan = request.env['simpasar.jenis.jualan'].sudo().search([])
        pasar = request.env['simpasar.pasar'].sudo().search([])
        #  print(propinsi)
        return  request.render('pasar.pendaftaran', {
            'propinsi' : propinsi,
            'kota' : kota,
            'kecamatan' : kecamatan,
            'jenis_jualan' : jenis_jualan,
            'pasar' : pasar,
            'desa'  : desa,
            'kota_lahir' : kota_lahir
        })

    @http.route('/create/pendaftaran', type='http', auth='public', website=True)
    def create_pendaftaran(self , **kw):
        image_ktp = kw.get('foto_ktp', False)
        image_kk = kw.get('foto_kk', False)
        pas_foto = kw.get('pas_foto', False)

        pedagang = request.env['simpasar.cln_pedagang'].sudo().create({
            'nama': kw.get('nama'),
            'nik': kw.get('nik'),
            'nomor_kk': kw.get('nomer_kk'),
            'jenis_kelamin': kw.get('jenis_kelamin'),
            'ktp_alamat': kw.get('ktp_alamat'),
            # 'ktp_rt_rw': kw.get('ktp_rt_rw'),
            # 'ktp_propinsi_id': kw.get('ktp_propinsi_id'),
            # 'ktp_kota_id': kw.get('ktp_kota_id'),
            # 'ktp_kecamatan_id': kw.get('ktp_kecamatan_id'),
            # 'ktp_desa_id': kw.get('ktp_desa_id'),
            'phone': kw.get('phone'),
            'mobile': kw.get('mobile'),
            'email': kw.get('email'),
            'tg_sesuai_ktp': kw.get('tg_sesuai_ktp'),
            'jenis_jualan_id': kw.get('jenis_jualan'),
            'ket_jualan': kw.get('ket_jualan'),
            'tg_street': kw.get('tg_street'),
            # 'tg_street2': kw.get('tg_street2'),
            # 'tg_propinsi_id': kw.get('tg_propinsi_id'),
            # 'tg_kota_id': kw.get('tg_kota_id'),
            # 'tg_kecamatan_id': kw.get('tg_kecamatan_id'),
            # 'tg_desa_id': kw.get('tg_desa_id'),
            'pasar_id': kw.get('pasar'),
            'foto_ktp': base64.encodebytes(image_ktp.read()) if image_ktp else False,
            'foto_kk': base64.encodebytes(image_kk.read()) if image_kk else False,
            'pas_foto': base64.encodebytes(pas_foto.read()) if pas_foto else False,
            'pekerjaan' : kw.get('pekerjaan'),
            'tmp_lahir' : kw.get('tg_kota_lahir'),
            'tgl_lahir' : kw.get('tanggal_lahir'),
        })
        vals = {
            'pedagang': pedagang,
        }
        return  request.render('pasar.peringatan', vals)

    @http.route('/pembaruan/<string:uuid>', type='http', auth='public', website=True)
    def pembaruan(self, uuid, **kw):
        data = request.env['simpasar.pendaftaran'].sudo().search([('uuid','=', uuid),('state','=','tolak')])
        propinsi = request.env['simpasar.propinsi'].sudo().search([('name','=ilike','Jawa Timur')])
        kota = request.env['simpasar.kota'].sudo().search([('propinsi_id','in',propinsi.mapped('id'))])
        kota_lahir = request.env['simpasar.kota'].sudo().search([])
        kecamatan = request.env['simpasar.kecamatan'].sudo().search([('kota_id','in',kota.mapped('id'))])
        desa = request.env['simpasar.desa'].sudo().search([])
        jenis_jualan = request.env['simpasar.jenis.jualan'].sudo().search([])
        pasar = request.env['simpasar.pasar'].sudo().search([])
        #  print(propinsi)
        if data :
            return request.render('pasar.pembaruan', {
                'alasan': data.verifikasi_notes,
                'uuid' : data.uuid,
                'data' : data.cln_pedagang_id,
                'propinsi' : propinsi,
                'kota' : kota,
                'kecamatan' : kecamatan,
                'jenis_jualan' : jenis_jualan,
                'pasar' : pasar,
                'desa'  : desa,
                'kota_lahir' : kota_lahir,
                'tg_street': data.cln_pedagang_id.tg_street if data.cln_pedagang_id.tg_sesuai_ktp == '0' else data.cln_pedagang_id.ktp_alamat,
                'tg_street2': data.cln_pedagang_id.tg_street2 if data.cln_pedagang_id.tg_sesuai_ktp == '0' else data.cln_pedagang_id.ktp_rt_rw,
                'tg_propinsi_id': data.cln_pedagang_id.tg_propinsi_id if data.cln_pedagang_id.tg_sesuai_ktp == '0' else data.cln_pedagang_id.ktp_propinsi_id,
                'tg_kota_id': data.cln_pedagang_id.tg_kota_id if data.cln_pedagang_id.tg_sesuai_ktp == '0' else data.cln_pedagang_id.ktp_kota_id,
                'tg_kecamatan_id': data.cln_pedagang_id.tg_kecamatan_id if data.cln_pedagang_id.tg_sesuai_ktp == '0' else data.cln_pedagang_id.ktp_kecamatan_id,
                'tg_desa_id': data.cln_pedagang_id.tg_desa_id if data.cln_pedagang_id.tg_sesuai_ktp == '0' else data.cln_pedagang_id.ktp_desa_id,
            })
        return request.render('http_routing.404',False)


    @http.route('/update/pendaftaran', type='http', website=True)
    def update(self, **kw):
        data_pendaftaran = request.env['simpasar.pendaftaran'].sudo().search([('uuid','=', kw.get('uuid')),('state','=','tolak')])
        data = {}
        for _,v in enumerate(kw):
            if kw[v] and v != "uuid":
                data[v] = kw[v]
        data['state'] = "sudah_direvisi"
        data_pendaftaran.cln_pedagang_id.write(data)
        return  request.render('pasar.peringatan', {})

class home(http.Controller):
    @http.route('/', type='http', auth='public', website=True)
    def home(self , **kw):
        return  request.render('pasar.home')

class denah(http.Controller):
    @http.route('/denah', type='http', auth='public', website=True)
    def denah(self , **kw):
        data_denah = request.env['simpasar.pasar'].sudo().search([])
        ress = []
        data_kosong = []
        for key,value in enumerate(data_denah):
            data_kosong.append(value)
            if key % 2:
                ress.append(data_kosong)
                data_kosong = []
        return  request.render('pasar.denah',{'data':ress})
