---
symbol: "KLHL36"
type: "gene"
col: 5742
ensembl_id: "ENSG00000135686"
name: "kelch like family member 36"
location: "16q24.1"
module: 20
arm: "-"
pooled_cpm: 25.67
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 24
n_dd_up_clean: 0
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 4
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# KLHL36

*kelch like family member 36* — 16q24.1

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (16 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.523× (z -13.8, q 1e-40, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLPBP]] (+0.48, fdr 6e-05), [[ZBTB34]] (+0.48, fdr 3e-05), [[CCNDBP1]] (+0.46, fdr 3e-05); moves opposite to [[SIK3]] (-0.46, fdr 6e-05), [[PCDH7]] (-0.46, fdr 1e-04), [[COL4A5]] (-0.45, fdr 1e-04).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 4 go from it, the strongest it → cells under [[ERK5-IN-2 (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5742.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pyridoxine (drug)]] 0.5 µM |  | 1.19× | +3.8 | 0.076 | 11/45 (SNU-423, NCI-H460, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 1.18× | +3.6 | 0.076 | 15/44 (PANC-1, NCI-H460, …) | inconsistent across doses | low cells (technical?) |
| [[Rapamycin (drug)]] 5 µM |  | 1.12× | +3.4 | 0.11 | 4/48 (HOP62, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | 1.17× | +3.4 | 0.11 | 9/48 (PANC-1, LOX-IMVI, …) | inconsistent across doses | position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | 1.33× | +3.2 | 0.14 | 5/47 (AN3 CA, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 21 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5742.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.523×** | -13.8 | 1e-40 | 42/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.859× | -10.7 | 2e-24 | 18/48 (RKO, KATO III, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.593×** | -10.7 | 2e-24 | 36/46 (NCI-H23, C-33 A, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.621×** | -10.1 | 5e-22 | 38/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.656×** | -9.0 | 3e-17 | 31/47 (HT-29, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.659×** | -8.9 | 7e-17 | 33/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.752×** | -8.5 | 1e-15 | 29/47 (NCI-H1792, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.682×** | -7.8 | 3e-13 | 26/48 (NCI-H1792, HEC-1-A, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.713×** | -7.2 | 4e-11 | 28/48 (SNU-423, HOP62, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.534×** | -7.0 | 2e-10 | 27/48 (NCI-H1573, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.750×** | -5.9 | 2e-07 | 17/48 (SW480, LOX-IMVI, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.759×** | -5.8 | 3e-07 | 23/48 (HEC-1-A, LOX-IMVI, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.627×** | -5.2 | 9e-06 | 19/47 (LoVo, PANC-1, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.783×** | -5.2 | 9e-06 | 18/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.841× | -5.2 | 1e-05 | 15/48 (SW480, HOP62, …) | top dose only |  |
| [[Tadalafil (drug)]] 5 µM |  | **0.791×** | -4.8 | 5e-05 | 19/47 (LOX-IMVI, SW1417, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.808×** | -4.5 | 2e-04 | 16/48 (SW480, PANC-1, …) | two highest doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.740×** | -3.3 | 0.016 | 8/46 (Hs 766T, SW 1271, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pyridoxine (drug)]] 5 µM |  | 0.894× | -3.3 | 0.017 | 5/48 (A549, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | 0.860× | -3.1 | 0.041 | 13/47 (HepG2/C3A, HT-29, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.871× | -2.9 | 0.064 | 12/48 (HEC-1-A, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Thymol (drug)]] 5 µM |  | 0.909× | -2.8 | 0.080 | 7/48 (SHP-77, Hs 766T, …) | top dose only |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | 0.833× | -2.7 | 0.098 | 5/48 (SNU-1, HOP62, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5742. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 41.8 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -12.4) ⚠ cell-cycle shift, explains ~40% of this change |
| [[SW480 (line)]] | alt | 20.0 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.303× (z -11.7) |
| [[HT-29 (line)]] | alt | 26.6 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.286× (z -10.0) |
| [[NCI-H1792 (line)]] | alt | 23.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -14.9) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.296× (z -8.7) |
| [[PANC-1 (line)]] | alt | 24.6 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.283× (z -13.3) |
| [[LoVo (line)]] | wt | 23.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -11.1) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.336× (z -9.7) |
| [[LS 180 (line)]] | wt | 23.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -9.5) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.293× (z -9.2) |
| [[NCI-H23 (line)]] | alt | 32.8 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.183× (z -13.9) ⚠ toxic |
| [[C32 (line)]] | wt | 18.6 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.182× (z -9.1) |
| [[H4 (line)]] | wt | 29.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.164× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 23.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -10.8) ⚠ cell-cycle shift, explains ~40% of this change |
| [[J82 (line)]] | alt | 24.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -10.0) ⚠ cell-cycle shift, explains ~40% of this change |
| [[KATO III (line)]] | alt | 31.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.363× (z -9.1) |
| [[LOX-IMVI (line)]] | wt | 24.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -11.4) ⚠ cell-cycle shift, explains ~40% of this change |
| [[MIA PaCa-2 (line)]] | alt | 33.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -9.3) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 31.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.286× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 26.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.432× (z -8.5) ⚠ cell-cycle shift, explains ~40% of this change |
| [[SNU-423 (line)]] | alt | 25.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -9.5) ⚠ cell-cycle shift, explains ~40% of this change |
| [[SW1417 (line)]] | alt | 23.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.294× (z -9.1) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SW48 (line)]] | wt | 24.2 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.0786× (z -11.9) |
| [[A-172 (line)]] | wt | 37.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 35.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 38.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5742), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLPBP]] | +0.48 | +0.44 / +0.39 | both halves | 6e-05 |  |
| [[ZBTB34]] | +0.48 | +0.43 / +0.48 | both halves | 3e-05 | same gene group |
| [[CCNDBP1]] | +0.46 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[IL17RD]] | +0.45 | +0.35 / +0.47 | both halves | 1e-04 |  |
| [[CHMP4C]] | +0.43 | +0.48 / +0.41 | both halves | 4e-05 |  |
| [[EEF2]] | +0.43 | +0.47 / +0.30 | both halves | 2e-04 |  |
| [[ABTB1]] | +0.42 | +0.41 / +0.46 | both halves | 4e-05 | same gene group |
| [[TSNARE1]] | +0.41 | +0.28 / +0.42 | both halves | 3e-04 |  |
| [[NBPF12]] | +0.41 | +0.31 / +0.49 | both halves | 2e-04 |  |
| [[QARS1]] | +0.41 | +0.33 / +0.45 | both halves | 1e-04 |  |
| [[MTMR10]] | +0.41 | +0.30 / +0.37 | both halves | 2e-04 |  |
| [[GOLGA7]] | +0.40 | +0.33 / +0.45 | both halves | 1e-04 |  |

## Genes that move opposite

*49 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIK3]] | -0.46 | -0.44 / -0.39 | both halves | 6e-05 |  |
| [[PCDH7]] | -0.46 | -0.34 / -0.44 | both halves | 1e-04 |  |
| [[COL4A5]] | -0.45 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[PALMD]] | -0.42 | -0.40 / -0.31 | both halves | 2e-04 |  |
| [[CXCL10]] | -0.41 | -0.33 / -0.45 | both halves | 1e-04 |  |
| [[BST2]] | -0.41 | -0.38 / -0.31 | both halves | 2e-04 |  |
| [[IFI44L]] | -0.40 | -0.23 / -0.40 | both halves | 5e-04 |  |
| [[LRP2]] | -0.40 | -0.45 / -0.36 | both halves | 9e-05 |  |
| [[COL5A2]] | -0.40 | -0.33 / -0.28 | both halves | 3e-04 |  |
| [[NREP]] | -0.40 | -0.34 / -0.41 | both halves | 1e-04 |  |
| [[MEIS2]] | -0.40 | -0.39 / -0.34 | both halves | 1e-04 |  |
| [[MAPK10]] | -0.40 | -0.42 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | C | KLHL36's natural level lowers the cells' numbers under ERK5-IN-2 0.5 µM (makes them more sensitive) | KLHL36's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.64 | 0.392 over the table, 0.040 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Fluvoxamine (drug)]] 0.5 µM | C | KLHL36's natural level lowers the cells' numbers under Fluvoxamine 0.5 µM (makes them more sensitive) | KLHL36's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.63 | 0.412 over the table, 0.052 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Clofarabine (drug)]] 0.5 µM | C | KLHL36's natural level lowers the cells' numbers under Clofarabine 0.5 µM (makes them more sensitive) | KLHL36's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.59 | 0.474 over the table, 0.076 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Bendamustine (drug)]] 0.5 µM | C | KLHL36's natural level lowers the cells' numbers under Bendamustine 0.5 µM (makes them more sensitive) | KLHL36's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.58 | 0.491 over the table, 0.087 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.0660). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (9.0, -48.4); signed map (-38.0, -9.2). **Vector** length 58.8, 8.57% of its response variance represented; |z| ≥ 3 in 980 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | +0.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | +2.5 | +3.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +2.4 | -8.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.3 | +0.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.1 | +0.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +2.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.6 | -0.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.5 | +0.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -1.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | -2.6 | -9.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.6 | -5.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -2.2 | -10.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -2.1 | -5.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.7 | -7.2 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.6 | -2.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.6 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | kelch like family member 36 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q24.1 — chr16:84,648,511-84,667,686 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12543; previously C16orf44 |
| Gene groups (HGNC) | Kelch like; BTB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N4N3](https://www.uniprot.org/uniprotkb/Q8N4N3) (Kelch-like protein 36):

> Probable substrate-specific adapter of an E3 ubiquitin-protein ligase complex which mediates the ubiquitination and subsequent proteasomal degradation of target proteins.

**Summary**, from NCBI Gene [79786](https://www.ncbi.nlm.nih.gov/gene/79786):

> Enables cullin family protein binding activity. Predicted to be involved in proteasome-mediated ubiquitin-dependent protein catabolic process. Predicted to be part of Cul3-RING ubiquitin ligase complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:17844](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17844) · Entrez [79786](https://www.ncbi.nlm.nih.gov/gene/79786) · UniProt [Q8N4N3](https://www.uniprot.org/uniprotkb/Q8N4N3) · Ensembl [ENSG00000135686](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135686)

## Data

Gene col 5742: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5742); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5742, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5742]; `tensor/DDL_lfc|DDL_z.npy` [5742]; `embed/gene_vectors.npy` [5742]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5742 or target_col == 5742). Every well: [[KLHL36 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLHL36.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
