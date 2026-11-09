---
symbol: "SPPL2A"
type: "gene"
col: 6190
ensembl_id: "ENSG00000138600"
name: "signal peptide peptidase like 2A"
location: "15q21.2"
module: 68
arm: "+"
pooled_cpm: 108.47
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 6
n_dd_up_clean: 7
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# SPPL2A

*signal peptide peptidase like 2A* — 15q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.67× (z +15.9, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.630× (z -10.1, q 4e-21, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CLN5]] (+0.65, fdr 1e-05), [[SMIM19]] (+0.64, fdr 2e-05), [[WAC-AS1]] (+0.62, fdr 6e-05); moves opposite to [[RRP1B]] (-0.61, fdr 1e-05), [[NKRF]] (-0.59, fdr 1e-05), [[GNB1L]] (-0.56, fdr 3e-05).
> It sits in the **+** arm of [[Module 068]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6190.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.67×** | +15.9 | 0e+00 | 44/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.62×** | +10.2 | 8e-22 | 42/48 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.46×** | +8.3 | 2e-14 | 33/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.40×** | +7.3 | 2e-11 | 33/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.90×** | +7.3 | 2e-11 | 33/49 (HT-29, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.24×** | +4.7 | 2e-04 | 22/48 (BT-474, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.23×** | +4.4 | 9e-04 | 23/47 (PANC-1, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.22×** | +4.3 | 0.001 | 22/48 (RKO, J82, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.21×** | +4.3 | 0.001 | 25/48 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.21×** | +4.1 | 0.002 | 22/48 (C-33 A, LoVo, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.12× | +3.5 | 0.026 | 13/49 (SW1417, MIA PaCa-2, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.12× | +3.5 | 0.026 | 12/49 (PANC-1, CFPAC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6190.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.630×** | -10.1 | 4e-21 | 44/48 (KATO III, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.635×** | -9.9 | 1e-20 | 41/48 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.637×** | -9.8 | 2e-20 | 44/48 (J82, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.671×** | -8.7 | 6e-16 | 43/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.720×** | -7.2 | 1e-10 | 34/48 (HOP62, MIA PaCa-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.717×** | -7.0 | 3e-10 | 37/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.948× | -4.4 | 0.001 | 0/50 | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.842× | -3.7 | 0.013 | 20/48 (NCI-H2347, LoVo, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | 0.858× | -3.2 | 0.084 | 20/47 (HT-29, NCI-H1573, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6190. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 101 | 9 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +22.7) | — |
| [[PANC-1 (line)]] | alt | 151 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +25.7) | — |
| [[BT-474 (line)]] | alt | 81.8 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.65× (z +13.2) | — |
| [[KATO III (line)]] | alt | 101 | 3 (1 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.44× (z +17.7) | [[Panobinostat (drug)]] 0.5 µM 0.321× (z -16.2) |
| [[SW480 (line)]] | alt | 84.0 | 1 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +12.7) | [[Belinostat (drug)]] 5 µM 0.455× (z -13.4) |
| [[SNU-1 (line)]] | wt | 126 | 4 (1 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.64× (z +12.2) | [[Dinaciclib (drug)]] 0.5 µM 0.327× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 152 | 2 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.07× (z +10.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.90× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.340× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change |
| [[NCI-H23 (line)]] | alt | 94.5 | 2 (1 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 2.05× (z +9.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.93× (z +8.6) | [[Panobinostat (drug)]] 5 µM 0.520× (z -8.7) |
| [[A-427 (line)]] | wt | 79.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.330× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change |
| [[A549 (line)]] | wt | 226 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +17.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.603× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 102 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.355× (z -12.1) |
| [[COLO 205 (line)]] | alt | 128 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.412× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 79.2 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +10.0) | [[Auranofin (drug)]] 5 µM 0.526× (z -8.5) |
| [[HOP62 (line)]] | alt | 80.3 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.460× (z -10.5) |
| [[Hs 766T (line)]] | wt | 90.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +9.9) | — |
| [[HT-29 (line)]] | alt | 134 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 3.65× (z +9.5) | [[Panobinostat (drug)]] 0.5 µM 0.487× (z -10.0) |
| [[J82 (line)]] | alt | 99.6 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +9.7) | [[Belinostat (drug)]] 0.5 µM 0.536× (z -8.7) |
| [[LOX-IMVI (line)]] | wt | 112 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.349× (z -12.6) |
| [[MIA PaCa-2 (line)]] | alt | 62.4 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +12.7) | [[Auranofin (drug)]] 5 µM 0.369× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 82.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.134× (z -20.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change |
| [[SW1417 (line)]] | alt | 95.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.444× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change |
| [[A-172 (line)]] | wt | 90.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +11.5) | — |
| [[A498 (line)]] | wt | 102 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +10.1) | — |
| [[CFPAC-1 (line)]] | alt | 128 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +10.2) | — |
| [[H4 (line)]] | wt | 95.0 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.160× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~1% of this change |
| [[HepG2_C3A (line)]] | wt | 100 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +12.9) | — |
| [[LoVo (line)]] | wt | 123 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 1.94× (z +8.8) | — |
| [[NCI-H2030 (line)]] | alt | 208 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.360× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change |
| [[NCI-H2347 (line)]] | alt | 129 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +10.8) | — |
| [[Panc 03.27 (line)]] | alt | 126 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +11.7) | — |
| [[RKO (line)]] | wt | 90.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +15.7) | — |
| [[RPMI-7951 (line)]] | alt | 116 | 0 | 1 | — | [[Belzutifan (drug)]] 5 µM 0.170× (z -10.5) |
| [[SW48 (line)]] | wt | 84.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +12.0) | — |
| [[AN3 CA (line)]] | alt | 98.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 90.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 62.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 79.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 92.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 101 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 85.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 68.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 93.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 93.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 75.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6190), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLN5]] | +0.65 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[SMIM19]] | +0.64 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[WAC-AS1]] | +0.62 | +0.39 / +0.51 | both halves | 6e-05 |  |
| [[FAM200B]] | +0.60 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[TRAM2-AS1]] | +0.60 | +0.46 / +0.39 | both halves | 6e-05 |  |
| [[TRAPPC6B]] | +0.59 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[TAPT1]] | +0.59 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[TSTD3]] | +0.58 | +0.50 / +0.38 | both halves | 6e-05 |  |
| [[STAT5A]] | +0.58 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[ETFRF1]] | +0.57 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[UBXN2A]] | +0.57 | +0.36 / +0.54 | both halves | 9e-05 |  |
| [[TMEM35B]] | +0.56 | +0.43 / +0.32 | both halves | 1e-04 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRP1B]] | -0.61 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[NKRF]] | -0.59 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[GNB1L]] | -0.56 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[RNF216]] | -0.56 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[EIPR1]] | -0.56 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[POLR3H]] | -0.55 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[POLRMT]] | -0.55 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[EPS15L1]] | -0.54 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[SPATA5]] | -0.54 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[RUVBL2]] | -0.54 | -0.33 / -0.52 | both halves | 1e-04 |  |
| [[EIF1AD]] | -0.53 | -0.39 / -0.55 | both halves | 6e-05 |  |
| [[LPCAT1]] | -0.52 | -0.34 / -0.41 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises SPPL2A's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **+** arm (projection on the module's main direction 0.542). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (2.2, 13.5); signed map (22.3, -14.8). **Vector** length 108, 30.6% of its response variance represented; |z| ≥ 3 in 1,085 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.6 | +15.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.9 | +3.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +7.2 | -1.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change | +7.1 | -2.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.8 | +10.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.4 | -0.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | -0.7 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.8 | +1.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.6 | -0.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.6 | +0.1 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -6.7 | -9.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.2 | -7.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -5.0 | -1.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.0 | -1.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.5 | -2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.4 | -2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.9 | +0.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.6 | -2.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.2 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | signal peptide peptidase like 2A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.2 — chr15:50,702,266-50,765,948 (-) |
| Ensembl biotype | protein_coding |
| Also known as | IMP3, PSL2 |
| Gene groups (HGNC) | Signal peptide peptidase like family |
| Hallmark sets | INTERFERON_GAMMA_RESPONSE |
| Reactome | 3 pathways, smallest: Regulation of TNFR1 signaling; TNF signaling; Death Receptor Signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TCT8](https://www.uniprot.org/uniprotkb/Q8TCT8) (Signal peptide peptidase-like 2A):

> Intramembrane-cleaving aspartic protease (I-CLiP) that cleaves type II membrane signal peptides in the hydrophobic plane of the membrane. Functions in FASLG, ITM2B and TNF processing. Catalyzes the intramembrane cleavage of the anchored fragment of shed TNF (TNF), which promotes the release of the intracellular domain (ICD) for signaling to the nucleus. Also responsible for the intramembrane cleavage of Fas antigen ligand FASLG, which promotes the release of the intracellular FasL domain (FasL …

**Summary**, from NCBI Gene [84888](https://www.ncbi.nlm.nih.gov/gene/84888):

> This gene encodes a member of the GXGD family of aspartic proteases, which are transmembrane proteins with two conserved catalytic motifs localized within the membrane-spanning regions, as well as a member of the signal peptide peptidase-like protease (SPPL) family. This protein is expressed in all major adult human tissues and localizes to late endosomal compartments and lysosomal membranes. A pseudogene of this gene also lies on chromosome 15. [provided by RefSeq, Feb 2012]

**Accessions** — [HGNC:30227](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30227) · Entrez [84888](https://www.ncbi.nlm.nih.gov/gene/84888) · UniProt [Q8TCT8](https://www.uniprot.org/uniprotkb/Q8TCT8) · Ensembl [ENSG00000138600](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138600)

## Data

Gene col 6190: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6190); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6190, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6190]; `tensor/DDL_lfc|DDL_z.npy` [6190]; `embed/gene_vectors.npy` [6190]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6190 or target_col == 6190). Every well: [[SPPL2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPPL2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
