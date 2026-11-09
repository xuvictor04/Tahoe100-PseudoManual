---
symbol: "OCIAD2"
type: "gene"
col: 6970
ensembl_id: "ENSG00000145247"
name: "OCIA domain containing 2"
location: "4p11"
module: 24
arm: "+"
pooled_cpm: 57.25
n_lines_expressing: 40
n_dd_up: 22
n_dd_down: 2
n_dd_up_clean: 13
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 6
direction_downstream: 6
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# OCIAD2

*OCIA domain containing 2* — 4p11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.06× (z +9.7, q 2e-19, up in 35 of 36 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Vinblastine (sulfate) (drug)]] 5 µM: 1.51× (z +5.1, q 6e-05, up in 34 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.507× (z -8.3, q 6e-14, down in 31 of 38 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (MIA PaCa-2 0.236×, NCI-H1573 0.286×, BT-474 0.284×, SW480 0.386×, …); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.0648×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.327×; ⚠ cell-cycle shift, explains ~35% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LDAF1]] (+0.61, fdr 1e-05), [[FLYWCH1]] (+0.55, fdr 1e-05), [[HEBP2]] (+0.54, fdr 3e-05); moves opposite to [[SRCAP]] (-0.53, fdr 1e-05), [[PTBP1]] (-0.51, fdr 2e-05), [[COPS3]] (-0.51, fdr 4e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[C19orf33]] → it (grade B ⚠); 6 go from it, the strongest it → [[CPA6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6970.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.06×** | +9.7 | 2e-19 | 35/36 (NCI-H1792, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.58×** | +7.9 | 7e-13 | 28/31 (NCI-H460, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.51×** | +5.1 | 6e-05 | 34/38 (HT-29, LS 180, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.70×** | +4.6 | 6e-04 | 31/38 (KATO III, NCI-H1792, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.75×** | +4.4 | 0.001 | 29/34 (A-172, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.63×** | +4.3 | 0.002 | 28/38 (LS 180, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +4.2 | 0.002 | 28/38 (HOP62, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.59×** | +4.1 | 0.003 | 28/38 (LS 180, NCI-H1573, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.62×** | +4.0 | 0.003 | 27/38 (HT-29, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.59×** | +4.0 | 0.003 | 27/38 (HT-29, LS 180, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.55×** | +3.8 | 0.007 | 27/38 (HT-29, NCI-H1573, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.54×** | +3.8 | 0.008 | 25/38 (HT-29, NCI-H1573, …) | rises with dose |  |
| [[vincristine (drug)]] 5 µM |  | **2.25×** | +3.7 | 0.010 | 28/36 (HT-29, LS 180, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | **1.51×** | +3.6 | 0.012 | 23/38 (SW1417, Panc 03.27, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Radotinib (drug)]] 5 µM |  | **1.34×** | +3.6 | 0.012 | 27/38 (CFPAC-1, NCI-H1792, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.54×** | +3.5 | 0.013 | 26/38 (LS 180, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[vincristine (drug)]] 0.5 µM |  | **2.47×** | +3.5 | 0.013 | 27/38 (HT-29, LS 180, …) | rises with dose | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +3.1 | 0.060 | 21/38 (SW480, SW48, …) | rises with dose |  |
| [[Vilanterol (drug)]] 5 µM |  | **1.27×** | +3.0 | 0.077 | 26/38 (NCI-H2347, AsPC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6970.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (MIA PaCa-2 0.236×, NCI-H1573 0.286×, BT-474 0.284×, SW480 0.386×, …); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.0648×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.327×; ⚠ cell-cycle shift, explains ~35% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.507×** | -8.3 | 6e-14 | 31/38 (MIA PaCa-2, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.603×** | -4.3 | 0.004 | 24/38 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | 0.630× | -3.4 | 0.11 | 23/39 (Hs 766T, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[RMC-6236 (drug)]] 5 µM |  | 0.480× | -3.3 | 0.11 | 28/38 (PANC-1, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | 0.485× | -3.3 | 0.11 | 25/38 (SW480, Hs 766T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | 0.487× | -3.2 | 0.11 | 25/38 (AsPC-1, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.671× | -3.1 | 0.15 | 22/38 (HEC-1-A, Hs 766T, …) | inconsistent across doses |  |
| [[ERK5-IN-2 (drug)]] 5 µM |  | 0.507× | -3.1 | 0.16 | 24/39 (HEC-1-A, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6970. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 111 | 5 (1 ⚠) | 1 | [[Vinblastine (sulfate) (drug)]] 5 µM 3.04× (z +12.2) | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -9.2) |
| [[MIA PaCa-2 (line)]] | alt | 29.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0648× (z -15.9) |
| [[NCI-H460 (line)]] | wt | 21.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.11× (z +8.8) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 89.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.97× (z +10.5) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 92.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.25× (z +9.5) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 31.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -10.5) |
| [[CFPAC-1 (line)]] | alt | 136 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.27× (z +9.1) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 121 | 1 | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 2.20× (z +8.5) | — |
| [[NCI-H1573 (line)]] | alt | 91.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -10.5) |
| [[NCI-H1792 (line)]] | alt | 43.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.63× (z +11.9) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 31.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -8.9) |
| [[RKO (line)]] | wt | 82.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.327× (z -10.2) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SHP-77 (line)]] | alt | 33.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -9.0) |
| [[SNU-423 (line)]] | alt | 69.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.13× (z +8.7) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 48.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -10.1) |
| [[A-427 (line)]] | wt | 11.2 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 45.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.67 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 64.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.81 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.05 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 38.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 66.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 138 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.58 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 97.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.45 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.67 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 110 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 60.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.70 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.27 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 74.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.21 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 89.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 64.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6970), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LDAF1]] | +0.61 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[FLYWCH1]] | +0.55 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[HEBP2]] | +0.54 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[CIB2]] | +0.54 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[ROBO3]] | +0.54 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[ACVR1]] | +0.54 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[FAM241B]] | +0.53 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[PIK3CD]] | +0.53 | +0.39 / +0.54 | both halves | 5e-05 |  |
| [[ATOX1]] | +0.53 | +0.46 / +0.47 | both halves | 3e-05 |  |
| [[PLCXD2]] | +0.53 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[CLDN12]] | +0.53 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[ATP6V0D2]] | +0.53 | +0.50 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRCAP]] | -0.53 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[PTBP1]] | -0.51 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[COPS3]] | -0.51 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[IRF2BP1]] | -0.48 | -0.53 / -0.36 | both halves | 1e-04 |  |
| [[TNS3]] | -0.48 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[ZMYND11]] | -0.47 | -0.49 / -0.38 | both halves | 6e-05 |  |
| [[MLH1]] | -0.47 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[UBAP2L]] | -0.47 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[SYNCRIP]] | -0.47 | -0.38 / -0.47 | both halves | 7e-05 |  |
| [[BCLAF1]] | -0.46 | -0.38 / -0.46 | both halves | 7e-05 |  |
| [[EIF4G1]] | -0.46 | -0.42 / -0.44 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C19orf33]] | B | C19orf33 activity raises OCIAD2's level | lines that do not express C19orf33 (19) vs lines expressing it (31) | 3.47× lower at baseline in the lines without C19orf33 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: KRT80, MISP, AREG |
| [[PLCXD2]] | B | PLCXD2 activity raises OCIAD2's level | lines that do not express PLCXD2 (7) vs lines expressing it (43) | 2.26× lower at baseline in the lines without PLCXD2 | 0.017 | ⚠ within organs, on part of the lines; also absent: SOX4; maybe low, not absent |
| [[TMEM154]] | B | TMEM154 activity raises OCIAD2's level | lines that do not express TMEM154 (26) vs lines expressing it (24) | 2.08× lower at baseline in the lines without TMEM154 | 0.036 | ⚠ within organs, on part of the lines; also absent: ENSG00000287003, SYNPR-AS1, MMP13 |
| [[ATG9B]] | B | ATG9B activity raises OCIAD2's level | lines that do not express ATG9B (20) vs lines expressing it (30) | 2.28× lower at baseline in the lines without ATG9B | 0.074 | ⚠ within organs, on part of the lines; also absent: AFAP1L2, GJB3, EREG |
| [[GALNT12]] | B | GALNT12 activity raises OCIAD2's level | lines that do not express GALNT12 (10) vs lines expressing it (40) | 3.02× lower at baseline in the lines without GALNT12 | 0.087 | ⚠ within organs, on part of the lines; also absent: ARHGEF4, TUBA4A, ALS2CL |
| [[S100A14]] | B | S100A14 activity raises OCIAD2's level | lines that do not express S100A14 (33) vs lines expressing it (17) | 2.38× lower at baseline in the lines without S100A14 | 0.097 | ⚠ within organs, on part of the lines; also absent: PRSS8, RAB25, TMPRSS4 |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CPA6]] | B | OCIAD2 activity lowers CPA6's level | lines that do not express OCIAD2 (10) vs lines expressing it (40) | 2.47× higher at baseline in the lines without OCIAD2 | 0.018 | ⚠ within organs, on part of the lines; also absent: CDCP1, STAMBPL1, SLCO4A1 |
| [[KIF5A]] | B | OCIAD2 activity lowers KIF5A's level | lines that do not express OCIAD2 (10) vs lines expressing it (40) | 2.86× higher at baseline in the lines without OCIAD2 | 0.063 | ⚠ within organs, on part of the lines; also absent: CDCP1, STAMBPL1, SLCO4A1 |
| [[GALNT12]] | B | OCIAD2 activity raises GALNT12's level | lines that do not express OCIAD2 (10) vs lines expressing it (40) | 2.30× lower at baseline in the lines without OCIAD2 | 0.081 | ⚠ within organs, on part of the lines; also absent: CDCP1, STAMBPL1, SLCO4A1 |
| [[LSM10]] | B | OCIAD2 activity lowers LSM10's level | lines that do not express OCIAD2 (10) vs lines expressing it (40) | 1.17× higher at baseline in the lines without OCIAD2 | 0.089 | ⚠ within organs, on part of the lines; also absent: CDCP1, STAMBPL1, SLCO4A1 |
| [[C19orf33]] | B | OCIAD2 activity raises C19orf33's level | lines that do not express OCIAD2 (10) vs lines expressing it (40) | 3.79× lower at baseline in the lines without OCIAD2 | 0.092 | ⚠ within organs, on part of the lines; also absent: CDCP1, STAMBPL1, SLCO4A1 |
| [[STPG1]] | B | OCIAD2 activity lowers STPG1's level | lines that do not express OCIAD2 (10) vs lines expressing it (40) | 1.37× higher at baseline in the lines without OCIAD2 | 0.095 | ⚠ within organs, on part of the lines; also absent: CDCP1, STAMBPL1, SLCO4A1 |

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.340). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (52.6, -2.3); signed map (-6.2, 51.0). **Vector** length 91.4, 33.1% of its response variance represented; |z| ≥ 3 in 704 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.6 | +3.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.7 | +3.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.6 | +1.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.3 | +4.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.1 | +4.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.6 | +5.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.8 | +1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +4.6 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | -1.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.2 | -8.3 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.1 | +0.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -2.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.5 | -4.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.3 | -2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.3 | -3.1 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -2.3 | +0.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.0 | -1.8 |
|  | [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | -2.0 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | OCIA domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p11 — chr4:48,885,019-48,906,937 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC45416 |
| Gene groups (HGNC) | Mitochondrial respiratory chain complex assembly factors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q56VL3](https://www.uniprot.org/uniprotkb/Q56VL3) (OCIA domain-containing protein 2):

> Has an essential role in the assembly of mitochondrial respiratory chain complex III. Is also required for STAT3 activation and plays a role in cell migration.

**Summary**, from NCBI Gene [132299](https://www.ncbi.nlm.nih.gov/gene/132299):

> Involved in cell migration and mitochondrial respiratory chain complex III assembly. Located in endosome and mitochondrial inner membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28685](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28685) · Entrez [132299](https://www.ncbi.nlm.nih.gov/gene/132299) · UniProt [Q56VL3](https://www.uniprot.org/uniprotkb/Q56VL3) · Ensembl [ENSG00000145247](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145247)

## Data

Gene col 6970: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6970); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6970, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6970]; `tensor/DDL_lfc|DDL_z.npy` [6970]; `embed/gene_vectors.npy` [6970]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6970 or target_col == 6970). Every well: [[OCIAD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OCIAD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
