---
symbol: "HSPB8"
type: "gene"
col: 7596
ensembl_id: "ENSG00000152137"
name: "heat shock protein family B (small) member 8"
location: "12q24.23"
module: 215
arm: "+"
pooled_cpm: 11.45
n_lines_expressing: 50
n_dd_up: 37
n_dd_down: 1
n_dd_up_clean: 24
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/215"]
generated_by: "tahoemap"
---

# HSPB8

*heat shock protein family B (small) member 8* — 12q24.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 37 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.17× (z +16.2, q 0e+00, up in 30 of 33 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.66× (z +11.1, q 2e-26, up in 41 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.661× (z -4.7, q 0.002, down in 21 of 42 measured lines) ⚠ toxic; transcription drop.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Pyridoxine (drug)]] 0.5 µM in 2 lines (SW 900 0.0716×, MIA PaCa-2 0.0867×); [[Pimozide (drug)]] 0.05 µM in 1 line (NCI-H23 0.0836×); [[palbociclib (drug)]] 0.05 µM in 1 line (SHP-77 0.0867×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF6]] (+0.69, fdr 1e-05), [[PSMC3]] (+0.69, fdr 7e-06), [[PDAP1]] (+0.67, fdr 1e-05); moves opposite to [[TMSB10]] (-0.66, fdr 1e-05), [[B3GAT3]] (-0.63, fdr 1e-05), [[ANAPC11]] (-0.63, fdr 6e-05).
> It is in [[Module 215]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 37 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7596.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.17×** | +16.2 | 0e+00 | 30/33 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.21×** | +15.7 | 0e+00 | 16/18 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.81×** | +14.0 | 2e-42 | 26/27 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.01×** | +11.2 | 8e-27 | 25/44 (SNU-423, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.66×** | +11.1 | 2e-26 | 41/46 (HS-578T, HOP62, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.35×** | +9.7 | 3e-20 | 37/46 (A498, A-172, …) | two highest doses | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.37×** | +9.4 | 5e-19 | 32/47 (HS-578T, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.14×** | +8.6 | 4e-16 | 30/43 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.13×** | +8.6 | 7e-16 | 30/47 (A498, SHP-77, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.19×** | +8.4 | 3e-15 | 28/44 (A498, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +8.2 | 1e-14 | 29/43 (hTERT-HPNE, BT-474, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.78×** | +6.5 | 3e-09 | 29/47 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.76×** | +6.2 | 3e-08 | 25/38 (NCI-H460, SNU-423, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.50×** | +4.6 | 2e-04 | 16/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.09×** | +4.4 | 4e-04 | 11/30 (A498, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.07×** | +4.3 | 5e-04 | 20/45 (NCI-H460, A-172, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.45×** | +4.2 | 8e-04 | 15/46 (A-172, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.43×** | +4.1 | 0.001 | 13/43 (HT-29, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | **1.28×** | +3.9 | 0.003 | 8/47 (SW480, HT-29, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.39×** | +3.6 | 0.009 | 13/46 (HT-29, BT-474, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.54×** | +3.5 | 0.011 | 14/48 (A498, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7596.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Pyridoxine (drug)]] 0.5 µM in 2 lines (SW 900 0.0716×, MIA PaCa-2 0.0867×); [[Pimozide (drug)]] 0.05 µM in 1 line (NCI-H23 0.0836×); [[palbociclib (drug)]] 0.05 µM in 1 line (SHP-77 0.0867×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.661×** | -4.7 | 0.002 | 21/42 (A-427, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | 0.725× | -3.4 | 0.13 | 11/48 (HS-578T, C-33 A, …) | inconsistent across doses | position effect removed |
| [[Pravastatin (sodium) (drug)]] 0.5 µM |  | 0.741× | -3.4 | 0.13 | 5/48 (BT-474, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.923× | -3.1 | 0.26 | 4/48 (LOX-IMVI, AN3 CA, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7596. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 21.8 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +10.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.03× (z +10.3) | — |
| [[A-172 (line)]] | wt | 22.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.04× (z +13.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.96× (z +10.0) | — |
| [[HOP62 (line)]] | alt | 6.57 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.82× (z +11.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 7.69× (z +9.2) | — |
| [[HS-578T (line)]] | alt | 16.6 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.26× (z +12.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 8.28× (z +10.5) | — |
| [[hTERT-HPNE (line)]] | wt | 18.4 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.62× (z +12.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.20× (z +10.5) | — |
| [[A498 (line)]] | wt | 47.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +11.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 6.59× (z +9.7) | — |
| [[A549 (line)]] | wt | 8.32 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.17× (z +10.2) | — |
| [[HEC-1-A (line)]] | alt | 7.21 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.44× (z +8.8) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 10.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.69× (z +12.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.99× (z +9.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 6.75 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 10.0× (z +8.9) ⚠ toxic; transcription drop | [[Pyridoxine (drug)]] 0.5 µM 0.0867× (z -9.5) |
| [[PANC-1 (line)]] | alt | 8.86 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.73× (z +10.0) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 8.87 | 1 | 1 | [[Bortezomib (drug)]] 0.05 µM 8.96× (z +8.5) | [[palbociclib (drug)]] 0.05 µM 0.0867× (z -9.5) |
| [[SW480 (line)]] | alt | 9.04 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.70× (z +11.4) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 19.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.37× (z +10.4) | — |
| [[C-33 A (line)]] | alt | 7.52 | 0 | 1 | — | [[Rifaximin (drug)]] 0.05 µM 0.0523× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 11.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.54× (z +12.0) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[KATO III (line)]] | alt | 9.80 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.4× (z +11.2) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 9.05 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.34× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 7.66 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0836× (z -10.5) |
| [[SNU-423 (line)]] | alt | 13.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.71× (z +13.8) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[SW 900 (line)]] | alt | 11.6 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0716× (z -11.1) |
| [[A-427 (line)]] | wt | 7.34 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.06 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.53 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.67 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.39 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.00 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.20 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.57 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.29 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.84 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.06 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.38 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7596), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF6]] | +0.69 | +0.70 / +0.51 | both halves | 1e-05 |  |
| [[PSMC3]] | +0.69 | +0.72 / +0.62 | both halves | 7e-06 |  |
| [[PDAP1]] | +0.67 | +0.74 / +0.54 | both halves | 1e-05 |  |
| [[HTATIP2]] | +0.66 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[ZXDB]] | +0.65 | +0.68 / +0.46 | both halves | 3e-05 |  |
| [[C17orf80]] | +0.65 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[DST]] | +0.63 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[NXT2]] | +0.62 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[BAG2]] | +0.62 | +0.61 / +0.46 | both halves | 3e-05 | pathway: Cellular response to heat stress; STRING 683 |
| [[PSMC5]] | +0.62 | +0.70 / +0.46 | both halves | 2e-05 |  |
| [[PRECSIT]] | +0.61 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[PPID]] | +0.61 | +0.67 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMSB10]] | -0.66 | -0.65 / -0.56 | both halves | 1e-05 |  |
| [[B3GAT3]] | -0.63 | -0.63 / -0.52 | both halves | 1e-05 |  |
| [[ANAPC11]] | -0.63 | -0.66 / -0.38 | both halves | 6e-05 |  |
| [[COX6A1]] | -0.60 | -0.54 / -0.47 | both halves | 2e-05 | pathway: HALLMARK_ADIPOGENESIS |
| [[C1QL1]] | -0.60 | -0.62 / -0.42 | both halves | 4e-05 |  |
| [[SNHG25]] | -0.60 | -0.59 / -0.58 | both halves | 8e-06 |  |
| [[MHENCR]] | -0.60 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[RPLP2]] | -0.60 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[PIBF1]] | -0.59 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[SH3GL1]] | -0.59 | -0.60 / -0.40 | both halves | 5e-05 |  |
| [[CLEC4A]] | -0.58 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[LSM2]] | -0.58 | -0.61 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers HSPB8's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.0% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 215]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.762). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-22.8, -9.9); signed map (-6.3, -36.6). **Vector** length 83.4, 16.4% of its response variance represented; |z| ≥ 3 in 1,019 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.9 | +16.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.8 | +11.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.5 | +14.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.5 | +15.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +5.8 | +11.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.3 | +9.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | +3.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.8 | +1.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.3 | +3.5 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.2 | -4.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | -0.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | -2.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | -1.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -2.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.9 | -0.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.6 | -0.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.5 | -2.7 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -1.2 | -2.8 |
|  | [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | -1.1 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | heat shock protein family B (small) member 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.23 — chr12:119,171,555-119,224,855 (+) |
| Ensembl biotype | protein_coding |
| Also known as | H11, E2IG1, HSP22, CMT2L |
| Gene groups (HGNC) | Small heat shock proteins |
| Hallmark sets | MYOGENESIS, ESTROGEN_RESPONSE_LATE, ADIPOGENESIS, ESTROGEN_RESPONSE_EARLY |
| Reactome | 4 pathways, smallest: HSF1-dependent transactivation; Cellular response to heat stress; Cellular responses to stress |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UJY1](https://www.uniprot.org/uniprotkb/Q9UJY1) (Heat shock protein beta-8):

> Involved in the chaperone-assisted selective autophagy (CASA), a crucial process for protein quality control, particularly in mechanical strained cells and tissues such as muscle. Displays temperature-dependent chaperone activity.

**Summary**, from NCBI Gene [26353](https://www.ncbi.nlm.nih.gov/gene/26353):

> The protein encoded by this gene belongs to the superfamily of small heat-shock proteins containing a conservative alpha-crystallin domain at the C-terminal part of the molecule. The expression of this gene in induced by estrogen in estrogen receptor-positive breast cancer cells, and this protein also functions as a chaperone in association with Bag3, a stimulator of macroautophagy. Thus, this gene appears to be involved in regulation of cell proliferation, apoptosis, and carcinogenesis, and …

**Accessions** — [HGNC:30171](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30171) · Entrez [26353](https://www.ncbi.nlm.nih.gov/gene/26353) · UniProt [Q9UJY1](https://www.uniprot.org/uniprotkb/Q9UJY1) · Ensembl [ENSG00000152137](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152137)

## Data

Gene col 7596: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7596); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7596, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7596]; `tensor/DDL_lfc|DDL_z.npy` [7596]; `embed/gene_vectors.npy` [7596]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7596 or target_col == 7596). Every well: [[HSPB8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HSPB8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
