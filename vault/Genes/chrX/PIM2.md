---
symbol: "PIM2"
type: "gene"
col: 2212
ensembl_id: "ENSG00000102096"
name: "Pim-2 proto-oncogene, serine/threonine kinase"
location: "Xp11.23"
module: 59
arm: "+"
pooled_cpm: 12.22
n_lines_expressing: 47
n_dd_up: 14
n_dd_down: 1
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 3
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# PIM2

*Pim-2 proto-oncogene, serine/threonine kinase* — Xp11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.95× (z +9.8, q 5e-20, up in 33 of 43 measured lines) ⚠ cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.65× (z +5.2, q 1e-05, up in 21 of 41 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (CFPAC-1 11.8×, HOP62 9.49×, J82 7.54×, AsPC-1 4.77×, …; ⚠ cell-cycle shift, explains ~39% of this change); [[Harringtonine (drug)]] 5 µM in 4 lines (HOP62 34.5×, CFPAC-1 8.75×, J82 11.0×, RPMI-7951 7.15×; ⚠ cell-cycle shift, explains ~40% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (J82 6.54×, hTERT-HPNE 12.4×, SW 900 5.25×).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.574× (z -5.8, q 4e-06, down in 22 of 30 measured lines) ⚠ toxic; transcription drop.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SW480 0.158×, KATO III 0.139×, SNU-423 0.205×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (SW 900 0.0933×, NCI-H460 0.168×, SNU-423 0.217×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SNU-423 0.117×, HT-29 0.119×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM53C]] (+0.71, fdr 7e-06), [[MYLIP]] (+0.65, fdr 7e-06), [[SLC25A4]] (+0.61, fdr 3e-05); moves opposite to [[NAA50]] (-0.67, fdr 1e-05), [[ZMPSTE24]] (-0.63, fdr 4e-04), [[STMP1]] (-0.57, fdr 2e-04).
> It sits in the **+** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NINJ1]] → it (grade B ⚠); 3 go from it, the strongest it → [[TLE3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 12 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2212.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (CFPAC-1 11.8×, HOP62 9.49×, J82 7.54×, AsPC-1 4.77×, …; ⚠ cell-cycle shift, explains ~39% of this change); [[Harringtonine (drug)]] 5 µM in 4 lines (HOP62 34.5×, CFPAC-1 8.75×, J82 11.0×, RPMI-7951 7.15×; ⚠ cell-cycle shift, explains ~40% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (J82 6.54×, hTERT-HPNE 12.4×, SW 900 5.25×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.95×** | +9.8 | 5e-20 | 33/43 (CFPAC-1, HOP62, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **2.25×** | +8.4 | 9e-15 | 32/45 (SW480, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **2.08×** | +7.6 | 5e-12 | 27/42 (SW 900, HOP62, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **2.03×** | +7.4 | 3e-11 | 30/44 (SW480, A549, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.81×** | +6.1 | 8e-08 | 27/44 (SW480, J82, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.85×** | +6.1 | 8e-08 | 22/43 (HOP62, CFPAC-1, …) | rises with dose | composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.75×** | +5.6 | 2e-06 | 25/36 (J82, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.65×** | +5.2 | 1e-05 | 21/41 (J82, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.62×** | +5.0 | 3e-05 | 24/45 (SW 900, NCI-H2347, …) | rises with dose | composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.65×** | +5.0 | 3e-05 | 21/41 (SW480, J82, …) | top dose only |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.17×** | +4.2 | 0.001 | 10/25 (SW480, J82, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~52% of this change | **1.47×** | +4.0 | 0.003 | 19/39 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.56×** | +3.3 | 0.045 | 13/38 (SHP-77, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.34×** | +3.0 | 0.096 | 13/44 (SW1417, SW480, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2212.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SW480 0.158×, KATO III 0.139×, SNU-423 0.205×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (SW 900 0.0933×, NCI-H460 0.168×, SNU-423 0.217×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SNU-423 0.117×, HT-29 0.119×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.574×** | -5.8 | 4e-06 | 22/30 (SW480, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Adenosine (drug)]] 0.5 µM |  | 0.734× | -3.2 | 0.33 | 9/45 (SW480, SW 1271, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.735× | -3.1 | 0.34 | 11/19 (SW 900, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 0.731× | -3.0 | 0.34 | 16/25 (SNU-423, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2212. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 34.6 | 3 (2 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 5.80× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.25× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.0933× (z -12.3) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 9.76 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.54× (z +13.9) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.54× (z +9.1) | — |
| [[SNU-423 (line)]] | alt | 27.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.117× (z -13.6) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 13.9 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.8× (z +19.7) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[HOP62 (line)]] | alt | 7.57 | 2 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 34.5× (z +15.8) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[AsPC-1 (line)]] | alt | 6.58 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.77× (z +9.5) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[COLO 205 (line)]] | alt | 6.99 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.60× (z +8.7) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[H4 (line)]] | wt | 11.6 | 0 | 1 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.0887× (z -8.9) ⚠ cell-cycle shift, explains ~59% of this change |
| [[HCT15 (line)]] | alt | 17.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -9.2) ⚠ cell-cycle shift, explains ~39% of this change |
| [[HT-29 (line)]] | alt | 11.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.119× (z -9.5) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 9.20 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 12.4× (z +9.0) | — |
| [[KATO III (line)]] | alt | 15.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.139× (z -11.2) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 15.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.168× (z -10.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 11.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +9.5) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[RPMI-7951 (line)]] | alt | 17.9 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 7.15× (z +9.2) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[SW480 (line)]] | alt | 18.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.158× (z -15.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 2.43 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.96 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 6.26 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.40 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.95 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.97 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 6.09 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.42 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.33 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.85 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.90 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2212), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM53C]] | +0.71 | +0.64 / +0.76 | both halves | 7e-06 |  |
| [[MYLIP]] | +0.65 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[SLC25A4]] | +0.61 | +0.44 / +0.68 | both halves | 3e-05 |  |
| [[ING1]] | +0.61 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[CNNM4]] | +0.61 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[POLR2H]] | +0.61 | +0.41 / +0.67 | both halves | 4e-05 |  |
| [[ALDOC]] | +0.60 | +0.36 / +0.70 | both halves | 1e-04 |  |
| [[RBM38]] | +0.59 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[IER5L]] | +0.58 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[FUT11]] | +0.57 | +0.35 / +0.54 | both halves | 1e-04 |  |
| [[CBX4]] | +0.57 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[OCEL1]] | +0.57 | +0.27 / +0.70 | both halves | 3e-04 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAA50]] | -0.67 | -0.57 / -0.68 | both halves | 1e-05 |  |
| [[ZMPSTE24]] | -0.63 | -0.25 / -0.74 | both halves | 4e-04 |  |
| [[STMP1]] | -0.57 | -0.32 / -0.55 | both halves | 2e-04 |  |
| [[TMEM33]] | -0.57 | -0.38 / -0.60 | both halves | 7e-05 |  |
| [[USP39]] | -0.57 | -0.31 / -0.53 | both halves | 2e-04 |  |
| [[MAPK9]] | -0.56 | -0.41 / -0.63 | both halves | 4e-05 |  |
| [[API5]] | -0.56 | -0.39 / -0.62 | both halves | 5e-05 |  |
| [[LARP4]] | -0.55 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[TMX3]] | -0.55 | -0.39 / -0.56 | both halves | 6e-05 |  |
| [[BTBD1]] | -0.54 | -0.30 / -0.61 | both halves | 2e-04 |  |
| [[PTPN11]] | -0.54 | -0.37 / -0.56 | both halves | 9e-05 |  |
| [[EIF3F]] | -0.54 | -0.30 / -0.58 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NINJ1]] | B | NINJ1 activity raises PIM2's level | lines that do not express NINJ1 (5) vs lines expressing it (45) | 1.98× lower at baseline in the lines without NINJ1 | 0.086 | ⚠ within organs, on part of the lines; also absent: FAM102A, ZMIZ1, MBNL2; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TLE3]] | C | PIM2 activity raises TLE3's level | lines that do not express PIM2 (3) vs lines expressing it (47) | 2.40× lower at baseline in the lines without PIM2 | 0.022 | ⚠ few lines (3 vs 47); across organs; also absent: JMJD8, CHD7, CYP2R1; maybe low, not absent |
| [[CDKN2D]] | C | PIM2 activity lowers CDKN2D's level | lines that do not express PIM2 (3) vs lines expressing it (47) | 2.26× higher at baseline in the lines without PIM2 | 0.026 | ⚠ few lines (3 vs 47); across organs; also absent: JMJD8, CHD7, CYP2R1; maybe low, not absent |
| [[STMP1]] | C | PIM2 activity lowers STMP1's level | lines that do not express PIM2 (3) vs lines expressing it (47) | 1.88× higher at baseline in the lines without PIM2 | 0.028 | ⚠ few lines (3 vs 47); across organs; also absent: JMJD8, CHD7, CYP2R1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **+** arm (projection on the module's main direction 0.570). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (31.3, -29.6); signed map (-0.3, 17.6). **Vector** length 80.5, 17.0% of its response variance represented; |z| ≥ 3 in 775 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +2.4 | +9.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | +2.1 | +5.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +2.0 | +1.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +1.9 | +6.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.7 | +2.7 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.7 | +2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +3.3 |
|  | [[Vilanterol (drug)]] 0.5 µM |  | +1.7 | +2.2 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.6 | +2.3 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -8.6 | -5.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -8.3 | -3.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.3 | -3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.3 | -0.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -1.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.9 | -2.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.3 | -2.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.3 | -1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | Pim-2 proto-oncogene, serine/threonine kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.23 — chrX:48,913,182-48,919,024 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | PIM kinase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P1W9](https://www.uniprot.org/uniprotkb/Q9P1W9) (Serine/threonine-protein kinase pim-2):

> Proto-oncogene with serine/threonine kinase activity involved in cell survival and cell proliferation. Exerts its oncogenic activity through: the regulation of MYC transcriptional activity, the regulation of cell cycle progression, the regulation of cap-dependent protein translation and through survival signaling by phosphorylation of a pro-apoptotic protein, BAD. Phosphorylation of MYC leads to an increase of MYC protein stability and thereby an increase transcriptional activity. The …

**Summary**, from NCBI Gene [11040](https://www.ncbi.nlm.nih.gov/gene/11040):

> This gene encodes a protooncogene that acts as a serine/threonine protein kinase. Studies determined the encoded protein functions to prevent apoptosis and to promote cell survival.[provided by RefSeq, Nov 2009]

**Accessions** — [HGNC:8987](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8987) · Entrez [11040](https://www.ncbi.nlm.nih.gov/gene/11040) · UniProt [Q9P1W9](https://www.uniprot.org/uniprotkb/Q9P1W9) · Ensembl [ENSG00000102096](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102096)

## Data

Gene col 2212: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2212); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2212, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2212]; `tensor/DDL_lfc|DDL_z.npy` [2212]; `embed/gene_vectors.npy` [2212]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2212 or target_col == 2212). Every well: [[PIM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIM2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
