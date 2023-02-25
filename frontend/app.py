from flask import Flask, request, jsonify, render_template, request, redirect, url_for
from algosdk.v2client import algod
from algosdk import mnemonic, transaction, encoding, name
# from algosdk.future import transaction as futuretxn
from pyteal import *

app = Flask(__name__)
algod_client = algod.AlgodClient('<algod-token>', '<algod-address>')  # Replace with your own Algod credentials
#
# mnemonic_secret = '<your-mnemonic>'
# mnemonic_phrase = mnemonic.from_private_key(encoding.decode_private_key(mnemonic_secret))
# account_address = mnemonic.to_public_key(mnemonic_phrase)
account_address = '1'

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<page>')
def display_page(page):
    return render_template(f'{page}.html')


@app.route('/search', methods=['GET'])
def search_domain():
    domain_name = request.args.get('domain_name')

    domain_info = get_domain_info(domain_name)
    text_record = get_text_record(domain_name)
    domain_owner = get_domain_owner(domain_name)

    return render_template('search.html', domain_name=domain_name,
                           domain_info=domain_info, text_record=text_record,
                           domain_owner=domain_owner)


def get_domain_info(domain_name):
    # try:
    #     local_state = algod_client.account_info(account_address)['apps-local-state'][0]['key-value']
    # except (KeyError, IndexError):
    #     return jsonify({'error': 'No names registered'}), 404
    # names = []
    # for item in local_state:
    #     if item['key'] == f'info:{domain_name}'.encode('utf-8'):
    #         return {'ip': item['value']['bytes'].decode('utf-8')}
    return 'TestIP'


def get_text_record(domain_name):
    # if not domain_name:
    #     return jsonify({'error': 'Missing required parameter(s)'}), 400
    # try:
    #     local_state = algod_client.account_info(account_address)['apps-local-state'][0]['key-value']
    # except (KeyError, IndexError):
    #     return jsonify({'error': 'No names registered'}), 404
    # for item in local_state:
    #     if item['key'] == f'text:{domain_name}'.encode('utf-8'):
    #         text_record = item['value']['bytes']
    #         return jsonify({'text_record': text_record.decode('utf-8')})
    return 'TestTextRecord'


def get_domain_owner(domain_name):
    # try:
    #     local_state = algod_client.account_info(account_address)['apps-local-state'][0]['key-value']
    # except (KeyError, IndexError):
    #     return {'error': 'No names registered'}
    # for item in local_state:
    #     if item['key'] == f'owner:{domain_name}'.encode('utf-8'):
    #         return {'owner': item['value']['bytes'].decode('utf-8')}
    return 'Test Domain owner'


@app.route('/addressinfo', methods=['GET'])
# def get_address_info():
#   account_address = request.args.get('account_address')
#   default_domain = get_default_domain(account_address)
#   asso_domains = get_asso_domains(account_address)
#   return default_domain
# #
#
def get_address_info():
  account_address = request.args.get('account_address')
  default_domain = get_default_domain(account_address)
  asso_domains = get_asso_domains(account_address)
  return render_template('search.html', account_address=account_address,
                         asso_domains=asso_domains,
                         default_domain=default_domain)

def get_default_domain(account_address):
    # try:
    #     local_state = algod_client.account_info(account_address)['apps-local-state'][0]['key-value']
    # except (KeyError, IndexError):
    #     return jsonify({'error': 'No default domain registered'}), 404
    # for item in local_state:
    #     if item['key'] == b'default_domain':
    #         default_domain = item['value']['bytes'].decode('utf-8')
    #     return jsonify({'default_domain': default_domain})
    return 'TestDomain'


def get_asso_domains(account_address):
    # try:
    #     local_state = algod_client.account_info(account_address)['apps-local-state'][0]['key-value']
    # except (KeyError, IndexError):
    #     return jsonify({'error': 'No default domain registered'}), 404
    # for item in local_state:
    #     if item['key'] == b'default_domain':
    #         default_domain = item['value']['bytes'].decode('utf-8')
    return ('AABB','CCDD')


@app.route('/register', methods=['GET'])
def register_status():
    register_name = request.json.get('register_name')
    register_address = request.json.get('register_address')
    register_duration = request.json.get('register_duration')
    reg_status = register_name(register_name, register_address, register_duration)
    return render_template('manage.html', reg_status=reg_status)


