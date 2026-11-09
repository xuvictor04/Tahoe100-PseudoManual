---
symbol: "TTC39C"
type: "gene"
col: 9614
ensembl_id: "ENSG00000168234"
name: "tetratricopeptide repeat domain 39C"
location: "18q11.2"
module: 143
arm: "+"
pooled_cpm: 41.34
n_lines_expressing: 47
n_dd_up: 10
n_dd_down: 3
n_dd_up_clean: 8
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/143"]
generated_by: "tahoemap"
---

# TTC39C

*tetratricopeptide repeat domain 39C* — 18q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 1.38× (z +7.3, q 2e-10, up in 29 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.764× (z -6.1, q 4e-07, down in 21 of 45 measured lines) ⚠ cell-cycle shift, explains ~24% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.598× (z -6.1, q 4e-07, down in 22 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 7 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (C32 0.257×, RKO 0.343×, NCI-H1792 0.403×, A498 0.440×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (C-33 A 0.144×, SW 900 0.188×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (PANC-1 0.259×, SW1417 0.257×; ⚠ cell-cycle shift, explains ~24% of this change); [[Panobinostat (drug)]] 0.5 µM in 2 lines (SHP-77 0.450×, C-33 A 0.360×); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (Hs 766T 0.194×); [[Auranofin (drug)]] 5 µM in 1 line (SW 900 0.328×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NSMAF]] (+0.62, fdr 3e-05), [[PTPN4]] (+0.58, fdr 1e-05), [[NFIB]] (+0.57, fdr 3e-05); moves opposite to [[MMUT]] (-0.57, fdr 3e-05), [[GNAI3]] (-0.54, fdr 3e-05), [[NAGK]] (-0.54, fdr 5e-05).
> It is in [[Module 143]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[NFIA]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9614.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.38×** | +7.3 | 2e-10 | 29/45 (NCI-H1573, NCI-H23, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +5.6 | 5e-06 | 19/45 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.22×** | +4.5 | 0.001 | 20/45 (NCI-H1573, NCI-H1792, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.26×** | +4.3 | 0.002 | 16/45 (HEC-1-A, J82, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.23×** | +4.2 | 0.003 | 13/45 (PANC-1, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | **1.23×** | +4.2 | 0.003 | 8/45 (LoVo, HCT15, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +4.1 | 0.003 | 18/44 (CFPAC-1, H4, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.20×** | +4.1 | 0.003 | 15/44 (HEC-1-A, A-172, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.22×** | +4.0 | 0.003 | 16/44 (J82, HS-578T, …) | all doses, flat |  |
| [[Afatinib (drug)]] 5 µM |  | **1.21×** | +3.8 | 0.008 | 14/46 (NCI-H1573, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.7 | 0.010 | 17/45 (LoVo, H4, …) | top dose only | composition shift |
| [[Belumosudil (drug)]] 5 µM |  | 1.19× | +3.7 | 0.011 | 14/45 (NCI-H2347, LS 180, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 1.17× | +3.5 | 0.020 | 9/45 (NCI-H2347, Panc 03.27, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.33×** | +3.3 | 0.032 | 9/45 (PANC-1, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.16× | +3.3 | 0.032 | 5/45 (NCI-H1573, NCI-H1792, …) | inconsistent across doses |  |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | 1.17× | +3.1 | 0.058 | 6/45 (LOX-IMVI, RKO, …) | inconsistent across doses |  |
| [[Bentamapimod (drug)]] 5 µM |  | **1.29×** | +3.0 | 0.087 | 3/45 (SW480, KATO III, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | 1.16× | +3.0 | 0.087 | 5/45 (HCT15, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9614.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 7 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (C32 0.257×, RKO 0.343×, NCI-H1792 0.403×, A498 0.440×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (C-33 A 0.144×, SW 900 0.188×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (PANC-1 0.259×, SW1417 0.257×; ⚠ cell-cycle shift, explains ~24% of this change); [[Panobinostat (drug)]] 0.5 µM in 2 lines (SHP-77 0.450×, C-33 A 0.360×); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (Hs 766T 0.194×); [[Auranofin (drug)]] 5 µM in 1 line (SW 900 0.328×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.764×** | -6.1 | 4e-07 | 21/45 (PANC-1, SW1417, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.598×** | -6.1 | 4e-07 | 22/46 (RKO, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.784×** | -5.5 | 7e-06 | 22/45 (SHP-77, C-33 A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.838× | -4.0 | 0.010 | 21/45 (SHP-77, RKO, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~40% of this change | 0.840× | -3.9 | 0.010 | 16/43 (Panc 03.27, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.844× | -3.8 | 0.012 | 21/45 (SHP-77, RKO, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | 0.863× | -3.3 | 0.073 | 19/43 (PANC-1, RKO, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.957× | -3.2 | 0.10 | 1/46 (HOP62) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.827× | -3.0 | 0.15 | 15/45 (Panc 03.27, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9614. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 137 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.368× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.450× (z -9.5) |
| [[C-33 A (line)]] | alt | 67.1 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.144× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.360× (z -8.6) |
| [[PANC-1 (line)]] | alt | 30.1 | 0 | 4 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.259× (z -14.8) ⚠ cell-cycle shift, explains ~24% of this change |
| [[RKO (line)]] | wt | 77.4 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -14.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 60.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.189× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.328× (z -8.6) |
| [[SW1417 (line)]] | alt | 41.2 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.257× (z -13.3) ⚠ cell-cycle shift, explains ~24% of this change |
| [[SW480 (line)]] | alt | 60.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.580× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 27.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.440× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 60.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -15.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 13.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +12.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[H4 (line)]] | wt | 33.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +10.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HCT15 (line)]] | alt | 32.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.62× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[HEC-1-A (line)]] | alt | 48.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.441× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 44.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +10.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HOP62 (line)]] | alt | 16.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[Hs 766T (line)]] | wt | 13.6 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.194× (z -8.8) |
| [[KATO III (line)]] | alt | 33.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.348× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[LoVo (line)]] | wt | 41.2 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.410× (z -9.4) ⚠ cell-cycle shift, explains ~24% of this change |
| [[NCI-H1573 (line)]] | alt | 92.0 | 1 | 0 | [[Ponatinib (drug)]] 5 µM 2.77× (z +8.9) | — |
| [[NCI-H1792 (line)]] | alt | 85.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -12.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 55.3 | 1 (1 ⚠) | 0 | [[Trametinib (drug)]] 5 µM 3.31× (z +8.7) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[Panc 03.27 (line)]] | alt | 38.0 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.304× (z -10.6) ⚠ transcription drop; cell-cycle shift, explains ~40% of this change |
| [[SK-MEL-2 (line)]] | alt | 49.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.341× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 50.5 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0812× (z -11.8) ⚠ toxic |
| [[A-172 (line)]] | wt | 35.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 73.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 44.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 39.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.93 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 10.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 54.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.36 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 106 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9614), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NSMAF]] | +0.62 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[PTPN4]] | +0.58 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[NFIB]] | +0.57 | +0.66 / +0.43 | both halves | 3e-05 |  |
| [[SLC25A13]] | +0.57 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[TFAP4]] | +0.57 | +0.57 / +0.46 | both halves | 2e-05 |  |
| [[LRRC8D]] | +0.57 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[PPA2]] | +0.56 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[USP13]] | +0.56 | +0.65 / +0.41 | both halves | 4e-05 |  |
| [[TULP4]] | +0.56 | +0.65 / +0.40 | both halves | 5e-05 |  |
| [[BID]] | +0.56 | +0.50 / +0.38 | both halves | 6e-05 |  |
| [[LARP1]] | +0.55 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[MGST1]] | +0.54 | +0.47 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MMUT]] | -0.57 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[GNAI3]] | -0.54 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[NAGK]] | -0.54 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[SWI5]] | -0.54 | -0.54 / -0.35 | both halves | 1e-04 |  |
| [[NDEL1]] | -0.52 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[SENP2]] | -0.52 | -0.51 / -0.29 | both halves | 2e-04 |  |
| [[ZMYM6]] | -0.51 | -0.52 / -0.36 | both halves | 9e-05 |  |
| [[TRIM52]] | -0.51 | -0.37 / -0.48 | both halves | 7e-05 |  |
| [[WASF2]] | -0.51 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[PLXNA3]] | -0.50 | -0.46 / -0.37 | both halves | 7e-05 |  |
| [[SAR1A]] | -0.50 | -0.51 / -0.39 | both halves | 6e-05 |  |
| [[TOX4]] | -0.49 | -0.50 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NFIA]] | B | NFIA activity raises TTC39C's level | lines that do not express NFIA (11) vs lines expressing it (39) | 2.09× lower at baseline in the lines without NFIA | 0.026 | ⚠ within organs, on part of the lines; also absent: CRACD, TSPAN33, PCAT7; maybe low, not absent |
| [[AADAT]] | B | AADAT activity raises TTC39C's level | lines that do not express AADAT (5) vs lines expressing it (45) | 1.92× lower at baseline in the lines without AADAT | 0.073 | ⚠ within organs, on part of the lines; also absent: GGH, LINC01341, HHAT; maybe low, not absent |
| [[TMEM92-AS1]] | B | TMEM92-AS1 activity strengthens TTC39C's drug response | lines that do not express TMEM92-AS1 (14) vs lines expressing it (32) | the lines without TMEM92-AS1 respond 0.72× as strongly (z diff +0.41); strongest at Homoharringtonine 5 µM: 0.75x vs 1.21x (z diff +4.1) | 0.075 | ⚠ within organs, on part of the lines; also absent: CXCL8, SPTLC3, PLOD2; target measured in part of the lines; both ways; the reference differs; artifact flags |
| [[PDE3B]] | B | PDE3B activity raises TTC39C's level | lines that do not express PDE3B (20) vs lines expressing it (30) | 1.64× lower at baseline in the lines without PDE3B | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000250049, MIR4458HG, ASB4 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 143]]; 32 genes; every member is in the + arm (projection on the module's main direction 0.640). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (4.2, -33.1); signed map (25.8, -36.2). **Vector** length 91.0, 19.0% of its response variance represented; |z| ≥ 3 in 921 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.1 | +2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +5.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.3 | +3.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.2 | +7.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~1% of this change | +3.2 | +3.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.8 | +4.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.7 | +3.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.5 | +2.7 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -4.8 | -5.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.4 | -4.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.9 | -3.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -2.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.0 | -2.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.8 | -2.2 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.4 | -2.6 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.4 | -1.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.4 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | tetratricopeptide repeat domain 39C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q11.2 — chr18:23,992,773-24,135,610 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ33761, HsT2697; previously C18orf17 |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing |
| Matched by | ensembl_id |

UniProt [Q8N584](https://www.uniprot.org/uniprotkb/Q8N584) carries no function annotation.

**Summary**, from NCBI Gene [125488](https://www.ncbi.nlm.nih.gov/gene/125488):

> Predicted to be involved in cilium assembly and otolith morphogenesis. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26595](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26595) · Entrez [125488](https://www.ncbi.nlm.nih.gov/gene/125488) · UniProt [Q8N584](https://www.uniprot.org/uniprotkb/Q8N584) · Ensembl [ENSG00000168234](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168234)

## Data

Gene col 9614: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9614); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9614, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9614]; `tensor/DDL_lfc|DDL_z.npy` [9614]; `embed/gene_vectors.npy` [9614]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9614 or target_col == 9614). Every well: [[TTC39C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TTC39C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
