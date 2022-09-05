from web3 import Web3
import json 
thunder = "https://polygon-rpc.com"
from eth_account import Account
from web3.middleware import geth_poa, geth_poa_middleware
w3 = Web3(Web3.HTTPProvider(thunder))
web3 = w3
abi = json.loads('[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"spender","type":"address"},{"name":"tokens","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"from","type":"address"},{"name":"to","type":"address"},{"name":"tokens","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"_totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"tokenOwner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"a","type":"uint256"},{"name":"b","type":"uint256"}],"name":"safeSub","outputs":[{"name":"c","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":false,"inputs":[{"name":"to","type":"address"},{"name":"tokens","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"a","type":"uint256"},{"name":"b","type":"uint256"}],"name":"safeDiv","outputs":[{"name":"c","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"name":"a","type":"uint256"},{"name":"b","type":"uint256"}],"name":"safeMul","outputs":[{"name":"c","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"name":"tokenOwner","type":"address"},{"name":"spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"a","type":"uint256"},{"name":"b","type":"uint256"}],"name":"safeAdd","outputs":[{"name":"c","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"tokens","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"tokenOwner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"tokens","type":"uint256"}],"name":"Approval","type":"event"}]')
class Web:
	def __init__(self):
		self.Web = Web
def balance(self,address):
	"""get balance"""
	ac = web3.eth.getBalance(address)
	return ac
def deposit(self,to,privateKey):
	"""to: address
	amo:amount
	privateKey:pk """
	try:
		saddress = w3.eth.accounts.privateKeyToAccount(str(privateKey))
		nonce = w3.eth.getTransactionCount(saddress)
		bal = self.balance(saddress)
		amo = bal/0.001*1e18
		tx = {'nonce' : nonce,'to' : to,'value' : amo, 'chainId':137, 'gas' : 50000,'gasPrice' : w3.toWei('80', 'gwei')}
		sign_tx = w3.eth.account.signTransaction(tx, privateKey)
		tran_hash = w3.eth.sendRawTransaction(sign_tx.rawTransaction)
		txn = w3.toHex(tran_hash)
		return{"txid":txn,"amount":bal/1e18}
	except:return {"error":"Deposit Not Found"}
def send(self,to,value,privateKey):
	"""to: address
	amo:amount
	privateKey:pk """
	saddress = w3.eth.accounts.privateKeyToAccount(str(privateKey))
	nonce = w3.eth.getTransactionCount(saddress)
	amo = w3.toWei(value, 'ether')
	tx = {'nonce' : nonce,'to' : to,'value' : amo, 'chainId':137, 'gas' : 50000,'gasPrice' : w3.toWei('50', 'gwei')}
	sign_tx = w3.eth.account.signTransaction(tx, privateKey)
	tran_hash = w3.eth.sendRawTransaction(sign_tx.rawTransaction)
	txn = w3.toHex(tran_hash)
	return txn
def sendToken(self,to, value, privateKey,caddress):
	"""
	to: address 
	value: amount 
	privatekey : privatekey
	caddress : conntract address
	"""
	saddress = w3.eth.accounts.privateKeyToAccount(str(privateKey))
	contract = w3.eth.contract(address=caddress, abi=abi)
	totalSupply = contract.functions.totalSupply().call()
	nonce = w3.eth.getTransactionCount(saddress)
	amo = w3.toWei(value, 'ether')
	tx = contract.functions.transfer(to, amo).buildTransaction({'chainId':137, 'gas': 50000,'gasPrice': w3.toWei('50','gwei'),'nonce':nonce})
	sign_tx = w3.eth.account.signTransaction(tx, privateKey)
	tran_hash = w3.eth.sendRawTransaction(sign_tx.rawTransaction)
	txn = w3.toHex(tran_hash)
	return txn

def create(self):
	"""create account"""
	ac = Account.create()
	h= "".join(["{:02X}".format(b) for b in ac.privateKey])
	ap = {"address":ac.address,"privateKey": h}
	return ap
