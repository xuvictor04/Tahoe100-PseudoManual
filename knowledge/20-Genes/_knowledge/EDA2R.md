> [!summary] In one line
> EDA2R, also called XEDAR or TNFRSF27, is an X-linked TNF-receptor-family receptor for the EDA-A2 isoform of ectodysplasin A, one of the most steeply p53-inducible transcripts in the genome, and an emerging marker of muscle wasting and ageing.

## What it is

EDA2R is a membrane receptor of the TNF receptor superfamily, encoded on the X chromosome. It is the receptor for EDA-A2, one of two splice isoforms of ectodysplasin A; a two-amino-acid difference in the ligand determines whether it binds EDAR (EDA-A1) or EDA2R (EDA-A2), one of the cleanest examples of a splice-level switch between two receptors. Unlike most TNFRSF members with cytotoxic activity, EDA2R has no death domain. It couples instead to NF-κB and JNK signalling, and in overexpression systems has been reported to drive caspase-dependent apoptosis. Its developmental role is unexpectedly dispensable: loss of EDAR or of ectodysplasin itself causes hypohidrotic ectodermal dysplasia, but Eda2r-null mice have essentially normal hair, teeth and glands.

What EDA2R is actually known for now is p53. It was identified by cross-referencing p53-introduced cells against tumour tissue, and p53 drives it through two response elements in intron 1 — so this is a direct target, not an inferred one. In colorectal cancer the gene is silenced by promoter hypermethylation at high frequency, and loss of it increases cell adhesion and spreading and confers resistance to p53-induced apoptosis, which is the basis of the proposal that it mediates a p53-regulated anoikis pathway. Independent work confirmed p53-dependent transactivation across several cell types and tissues in vivo, including during chemotherapy-induced hair loss, though EDA2R is not required for that hair loss.

A separate literature has grown recently. EDA2R is among the most consistently age-upregulated transcripts across human and animal tissues, and it is elevated in denervated muscle, cancer cachexia and muscular dystrophy. Work published in 2025 reports that raising it in muscle activates inflammatory signalling and produces sarcopenia-like changes that are relieved on knockdown, putting it forward as both an ageing biomarker and an inflammaging target.

## Why it appears in this work

EDA2R is a high-dynamic-range reporter for [[p53 program P]]. Its baseline in most cancer lines is very low and its p53-driven induction is large, so its fold-change is informative even where absolute counts are small — the opposite trade-off to [[CDKN1A]], and a useful complement to it. Its second life as a muscle-wasting gene is a curious adjacency to [[MG53 (TRIM72)]]'s muscle biology, but adjacency is all it is: here EDA2R is being read as a p53 reporter in pooled cancer lines, not as muscle physiology.

## What is uncertain

The direct-versus-indirect question is settled for the transcription, but whether the protein does anything in these cells is genuinely open: no ligand is supplied in this experiment, EDA-A2 is not appreciably expressed in most cancer lines, and the apoptosis-inducing activity rests largely on overexpression. Induction here may be transcription without signalling. The receptor biology is thin overall — far thinner than the p53-target literature that cites it. The low baseline that makes the fold-change large also makes single-cell detection sparse and ratios unstable. Being X-linked, its dosage may vary with donor sex and X-inactivation state across the pooled lines, a source of between-line variance unrelated to p53. The ageing and cachexia literature is young and largely associational.

## References

- Yan et al., 2000, Science — identified XEDAR/EDA2R as the receptor for the EDA-A2 isoform and showed a two-amino-acid switch in ectodysplasin selects between the two receptors.
- Tanikawa et al., 2009, Oncogene — identified XEDAR as a p53 target driven by two response elements in intron 1, frequently hypermethylated in colorectal cancer, and proposed it mediates p53-regulated anoikis.
- Brosh et al., 2010, FEBS Letters — showed p53-dependent transactivation of EDA2R across cell types and tissues, including in chemotherapy-induced hair loss, which nonetheless does not require EDA2R.
