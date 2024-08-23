// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";



contract PaidMintNFT is ERC721, Ownable {
    IERC20 public acceptedToken;
    uint256 public mintPrice;
    uint256 public nextTokenId;

    constructor(
        string memory name,
        string memory symbol,
        address tokenAddress,
        uint256 price
    ) ERC721(name, symbol) {
        acceptedToken = IERC20(tokenAddress);
        mintPrice = price;
    }

    function mint() external {
        require(
            acceptedToken.transferFrom(msg.sender, address(this), mintPrice),
            "Payment failed"
        );

        _safeMint(msg.sender, nextTokenId);
        nextTokenId++;
    }

    function withdrawTokens() external onlyOwner {
        uint256 balance = acceptedToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        acceptedToken.transfer(owner(), balance);
    }

    function setMintPrice(uint256 price) external onlyOwner {
        mintPrice = price;
    }
}
