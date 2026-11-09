---
symbol: "ZFHX4"
type: "gene"
col: 1675
ensembl_id: "ENSG00000091656"
name: "zinc finger homeobox 4"
location: "8q21.13"
module: 9
arm: "+"
pooled_cpm: 29.1
n_lines_expressing: 27
n_dd_up: 14
n_dd_down: 25
n_dd_up_clean: 11
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 11
direction_downstream: 5
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# ZFHX4

*zinc finger homeobox 4* — 8q21.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.59× (z +7.1, q 9e-10, up in 16 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (17 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.515× (z -9.6, q 5e-19, down in 20 of 24 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.706× (z -5.5, q 3e-06, down in 15 of 25 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MIR3171HG]] (+0.70, fdr 7e-06), [[SLITRK5]] (+0.68, fdr 7e-06), [[FIGN]] (+0.67, fdr 7e-06); moves opposite to [[TMEM50B]] (-0.49, fdr 4e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[ZFHX4-AS1]] → it (grade C ⚠); 5 go from it, the strongest it → [[TBX18]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1675.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.59×** | +7.1 | 9e-10 | 16/24 (HEC-1-A, A-427, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.50×** | +5.9 | 1e-06 | 12/25 (A-172, hTERT-HPNE, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.40×** | +5.2 | 4e-05 | 11/25 (NCI-H2347, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.26×** | +5.1 | 6e-05 | 12/25 (NCI-H2347, A-172, …) | rises with dose | low cells (technical?) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.34×** | +4.2 | 0.003 | 13/24 (HEC-1-A, A-427, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.21×** | +4.1 | 0.003 | 10/25 (A-427, HEC-1-A, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.30×** | +4.1 | 0.003 | 12/25 (PANC-1, BT-474, …) | two highest doses |  |
| [[NG25 (drug)]] 5 µM |  | **1.62×** | +4.0 | 0.005 | 10/24 (NCI-H2347, HOP62, …) | top dose only | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.28×** | +3.9 | 0.005 | 9/25 (hTERT-HPNE, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.26×** | +3.6 | 0.019 | 10/25 (A-427, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **1.25×** | +3.5 | 0.021 | 4/25 (J82, A-427, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.17× | +3.5 | 0.021 | 10/25 (PANC-1, NCI-H1573, …) | two highest doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.26×** | +3.5 | 0.021 | 10/24 (A-427, NCI-H2030, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.18× | +3.2 | 0.053 | 11/25 (A-427, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.21×** | +3.1 | 0.079 | 8/25 (HOP62, LOX-IMVI, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.23×** | +3.0 | 0.086 | 7/25 (A-427, HEC-1-A, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 17 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1675.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.515×** | -9.6 | 5e-19 | 20/24 (LOX-IMVI, C-33 A, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.546×** | -8.9 | 2e-16 | 19/23 (A-427, LOX-IMVI, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.580×** | -8.6 | 1e-15 | 15/25 (LOX-IMVI, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.584×** | -8.5 | 3e-15 | 17/25 (LOX-IMVI, HEC-1-A, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.683×** | -6.0 | 2e-07 | 17/24 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.706×** | -5.5 | 3e-06 | 15/25 (HEC-1-A, NCI-H2347, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.713×** | -5.3 | 8e-06 | 13/25 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.722×** | -5.1 | 2e-05 | 14/25 (NCI-H460, NCI-H23, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.541×** | -5.1 | 2e-05 | 18/25 (NCI-H2347, HOP62, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.804×** | -4.8 | 8e-05 | 14/25 (LOX-IMVI, C-33 A, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.763×** | -4.3 | 1e-03 | 11/25 (A-427, PANC-1, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.763×** | -4.1 | 0.002 | 14/25 (NCI-H460, A-427, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.773×** | -4.1 | 0.002 | 14/25 (A-427, HEC-1-A, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **0.779×** | -3.9 | 0.003 | 13/25 (HEC-1-A, SHP-77, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.781×** | -3.7 | 0.007 | 11/25 (LOX-IMVI, A498, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.744×** | -3.3 | 0.025 | 10/25 (LOX-IMVI, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.865× | -3.2 | 0.035 | 8/25 (CHP-212, LOX-IMVI, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.812×** | -3.0 | 0.069 | 8/24 (H4, LOX-IMVI, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 0.5 µM |  | **0.773×** | -2.9 | 0.085 | 7/25 (HOP62, LOX-IMVI, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[PF-06260933 (drug)]] 5 µM |  | **0.704×** | -2.9 | 0.085 | 3/25 (J82, A498, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1675. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 21.7 | 0 | 11 (9 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.203× (z -12.5) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.228× (z -10.6) |
| [[LOX-IMVI (line)]] | wt | 140 | 0 | 10 (10 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.156× (z -18.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[C-33 A (line)]] | alt | 186 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0878× (z -20.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 110 | 1 (1 ⚠) | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +10.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.0963× (z -19.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HEC-1-A (line)]] | alt | 101 | 0 | 5 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.326× (z -13.6) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H2347 (line)]] | alt | 64.5 | 2 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.36× (z +8.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.336× (z -11.0) ⚠ toxic; cell-cycle shift, explains ~77% of this change |
| [[SHP-77 (line)]] | alt | 59.0 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.248× (z -11.2) ⚠ cell-cycle shift, explains ~38% of this change |
| [[NCI-H1573 (line)]] | alt | 14.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.135× (z -9.6) |
| [[CHP-212 (line)]] | wt | 163 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.196× (z -10.3) ⚠ cell-cycle shift, explains ~38% of this change |
| [[A498 (line)]] | wt | 47.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -9.8) ⚠ cell-cycle shift, explains ~35% of this change |
| [[A549 (line)]] | wt | 22.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.251× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[H4 (line)]] | wt | 58.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.257× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 58.1 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.89× (z +9.8) | — |
| [[NCI-H1792 (line)]] | alt | 13.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.190× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 20.8 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.126× (z -13.3) ⚠ toxic; cell-cycle shift, explains ~77% of this change |
| [[NCI-H23 (line)]] | alt | 20.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.198× (z -10.0) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SNU-423 (line)]] | alt | 54.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +10.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A-172 (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.86 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.50 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.16 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.50 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.57 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.08 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.42 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.86 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.14 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.13 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 250 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.60 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.59 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.91 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.76 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.83 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.09 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.10 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.75 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 6.95 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1675), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIR3171HG]] | +0.70 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[SLITRK5]] | +0.68 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[FIGN]] | +0.67 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[FAT4]] | +0.65 | +0.62 / +0.58 | both halves | 7e-06 | STRING 572 |
| [[KCNH5]] | +0.65 | +0.61 / +0.58 | both halves | 8e-06 |  |
| [[MIR99AHG]] | +0.64 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[EPHA5]] | +0.64 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[IGSF1]] | +0.63 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[CRISPLD1]] | +0.61 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[KLHL13]] | +0.61 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[EPHA5-AS1]] | +0.60 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[PCDH18]] | +0.59 | +0.53 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM50B]] | -0.49 | -0.41 / -0.44 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 0, C 11.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZFHX4-AS1]] | C | ZFHX4-AS1 activity raises ZFHX4's level | lines that do not express ZFHX4-AS1 (29) vs lines expressing it (21) | 8.48× lower at baseline in the lines without ZFHX4-AS1 | 0.002 | ⚠ within organs, on part of the lines; also absent: PCDH17, LRCH2, GNAT3; maybe low, not absent; co-absent with the target |
| [[ERBB4]] | C | ERBB4 activity raises ZFHX4's level | lines that do not express ERBB4 (33) vs lines expressing it (17) | 6.40× lower at baseline in the lines without ERBB4 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FUT9, NETO1, CDH10; co-absent with the target |
| [[NETO1]] | C | NETO1 activity raises ZFHX4's level | lines that do not express NETO1 (43) vs lines expressing it (7) | 6.16× lower at baseline in the lines without NETO1 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, GPR15, SYT4; co-absent with the target |
| [[SNCA]] | C | SNCA activity raises ZFHX4's level | lines that do not express SNCA (29) vs lines expressing it (21) | 6.37× lower at baseline in the lines without SNCA | 0.053 | ⚠ within organs, on part of the lines; also absent: SLC6A15, CNKSR2, CDH10; co-absent with the target |
| [[CDH10]] | C | CDH10 activity raises ZFHX4's level | lines that do not express CDH10 (37) vs lines expressing it (13) | 6.97× lower at baseline in the lines without CDH10 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01035, FUT9, KCNH5; co-absent with the target |
| [[MGAT4C]] | C | MGAT4C activity raises ZFHX4's level | lines that do not express MGAT4C (35) vs lines expressing it (15) | 2.75× lower at baseline in the lines without MGAT4C | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000281566, LINC01205, ENSG00000286385; co-absent with the target |
| [[FMN2]] | C | FMN2 activity raises ZFHX4's level | lines that do not express FMN2 (26) vs lines expressing it (24) | 5.07× lower at baseline in the lines without FMN2 | 0.069 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, TRPC4, HECW2; maybe low, not absent; co-absent with the target |
| [[EPHA5]] | C | EPHA5 activity raises ZFHX4's level | lines that do not express EPHA5 (30) vs lines expressing it (20) | 5.72× lower at baseline in the lines without EPHA5 | 0.078 | ⚠ within organs, on part of the lines; also absent: EPHA5-AS1, CDH10, TRPC4; co-absent with the target |
| [[EPHA5-AS1]] | C | EPHA5-AS1 activity raises ZFHX4's level | lines that do not express EPHA5-AS1 (28) vs lines expressing it (22) | 6.28× lower at baseline in the lines without EPHA5-AS1 | 0.079 | ⚠ within organs, on part of the lines; also absent: EPHA5, ADAM23, TRPC4; co-absent with the target |
| [[TRPC4]] | C | TRPC4 activity raises ZFHX4's level | lines that do not express TRPC4 (32) vs lines expressing it (18) | 5.03× lower at baseline in the lines without TRPC4 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FMN2, LINC02211, FAM133A; co-absent with the target |
| [[ADGRB3]] | C | ADGRB3 activity raises ZFHX4's level | lines that do not express ADGRB3 (28) vs lines expressing it (22) | 5.07× lower at baseline in the lines without ADGRB3 | 0.095 | ⚠ within organs, on part of the lines; also absent: EPHA3, NCAM2, ST8SIA4; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TBX18]] | C | ZFHX4 activity raises TBX18's level | lines that do not express ZFHX4 (23) vs lines expressing it (27) | 4.00× lower at baseline in the lines without ZFHX4 | 0.010 | ⚠ within organs, on part of the lines; also absent: SNCA, UCHL1, SLITRK5; co-absent with the target |
| [[LRRK2]] | C | ZFHX4 activity raises LRRK2's level | lines that do not express ZFHX4 (23) vs lines expressing it (27) | 2.84× lower at baseline in the lines without ZFHX4 | 0.032 | ⚠ within organs, on part of the lines; also absent: SNCA, UCHL1, SLITRK5; co-absent with the target |
| [[ADGRB3]] | C | ZFHX4 activity raises ADGRB3's level | lines that do not express ZFHX4 (23) vs lines expressing it (27) | 4.53× lower at baseline in the lines without ZFHX4 | 0.079 | ⚠ within organs, on part of the lines; also absent: SNCA, UCHL1, SLITRK5; co-absent with the target |
| [[TRIM6]] | C | ZFHX4 activity raises TRIM6's level | lines that do not express ZFHX4 (23) vs lines expressing it (27) | 2.48× lower at baseline in the lines without ZFHX4 | 0.088 | ⚠ within organs, on part of the lines; also absent: SNCA, UCHL1, SLITRK5; co-absent with the target |
| [[CACNA2D1]] | C | ZFHX4 activity raises CACNA2D1's level | lines that do not express ZFHX4 (23) vs lines expressing it (27) | 5.00× lower at baseline in the lines without ZFHX4 | 0.097 | ⚠ within organs, on part of the lines; also absent: SNCA, UCHL1, SLITRK5; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.562). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.7, 32.0); signed map (39.4, 37.1). **Vector** length 80.8, 24.2% of its response variance represented; |z| ≥ 3 in 668 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +3.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | +4.2 | +4.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.2 | +5.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +3.1 | -4.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.1 | +5.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.3 | +7.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.3 | +3.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.0 | +3.2 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.9 | +4.2 |
| fall | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -2.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -2.6 | -8.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -2.3 | -8.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.3 | -0.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.1 | -1.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.1 | -5.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.8 | -1.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.7 | -2.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.5 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger homeobox 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q21.13 — chr8:76,681,239-76,867,281 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ZFH4, FLJ20980 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; Zinc fingers matrin-type; ZF class homeoboxes and pseudogenes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86UP3](https://www.uniprot.org/uniprotkb/Q86UP3) (Zinc finger homeobox protein 4):

> May play a role in neural and muscle differentiation (By similarity). May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [79776](https://www.ncbi.nlm.nih.gov/gene/79776):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to be located in chromatin. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30939](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30939) · Entrez [79776](https://www.ncbi.nlm.nih.gov/gene/79776) · UniProt [Q86UP3](https://www.uniprot.org/uniprotkb/Q86UP3) · Ensembl [ENSG00000091656](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000091656)

## Data

Gene col 1675: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1675); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1675, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1675]; `tensor/DDL_lfc|DDL_z.npy` [1675]; `embed/gene_vectors.npy` [1675]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1675 or target_col == 1675). Every well: [[ZFHX4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZFHX4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
