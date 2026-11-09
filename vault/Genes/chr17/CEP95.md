---
symbol: "CEP95"
type: "gene"
col: 15148
ensembl_id: "ENSG00000258890"
name: "centrosomal protein 95"
location: "17q23.3"
module: 4
arm: "-"
pooled_cpm: 188.47
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 12
n_dd_up_clean: 4
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# CEP95

*centrosomal protein 95* — 17q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.55× (z +9.2, q 1e-17, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.391× (z -13.5, q 8e-39, down in 41 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.735× (z -4.4, q 0.002, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAB5A]] (+0.57, fdr 1e-05), [[ODF2]] (+0.56, fdr 1e-05), [[FAM177A1]] (+0.55, fdr 1e-05); moves opposite to [[STARD7]] (-0.54, fdr 1e-04), [[DIS3L2]] (-0.53, fdr 2e-05), [[PSMA1]] (-0.53, fdr 5e-05).
> It sits in the **-** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15148.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.55×** | +9.2 | 1e-17 | 38/48 (RKO, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.75×** | +8.4 | 2e-14 | 44/48 (AsPC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.52×** | +6.2 | 8e-08 | 43/48 (HepG2/C3A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.44×** | +5.4 | 8e-06 | 38/48 (HepG2/C3A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.32×** | +4.1 | 0.004 | 29/48 (RKO, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.5 | 0.039 | 22/49 (AsPC-1, C32, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | 1.48× | +3.1 | 0.18 | 27/49 (A498, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15148.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.391×** | -13.5 | 8e-39 | 41/44 (NCI-H1792, A-172, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.474×** | -11.2 | 2e-26 | 46/49 (A549, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.735×** | -4.4 | 0.002 | 32/48 (C32, PANC-1, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.819×** | -4.2 | 0.003 | 24/48 (H4, SW 900, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.781×** | -3.7 | 0.022 | 29/48 (COLO 205, LoVo, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.782×** | -3.7 | 0.022 | 25/48 (A498, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **0.790×** | -3.5 | 0.033 | 26/48 (HT-29, SW 1271, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~23% of this change | **0.792×** | -3.4 | 0.047 | 26/47 (A549, C32, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.788×** | -3.4 | 0.047 | 27/47 (C32, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.805×** | -3.3 | 0.059 | 27/48 (C32, Panc 03.27, …) | inconsistent across doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.660×** | -3.3 | 0.059 | 27/47 (CHP-212, C-33 A, …) | top dose only | noisy plate (z scaled) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.815×** | -3.1 | 0.098 | 25/49 (Panc 03.27, A-172, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15148. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 168 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +14.6) | [[Dinaciclib (drug)]] 5 µM 0.418× (z -9.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 172 | 5 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +16.1) | [[Dinaciclib (drug)]] 0.5 µM 0.368× (z -10.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 244 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.435× (z -10.3) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 181 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +16.0) | — |
| [[HepG2_C3A (line)]] | wt | 161 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.33× (z +11.8) | — |
| [[SNU-1 (line)]] | wt | 172 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.35× (z +11.1) | — |
| [[BT-474 (line)]] | alt | 188 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.60× (z +10.0) | — |
| [[C-33 A (line)]] | alt | 226 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.359× (z -10.3) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 232 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.62× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.440× (z -10.2) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 164 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.292× (z -12.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 195 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.295× (z -11.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 159 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.433× (z -8.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 259 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.26× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.309× (z -14.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 302 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.297× (z -13.5) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 113 | 1 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +10.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Belumosudil (drug)]] 5 µM 0.393× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 187 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.435× (z -9.2) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 316 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.225× (z -12.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 207 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.365× (z -11.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 157 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.402× (z -9.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 231 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.332× (z -10.6) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 155 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.392× (z -10.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 175 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.355× (z -10.7) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 165 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.289× (z -12.3) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 192 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.217× (z -15.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 193 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +13.8) | [[Dinaciclib (drug)]] 5 µM 0.304× (z -12.7) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 153 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.351× (z -12.6) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 249 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.365× (z -11.7) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 180 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.290× (z -12.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 201 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.268× (z -13.8) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 189 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.333× (z -13.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 181 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -15.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 228 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.355× (z -10.2) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 182 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.06× (z +11.2) | — |
| [[H4 (line)]] | wt | 203 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.275× (z -10.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 230 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.398× (z -8.5) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 186 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.402× (z -8.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 234 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.407× (z -11.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 123 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +10.8) | — |
| [[SW 900 (line)]] | alt | 175 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.382× (z -9.9) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 145 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.389× (z -8.7) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 171 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 157 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 199 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 185 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 155 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 203 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15148), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*36 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB5A]] | +0.57 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[ODF2]] | +0.56 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[FAM177A1]] | +0.55 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[SLC35F5]] | +0.53 | +0.57 / +0.43 | both halves | 3e-05 |  |
| [[STX5]] | +0.53 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[GCAT]] | +0.50 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[INTS6L]] | +0.49 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[SAFB2]] | +0.49 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[SP4]] | +0.48 | +0.54 / +0.33 | both halves | 1e-04 |  |
| [[ATG12]] | +0.47 | +0.40 / +0.48 | both halves | 4e-05 |  |
| [[MNT]] | +0.47 | +0.56 / +0.30 | both halves | 2e-04 |  |
| [[NKTR]] | +0.46 | +0.50 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*64 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STARD7]] | -0.54 | -0.63 / -0.35 | both halves | 1e-04 |  |
| [[DIS3L2]] | -0.53 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[PSMA1]] | -0.53 | -0.65 / -0.40 | both halves | 5e-05 |  |
| [[EIF4E]] | -0.52 | -0.63 / -0.38 | both halves | 6e-05 |  |
| [[AGPS]] | -0.52 | -0.56 / -0.40 | both halves | 5e-05 |  |
| [[CCT5]] | -0.50 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[CCT3]] | -0.50 | -0.54 / -0.40 | both halves | 5e-05 |  |
| [[PSMC5]] | -0.50 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[LRP12]] | -0.49 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[FAM98B]] | -0.48 | -0.58 / -0.37 | both halves | 8e-05 |  |
| [[NUDC]] | -0.48 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[CDC123]] | -0.48 | -0.57 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **-** arm (projection on the module's main direction -0.461). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (10.9, -41.6); signed map (-12.8, 16.8). **Vector** length 110, 39.3% of its response variance represented; |z| ≥ 3 in 946 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.5 | +3.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +3.3 | +5.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.3 | -1.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +4.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +3.0 | +8.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.2 | +1.4 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +2.1 | +0.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +1.9 | +1.4 |
|  | [[Retinoic acid (drug)]] 5 µM |  | +1.8 | +1.2 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.7 | +0.6 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -7.5 | -0.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -6.9 | -1.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -6.7 | -3.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.5 | -3.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -5.3 | -2.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.9 | -4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.6 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | centrosomal protein 95 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q23.3 — chr17:64,506,865-64,542,461 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp667E1824; previously CCDC45 |
| Matched by | ensembl_id |

UniProt [Q96GE4](https://www.uniprot.org/uniprotkb/Q96GE4) carries no function annotation.

**Summary**, from NCBI Gene [90799](https://www.ncbi.nlm.nih.gov/gene/90799):

> Located in centrosome and spindle pole. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25141](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25141) · Entrez [90799](https://www.ncbi.nlm.nih.gov/gene/90799) · UniProt [Q96GE4](https://www.uniprot.org/uniprotkb/Q96GE4) · Ensembl [ENSG00000258890](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000258890)

## Data

Gene col 15148: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15148); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15148, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15148]; `tensor/DDL_lfc|DDL_z.npy` [15148]; `embed/gene_vectors.npy` [15148]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15148 or target_col == 15148). Every well: [[CEP95 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CEP95.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
