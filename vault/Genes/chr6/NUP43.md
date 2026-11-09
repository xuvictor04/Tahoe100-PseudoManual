---
symbol: "NUP43"
type: "gene"
col: 4169
ensembl_id: "ENSG00000120253"
name: "nucleoporin 43"
location: "6q25.1"
module: 6
arm: "+"
pooled_cpm: 32.85
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 1
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# NUP43

*nucleoporin 43* — 6q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.38× (z +21.9, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.857× (z -5.5, q 2e-05, down in 17 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A-427 0.423×, PANC-1 0.587×, AN3 CA 0.336×; ⚠ cell-cycle shift, explains ~22% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (PANC-1 0.434×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (C-33 A 0.190×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ORC3]] (+0.67, fdr 7e-06), [[RPA1]] (+0.67, fdr 7e-06), [[TPRKB]] (+0.65, fdr 1e-05); moves opposite to [[MMP25-AS1]] (-0.59, fdr 3e-05), [[NANOS3]] (-0.57, fdr 6e-05), [[CXCL2]] (-0.54, fdr 4e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CXCL2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 16 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4169.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.38×** | +21.9 | 0e+00 | 47/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.29×** | +20.9 | 0e+00 | 47/48 (LoVo, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.18×** | +19.7 | 0e+00 | 48/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.37×** | +11.3 | 3e-27 | 34/48 (PANC-1, SW1417, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.58×** | +11.1 | 2e-26 | 26/38 (LoVo, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.51×** | +10.0 | 2e-21 | 31/47 (NCI-H23, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **1.48×** | +9.8 | 7e-21 | 32/44 (LoVo, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.46×** | +9.4 | 3e-19 | 32/48 (SW480, LOX-IMVI, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.39×** | +8.2 | 1e-14 | 28/47 (LoVo, LOX-IMVI, …) | two highest doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.38×** | +7.7 | 7e-13 | 27/48 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.25×** | +5.6 | 1e-06 | 22/48 (NCI-H23, LoVo, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **1.25×** | +5.4 | 4e-06 | 17/47 (LoVo, C-33 A, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 1.20× | +4.5 | 3e-04 | 13/48 (LoVo, LOX-IMVI, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 1.19× | +4.4 | 4e-04 | 17/47 (A498, J82, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change | 1.20× | +4.2 | 0.001 | 13/42 (SNU-423, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.20×** | +3.8 | 0.006 | 12/48 (PANC-1, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.32×** | +3.6 | 0.009 | 8/48 (SW480, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.16× | +3.5 | 0.014 | 9/47 (NCI-H2030, LoVo, …) | inconsistent across doses | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | 1.14× | +3.4 | 0.020 | 4/48 (HepG2/C3A, HT-29, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.13× | +3.0 | 0.057 | 10/48 (LOX-IMVI, NCI-H1792, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.09× | +3.0 | 0.062 | 8/48 (PANC-1, SNU-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4169.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A-427 0.423×, PANC-1 0.587×, AN3 CA 0.336×; ⚠ cell-cycle shift, explains ~22% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (PANC-1 0.434×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (C-33 A 0.190×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | 0.857× | -5.5 | 2e-05 | 17/48 (NCI-H1573, HepG2/C3A, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.830×** | -4.7 | 8e-04 | 15/48 (Hs 766T, SW480, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.866× | -3.6 | 0.052 | 11/47 (NCI-H2030, A-172, …) | all doses, flat | low cells (technical?) |
| [[Cobimetinib (drug)]] 5 µM |  | 0.877× | -3.2 | 0.18 | 11/47 (LOX-IMVI, MIA PaCa-2, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.882× | -3.2 | 0.18 | 7/47 (J82, A-427, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 0.919× | -3.0 | 0.23 | 15/48 (A-427, PANC-1, …) | top dose only | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4169. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 83.7 | 4 (2 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.11× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.427× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[PANC-1 (line)]] | alt | 44.4 | 2 (1 ⚠) | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.72× (z +10.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Belinostat (drug)]] 5 µM 1.82× (z +8.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.434× (z -11.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 29.8 | 4 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.37× (z +12.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.99× (z +11.3) | — |
| [[LOX-IMVI (line)]] | wt | 27.2 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.17× (z +10.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 38.1 | 3 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.57× (z +8.8) | — |
| [[SW480 (line)]] | alt | 67.3 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.29× (z +11.8) | — |
| [[HEC-1-A (line)]] | alt | 42.9 | 2 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.10× (z +9.0) | — |
| [[NCI-H460 (line)]] | wt | 26.3 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.34× (z +9.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.21× (z +8.6) | — |
| [[RKO (line)]] | wt | 34.0 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.37× (z +9.4) | — |
| [[A-427 (line)]] | wt | 37.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.423× (z -11.3) ⚠ cell-cycle shift, explains ~22% of this change |
| [[A498 (line)]] | wt | 27.5 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.66× (z +10.5) | — |
| [[A549 (line)]] | wt | 26.4 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.90× (z +8.5) | — |
| [[AN3 CA (line)]] | alt | 66.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -8.6) ⚠ cell-cycle shift, explains ~22% of this change |
| [[C-33 A (line)]] | alt | 41.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.190× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change |
| [[Hs 766T (line)]] | wt | 25.0 | 0 | 1 (1 ⚠) | — | [[Tucidinostat (drug)]] 0.5 µM 0.300× (z -8.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[HT-29 (line)]] | alt | 26.4 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.03× (z +8.6) | — |
| [[LS 180 (line)]] | wt | 28.8 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.92× (z +9.1) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[A-172 (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 37.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 34.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4169), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ORC3]] | +0.67 | +0.70 / +0.60 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[RPA1]] | +0.67 | +0.61 / +0.61 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[TPRKB]] | +0.65 | +0.59 / +0.53 | both halves | 1e-05 | pathway: tRNA processing; STRING 799 |
| [[MRE11]] | +0.65 | +0.63 / +0.58 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[NAP1L4]] | +0.65 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[EFCAB11]] | +0.64 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[PPIH]] | +0.64 | +0.62 / +0.60 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[MSH2]] | +0.63 | +0.51 / +0.65 | both halves | 1e-05 | STRING 438 |
| [[RFC4]] | +0.63 | +0.59 / +0.60 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 866 |
| [[TRAIP]] | +0.63 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[ZCCHC17]] | +0.61 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[RFC5]] | +0.61 | +0.57 / +0.54 | both halves | 1e-05 | pathway: Cell Cycle Checkpoints |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MMP25-AS1]] | -0.59 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[NANOS3]] | -0.57 | -0.53 / -0.39 | both halves | 6e-05 |  |
| [[CXCL2]] | -0.54 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[SYNPO]] | -0.53 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[LITAF]] | -0.53 | -0.54 / -0.32 | both halves | 2e-04 |  |
| [[ZFHX2]] | -0.53 | -0.57 / -0.34 | both halves | 1e-04 |  |
| [[PATL2]] | -0.53 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[MAP3K2-DT]] | -0.52 | -0.52 / -0.38 | both halves | 6e-05 |  |
| [[PDE4C]] | -0.52 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[LGALSL-DT]] | -0.51 | -0.52 / -0.29 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CXCL2]] | B | CXCL2 activity lowers NUP43's level | lines that do not express CXCL2 (14) vs lines expressing it (36) | 1.39× higher at baseline in the lines without CXCL2 | 0.071 | ⚠ within organs, on part of the lines; also absent: TENT5A, GPR39, CXCL3 |
| [[TOP2A]] | B | TOP2A activity lowers NUP43's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.525). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-27.9, -47.8); signed map (-36.9, -31.6). **Vector** length 73.6, 13.3% of its response variance represented; |z| ≥ 3 in 864 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +3.5 | +20.9 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.4 | +19.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.3 | +21.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +2.5 | +10.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | +2.3 | +9.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.2 | +9.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.6 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +5.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.3 | +2.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.3 | -0.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -7.3 | -3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.3 | -5.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -5.3 | -4.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.9 | +2.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | -3.3 | +0.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.1 | -2.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.9 | -3.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.9 | -2.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.7 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | nucleoporin 43 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q25.1 — chr6:149,724,315-149,749,665 (-) |
| Ensembl biotype | protein_coding |
| Also known as | bA350J20.1, FLJ13287 |
| Gene groups (HGNC) | WD repeat domain containing; Nucleoporins |
| Reactome | 85 pathways, smallest: Postmitotic nuclear pore complex (NPC) reformation; IP3 and IP4 transport between cytosol and nucleus; IP6 and IP7 transport between cytosol and nucleus |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NFH3](https://www.uniprot.org/uniprotkb/Q8NFH3) (Nucleoporin Nup43):

> Component of the Nup107-160 subcomplex of the nuclear pore complex (NPC). The Nup107-160 subcomplex is required for the assembly of a functional NPC. The Nup107-160 subcomplex is also required for normal kinetochore microtubule attachment, mitotic progression and chromosome segregation.

**Summary**, from NCBI Gene [348995](https://www.ncbi.nlm.nih.gov/gene/348995):

> Bidirectional transport of macromolecules between the cytoplasm and nucleus occurs through nuclear pore complexes (NPCs) embedded in the nuclear envelope. NPCs are composed of subcomplexes, and NUP43 is part of one such subcomplex, Nup107-160 (Loiodice et al., 2004 [PubMed 15146057]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:21182](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21182) · Entrez [348995](https://www.ncbi.nlm.nih.gov/gene/348995) · UniProt [Q8NFH3](https://www.uniprot.org/uniprotkb/Q8NFH3) · Ensembl [ENSG00000120253](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120253)

## Data

Gene col 4169: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4169); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4169, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4169]; `tensor/DDL_lfc|DDL_z.npy` [4169]; `embed/gene_vectors.npy` [4169]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4169 or target_col == 4169). Every well: [[NUP43 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NUP43.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