def register_name(register_name, register_address, register_duration):
    if not register_name or not register_address or not register_duration:
        return jsonify({'error': 'Missing required parameter(s)'}), 400
    # if not encoding.is_valid_address(register_address):
    #     return jsonify({'error': 'Invalid Algorand address'}), 400
    #
    # program = Seq([
    #     App.localPut(Int(0), Bytes("owner"), Txn.sender()),
    #     App.localPut(Int(0), Bytes("address"), Bytes(address)),
    #     App.localPut(Int(0), Bytes("duration"), Int(duration)),
    #     Return(Int(1))
    # ])
    # teal_code = program.teal()
    # compiled = algod_client.compile(teal_code)
    # txn = transaction.Transaction(
    #     sender=account_address,
    #     fee=algod_client.suggested_params()['fee'],
    #     first=algod_client.suggested_params()['last'],
    #     last=algod_client.suggested_params()['last'] + 1000,
    #     gh=algod_client.suggested_params()['genesis_hash'],
    #     **compiled)
    # signed_txn = txn.sign(mnemonic_secret)
    # tx_id = algod_client.send_transaction(signed_txn)
    return 'Registration Completed.'
        # jsonify({'success': True, 'tx_id': tx_id})


@app.route('/renew', methods=['POST'])
def renew_status():
    renew_name = request.json.get('renew_name')
    renew_address = request.json.get('renew_address')
    renew_duration = request.json.get('renew_duration')
    renew_status = renew_name(renew_name, renew_address, renew_duration)
    return render_template('manage.html', renew_status=renew_status)


def renew_name(renew_name, renew_address, renew_duration):
    # if not renew_name or not renew_address or not renew_duration:
    #     return jsonify({'error': 'Missing required parameter(s)'}), 400
    #
    # program = Seq([
    #     App.localPut(Int(0), Bytes("duration"), Int(duration)),
    #     Return(Int(1))
    # ])
    # teal_code = program.teal()
    # compiled = algod_client.compile(teal_code)
    # txn = futuretxn.Transaction(
    #     sender=account_address,
    #     fee=algod_client.suggested_params()['fee'],
    #     first=algod_client.suggested_params()['last'],
    #     last=algod_client.suggested_params()['last'] + 1000,
    #     gh=algod_client.suggested_params()['genesis_hash'],
    #     **compiled)
    # signed_txn = txn.sign(mnemonic_secret)
    # tx_id = algod_client.send_transaction(signed_txn)
    return 'Renew Completed.'
        # jsonify({'success': True, 'tx_id': tx_id})


@app.route('/update', methods=['POST'])
def update_status():
    update_old_name = request.json.get('update_old_name')
    update_new_name = request.json.get('update_new_name')
    update_address = request.json.get('update_address')
    update_duration = request.json.get('renew_duration')
    update_status = update_name(update_old_name, update_new_name,
                                update_address, update_duration)
    return render_template('manage.html', update_status=update_status)


def update_name(update_old_name, update_new_name, update_address, update_duration):
    if not update_old_name or not update_new_name or not update_address or not update_duration:
        return jsonify({'error': 'Missing required parameter(s)'}), 400
    # if not encoding.is_valid_address(update_address):
    #     return jsonify({'error': 'Invalid Algorand address'}),
    #
    # program = Seq([
    #     App.localPut(Int(0), Bytes("address"), Bytes(address)),
    #     Return(Int(1))
    # ])
    # teal_code = program.teal()
    # compiled = algod_client.compile(teal_code)
    # txn = futuretxn.Transaction(
    #     sender=account_address,
    #     fee=algod_client.suggested_params()['fee'],
    #     first=algod_client.suggested_params()['last'],
    #     last=algod_client.suggested_params()['last'] + 1000,
    #     gh=algod_client.suggested_params()['genesis_hash'],
    #     **compiled)
    # signed_txn = txn.sign(mnemonic_secret)
    # tx_id = algod_client.send_transaction(signed_txn)
    return 'Update Completes.'
        # jsonify({'success': True, 'tx_id': tx_id})


if name == 'main':
    app.run(debug=True)



