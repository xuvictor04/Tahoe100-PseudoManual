---
symbol: "RNF8"
type: "gene"
col: 3322
ensembl_id: "ENSG00000112130"
name: "ring finger protein 8"
location: "6p21.2"
module: 107
arm: "+"
pooled_cpm: 33.77
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 6
n_dd_up_clean: 18
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/107"]
generated_by: "tahoemap"
---

# RNF8

*ring finger protein 8* — 6p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (5 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.61× (z +10.4, q 2e-22, up in 34 of 46 measured lines) ⚠ toxic. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.31× (z +8.6, q 2e-15, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.719× (z -10.6, q 2e-23, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPS5]] (+0.66, fdr 7e-06), [[SNX4]] (+0.62, fdr 1e-05), [[DBR1]] (+0.62, fdr 2e-05); moves opposite to [[JUNB]] (-0.55, fdr 1e-05), [[DAP]] (-0.52, fdr 2e-04), [[ARL5B]] (-0.50, fdr 2e-05).
> It is in [[Module 107]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MEX3A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3322.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +10.4 | 2e-22 | 34/46 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.31×** | +8.6 | 2e-15 | 31/48 (HT-29, SNU-423, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.42×** | +8.0 | 3e-13 | 30/47 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.31×** | +6.1 | 1e-07 | 26/48 (HOP62, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.65×** | +5.9 | 3e-07 | 25/42 (SK-MEL-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.30×** | +5.9 | 4e-07 | 23/48 (HOP62, KATO III, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.62×** | +5.7 | 7e-07 | 21/48 (SW480, SHP-77, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 1.20× | +5.7 | 7e-07 | 22/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.28×** | +5.5 | 2e-06 | 22/47 (A498, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.57×** | +5.4 | 5e-06 | 21/48 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.23×** | +4.8 | 1e-04 | 22/48 (J82, NCI-H460, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.23×** | +4.7 | 1e-04 | 16/48 (PANC-1, SW480, …) | inconsistent across doses | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **1.22×** | +4.5 | 3e-04 | 16/47 (PANC-1, KATO III, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.23×** | +4.4 | 4e-04 | 19/48 (HT-29, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.30×** | +4.2 | 9e-04 | 14/48 (HT-29, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.22×** | +4.1 | 0.002 | 16/47 (SW48, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.13× | +3.9 | 0.004 | 12/48 (PANC-1, hTERT-HPNE, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **1.38×** | +3.8 | 0.004 | 9/47 (COLO 205, NCI-H23, …) | top dose only | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.36×** | +3.6 | 0.009 | 9/48 (NCI-H23, J82, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.11× | +3.5 | 0.013 | 8/48 (AsPC-1, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3322.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.719×** | -10.6 | 2e-23 | 31/48 (HOP62, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.760×** | -5.8 | 2e-06 | 23/43 (AN3 CA, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **0.803×** | -5.0 | 1e-04 | 20/48 (CHP-212, SW 1088, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.859× | -4.9 | 1e-04 | 18/48 (NCI-H2347, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.808×** | -4.8 | 2e-04 | 20/48 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.819×** | -4.5 | 6e-04 | 21/48 (C-33 A, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.829×** | -4.1 | 0.004 | 15/38 (Panc 03.27, SW48, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | 0.860× | -3.4 | 0.044 | 16/48 (SK-MEL-2, SW48, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3322. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 28.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -13.7) |
| [[AN3 CA (line)]] | alt | 94.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.104× (z -14.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 39.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.187× (z -12.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 36.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.409× (z -11.7) |
| [[Panc 03.27 (line)]] | alt | 70.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.203× (z -15.6) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 51.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.153× (z -13.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 34.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.462× (z -9.8) |
| [[BT-474 (line)]] | alt | 24.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.117× (z -13.5) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 60.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.237× (z -11.9) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 36.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -13.4) |
| [[CHP-212 (line)]] | wt | 35.4 | 0 | 1 | — | [[Triamcinolone (drug)]] 0.05 µM 0.114× (z -8.6) |
| [[HOP62 (line)]] | alt | 39.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -13.9) |
| [[J82 (line)]] | alt | 29.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.510× (z -8.5) |
| [[LS 180 (line)]] | wt | 46.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.292× (z -12.8) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 43.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.545× (z -10.0) |
| [[PANC-1 (line)]] | alt | 24.2 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.38× (z +8.6) ⚠ toxic | — |
| [[RPMI-7951 (line)]] | alt | 22.6 | 0 | 1 | — | [[Bergenin (drug)]] 0.5 µM 0.170× (z -10.8) |
| [[SNU-1 (line)]] | wt | 43.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.189× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 35.9 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.76× (z +10.0) ⚠ cell-cycle shift, explains ~12% of this change | — |
| [[A-427 (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 39.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 39.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 35.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 68.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 41.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3322), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS5]] | +0.66 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[SNX4]] | +0.62 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[DBR1]] | +0.62 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[PCGF6]] | +0.61 | +0.65 / +0.56 | both halves | 1e-05 | same gene group |
| [[ZNF343]] | +0.60 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[CASP6]] | +0.58 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[SREK1IP1]] | +0.58 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[ALKBH4]] | +0.57 | +0.40 / +0.59 | both halves | 4e-05 |  |
| [[RTCA]] | +0.57 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[ZNF148]] | +0.56 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[SLC16A14]] | +0.56 | +0.38 / +0.57 | both halves | 6e-05 |  |
| [[IL17RA]] | +0.55 | +0.46 / +0.57 | both halves | 3e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JUNB]] | -0.55 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[DAP]] | -0.52 | -0.32 / -0.59 | both halves | 2e-04 |  |
| [[ARL5B]] | -0.50 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[ARMH4]] | -0.49 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[YIPF6]] | -0.49 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[MAGT1]] | -0.49 | -0.36 / -0.54 | both halves | 1e-04 |  |
| [[LINC00641]] | -0.49 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[SLC35C2]] | -0.49 | -0.59 / -0.37 | both halves | 8e-05 |  |
| [[PPP1R15B]] | -0.48 | -0.39 / -0.55 | both halves | 6e-05 |  |
| [[CYP2E1]] | -0.47 | -0.37 / -0.46 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MEX3A]] | B | MEX3A activity raises RNF8's level | lines that do not express MEX3A (6) vs lines expressing it (44) | 1.64× lower at baseline in the lines without MEX3A | 0.008 | ⚠ within organs, on part of the lines; also absent: SNTA1, POGLUT3, FMNL3; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises RNF8's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[FGD1]] | B | FGD1 activity raises RNF8's level | lines that do not express FGD1 (9) vs lines expressing it (41) | 1.28× lower at baseline in the lines without FGD1 | 0.084 | ⚠ within organs, on part of the lines; also absent: CERCAM, CMTM3, CSRP2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 107]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.593). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.16; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-20.8, -2.5); signed map (-26.9, -18.1). **Vector** length 97.7, 20.7% of its response variance represented; |z| ≥ 3 in 924 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +9.4 | +8.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.8 | +10.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.2 | +8.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | +5.2 | +4.5 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +5.2 | +6.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.6 | +4.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.5 | +5.9 |
|  | [[EX229 (drug)]] 5 µM |  | +3.4 | +3.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.9 | +4.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.8 | +5.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -4.9 | -10.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.9 | -0.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -1.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | +0.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | +0.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | -3.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.1 | -0.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | -4.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.6 | -0.6 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.6 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | ring finger protein 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.2 — chr6:37,353,979-37,394,734 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0646 |
| Gene groups (HGNC) | Ring finger proteins; RING finger E3 ubiquitin protein ligases |
| Reactome | 12 pathways, smallest: Nonhomologous End-Joining (NHEJ); Recruitment and ATM-mediated phosphorylation of repair and signaling proteins at DNA double strand breaks; G2/M DNA damage checkpoint |
| Matched by | ensembl_id |

**Function**, from UniProt [O76064](https://www.uniprot.org/uniprotkb/O76064) (E3 ubiquitin-protein ligase RNF8):

> E3 ubiquitin-protein ligase that plays a key role in DNA damage signaling via 2 distinct roles: by mediating the 'Lys-63'-linked ubiquitination of histones H2A and H2AX and promoting the recruitment of DNA repair proteins at double-strand breaks (DSBs) sites, and by catalyzing 'Lys-48'-linked ubiquitination to remove target proteins from DNA damage sites. Following DNA DSBs, it is recruited to the sites of damage by ATM-phosphorylated MDC1 and catalyzes the 'Lys-63'-linked ubiquitination of …

**Summary**, from NCBI Gene [9025](https://www.ncbi.nlm.nih.gov/gene/9025):

> The protein encoded by this gene contains a RING finger motif and an FHA domain. This protein has been shown to interact with several class II ubiquitin-conjugating enzymes (E2), including UBE2E1/UBCH6, UBE2E2, and UBE2E3, and may act as an ubiquitin ligase (E3) in the ubiquitination of certain nuclear proteins. This protein is also known to play a role in the DNA damage response and depletion of this protein causes cell growth inhibition and cell cycle arrest. Alternative splicing results in …

**Accessions** — [HGNC:10071](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10071) · Entrez [9025](https://www.ncbi.nlm.nih.gov/gene/9025) · UniProt [O76064](https://www.uniprot.org/uniprotkb/O76064) · Ensembl [ENSG00000112130](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112130)

## Data

Gene col 3322: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3322); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3322, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3322]; `tensor/DDL_lfc|DDL_z.npy` [3322]; `embed/gene_vectors.npy` [3322]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3322 or target_col == 3322). Every well: [[RNF8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RNF8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
