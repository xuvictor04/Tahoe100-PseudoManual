---
symbol: "TTLL11"
type: "gene"
col: 10645
ensembl_id: "ENSG00000175764"
name: "tubulin tyrosine ligase like 11"
location: "9q33.2"
module: 52
arm: "+"
pooled_cpm: 21.89
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 10
n_dd_up_clean: 14
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# TTLL11

*tubulin tyrosine ligase like 11* — 9q33.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.48× (z +14.2, q 4e-43, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.400× (z -10.4, q 1e-22, down in 36 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.436× (z -9.4, q 1e-18, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SCFD2]] (+0.61, fdr 9e-06), [[ASCC2]] (+0.55, fdr 2e-05), [[GFUS]] (+0.53, fdr 2e-04); moves opposite to [[BRWD3]] (-0.53, fdr 1e-05), [[SLC25A27]] (-0.51, fdr 9e-05), [[PGAP1]] (-0.50, fdr 3e-05).
> It sits in the **+** arm of [[Module 052]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TGFB1I1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 1 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10645.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.48×** | +14.2 | 4e-43 | 46/48 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.99×** | +12.5 | 2e-33 | 44/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.75×** | +11.6 | 1e-28 | 43/48 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.85×** | +9.9 | 5e-21 | 32/46 (MIA PaCa-2, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.89×** | +7.3 | 5e-11 | 29/44 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.67×** | +5.4 | 8e-06 | 27/48 (LS 180, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.28×** | +4.9 | 7e-05 | 25/48 (PANC-1, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.49×** | +4.6 | 3e-04 | 17/46 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.24×** | +3.5 | 0.030 | 20/44 (A549, PANC-1, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.35×** | +3.5 | 0.030 | 19/46 (HOP62, LOX-IMVI, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +3.4 | 0.030 | 12/48 (MIA PaCa-2, Hs 766T, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.33×** | +3.3 | 0.054 | 12/48 (HOP62, LOX-IMVI, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.32×** | +3.2 | 0.057 | 16/48 (SW480, NCI-H23, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.32×** | +3.2 | 0.065 | 10/48 (A498, SW48, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.33×** | +3.1 | 0.068 | 17/47 (RKO, SHP-77, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10645.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.400×** | -10.4 | 1e-22 | 36/47 (RPMI-7951, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.436×** | -9.4 | 1e-18 | 31/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.513×** | -7.6 | 6e-12 | 34/48 (H4, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.525×** | -7.3 | 3e-11 | 31/47 (KATO III, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.668×** | -4.2 | 0.003 | 21/48 (H4, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | **0.718×** | -3.6 | 0.026 | 21/44 (H4, RKO, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.728×** | -3.6 | 0.026 | 22/47 (LoVo, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.749×** | -3.3 | 0.068 | 15/48 (NCI-H2347, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~64% of this change | **0.749×** | -3.3 | 0.068 | 18/45 (hTERT-HPNE, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.581×** | -3.2 | 0.072 | 14/36 (CFPAC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | 0.595× | -3.1 | 0.11 | 13/44 (NCI-H2347, C32, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10645. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 50.3 | 0 | 7 (4 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0131× (z -21.8) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.109× (z -12.2) |
| [[NCI-H460 (line)]] | wt | 24.7 | 6 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +10.4) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.264× (z -9.7) |
| [[A498 (line)]] | wt | 55.7 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.145× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.316× (z -12.2) |
| [[MIA PaCa-2 (line)]] | alt | 19.1 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.176× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 5.98 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +10.8) | — |
| [[HOP62 (line)]] | alt | 28.4 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.139× (z -11.7) |
| [[LOX-IMVI (line)]] | wt | 34.9 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.171× (z -10.8) |
| [[NCI-H23 (line)]] | alt | 11.9 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +9.8) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.116× (z -11.1) |
| [[SW480 (line)]] | alt | 21.8 | 1 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.30× (z +9.2) | [[Digitoxin (drug)]] 5 µM 0.179× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.219× (z -11.8) |
| [[HEC-1-A (line)]] | alt | 33.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.47× (z +9.5) | — |
| [[J82 (line)]] | alt | 22.2 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.161× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.161× (z -11.1) |
| [[KATO III (line)]] | alt | 30.2 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.148× (z -12.0) |
| [[LoVo (line)]] | wt | 20.1 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.178× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.239× (z -9.0) |
| [[LS 180 (line)]] | wt | 13.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.59× (z +10.3) | — |
| [[NCI-H1792 (line)]] | alt | 14.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.77× (z +11.1) | — |
| [[RKO (line)]] | wt | 15.8 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0702× (z -12.0) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 42.5 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.48× (z +8.8) | — |
| [[CFPAC-1 (line)]] | alt | 9.77 | 0 | 1 | — | [[Menadione (drug)]] 0.05 µM 0.120× (z -10.7) |
| [[CHP-212 (line)]] | wt | 23.7 | 0 | 1 | — | [[Retinoic acid (drug)]] 0.5 µM 0.0644× (z -8.8) |
| [[COLO 205 (line)]] | alt | 10.1 | 0 | 1 | — | [[Hesperidin (drug)]] 0.05 µM 0.0785× (z -9.0) |
| [[HCT15 (line)]] | alt | 18.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.76× (z +9.3) | — |
| [[Hs 766T (line)]] | wt | 17.1 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0825× (z -9.4) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 24.7 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.136× (z -9.2) |
| [[NCI-H1573 (line)]] | alt | 5.49 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0929× (z -9.0) |
| [[RPMI-7951 (line)]] | alt | 19.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0555× (z -13.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 10.9 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.0908× (z -9.5) |
| [[SW1417 (line)]] | alt | 22.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.280× (z -8.7) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 15.1 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.0615× (z -10.3) |
| [[A-172 (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.69 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.81 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10645), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCFD2]] | +0.61 | +0.57 / +0.58 | both halves | 9e-06 |  |
| [[ASCC2]] | +0.55 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[GFUS]] | +0.53 | +0.64 / +0.29 | both halves | 2e-04 |  |
| [[SF3A3]] | +0.53 | +0.52 / +0.46 | both halves | 2e-05 |  |
| [[UTP6]] | +0.52 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[FAM98A]] | +0.52 | +0.46 / +0.52 | both halves | 3e-05 |  |
| [[PWP1]] | +0.51 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[NOL6]] | +0.51 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[WDR46]] | +0.51 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[AP3D1]] | +0.51 | +0.56 / +0.41 | both halves | 4e-05 |  |
| [[NELFE]] | +0.50 | +0.52 / +0.34 | both halves | 1e-04 |  |
| [[AP1M1]] | +0.50 | +0.32 / +0.48 | both halves | 2e-04 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRWD3]] | -0.53 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[SLC25A27]] | -0.51 | -0.47 / -0.36 | both halves | 9e-05 |  |
| [[PGAP1]] | -0.50 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[PDK3]] | -0.50 | -0.65 / -0.55 | both halves | 1e-05 |  |
| [[TMEM144]] | -0.50 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[C20orf96]] | -0.48 | -0.59 / -0.46 | both halves | 3e-05 |  |
| [[FOXN3]] | -0.48 | -0.52 / -0.38 | both halves | 7e-05 |  |
| [[MICB]] | -0.48 | -0.33 / -0.50 | both halves | 1e-04 |  |
| [[LINC00958]] | -0.48 | -0.25 / -0.43 | both halves | 4e-04 |  |
| [[TRIM33]] | -0.47 | -0.58 / -0.38 | both halves | 6e-05 |  |
| [[BCL2L11]] | -0.46 | -0.26 / -0.42 | both halves | 4e-04 |  |
| [[ZMYM2]] | -0.46 | -0.57 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TGFB1I1]] | B | TGFB1I1 activity raises TTLL11's level | lines that do not express TGFB1I1 (13) vs lines expressing it (37) | 1.38× lower at baseline in the lines without TGFB1I1 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000281091, ENSG00000234405, TMOD1 |
| [[PSMB5]] | B | PSMB5 activity raises TTLL11's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.428). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-22.9, -39.9); signed map (-12.6, -23.6). **Vector** length 87.9, 20.2% of its response variance represented; |z| ≥ 3 in 1,185 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.2 | +7.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.7 | +9.9 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | -0.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.0 | +0.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.5 | +0.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +2.0 | +3.3 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.8 | +2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.8 | -1.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.3 | -2.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.4 | -3.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -3.0 | -1.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.9 | -10.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | -2.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.6 | -1.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.1 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | tubulin tyrosine ligase like 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q33.2 — chr9:121,815,674-122,093,606 (-) |
| Ensembl biotype | protein_coding |
| Also known as | bA244O19.1; previously C9orf20, TTLL11-IT1, C9orf148 |
| Gene groups (HGNC) | Tubulin tyrosine ligase family |
| Reactome | 1 pathways, smallest: Carboxyterminal post-translational modifications of tubulin |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NHH1](https://www.uniprot.org/uniprotkb/Q8NHH1) (Tubulin polyglutamylase TTLL11):

> Polyglutamylase which modifies tubulin, generating polyglutamate side chains of variable lengths on the gamma-carboxyl group of specific glutamate residues within the C-terminal tail of tubulin. Preferentially mediates ATP-dependent polyglutamate long side-chain elongation over the initiation step of the polyglutamylation reaction. Preferentially modifies the alpha-tubulin tail over a beta-tail (By similarity). Required for CCSAP localization to both spindle and cilia microtubules. Promotes …

**Summary**, from NCBI Gene [158135](https://www.ncbi.nlm.nih.gov/gene/158135):

> Predicted to enable tubulin binding activity and tubulin-glutamic acid ligase activity. Predicted to be involved in microtubule cytoskeleton organization. Predicted to act upstream of or within microtubule severing and protein polyglutamylation. Predicted to be located in cytosol. Predicted to be active in ciliary basal body. [provided by Alliance of Genome Resources, Apr 2025]

**Accessions** — [HGNC:18113](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18113) · Entrez [158135](https://www.ncbi.nlm.nih.gov/gene/158135) · UniProt [Q8NHH1](https://www.uniprot.org/uniprotkb/Q8NHH1) · Ensembl [ENSG00000175764](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175764)

## Data

Gene col 10645: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10645); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10645, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10645]; `tensor/DDL_lfc|DDL_z.npy` [10645]; `embed/gene_vectors.npy` [10645]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10645 or target_col == 10645). Every well: [[TTLL11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TTLL11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
