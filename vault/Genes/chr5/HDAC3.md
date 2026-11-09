---
symbol: "HDAC3"
type: "gene"
col: 10151
ensembl_id: "ENSG00000171720"
name: "histone deacetylase 3"
location: "5q31.3"
module: 99
arm: "+"
pooled_cpm: 71.8
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 11
n_dd_up_clean: 11
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 599
tags: ["gene", "module/099"]
generated_by: "tahoemap"
---

# HDAC3

*histone deacetylase 3* — 5q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (9 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 2.83× (z +12.2, q 1e-31, up in 47 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.57× (z +11.1, q 4e-26, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.561× (z -9.6, q 3e-19, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDK3]] (+0.79, fdr 7e-06), [[HERC3]] (+0.78, fdr 7e-06), [[FAM162A]] (+0.77, fdr 7e-06); moves opposite to [[FIZ1]] (-0.72, fdr 1e-05), [[EPC2]] (-0.72, fdr 7e-06), [[ZNF268]] (-0.71, fdr 7e-06).
> It is in [[Module 099]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[NOG]] → it (grade B ⚠); 599 go from it, the strongest it → [[CDC23]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10151.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.83×** | +12.2 | 1e-31 | 47/48 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.57×** | +11.1 | 4e-26 | 45/48 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.25×** | +9.5 | 4e-19 | 42/48 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.19×** | +9.2 | 5e-18 | 46/48 (SW480, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.08×** | +8.6 | 1e-15 | 39/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.04×** | +8.3 | 7e-15 | 39/48 (SW480, A498, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.85×** | +7.2 | 6e-11 | 39/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.62×** | +5.7 | 1e-06 | 30/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.57×** | +5.3 | 8e-06 | 35/48 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +4.9 | 6e-05 | 37/48 (RKO, KATO III, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.34×** | +4.8 | 8e-05 | 31/49 (NCI-H2347, SW1417, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.46×** | +4.4 | 4e-04 | 33/48 (LS 180, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.46×** | +4.4 | 4e-04 | 25/47 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.98×** | +4.2 | 0.001 | 28/48 (SHP-77, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.42×** | +4.1 | 0.002 | 29/48 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.41×** | +3.8 | 0.004 | 29/49 (NCI-H460, HEC-1-A, …) | top dose only | plate-row cell shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.37×** | +3.7 | 0.007 | 28/49 (CHP-212, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **1.34×** | +3.3 | 0.029 | 27/48 (NCI-H460, HEC-1-A, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10151.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.561×** | -9.6 | 3e-19 | 35/48 (NCI-H1792, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.619×** | -5.7 | 4e-06 | 35/48 (C32, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.665×** | -4.6 | 7e-04 | 29/48 (A-172, C32, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.679×** | -4.4 | 0.002 | 29/43 (SK-MEL-2, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.728×** | -3.8 | 0.019 | 26/48 (HOP62, RKO, …) | inconsistent across doses |  |
| [[Apalutamide (drug)]] 0.5 µM |  | **0.749×** | -3.4 | 0.051 | 23/48 (HOP62, RKO, …) | inconsistent across doses |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | **0.750×** | -3.4 | 0.051 | 26/48 (LOX-IMVI, RKO, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.756×** | -3.3 | 0.063 | 22/48 (HOP62, NCI-H1573, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.752×** | -3.3 | 0.070 | 21/47 (C32, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.762×** | -3.2 | 0.070 | 26/48 (CFPAC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **0.770×** | -3.1 | 0.100 | 21/48 (HOP62, RKO, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | 0.834× | -3.1 | 0.10 | 23/48 (SK-MEL-2, C32, …) | rises with dose | low cells (technical?) |
| [[Demeclocycline (drug)]] 5 µM |  | 0.835× | -3.0 | 0.10 | 22/48 (SW1417, A498, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10151. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 60.8 | 9 (4 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.22× (z +18.0) | [[Homoharringtonine (drug)]] 5 µM 0.533× (z -9.6) |
| [[SW480 (line)]] | alt | 53.9 | 9 (5 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.56× (z +17.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.25× (z +17.0) | — |
| [[NCI-H460 (line)]] | wt | 81.8 | 7 (2 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 10.0× (z +17.4) | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -10.3) |
| [[KATO III (line)]] | alt | 37.6 | 7 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 11.8× (z +20.3) | — |
| [[PANC-1 (line)]] | alt | 45.3 | 7 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.86× (z +19.8) | — |
| [[COLO 205 (line)]] | alt | 33.0 | 5 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.58× (z +11.0) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.30× (z +9.3) | — |
| [[HOP62 (line)]] | alt | 97.9 | 4 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.71× (z +11.7) | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -9.6) |
| [[SW1417 (line)]] | alt | 93.1 | 5 (4 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.92× (z +10.6) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.83× (z +10.3) | — |
| [[A498 (line)]] | wt | 34.6 | 3 (3 ⚠) | 1 | [[Panobinostat (drug)]] 0.5 µM 3.36× (z +10.5) ⚠ cell-cycle shift, explains ~31% of this change | [[Homoharringtonine (drug)]] 5 µM 0.491× (z -8.7) |
| [[LS 180 (line)]] | wt | 61.3 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.71× (z +12.5) | — |
| [[NCI-H1792 (line)]] | alt | 74.3 | 3 (1 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 6.58× (z +12.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 5.92× (z +11.8) | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -16.3) |
| [[NCI-H23 (line)]] | alt | 45.7 | 4 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.84× (z +11.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.80× (z +8.6) | — |
| [[A-172 (line)]] | wt | 73.7 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.208× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.272× (z -9.5) |
| [[A-427 (line)]] | wt | 53.9 | 3 (3 ⚠) | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +9.2) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[HT-29 (line)]] | alt | 40.4 | 3 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.39× (z +9.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 57.3 | 2 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.26× (z +11.9) | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -11.5) |
| [[C-33 A (line)]] | alt | 75.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.135× (z -14.0) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 94.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -12.4) |
| [[H4 (line)]] | wt | 67.6 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.37× (z +9.6) | — |
| [[HEC-1-A (line)]] | alt | 123 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.25× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.387× (z -9.7) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 55.4 | 1 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.32× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -10.3) |
| [[NCI-H2347 (line)]] | alt | 95.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +9.8) ⚠ cell-cycle shift, explains ~29% of this change | [[Dinaciclib (drug)]] 5 µM 0.373× (z -9.5) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 61.2 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.01× (z +9.6) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 98.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0843× (z -17.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.442× (z -8.6) |
| [[SW 1088 (line)]] | alt | 91.5 | 0 | 2 | — | [[Entrectinib (drug)]] 5 µM 0.0595× (z -10.2) |
| [[AsPC-1 (line)]] | alt | 72.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -10.4) |
| [[CFPAC-1 (line)]] | alt | 122 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -9.5) |
| [[CHP-212 (line)]] | wt | 68.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.103× (z -9.4) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 52.5 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.85× (z +8.9) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 81.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -9.2) |
| [[HS-578T (line)]] | alt | 94.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -8.6) |
| [[hTERT-HPNE (line)]] | wt | 68.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 132 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -12.8) |
| [[NCI-H2030 (line)]] | alt | 67.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -8.8) |
| [[SHP-77 (line)]] | alt | 58.2 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.326× (z -8.8) |
| [[SNU-1 (line)]] | wt | 71.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.233× (z -8.5) |
| [[A549 (line)]] | wt | 63.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 136 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 68.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 86.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 80.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 89.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 68.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 84.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 74.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 76.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 93.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 111 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10151), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDK3]] | +0.79 | +0.82 / +0.71 | both halves | 7e-06 | pathway: Signaling by Nuclear Receptors |
| [[HERC3]] | +0.78 | +0.77 / +0.74 | both halves | 7e-06 |  |
| [[FAM162A]] | +0.77 | +0.80 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_P53_PATHWAY |
| [[PDXP]] | +0.77 | +0.72 / +0.69 | both halves | 7e-06 |  |
| [[INSIG2]] | +0.76 | +0.75 / +0.77 | both halves | 7e-06 |  |
| [[UBE2O]] | +0.75 | +0.78 / +0.63 | both halves | 7e-06 |  |
| [[PDK1]] | +0.75 | +0.86 / +0.64 | both halves | 7e-06 | pathway: Signaling by Nuclear Receptors |
| [[FBXO42]] | +0.75 | +0.79 / +0.70 | both halves | 7e-06 |  |
| [[PMS2P3-1]] | +0.74 | +0.82 / +0.57 | both halves | 9e-06 |  |
| [[SAP30-DT]] | +0.73 | +0.72 / +0.76 | both halves | 7e-06 |  |
| [[RAB6A]] | +0.72 | +0.78 / +0.65 | both halves | 7e-06 | pathway: Signaling by NOTCH |
| [[WDR45B]] | +0.72 | +0.74 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FIZ1]] | -0.72 | -0.75 / -0.53 | both halves | 1e-05 |  |
| [[EPC2]] | -0.72 | -0.58 / -0.73 | both halves | 7e-06 |  |
| [[ZNF268]] | -0.71 | -0.67 / -0.68 | both halves | 7e-06 |  |
| [[ZNF140]] | -0.70 | -0.64 / -0.67 | both halves | 7e-06 |  |
| [[MIS12]] | -0.70 | -0.71 / -0.58 | both halves | 7e-06 |  |
| [[SRCAP]] | -0.69 | -0.62 / -0.69 | both halves | 7e-06 |  |
| [[RBM23]] | -0.69 | -0.68 / -0.58 | both halves | 7e-06 |  |
| [[INTS14]] | -0.69 | -0.70 / -0.54 | both halves | 1e-05 |  |
| [[ZXDB]] | -0.69 | -0.66 / -0.55 | both halves | 1e-05 |  |
| [[TASOR]] | -0.69 | -0.74 / -0.48 | both halves | 2e-05 | pathway: Epigenetic regulation of gene expression |
| [[ZNF764]] | -0.68 | -0.69 / -0.50 | both halves | 1e-05 |  |
| [[FKRP]] | -0.68 | -0.73 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NOG]] | B | NOG activity raises HDAC3's level | lines that do not express NOG (26) vs lines expressing it (24) | 1.19× lower at baseline in the lines without NOG | 0.084 | ⚠ within organs, on part of the lines; also absent: LINC01776, ENSG00000279289, FLI1 |
| [[SNTA1]] | B | SNTA1 activity raises HDAC3's level | lines that do not express SNTA1 (5) vs lines expressing it (45) | 1.42× lower at baseline in the lines without SNTA1 | 0.091 | ⚠ within organs, on part of the lines; also absent: SACS, CLTCL1, MXRA7; maybe low, not absent |

### Downstream of this gene

*599 arrows, 599 of them with an alert ⚠; grade A 0, B 599, C 0. Shown: the 12 strongest; 587 more arrows (587 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDC23]] | B | [[HDAC1]], [[HDAC2]], HDAC3, [[HDAC8]], [[HDAC10]], [[HDAC11]] activity raises CDC23's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[CMIP]] | B | [[HDAC1]], [[HDAC2]], HDAC3, [[HDAC8]], [[HDAC10]], [[HDAC11]] activity lowers CMIP's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[CROCCP3]] | B | [[HDAC1]], [[HDAC2]], HDAC3, [[HDAC8]], [[HDAC10]], [[HDAC11]] activity lowers CROCCP3's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[CYB561]] | B | [[HDAC1]], [[HDAC2]], HDAC3, [[HDAC8]], [[HDAC10]], [[HDAC11]] activity raises CYB561's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[DNAJC2]] | B | [[HDAC1]], [[HDAC2]], HDAC3, [[HDAC8]], [[HDAC10]], [[HDAC11]] activity raises DNAJC2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[ENSG00000288899]] | B | [[HDAC1]], [[HDAC2]], HDAC3, [[HDAC8]], [[HDAC10]], [[HDAC11]] activity raises ENSG00000288899's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[FAM78B]] | B | [[HDAC1]], [[HDAC2]], HDAC3, [[HDAC8]], [[HDAC10]], [[HDAC11]] activity lowers FAM78B's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[FBXW9]] | B | [[HDAC1]], [[HDAC2]], HDAC3, [[HDAC8]], [[HDAC10]], [[HDAC11]] activity raises FBXW9's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[FMN1]] | B | [[HDAC1]], [[HDAC2]], HDAC3, [[HDAC8]], [[HDAC10]], [[HDAC11]] activity lowers FMN1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[LRRC51]] | B | [[HDAC1]], [[HDAC2]], HDAC3, [[HDAC8]], [[HDAC10]], [[HDAC11]] activity raises LRRC51's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[MRPS7]] | B | [[HDAC1]], [[HDAC2]], HDAC3, [[HDAC8]], [[HDAC10]], [[HDAC11]] activity raises MRPS7's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[NCBP3]] | B | [[HDAC1]], [[HDAC2]], HDAC3, [[HDAC8]], [[HDAC10]], [[HDAC11]] activity raises NCBP3's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

## Where it sits

- **Module**: [[Module 099]] — hypoxia; 48 genes; every member is in the + arm (projection on the module's main direction 0.776). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (9.9, -16.7); signed map (-36.3, 23.1). **Vector** length 134, 49.4% of its response variance represented; |z| ≥ 3 in 1,188 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Regulation of pyruvate metabolism* (reactome, mean cos +0.53 to 4); *Pyruvate metabolism* (reactome, mean cos +0.53 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.8 | +4.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +7.9 | +9.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +7.8 | +9.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +7.2 | +8.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.9 | +3.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.3 | +2.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.1 | +1.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.9 | +4.2 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +2.8 | +3.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -14.2 | -9.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -13.3 | -4.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -12.1 | -5.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.6 | +0.9 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | +2.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.4 | -2.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.3 | +2.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.2 | -2.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.1 | -2.5 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -2.6 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | histone deacetylase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.3 — chr5:141,620,876-141,636,849 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RPD3, HD3, RPD3-2, KDAC3 |
| Gene groups (HGNC) | Histone deacetylases, class I; NCoR/SMRT transcriptional repression complex subunits |
| Hallmark sets | P53_PATHWAY |
| Reactome | 69 pathways, smallest: p75NTR negatively regulates cell cycle via SC1; Loss of MECP2 binding ability to the NCoR/SMRT complex; STAT3 nuclear events downstream of ALK signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [O15379](https://www.uniprot.org/uniprotkb/O15379) (Histone deacetylase 3):

> Histone deacetylase that catalyzes the deacetylation of lysine residues on the N-terminal part of the core histones (H2A, H2B, H3 and H4), and some other non-histone substrates. Histone deacetylation gives a tag for epigenetic repression and plays an important role in transcriptional regulation, cell cycle progression and developmental events. Histone deacetylases act via the formation of large multiprotein complexes, such as N-Cor repressor complex, which activate the histone deacetylase …

**Summary**, from NCBI Gene [8841](https://www.ncbi.nlm.nih.gov/gene/8841):

> Histones play a critical role in transcriptional regulation, cell cycle progression, and developmental events. Histone acetylation/deacetylation alters chromosome structure and affects transcription factor access to DNA. The protein encoded by this gene belongs to the histone deacetylase/acuc/apha family. It has histone deacetylase activity and represses transcription when tethered to a promoter. It may participate in the regulation of transcription through its binding with the zinc-finger …

**Accessions** — [HGNC:4854](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4854) · Entrez [8841](https://www.ncbi.nlm.nih.gov/gene/8841) · UniProt [O15379](https://www.uniprot.org/uniprotkb/O15379) · Ensembl [ENSG00000171720](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171720)

## Data

Gene col 10151: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10151); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10151, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10151]; `tensor/DDL_lfc|DDL_z.npy` [10151]; `embed/gene_vectors.npy` [10151]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10151 or target_col == 10151). Every well: [[HDAC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HDAC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
