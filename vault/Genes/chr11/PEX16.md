---
symbol: "PEX16"
type: "gene"
col: 4286
ensembl_id: "ENSG00000121680"
name: "peroxisomal biogenesis factor 16"
location: "11p11.2"
module: 107
arm: "+"
pooled_cpm: 7.02
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 6
n_dd_up_clean: 10
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/107"]
generated_by: "tahoemap"
---

# PEX16

*peroxisomal biogenesis factor 16* — 11p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.12× (z +9.4, q 2e-18, up in 36 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.638× (z -5.7, q 8e-06, down in 20 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM208]] (+0.70, fdr 1e-05), [[ZNF581]] (+0.70, fdr 7e-06), [[ACOX3]] (+0.67, fdr 7e-06); moves opposite to [[ECT2]] (-0.64, fdr 7e-06), [[EPB41L2]] (-0.62, fdr 1e-05), [[TMEM123]] (-0.60, fdr 1e-05).
> It is in [[Module 107]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4286.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.12×** | +9.4 | 2e-18 | 36/46 (Panc 03.27, A498, …) | two highest doses | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.03×** | +8.9 | 2e-16 | 37/47 (LoVo, SW480, …) | two highest doses | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.82×** | +7.5 | 1e-11 | 29/47 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.71×** | +6.5 | 1e-08 | 21/32 (KATO III, PANC-1, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +6.4 | 2e-08 | 21/42 (MIA PaCa-2, A549, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.43×** | +4.5 | 6e-04 | 7/47 (C32, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.41×** | +4.3 | 0.001 | 11/45 (HEC-1-A, HT-29, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.39×** | +3.9 | 0.007 | 14/43 (PANC-1, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.37×** | +3.8 | 0.010 | 11/40 (SNU-423, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.55×** | +3.7 | 0.011 | 4/44 (Hs 766T, COLO 205, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.34×** | +3.7 | 0.011 | 11/45 (NCI-H23, HEC-1-A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **1.31×** | +3.2 | 0.062 | 2/12 (J82, SW480) | rises with dose | composition shift; position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **1.60×** | +3.1 | 0.092 | 5/34 (A-427, KATO III, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4286.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.638×** | -5.7 | 8e-06 | 20/47 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.660×** | -5.3 | 4e-05 | 18/46 (LoVo, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.801×** | -4.0 | 0.011 | 9/46 (Hs 766T, RKO, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.731×** | -4.0 | 0.011 | 13/41 (NCI-H2030, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.760×** | -3.3 | 0.093 | 12/41 (NCI-H2030, SNU-423, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.771×** | -3.3 | 0.093 | 14/46 (LoVo, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.760× | -3.2 | 0.10 | 5/47 (CHP-212, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4286. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 4.08 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0729× (z -10.0) ⚠ toxic |
| [[HS-578T (line)]] | alt | 6.59 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0866× (z -14.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 5.70 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.115× (z -10.4) |
| [[A-172 (line)]] | wt | 7.59 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.58 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.28 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.81 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.72 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.91 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.85 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.45 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.52 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.42 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.38 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.21 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.42 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.44 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.77 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.12 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.96 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.56 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.77 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.44 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.12 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.79 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4286), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM208]] | +0.70 | +0.55 / +0.71 | both halves | 1e-05 | pathway: Protein localization |
| [[ZNF581]] | +0.70 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[ACOX3]] | +0.67 | +0.62 / +0.62 | both halves | 7e-06 | pathway: Protein localization; STRING 440 |
| [[MRPL55]] | +0.65 | +0.43 / +0.70 | both halves | 3e-05 |  |
| [[C18orf21]] | +0.64 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[JOSD2]] | +0.63 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[ZFAND2A]] | +0.63 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[TRADD]] | +0.63 | +0.41 / +0.66 | both halves | 4e-05 |  |
| [[ADPRM]] | +0.63 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[TRAPPC2B]] | +0.62 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[SIRT7]] | +0.62 | +0.41 / +0.64 | both halves | 4e-05 |  |
| [[C16orf91]] | +0.62 | +0.52 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ECT2]] | -0.64 | -0.64 / -0.63 | both halves | 7e-06 |  |
| [[EPB41L2]] | -0.62 | -0.54 / -0.66 | both halves | 1e-05 |  |
| [[TMEM123]] | -0.60 | -0.54 / -0.61 | both halves | 1e-05 |  |
| [[SEPTIN11]] | -0.60 | -0.41 / -0.60 | both halves | 4e-05 |  |
| [[TMSB4X]] | -0.60 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[CBX5]] | -0.60 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[TMPO]] | -0.60 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[CALM2]] | -0.58 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[GNG12]] | -0.58 | -0.44 / -0.64 | both halves | 3e-05 |  |
| [[MBNL1]] | -0.58 | -0.46 / -0.53 | both halves | 2e-05 |  |
| [[CDH2]] | -0.57 | -0.38 / -0.61 | both halves | 6e-05 |  |
| [[CHRAC1]] | -0.57 | -0.46 / -0.51 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 107]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.594). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.16; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-40.6, -6.0); signed map (-19.1, -2.1). **Vector** length 51.7, 6.96% of its response variance represented; |z| ≥ 3 in 717 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +2.9 | +4.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +2.8 | +3.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.5 | +4.3 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.7 | +3.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +1.6 | +9.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.5 | +2.7 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.5 | +3.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +2.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.9 | -4.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -2.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | -2.6 | +3.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.4 | +1.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.3 | +0.5 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.3 | -2.4 |
|  | [[Ralimetinib dimesylate (drug)]] 5 µM |  | -1.3 | -1.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.1 | -0.2 |
|  | [[Bentamapimod (drug)]] 5 µM |  | -1.1 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | peroxisomal biogenesis factor 16 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p11.2 — chr11:45,909,663-45,918,812 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Peroxins |
| Hallmark sets | BILE_ACID_METABOLISM |
| Reactome | 2 pathways, smallest: Class I peroxisomal membrane protein import; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5Y5](https://www.uniprot.org/uniprotkb/Q9Y5Y5) (Peroxisomal membrane protein PEX16):

> Required for peroxisome membrane biogenesis. May play a role in early stages of peroxisome assembly. Can recruit other peroxisomal proteins, such as PEX3 and PMP34, to de novo peroxisomes derived from the endoplasmic reticulum (ER). May function as receptor for PEX3.

**Summary**, from NCBI Gene [9409](https://www.ncbi.nlm.nih.gov/gene/9409):

> The protein encoded by this gene is an integral peroxisomal membrane protein. An inactivating nonsense mutation localized to this gene was observed in a patient with Zellweger syndrome of the complementation group CGD/CG9. Expression of this gene product morphologically and biochemically restores the formation of new peroxisomes, suggesting a role in peroxisome organization and biogenesis. Alternative splicing has been observed for this gene and two variants have been described. [provided by …

**Accessions** — [HGNC:8857](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8857) · Entrez [9409](https://www.ncbi.nlm.nih.gov/gene/9409) · UniProt [Q9Y5Y5](https://www.uniprot.org/uniprotkb/Q9Y5Y5) · Ensembl [ENSG00000121680](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121680)

## Data

Gene col 4286: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4286); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4286, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4286]; `tensor/DDL_lfc|DDL_z.npy` [4286]; `embed/gene_vectors.npy` [4286]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4286 or target_col == 4286). Every well: [[PEX16 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PEX16.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
