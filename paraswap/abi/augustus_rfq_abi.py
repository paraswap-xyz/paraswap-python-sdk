AUGUSTUS_RFQ_ABI = """
[
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "bytes32",
        "name": "orderHash",
        "type": "bytes32"
      },
      {
        "indexed": true,
        "internalType": "address",
        "name": "maker",
        "type": "address"
      }
    ],
    "name": "OrderCancelled",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "bytes32",
        "name": "orderHash",
        "type": "bytes32"
      },
      {
        "indexed": true,
        "internalType": "address",
        "name": "maker",
        "type": "address"
      },
      {
        "indexed": false,
        "internalType": "address",
        "name": "makerAsset",
        "type": "address"
      },
      {
        "indexed": false,
        "internalType": "uint256",
        "name": "makerAmount",
        "type": "uint256"
      },
      {
        "indexed": true,
        "internalType": "address",
        "name": "taker",
        "type": "address"
      },
      {
        "indexed": false,
        "internalType": "address",
        "name": "takerAsset",
        "type": "address"
      },
      {
        "indexed": false,
        "internalType": "uint256",
        "name": "takerAmount",
        "type": "uint256"
      }
    ],
    "name": "OrderFilled",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "bytes32",
        "name": "orderHash",
        "type": "bytes32"
      },
      {
        "indexed": true,
        "internalType": "address",
        "name": "maker",
        "type": "address"
      },
      {
        "indexed": false,
        "internalType": "uint256",
        "name": "makerAsset",
        "type": "uint256"
      },
      {
        "indexed": false,
        "internalType": "uint256",
        "name": "makerAssetId",
        "type": "uint256"
      },
      {
        "indexed": false,
        "internalType": "uint256",
        "name": "makerAmount",
        "type": "uint256"
      },
      {
        "indexed": true,
        "internalType": "address",
        "name": "taker",
        "type": "address"
      },
      {
        "indexed": false,
        "internalType": "uint256",
        "name": "takerAsset",
        "type": "uint256"
      },
      {
        "indexed": false,
        "internalType": "uint256",
        "name": "takerAssetId",
        "type": "uint256"
      },
      {
        "indexed": false,
        "internalType": "uint256",
        "name": "takerAmount",
        "type": "uint256"
      }
    ],
    "name": "OrderFilledNFT",
    "type": "event"
  },
  {
    "inputs": [],
    "name": "FILLED_ORDER",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "RFQ_LIMIT_NFT_ORDER_TYPEHASH",
    "outputs": [
      {
        "internalType": "bytes32",
        "name": "",
        "type": "bytes32"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "RFQ_LIMIT_ORDER_TYPEHASH",
    "outputs": [
      {
        "internalType": "bytes32",
        "name": "",
        "type": "bytes32"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "UNFILLED_ORDER",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "components": [
          {
            "components": [
              {
                "internalType": "uint256",
                "name": "nonceAndMeta",
                "type": "uint256"
              },
              {
                "internalType": "uint128",
                "name": "expiry",
                "type": "uint128"
              },
              {
                "internalType": "address",
                "name": "makerAsset",
                "type": "address"
              },
              {
                "internalType": "address",
                "name": "takerAsset",
                "type": "address"
              },
              {
                "internalType": "address",
                "name": "maker",
                "type": "address"
              },
              {
                "internalType": "address",
                "name": "taker",
                "type": "address"
              },
              {
                "internalType": "uint256",
                "name": "makerAmount",
                "type": "uint256"
              },
              {
                "internalType": "uint256",
                "name": "takerAmount",
                "type": "uint256"
              }
            ],
            "internalType": "struct AugustusRFQ.Order",
            "name": "order",
            "type": "tuple"
          },
          {
            "internalType": "bytes",
            "name": "signature",
            "type": "bytes"
          },
          {
            "internalType": "uint256",
            "name": "takerTokenFillAmount",
            "type": "uint256"
          },
          {
            "internalType": "bytes",
            "name": "permitTakerAsset",
            "type": "bytes"
          },
          {
            "internalType": "bytes",
            "name": "permitMakerAsset",
            "type": "bytes"
          }
        ],
        "internalType": "struct AugustusRFQ.OrderInfo[]",
        "name": "orderInfos",
        "type": "tuple[]"
      },
      {
        "internalType": "address",
        "name": "target",
        "type": "address"
      }
    ],
    "name": "batchFillOrderWithTarget",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "components": [
          {
            "components": [
              {
                "internalType": "uint256",
                "name": "nonceAndMeta",
                "type": "uint256"
              },
              {
                "internalType": "uint128",
                "name": "expiry",
                "type": "uint128"
              },
              {
                "internalType": "uint256",
                "name": "makerAsset",
                "type": "uint256"
              },
              {
                "internalType": "uint256",
                "name": "makerAssetId",
                "type": "uint256"
              },
              {
                "internalType": "uint256",
                "name": "takerAsset",
                "type": "uint256"
              },
              {
                "internalType": "uint256",
                "name": "takerAssetId",
                "type": "uint256"
              },
              {
                "internalType": "address",
                "name": "maker",
                "type": "address"
              },
              {
                "internalType": "address",
                "name": "taker",
                "type": "address"
              },
              {
                "internalType": "uint256",
                "name": "makerAmount",
                "type": "uint256"
              },
              {
                "internalType": "uint256",
                "name": "takerAmount",
                "type": "uint256"
              }
            ],
            "internalType": "struct AugustusRFQ.OrderNFT",
            "name": "order",
            "type": "tuple"
          },
          {
            "internalType": "bytes",
            "name": "signature",
            "type": "bytes"
          },
          {
            "internalType": "uint256",
            "name": "takerTokenFillAmount",
            "type": "uint256"
          },
          {
            "internalType": "bytes",
            "name": "permitTakerAsset",
            "type": "bytes"
          },
          {
            "internalType": "bytes",
            "name": "permitMakerAsset",
            "type": "bytes"
          }
        ],
        "internalType": "struct AugustusRFQ.OrderNFTInfo[]",
        "name": "orderInfos",
        "type": "tuple[]"
      },
      {
        "internalType": "address",
        "name": "target",
        "type": "address"
      }
    ],
    "name": "batchFillOrderWithTargetNFT",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "bytes32",
        "name": "orderHash",
        "type": "bytes32"
      }
    ],
    "name": "cancelOrder",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "bytes32[]",
        "name": "orderHashes",
        "type": "bytes32[]"
      }
    ],
    "name": "cancelOrders",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "components": [
          {
            "internalType": "uint256",
            "name": "nonceAndMeta",
            "type": "uint256"
          },
          {
            "internalType": "uint128",
            "name": "expiry",
            "type": "uint128"
          },
          {
            "internalType": "address",
            "name": "makerAsset",
            "type": "address"
          },
          {
            "internalType": "address",
            "name": "takerAsset",
            "type": "address"
          },
          {
            "internalType": "address",
            "name": "maker",
            "type": "address"
          },
          {
            "internalType": "address",
            "name": "taker",
            "type": "address"
          },
          {
            "internalType": "uint256",
            "name": "makerAmount",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "takerAmount",
            "type": "uint256"
          }
        ],
        "internalType": "struct AugustusRFQ.Order",
        "name": "order",
        "type": "tuple"
      },
      {
        "internalType": "bytes",
        "name": "signature",
        "type": "bytes"
      }
    ],
    "name": "fillOrder",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "components": [
          {
            "internalType": "uint256",
            "name": "nonceAndMeta",
            "type": "uint256"
          },
          {
            "internalType": "uint128",
            "name": "expiry",
            "type": "uint128"
          },
          {
            "internalType": "uint256",
            "name": "makerAsset",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "makerAssetId",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "takerAsset",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "takerAssetId",
            "type": "uint256"
          },
          {
            "internalType": "address",
            "name": "maker",
            "type": "address"
          },
          {
            "internalType": "address",
            "name": "taker",
            "type": "address"
          },
          {
            "internalType": "uint256",
            "name": "makerAmount",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "takerAmount",
            "type": "uint256"
          }
        ],
        "internalType": "struct AugustusRFQ.OrderNFT",
        "name": "order",
        "type": "tuple"
      },
      {
        "internalType": "bytes",
        "name": "signature",
        "type": "bytes"
      }
    ],
    "name": "fillOrderNFT",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "components": [
          {
            "internalType": "uint256",
            "name": "nonceAndMeta",
            "type": "uint256"
          },
          {
            "internalType": "uint128",
            "name": "expiry",
            "type": "uint128"
          },
          {
            "internalType": "address",
            "name": "makerAsset",
            "type": "address"
          },
          {
            "internalType": "address",
            "name": "takerAsset",
            "type": "address"
          },
          {
            "internalType": "address",
            "name": "maker",
            "type": "address"
          },
          {
            "internalType": "address",
            "name": "taker",
            "type": "address"
          },
          {
            "internalType": "uint256",
            "name": "makerAmount",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "takerAmount",
            "type": "uint256"
          }
        ],
        "internalType": "struct AugustusRFQ.Order",
        "name": "order",
        "type": "tuple"
      },
      {
        "internalType": "bytes",
        "name": "signature",
        "type": "bytes"
      },
      {
        "internalType": "address",
        "name": "target",
        "type": "address"
      }
    ],
    "name": "fillOrderWithTarget",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "components": [
          {
            "internalType": "uint256",
            "name": "nonceAndMeta",
            "type": "uint256"
          },
          {
            "internalType": "uint128",
            "name": "expiry",
            "type": "uint128"
          },
          {
            "internalType": "uint256",
            "name": "makerAsset",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "makerAssetId",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "takerAsset",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "takerAssetId",
            "type": "uint256"
          },
          {
            "internalType": "address",
            "name": "maker",
            "type": "address"
          },
          {
            "internalType": "address",
            "name": "taker",
            "type": "address"
          },
          {
            "internalType": "uint256",
            "name": "makerAmount",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "takerAmount",
            "type": "uint256"
          }
        ],
        "internalType": "struct AugustusRFQ.OrderNFT",
        "name": "order",
        "type": "tuple"
      },
      {
        "internalType": "bytes",
        "name": "signature",
        "type": "bytes"
      },
      {
        "internalType": "address",
        "name": "target",
        "type": "address"
      }
    ],
    "name": "fillOrderWithTargetNFT",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "maker",
        "type": "address"
      },
      {
        "internalType": "bytes32[]",
        "name": "orderHashes",
        "type": "bytes32[]"
      }
    ],
    "name": "getRemainingOrderBalance",
    "outputs": [
      {
        "internalType": "uint256[]",
        "name": "remainingBalances",
        "type": "uint256[]"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "components": [
          {
            "internalType": "uint256",
            "name": "nonceAndMeta",
            "type": "uint256"
          },
          {
            "internalType": "uint128",
            "name": "expiry",
            "type": "uint128"
          },
          {
            "internalType": "address",
            "name": "makerAsset",
            "type": "address"
          },
          {
            "internalType": "address",
            "name": "takerAsset",
            "type": "address"
          },
          {
            "internalType": "address",
            "name": "maker",
            "type": "address"
          },
          {
            "internalType": "address",
            "name": "taker",
            "type": "address"
          },
          {
            "internalType": "uint256",
            "name": "makerAmount",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "takerAmount",
            "type": "uint256"
          }
        ],
        "internalType": "struct AugustusRFQ.Order",
        "name": "order",
        "type": "tuple"
      },
      {
        "internalType": "bytes",
        "name": "signature",
        "type": "bytes"
      },
      {
        "internalType": "uint256",
        "name": "takerTokenFillAmount",
        "type": "uint256"
      }
    ],
    "name": "partialFillOrder",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "makerTokenFilledAmount",
        "type": "uint256"
      }
    ],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "components": [
          {
            "internalType": "uint256",
            "name": "nonceAndMeta",
            "type": "uint256"
          },
          {
            "internalType": "uint128",
            "name": "expiry",
            "type": "uint128"
          },
          {
            "internalType": "uint256",
            "name": "makerAsset",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "makerAssetId",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "takerAsset",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "takerAssetId",
            "type": "uint256"
          },
          {
            "internalType": "address",
            "name": "maker",
            "type": "address"
          },
          {
            "internalType": "address",
            "name": "taker",
            "type": "address"
          },
          {
            "internalType": "uint256",
            "name": "makerAmount",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "takerAmount",
            "type": "uint256"
          }
        ],
        "internalType": "struct AugustusRFQ.OrderNFT",
        "name": "order",
        "type": "tuple"
      },
      {
        "internalType": "bytes",
        "name": "signature",
        "type": "bytes"
      },
      {
        "internalType": "uint256",
        "name": "takerTokenFillAmount",
        "type": "uint256"
      }
    ],
    "name": "partialFillOrderNFT",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "makerTokenFilledAmount",
        "type": "uint256"
      }
    ],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "components": [
          {
            "internalType": "uint256",
            "name": "nonceAndMeta",
            "type": "uint256"
          },
          {
            "internalType": "uint128",
            "name": "expiry",
            "type": "uint128"
          },
          {
            "internalType": "address",
            "name": "makerAsset",
            "type": "address"
          },
          {
            "internalType": "address",
            "name": "takerAsset",
            "type": "address"
          },
          {
            "internalType": "address",
            "name": "maker",
            "type": "address"
          },
          {
            "internalType": "address",
            "name": "taker",
            "type": "address"
          },
          {
            "internalType": "uint256",
            "name": "makerAmount",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "takerAmount",
            "type": "uint256"
          }
        ],
        "internalType": "struct AugustusRFQ.Order",
        "name": "order",
        "type": "tuple"
      },
      {
        "internalType": "bytes",
        "name": "signature",
        "type": "bytes"
      },
      {
        "internalType": "uint256",
        "name": "takerTokenFillAmount",
        "type": "uint256"
      },
      {
        "internalType": "address",
        "name": "target",
        "type": "address"
      }
    ],
    "name": "partialFillOrderWithTarget",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "makerTokenFilledAmount",
        "type": "uint256"
      }
    ],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "components": [
          {
            "internalType": "uint256",
            "name": "nonceAndMeta",
            "type": "uint256"
          },
          {
            "internalType": "uint128",
            "name": "expiry",
            "type": "uint128"
          },
          {
            "internalType": "uint256",
            "name": "makerAsset",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "makerAssetId",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "takerAsset",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "takerAssetId",
            "type": "uint256"
          },
          {
            "internalType": "address",
            "name": "maker",
            "type": "address"
          },
          {
            "internalType": "address",
            "name": "taker",
            "type": "address"
          },
          {
            "internalType": "uint256",
            "name": "makerAmount",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "takerAmount",
            "type": "uint256"
          }
        ],
        "internalType": "struct AugustusRFQ.OrderNFT",
        "name": "order",
        "type": "tuple"
      },
      {
        "internalType": "bytes",
        "name": "signature",
        "type": "bytes"
      },
      {
        "internalType": "uint256",
        "name": "takerTokenFillAmount",
        "type": "uint256"
      },
      {
        "internalType": "address",
        "name": "target",
        "type": "address"
      }
    ],
    "name": "partialFillOrderWithTargetNFT",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "makerTokenFilledAmount",
        "type": "uint256"
      }
    ],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "components": [
          {
            "internalType": "uint256",
            "name": "nonceAndMeta",
            "type": "uint256"
          },
          {
            "internalType": "uint128",
            "name": "expiry",
            "type": "uint128"
          },
          {
            "internalType": "address",
            "name": "makerAsset",
            "type": "address"
          },
          {
            "internalType": "address",
            "name": "takerAsset",
            "type": "address"
          },
          {
            "internalType": "address",
            "name": "maker",
            "type": "address"
          },
          {
            "internalType": "address",
            "name": "taker",
            "type": "address"
          },
          {
            "internalType": "uint256",
            "name": "makerAmount",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "takerAmount",
            "type": "uint256"
          }
        ],
        "internalType": "struct AugustusRFQ.Order",
        "name": "order",
        "type": "tuple"
      },
      {
        "internalType": "bytes",
        "name": "signature",
        "type": "bytes"
      },
      {
        "internalType": "uint256",
        "name": "takerTokenFillAmount",
        "type": "uint256"
      },
      {
        "internalType": "address",
        "name": "target",
        "type": "address"
      },
      {
        "internalType": "bytes",
        "name": "permitTakerAsset",
        "type": "bytes"
      },
      {
        "internalType": "bytes",
        "name": "permitMakerAsset",
        "type": "bytes"
      }
    ],
    "name": "partialFillOrderWithTargetPermit",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "makerTokenFilledAmount",
        "type": "uint256"
      }
    ],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "components": [
          {
            "internalType": "uint256",
            "name": "nonceAndMeta",
            "type": "uint256"
          },
          {
            "internalType": "uint128",
            "name": "expiry",
            "type": "uint128"
          },
          {
            "internalType": "uint256",
            "name": "makerAsset",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "makerAssetId",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "takerAsset",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "takerAssetId",
            "type": "uint256"
          },
          {
            "internalType": "address",
            "name": "maker",
            "type": "address"
          },
          {
            "internalType": "address",
            "name": "taker",
            "type": "address"
          },
          {
            "internalType": "uint256",
            "name": "makerAmount",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "takerAmount",
            "type": "uint256"
          }
        ],
        "internalType": "struct AugustusRFQ.OrderNFT",
        "name": "order",
        "type": "tuple"
      },
      {
        "internalType": "bytes",
        "name": "signature",
        "type": "bytes"
      },
      {
        "internalType": "uint256",
        "name": "takerTokenFillAmount",
        "type": "uint256"
      },
      {
        "internalType": "address",
        "name": "target",
        "type": "address"
      },
      {
        "internalType": "bytes",
        "name": "permitTakerAsset",
        "type": "bytes"
      },
      {
        "internalType": "bytes",
        "name": "permitMakerAsset",
        "type": "bytes"
      }
    ],
    "name": "partialFillOrderWithTargetPermitNFT",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "makerTokenFilledAmount",
        "type": "uint256"
      }
    ],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      },
      {
        "internalType": "bytes32",
        "name": "",
        "type": "bytes32"
      }
    ],
    "name": "remaining",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  }
]
"""
