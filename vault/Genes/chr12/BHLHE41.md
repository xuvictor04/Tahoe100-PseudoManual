---
symbol: "BHLHE41"
type: "gene"
col: 4399
ensembl_id: "ENSG00000123095"
name: "basic helix-loop-helix family member e41"
location: "12p12.1"
module: 14
arm: "+"
pooled_cpm: 35.72
n_lines_expressing: 31
n_dd_up: 12
n_dd_down: 23
n_dd_up_clean: 10
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 3
direction_downstream: 12
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# BHLHE41

*basic helix-loop-helix family member e41* — 12p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 8.85× (z +34.6, q 0e+00, up in 29 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (10 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.571× (z -6.3, q 2e-07, down in 22 of 28 measured lines) ⚠ cell-cycle shift, explains ~49% of this change. The strongest without an alert is [[Vinblastine (sulfate) (drug)]] 0.5 µM: 0.651× (z -4.8, q 3e-04, down in 17 of 27 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BCOR]] (+0.74, fdr 7e-06), [[TEF]] (+0.68, fdr 7e-06), [[SYNPO]] (+0.67, fdr 7e-06); moves opposite to [[DIP2A]] (-0.70, fdr 7e-06), [[VKORC1L1]] (-0.63, fdr 7e-06), [[PPHLN1]] (-0.59, fdr 1e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[SYNPO]] → it (grade B ⚠); 12 go from it, the strongest it → [[FOSL2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4399.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **8.85×** | +34.6 | 0e+00 | 29/29 (A498, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **13.7×** | +28.3 | 0e+00 | 29/29 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.91×** | +17.9 | 0e+00 | 26/29 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **3.80×** | +15.0 | 0e+00 | 28/29 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[TAK-901 (drug)]] 5 µM |  | **7.65×** | +11.9 | 8e-31 | 29/29 (MIA PaCa-2, HOP62, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.52×** | +6.7 | 2e-09 | 13/29 (SW480, CFPAC-1, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.56×** | +5.0 | 5e-05 | 9/25 (SW480, KATO III, …) | inconsistent across doses | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.49×** | +4.5 | 5e-04 | 16/29 (A-172, A498, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.50×** | +4.2 | 0.002 | 8/25 (SW480, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~5% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.89×** | +3.7 | 0.010 | 13/28 (HOP62, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.35×** | +3.4 | 0.033 | 10/29 (SW480, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Entrectinib (drug)]] 5 µM |  | **1.32×** | +3.1 | 0.081 | 12/28 (SK-MEL-2, Panc 03.27, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 10 with an alert ⚠. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4399.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.571×** | -6.3 | 2e-07 | 22/28 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.651×** | -4.8 | 3e-04 | 17/27 (NCI-H1573, HT-29, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.653×** | -4.8 | 3e-04 | 20/29 (HOP62, NCI-H1792, …) | rises with dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.644×** | -4.7 | 3e-04 | 19/27 (SNU-423, MIA PaCa-2, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~56% of this change | **0.651×** | -4.6 | 4e-04 | 17/27 (LoVo, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.625×** | -4.5 | 7e-04 | 21/29 (PANC-1, HOP62, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.672×** | -4.4 | 7e-04 | 17/28 (NCI-H1573, NCI-H23, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.758×** | -4.4 | 8e-04 | 19/29 (PANC-1, Panc 03.27, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.685×** | -4.2 | 0.002 | 14/28 (LoVo, MIA PaCa-2, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.689×** | -4.2 | 0.002 | 18/29 (HOP62, SNU-423, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~48% of this change | **0.497×** | -4.1 | 0.002 | 16/26 (NCI-H1792, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.502×** | -4.0 | 0.003 | 18/29 (SK-MEL-2, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.698×** | -4.0 | 0.003 | 12/29 (LoVo, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.525×** | -3.8 | 0.006 | 12/21 (SW 900, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.714×** | -3.8 | 0.006 | 13/29 (NCI-H460, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.731×** | -3.5 | 0.017 | 16/29 (NCI-H460, SW 900, …) | rises with dose |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.737×** | -3.4 | 0.022 | 14/28 (J82, LOX-IMVI, …) | inconsistent across doses | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.735×** | -3.3 | 0.030 | 13/28 (NCI-H460, C32, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.745×** | -3.3 | 0.030 | 16/29 (HOP62, C32, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.746×** | -3.3 | 0.030 | 14/28 (NCI-H1792, NCI-H1573, …) | top dose only |  |
| [[Megestrol (drug)]] 5 µM |  | **0.813×** | -3.3 | 0.031 | 15/29 (SW480, A498, …) | top dose only |  |
| [[BAY1125976 (drug)]] 5 µM |  | **0.585×** | -3.1 | 0.045 | 8/29 (LoVo, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.604×** | -2.9 | 0.079 | 15/29 (NCI-H1792, HOP62, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, +0.83 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4399. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 197 | 4 | 8 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.70× (z +24.5) | [[Panobinostat (drug)]] 5 µM 0.253× (z -11.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.269× (z -11.1) |
| [[LoVo (line)]] | wt | 72.7 | 4 | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.52× (z +15.1) | [[Digitoxin (drug)]] 0.5 µM 0.178× (z -12.1) |
| [[SW480 (line)]] | alt | 14.1 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 19.8× (z +26.3) | — |
| [[PANC-1 (line)]] | alt | 115 | 5 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.06× (z +25.4) | [[Ixazomib citrate (drug)]] 5 µM 0.369× (z -10.0) ⚠ cell-cycle shift, explains ~49% of this change |
| [[MIA PaCa-2 (line)]] | alt | 33.1 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 11.0× (z +24.2) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.237× (z -9.9) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H1573 (line)]] | alt | 42.2 | 5 | 1 | [[Homoharringtonine (drug)]] 5 µM 9.59× (z +22.2) | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.287× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 31.0 | 4 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.95× (z +15.0) | [[Ixazomib citrate (drug)]] 5 µM 0.215× (z -10.2) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.266× (z -8.8) |
| [[A-172 (line)]] | wt | 16.5 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 36.6× (z +27.2) | — |
| [[A498 (line)]] | wt | 34.3 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.0× (z +34.5) | — |
| [[NCI-H1792 (line)]] | alt | 74.8 | 3 | 2 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 12.0× (z +15.6) | [[Bortezomib (drug)]] 5 µM 0.0530× (z -10.0) ⚠ toxic; cell-cycle shift, explains ~48% of this change |
| [[NCI-H23 (line)]] | alt | 73.8 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.31× (z +19.9) | [[Niclosamide (olamine) (drug)]] 5 µM 0.269× (z -9.6) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 28.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.7× (z +22.2) | — |
| [[hTERT-HPNE (line)]] | wt | 29.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.1× (z +17.9) | — |
| [[KATO III (line)]] | alt | 34.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.9× (z +28.8) | — |
| [[SW 900 (line)]] | alt | 44.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.94× (z +17.7) | — |
| [[CFPAC-1 (line)]] | alt | 14.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.0× (z +20.6) | — |
| [[H4 (line)]] | wt | 31.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.5× (z +15.7) | — |
| [[J82 (line)]] | alt | 12.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.6× (z +23.2) | — |
| [[Panc 03.27 (line)]] | alt | 27.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.5× (z +20.1) | — |
| [[SNU-423 (line)]] | alt | 96.9 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.89× (z +20.0) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.183× (z -11.3) ⚠ cell-cycle shift, explains ~32% of this change |
| [[COLO 205 (line)]] | alt | 12.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 57.4× (z +22.4) | — |
| [[HT-29 (line)]] | alt | 52.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.54× (z +20.0) | — |
| [[RPMI-7951 (line)]] | alt | 37.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.21× (z +14.6) | — |
| [[C32 (line)]] | wt | 45.8 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.144× (z -9.3) |
| [[HCT15 (line)]] | alt | 9.42 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.4× (z +13.6) | — |
| [[SK-MEL-2 (line)]] | alt | 63.3 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 5.15× (z +10.1) | — |
| [[A-427 (line)]] | wt | 2.39 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.71 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.06 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.46 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.27 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 6.51 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 7.39 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.92 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.58 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 6.92 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.11 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 7.76 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.53 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.43 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.84 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.20 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.07 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.16 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.32 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4399), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCOR]] | +0.74 | +0.68 / +0.75 | both halves | 7e-06 |  |
| [[TEF]] | +0.68 | +0.69 / +0.64 | both halves | 7e-06 | STRING 534 |
| [[SYNPO]] | +0.67 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[KLF10]] | +0.67 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[PER2]] | +0.64 | +0.55 / +0.66 | both halves | 1e-05 | pathway: Circadian clock; STRING 999 |
| [[ZFHX2]] | +0.64 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[MIDEAS]] | +0.63 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[BCL9L]] | +0.63 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[RBMS3]] | +0.63 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[BCL3]] | +0.63 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[CLK4]] | +0.63 | +0.57 / +0.64 | both halves | 9e-06 |  |
| [[COQ5]] | +0.62 | +0.63 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DIP2A]] | -0.70 | -0.63 / -0.70 | both halves | 7e-06 |  |
| [[VKORC1L1]] | -0.63 | -0.62 / -0.60 | both halves | 7e-06 |  |
| [[PPHLN1]] | -0.59 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[ZNF731P]] | -0.59 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[GPR89A]] | -0.59 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[COP1]] | -0.59 | -0.58 / -0.58 | both halves | 7e-06 |  |
| [[TRMT2B]] | -0.58 | -0.65 / -0.50 | both halves | 1e-05 |  |
| [[NAP1L4]] | -0.58 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[TMPRSS5]] | -0.57 | -0.46 / -0.56 | both halves | 2e-05 |  |
| [[NTAQ1]] | -0.57 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[ADPGK]] | -0.56 | -0.57 / -0.46 | both halves | 3e-05 |  |
| [[FAM20B]] | -0.56 | -0.55 / -0.60 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SYNPO]] | B | SYNPO activity raises BHLHE41's level | lines that do not express SYNPO (15) vs lines expressing it (35) | 2.87× lower at baseline in the lines without SYNPO | 0.047 | ⚠ within organs, on part of the lines; also absent: GLIS3, ENSG00000261227, ADAM7-AS1; maybe low, not absent |
| [[NALCN]] | B | NALCN activity raises BHLHE41's level | lines that do not express NALCN (22) vs lines expressing it (28) | 2.66× lower at baseline in the lines without NALCN | 0.060 | ⚠ within organs, on part of the lines; also absent: STAC, EDIL3-DT, ZNF229 |
| [[SNAP25]] | C | SNAP25 activity raises BHLHE41's level | lines that do not express SNAP25 (26) vs lines expressing it (24) | 2.57× lower at baseline in the lines without SNAP25 | 0.087 | ⚠ within organs, on part of the lines; also absent: EYA4, SPOCK1, DPYSL3; co-absent with the target |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 10, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FOSL2]] | B | BHLHE41 activity raises FOSL2's level | lines that do not express BHLHE41 (19) vs lines expressing it (31) | 1.55× lower at baseline in the lines without BHLHE41 | 0.010 | ⚠ within organs, on part of the lines; also absent: RAC2, JHY, ENSG00000289600 |
| [[LMLN]] | B | BHLHE41 activity raises LMLN's level | lines that do not express BHLHE41 (19) vs lines expressing it (31) | 1.80× lower at baseline in the lines without BHLHE41 | 0.014 | ⚠ within organs, on part of the lines; also absent: RAC2, JHY, ENSG00000289600 |
| [[SLC27A4]] | B | BHLHE41 activity lowers SLC27A4's level | lines that do not express BHLHE41 (19) vs lines expressing it (31) | 1.35× higher at baseline in the lines without BHLHE41 | 0.018 | ⚠ within organs, on part of the lines; also absent: RAC2, JHY, ENSG00000289600 |
| [[AHSA1]] | B | BHLHE41 activity lowers AHSA1's level | lines that do not express BHLHE41 (19) vs lines expressing it (31) | 1.37× higher at baseline in the lines without BHLHE41 | 0.028 | ⚠ within organs, on part of the lines; also absent: RAC2, JHY, ENSG00000289600 |
| [[SMG1P5]] | B | BHLHE41 activity lowers SMG1P5's level | lines that do not express BHLHE41 (19) vs lines expressing it (31) | 1.20× higher at baseline in the lines without BHLHE41 | 0.030 | ⚠ within organs, on part of the lines; also absent: RAC2, JHY, ENSG00000289600 |
| [[ATP7A]] | B | BHLHE41 activity raises ATP7A's level | lines that do not express BHLHE41 (19) vs lines expressing it (31) | 1.30× lower at baseline in the lines without BHLHE41 | 0.039 | ⚠ within organs, on part of the lines; also absent: RAC2, JHY, ENSG00000289600 |
| [[DPY19L2P2]] | B | BHLHE41 activity raises DPY19L2P2's level | lines that do not express BHLHE41 (19) vs lines expressing it (31) | 1.77× lower at baseline in the lines without BHLHE41 | 0.039 | ⚠ within organs, on part of the lines; also absent: RAC2, JHY, ENSG00000289600 |
| [[MAVS]] | B | BHLHE41 activity raises MAVS's level | lines that do not express BHLHE41 (19) vs lines expressing it (31) | 1.19× lower at baseline in the lines without BHLHE41 | 0.069 | ⚠ within organs, on part of the lines; also absent: RAC2, JHY, ENSG00000289600 |
| cells under [[Pentoxifylline (drug)]] 0.5 µM | B | BHLHE41 activity raises the cells' numbers under Pentoxifylline 0.5 µM (protects the cells) | lines that do not express BHLHE41 (19) vs lines expressing it (29) | the lines without BHLHE41: 0.83× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: RAC2, JHY, ENSG00000289600 |
| [[VKORC1L1]] | B | BHLHE41 activity lowers VKORC1L1's level | lines that do not express BHLHE41 (19) vs lines expressing it (31) | 1.22× higher at baseline in the lines without BHLHE41 | 0.099 | ⚠ within organs, on part of the lines; also absent: RAC2, JHY, ENSG00000289600 |
| [[SLFN11]] | C | BHLHE41 activity raises SLFN11's level | lines that do not express BHLHE41 (19) vs lines expressing it (31) | 4.34× lower at baseline in the lines without BHLHE41 | 0.011 | ⚠ within organs, on part of the lines; also absent: RAC2, JHY, ENSG00000289600; co-absent with the target |
| [[POGZ]] | C | BHLHE41 activity weakens POGZ's drug response | lines that do not express BHLHE41 (19) vs lines expressing it (31) | the lines without BHLHE41 respond 1.06× as strongly (z diff -0.95); rises at some drug-doses, falls at others (68% from rises): Homoharringtonine 5 µM: 1.71x vs 1.40x (z diff -3.1); Harringtonine 5 µM: 1.66x vs 1.47x (z diff -1.8); Doxorubicin (hydrochloride) 5 µM: 0.58x vs 0.53x (z diff -1.1) | 0.050 | ⚠ within organs, on part of the lines; also absent: RAC2, JHY, ENSG00000289600; rises at some drug-doses, falls at others; rests on the correction; artifact flags |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.639). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.1, 5.0); signed map (28.7, 7.6). **Vector** length 115, 34.8% of its response variance represented; |z| ≥ 3 in 903 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.9 | +34.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.8 | +28.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.3 | +17.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.7 | +15.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.2 | +11.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.8 | +4.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +6.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.9 | +2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.8 | +3.7 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | +2.2 | +1.9 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | -5.7 | -6.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~57% of this change | -5.4 | -4.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -5.0 | -4.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.6 | -3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.2 | -4.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -4.2 | -4.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.5 | -4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.2 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | basic helix-loop-helix family member e41 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p12.1 — chr12:26,120,030-26,125,037 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DEC2, SHARP-1, SHARP1; previously BHLHB3 |
| Gene groups (HGNC) | Basic helix-loop-helix proteins |
| Reactome | 2 pathways, smallest: BMAL1:CLOCK,NPAS2 activates circadian expression; Circadian clock |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9C0J9](https://www.uniprot.org/uniprotkb/Q9C0J9) (Class E basic helix-loop-helix protein 41):

> Transcriptional repressor involved in the regulation of the circadian rhythm by negatively regulating the activity of the clock genes and clock-controlled genes. Acts as the negative limb of a novel autoregulatory feedback loop (DEC loop) which differs from the one formed by the PER and CRY transcriptional repressors (PER/CRY loop). Both these loops are interlocked as it represses the expression of PER1 and in turn is repressed by PER1/2 and CRY1/2. Represses the activity of the circadian …

**Summary**, from NCBI Gene [79365](https://www.ncbi.nlm.nih.gov/gene/79365):

> This gene encodes a basic helix-loop-helix protein expressed in various tissues. The encoded protein can interact with ARNTL or compete for E-box binding sites in the promoter of PER1 and repress CLOCK/ARNTL's transactivation of PER1. This gene is believed to be involved in the control of circadian rhythm and cell differentiation. Defects in this gene are associated with the short sleep phenotype. [provided by RefSeq, Feb 2014]

**Accessions** — [HGNC:16617](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16617) · Entrez [79365](https://www.ncbi.nlm.nih.gov/gene/79365) · UniProt [Q9C0J9](https://www.uniprot.org/uniprotkb/Q9C0J9) · Ensembl [ENSG00000123095](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123095)

## Data

Gene col 4399: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4399); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4399, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4399]; `tensor/DDL_lfc|DDL_z.npy` [4399]; `embed/gene_vectors.npy` [4399]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4399 or target_col == 4399). Every well: [[BHLHE41 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BHLHE41.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
