---
symbol: "FGD6"
type: "gene"
col: 11094
ensembl_id: "ENSG00000180263"
name: "FYVE, RhoGEF and PH domain containing 6"
location: "12q22"
module: 34
arm: "+"
pooled_cpm: 142.52
n_lines_expressing: 38
n_dd_up: 13
n_dd_down: 27
n_dd_up_clean: 9
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 14
direction_downstream: 21
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# FGD6

*FYVE, RhoGEF and PH domain containing 6* — 12q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.09× (z +7.4, q 8e-11, up in 28 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (5 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.662× (z -7.9, q 2e-12, down in 26 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LAMC2]] (+0.66, fdr 7e-06), [[FAM107B]] (+0.63, fdr 7e-06), [[WNT7B]] (+0.62, fdr 1e-05); moves opposite to [[FAM53B]] (-0.53, fdr 4e-05, ⚠ FAM53B in the vector space only through flagged drug-doses), [[TM9SF1]] (-0.48, fdr 1e-04), [[TIMM44]] (-0.46, fdr 4e-05), [[BOD1]] (-0.46, fdr 1e-04).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[CYP24A1]] → it (grade B ⚠); 21 go from it, the strongest it → [[PARD6B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11094.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.09×** | +7.4 | 8e-11 | 28/37 (A-427, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.27×** | +6.6 | 2e-08 | 17/36 (A-427, J82, …) | top dose only | composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.39×** | +6.3 | 4e-08 | 17/36 (J82, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +6.3 | 5e-08 | 14/36 (SW480, SNU-423, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.34×** | +5.7 | 1e-06 | 15/36 (J82, SW480, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.30×** | +5.0 | 4e-05 | 13/36 (SW480, J82, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change | **1.30×** | +5.0 | 4e-05 | 18/36 (J82, HT-29, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.27×** | +4.6 | 4e-04 | 15/36 (J82, SW480, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.26×** | +4.4 | 7e-04 | 19/36 (HT-29, J82, …) | rises with dose | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.25×** | +4.2 | 0.001 | 17/37 (HOP62, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.25×** | +4.2 | 0.002 | 15/36 (A-427, A498, …) | top dose only | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.39×** | +3.3 | 0.043 | 18/36 (NCI-H2030, A549, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 1.18× | +3.2 | 0.061 | 15/36 (HT-29, KATO III, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.37×** | +3.2 | 0.063 | 10/37 (J82, NCI-H1792, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.17× | +3.1 | 0.077 | 17/36 (HT-29, LS 180, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.17× | +3.1 | 0.078 | 14/36 (LS 180, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11094.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.662×** | -7.9 | 2e-12 | 26/36 (MIA PaCa-2, LOX-IMVI, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.695×** | -6.7 | 7e-09 | 23/36 (CFPAC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.708×** | -6.6 | 9e-09 | 28/36 (PANC-1, A549, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.715×** | -6.4 | 3e-08 | 26/36 (NCI-H1573, NCI-H1792, …) | all doses, flat |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.530×** | -6.3 | 3e-08 | 24/36 (MIA PaCa-2, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | **0.801×** | -6.0 | 2e-07 | 19/36 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.732×** | -5.9 | 2e-07 | 25/36 (NCI-H1573, NCI-H1792, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.739×** | -5.8 | 6e-07 | 25/36 (NCI-H1792, NCI-H1573, …) | all doses, flat |  |
| [[Darinaparsin (drug)]] 5 µM |  | **0.815×** | -5.5 | 3e-06 | 21/36 (A498, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.750×** | -5.5 | 3e-06 | 26/37 (CFPAC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.749×** | -5.3 | 6e-06 | 21/34 (NCI-H1573, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.773×** | -4.9 | 5e-05 | 23/36 (NCI-H1573, NCI-H1792, …) | all doses, flat |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.624×** | -4.7 | 1e-04 | 21/36 (A549, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 0.840× | -4.7 | 1e-04 | 17/36 (NCI-H2347, LoVo, …) | top dose only | low cells (technical?) |
| [[Budesonide (drug)]] 5 µM |  | **0.784×** | -4.6 | 1e-04 | 19/36 (NCI-H1792, NCI-H1573, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.771×** | -4.6 | 2e-04 | 20/36 (NCI-H1573, NCI-H1792, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.637×** | -4.5 | 2e-04 | 25/36 (A549, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.05 µM |  | **0.797×** | -4.3 | 5e-04 | 21/36 (NCI-H1573, NCI-H1792, …) | all doses, flat |  |
| [[venetoclax (drug)]] 5 µM |  | **0.654×** | -4.2 | 7e-04 | 21/36 (NCI-H2030, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.5 µM |  | **0.801×** | -4.2 | 7e-04 | 21/36 (NCI-H1792, NCI-H1573, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11094. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 193 | 0 | 18 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -21.2) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Clobetasol propionate (drug)]] 0.05 µM 0.303× (z -11.4) |
| [[HEC-1-A (line)]] | alt | 196 | 0 | 13 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.479× (z -13.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.410× (z -11.4) |
| [[A-427 (line)]] | wt | 103 | 6 (4 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +15.6) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.20× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.219× (z -15.9) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 478 | 0 | 7 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.245× (z -22.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.428× (z -9.6) |
| [[LOX-IMVI (line)]] | wt | 211 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -12.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.363× (z -10.8) |
| [[NCI-H2030 (line)]] | alt | 421 | 0 | 7 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -19.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 171 | 2 (2 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +14.6) ⚠ cell-cycle shift, explains ~19% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -17.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.477× (z -9.1) |
| [[A549 (line)]] | wt | 461 | 1 | 5 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 4.60× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.227× (z -25.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 56.8 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +14.8) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 3.18× (z +12.1) | — |
| [[LoVo (line)]] | wt | 193 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.339× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.474× (z -8.7) |
| [[MIA PaCa-2 (line)]] | alt | 170 | 0 | 5 (4 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.312× (z -12.5) |
| [[NCI-H2347 (line)]] | alt | 244 | 0 | 5 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -14.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 102 | 4 | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 2.04× (z +10.6) | — |
| [[NCI-H1792 (line)]] | alt | 90.6 | 0 | 4 | — | [[Clobetasol propionate (drug)]] 0.5 µM 0.337× (z -11.3) |
| [[AsPC-1 (line)]] | alt | 696 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.298× (z -19.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.467× (z -8.8) |
| [[HepG2_C3A (line)]] | wt | 107 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.351× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 141 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.335× (z -13.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 214 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.480× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 137 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.25× (z +9.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.450× (z -10.1) ⚠ unreliable plate only |
| [[SW480 (line)]] | alt | 48.1 | 2 | 0 | [[Belinostat (drug)]] 5 µM 2.22× (z +9.4) | — |
| [[KATO III (line)]] | alt | 39.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.55× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW 900 (line)]] | alt | 108 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.420× (z -8.8) |
| [[SW1417 (line)]] | alt | 157 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.33× (z +8.6) | — |
| [[A-172 (line)]] | wt | 35.2 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 59.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 126 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.9 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 31.9 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 89.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 37.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 77.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 36.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.5 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 28.8 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 115 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 201 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 35.2 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 68.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.6 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 30.9 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 30.4 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 25.5 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 17.0 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 77.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.0 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 76.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11094), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LAMC2]] | +0.66 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[FAM107B]] | +0.63 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[WNT7B]] | +0.62 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[RHOF]] | +0.60 | +0.64 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[PKIA]] | +0.59 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[BMAL2]] | +0.59 | +0.58 / +0.66 | both halves | 8e-06 |  |
| [[GDPGP1]] | +0.58 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[PIM1]] | +0.58 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[GPRC5A]] | +0.56 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[SEMA7A]] | +0.56 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[SERPINB9]] | +0.56 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[SERPINB1]] | +0.55 | +0.54 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM53B]] ⚠ | -0.53 | -0.40 / -0.47 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TM9SF1]] | -0.48 | -0.36 / -0.34 | both halves | 1e-04 |  |
| [[TIMM44]] | -0.46 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[BOD1]] | -0.46 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[MTO1]] | -0.46 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[MKX]] | -0.45 | -0.37 / -0.29 | both halves | 3e-04 |  |
| [[PAAF1]] | -0.45 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[DUS3L]] | -0.45 | -0.32 / -0.34 | both halves | 2e-04 |  |
| [[MTRF1]] | -0.45 | -0.45 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 11, C 3. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CYP24A1]] | B | CYP24A1 activity raises FGD6's level | lines that do not express CYP24A1 (39) vs lines expressing it (11) | 3.06× lower at baseline in the lines without CYP24A1 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, S100A9, FGG |
| [[BARX2]] | B | BARX2 activity raises FGD6's level | lines that do not express BARX2 (29) vs lines expressing it (21) | 2.39× lower at baseline in the lines without BARX2 | 0.022 | ⚠ within organs, on part of the lines; also absent: COL17A1, FXYD3, CEACAM6 |
| [[CCDC68]] | B | CCDC68 activity raises FGD6's level | lines that do not express CCDC68 (25) vs lines expressing it (25) | 2.44× lower at baseline in the lines without CCDC68 | 0.025 | ⚠ within organs, on part of the lines; also absent: GRB7, SH2D3A, GOLT1A |
| [[SMAD3]] | B | SMAD3 activity raises FGD6's level | lines that do not express SMAD3 (6) vs lines expressing it (44) | 1.69× lower at baseline in the lines without SMAD3 | 0.026 | ⚠ within organs, on part of the lines; also absent: ITGA3, NIBAN2, IER3; maybe low, not absent |
| [[IRF6]] | B | IRF6 activity raises FGD6's level | lines that do not express IRF6 (31) vs lines expressing it (19) | 1.97× lower at baseline in the lines without IRF6 | 0.034 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[LAMC2]] | B | LAMC2 activity raises FGD6's level | lines that do not express LAMC2 (27) vs lines expressing it (23) | 2.15× lower at baseline in the lines without LAMC2 | 0.042 | ⚠ within organs, on part of the lines; also absent: ENSG00000287929, TNS4, HS3ST1 |
| [[GPRC5A]] | B | GPRC5A activity raises FGD6's level | lines that do not express GPRC5A (12) vs lines expressing it (38) | 2.04× lower at baseline in the lines without GPRC5A | 0.061 | ⚠ within organs, on part of the lines; also absent: TESMIN, PSORS1C1, ITGA3 |
| [[FA2H]] | B | FA2H activity raises FGD6's level | lines that do not express FA2H (27) vs lines expressing it (23) | 2.02× lower at baseline in the lines without FA2H | 0.074 | ⚠ within organs, on part of the lines; also absent: IRF6, ST14, SGPP2 |
| [[CDCP1]] | B | CDCP1 activity raises FGD6's level | lines that do not express CDCP1 (16) vs lines expressing it (34) | 2.55× lower at baseline in the lines without CDCP1 | 0.085 | ⚠ within organs, on part of the lines; also absent: PTK6, TNK1, CHMP4C |
| [[CCDC68]] | B | CCDC68 activity weakens FGD6's drug response | lines that do not express CCDC68 (16) vs lines expressing it (21) | the lines without CCDC68 respond 1.16× as strongly (z diff -0.51); strongest at Homoharringtonine 5 µM: 1.43x vs 0.85x (z diff -5.3) | 0.090 | ⚠ within organs, on part of the lines; also absent: GRB7, SH2D3A, GOLT1A; target measured in part of the lines; both ways; artifact flags |
| [[WNT7B]] | B | WNT7B activity raises FGD6's level | lines that do not express WNT7B (20) vs lines expressing it (30) | 1.62× lower at baseline in the lines without WNT7B | 0.098 | ⚠ within organs, on part of the lines; also absent: ABCC3, NHS, PPARG |
| [[F2RL1]] | C | F2RL1 activity raises FGD6's level | lines that do not express F2RL1 (20) vs lines expressing it (30) | 2.36× lower at baseline in the lines without F2RL1 | 0.003 | ⚠ within organs, on part of the lines; also absent: PRSS22, ENSG00000267748, CDH1; co-absent with the target |

### Downstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 18, C 3. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PARD6B]] | B | FGD6 activity raises PARD6B's level | lines that do not express FGD6 (12) vs lines expressing it (38) | 3.68× lower at baseline in the lines without FGD6 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000290957, PKP2, EPHA2-AS1; maybe low, not absent |
| [[ITGA6]] | B | FGD6 activity raises ITGA6's level | lines that do not express FGD6 (12) vs lines expressing it (38) | 2.56× lower at baseline in the lines without FGD6 | 0.008 | ⚠ within organs, on part of the lines; also absent: ENSG00000290957, PKP2, EPHA2-AS1; maybe low, not absent |
| [[RAC1]] | B | FGD6 activity raises RAC1's level | lines that do not express FGD6 (12) vs lines expressing it (38) | 1.33× lower at baseline in the lines without FGD6 | 0.022 | ⚠ within organs, on part of the lines; also absent: ENSG00000290957, PKP2, EPHA2-AS1; maybe low, not absent |
| [[BARX2]] | B | FGD6 activity raises BARX2's level | lines that do not express FGD6 (12) vs lines expressing it (38) | 4.05× lower at baseline in the lines without FGD6 | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000290957, PKP2, EPHA2-AS1; maybe low, not absent |
| [[LIMA1]] | B | FGD6 activity raises LIMA1's level | lines that do not express FGD6 (12) vs lines expressing it (38) | 1.61× lower at baseline in the lines without FGD6 | 0.050 | ⚠ within organs, on part of the lines; also absent: ENSG00000290957, PKP2, EPHA2-AS1; maybe low, not absent |
| [[WNT7B]] | B | FGD6 activity raises WNT7B's level | lines that do not express FGD6 (12) vs lines expressing it (38) | 2.80× lower at baseline in the lines without FGD6 | 0.052 | ⚠ within organs, on part of the lines; also absent: ENSG00000290957, PKP2, EPHA2-AS1; maybe low, not absent |
| [[RHOF]] | B | FGD6 activity raises RHOF's level | lines that do not express FGD6 (12) vs lines expressing it (38) | 2.54× lower at baseline in the lines without FGD6 | 0.053 | ⚠ within organs, on part of the lines; also absent: ENSG00000290957, PKP2, EPHA2-AS1; maybe low, not absent |
| [[SMAD3]] | B | FGD6 activity raises SMAD3's level | lines that do not express FGD6 (12) vs lines expressing it (38) | 1.69× lower at baseline in the lines without FGD6 | 0.056 | ⚠ within organs, on part of the lines; also absent: ENSG00000290957, PKP2, EPHA2-AS1; maybe low, not absent |
| [[IRF6]] | B | FGD6 activity raises IRF6's level | lines that do not express FGD6 (12) vs lines expressing it (38) | 4.44× lower at baseline in the lines without FGD6 | 0.058 | ⚠ within organs, on part of the lines; also absent: ENSG00000290957, PKP2, EPHA2-AS1; maybe low, not absent |
| [[BAIAP2L1]] | B | FGD6 activity raises BAIAP2L1's level | lines that do not express FGD6 (12) vs lines expressing it (38) | 2.71× lower at baseline in the lines without FGD6 | 0.065 | ⚠ within organs, on part of the lines; also absent: ENSG00000290957, PKP2, EPHA2-AS1; maybe low, not absent |
| [[NCEH1]] | B | FGD6 activity raises NCEH1's level | lines that do not express FGD6 (12) vs lines expressing it (38) | 2.16× lower at baseline in the lines without FGD6 | 0.076 | ⚠ within organs, on part of the lines; also absent: ENSG00000290957, PKP2, EPHA2-AS1; maybe low, not absent |
| [[GDPGP1]] | B | FGD6 activity raises GDPGP1's level | lines that do not express FGD6 (12) vs lines expressing it (38) | 1.60× lower at baseline in the lines without FGD6 | 0.078 | ⚠ within organs, on part of the lines; also absent: ENSG00000290957, PKP2, EPHA2-AS1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.576). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (43.3, -0.2); signed map (1.6, 44.7). **Vector** length 122, 36.1% of its response variance represented; |z| ≥ 3 in 1,387 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +6.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.7 | +6.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.4 | +5.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.2 | +4.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.7 | +4.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.7 | +3.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.5 | +1.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.0 | +2.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | +1.9 | +0.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.4 | -6.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.1 | -7.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.5 | -6.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -4.3 | -6.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -4.3 | -6.4 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -4.2 | -5.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.2 | -6.3 |

## What is on record

|  |  |
|---|---|
| Name | FYVE, RhoGEF and PH domain containing 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q22 — chr12:95,076,749-95,217,482 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ZFYVE24, FLJ11183 |
| Gene groups (HGNC) | Zinc fingers FYVE-type; Pleckstrin homology domain containing; Dbl family Rho GEFs |
| Hallmark sets | MITOTIC_SPINDLE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZV73](https://www.uniprot.org/uniprotkb/Q6ZV73) (FYVE, RhoGEF and PH domain-containing protein 6):

> May activate CDC42, a member of the Ras-like family of Rho- and Rac proteins, by exchanging bound GDP for free GTP. May play a role in regulating the actin cytoskeleton and cell shape (By similarity).

**Summary**, from NCBI Gene [55785](https://www.ncbi.nlm.nih.gov/gene/55785):

> Predicted to enable guanyl-nucleotide exchange factor activity and small GTPase binding activity. Predicted to be involved in actin cytoskeleton organization; filopodium assembly; and regulation of cell shape. Predicted to be located in Golgi apparatus; lamellipodium; and ruffle. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21740](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21740) · Entrez [55785](https://www.ncbi.nlm.nih.gov/gene/55785) · UniProt [Q6ZV73](https://www.uniprot.org/uniprotkb/Q6ZV73) · Ensembl [ENSG00000180263](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180263)

## Data

Gene col 11094: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11094); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11094, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11094]; `tensor/DDL_lfc|DDL_z.npy` [11094]; `embed/gene_vectors.npy` [11094]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11094 or target_col == 11094). Every well: [[FGD6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FGD6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
