---
symbol: "DIAPH2"
type: "gene"
col: 7162
ensembl_id: "ENSG00000147202"
name: "diaphanous related formin 2"
location: "Xq21.33"
module: 200
arm: "+"
pooled_cpm: 289.48
n_lines_expressing: 43
n_dd_up: 0
n_dd_down: 35
n_dd_up_clean: 0
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 4
direction_downstream: 4
tags: ["gene", "module/200"]
generated_by: "tahoemap"
---

# DIAPH2

*diaphanous related formin 2* — Xq21.33

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 35 drug-doses (12 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.208× (z -31.1, q 0e+00, down in 41 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IMMP2L]] (+0.67, fdr 1e-05), [[DOCK1]] (+0.66, fdr 7e-06), [[SUPT3H]] (+0.64, fdr 7e-06); moves opposite to [[PRMT9]] (-0.50, fdr 3e-05), [[PPM1D]] (-0.49, fdr 3e-05), [[BMF]] (-0.49, fdr 1e-05).
> It is in [[Module 200]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[FUT4]] → it (grade B ⚠); 4 go from it, the strongest it → [[UBE2E2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7162.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.19× | +3.5 | 0.24 | 18/41 (NCI-H2347, SW 900, …) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.13× | +3.3 | 0.24 | 2/41 (HT-29, SW48) | top dose only |  |
| [[BAY1125976 (drug)]] 5 µM |  | 1.37× | +3.2 | 0.24 | 21/41 (A-427, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 1.17× | +3.1 | 0.28 | 9/41 (NCI-H1792, LoVo, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 50 in all, 18 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 35 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7162.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.208×** | -31.1 | 0e+00 | 41/41 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.212×** | -30.7 | 0e+00 | 41/41 (LOX-IMVI, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.368×** | -27.4 | 0e+00 | 41/41 (LOX-IMVI, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.297×** | -24.0 | 0e+00 | 40/41 (A549, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.315×** | -21.9 | 0e+00 | 40/40 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.470×** | -20.8 | 0e+00 | 38/42 (A549, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.503×** | -13.1 | 5e-37 | 40/41 (C32, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.503×** | -12.8 | 9e-36 | 41/41 (C32, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.520×** | -12.4 | 1e-33 | 33/38 (NCI-H23, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.543×** | -12.1 | 1e-31 | 37/41 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.552×** | -11.7 | 4e-30 | 38/41 (SNU-423, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **0.538×** | -11.6 | 3e-29 | 34/42 (LS 180, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.551×** | -10.9 | 6e-26 | 34/39 (SNU-423, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.648×** | -8.6 | 4e-16 | 36/41 (NCI-H1792, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.652×** | -8.5 | 1e-15 | 27/41 (SNU-1, LS 180, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.486×** | -7.5 | 3e-12 | 30/42 (LOX-IMVI, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.700×** | -7.0 | 5e-11 | 37/42 (HOP62, A-172, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.708×** | -6.8 | 2e-10 | 37/41 (HEC-1-A, A549, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.537×** | -6.4 | 3e-09 | 36/42 (A549, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.543×** | -6.3 | 7e-09 | 31/41 (LS 180, SNU-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.37 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7162. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 368 | 0 | 18 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -34.6) |
| [[SNU-423 (line)]] | alt | 632 | 0 | 18 (9 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.118× (z -28.8) |
| [[C32 (line)]] | wt | 406 | 0 | 17 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -29.3) |
| [[HOP62 (line)]] | alt | 489 | 0 | 17 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.122× (z -21.4) |
| [[NCI-H460 (line)]] | wt | 367 | 0 | 16 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.184× (z -28.9) |
| [[PANC-1 (line)]] | alt | 332 | 0 | 16 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.206× (z -23.7) |
| [[A549 (line)]] | wt | 374 | 0 | 15 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -28.8) |
| [[HEC-1-A (line)]] | alt | 311 | 0 | 15 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.194× (z -26.4) |
| [[SK-MEL-2 (line)]] | alt | 419 | 0 | 15 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.158× (z -28.1) |
| [[RKO (line)]] | wt | 317 | 0 | 14 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -25.5) |
| [[SNU-1 (line)]] | wt | 428 | 0 | 14 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.187× (z -21.2) |
| [[SW48 (line)]] | wt | 389 | 0 | 14 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.153× (z -21.5) |
| [[SW480 (line)]] | alt | 391 | 0 | 14 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.149× (z -29.0) |
| [[hTERT-HPNE (line)]] | wt | 534 | 0 | 13 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.134× (z -16.7) |
| [[J82 (line)]] | alt | 277 | 0 | 13 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.175× (z -23.5) |
| [[LS 180 (line)]] | wt | 470 | 0 | 13 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.194× (z -23.8) |
| [[NCI-H1792 (line)]] | alt | 372 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -33.6) |
| [[NCI-H23 (line)]] | alt | 289 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -27.0) |
| [[AsPC-1 (line)]] | alt | 593 | 0 | 10 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.138× (z -22.3) |
| [[CFPAC-1 (line)]] | alt | 205 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -24.7) |
| [[KATO III (line)]] | alt | 374 | 0 | 10 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.212× (z -21.3) |
| [[LoVo (line)]] | wt | 288 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -21.9) |
| [[A-172 (line)]] | wt | 109 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -25.2) |
| [[A498 (line)]] | wt | 290 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -19.8) |
| [[C-33 A (line)]] | alt | 236 | 0 | 9 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.200× (z -19.7) |
| [[CHP-212 (line)]] | wt | 354 | 0 | 9 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.124× (z -16.6) |
| [[HCT15 (line)]] | alt | 297 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -17.0) |
| [[SW1417 (line)]] | alt | 291 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.323× (z -15.8) |
| [[Panc 03.27 (line)]] | alt | 223 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.192× (z -22.0) |
| [[RPMI-7951 (line)]] | alt | 181 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -18.9) |
| [[A-427 (line)]] | wt | 269 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -18.8) |
| [[H4 (line)]] | wt | 246 | 0 | 6 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.232× (z -15.5) |
| [[HT-29 (line)]] | alt | 446 | 0 | 6 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.191× (z -19.1) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.298× (z -14.6) |
| [[AN3 CA (line)]] | alt | 256 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.161× (z -15.9) |
| [[HS-578T (line)]] | alt | 109 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -14.8) |
| [[NCI-H2030 (line)]] | alt | 179 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -16.1) |
| [[COLO 205 (line)]] | alt | 221 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.265× (z -14.7) |
| [[NCI-H1573 (line)]] | alt | 109 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -17.6) |
| [[NCI-H2347 (line)]] | alt | 106 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.369× (z -12.3) |
| [[SW 900 (line)]] | alt | 116 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.348× (z -11.6) |
| [[BT-474 (line)]] | alt | 68.0 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 64.8 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 45.6 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 17.6 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 222 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 303 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.9 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 20.8 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 97.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.4 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7162), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IMMP2L]] | +0.67 | +0.50 / +0.71 | both halves | 1e-05 |  |
| [[DOCK1]] | +0.66 | +0.69 / +0.66 | both halves | 7e-06 | same gene group |
| [[SUPT3H]] | +0.64 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[EHBP1]] | +0.63 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[LDLRAD3]] | +0.62 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[ASAP1]] | +0.60 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[DDX10]] | +0.60 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[PTPRG]] | +0.60 | +0.52 / +0.72 | both halves | 1e-05 |  |
| [[PHF14]] | +0.59 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[FAF1]] | +0.58 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[EXOC4]] | +0.57 | +0.39 / +0.66 | both halves | 5e-05 |  |
| [[PITPNB]] | +0.57 | +0.54 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRMT9]] | -0.50 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[PPM1D]] | -0.49 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[BMF]] | -0.49 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[BPNT1]] | -0.48 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[ANKRA2]] | -0.48 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[SUPT5H]] | -0.48 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[CDC42BPG]] | -0.48 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[FDXR]] | -0.48 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[ZNF821]] | -0.47 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[MIR34AHG]] | -0.47 | -0.43 / -0.37 | both halves | 7e-05 |  |
| [[SAR1B]] | -0.47 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[DUSP11]] | -0.47 | -0.24 / -0.44 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FUT4]] | B | FUT4 activity raises DIAPH2's level | lines that do not express FUT4 (10) vs lines expressing it (40) | 2.44× lower at baseline in the lines without FUT4 | 0.065 | ⚠ within organs, on part of the lines; also absent: PIWIL4, LRRK1, LONRF3 |
| [[MYO1B]] | B | MYO1B activity raises DIAPH2's level | lines that do not express MYO1B (7) vs lines expressing it (43) | 1.95× lower at baseline in the lines without MYO1B | 0.065 | ⚠ within organs, on part of the lines; also absent: TBC1D8B, AHR, FAM241A |
| [[TOP1]] | B | TOP1 activity raises DIAPH2's level | compounds that target TOP1: 3 of 3 lower it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 6.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[UBE2E2]] | B | UBE2E2 activity raises DIAPH2's level | lines that do not express UBE2E2 (11) vs lines expressing it (39) | 1.15× lower at baseline in the lines without UBE2E2 | 0.094 | ⚠ within organs, on part of the lines; also absent: PRDM5, AMOTL1, RAB31 |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UBE2E2]] | B | DIAPH2 activity raises UBE2E2's level | lines that do not express DIAPH2 (7) vs lines expressing it (43) | 2.15× lower at baseline in the lines without DIAPH2 | 0.031 | ⚠ within organs, on part of the lines; also absent: ENSG00000271204 |
| [[PRPSAP2]] | B | DIAPH2 activity lowers PRPSAP2's level | lines that do not express DIAPH2 (7) vs lines expressing it (43) | 1.28× higher at baseline in the lines without DIAPH2 | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000271204 |
| [[SIPA1L1]] | B | DIAPH2 activity raises SIPA1L1's level | lines that do not express DIAPH2 (7) vs lines expressing it (43) | 1.65× lower at baseline in the lines without DIAPH2 | 0.082 | ⚠ within organs, on part of the lines; also absent: ENSG00000271204 |
| [[DOCK1]] | B | DIAPH2 activity raises DOCK1's level | lines that do not express DIAPH2 (7) vs lines expressing it (43) | 1.74× lower at baseline in the lines without DIAPH2 | 0.087 | ⚠ within organs, on part of the lines; also absent: ENSG00000271204 |

