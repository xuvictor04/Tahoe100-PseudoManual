---
symbol: "CCDC24"
type: "gene"
col: 8231
ensembl_id: "ENSG00000159214"
name: "coiled-coil domain containing 24"
location: "1p34.1"
module: 14
arm: "+"
pooled_cpm: 6.77
n_lines_expressing: 48
n_dd_up: 6
n_dd_down: 15
n_dd_up_clean: 5
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# CCDC24

*coiled-coil domain containing 24* — 1p34.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.37× (z +4.6, q 0.003, up in 16 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.527× (z -6.6, q 2e-08, down in 26 of 45 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.567× (z -5.8, q 1e-06, down in 22 of 40 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GALT]] (+0.62, fdr 7e-06), [[TLCD1]] (+0.59, fdr 1e-05), [[SLC2A6]] (+0.58, fdr 1e-05); moves opposite to [[GCN1]] (-0.61, fdr 1e-05), [[ZNF587B]] (-0.58, fdr 1e-05), [[TXNDC5]] (-0.53, fdr 9e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8231.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +4.6 | 0.003 | 16/41 (Hs 766T, NCI-H460, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +4.1 | 0.010 | 7/46 (NCI-H23, HOP62, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.35×** | +3.7 | 0.037 | 12/45 (NCI-H23, SW480, …) | two highest doses | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **1.28×** | +3.6 | 0.044 | 7/45 (A-427, NCI-H23, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.43×** | +3.5 | 0.048 | 9/44 (NCI-H23, HS-578T, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.42×** | +3.5 | 0.050 | 1/9 (PANC-1) | top dose only | cell-cycle shift (explains ~12% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.55×** | +3.2 | 0.097 | 6/32 (Panc 03.27, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.54× | +3.2 | 0.10 | 5/29 (SW480, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | 1.53× | +3.2 | 0.10 | 3/43 (Panc 03.27, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.27× | +3.0 | 0.14 | 4/46 (NCI-H23, SW480, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8231.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.527×** | -6.6 | 2e-08 | 26/45 (PANC-1, HOP62, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.567×** | -5.8 | 1e-06 | 22/40 (NCI-H23, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.580×** | -5.6 | 4e-06 | 22/45 (hTERT-HPNE, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.589×** | -5.5 | 7e-06 | 25/44 (HCT15, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.605×** | -5.2 | 2e-05 | 21/41 (NCI-H23, PANC-1, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.384×** | -5.2 | 2e-05 | 20/39 (C-33 A, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.400×** | -4.9 | 7e-05 | 20/42 (A-427, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.435×** | -4.5 | 5e-04 | 19/45 (HCT15, RPMI-7951, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.648×** | -4.5 | 5e-04 | 16/35 (HOP62, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.683×** | -3.9 | 0.005 | 16/40 (NCI-H1573, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.696×** | -3.7 | 0.010 | 17/44 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.701×** | -3.7 | 0.012 | 11/39 (NCI-H1573, HEC-1-A, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.719×** | -3.4 | 0.030 | 14/45 (SK-MEL-2, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.637×** | -3.3 | 0.037 | 11/46 (PANC-1, C-33 A, …) | two highest doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.717×** | -3.2 | 0.046 | 14/42 (C32, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8231. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 4.39 | 0 | 2 | — | [[TAK-901 (drug)]] 0.05 µM 0.0541× (z -9.5) |
| [[NCI-H23 (line)]] | alt | 20.0 | 1 (1 ⚠) | 1 | [[Adagrasib (drug)]] 0.05 µM 1.57× (z +8.6) ⚠ position not correctable | [[Auranofin (drug)]] 5 µM 0.115× (z -11.7) |
| [[C-33 A (line)]] | alt | 8.74 | 0 | 1 | — | [[Ferulic acid (drug)]] 0.05 µM 0.0637× (z -8.6) |
| [[HCT15 (line)]] | alt | 10.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 4.51 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.0814× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 13.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.168× (z -10.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 7.72 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.34 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.92 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.69 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.99 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.48 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.79 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.18 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.14 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.36 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.77 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.15 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.13 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.33 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.94 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.29 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.62 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8231), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GALT]] | +0.62 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[TLCD1]] | +0.59 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[SLC2A6]] | +0.58 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[PLPP1]] | +0.58 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[NINJ1]] | +0.58 | +0.46 / +0.62 | both halves | 3e-05 |  |
| [[NCOA1]] | +0.57 | +0.46 / +0.59 | both halves | 2e-05 |  |
| [[NDUFB1]] | +0.55 | +0.38 / +0.67 | both halves | 6e-05 |  |
| [[TBC1D12]] | +0.55 | +0.34 / +0.57 | both halves | 1e-04 |  |
| [[WSB1]] | +0.55 | +0.32 / +0.63 | both halves | 2e-04 |  |
| [[HCFC1R1]] | +0.55 | +0.43 / +0.63 | both halves | 3e-05 |  |
| [[OGA]] | +0.54 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[LACTB]] | +0.54 | +0.43 / +0.61 | both halves | 3e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GCN1]] | -0.61 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[ZNF587B]] | -0.58 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[TXNDC5]] | -0.53 | -0.36 / -0.60 | both halves | 9e-05 |  |
| [[SLC38A1]] | -0.51 | -0.31 / -0.59 | both halves | 2e-04 |  |
| [[EIF2S1]] | -0.51 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[PUM3]] | -0.51 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[XRCC5]] | -0.50 | -0.38 / -0.54 | both halves | 7e-05 |  |
| [[RNF32-AS1]] | -0.50 | -0.30 / -0.56 | both halves | 2e-04 |  |
| [[LINC02728]] | -0.49 | -0.25 / -0.53 | both halves | 4e-04 |  |
| [[NUP155]] | -0.48 | -0.39 / -0.52 | both halves | 5e-05 |  |
| [[GNL3L]] | -0.48 | -0.29 / -0.56 | both halves | 3e-04 |  |
| [[SPTLC1]] | -0.48 | -0.40 / -0.51 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.484). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.9, -6.4); signed map (40.3, 6.3). **Vector** length 58.3, 9.01% of its response variance represented; |z| ≥ 3 in 761 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +1.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.8 | +2.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.7 | +3.7 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | +1.6 | +2.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.5 | +2.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.5 | +3.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.3 | +3.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.1 | -5.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.3 | -6.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.5 | -3.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.5 | +3.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.3 | -5.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.9 | -2.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.9 | -4.5 |
|  | [[EX229 (drug)]] 5 µM |  | -1.8 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 24 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.1 — chr1:43,991,359-43,996,528 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC45441 |
| Matched by | ensembl_id |

UniProt [Q8N4L8](https://www.uniprot.org/uniprotkb/Q8N4L8) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:28688](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28688) · Entrez [149473](https://www.ncbi.nlm.nih.gov/gene/149473) · UniProt [Q8N4L8](https://www.uniprot.org/uniprotkb/Q8N4L8) · Ensembl [ENSG00000159214](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159214)

## Data

Gene col 8231: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8231); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8231, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8231]; `tensor/DDL_lfc|DDL_z.npy` [8231]; `embed/gene_vectors.npy` [8231]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8231 or target_col == 8231). Every well: [[CCDC24 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC24.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
