import nacl.hash
from enum import Enum

#
# This project contains an implementation of a Digest class with some
# missing functionality. Use the provided Docker container to run the tests
# and see what's currently broken.
#

# Default output length in bits
DEFAULT_OUTPUT_LEN_BITS = 256


class DigestAlgorithm(Enum):
    SHA256 = "sha256"
    BLAKE2B = "blake2b"


class Digest:
    """Class to compute the truncated hash of data"""

    def __init__(
        self,
        algorithm: str,
        output_len_bits: int = DEFAULT_OUTPUT_LEN_BITS,
    ):
        """
        Initializes the Digest class.

        :param output_len_bits: The output length in bits
        :param algorithm: The algorithm to use (see `DigestAlgorithm`)
        """
        assert (output_len_bits > 0)
        assert (output_len_bits % 8 == 0)
        # TODO: add more sanity checks of the input parameters
        self.output_len_bytes = output_len_bits // 8
        self.algorithm = algorithm

    def digest(
        self,
        data: bytes,
    ) -> bytes:
        """
        Computes a diggest of the data using the specified algorithm.
        The result is truncated to the specified output length.

        :param data: The data to compute the digest of
        :return: The truncated digest of the data
        """
        if self.algorithm == DigestAlgorithm.SHA256:
            # TODO: fix the following lines first
            h = nacl.hash.sha256(
                message=data,
                encoder=nacl.encoding.RawEncoder,
            )
            return h
        elif self.algorithm == DigestAlgorithm.BLAKE2B:
            # TODO: Implement BLAKE2
            raise NotImplementedError("BLAKE2 is not implemented")
        else:
            raise ValueError(f"Unsupported algorithm: {self.algorithm}")
