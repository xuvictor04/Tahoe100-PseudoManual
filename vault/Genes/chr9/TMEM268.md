---
symbol: "TMEM268"
type: "gene"
col: 8096
ensembl_id: "ENSG00000157693"
name: "transmembrane protein 268"
location: "9q32"
module: 133
arm: "+"
pooled_cpm: 12.92
n_lines_expressing: 48
n_dd_up: 25
n_dd_down: 13
n_dd_up_clean: 20
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/133"]
generated_by: "tahoemap"
---

# TMEM268

*transmembrane protein 268* — 9q32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (5 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.82× (z +10.0, q 6e-21, up in 31 of 45 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Artesunate (drug)]] 5 µM: 1.44× (z +8.7, q 9e-16, up in 32 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.355× (z -17.3, q 0e+00, down in 37 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZBED3]] (+0.76, fdr 7e-06), [[KCTD15]] (+0.74, fdr 7e-06), [[YARS1]] (+0.73, fdr 7e-06); moves opposite to [[SRSF9]] (-0.65, fdr 1e-05, ⚠ SRSF9 in the vector space only through flagged drug-doses), [[MARCHF3]] (-0.56, fdr 3e-05), [[SH3BGRL3]] (-0.53, fdr 5e-05), [[TXNDC17]] (-0.51, fdr 1e-04).
> It is in [[Module 133]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[ANK2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8096.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.82×** | +10.0 | 6e-21 | 31/45 (NCI-H460, NCI-H2347, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM |  | **1.44×** | +8.7 | 9e-16 | 32/46 (SNU-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +7.1 | 3e-10 | 20/40 (RKO, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.49×** | +6.8 | 2e-09 | 21/45 (NCI-H460, SW480, …) | rises with dose | position effect removed |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.32×** | +6.5 | 7e-09 | 24/46 (LOX-IMVI, LoVo, …) | rises with dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | **1.44×** | +6.1 | 9e-08 | 21/46 (SNU-1, MIA PaCa-2, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.79×** | +5.1 | 3e-05 | 14/44 (NCI-H460, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.78×** | +5.1 | 3e-05 | 13/43 (NCI-H460, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.35×** | +5.1 | 3e-05 | 13/45 (NCI-H460, LOX-IMVI, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.34×** | +4.9 | 6e-05 | 11/45 (NCI-H460, RKO, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **1.66×** | +4.4 | 4e-04 | 7/41 (HOP62, H4, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.63×** | +4.3 | 8e-04 | 9/43 (NCI-H460, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 0.5 µM |  | **1.28×** | +4.1 | 0.002 | 8/45 (SW480, RKO, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.27×** | +4.1 | 0.002 | 16/45 (A498, NCI-H460, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.26×** | +3.9 | 0.004 | 13/44 (LoVo, LOX-IMVI, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.55×** | +3.9 | 0.004 | 4/44 (NCI-H460, LOX-IMVI, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **1.25×** | +3.8 | 0.005 | 10/45 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 1.17× | +3.7 | 0.006 | 12/46 (SNU-1, Hs 766T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8096.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.355×** | -17.3 | 0e+00 | 37/45 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.361×** | -17.1 | 0e+00 | 42/45 (RKO, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.379×** | -16.3 | 0e+00 | 39/45 (RKO, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.582×** | -9.1 | 2e-17 | 31/45 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.642×** | -7.4 | 1e-11 | 22/43 (HepG2/C3A, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.663×** | -6.6 | 3e-09 | 20/44 (RKO, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.809×** | -5.0 | 4e-05 | 20/46 (PANC-1, LS 180, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.825×** | -4.6 | 4e-04 | 18/45 (MIA PaCa-2, PANC-1, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.786×** | -4.0 | 0.003 | 13/45 (NCI-H460, SNU-1, …) | all doses, stronger at high dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.641×** | -3.9 | 0.006 | 10/43 (RPMI-7951, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[ULK-101 (drug)]] 0.5 µM |  | **0.754×** | -3.4 | 0.039 | 7/43 (Hs 766T, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.826×** | -3.2 | 0.067 | 12/45 (RKO, SW480, …) | rises with dose | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.702×** | -3.1 | 0.084 | 8/46 (LoVo, SNU-423, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 5 µM |  | 0.880× | -3.0 | 0.10 | 8/46 (NCI-H1792, SHP-77, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8096. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 40.8 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.165× (z -13.7) |
| [[PANC-1 (line)]] | alt | 13.6 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.176× (z -14.6) |
| [[MIA PaCa-2 (line)]] | alt | 17.4 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -17.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.139× (z -12.5) |
| [[NCI-H460 (line)]] | wt | 16.3 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.251× (z -11.7) |
| [[SW480 (line)]] | alt | 11.9 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.276× (z -9.6) |
| [[A498 (line)]] | wt | 23.0 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.373× (z -8.9) |
| [[H4 (line)]] | wt | 23.3 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.159× (z -9.7) |
| [[LoVo (line)]] | wt | 17.7 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.227× (z -10.6) |
| [[SHP-77 (line)]] | alt | 20.0 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.202× (z -9.3) |
| [[SK-MEL-2 (line)]] | alt | 22.1 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.120× (z -12.2) |
| [[SNU-1 (line)]] | wt | 39.5 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.133× (z -10.8) |
| [[SW1417 (line)]] | alt | 18.0 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.203× (z -10.7) |
| [[SW48 (line)]] | wt | 23.4 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.127× (z -9.9) |
| [[BT-474 (line)]] | alt | 22.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.225× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 15.2 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.200× (z -9.9) |
| [[SNU-423 (line)]] | alt | 16.7 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.200× (z -9.6) |
| [[A-172 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.49 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.10 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.62 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.24 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.16 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.19 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.77 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.69 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.45 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.72 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.55 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.59 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8096), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBED3]] | +0.76 | +0.62 / +0.71 | both halves | 7e-06 |  |
| [[KCTD15]] | +0.74 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[YARS1]] | +0.73 | +0.69 / +0.78 | both halves | 7e-06 |  |
| [[PCK2]] | +0.71 | +0.58 / +0.71 | both halves | 7e-06 |  |
| [[BLTP3A]] | +0.70 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[SLC6A9]] | +0.68 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[NARS1]] | +0.67 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[CEBPG]] | +0.66 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[XPOT]] | +0.66 | +0.69 / +0.75 | both halves | 7e-06 |  |
| [[PSAT1]] | +0.66 | +0.68 / +0.73 | both halves | 7e-06 |  |
| [[SLC3A2]] | +0.65 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[TARS1]] | +0.65 | +0.59 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRSF9]] ⚠ | -0.65 | -0.65 / -0.49 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MARCHF3]] | -0.56 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[SH3BGRL3]] | -0.53 | -0.42 / -0.39 | both halves | 5e-05 |  |
| [[TXNDC17]] | -0.51 | -0.44 / -0.34 | both halves | 1e-04 |  |
| [[SYAP1]] | -0.51 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[TIMP1]] | -0.51 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[LUZP1]] | -0.51 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[CD59]] | -0.51 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[CALM1]] | -0.50 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[POLR2L]] | -0.50 | -0.38 / -0.55 | both halves | 7e-05 |  |
| [[PLIN3]] | -0.50 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[CIB1]] | -0.49 | -0.41 / -0.34 | both halves | 1e-04 |  |
| [[POLD4]] | -0.49 | -0.39 / -0.47 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANK2]] | B | ANK2 activity raises TMEM268's level | lines that do not express ANK2 (16) vs lines expressing it (34) | 1.90× lower at baseline in the lines without ANK2 | 0.031 | ⚠ within organs, on part of the lines; also absent: VASH1, SOBP, GXYLT2; maybe low, not absent |
| [[PSAT1]] | B | PSAT1 activity raises TMEM268's level | lines that do not express PSAT1 (8) vs lines expressing it (42) | 2.16× lower at baseline in the lines without PSAT1 | 0.051 | ⚠ within organs, on part of the lines; also absent: SLC1A4, ACBD7; maybe low, not absent |
| [[ANK2]] | B | ANK2 activity strengthens TMEM268's drug response | lines that do not express ANK2 (14) vs lines expressing it (32) | the lines without ANK2 respond 0.68× as strongly (z diff +1.20); strongest at Panobinostat 0.5 µM: 0.44x vs 0.30x (z diff +2.8) | 0.094 | ⚠ within organs, on part of the lines; also absent: VASH1, SOBP, GXYLT2; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[PSAT1]] | B | PSAT1 activity strengthens TMEM268's drug response | lines that do not express PSAT1 (6) vs lines expressing it (40) | the lines without PSAT1 respond 0.64× as strongly (z diff +1.57); strongest at Panobinostat 5 µM: 0.55x vs 0.34x (z diff +3.3) | 0.096 | ⚠ within organs, on part of the lines; also absent: SLC1A4, ACBD7; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[SLC1A4]] | C | SLC1A4 activity raises TMEM268's level | lines that do not express SLC1A4 (4) vs lines expressing it (46) | 2.11× lower at baseline in the lines without SLC1A4 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CCNP, PSAT1, KAZN; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 133]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.789). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-15.7, 46.6); signed map (-13.1, 22.4). **Vector** length 91.8, 18.8% of its response variance represented; |z| ≥ 3 in 981 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.7 | +10.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.3 | +6.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.8 | +1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.8 | +4.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.6 | +7.1 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.9 | +4.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.8 | +5.1 |
|  | [[EX229 (drug)]] 5 µM |  | +3.6 | +5.1 |
| fall | [[Belinostat (drug)]] 5 µM |  | -3.5 | -16.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.0 | -17.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.8 | -17.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.6 | -2.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.6 | -9.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.5 | -2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.4 | -0.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.4 | -3.9 |
|  | [[Ciclopirox (drug)]] 5 µM |  | -1.4 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 268 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q32 — chr9:114,611,206-114,646,422 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp547P234, FLJ38045; previously C9orf91 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5VZI3](https://www.uniprot.org/uniprotkb/Q5VZI3) (Transmembrane protein 268):

> Stabilizes cell surface expression of ITGAM and participates in the adhesion and migration of phagocytes during bacterial clearance.

**Summary**, from NCBI Gene [203197](https://www.ncbi.nlm.nih.gov/gene/203197):

> Predicted to be located in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24513](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24513) · Entrez [203197](https://www.ncbi.nlm.nih.gov/gene/203197) · UniProt [Q5VZI3](https://www.uniprot.org/uniprotkb/Q5VZI3) · Ensembl [ENSG00000157693](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157693)

## Data

Gene col 8096: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8096); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8096, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8096]; `tensor/DDL_lfc|DDL_z.npy` [8096]; `embed/gene_vectors.npy` [8096]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8096 or target_col == 8096). Every well: [[TMEM268 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM268.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
