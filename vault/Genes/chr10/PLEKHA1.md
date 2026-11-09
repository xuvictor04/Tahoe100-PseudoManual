---
symbol: "PLEKHA1"
type: "gene"
col: 2869
ensembl_id: "ENSG00000107679"
name: "pleckstrin homology domain containing A1"
location: "10q26.13"
module: 186
arm: "+"
pooled_cpm: 119.58
n_lines_expressing: 49
n_dd_up: 0
n_dd_down: 27
n_dd_up_clean: 0
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/186"]
generated_by: "tahoemap"
---

# PLEKHA1

*pleckstrin homology domain containing A1* — 10q26.13

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (PANC-1 1.67×; ⚠ cell-cycle shift, explains ~0% of this change); [[Trametinib (drug)]] 5 µM in 1 line (AsPC-1 2.36×; ⚠ cell-cycle shift, explains ~40% of this change); [[Trametinib (drug)]] 0.05 µM in 1 line (AsPC-1 1.83×); [[Trametinib (drug)]] 0.5 µM in 1 line (AsPC-1 2.01×).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (14 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.493× (z -17.7, q 0e+00, down in 44 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LNX2]] (+0.62, fdr 7e-06), [[TAPT1]] (+0.55, fdr 1e-05), [[EPS8]] (+0.53, fdr 2e-05); moves opposite to [[RRP7BP-1]] (-0.54, fdr 1e-05), [[VAC14]] (-0.52, fdr 3e-05), [[ZNF787]] (-0.52, fdr 2e-05).
> It is in [[Module 186]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[RASSF6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2869.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (PANC-1 1.67×; ⚠ cell-cycle shift, explains ~0% of this change); [[Trametinib (drug)]] 5 µM in 1 line (AsPC-1 2.36×; ⚠ cell-cycle shift, explains ~40% of this change); [[Trametinib (drug)]] 0.05 µM in 1 line (AsPC-1 1.83×); [[Trametinib (drug)]] 0.5 µM in 1 line (AsPC-1 2.01×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 1.18× | +4.1 | 0.026 | 17/49 (AsPC-1, Hs 766T, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 1.16× | +3.8 | 0.049 | 15/48 (NCI-H2347, HOP62, …) | all doses, flat |  |
| [[RMC-6236 (drug)]] 5 µM |  | 1.29× | +3.3 | 0.13 | 14/47 (AsPC-1, Hs 766T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 1.15× | +3.3 | 0.13 | 13/46 (COLO 205, AsPC-1, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.14× | +3.2 | 0.14 | 13/48 (AsPC-1, Hs 766T, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 20 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2869.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.493×** | -17.7 | 0e+00 | 44/47 (SW480, PANC-1, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.569×** | -14.2 | 4e-43 | 40/47 (SW480, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.615×** | -12.2 | 6e-32 | 40/47 (HEC-1-A, A549, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.616×** | -12.1 | 9e-32 | 38/47 (HEC-1-A, A549, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.638×** | -11.3 | 2e-27 | 33/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.684×** | -9.5 | 1e-19 | 34/47 (HepG2/C3A, HEC-1-A, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.706×** | -8.7 | 2e-16 | 32/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.713×** | -8.5 | 1e-15 | 31/47 (Hs 766T, C32, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.713×** | -8.5 | 1e-15 | 29/47 (NCI-H460, SW 900, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.718×** | -8.3 | 5e-15 | 36/47 (HepG2/C3A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | **0.734×** | -7.8 | 4e-13 | 30/48 (HepG2/C3A, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **0.729×** | -7.6 | 1e-12 | 28/43 (SHP-77, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.749×** | -7.2 | 2e-11 | 28/47 (NCI-H460, HepG2/C3A, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.819×** | -7.1 | 6e-11 | 23/48 (HEC-1-A, NCI-H1792, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.594×** | -6.8 | 3e-10 | 32/48 (NCI-H460, A549, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.768×** | -6.2 | 1e-08 | 27/47 (A549, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.853× | -5.6 | 5e-07 | 22/47 (HEC-1-A, HOP62, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.703×** | -4.6 | 1e-04 | 23/47 (RKO, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.747×** | -3.8 | 0.003 | 18/46 (SW48, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.5 µM |  | **0.818×** | -3.4 | 0.013 | 6/47 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.828×** | -3.2 | 0.025 | 11/47 (COLO 205, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | 0.835× | -3.1 | 0.039 | 11/48 (MIA PaCa-2, SW 900, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.802×** | -2.9 | 0.069 | 13/47 (NCI-H1792, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.803×** | -2.9 | 0.071 | 11/47 (NCI-H1792, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | 0.894× | -2.8 | 0.087 | 14/47 (C32, SNU-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2869. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 253 | 0 | 13 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -16.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.331× (z -11.5) |
| [[NCI-H460 (line)]] | wt | 78.9 | 0 | 11 (9 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.312× (z -18.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.493× (z -11.0) |
| [[HepG2_C3A (line)]] | wt | 392 | 0 | 10 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.272× (z -14.9) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.407× (z -10.3) |
| [[AsPC-1 (line)]] | alt | 275 | 3 (1 ⚠) | 6 (5 ⚠) | [[Trametinib (drug)]] 5 µM 2.36× (z +9.1) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Trametinib (drug)]] 0.05 µM 1.83× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.250× (z -14.9) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.423× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 241 | 0 | 9 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -17.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.363× (z -13.8) |
| [[A549 (line)]] | wt | 201 | 0 | 8 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.251× (z -15.7) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.440× (z -9.3) |
| [[SW480 (line)]] | alt | 106 | 0 | 8 (6 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.304× (z -17.9) |
| [[SHP-77 (line)]] | alt | 192 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.132× (z -20.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.411× (z -9.3) |
| [[Hs 766T (line)]] | wt | 290 | 0 | 6 (4 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.267× (z -14.1) |
| [[KATO III (line)]] | alt | 130 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.405× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change |
| [[HT-29 (line)]] | alt | 179 | 0 | 5 (4 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.356× (z -13.2) |
| [[LoVo (line)]] | wt | 144 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.426× (z -12.6) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.439× (z -12.2) |
| [[LS 180 (line)]] | wt | 177 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.360× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change |
| [[COLO 205 (line)]] | alt | 163 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -12.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 210 | 1 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +12.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Auranofin (drug)]] 5 µM 0.424× (z -15.0) |
| [[SW 900 (line)]] | alt | 106 | 0 | 4 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.325× (z -12.1) |
| [[C32 (line)]] | wt | 90.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.340× (z -11.8) |
| [[CFPAC-1 (line)]] | alt | 114 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.486× (z -11.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.386× (z -11.1) |
| [[HOP62 (line)]] | alt | 54.3 | 0 | 3 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.539× (z -10.4) |
| [[LOX-IMVI (line)]] | wt | 69.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.380× (z -11.2) |
| [[SNU-1 (line)]] | wt | 98.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.160× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change |
| [[NCI-H23 (line)]] | alt | 73.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.484× (z -12.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 75.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -12.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.352× (z -9.6) |
| [[A-427 (line)]] | wt | 122 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.478× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change |
| [[H4 (line)]] | wt | 61.7 | 0 | 1 | — | [[Sonidegib (drug)]] 5 µM 0.122× (z -8.8) |
| [[NCI-H1573 (line)]] | alt | 72.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.372× (z -12.0) ⚠ toxic; transcription drop |
| [[NCI-H596 (line)]] | alt | 114 | 0 | 1 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.05 µM 0.112× (z -14.1) |
| [[Panc 03.27 (line)]] | alt | 108 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.401× (z -9.8) |
| [[SNU-423 (line)]] | alt | 91.5 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.420× (z -10.4) |
| [[SW1417 (line)]] | alt | 139 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.474× (z -9.2) ⚠ cell-cycle shift, explains ~29% of this change |
| [[A-172 (line)]] | wt | 37.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 92.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.6 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 107 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 55.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 78.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 60.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 59.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 240 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 66.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 74.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 72.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 74.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 85.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 76.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2869), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LNX2]] | +0.62 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[TAPT1]] | +0.55 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[EPS8]] | +0.53 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[SLC50A1]] | +0.53 | +0.46 / +0.57 | both halves | 3e-05 |  |
| [[CEPT1]] | +0.53 | +0.51 / +0.44 | both halves | 3e-05 | pathway: Phospholipid metabolism |
| [[PPTC7]] | +0.52 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[TLCD4]] | +0.51 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[LRRC1]] | +0.51 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[SPOPL]] | +0.50 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[B4GALT4]] | +0.50 | +0.46 / +0.37 | both halves | 9e-05 |  |
| [[EFNA1]] | +0.50 | +0.46 / +0.49 | both halves | 3e-05 |  |
| [[ACBD5]] | +0.48 | +0.52 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*49 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRP7BP-1]] | -0.54 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[VAC14]] | -0.52 | -0.54 / -0.43 | both halves | 3e-05 | pathway: PI Metabolism |
| [[ZNF787]] | -0.52 | -0.46 / -0.55 | both halves | 2e-05 |  |
| [[YRDC]] | -0.50 | -0.46 / -0.55 | both halves | 2e-05 |  |
| [[ZSCAN5A]] | -0.50 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[ZNF551]] | -0.48 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[TRMT1]] | -0.48 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[MEF2B]] | -0.48 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[ZNF407]] | -0.47 | -0.56 / -0.40 | both halves | 5e-05 |  |
| [[BIN3]] | -0.47 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[BRD9]] | -0.47 | -0.54 / -0.39 | both halves | 5e-05 |  |
| [[NUP214]] | -0.47 | -0.40 / -0.45 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RASSF6]] | B | RASSF6 activity raises PLEKHA1's level | lines that do not express RASSF6 (28) vs lines expressing it (22) | 1.81× lower at baseline in the lines without RASSF6 | 0.050 | ⚠ within organs, on part of the lines; also absent: TOX3, ELF3, ITGB6 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 186]]; 20 genes; every member is in the + arm (projection on the module's main direction 0.340). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (2.9, -25.5); signed map (35.8, -24.3). **Vector** length 96.0, 24.7% of its response variance represented; |z| ≥ 3 in 1,330 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.3 | +0.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.0 | +1.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +2.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.5 | +0.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.3 | +1.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.5 | +1.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.3 | +2.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.2 | +3.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.2 | +2.7 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.3 | -17.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.7 | -8.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -3.7 | -8.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -3.6 | -8.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.5 | -2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.0 | -4.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | -7.2 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | -2.0 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | pleckstrin homology domain containing A1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.13 — chr10:122,374,696-122,432,354 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TAPP1 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; MicroRNA protein coding host genes |
| Reactome | 4 pathways, smallest: Synthesis of PIPs at the plasma membrane; PI Metabolism; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HB21](https://www.uniprot.org/uniprotkb/Q9HB21) (Pleckstrin homology domain-containing family A member 1):

> Binds specifically to phosphatidylinositol 3,4-diphosphate (PtdIns3,4P2), but not to other phosphoinositides. May recruit other proteins to the plasma membrane.

**Summary**, from NCBI Gene [59338](https://www.ncbi.nlm.nih.gov/gene/59338):

> This gene encodes a pleckstrin homology domain-containing adapter protein. The encoded protein is localized to the plasma membrane where it specifically binds phosphatidylinositol 3,4-bisphosphate. This protein may be involved in the formation of signaling complexes in the plasma membrane. Polymorphisms in this gene are associated with age-related macular degeneration. Alternate splicing results in multiple transcript variants. A pseudogene of this gene is found on chromosome 5.[provided by …

**Accessions** — [HGNC:14335](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14335) · Entrez [59338](https://www.ncbi.nlm.nih.gov/gene/59338) · UniProt [Q9HB21](https://www.uniprot.org/uniprotkb/Q9HB21) · Ensembl [ENSG00000107679](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107679)

## Data

Gene col 2869: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2869); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2869, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2869]; `tensor/DDL_lfc|DDL_z.npy` [2869]; `embed/gene_vectors.npy` [2869]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2869 or target_col == 2869). Every well: [[PLEKHA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLEKHA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