## Where it sits

- **Module**: [[Module 200]]; 16 genes; every member is in the + arm (projection on the module's main direction 0.682). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-2.9, -34.2); signed map (3.8, -51.8). **Vector** length 102, 38.0% of its response variance represented; |z| ≥ 3 in 1,699 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.6 | +0.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.2 | -2.8 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.9 | +3.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.5 | +1.0 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.0 | -2.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.0 | +1.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.7 | -0.8 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -8.1 | -21.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -5.7 | -12.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -4.5 | -8.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | -4.1 | -8.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.7 | -2.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.5 | -3.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -2.9 | -6.0 |
|  | [[Amsacrine (drug)]] 5 µM |  | -2.8 | -4.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.6 | -7.0 |

## What is on record

|  |  |
|---|---|
| Name | diaphanous related formin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq21.33 — chrX:96,684,712-97,604,997 (+) |
| Ensembl biotype | protein_coding |
| Also known as | POF, DIA, POF2, DIA2 |
| Gene groups (HGNC) | Armadillo like helical domain containing; Formins |
| Reactome | 7 pathways, smallest: RHOF GTPase cycle; RHOD GTPase cycle; RHO GTPases Activate Formins |
| Matched by | ensembl_id |

**Function**, from UniProt [O60879](https://www.uniprot.org/uniprotkb/O60879) (Protein diaphanous homolog 2):

> Could be involved in oogenesis. Involved in the regulation of endosome dynamics. Implicated in a novel signal transduction pathway, in which isoform 3 and CSK are sequentially activated by RHOD to regulate the motility of early endosomes through interactions with the actin cytoskeleton.

**Summary**, from NCBI Gene [1730](https://www.ncbi.nlm.nih.gov/gene/1730):

> The product of this gene belongs to the diaphanous subfamily of the formin homology family of proteins. This gene may play a role in the development and normal function of the ovaries. Defects in this gene have been linked to premature ovarian failure 2. Alternatively spliced transcript variants encoding different isoforms have been identified. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:2877](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2877) · Entrez [1730](https://www.ncbi.nlm.nih.gov/gene/1730) · UniProt [O60879](https://www.uniprot.org/uniprotkb/O60879) · Ensembl [ENSG00000147202](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147202)

## Data

Gene col 7162: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7162); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7162, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7162]; `tensor/DDL_lfc|DDL_z.npy` [7162]; `embed/gene_vectors.npy` [7162]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7162 or target_col == 7162). Every well: [[DIAPH2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DIAPH2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
