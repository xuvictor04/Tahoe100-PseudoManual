---
symbol: "MRNIP"
type: "gene"
col: 8407
ensembl_id: "ENSG00000161010"
name: "MRN complex interacting protein"
location: "5q35.3"
module: 20
arm: "-"
pooled_cpm: 38.69
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 17
n_dd_up_clean: 4
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# MRNIP

*MRN complex interacting protein* — 5q35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 1.59× (z +10.2, q 1e-21, up in 30 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.587× (z -11.7, q 7e-29, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SUGP1]] (+0.64, fdr 1e-05), [[NOSIP]] (+0.62, fdr 1e-05), [[WIPF2]] (+0.62, fdr 3e-05); moves opposite to [[NAA50]] (-0.56, fdr 1e-05), [[FUCA2]] (-0.56, fdr 1e-05), [[RCC2]] (-0.54, fdr 3e-05).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8407.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.59×** | +10.2 | 1e-21 | 30/48 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.41×** | +7.5 | 2e-11 | 27/48 (PANC-1, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.33×** | +6.3 | 7e-08 | 23/48 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.25×** | +4.9 | 1e-04 | 19/48 (HOP62, NCI-H2030, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.19× | +3.9 | 0.012 | 12/48 (LoVo, A-172, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.5 | 0.051 | 18/48 (NCI-H2347, SW480, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.16× | +3.3 | 0.091 | 12/48 (KATO III, CFPAC-1, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.11× | +3.1 | 0.13 | 17/48 (LoVo, COLO 205, …) | top dose only | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8407.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.587×** | -11.7 | 7e-29 | 39/48 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.602×** | -11.2 | 2e-26 | 44/48 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.605×** | -11.0 | 4e-26 | 39/48 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.614×** | -10.7 | 1e-24 | 33/48 (SNU-423, AN3 CA, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.649×** | -9.5 | 2e-19 | 34/48 (C-33 A, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.760×** | -8.6 | 1e-15 | 30/48 (A-172, SNU-1, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.678×** | -8.2 | 2e-14 | 29/47 (BT-474, H4, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.705×** | -7.1 | 9e-11 | 24/43 (Panc 03.27, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.727×** | -7.0 | 2e-10 | 31/48 (NCI-H460, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.734×** | -6.8 | 6e-10 | 26/47 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.606×** | -5.8 | 4e-07 | 24/48 (LOX-IMVI, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.612×** | -5.6 | 8e-07 | 22/49 (A-172, SNU-423, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.780×** | -5.5 | 2e-06 | 21/48 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.787×** | -5.3 | 5e-06 | 22/48 (H4, A-172, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.826×** | -4.2 | 1e-03 | 16/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.829×** | -4.1 | 0.001 | 17/48 (NCI-H460, C-33 A, …) | rises with dose |  |
| [[Benproperine (phosphate) (drug)]] 5 µM |  | 0.863× | -3.1 | 0.057 | 8/48 (C32, NCI-H1573, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8407. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 45.4 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.337× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.351× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 37.4 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.295× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.05 µM 0.403× (z -10.0) |
| [[SNU-423 (line)]] | alt | 51.9 | 0 | 4 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.242× (z -11.8) |
| [[C-33 A (line)]] | alt | 86.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.173× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[HOP62 (line)]] | alt | 49.8 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.273× (z -13.9) |
| [[SNU-1 (line)]] | wt | 40.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.222× (z -9.2) ⚠ cell-cycle shift, explains ~1% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.345× (z -9.2) |
| [[BT-474 (line)]] | alt | 25.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.103× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[COLO 205 (line)]] | alt | 34.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +12.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.258× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[H4 (line)]] | wt | 59.2 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.206× (z -10.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 34.9 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.01× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.387× (z -10.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 76.8 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.492× (z -9.9) |
| [[AN3 CA (line)]] | alt | 47.5 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.137× (z -9.4) |
| [[HCT15 (line)]] | alt | 53.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.280× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[HEC-1-A (line)]] | alt | 72.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.335× (z -11.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 43.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +14.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 53.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.410× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[Panc 03.27 (line)]] | alt | 52.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.181× (z -16.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 44.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.328× (z -8.8) |
| [[SW 1271 (line)]] | alt | 48.5 | 0 | 1 | — | [[Rifaximin (drug)]] 5 µM 0.0712× (z -8.8) |
| [[SW48 (line)]] | wt | 31.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.196× (z -8.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 32.6 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.462× (z -8.5) |
| [[A-427 (line)]] | wt | 37.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 33.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 36.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 39.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 37.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 30.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8407), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUGP1]] | +0.64 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[NOSIP]] | +0.62 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[WIPF2]] | +0.62 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[ACTR1B]] | +0.59 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[NBPF12]] | +0.57 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[SIDT2]] | +0.56 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[NPHP3]] | +0.56 | +0.62 / +0.57 | both halves | 9e-06 |  |
| [[PFKFB4]] | +0.56 | +0.39 / +0.45 | both halves | 5e-05 |  |
| [[MAPK8IP3]] | +0.56 | +0.45 / +0.44 | both halves | 3e-05 |  |
| [[ZNF395]] | +0.55 | +0.53 / +0.36 | both halves | 1e-04 |  |
| [[RANBP10]] | +0.54 | +0.36 / +0.53 | both halves | 1e-04 |  |
| [[NBPF11]] | +0.54 | +0.46 / +0.60 | both halves | 2e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAA50]] | -0.56 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[FUCA2]] | -0.56 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[RCC2]] | -0.54 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[EPM2A]] | -0.53 | -0.30 / -0.40 | both halves | 2e-04 |  |
| [[RCN1]] | -0.52 | -0.33 / -0.49 | both halves | 1e-04 |  |
| [[EMB]] | -0.52 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[TMEM33]] | -0.52 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[ATE1]] | -0.51 | -0.38 / -0.50 | both halves | 7e-05 |  |
| [[TMX3]] | -0.51 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[PSME3]] | -0.51 | -0.34 / -0.50 | both halves | 1e-04 |  |
| [[PON2]] | -0.50 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[MOB1A]] | -0.50 | -0.33 / -0.51 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers MRNIP's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ZNF404]] | B | ZNF404 activity raises MRNIP's level | lines that do not express ZNF404 (14) vs lines expressing it (36) | 1.44× lower at baseline in the lines without ZNF404 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: MIR130AHG, RAB34, PYGO1 |
| [[WDR54]] | C | WDR54 activity raises MRNIP's level | lines that do not express WDR54 (4) vs lines expressing it (46) | 1.46× lower at baseline in the lines without WDR54 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: COPZ2, CNTLN, KLF9; maybe low, not absent; its own permutation p |
| [[TERT]] | C | TERT activity strengthens MRNIP's drug response | recorded gain-of-function mutation of TERT in 8 lines vs 37 not recorded | the TERT-altered lines respond 1.57× as strongly (z diff -1.53); strongest at Ouabain (Octahydrate) 5 µM: 0.37x vs 0.63x (z diff -4.0) | 0.170 over the table, 0.079 within its group | ⚠ within its group only (a lead); tissue-confounded; across organs; TERT not expressed in 1 of the 8 altered lines; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.489). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-25.0, -30.7); signed map (-26.9, 12.9). **Vector** length 88.0, 18.9% of its response variance represented; |z| ≥ 3 in 930 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.4 | +3.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.9 | +2.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.8 | +10.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.3 | +6.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.3 | +7.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.3 | +4.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.2 | +0.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +2.2 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.5 | -0.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.3 | -10.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.2 | -8.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.5 | -8.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.7 | -7.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -0.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.0 | -0.8 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.3 | -1.1 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -1.8 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | MRN complex interacting protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.3 — chr5:179,835,133-179,862,173 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC65027, MGC78537, DKFZp686L2452, LOC51149; previously C5orf45 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6NTE8](https://www.uniprot.org/uniprotkb/Q6NTE8) (MRN complex-interacting protein):

> Plays a role in the cellular response to DNA damage and the maintenance of genome stability through its association with the MRN damage-sensing complex. Promotes chromatin loading and activity of the MRN complex to facilitate subsequent ATM-mediated DNA damage response signaling and DNA repair.

**Summary**, from NCBI Gene [51149](https://www.ncbi.nlm.nih.gov/gene/51149):

> Enables chromatin binding activity. Involved in several processes, including mitotic G2 DNA damage checkpoint signaling; positive regulation of protein kinase activity; and regulation of double-strand break repair. Located in Mre11 complex and nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30817](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30817) · Entrez [51149](https://www.ncbi.nlm.nih.gov/gene/51149) · UniProt [Q6NTE8](https://www.uniprot.org/uniprotkb/Q6NTE8) · Ensembl [ENSG00000161010](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161010)

## Data

Gene col 8407: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8407); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8407, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8407]; `tensor/DDL_lfc|DDL_z.npy` [8407]; `embed/gene_vectors.npy` [8407]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8407 or target_col == 8407). Every well: [[MRNIP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRNIP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
