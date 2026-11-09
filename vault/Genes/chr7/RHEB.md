---
symbol: "RHEB"
type: "gene"
col: 2784
ensembl_id: "ENSG00000106615"
name: "Ras homolog, mTORC1 binding"
location: "7q36.1"
module: 163
arm: "+"
pooled_cpm: 212.84
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 12
n_dd_up_clean: 9
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/163"]
generated_by: "tahoemap"
---

# RHEB

*Ras homolog, mTORC1 binding* — 7q36.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.71× (z +12.1, q 4e-31, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.606× (z -8.5, q 7e-15, down in 35 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.705× (z -6.2, q 2e-07, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RANBP9]] (+0.48, fdr 3e-05), [[AMBRA1]] (+0.48, fdr 3e-05), [[CUL3]] (+0.48, fdr 3e-05); moves opposite to [[NCBP2]] (-0.55, fdr 1e-05), [[ZNG1B]] (-0.54, fdr 2e-05), [[MYSM1]] (-0.51, fdr 3e-05).
> It is in [[Module 163]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2784.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.71×** | +12.1 | 4e-31 | 48/49 (C32, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.92×** | +11.1 | 2e-26 | 39/47 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.32×** | +11.1 | 2e-26 | 43/48 (SW480, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.79×** | +10.3 | 1e-22 | 45/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.60×** | +8.3 | 8e-15 | 41/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.59×** | +8.2 | 2e-14 | 42/48 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.55×** | +7.8 | 6e-13 | 43/48 (C32, PANC-1, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.46×** | +6.7 | 2e-09 | 36/48 (SNU-1, C32, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.35×** | +5.3 | 9e-06 | 34/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +4.8 | 9e-05 | 0/50 | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.33×** | +4.8 | 9e-05 | 28/48 (CFPAC-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.29×** | +3.5 | 0.024 | 24/48 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.21×** | +3.3 | 0.049 | 21/48 (NCI-H460, J82, …) | top dose only | composition shift |
| [[Auranofin (drug)]] 0.5 µM |  | 1.18× | +3.0 | 0.11 | 15/48 (C32, J82, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2784.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.606×** | -8.5 | 7e-15 | 35/44 (AsPC-1, C-33 A, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.705×** | -6.2 | 2e-07 | 37/48 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.712×** | -6.0 | 3e-07 | 38/48 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.718×** | -5.9 | 6e-07 | 33/49 (SW 1271, SW1417, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | **0.734×** | -5.3 | 1e-05 | 34/47 (SW1417, LoVo, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.816×** | -5.1 | 3e-05 | 26/48 (NCI-H23, Hs 766T, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **0.783×** | -4.3 | 0.001 | 31/48 (KATO III, NCI-H23, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.843× | -4.3 | 0.001 | 27/48 (SW1417, LS 180, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.806×** | -3.8 | 0.008 | 26/48 (PANC-1, AsPC-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.821×** | -3.5 | 0.024 | 23/48 (NCI-H2347, LS 180, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.870× | -3.5 | 0.024 | 19/48 (BT-474, MIA PaCa-2, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.816×** | -3.5 | 0.025 | 21/47 (SW480, Hs 766T, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.833×** | -3.2 | 0.052 | 22/48 (NCI-H23, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.835× | -3.2 | 0.054 | 18/49 (SW480, CHP-212, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.836× | -3.2 | 0.054 | 22/48 (NCI-H23, KATO III, …) | rises with dose |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | 0.834× | -3.1 | 0.068 | 20/49 (CFPAC-1, SNU-1, …) | top dose only | plate-row cell shift |
| [[Arbutin (drug)]] 0.05 µM |  | **0.829×** | -3.1 | 0.068 | 18/48 (LS 180, A-172, …) | inconsistent across doses |  |
| [[Bestatin (hydrochloride) (drug)]] 0.5 µM |  | 0.845× | -3.0 | 0.091 | 15/48 (C32, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2784. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 207 | 12 (6 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.85× (z +24.9) | — |
| [[PANC-1 (line)]] | alt | 201 | 8 (2 ⚠) | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.89× (z +16.5) | [[Panobinostat (drug)]] 5 µM 0.459× (z -12.0) |
| [[NCI-H23 (line)]] | alt | 246 | 5 (2 ⚠) | 3 (2 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.45× (z +11.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.504× (z -12.3) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.497× (z -8.9) |
| [[LoVo (line)]] | wt | 196 | 6 (2 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.76× (z +14.4) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.10× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.496× (z -10.0) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 186 | 7 (1 ⚠) | 0 | [[PH-797804 (drug)]] 5 µM 5.16× (z +14.3) | — |
| [[LS 180 (line)]] | wt | 146 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.66× (z +16.0) | — |
| [[SNU-423 (line)]] | alt | 173 | 6 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.76× (z +11.6) ⚠ toxic · without an alert: [[PH-797804 (drug)]] 5 µM 5.58× (z +10.7) | — |
| [[SW1417 (line)]] | alt | 424 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.30× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.374× (z -12.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 234 | 4 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 5.52× (z +15.6) | [[Dinaciclib (drug)]] 5 µM 0.358× (z -9.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 157 | 1 | 3 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 3.68× (z +8.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.412× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.434× (z -10.5) |
| [[A498 (line)]] | wt | 449 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.418× (z -9.9) |
| [[AsPC-1 (line)]] | alt | 293 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.231× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.424× (z -9.7) |
| [[C32 (line)]] | wt | 383 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 15.3× (z +13.1) | — |
| [[HOP62 (line)]] | alt | 154 | 3 | 0 | [[Digitoxin (drug)]] 0.5 µM 2.35× (z +9.2) | — |
| [[J82 (line)]] | alt | 226 | 3 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.27× (z +9.9) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.11× (z +9.4) | — |
| [[KATO III (line)]] | alt | 186 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.61× (z +13.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.54× (z +13.0) | — |
| [[Panc 03.27 (line)]] | alt | 184 | 2 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 5.20× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.417× (z -10.1) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 251 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.62× (z +10.2) | — |
| [[C-33 A (line)]] | alt | 200 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.303× (z -12.7) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 165 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 4.15× (z +12.9) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 10.2× (z +11.4) | — |
| [[Hs 766T (line)]] | wt | 183 | 1 (1 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.77× (z +10.3) ⚠ toxic | [[Selinexor (drug)]] 5 µM 0.538× (z -9.4) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H1573 (line)]] | alt | 88.4 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.33× (z +10.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.21× (z +9.8) | — |
| [[NCI-H1792 (line)]] | alt | 145 | 2 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.31× (z +11.1) ⚠ toxic | — |
| [[RKO (line)]] | wt | 225 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 5.54× (z +11.1) | — |
| [[SK-MEL-2 (line)]] | alt | 240 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.97× (z +11.7) | — |
| [[A-172 (line)]] | wt | 148 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 4.19× (z +8.7) | — |
| [[H4 (line)]] | wt | 194 | 1 | 0 | [[Digitoxin (drug)]] 0.5 µM 2.74× (z +8.7) | — |
| [[HT-29 (line)]] | alt | 348 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.530× (z -8.7) |
| [[LOX-IMVI (line)]] | wt | 144 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 5.91× (z +9.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 226 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 4.82× (z +8.9) | — |
| [[NCI-H2347 (line)]] | alt | 314 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.328× (z -11.0) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 170 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0851× (z -13.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 149 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 363 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 193 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 132 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 132 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 119 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 228 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 104 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 217 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 186 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 204 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 334 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 198 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 205 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 249 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2784), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RANBP9]] | +0.48 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[AMBRA1]] | +0.48 | +0.48 / +0.45 | both halves | 3e-05 | pathway: Autophagy; STRING 458 |
| [[CUL3]] | +0.48 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[MFSD14B]] | +0.47 | +0.58 / +0.41 | both halves | 4e-05 |  |
| [[SCAF4]] | +0.45 | +0.57 / +0.33 | both halves | 1e-04 |  |
| [[ZNF410]] | +0.45 | +0.57 / +0.42 | both halves | 4e-05 |  |
| [[DYRK1A]] | +0.45 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[SLC25A33]] | +0.44 | +0.50 / +0.37 | both halves | 8e-05 |  |
| [[MARCHF6]] | +0.44 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[KPNA1]] | +0.44 | +0.48 / +0.40 | both halves | 4e-05 |  |
| [[ACSL3]] | +0.44 | +0.48 / +0.37 | both halves | 7e-05 |  |
| [[ABHD12]] | +0.44 | +0.55 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCBP2]] | -0.55 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[ZNG1B]] | -0.54 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[MYSM1]] | -0.51 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[FNTA]] | -0.49 | -0.57 / -0.42 | both halves | 4e-05 | STRING 516 |
| [[ZNF160]] | -0.48 | -0.55 / -0.37 | both halves | 8e-05 |  |
| [[ZNF264]] | -0.47 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[ZNG1A]] | -0.47 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[LVRN]] | -0.45 | -0.56 / -0.33 | both halves | 1e-04 |  |
| [[UBE2V2]] | -0.45 | -0.47 / -0.36 | both halves | 9e-05 |  |
| [[AIMP1]] | -0.45 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[NOTCH2NLB]] | -0.45 | -0.54 / -0.33 | both halves | 1e-04 |  |
| [[ZNF638]] | -0.45 | -0.59 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 163]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.512). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.53; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-24.0, 17.8); signed map (-49.4, 23.8). **Vector** length 104, 37.9% of its response variance represented; |z| ≥ 3 in 1,228 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +5.5 | +11.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.2 | -0.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +3.6 | -2.7 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +3.3 | -0.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | -5.9 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +3.1 | +0.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | +0.5 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +2.7 | -0.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.7 | +7.8 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.2 | -0.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.9 | +10.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.6 | -0.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.5 | +5.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.0 | -2.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.0 | -0.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -3.3 | -0.3 |
|  | [[EX229 (drug)]] 5 µM |  | -3.0 | -2.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.9 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | Ras homolog, mTORC1 binding |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q36.1 — chr7:151,466,012-151,520,120 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously RHEB2 |
| Gene groups (HGNC) | RAS type GTPase family |
| Reactome | 15 pathways, smallest: mTORC1-mediated signalling; Energy dependent regulation of mTOR by LKB1-AMPK; MTOR signalling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15382](https://www.uniprot.org/uniprotkb/Q15382) (GTP-binding protein Rheb):

> Small GTPase that acts as an allosteric activator of the canonical mTORC1 complex, an evolutionarily conserved central nutrient sensor that stimulates anabolic reactions and macromolecule biosynthesis to promote cellular biomass generation and growth. In response to nutrients, growth factors or amino acids, specifically activates the protein kinase activity of MTOR, the catalytic component of the mTORC1 complex: acts by causing a conformational change that allows the alignment of residues in …

**Summary**, from NCBI Gene [6009](https://www.ncbi.nlm.nih.gov/gene/6009):

> This gene is a member of the small GTPase superfamily and encodes a lipid-anchored, cell membrane protein with five repeats of the RAS-related GTP-binding region. This protein is vital in regulation of growth and cell cycle progression due to its role in the insulin/TOR/S6K signaling pathway. The protein has GTPase activity and shuttles between a GDP-bound form and a GTP-bound form, and farnesylation of the protein is required for this activity. Three pseudogenes have been mapped, two on …

**Accessions** — [HGNC:10011](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10011) · Entrez [6009](https://www.ncbi.nlm.nih.gov/gene/6009) · UniProt [Q15382](https://www.uniprot.org/uniprotkb/Q15382) · Ensembl [ENSG00000106615](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106615)

## Data

Gene col 2784: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2784); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2784, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2784]; `tensor/DDL_lfc|DDL_z.npy` [2784]; `embed/gene_vectors.npy` [2784]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2784 or target_col == 2784). Every well: [[RHEB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RHEB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
