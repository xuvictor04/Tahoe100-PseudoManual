---
symbol: "CHD1-DT"
type: "gene"
col: 14543
ensembl_id: "ENSG00000248489"
name: "CHD1 divergent transcript"
location: "5q21.1"
module: 23
arm: "+"
pooled_cpm: 10.97
n_lines_expressing: 50
n_dd_up: 35
n_dd_down: 12
n_dd_up_clean: 31
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# CHD1-DT

*CHD1 divergent transcript* — 5q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.25× (z +22.4, q 0e+00, up in 44 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.467× (z -6.6, q 2e-08, down in 28 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.543× (z -5.3, q 2e-05, down in 26 of 47 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKRD17-DT]] (+0.89, fdr 7e-06), [[PRANCR]] (+0.87, fdr 7e-06), [[RFX3-DT]] (+0.85, fdr 7e-06).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[DDX59-AS1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[PPP1R3F]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14543.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.25×** | +22.4 | 0e+00 | 44/44 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.99×** | +11.5 | 5e-28 | 39/44 (SW480, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.41×** | +10.7 | 1e-24 | 41/48 (NCI-H2347, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.13×** | +9.8 | 1e-20 | 38/44 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.10×** | +9.0 | 2e-17 | 35/45 (LoVo, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.69×** | +8.5 | 1e-15 | 39/47 (HT-29, A-172, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.58×** | +7.8 | 4e-13 | 33/46 (HT-29, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.33×** | +7.0 | 2e-10 | 28/39 (NCI-H1573, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **2.04×** | +6.2 | 5e-08 | 36/48 (KATO III, A-172, …) | rises with dose | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.79×** | +4.6 | 2e-04 | 24/48 (SW480, LoVo, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.42×** | +4.2 | 0.002 | 12/48 (MIA PaCa-2, SW480, …) | all doses, flat |  |
| [[GSK1059615 (drug)]] 5 µM |  | **2.48×** | +4.1 | 0.002 | 22/46 (A-172, HCT15, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.61×** | +4.1 | 0.002 | 19/47 (C32, HOP62, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.60×** | +4.1 | 0.002 | 19/47 (LoVo, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.59×** | +4.0 | 0.003 | 21/48 (NCI-H460, A498, …) | top dose only |  |
| [[Bimiralisib (drug)]] 5 µM |  | **2.25×** | +3.7 | 0.008 | 16/47 (NCI-H2347, HS-578T, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14543.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.467×** | -6.6 | 2e-08 | 28/44 (H4, KATO III, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **0.509×** | -5.6 | 5e-06 | 25/41 (COLO 205, NCI-H23, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.543×** | -5.3 | 2e-05 | 26/47 (HS-578T, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.561×** | -5.0 | 7e-05 | 25/48 (LoVo, NCI-H460, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.350×** | -4.8 | 2e-04 | 27/48 (NCI-H23, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.607×** | -4.3 | 0.001 | 20/44 (LOX-IMVI, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.612×** | -4.3 | 0.002 | 24/47 (PANC-1, HepG2/C3A, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.658×** | -3.7 | 0.018 | 17/47 (PANC-1, NCI-H23, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.666×** | -3.5 | 0.023 | 20/48 (BT-474, HT-29, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **0.666×** | -3.5 | 0.023 | 20/48 (PANC-1, KATO III, …) | rises with dose | composition shift; position effect removed |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.676×** | -3.3 | 0.053 | 9/47 (RPMI-7951, PANC-1, …) | top dose only | plate-row cell shift |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **0.779×** | -3.1 | 0.093 | 8/48 (NCI-H661, SW 900, …) | all doses, flat | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | 0.515× | -3.0 | 0.11 | 9/46 (NCI-H460, NCI-H1792, …) | rises with dose | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.39 per unit of S-phase module lfc, -0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14543. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 12.9 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.73× (z +10.9) | [[Digitoxin (drug)]] 5 µM 0.140× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[LoVo (line)]] | wt | 12.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.86× (z +15.0) | — |
| [[A-172 (line)]] | wt | 15.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.33× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.112× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 8.07 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0625× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.0640× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 9.41 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.88× (z +12.4) | [[Docetaxel (drug)]] 0.05 µM 0.0985× (z -9.4) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 15.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.18× (z +10.5) | [[Docetaxel (drug)]] 0.05 µM 0.0822× (z -8.9) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 8.15 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.93× (z +9.5) | [[Orlistat (drug)]] 0.05 µM 0.0738× (z -10.2) |
| [[HOP62 (line)]] | alt | 17.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.88× (z +11.8) | — |
| [[HS-578T (line)]] | alt | 13.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.40× (z +12.5) | — |
| [[HT-29 (line)]] | alt | 9.66 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.22× (z +13.4) | — |
| [[J82 (line)]] | alt | 5.84 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.38× (z +11.5) | [[Pemetrexed (drug)]] 5 µM 0.0805× (z -9.4) |
| [[LOX-IMVI (line)]] | wt | 7.16 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.32× (z +11.1) | [[Belinostat (drug)]] 0.5 µM 0.0625× (z -10.4) |
| [[MIA PaCa-2 (line)]] | alt | 9.77 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.0× (z +13.1) | — |
| [[NCI-H1573 (line)]] | alt | 17.6 | 2 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 6.49× (z +9.6) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.46× (z +9.4) | — |
| [[NCI-H2030 (line)]] | alt | 7.43 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.89× (z +11.0) | [[Bestatin (drug)]] 0.05 µM 0.0820× (z -8.8) |
| [[RKO (line)]] | wt | 6.41 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.81× (z +10.1) | [[Pexidartinib (hydrochloride) (drug)]] 5 µM 0.0549× (z -8.8) |
| [[SW480 (line)]] | alt | 10.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.44× (z +14.3) | — |
| [[A549 (line)]] | wt | 6.18 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.43× (z +11.0) | — |
| [[AsPC-1 (line)]] | alt | 10.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.2× (z +13.9) | — |
| [[C-33 A (line)]] | alt | 12.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.59× (z +10.0) | — |
| [[C32 (line)]] | wt | 13.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.86× (z +10.1) | — |
| [[COLO 205 (line)]] | alt | 12.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.36× (z +9.0) | — |
| [[H4 (line)]] | wt | 23.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0701× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[HepG2_C3A (line)]] | wt | 10.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.40× (z +9.5) | — |
| [[Hs 766T (line)]] | wt | 10.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.46× (z +11.5) | — |
| [[hTERT-HPNE (line)]] | wt | 12.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.07× (z +9.8) | — |
| [[LS 180 (line)]] | wt | 7.60 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.68× (z +10.2) | — |
| [[NCI-H23 (line)]] | alt | 13.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.89× (z +10.1) | — |
| [[NCI-H2347 (line)]] | alt | 8.48 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.16× (z +13.4) | — |
| [[NCI-H460 (line)]] | wt | 11.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.89× (z +12.0) | — |
| [[Panc 03.27 (line)]] | alt | 7.16 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.9× (z +12.4) | — |
| [[PANC-1 (line)]] | alt | 15.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.45× (z +14.0) | — |
| [[RPMI-7951 (line)]] | alt | 12.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.78× (z +9.0) | — |
| [[SHP-77 (line)]] | alt | 5.08 | 0 | 1 | — | [[Ranolazine (drug)]] 0.5 µM 0.0505× (z -9.4) |
| [[SK-MEL-2 (line)]] | alt | 16.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.90× (z +10.7) | — |
| [[SNU-423 (line)]] | alt | 10.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.09× (z +11.9) | — |
| [[SW 900 (line)]] | alt | 8.17 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.22× (z +9.9) | — |
| [[SW1417 (line)]] | alt | 4.47 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.5× (z +11.9) | — |
| [[A-427 (line)]] | wt | 7.43 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.62 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.17 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.89 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.47 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14543), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD17-DT]] | +0.89 | +0.89 / +0.76 | both halves | 7e-06 | same gene group |
| [[PRANCR]] | +0.87 | +0.84 / +0.72 | both halves | 7e-06 |  |
| [[RFX3-DT]] | +0.85 | +0.87 / +0.62 | both halves | 7e-06 | same gene group |
| [[PPP1R12A-AS2]] | +0.84 | +0.85 / +0.55 | both halves | 1e-05 |  |
| [[INTS6-AS1]] | +0.84 | +0.84 / +0.60 | both halves | 7e-06 |  |
| [[PKN2-AS1]] | +0.84 | +0.83 / +0.58 | both halves | 7e-06 |  |
| [[MAD2L1-DT]] | +0.83 | +0.81 / +0.56 | both halves | 1e-05 | same gene group |
| [[OXA1L-DT]] | +0.83 | +0.83 / +0.57 | both halves | 1e-05 | same gene group |
| [[DNAI4]] | +0.83 | +0.84 / +0.62 | both halves | 7e-06 |  |
| [[HEXIM2-AS1]] | +0.82 | +0.76 / +0.67 | both halves | 7e-06 |  |
| [[TMEM202-AS1]] | +0.82 | +0.85 / +0.42 | both halves | 4e-05 |  |
| [[TAS2R4]] | +0.82 | +0.83 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DDX59-AS1]] | B | DDX59-AS1 activity raises CHD1-DT's level | lines that do not express DDX59-AS1 (6) vs lines expressing it (44) | 1.58× lower at baseline in the lines without DDX59-AS1 | 0.007 | ⚠ within organs, on part of the lines; also absent: LTBP4; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers CHD1-DT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PPP1R3F]] | C | CHD1-DT's natural level strengthens PPP1R3F's drug response | CHD1-DT's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.17; direction not clear | 0.096 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.876). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (5.0, 16.6); signed map (26.3, -8.2). **Vector** length 109, 28.8% of its response variance represented; |z| ≥ 3 in 1,252 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.5 | +9.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.8 | +8.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.7 | +22.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +11.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.2 | +10.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.3 | +3.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.4 | +4.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | +6.2 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -8.6 | -2.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -7.9 | -0.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -7.1 | +0.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -7.0 | -4.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -6.8 | -2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.9 | -0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | +0.7 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.3 | -2.8 |
|  | [[Brivudine (drug)]] 0.5 µM |  | -2.1 | -1.4 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -2.1 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | CHD1 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 5q21.1 — chr5:98,929,163-98,995,013 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously LINC02062 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:52907](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:52907) · Entrez [102724810](https://www.ncbi.nlm.nih.gov/gene/102724810) · Ensembl [ENSG00000248489](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000248489)

## Data

Gene col 14543: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14543); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14543, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14543]; `tensor/DDL_lfc|DDL_z.npy` [14543]; `embed/gene_vectors.npy` [14543]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14543 or target_col == 14543). Every well: [[CHD1-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHD1-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
