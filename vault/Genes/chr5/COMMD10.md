---
symbol: "COMMD10"
type: "gene"
col: 7026
ensembl_id: "ENSG00000145781"
name: "COMM domain containing 10"
location: "5q23.1"
module: 1
arm: "+"
pooled_cpm: 138.71
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 16
n_dd_up_clean: 7
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# COMMD10

*COMM domain containing 10* — 5q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.54× (z +7.5, q 5e-11, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.630× (z -11.3, q 6e-27, down in 40 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEMA6A-AS1]] (+0.77, fdr 7e-06, ⚠ same locus), [[PRH1]] (+0.76, fdr 7e-06), [[DDX10]] (+0.74, fdr 7e-06), [[THADA]] (+0.73, fdr 7e-06); moves opposite to [[SRP54-AS1]] (-0.74, fdr 7e-06), [[APAF1]] (-0.73, fdr 7e-06), [[KMT5C]] (-0.66, fdr 7e-06).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7026.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.54×** | +7.5 | 5e-11 | 36/48 (NCI-H1573, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.48×** | +6.8 | 3e-09 | 42/48 (NCI-H2347, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.25×** | +5.5 | 7e-06 | 26/48 (COLO 205, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.35×** | +4.9 | 2e-04 | 40/47 (LOX-IMVI, HEC-1-A, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.30×** | +4.5 | 9e-04 | 27/48 (C32, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **1.60×** | +4.2 | 0.002 | 32/48 (SK-MEL-2, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.27×** | +4.0 | 0.005 | 29/48 (NCI-H2347, C-33 A, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.25×** | +3.9 | 0.008 | 26/48 (C32, AsPC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | 1.21× | +3.1 | 0.13 | 19/48 (CFPAC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | 1.40× | +3.0 | 0.13 | 24/49 (NCI-H460, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 9 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7026.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.630×** | -11.3 | 6e-27 | 40/49 (LOX-IMVI, SNU-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.542×** | -10.2 | 7e-22 | 43/47 (RKO, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.630×** | -7.7 | 2e-12 | 41/48 (LOX-IMVI, RKO, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.641×** | -7.7 | 2e-12 | 38/48 (MIA PaCa-2, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.654×** | -7.1 | 2e-10 | 42/50 (A-427, SW48, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.685×** | -6.5 | 5e-09 | 38/48 (J82, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.689×** | -6.4 | 9e-09 | 35/48 (HEC-1-A, MIA PaCa-2, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~21% of this change | **0.782×** | -4.3 | 0.001 | 31/48 (KATO III, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.791×** | -4.1 | 0.003 | 30/48 (J82, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.794×** | -4.0 | 0.004 | 28/48 (MIA PaCa-2, NCI-H1573, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.708×** | -3.7 | 0.009 | 26/48 (MIA PaCa-2, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **0.807×** | -3.7 | 0.009 | 24/48 (NCI-H1573, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | **0.809×** | -3.5 | 0.017 | 22/44 (NCI-H1573, SNU-1, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.822×** | -3.4 | 0.026 | 23/48 (NCI-H1573, C32, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **0.733×** | -3.4 | 0.028 | 22/49 (SK-MEL-2, A-427, …) | rises with dose | composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.692×** | -3.3 | 0.030 | 27/49 (SNU-1, COLO 205, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7026. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 131 | 4 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 18.1× (z +40.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.324× (z -10.6) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 106 | 3 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.68× (z +29.2) | [[Dinaciclib (drug)]] 5 µM 0.0941× (z -24.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change |
| [[NCI-H460 (line)]] | wt | 173 | 2 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +11.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.547× (z -11.6) |
| [[SK-MEL-2 (line)]] | alt | 358 | 2 | 4 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 4.36× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.347× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.470× (z -9.9) |
| [[A-427 (line)]] | wt | 230 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.251× (z -17.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.328× (z -13.9) |
| [[LOX-IMVI (line)]] | wt | 184 | 1 | 4 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.11× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.392× (z -16.5) |
| [[NCI-H23 (line)]] | alt | 140 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.417× (z -13.0) |
| [[C32 (line)]] | wt | 183 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -13.3) |
| [[HEC-1-A (line)]] | alt | 209 | 1 | 3 (2 ⚠) | [[Auranofin (drug)]] 5 µM 1.87× (z +8.9) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.519× (z -9.0) |
| [[RKO (line)]] | wt | 146 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +9.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.324× (z -11.2) ⚠ toxic · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.347× (z -10.5) |
| [[AsPC-1 (line)]] | alt | 104 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.82× (z +28.5) | — |
| [[NCI-H2347 (line)]] | alt | 127 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +13.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.543× (z -9.5) |
| [[PANC-1 (line)]] | alt | 169 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.519× (z -13.6) |
| [[HOP62 (line)]] | alt | 118 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.495× (z -12.4) |
| [[J82 (line)]] | alt | 128 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.516× (z -10.8) |
| [[KATO III (line)]] | alt | 155 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.435× (z -10.9) ⚠ transcription drop; cell-cycle shift, explains ~21% of this change |
| [[LoVo (line)]] | wt | 163 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +18.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 172 | 0 | 2 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.429× (z -9.7) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H2030 (line)]] | alt | 64.4 | 1 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 2.76× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.507× (z -8.6) |
| [[SNU-1 (line)]] | wt | 193 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0973× (z -21.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -14.0) |
| [[SW48 (line)]] | wt | 164 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.325× (z -13.4) |
| [[SW480 (line)]] | alt | 145 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.22× (z +14.9) | — |
| [[C-33 A (line)]] | alt | 118 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.131× (z -18.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change |
| [[H4 (line)]] | wt | 174 | 1 | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 1.91× (z +8.5) | — |
| [[HepG2_C3A (line)]] | wt | 139 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.375× (z -9.6) ⚠ toxic |
| [[HT-29 (line)]] | alt | 81.7 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.410× (z -8.8) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 126 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.506× (z -10.0) |
| [[SHP-77 (line)]] | alt | 145 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -12.2) |
| [[SNU-423 (line)]] | alt | 112 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.414× (z -8.8) ⚠ toxic |
| [[SW 1271 (line)]] | alt | 219 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -8.9) |
| [[SW 900 (line)]] | alt | 81.0 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.387× (z -9.2) |
| [[SW1417 (line)]] | alt | 96.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.548× (z -9.2) |
| [[A-172 (line)]] | wt | 78.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 64.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 114 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 202 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 82.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 149 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 87.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 113 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 102 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 186 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 84.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 157 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7026), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEMA6A-AS1]] | +0.77 | +0.73 / +0.76 | both halves | 7e-06 | ⚠ same locus (34.8 kb, same strand: neighbours can correlate without regulation) |
| [[PRH1]] | +0.76 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[DDX10]] | +0.74 | +0.78 / +0.79 | both halves | 7e-06 |  |
| [[THADA]] | +0.73 | +0.80 / +0.60 | both halves | 7e-06 |  |
| [[STAG1]] | +0.73 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[UTP20]] | +0.72 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[JPX]] | +0.71 | +0.75 / +0.60 | both halves | 7e-06 |  |
| [[INO80]] | +0.70 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[TTC27]] | +0.68 | +0.73 / +0.58 | both halves | 8e-06 |  |
| [[PHF14]] | +0.68 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[TRIM44]] | +0.68 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[RRP15]] | +0.67 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[COA7]] | +0.66 | +0.64 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRP54-AS1]] | -0.74 | -0.73 / -0.67 | both halves | 7e-06 |  |
| [[APAF1]] | -0.73 | -0.72 / -0.70 | both halves | 7e-06 |  |
| [[KMT5C]] | -0.66 | -0.59 / -0.67 | both halves | 7e-06 |  |
| [[GMCL1]] | -0.66 | -0.69 / -0.60 | both halves | 7e-06 |  |
| [[LMBR1L]] | -0.66 | -0.63 / -0.63 | both halves | 7e-06 |  |
| [[NARF]] | -0.66 | -0.54 / -0.68 | both halves | 1e-05 |  |
| [[IFI27L1]] | -0.63 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[UBTD1]] | -0.63 | -0.63 / -0.53 | both halves | 1e-05 |  |
| [[MAX]] | -0.63 | -0.59 / -0.58 | both halves | 7e-06 |  |
| [[PPP1R2]] | -0.63 | -0.62 / -0.56 | both halves | 1e-05 |  |
| [[TMEM50B]] | -0.63 | -0.60 / -0.59 | both halves | 7e-06 |  |
| [[ANKRD37]] | -0.62 | -0.62 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises COMMD10's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[PYDC2-AS1]] | B | PYDC2-AS1 activity raises COMMD10's level | lines that do not express PYDC2-AS1 (26) vs lines expressing it (24) | 1.35× lower at baseline in the lines without PYDC2-AS1 | 0.087 | ⚠ within organs, on part of the lines; also absent: BCHE, CPED1, CCNYL2 |
| [[KMT5C]] | C | KMT5C's natural level weakens COMMD10's drug response | KMT5C's natural level across 50 lines (lineage-adjusted; a glimpse) | r -0.61, reverse -0.10; direction not clear | 0.086 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.639). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-22.9, 13.8); signed map (6.4, -43.0). **Vector** length 135, 44.0% of its response variance represented; |z| ≥ 3 in 985 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +10.8 | +7.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.0 | +5.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.9 | +6.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.5 | +0.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | +5.8 | -3.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +5.7 | +4.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +5.6 | +4.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.3 | +2.4 |
|  | [[EX229 (drug)]] 5 µM |  | +4.7 | +4.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.6 | +0.7 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -5.7 | -6.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.8 | -10.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.7 | -11.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.7 | -7.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -3.6 | -3.7 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -3.5 | -2.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.1 | -2.9 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -3.1 | -1.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.1 | -3.3 |
|  | [[Retinoic acid (drug)]] 5 µM |  | -2.7 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | COMM domain containing 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q23.1 — chr5:116,085,016-116,412,762 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PTD002 |
| Gene groups (HGNC) | COMM domain containing; CCC complex |
| Reactome | 1 pathways, smallest: Neddylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6G5](https://www.uniprot.org/uniprotkb/Q9Y6G5) (COMM domain-containing protein 10):

> Scaffold protein in the commander complex that is essential for endosomal recycling of transmembrane cargos; the commander complex is composed of the CCC subcomplex and the retriever subcomplex. May modulate activity of cullin-RING E3 ubiquitin ligase (CRL) complexes. May down-regulate activation of NF-kappa-B.

**Summary**, from NCBI Gene [51397](https://www.ncbi.nlm.nih.gov/gene/51397):

> Predicted to be involved in endocytic recycling. Located in nucleoplasm. Part of protein-containing complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30201](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30201) · Entrez [51397](https://www.ncbi.nlm.nih.gov/gene/51397) · UniProt [Q9Y6G5](https://www.uniprot.org/uniprotkb/Q9Y6G5) · Ensembl [ENSG00000145781](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145781)

## Data

Gene col 7026: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7026); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7026, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7026]; `tensor/DDL_lfc|DDL_z.npy` [7026]; `embed/gene_vectors.npy` [7026]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7026 or target_col == 7026). Every well: [[COMMD10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COMMD10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
