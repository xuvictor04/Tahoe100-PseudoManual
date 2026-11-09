---
symbol: "MDN1"
type: "gene"
col: 3328
ensembl_id: "ENSG00000112159"
name: "midasin AAA ATPase 1"
location: "6q15"
module: 18
arm: "+"
pooled_cpm: 120.57
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 5
n_dd_up_clean: 16
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# MDN1

*midasin AAA ATPase 1* — 6q15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (9 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.94× (z +14.2, q 7e-43, up in 47 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.80× (z +12.6, q 5e-34, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.844× (z -5.2, q 9e-05, down in 21 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HEATR1]] (+0.86, fdr 7e-06), [[TSEN2]] (+0.83, fdr 7e-06), [[DKC1]] (+0.83, fdr 7e-06); moves opposite to [[MXD1]] (-0.63, fdr 7e-06).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[ADCY3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3328.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.94×** | +14.2 | 7e-43 | 47/48 (NCI-H460, A498, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.80×** | +12.6 | 5e-34 | 44/48 (NCI-H1573, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.69×** | +11.3 | 4e-27 | 37/48 (LS 180, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.65×** | +10.8 | 6e-25 | 43/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.64×** | +10.6 | 2e-24 | 39/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.28×** | +9.2 | 2e-18 | 39/48 (PANC-1, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +8.7 | 3e-16 | 39/47 (NCI-H1792, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[EX229 (drug)]] 5 µM |  | **1.96×** | +7.5 | 4e-12 | 40/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.87×** | +7.0 | 2e-10 | 33/49 (SK-MEL-2, COLO 205, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.84×** | +6.8 | 6e-10 | 36/48 (NCI-H1792, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.36×** | +6.6 | 2e-09 | 30/48 (A-172, C32, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.33×** | +6.1 | 5e-08 | 29/48 (Hs 766T, HS-578T, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.33×** | +5.9 | 2e-07 | 33/48 (NCI-H1792, NCI-H23, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.31×** | +5.7 | 4e-07 | 27/48 (A-172, NCI-H1792, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.60×** | +5.3 | 6e-06 | 29/48 (NCI-H460, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.36×** | +4.6 | 1e-04 | 28/48 (NCI-H460, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[Budesonide (drug)]] 5 µM |  | **1.22×** | +4.3 | 5e-04 | 21/48 (NCI-H1792, A498, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.44×** | +4.1 | 0.001 | 24/48 (AsPC-1, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.21×** | +4.1 | 0.001 | 20/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Dexamethasone (drug)]] 5 µM |  | 1.19× | +3.6 | 0.007 | 18/48 (SHP-77, A498, …) | all doses, flat | position effect removed |
| [[Dexamethasone (drug)]] 0.5 µM |  | 1.17× | +3.4 | 0.017 | 15/48 (SHP-77, hTERT-HPNE, …) | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠; shown: the 15 strongest. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3328.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | 0.844× | -5.2 | 9e-05 | 21/48 (A498, LS 180, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.846× | -5.1 | 9e-05 | 22/49 (RKO, MIA PaCa-2, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.793×** | -5.0 | 1e-04 | 24/49 (LS 180, SNU-423, …) | rises with dose |  |
| [[Entrectinib (drug)]] 5 µM |  | **0.807×** | -4.6 | 5e-04 | 25/48 (KATO III, HT-29, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.838× | -4.4 | 0.001 | 22/48 (LoVo, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.822×** | -4.2 | 0.002 | 23/48 (RKO, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.772×** | -4.0 | 0.006 | 24/48 (Hs 766T, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.843× | -3.7 | 0.016 | 20/47 (A498, LoVo, …) | two highest doses | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.844× | -3.5 | 0.026 | 18/48 (MIA PaCa-2, A-427, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.867× | -3.4 | 0.032 | 16/48 (MIA PaCa-2, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.801×** | -3.4 | 0.032 | 19/48 (LoVo, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.855× | -3.4 | 0.033 | 19/49 (LoVo, MIA PaCa-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | 0.901× | -3.2 | 0.059 | 20/48 (C32, SW48, …) | top dose only | composition shift |
| [[Ponatinib (drug)]] 0.05 µM |  | 0.863× | -3.2 | 0.059 | 14/48 (A-427, J82, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.868× | -3.0 | 0.081 | 17/49 (LoVo, CHP-212, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3328. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 228 | 6 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.44× (z +12.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.559× (z -11.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 245 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -14.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.433× (z -9.7) |
| [[HT-29 (line)]] | alt | 102 | 5 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.06× (z +12.4) | — |
| [[NCI-H1573 (line)]] | alt | 58.3 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.27× (z +13.6) | — |
| [[NCI-H1792 (line)]] | alt | 81.0 | 5 (3 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.75× (z +12.7) ⚠ toxic · without an alert: [[Belumosudil (drug)]] 5 µM 3.16× (z +11.0) | — |
| [[NCI-H460 (line)]] | wt | 112 | 4 (2 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.64× (z +12.0) ⚠ unreliable plate only · without an alert: [[Digitoxin (drug)]] 0.05 µM 2.32× (z +10.4) | — |
| [[SW480 (line)]] | alt | 159 | 4 (1 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 2.34× (z +11.1) | — |
| [[C-33 A (line)]] | alt | 302 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.282× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change |
| [[SW48 (line)]] | wt | 241 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -11.7) ⚠ cell-cycle shift, explains ~55% of this change |
| [[A-172 (line)]] | wt | 46.8 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +9.3) ⚠ cell-cycle shift, explains ~55% of this change | — |
| [[C32 (line)]] | wt | 101 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.482× (z -12.3) ⚠ cell-cycle shift, explains ~55% of this change |
| [[CFPAC-1 (line)]] | alt | 39.5 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.82× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[Hs 766T (line)]] | wt | 67.0 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.97× (z +9.6) | — |
| [[LS 180 (line)]] | wt | 114 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.61× (z +13.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 253 | 1 (1 ⚠) | 1 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.45× (z +10.0) ⚠ unreliable plate only | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -12.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 197 | 1 | 1 (1 ⚠) | [[Belumosudil (drug)]] 5 µM 1.88× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.573× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 45.5 | 2 (2 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.84× (z +10.3) ⚠ unreliable plate only | — |
| [[Panc 03.27 (line)]] | alt | 67.1 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.88× (z +10.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 120 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.29× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.514× (z -10.6) ⚠ cell-cycle shift, explains ~55% of this change |
| [[A-427 (line)]] | wt | 199 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 3.72× (z +8.9) | — |
| [[A498 (line)]] | wt | 53.5 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.48× (z +11.6) ⚠ unreliable plate only | — |
| [[A549 (line)]] | wt | 87.7 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +8.5) | — |
| [[AsPC-1 (line)]] | alt | 53.5 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.77× (z +11.2) ⚠ unreliable plate only | — |
| [[H4 (line)]] | wt | 51.1 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.90× (z +9.6) | — |
| [[HEC-1-A (line)]] | alt | 154 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.462× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 70.1 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.50× (z +9.4) ⚠ unreliable plate only | — |
| [[J82 (line)]] | alt | 105 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +9.8) | — |
| [[LoVo (line)]] | wt | 113 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.06× (z +8.5) | — |
| [[NCI-H2030 (line)]] | alt | 161 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.24× (z +8.7) | — |
| [[RPMI-7951 (line)]] | alt | 103 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.22× (z +8.6) ⚠ unreliable plate only | — |
| [[SNU-1 (line)]] | wt | 191 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.299× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 127 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.49× (z +9.9) | — |
| [[SW 1088 (line)]] | alt | 75.4 | 0 | 1 | — | [[Flutamide (drug)]] 0.5 µM 0.0806× (z -8.5) |
| [[AN3 CA (line)]] | alt | 250 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 177 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 87.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 77.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 64.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 102 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 157 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 90.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 205 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 190 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 65.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 83.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3328), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HEATR1]] | +0.86 | +0.85 / +0.85 | both halves | 7e-06 | STRING 579 |
| [[TSEN2]] | +0.83 | +0.82 / +0.82 | both halves | 7e-06 |  |
| [[DKC1]] | +0.83 | +0.84 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[PUM3]] | +0.81 | +0.73 / +0.86 | both halves | 7e-06 | **novel candidate** |
| [[URB1]] | +0.81 | +0.81 / +0.80 | both halves | 7e-06 | STRING 443 |
| [[POLR1A]] | +0.80 | +0.73 / +0.82 | both halves | 7e-06 | STRING 486 |
| [[URB2]] | +0.79 | +0.83 / +0.75 | both halves | 7e-06 |  |
| [[CAD]] | +0.79 | +0.75 / +0.79 | both halves | 7e-06 |  |
| [[DHX33]] | +0.78 | +0.85 / +0.77 | both halves | 7e-06 |  |
| [[MYBBP1A]] | +0.77 | +0.74 / +0.78 | both halves | 7e-06 |  |
| [[CMSS1]] | +0.77 | +0.76 / +0.78 | both halves | 7e-06 |  |
| [[KLHDC4]] | +0.77 | +0.73 / +0.78 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MXD1]] | -0.63 | -0.59 / -0.68 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADCY3]] | B | ADCY3 activity raises MDN1's level | lines that do not express ADCY3 (5) vs lines expressing it (45) | 1.32× lower at baseline in the lines without ADCY3 | 0.022 | ⚠ within organs, on part of the lines; also absent: PPP2R3A, TBC1D19, SSBP2 |
| [[PDE3B]] | B | PDE3B activity raises MDN1's level | lines that do not express PDE3B (20) vs lines expressing it (30) | 1.48× lower at baseline in the lines without PDE3B | 0.075 | ⚠ within organs, on part of the lines; also absent: ENSG00000250049, MIR4458HG, ASB4 |
| [[WNK2]] | B | WNK2 activity raises MDN1's level | lines that do not express WNK2 (16) vs lines expressing it (34) | 1.70× lower at baseline in the lines without WNK2 | 0.086 | ⚠ within organs, on part of the lines; also absent: NUP210, SLC27A2, CHDH |
| [[MEX3A]] | B | MEX3A activity raises MDN1's level | lines that do not express MEX3A (6) vs lines expressing it (44) | 1.47× lower at baseline in the lines without MEX3A | 0.090 | ⚠ within organs, on part of the lines; also absent: SNTA1, POGLUT3, FMNL3; maybe low, not absent |
| [[MTHFD1L]], [[USP31]] | C | MTHFD1L, USP31 activity raises MDN1's level | lines that do not express MTHFD1L, USP31 (3) vs lines expressing them (47) | 2.58× lower at baseline in the lines without MTHFD1L, USP31 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MIR3659HG, SLC4A7, HCN2; maybe low, not absent; its own permutation p; co-absent genes |
| [[PPARGC1B]] | C | PPARGC1B activity raises MDN1's level | lines that do not express PPARGC1B (3) vs lines expressing it (47) | 2.05× lower at baseline in the lines without PPARGC1B | 0.092 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SLC4A7, SPDL1, ARHGAP10; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.829). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-11.5, -37.2); signed map (-5.0, -50.8). **Vector** length 141, 50.4% of its response variance represented; |z| ≥ 3 in 1,444 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Nucleotide biosynthesis* (reactome, mean cos +0.66 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +11.7 | +14.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +7.0 | +5.9 |
|  | [[EX229 (drug)]] 5 µM |  | +6.7 | +7.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +6.1 | +6.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +5.4 | +8.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | +4.9 | +4.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.5 | +3.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | -8.8 | -3.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.8 | +1.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | -4.4 | -5.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | -2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.0 | -5.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.8 | -3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.7 | -2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.3 | -3.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.2 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | midasin AAA ATPase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q15 — chr6:89,642,498-89,819,794 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0301, Rea1 |
| Gene groups (HGNC) | AAA ATPases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NU22](https://www.uniprot.org/uniprotkb/Q9NU22) (Midasin):

> Nuclear chaperone required for maturation and nuclear export of pre-60S ribosome subunits. Functions at successive maturation steps to remove ribosomal factors at critical transition points, first driving the exit of early pre-60S particles from the nucleolus and then driving late pre-60S particles from the nucleus (By similarity). At an early stage in 60S maturation, mediates the dissociation of the PeBoW complex (PES1-BOP1-WDR12) from early pre-60S particles, rendering them competent for …

**Summary**, from NCBI Gene [23195](https://www.ncbi.nlm.nih.gov/gene/23195):

> Predicted to enable ATP hydrolysis activity. Involved in ribosomal large subunit assembly. Located in nucleolus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:18302](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18302) · Entrez [23195](https://www.ncbi.nlm.nih.gov/gene/23195) · UniProt [Q9NU22](https://www.uniprot.org/uniprotkb/Q9NU22) · Ensembl [ENSG00000112159](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112159)

## Data

Gene col 3328: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3328); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3328, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3328]; `tensor/DDL_lfc|DDL_z.npy` [3328]; `embed/gene_vectors.npy` [3328]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3328 or target_col == 3328). Every well: [[MDN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MDN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
