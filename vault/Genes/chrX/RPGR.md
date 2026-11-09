---
symbol: "RPGR"
type: "gene"
col: 7971
ensembl_id: "ENSG00000156313"
name: "retinitis pigmentosa GTPase regulator"
location: "Xp11.4"
module: 97
arm: "+"
pooled_cpm: 47.24
n_lines_expressing: 50
n_dd_up: 32
n_dd_down: 30
n_dd_up_clean: 27
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/097"]
generated_by: "tahoemap"
---

# RPGR

*retinitis pigmentosa GTPase regulator* — Xp11.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.05× (z +14.4, q 5e-44, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (5 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.563× (z -11.5, q 6e-28, down in 42 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.415× (z -9.2, q 9e-18, down in 39 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTPN12]] (+0.62, fdr 7e-06), [[TBC1D8]] (+0.60, fdr 1e-05), [[SNED1]] (+0.59, fdr 1e-05); moves opposite to [[MATN2]] (-0.51, fdr 3e-05), [[GRIK4]] (-0.50, fdr 5e-05), [[ADAMTS16]] (-0.48, fdr 3e-05).
> It is in [[Module 097]], a single-armed module (estrogen response early).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7971.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.05×** | +14.4 | 5e-44 | 43/48 (SW1417, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.87×** | +12.5 | 2e-33 | 41/48 (SW1417, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.80×** | +11.8 | 9e-30 | 39/48 (SW1417, LS 180, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.62×** | +9.7 | 5e-20 | 31/47 (BT-474, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.59×** | +9.3 | 1e-18 | 38/48 (BT-474, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.58×** | +9.2 | 4e-18 | 39/48 (BT-474, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.53×** | +8.6 | 8e-16 | 38/48 (BT-474, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.45×** | +7.5 | 7e-12 | 23/47 (A549, NCI-H1792, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.41×** | +6.9 | 3e-10 | 30/48 (SW1417, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.26×** | +6.5 | 6e-09 | 25/48 (LoVo, MIA PaCa-2, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.31×** | +5.5 | 2e-06 | 22/47 (A549, SK-MEL-2, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.31×** | +5.3 | 4e-06 | 24/48 (Hs 766T, NCI-H1792, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.29×** | +5.0 | 2e-05 | 20/48 (Hs 766T, SK-MEL-2, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **1.28×** | +5.0 | 2e-05 | 21/48 (SK-MEL-2, Hs 766T, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.28×** | +5.0 | 2e-05 | 22/47 (SK-MEL-2, NCI-H1792, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.30×** | +4.9 | 3e-05 | 22/47 (SK-MEL-2, NCI-H1792, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.27×** | +4.8 | 5e-05 | 22/47 (BT-474, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7971.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.563×** | -11.5 | 6e-28 | 42/48 (NCI-H460, RKO, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.415×** | -9.2 | 9e-18 | 39/46 (NCI-H460, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.451×** | -8.3 | 1e-14 | 35/49 (SK-MEL-2, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.668×** | -8.1 | 9e-14 | 32/48 (C-33 A, NCI-H460, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **0.489×** | -7.5 | 8e-12 | 32/45 (RKO, A549, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.500×** | -7.3 | 4e-11 | 34/48 (NCI-H460, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.631×** | -6.6 | 4e-09 | 28/48 (SW480, SW48, …) | rises with dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.797×** | -6.4 | 1e-08 | 25/48 (A549, NCI-H460, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.585×** | -5.6 | 1e-06 | 28/47 (NCI-H460, RKO, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.597×** | -5.4 | 4e-06 | 25/47 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.771×** | -5.2 | 1e-05 | 24/49 (C32, NCI-H460, …) | all doses, flat |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.705×** | -5.0 | 3e-05 | 23/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.783×** | -4.9 | 4e-05 | 26/45 (KATO III, PANC-1, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Binimetinib (drug)]] 5 µM |  | **0.793×** | -4.7 | 1e-04 | 23/48 (C32, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.643×** | -4.6 | 1e-04 | 21/47 (LoVo, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.810×** | -4.2 | 8e-04 | 16/47 (C32, NCI-H460, …) | two highest doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.842× | -4.2 | 8e-04 | 17/48 (C32, RKO, …) | all doses, stronger at high dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7971. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 70.5 | 14 | 3 (2 ⚠) | [[Dexamethasone (drug)]] 0.5 µM 3.46× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.173× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.189× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 52.2 | 15 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 4.74× (z +12.0) | — |
| [[A549 (line)]] | wt | 124 | 11 | 2 (1 ⚠) | [[Clobetasol propionate (drug)]] 0.05 µM 2.93× (z +12.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.535× (z -9.9) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.555× (z -9.3) |
| [[Hs 766T (line)]] | wt | 31.4 | 13 | 0 | [[Clobetasol propionate (drug)]] 5 µM 6.25× (z +11.6) | — |
| [[NCI-H460 (line)]] | wt | 94.2 | 9 | 3 (1 ⚠) | [[Clobetasol propionate (drug)]] 5 µM 2.34× (z +10.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.316× (z -13.6) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.134× (z -12.4) |
| [[C32 (line)]] | wt | 74.7 | 1 | 9 (2 ⚠) | [[Clobetasol propionate (drug)]] 0.5 µM 2.95× (z +9.0) | [[Binimetinib (drug)]] 0.5 µM 0.300× (z -12.3) |
| [[H4 (line)]] | wt | 48.4 | 6 | 0 | [[Clobetasol propionate (drug)]] 0.5 µM 4.19× (z +8.9) | — |
| [[LS 180 (line)]] | wt | 37.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.01× (z +9.7) | — |
| [[NCI-H2347 (line)]] | alt | 21.2 | 2 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.95× (z +9.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.355× (z -8.6) ⚠ unreliable plate only |
| [[SW1417 (line)]] | alt | 45.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.26× (z +11.2) | — |
| [[A-172 (line)]] | wt | 18.7 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.99× (z +10.0) | — |
| [[KATO III (line)]] | alt | 86.9 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.310× (z -12.7) ⚠ transcription drop |
| [[PANC-1 (line)]] | alt | 41.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.464× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 35.8 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.214× (z -10.6) |
| [[CHP-212 (line)]] | wt | 41.0 | 0 | 1 | — | [[Monocrotaline (drug)]] 0.05 µM 0.0768× (z -10.1) |
| [[HCT15 (line)]] | alt | 27.9 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.212× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 22.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.17× (z +9.4) | — |
| [[HOP62 (line)]] | alt | 33.9 | 1 | 0 | [[Budesonide (drug)]] 5 µM 2.82× (z +8.7) | — |
| [[LoVo (line)]] | wt | 49.7 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.72× (z +8.6) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[LOX-IMVI (line)]] | wt | 41.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +9.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H1573 (line)]] | alt | 52.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.363× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 64.3 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.383× (z -9.3) ⚠ unreliable plate only |
| [[SW480 (line)]] | alt | 85.7 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.553× (z -8.6) ⚠ unreliable plate only |
| [[A-427 (line)]] | wt | 48.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 63.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 61.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 59.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 67.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 41.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7971), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTPN12]] | +0.62 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[TBC1D8]] | +0.60 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[SNED1]] | +0.59 | +0.54 / +0.51 | both halves | 1e-05 | **novel candidate** |
| [[CCND3]] | +0.58 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[MT2A]] | +0.57 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[DNER]] | +0.57 | +0.46 / +0.52 | both halves | 3e-05 |  |
| [[ATP1A1]] | +0.54 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[AKAP13]] | +0.53 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[ANGPTL4]] | +0.52 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[APPL2]] | +0.52 | +0.54 / +0.46 | both halves | 3e-05 |  |
| [[TOP1]] | +0.50 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[LDLRAD3]] | +0.50 | +0.52 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MATN2]] | -0.51 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[GRIK4]] | -0.50 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[ADAMTS16]] | -0.48 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[WDFY1]] | -0.45 | -0.34 / -0.51 | both halves | 1e-04 |  |
| [[SYTL2]] | -0.45 | -0.46 / -0.49 | both halves | 2e-05 |  |
| [[KCP]] | -0.45 | -0.34 / -0.49 | both halves | 1e-04 |  |
| [[SLAMF7]] | -0.45 | -0.33 / -0.45 | both halves | 1e-04 |  |
| [[ANKRD30B]] | -0.45 | -0.30 / -0.41 | both halves | 2e-04 |  |
| [[CNN3-DT]] | -0.45 | -0.37 / -0.45 | both halves | 9e-05 |  |
| [[ZSCAN31]] | -0.44 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[NUAK1]] | -0.44 | -0.51 / -0.32 | both halves | 1e-04 |  |
| [[LINC00536]] | -0.44 | -0.27 / -0.50 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises RPGR's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 5.6% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds |
| [[PDGFC]] | B | PDGFC activity lowers RPGR's level | lines that do not express PDGFC (13) vs lines expressing it (37) | 1.50× higher at baseline in the lines without PDGFC | 0.058 | ⚠ within organs, on part of the lines; also absent: OSMR-DT, GLRB, DNAH11 |
| [[NR3C1]] | B | NR3C1 activity raises RPGR's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 5.0% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 097]] — estrogen response early; 48 genes; every member is in the + arm (projection on the module's main direction 0.627). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.6, 12.9); signed map (14.7, 33.7). **Vector** length 131, 38.9% of its response variance represented; |z| ≥ 3 in 1,565 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 0.5 µM |  | +7.4 | +9.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +6.9 | +9.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.3 | +9.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +6.2 | +8.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +5.8 | +7.5 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +5.0 | +5.5 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +4.8 | +3.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +4.8 | +2.4 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | +4.7 | +4.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -9.2 | -11.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -8.3 | -8.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -7.2 | -9.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.0 | +0.5 |
|  | [[venetoclax (drug)]] 5 µM |  | -6.8 | -7.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -6.3 | -3.6 |
|  | [[EX229 (drug)]] 5 µM |  | -6.2 | -5.4 |

## What is on record

|  |  |
|---|---|
| Name | retinitis pigmentosa GTPase regulator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.4 — chrX:38,269,163-38,327,544 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CORDX1; previously CRD, RP3, RP15, COD1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92834](https://www.uniprot.org/uniprotkb/Q92834) (X-linked retinitis pigmentosa GTPase regulator):

> Acts as a guanine-nucleotide releasing factor (GEF) for RAB8A and RAB37 by promoting the conversion of inactive RAB-GDP to the active form RAB-GTP. GEF activity towards RAB8A may facilitate ciliary trafficking by modulating ciliary intracellular localization of RAB8A. GEF activity towards RAB37 maintains autophagic homeostasis and retinal function (By similarity). Involved in photoreceptor integrity (By similarity). May control cilia formation by regulating actin stress filaments and cell …

**Summary**, from NCBI Gene [6103](https://www.ncbi.nlm.nih.gov/gene/6103):

> This gene encodes a protein with a series of six RCC1-like domains (RLDs), characteristic of the highly conserved guanine nucleotide exchange factors. The encoded protein is found in the Golgi body and interacts with RPGRIP1. This protein localizes to the outer segment of rod photoreceptors and is essential for their viability. Mutations in this gene have been associated with X-linked retinitis pigmentosa (XLRP). Multiple alternatively spliced transcript variants that encode different isoforms …

**Accessions** — [HGNC:10295](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10295) · Entrez [6103](https://www.ncbi.nlm.nih.gov/gene/6103) · UniProt [Q92834](https://www.uniprot.org/uniprotkb/Q92834) · Ensembl [ENSG00000156313](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156313)

## Data

Gene col 7971: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7971); `tables/drug_effects.parquet` (85 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7971, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7971]; `tensor/DDL_lfc|DDL_z.npy` [7971]; `embed/gene_vectors.npy` [7971]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7971 or target_col == 7971). Every well: [[RPGR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPGR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
