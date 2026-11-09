---
symbol: "RAB21"
type: "gene"
col: 1280
ensembl_id: "ENSG00000080371"
name: "RAB21, member RAS oncogene family"
location: "12q21.1"
module: 35
arm: "+"
pooled_cpm: 111.39
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 4
n_dd_up_clean: 19
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# RAB21

*RAB21, member RAS oncogene family* — 12q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.91× (z +30.3, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Tirabrutinib (drug)]] 0.5 µM: 0.791× (z -4.7, q 0.001, down in 26 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PIGP]] (+0.73, fdr 3e-05), [[PLEKHF2]] (+0.72, fdr 7e-06), [[AHI1-DT]] (+0.70, fdr 2e-05); moves opposite to [[DGKD]] (-0.70, fdr 1e-05), [[DDX19A]] (-0.65, fdr 8e-06), [[EML4]] (-0.62, fdr 6e-05).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CA11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1280.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.91×** | +30.3 | 0e+00 | 47/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.43×** | +17.8 | 0e+00 | 48/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **5.41×** | +17.7 | 0e+00 | 48/49 (SW480, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.26×** | +16.3 | 0e+00 | 48/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.21×** | +15.9 | 0e+00 | 46/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.21×** | +15.3 | 0e+00 | 47/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.81×** | +11.9 | 9e-31 | 45/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.98×** | +11.5 | 1e-28 | 45/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.71×** | +10.7 | 6e-25 | 42/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.66×** | +10.2 | 1e-22 | 42/48 (HT-29, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.54×** | +8.7 | 3e-16 | 36/48 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.50×** | +8.1 | 2e-14 | 39/48 (HT-29, LoVo, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +8.1 | 2e-14 | 40/47 (LoVo, COLO 205, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.51×** | +7.8 | 2e-13 | 42/48 (PANC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +7.0 | 1e-10 | 30/49 (PANC-1, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.39×** | +5.8 | 2e-07 | 30/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.22×** | +5.7 | 4e-07 | 24/48 (PANC-1, Panc 03.27, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1280.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tirabrutinib (drug)]] 0.5 µM |  | **0.791×** | -4.7 | 0.001 | 26/48 (NCI-H1573, A498, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **0.806×** | -4.3 | 0.004 | 27/48 (LOX-IMVI, NCI-H1792, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 0.876× | -3.8 | 0.024 | 8/48 (SNU-1, NCI-H2347, …) | rises with dose |  |
| [[Apalutamide (drug)]] 0.5 µM |  | **0.830×** | -3.8 | 0.024 | 22/48 (C32, HOP62, …) | inconsistent across doses |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 0.841× | -3.5 | 0.046 | 13/48 (A498, NCI-H1573, …) | top dose only |  |
| [[Pexidartinib (hydrochloride) (drug)]] 0.5 µM |  | 0.842× | -3.5 | 0.046 | 17/48 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Afatinib (drug)]] 0.5 µM |  | 0.879× | -3.4 | 0.046 | 5/49 (MIA PaCa-2, RKO, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Filgotinib (drug)]] 0.05 µM |  | **0.825×** | -3.4 | 0.046 | 17/48 (C32, NCI-H1792, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~6% of this change | 0.845× | -3.3 | 0.062 | 20/44 (Panc 03.27, CFPAC-1, …) | top dose only | composition shift |
| [[Carbamazepine (drug)]] 5 µM |  | 0.851× | -3.3 | 0.062 | 16/47 (SW 1271, SW1417, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 0.852× | -3.2 | 0.062 | 21/48 (CFPAC-1, NCI-H1573, …) | two highest doses | position effect removed |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 0.855× | -3.2 | 0.070 | 12/48 (A498, C32, …) | top dose only |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | 0.850× | -3.2 | 0.070 | 17/49 (NCI-H1792, NCI-H1573, …) | top dose only | plate-row cell shift |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 0.857× | -3.1 | 0.074 | 11/48 (CFPAC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | 0.853× | -3.1 | 0.076 | 16/48 (SW48, Panc 03.27, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1280. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 109 | 16 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.23× (z +30.0) | — |
| [[PANC-1 (line)]] | alt | 74.0 | 14 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.75× (z +33.9) | — |
| [[LoVo (line)]] | wt | 164 | 12 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +26.5) | — |
| [[SW480 (line)]] | alt | 75.1 | 12 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +19.2) | — |
| [[KATO III (line)]] | alt | 92.3 | 8 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.99× (z +18.2) | [[Dinaciclib (drug)]] 0.05 µM 0.481× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 134 | 8 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +20.2) | [[Dinaciclib (drug)]] 5 µM 0.408× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~6% of this change |
| [[NCI-H1792 (line)]] | alt | 179 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +22.3) | — |
| [[NCI-H23 (line)]] | alt | 96.1 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +24.1) | — |
| [[SW48 (line)]] | wt | 113 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +14.1) | — |
| [[HEC-1-A (line)]] | alt | 122 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +19.5) | — |
| [[HT-29 (line)]] | alt | 102 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +15.0) | — |
| [[BT-474 (line)]] | alt | 124 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +18.5) | — |
| [[HOP62 (line)]] | alt | 106 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +16.4) | — |
| [[hTERT-HPNE (line)]] | wt | 124 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.72× (z +21.1) | — |
| [[RKO (line)]] | wt | 98.0 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +14.5) | — |
| [[A-172 (line)]] | wt | 119 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +22.9) | — |
| [[A-427 (line)]] | wt | 82.6 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +12.0) | — |
| [[COLO 205 (line)]] | alt | 97.0 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +15.9) | — |
| [[LS 180 (line)]] | wt | 151 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.09× (z +16.1) | — |
| [[SW 900 (line)]] | alt | 136 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +12.9) | — |
| [[A549 (line)]] | wt | 84.7 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.91× (z +23.0) | — |
| [[J82 (line)]] | alt | 99.5 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +23.2) | — |
| [[SNU-423 (line)]] | alt | 127 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +19.5) | — |
| [[A498 (line)]] | wt | 135 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.21× (z +20.3) | — |
| [[AsPC-1 (line)]] | alt | 108 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +18.5) | — |
| [[H4 (line)]] | wt | 110 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +11.2) | — |
| [[Hs 766T (line)]] | wt | 77.7 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +15.1) | — |
| [[LOX-IMVI (line)]] | wt | 184 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +12.7) | — |
| [[NCI-H2030 (line)]] | alt | 79.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +14.9) | — |
| [[C32 (line)]] | wt | 109 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +17.9) | — |
| [[CFPAC-1 (line)]] | alt | 136 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +18.9) | [[Dinaciclib (drug)]] 5 µM 0.417× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~6% of this change |
| [[HS-578T (line)]] | alt | 96.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +16.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 71.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +15.4) | — |
| [[NCI-H2347 (line)]] | alt | 168 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +15.1) | — |
| [[Panc 03.27 (line)]] | alt | 78.0 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +16.7) | [[Dinaciclib (drug)]] 5 µM 0.319× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~6% of this change |
| [[RPMI-7951 (line)]] | alt | 92.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +14.6) | — |
| [[SHP-77 (line)]] | alt | 82.8 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.81× (z +11.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.43× (z +9.7) | — |
| [[SNU-1 (line)]] | wt | 125 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +12.7) | — |
| [[HCT15 (line)]] | alt | 113 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +14.1) | — |
| [[HepG2_C3A (line)]] | wt | 142 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +14.3) | — |
| [[SK-MEL-2 (line)]] | alt | 96.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +18.4) | — |
| [[SW1417 (line)]] | alt | 116 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +12.0) | — |
| [[AN3 CA (line)]] | alt | 127 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +8.7) | — |
| [[C-33 A (line)]] | alt | 71.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 162 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 97.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 123 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1280), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIGP]] | +0.73 | +0.63 / +0.43 | both halves | 3e-05 |  |
| [[PLEKHF2]] | +0.72 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[AHI1-DT]] | +0.70 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[CHASERR]] | +0.68 | +0.57 / +0.67 | both halves | 9e-06 |  |
| [[APPBP2-DT]] | +0.68 | +0.52 / +0.46 | both halves | 2e-05 |  |
| [[CCNT2]] | +0.68 | +0.73 / +0.47 | both halves | 2e-05 |  |
| [[IDNK]] | +0.67 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[BLOC1S2]] | +0.67 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[DPH6-DT]] | +0.66 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[C3orf38]] | +0.66 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[GIPC2]] | +0.66 | +0.57 / +0.42 | both halves | 4e-05 |  |
| [[TSTD3]] | +0.66 | +0.51 / +0.36 | both halves | 9e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DGKD]] | -0.70 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[DDX19A]] | -0.65 | -0.58 / -0.66 | both halves | 8e-06 |  |
| [[EML4]] | -0.62 | -0.57 / -0.38 | both halves | 6e-05 |  |
| [[TMEM104]] | -0.61 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[EHD4]] | -0.61 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[ATAD3B]] | -0.60 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[GNB1L]] | -0.59 | -0.38 / -0.50 | both halves | 6e-05 |  |
| [[GBA2]] | -0.59 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[CMIP]] | -0.59 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[POLR1E]] | -0.59 | -0.37 / -0.56 | both halves | 7e-05 |  |
| [[NUP98]] | -0.58 | -0.54 / -0.37 | both halves | 8e-05 |  |
| [[AP3M2]] | -0.58 | -0.47 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CA11]] | B | CA11 activity lowers RAB21's level | lines that do not express CA11 (6) vs lines expressing it (44) | 1.24× higher at baseline in the lines without CA11 | 0.060 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.625). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-0.0, 18.0); signed map (27.8, -15.4). **Vector** length 80.6, 26.2% of its response variance represented; |z| ≥ 3 in 1,250 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +7.3 | +5.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +6.5 | +3.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +7.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.3 | +0.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~6% of this change | +4.4 | -3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.9 | +5.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.8 | +1.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.6 | +0.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.6 | +0.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.6 | -0.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | -4.5 | -3.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | -1.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | -2.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -1.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.1 | +0.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.9 | +1.7 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | -1.7 | -4.3 |
|  | [[EX229 (drug)]] 5 µM |  | -1.7 | -0.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.6 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | RAB21, member RAS oncogene family |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q21.1 — chr12:71,754,863-71,800,286 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0118 |
| Gene groups (HGNC) | RAB, member RAS oncogene GTPases |
| Reactome | 5 pathways, smallest: RAB geranylgeranylation; RAB GEFs exchange GTP for GDP on RABs; Rab regulation of trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UL25](https://www.uniprot.org/uniprotkb/Q9UL25) (Ras-related protein Rab-21):

> The small GTPases Rab are key regulators of intracellular membrane trafficking, from the formation of transport vesicles to their fusion with membranes. Rabs cycle between an inactive GDP-bound form and an active GTP-bound form that is able to recruit to membranes different sets of downstream effectors directly responsible for vesicle formation, movement, tethering and fusion. RAB21 is involved in membrane trafficking control. During the mitosis of adherent cells, controls the endosomal …

**Summary**, from NCBI Gene [23011](https://www.ncbi.nlm.nih.gov/gene/23011):

> This gene belongs to the Rab family of monomeric GTPases, which are involved in the control of cellular membrane traffic. The encoded protein plays a role in the targeted trafficking of integrins via its association with integrin alpha tails. As a consequence, the encoded protein is involved in the regulation of cell adhesion and migration. Expression of this gene is associated with a poor prognosis for glioma patients. This gene is downregulated by the tumor suppressor miR-200b, and miRNA-200b …

**Accessions** — [HGNC:18263](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18263) · Entrez [23011](https://www.ncbi.nlm.nih.gov/gene/23011) · UniProt [Q9UL25](https://www.uniprot.org/uniprotkb/Q9UL25) · Ensembl [ENSG00000080371](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000080371)

## Data

Gene col 1280: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1280); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1280, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1280]; `tensor/DDL_lfc|DDL_z.npy` [1280]; `embed/gene_vectors.npy` [1280]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1280 or target_col == 1280). Every well: [[RAB21 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAB21.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
