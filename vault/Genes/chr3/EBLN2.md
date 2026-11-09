---
symbol: "EBLN2"
type: "gene"
col: 14937
ensembl_id: "ENSG00000255423"
name: "endogenous Bornavirus like nucleoprotein 2"
location: "3p13"
module: 17
arm: "+"
pooled_cpm: 5.04
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 10
n_dd_up_clean: 7
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# EBLN2

*endogenous Bornavirus like nucleoprotein 2* — 3p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 9.61× (z +13.7, q 4e-40, up in 40 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.745× (z -11.9, q 5e-30, down in 45 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.613× (z -8.0, q 3e-13, down in 25 of 42 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPP4R2]] (+0.65, fdr 7e-06, ⚠ read-through risk), [[FAM133B]] (+0.60, fdr 1e-05), [[ANKRD13C]] (+0.58, fdr 1e-05), [[SLC25A12]] (+0.57, fdr 1e-05); moves opposite to [[PSMD8]] (-0.52, fdr 7e-05), [[DPAGT1]] (-0.51, fdr 2e-04), [[UBR4]] (-0.51, fdr 3e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14937.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **9.61×** | +13.7 | 4e-40 | 40/43 (SW480, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **5.06×** | +9.8 | 2e-20 | 31/38 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.54×** | +7.1 | 3e-10 | 21/40 (A549, SNU-423, …) | top dose only | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.52×** | +4.7 | 4e-04 | 20/44 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.43×** | +4.1 | 0.004 | 12/46 (NCI-H2030, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +3.8 | 0.015 | 11/33 (LoVo, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.35×** | +3.5 | 0.042 | 9/47 (NCI-H1573, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Sulfisoxazole (drug)]] 5 µM |  | **1.22×** | +3.3 | 0.070 | 6/46 (RPMI-7951, SK-MEL-2, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.32×** | +3.2 | 0.082 | 8/39 (LoVo, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14937.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.745×** | -11.9 | 5e-30 | 45/48 (A-172, CHP-212, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.613×** | -8.0 | 3e-13 | 25/42 (LOX-IMVI, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.543×** | -7.1 | 3e-10 | 20/27 (HEC-1-A, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.616×** | -5.6 | 3e-06 | 19/45 (SW480, RPMI-7951, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.633×** | -5.3 | 1e-05 | 19/46 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.676×** | -4.2 | 0.003 | 11/15 (HOP62, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.716×** | -3.9 | 0.009 | 9/47 (SW1417, NCI-H661, …) | all doses, stronger at high dose | position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.727×** | -3.7 | 0.015 | 12/46 (NCI-H23, HCT15, …) | inconsistent across doses |  |
| [[Decitabine (drug)]] 0.05 µM |  | **0.721×** | -3.5 | 0.028 | 7/39 (NCI-H460, RPMI-7951, …) | inconsistent across doses | position effect removed |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM |  | **0.757×** | -3.2 | 0.072 | 15/39 (SNU-423, NCI-H1573, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14937. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 5.93 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.114× (z -9.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 7.46 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0956× (z -12.6) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 4.19 | 0 | 1 | — | [[Altretamine (drug)]] 0.05 µM 0.0770× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 5.58 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.132× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 4.46 | 0 | 1 | — | [[Erlotinib (drug)]] 5 µM 0.0828× (z -8.6) |
| [[RKO (line)]] | wt | 7.53 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.105× (z -8.6) |
| [[SNU-423 (line)]] | alt | 6.19 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0750× (z -9.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.18 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.98 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.68 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.68 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.29 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.59 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.54 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.02 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.06 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.26 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.65 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.72 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.77 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14937), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP4R2]] | +0.65 | +0.60 / +0.58 | both halves | 7e-06 | ⚠ **readthrough risk**: this gene lies 0.0 kb 3′ of PPP4R2 on the same strand (can correlate by spillover, not regulation) |
| [[FAM133B]] | +0.60 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[ANKRD13C]] | +0.58 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[SLC25A12]] | +0.57 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[METTL14]] | +0.57 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[EBAG9]] | +0.57 | +0.46 / +0.48 | both halves | 2e-05 |  |
| [[ZNF14]] | +0.57 | +0.54 / +0.46 | both halves | 3e-05 |  |
| [[PTBP2]] | +0.56 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[GTF2H5]] | +0.55 | +0.40 / +0.34 | both halves | 1e-04 |  |
| [[RPS26]] | +0.55 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[MECP2]] | +0.55 | +0.46 / +0.46 | both halves | 2e-05 |  |
| [[DET1]] | +0.53 | +0.53 / +0.39 | both halves | 6e-05 |  |
| [[VAPA]] | +0.53 | +0.49 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMD8]] | -0.52 | -0.37 / -0.51 | both halves | 7e-05 |  |
| [[DPAGT1]] | -0.51 | -0.29 / -0.55 | both halves | 2e-04 |  |
| [[UBR4]] | -0.51 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[HCFC1]] | -0.51 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[CEP170B]] | -0.50 | -0.43 / -0.39 | both halves | 5e-05 |  |
| [[PEPD]] | -0.49 | -0.47 / -0.39 | both halves | 5e-05 |  |
| [[DVL3]] | -0.49 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[C1orf198]] | -0.48 | -0.29 / -0.44 | both halves | 2e-04 |  |
| [[RBM19]] | -0.48 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[FKBP4]] | -0.47 | -0.37 / -0.46 | both halves | 8e-05 |  |
| [[ZNF731P]] | -0.47 | -0.28 / -0.42 | both halves | 3e-04 |  |
| [[RELT]] | -0.47 | -0.37 / -0.39 | both halves | 8e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.437). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-25.8, 15.5); signed map (-21.3, -10.3). **Vector** length 47.5, 5.24% of its response variance represented; |z| ≥ 3 in 1,024 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +4.2 | +13.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.8 | +9.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +0.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +1.9 | +4.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.9 | +1.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.3 | +2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +0.9 | +0.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +0.9 | +1.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.7 | -5.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.2 | -8.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -2.8 | -7.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | -2.7 | -2.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | +0.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | +1.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.4 | -2.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.2 | -1.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -1.1 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | endogenous Bornavirus like nucleoprotein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p13 — chr3:73,061,659-73,063,337 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P2I7](https://www.uniprot.org/uniprotkb/Q6P2I7) (Endogenous Bornavirus-like nucleoprotein 2):

> May act as an RNA-binding protein. The C-terminal region is highly homologous to the bornavirus nucleocapsid N protein that binds viral RNA and oligomerizes. The viral protein also possesses a nuclear import and a nuclear export signal. These 2 signals seem absent in EBLN-2 supporting an unrelated function in Human.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:25493](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25493) · Entrez [55096](https://www.ncbi.nlm.nih.gov/gene/55096) · UniProt [Q6P2I7](https://www.uniprot.org/uniprotkb/Q6P2I7) · Ensembl [ENSG00000255423](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000255423)

## Data

Gene col 14937: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14937); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14937, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14937]; `tensor/DDL_lfc|DDL_z.npy` [14937]; `embed/gene_vectors.npy` [14937]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14937 or target_col == 14937). Every well: [[EBLN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EBLN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
