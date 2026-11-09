---
symbol: "ZSCAN5A"
type: "gene"
col: 5252
ensembl_id: "ENSG00000131848"
name: "zinc finger and SCAN domain containing 5A"
location: "19q13.43"
module: 45
arm: "-"
pooled_cpm: 40.65
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 26
n_dd_up_clean: 2
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# ZSCAN5A

*zinc finger and SCAN domain containing 5A* — 19q13.43

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Filgotinib (drug)]] 5 µM: 1.37× (z +4.0, q 0.038, up in 30 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 1 line (SK-MEL-2 3.90×); [[Panobinostat (drug)]] 0.5 µM in 1 line (SK-MEL-2 3.44×; ⚠ cell-cycle shift, explains ~87% of this change).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (14 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.356× (z -12.4, q 1e-32, down in 40 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.250× (z -9.1, q 2e-17, down in 45 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[INO80]] (+0.59, fdr 1e-05), [[TAF2]] (+0.59, fdr 1e-05), [[EPC2]] (+0.58, fdr 1e-05); moves opposite to [[LNX2]] (-0.59, fdr 1e-05), [[RCOR3]] (-0.58, fdr 1e-05), [[PXK]] (-0.55, fdr 1e-05).
> It sits in the **-** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[JAK2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5252.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 1 line (SK-MEL-2 3.90×); [[Panobinostat (drug)]] 0.5 µM in 1 line (SK-MEL-2 3.44×; ⚠ cell-cycle shift, explains ~87% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Filgotinib (drug)]] 5 µM |  | **1.37×** | +4.0 | 0.038 | 30/48 (PANC-1, A-172, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.36×** | +3.8 | 0.038 | 25/48 (NCI-H460, MIA PaCa-2, …) | top dose only |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | 1.31× | +3.2 | 0.24 | 17/48 (NCI-H1792, HT-29, …) | top dose only | plate-row cell shift |
| [[Demeclocycline (drug)]] 5 µM |  | 1.19× | +3.1 | 0.26 | 10/48 (A-427, RPMI-7951, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5252.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.356×** | -12.4 | 1e-32 | 40/47 (SHP-77, LoVo, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.421×** | -10.8 | 1e-24 | 41/48 (PANC-1, HT-29, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.480×** | -9.2 | 9e-18 | 37/48 (PANC-1, KATO III, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.250×** | -9.1 | 2e-17 | 45/49 (PANC-1, RPMI-7951, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.513×** | -8.0 | 1e-13 | 38/48 (RPMI-7951, hTERT-HPNE, …) | rises with dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.524×** | -7.8 | 8e-13 | 33/48 (C-33 A, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.660×** | -7.4 | 2e-11 | 33/48 (SHP-77, CHP-212, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **0.671×** | -7.1 | 1e-10 | 32/47 (SNU-423, Panc 03.27, …) | rises with dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.592×** | -6.3 | 2e-08 | 33/48 (SNU-1, NCI-H23, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.628×** | -5.8 | 4e-07 | 32/48 (MIA PaCa-2, A549, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.443×** | -5.3 | 5e-06 | 29/48 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change | **0.671×** | -5.0 | 3e-05 | 26/47 (LoVo, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.685×** | -4.7 | 1e-04 | 27/47 (NCI-H1792, A549, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~64% of this change | **0.704×** | -4.4 | 5e-04 | 24/46 (PANC-1, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.709×** | -4.3 | 6e-04 | 27/48 (NCI-H1792, LoVo, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.717×** | -4.2 | 0.001 | 27/48 (RPMI-7951, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.732×** | -3.9 | 0.003 | 30/48 (HS-578T, RPMI-7951, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.813×** | -3.7 | 0.007 | 22/48 (NCI-H1792, LoVo, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | **0.813×** | -3.6 | 0.007 | 23/48 (NCI-H2030, PANC-1, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.814×** | -3.6 | 0.007 | 18/48 (HT-29, NCI-H1573, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.760×** | -3.2 | 0.029 | 24/48 (SW 1271, AN3 CA, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5252. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 94.7 | 0 | 9 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0651× (z -20.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.256× (z -10.2) |
| [[PANC-1 (line)]] | alt | 63.2 | 0 | 8 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.103× (z -21.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.116× (z -10.5) |
| [[RPMI-7951 (line)]] | alt | 68.2 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.206× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.225× (z -10.9) |
| [[C-33 A (line)]] | alt | 113 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.109× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.190× (z -12.5) |
| [[HT-29 (line)]] | alt | 60.3 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.188× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[KATO III (line)]] | alt | 42.3 | 0 | 4 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.151× (z -13.6) ⚠ cell-cycle shift, explains ~35% of this change |
| [[NCI-H1573 (line)]] | alt | 43.2 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.207× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[NCI-H460 (line)]] | wt | 35.2 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.241× (z -11.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -9.4) |
| [[A-427 (line)]] | wt | 60.4 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.207× (z -13.1) ⚠ toxic · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.210× (z -13.0) |
| [[A549 (line)]] | wt | 46.9 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.215× (z -9.7) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.253× (z -9.1) |
| [[LS 180 (line)]] | wt | 24.3 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.216× (z -10.5) ⚠ cell-cycle shift, explains ~79% of this change |
| [[MIA PaCa-2 (line)]] | alt | 39.0 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.159× (z -12.0) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.179× (z -11.7) |
| [[NCI-H1792 (line)]] | alt | 48.2 | 0 | 3 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.281× (z -9.6) ⚠ cell-cycle shift, explains ~41% of this change |
| [[SK-MEL-2 (line)]] | alt | 52.1 | 2 (1 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.90× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.301× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 48.9 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0404× (z -19.0) |
| [[SW480 (line)]] | alt | 52.2 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.277× (z -12.7) ⚠ cell-cycle shift, explains ~35% of this change |
| [[CHP-212 (line)]] | wt | 46.2 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.156× (z -10.5) |
| [[COLO 205 (line)]] | alt | 53.0 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.153× (z -13.1) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 32.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.255× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.278× (z -9.9) |
| [[LoVo (line)]] | wt | 48.1 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.135× (z -16.3) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 70.5 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.138× (z -17.2) |
| [[SHP-77 (line)]] | alt | 47.2 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0947× (z -17.8) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -11.8) |
| [[SNU-423 (line)]] | alt | 38.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -13.6) ⚠ cell-cycle shift, explains ~83% of this change |
| [[SW48 (line)]] | wt | 49.9 | 0 | 2 (1 ⚠) | — | [[Hesperidin (drug)]] 5 µM 0.147× (z -10.4) |
| [[A-172 (line)]] | wt | 31.4 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0573× (z -9.8) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 51.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.160× (z -11.0) ⚠ toxic |
| [[HOP62 (line)]] | alt | 32.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.286× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[hTERT-HPNE (line)]] | wt | 35.4 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.171× (z -9.9) ⚠ cell-cycle shift, explains ~42% of this change |
| [[J82 (line)]] | alt | 27.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.215× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[LOX-IMVI (line)]] | wt | 46.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.423× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 32.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0937× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 27.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -10.6) ⚠ cell-cycle shift, explains ~83% of this change |
| [[RKO (line)]] | wt | 30.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.243× (z -8.6) ⚠ toxic |
| [[SW1417 (line)]] | alt | 29.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -9.6) ⚠ cell-cycle shift, explains ~83% of this change |
| [[A498 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 62.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 35.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5252), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INO80]] | +0.59 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[TAF2]] | +0.59 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[EPC2]] | +0.58 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[RRP7BP-1]] | +0.58 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[PIGL]] | +0.58 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[RABL3]] | +0.57 | +0.58 / +0.57 | both halves | 8e-06 |  |
| [[WARS2]] | +0.57 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[COMMD10]] | +0.57 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[PPP1R10]] | +0.56 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[NCOA5]] | +0.56 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[THADA]] | +0.56 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[TTC27]] | +0.55 | +0.52 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LNX2]] | -0.59 | -0.54 / -0.65 | both halves | 1e-05 |  |
| [[RCOR3]] | -0.58 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[PXK]] | -0.55 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[USP33]] | -0.55 | -0.51 / -0.60 | both halves | 1e-05 |  |
| [[RAB12]] | -0.54 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[TBC1D12]] | -0.53 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[PPP2R5A]] | -0.53 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[PPTC7]] | -0.52 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[MANBA]] | -0.52 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[DRAM2]] | -0.52 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[EPB41L4B]] | -0.51 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[RREB1]] | -0.50 | -0.56 / -0.41 | both halves | 4e-05 | same gene group |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[JAK2]] | B | JAK2 activity lowers ZSCAN5A's level | compounds that target JAK2: 2 of 3 raise it (Fedratinib, Filgotinib) | 67% of the class's compounds vs 0.6% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **-** arm (projection on the module's main direction -0.465). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (3.3, -25.0); signed map (13.0, -30.8). **Vector** length 91.1, 24.2% of its response variance represented; |z| ≥ 3 in 1,113 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.9 | -1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.4 | -1.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.3 | +1.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +2.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +4.1 | -4.7 |
|  | [[EX229 (drug)]] 5 µM |  | +3.6 | +2.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.2 | +4.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.9 | +1.3 |
| fall | [[Radotinib (drug)]] 5 µM |  | -4.1 | -3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.1 | -3.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | -2.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.5 | -2.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.4 | -2.3 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.4 | -2.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.4 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger and SCAN domain containing 5A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.43 — chr19:56,219,670-56,368,383 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC4161; previously ZNF495, ZSCAN5 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; SCAN domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BUG6](https://www.uniprot.org/uniprotkb/Q9BUG6) (Zinc finger and SCAN domain-containing protein 5A):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [79149](https://www.ncbi.nlm.nih.gov/gene/79149):

> Enables sequence-specific double-stranded DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to be located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23710](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23710) · Entrez [79149](https://www.ncbi.nlm.nih.gov/gene/79149) · UniProt [Q9BUG6](https://www.uniprot.org/uniprotkb/Q9BUG6) · Ensembl [ENSG00000131848](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131848)

## Data

Gene col 5252: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5252); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5252, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5252]; `tensor/DDL_lfc|DDL_z.npy` [5252]; `embed/gene_vectors.npy` [5252]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5252 or target_col == 5252). Every well: [[ZSCAN5A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZSCAN5A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
