from fairseq.models.transformer import TransformerModel
import subword_nmt
import warnings
warnings.filterwarnings('ignore')

def translation_task(text):
    hi2bn = TransformerModel.from_pretrained(
                    'checkpoints',
                    checkpoint_file='checkpoint_best.pt',
                    data_name_or_path='data-bin/custom.tokenized.hi-bn',
                    bpe='subword_nmt',
                    bpe_codes='checkpoints/code',
                    beam_size=5
                    )
    return hi2bn.translate(text)

