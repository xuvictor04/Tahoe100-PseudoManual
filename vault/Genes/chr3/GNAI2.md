---
symbol: "GNAI2"
type: "gene"
col: 3542
ensembl_id: "ENSG00000114353"
name: "G protein subunit alpha i2"
location: "3p21.31"
module: 85
arm: "+"
pooled_cpm: 87.67
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 23
n_dd_up_clean: 5
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/085"]
generated_by: "tahoemap"
---

# GNAI2

*G protein subunit alpha i2* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.50× (z +12.2, q 1e-31, up in 44 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 2.33× (z +11.3, q 2e-27, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.533× (z -8.4, q 2e-14, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (83 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 17 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PCMT1]] (+0.75, fdr 3e-05), [[SLC27A1]] (+0.75, fdr 4e-05), [[RRAS]] (+0.73, fdr 3e-05); moves opposite to [[GABPB1-AS1]] (-0.72, fdr 3e-04), [[KICS2]] (-0.71, fdr 1e-05), [[RNF146]] (-0.68, fdr 4e-04).
> It sits in the **+** arm of [[Module 085]].
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[PLCXD1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3542.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.50×** | +12.2 | 1e-31 | 44/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.48×** | +11.7 | 5e-29 | 39/41 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.33×** | +11.3 | 2e-27 | 46/48 (LS 180, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.30×** | +11.1 | 1e-26 | 46/48 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.29×** | +11.1 | 2e-26 | 45/48 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.56×** | +6.0 | 2e-07 | 41/48 (SW1417, LoVo, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.62×** | +6.0 | 2e-07 | 33/44 (SNU-423, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~67% of this change | **1.30×** | +3.5 | 0.028 | 25/48 (SW1417, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.30×** | +3.5 | 0.029 | 27/48 (LS 180, SW1417, …) | all doses, stronger at high dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.46×** | +3.2 | 0.072 | 25/48 (PANC-1, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3542.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.533×** | -8.4 | 2e-14 | 40/48 (A-427, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.583×** | -6.9 | 1e-09 | 34/48 (NCI-H23, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.627×** | -6.2 | 9e-08 | 30/48 (RPMI-7951, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.727×** | -5.9 | 4e-07 | 30/48 (NCI-H2347, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.728×** | -5.9 | 4e-07 | 39/49 (AsPC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.674×** | -5.3 | 1e-05 | 32/48 (SNU-423, A-172, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.771×** | -4.9 | 1e-04 | 28/48 (SK-MEL-2, MIA PaCa-2, …) | rises with dose | low cells (technical?) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.705×** | -4.7 | 2e-04 | 32/48 (hTERT-HPNE, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.718×** | -4.4 | 6e-04 | 35/48 (MIA PaCa-2, AsPC-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.732×** | -4.2 | 0.002 | 28/48 (hTERT-HPNE, RPMI-7951, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.734×** | -4.0 | 0.004 | 28/48 (J82, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.751×** | -3.8 | 0.006 | 25/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.587×** | -3.7 | 0.009 | 32/49 (RPMI-7951, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.741×** | -3.7 | 0.009 | 35/48 (HepG2/C3A, J82, …) | inconsistent across doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.758×** | -3.4 | 0.023 | 31/48 (AN3 CA, H4, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.617×** | -3.4 | 0.026 | 26/48 (LOX-IMVI, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.789×** | -3.2 | 0.053 | 27/48 (AN3 CA, HCT15, …) | inconsistent across doses | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3542. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 97.2 | 6 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +11.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.33× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.523× (z -9.8) |
| [[HOP62 (line)]] | alt | 188 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +10.7) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -12.3) |
| [[LoVo (line)]] | wt | 29.4 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.90× (z +13.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 87.5 | 2 (1 ⚠) | 3 | [[Belinostat (drug)]] 5 µM 2.84× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -13.1) |
| [[Panc 03.27 (line)]] | alt | 96.8 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.02× (z +10.5) | — |
| [[A-172 (line)]] | wt | 203 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.85× (z +11.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.285× (z -13.1) |
| [[A-427 (line)]] | wt | 50.5 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.07× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.0649× (z -22.2) |
| [[A549 (line)]] | wt | 24.8 | 4 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.19× (z +10.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.93× (z +10.3) | — |
| [[KATO III (line)]] | alt | 52.4 | 4 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 4.79× (z +12.3) | — |
| [[LS 180 (line)]] | wt | 31.1 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 7.10× (z +13.9) | — |
| [[RKO (line)]] | wt | 61.0 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.92× (z +11.1) | — |
| [[SW480 (line)]] | alt | 91.3 | 4 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +12.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.90× (z +10.9) | — |
| [[HCT15 (line)]] | alt | 54.5 | 3 | 0 | [[Belinostat (drug)]] 5 µM 4.78× (z +11.5) | — |
| [[HEC-1-A (line)]] | alt | 49.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.32× (z +10.4) | — |
| [[HepG2_C3A (line)]] | wt | 31.8 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.49× (z +9.2) | — |
| [[HS-578T (line)]] | alt | 159 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.63× (z +10.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.420× (z -9.0) |
| [[HT-29 (line)]] | alt | 59.2 | 3 | 0 | [[Belinostat (drug)]] 5 µM 3.11× (z +9.5) | — |
| [[NCI-H2030 (line)]] | alt | 67.1 | 1 | 2 | [[Panobinostat (drug)]] 0.5 µM 2.51× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -10.7) |
| [[NCI-H23 (line)]] | alt | 46.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.220× (z -12.3) |
| [[RPMI-7951 (line)]] | alt | 173 | 0 | 3 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.130× (z -11.6) ⚠ toxic; cell-cycle shift, explains ~59% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.428× (z -9.3) |
| [[SW1417 (line)]] | alt | 106 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.25× (z +13.3) | — |
| [[Hs 766T (line)]] | wt | 110 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -12.5) |
| [[J82 (line)]] | alt | 158 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.477× (z -11.4) |
| [[NCI-H1792 (line)]] | alt | 63.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.08× (z +9.3) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.452× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 146 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.419× (z -13.7) |
| [[NCI-H460 (line)]] | wt | 54.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.62× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.05 µM 0.382× (z -8.9) |
| [[PANC-1 (line)]] | alt | 68.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.36× (z +14.4) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 90.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.44× (z +9.2) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 126 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.289× (z -16.9) |
| [[BT-474 (line)]] | alt | 23.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.118× (z -12.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 104 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.88× (z +9.5) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 84.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -9.6) |
| [[H4 (line)]] | wt | 109 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -11.2) |
| [[LOX-IMVI (line)]] | wt | 109 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +9.8) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 51.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.15× (z +9.1) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 221 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -12.6) |
| [[SW 900 (line)]] | alt | 85.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.347× (z -9.4) |
| [[AN3 CA (line)]] | alt | 86.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 61.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 152 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 68.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 78.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 185 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 86.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3542), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCMT1]] | +0.75 | +0.65 / +0.45 | both halves | 3e-05 |  |
| [[SLC27A1]] | +0.75 | +0.64 / +0.42 | both halves | 4e-05 |  |
| [[RRAS]] | +0.73 | +0.69 / +0.43 | both halves | 3e-05 | pathway: HALLMARK_APICAL_JUNCTION |
| [[PEDS1]] | +0.73 | +0.66 / +0.43 | both halves | 3e-05 |  |
| [[YIF1B]] | +0.72 | +0.64 / +0.23 | both halves | 5e-04 |  |
| [[TNK2]] | +0.71 | +0.57 / +0.47 | both halves | 2e-05 | same gene group |
| [[DNAAF3]] | +0.71 | +0.46 / +0.37 | both halves | 7e-05 |  |
| [[PLA2G15]] | +0.71 | +0.61 / +0.46 | both halves | 3e-05 |  |
| [[CEP131]] | +0.70 | +0.53 / +0.23 | both halves | 5e-04 |  |
| [[IGSF8]] | +0.70 | +0.65 / +0.47 | both halves | 2e-05 |  |
| [[F11R]] | +0.70 | +0.70 / +0.46 | both halves | 3e-05 |  |
| [[PLPPR2]] | +0.69 | +0.60 / +0.31 | both halves | 2e-04 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 14 of them with an alert (⚠; 14 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GABPB1-AS1]] | -0.72 | -0.70 / -0.26 | both halves | 3e-04 |  |
| [[KICS2]] | -0.71 | -0.66 / -0.53 | both halves | 1e-05 |  |
| [[RNF146]] | -0.68 | -0.56 / -0.24 | both halves | 4e-04 |  |
| [[NIPAL2]] | -0.68 | -0.54 / -0.27 | both halves | 3e-04 |  |
| [[GALNT7-DT]] | -0.67 | -0.56 / -0.07 | ⚠ one half (not replicated) | 0.004 |  |
| [[SMAD1]] | -0.67 | -0.61 / -0.30 | both halves | 2e-04 |  |
| [[DPH5-DT]] | -0.67 | -0.66 / -0.32 | both halves | 2e-04 |  |
| [[EPM2A]] | -0.66 | -0.60 / -0.10 | ⚠ one half (not replicated) | 0.003 |  |
| [[RWDD2B]] | -0.66 | -0.54 / -0.29 | both halves | 2e-04 |  |
| [[KLHL42]] | -0.66 | -0.54 / -0.25 | both halves | 4e-04 |  |
| [[ZNF337-AS1]] | -0.65 | -0.59 / -0.09 | ⚠ one half (not replicated) | 0.003 |  |
| [[LACTB2]] | -0.65 | -0.62 / -0.30 | both halves | 2e-04 |  |
| [[GABPB1]] | -0.65 | -0.49 / -0.23 | both halves | 5e-04 |  |
| [[MIER3]] | -0.65 | -0.42 / -0.29 | both halves | 3e-04 |  |
| [[CCDC122]] | -0.65 | -0.55 / -0.23 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLCXD1]] | B | PLCXD1 activity lowers GNAI2's level | lines that do not express PLCXD1 (11) vs lines expressing it (39) | 1.59× higher at baseline in the lines without PLCXD1 | 0.060 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ANKRD18A]] | B | ANKRD18A activity lowers GNAI2's level | lines that do not express ANKRD18A (11) vs lines expressing it (39) | 2.07× higher at baseline in the lines without ANKRD18A | 0.067 | ⚠ within organs, on part of the lines; also absent: LRRC61, SLC27A2, CHMP4C |
| [[HDAC6]] | B | HDAC6 activity lowers GNAI2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[HPCAL1]] | B | HPCAL1 activity raises GNAI2's level | lines that do not express HPCAL1 (6) vs lines expressing it (44) | 1.54× lower at baseline in the lines without HPCAL1 | 0.087 | ⚠ within organs, on part of the lines; also absent: SHB, ARMCX3, ECE1; maybe low, not absent |
| [[BMPR1B]] | B | BMPR1B activity lowers GNAI2's level | lines that do not express BMPR1B (28) vs lines expressing it (22) | 1.20× higher at baseline in the lines without BMPR1B | 0.092 | ⚠ within organs, on part of the lines; also absent: ENSG00000286385, SLC6A17, EPHA5-AS1 |
| [[PCSK6]] | B | PCSK6 activity lowers GNAI2's level | lines that do not express PCSK6 (21) vs lines expressing it (29) | 1.75× higher at baseline in the lines without PCSK6 | 0.094 | ⚠ within organs, on part of the lines; also absent: BTNL9, CYP4F12, LINC02964 |
| [[ZBED3]] | C | ZBED3 activity lowers GNAI2's level | lines that do not express ZBED3 (3) vs lines expressing it (47) | 2.15× higher at baseline in the lines without ZBED3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GPD1L, DBNDD1, CDON; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 085]]; 52 genes; this gene is in the **+** arm (projection on the module's main direction 0.833). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (5.2, -1.3); signed map (-28.0, 19.0). **Vector** length 126, 44.8% of its response variance represented; |z| ≥ 3 in 1,111 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +9.8 | +11.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +9.7 | +11.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +9.6 | +11.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | +5.4 | +3.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +5.4 | +6.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.7 | +2.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.1 | +1.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.1 | +2.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.0 | +1.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +2.3 | +0.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -10.5 | -5.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -8.3 | -6.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -8.0 | -4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -7.6 | -1.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.2 | -8.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.1 | -3.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.0 | -0.8 |
|  | [[Amsacrine (drug)]] 5 µM |  | -3.6 | -1.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.5 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | G protein subunit alpha i2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:50,226,292-50,259,362 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GIP; previously GNAI2B |
| Gene groups (HGNC) | G protein subunits alpha, group i; MicroRNA protein coding host genes |
| Hallmark sets | COMPLEMENT, APICAL_JUNCTION |
| Reactome | 30 pathways, smallest: Adenylate cyclase inhibitory pathway; ADP signalling through P2Y purinoceptor 12; Adrenaline,noradrenaline inhibits insulin secretion |
| Matched by | ensembl_id |

**Function**, from UniProt [P04899](https://www.uniprot.org/uniprotkb/P04899) (Guanine nucleotide-binding protein G(i) subunit alpha-2):

> Guanine nucleotide-binding proteins (G proteins) function as transducers downstream of G protein-coupled receptors (GPCRs) in numerous signaling cascades. The alpha chain contains the guanine nucleotide binding site and alternates between an active, GTP-bound state and an inactive, GDP-bound state. Signaling by an activated GPCR promotes GDP release and GTP binding. Examples of interacting GPCRs include the adenosine A1 receptor/ADORA1, CNR1, and FPR2. The alpha subunit has a low GTPase …

**Summary**, from NCBI Gene [2771](https://www.ncbi.nlm.nih.gov/gene/2771):

> The protein encoded by this gene is an alpha subunit of guanine nucleotide binding proteins (G proteins). The encoded protein contains the guanine nucleotide binding site and is involved in the hormonal regulation of adenylate cyclase. Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Sep 2013]

**Accessions** — [HGNC:4385](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4385) · Entrez [2771](https://www.ncbi.nlm.nih.gov/gene/2771) · UniProt [P04899](https://www.uniprot.org/uniprotkb/P04899) · Ensembl [ENSG00000114353](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114353)

## Data

Gene col 3542: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3542); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3542, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3542]; `tensor/DDL_lfc|DDL_z.npy` [3542]; `embed/gene_vectors.npy` [3542]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3542 or target_col == 3542). Every well: [[GNAI2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GNAI2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
