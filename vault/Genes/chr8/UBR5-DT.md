---
symbol: "UBR5-DT"
type: "gene"
col: 14460
ensembl_id: "ENSG00000246263"
name: "UBR5 divergent transcript"
location: "8q22.3"
module: 14
arm: "+"
pooled_cpm: 3.86
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 1
n_dd_up_clean: 18
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# UBR5-DT

*UBR5 divergent transcript* — 8q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.84× (z +11.9, q 5e-30, up in 33 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.864× (z -5.6, q 1e-05, down in 17 of 47 measured lines) ⚠ position not correctable. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 0.455× (z -4.7, q 8e-04, down in 14 of 34 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Bestatin (drug)]] 0.05 µM in 1 line (NCI-H23 0.0603×); [[Cepharanthine (drug)]] 0.5 µM in 1 line (BT-474 0.0777×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GCC2-AS1]] (+0.54, fdr 1e-05), [[ELOVL7]] (+0.50, fdr 2e-05), [[BTG1-DT]] (+0.50, fdr 5e-05); moves opposite to [[COASY]] (-0.47, fdr 2e-05), [[TOMM70]] (-0.45, fdr 5e-05), [[SUV39H1]] (-0.45, fdr 5e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14460.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.84×** | +11.9 | 5e-30 | 33/47 (SW1417, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.88×** | +10.2 | 4e-22 | 22/38 (A498, C32, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.44×** | +10.2 | 4e-22 | 29/43 (PANC-1, A498, …) | top dose only | cell-cycle shift (explains ~6% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.37×** | +9.9 | 8e-21 | 33/43 (SW1417, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.14×** | +8.1 | 9e-14 | 5/9 (A498, A549, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.56×** | +7.2 | 5e-11 | 21/45 (LOX-IMVI, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.69×** | +5.8 | 6e-07 | 2/5 (LOX-IMVI, SW1417) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.43×** | +5.8 | 6e-07 | 16/38 (A498, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.61×** | +5.5 | 3e-06 | 6/18 (A498, SW480, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.56×** | +5.1 | 2e-05 | 12/43 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +4.9 | 4e-05 | 11/33 (A498, C32, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.53×** | +4.9 | 4e-05 | 13/46 (Hs 766T, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +4.9 | 4e-05 | 6/24 (A498, LS 180, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.50×** | +4.7 | 1e-04 | 12/40 (SW1417, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.28×** | +4.0 | 0.002 | 7/47 (A549, A498, …) | rises with dose | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +3.6 | 0.013 | 9/37 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.35×** | +3.3 | 0.028 | 14/44 (A498, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Norepinephrine (hydrochloride) (drug)]] 5 µM |  | **1.21×** | +3.1 | 0.049 | 6/45 (SHP-77, LS 180, …) | top dose only | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.31×** | +3.1 | 0.049 | 11/43 (C-33 A, BT-474, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.31×** | +3.1 | 0.049 | 9/46 (SW480, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14460.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Bestatin (drug)]] 0.05 µM in 1 line (NCI-H23 0.0603×); [[Cepharanthine (drug)]] 0.5 µM in 1 line (BT-474 0.0777×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.864× | -5.6 | 1e-05 | 17/47 (H4, A549, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.455×** | -4.7 | 8e-04 | 14/34 (SW480, A549, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | 0.739× | -3.4 | 0.12 | 12/45 (A549, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14460. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 2.67 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.25× (z +10.2) | — |
| [[BT-474 (line)]] | alt | 5.24 | 0 | 1 | — | [[Cepharanthine (drug)]] 0.5 µM 0.0777× (z -8.9) |
| [[C32 (line)]] | wt | 3.29 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.85× (z +8.8) | — |
| [[NCI-H23 (line)]] | alt | 6.10 | 0 | 1 | — | [[Bestatin (drug)]] 0.05 µM 0.0603× (z -10.2) |
| [[NCI-H460 (line)]] | wt | 3.24 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.30× (z +8.6) | — |
| [[A-172 (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.18 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.04 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.84 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.74 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.09 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.56 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.86 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.89 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14460), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GCC2-AS1]] | +0.54 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[ELOVL7]] | +0.50 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[BTG1-DT]] | +0.50 | +0.39 / +0.54 | both halves | 5e-05 | same gene group |
| [[NBEAP1]] | +0.47 | +0.27 / +0.59 | both halves | 3e-04 |  |
| [[HES6]] | +0.47 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[GDF15]] | +0.46 | +0.28 / +0.50 | both halves | 3e-04 |  |
| [[MAK]] | +0.45 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[GATM]] | +0.45 | +0.39 / +0.47 | both halves | 6e-05 |  |
| [[PAXIP1-DT]] | +0.45 | +0.50 / +0.39 | both halves | 5e-05 | same gene group |
| [[WASL-DT]] | +0.45 | +0.47 / +0.39 | both halves | 5e-05 | same gene group |
| [[MEF2A]] | +0.45 | +0.37 / +0.44 | both halves | 8e-05 |  |
| [[KDM7A-DT]] | +0.44 | +0.25 / +0.54 | both halves | 4e-04 | same gene group |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COASY]] | -0.47 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[TOMM70]] | -0.45 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[SUV39H1]] | -0.45 | -0.39 / -0.48 | both halves | 5e-05 |  |
| [[SLC10A7]] | -0.45 | -0.48 / -0.33 | both halves | 1e-04 |  |
| [[RBM10]] | -0.44 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[THRAP3]] | -0.43 | -0.38 / -0.37 | both halves | 8e-05 |  |
| [[TTLL11]] | -0.43 | -0.27 / -0.46 | both halves | 3e-04 |  |
| [[ORC1]] | -0.43 | -0.38 / -0.46 | both halves | 6e-05 |  |
| [[NVL]] | -0.42 | -0.36 / -0.37 | both halves | 9e-05 |  |
| [[ZNF519]] | -0.42 | -0.38 / -0.42 | both halves | 7e-05 |  |
| [[TMEM11]] | -0.42 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[CHEK1]] | -0.41 | -0.35 / -0.46 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.309). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.6, 32.1); signed map (39.3, 8.9). **Vector** length 54.0, 7.09% of its response variance represented; |z| ≥ 3 in 1,001 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.8 | +8.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.7 | +5.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +5.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +7.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.7 | +10.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.6 | +2.1 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.6 | +2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +3.1 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +1.2 | +2.4 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -2.4 | -3.4 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.3 | -5.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | -1.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.1 | -4.7 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -1.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.6 | -0.5 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.2 | -0.1 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.2 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | UBR5 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 8q22.3 — chr8:102,239,386-102,253,750 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously UBR5-AS1 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:51661](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51661) · Entrez [101927221](https://www.ncbi.nlm.nih.gov/gene/101927221) · Ensembl [ENSG00000246263](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000246263)

## Data

Gene col 14460: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14460); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14460, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14460]; `tensor/DDL_lfc|DDL_z.npy` [14460]; `embed/gene_vectors.npy` [14460]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14460 or target_col == 14460). Every well: [[UBR5-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBR5-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
