---
symbol: "OTUD5"
type: "gene"
col: 885
ensembl_id: "ENSG00000068308"
name: "OTU deubiquitinase 5"
location: "Xp11.23"
module: 145
arm: "+"
pooled_cpm: 68.1
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 25
n_dd_up_clean: 4
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/145"]
generated_by: "tahoemap"
---

# OTUD5

*OTU deubiquitinase 5* — Xp11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[PH-797804 (drug)]] 5 µM: 1.89× (z +6.8, q 4e-09, up in 29 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (7 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.529× (z -13.1, q 2e-36, down in 46 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[venetoclax (drug)]] 5 µM: 0.430× (z -9.1, q 4e-17, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[INPP5K]] (+0.73, fdr 7e-06), [[CYTH2]] (+0.72, fdr 7e-06), [[PAIP2]] (+0.69, fdr 7e-06); moves opposite to [[OTUD6B]] (-0.62, fdr 1e-05), [[ATIC]] (-0.56, fdr 1e-05), [[HEATR3]] (-0.55, fdr 1e-05).
> It is in [[Module 145]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 885.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **1.89×** | +6.8 | 4e-09 | 29/48 (SW480, MIA PaCa-2, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.20×** | +5.4 | 2e-05 | 24/49 (MIA PaCa-2, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.51×** | +4.5 | 0.002 | 23/49 (LoVo, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.44×** | +3.9 | 0.013 | 22/48 (CFPAC-1, NCI-H2347, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~4% of this change | 1.19× | +3.3 | 0.100 | 16/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 885.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.529×** | -13.1 | 2e-36 | 46/48 (HT-29, NCI-H460, …) | all doses, flat |  |
| [[venetoclax (drug)]] 5 µM |  | **0.430×** | -9.1 | 4e-17 | 39/48 (SHP-77, RPMI-7951, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.462×** | -8.3 | 2e-14 | 43/48 (NCI-H460, Hs 766T, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[EX229 (drug)]] 5 µM |  | **0.471×** | -8.1 | 9e-14 | 38/48 (SW1417, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.497×** | -7.5 | 7e-12 | 36/48 (MIA PaCa-2, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.706×** | -7.1 | 9e-11 | 30/48 (A498, SW 900, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.708×** | -7.1 | 1e-10 | 30/48 (NCI-H1792, A498, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.521×** | -7.0 | 2e-10 | 36/48 (KATO III, HT-29, …) | all doses, flat | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.786×** | -7.0 | 2e-10 | 30/48 (NCI-H2347, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.740×** | -6.2 | 4e-08 | 31/48 (A498, BT-474, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.749×** | -5.7 | 6e-07 | 28/47 (MIA PaCa-2, RPMI-7951, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.766×** | -5.5 | 2e-06 | 30/48 (SW 1088, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.833×** | -5.3 | 5e-06 | 24/48 (A549, A-172, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.704×** | -5.1 | 1e-05 | 27/48 (PANC-1, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.771×** | -5.1 | 1e-05 | 30/48 (MIA PaCa-2, NCI-H1573, …) | top dose only |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.718×** | -4.8 | 4e-05 | 29/49 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.793×** | -4.8 | 6e-05 | 27/48 (AN3 CA, SNU-423, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.804×** | -4.1 | 0.001 | 26/48 (AsPC-1, SW480, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.817×** | -4.0 | 0.002 | 21/48 (SW480, HT-29, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **0.690×** | -4.0 | 0.002 | 22/49 (HT-29, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 885. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 48.4 | 0 | 4 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.385× (z -11.3) ⚠ unreliable plate only |
| [[HT-29 (line)]] | alt | 84.7 | 0 | 4 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.330× (z -12.7) ⚠ unreliable plate only |
| [[MIA PaCa-2 (line)]] | alt | 126 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.83× (z +10.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.400× (z -11.6) ⚠ unreliable plate only · without an alert: [[venetoclax (drug)]] 5 µM 0.254× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 65.8 | 3 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +12.1) ⚠ cell-cycle shift, explains ~9% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.378× (z -12.4) ⚠ unreliable plate only |
| [[SW480 (line)]] | alt | 86.5 | 3 (3 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.09× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.526× (z -9.3) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 62.6 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.476× (z -8.8) ⚠ cell-cycle shift, explains ~35% of this change |
| [[KATO III (line)]] | alt | 90.0 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.357× (z -11.6) ⚠ unreliable plate only · without an alert: [[venetoclax (drug)]] 5 µM 0.237× (z -8.5) |
| [[LoVo (line)]] | wt | 59.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.30× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.342× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change |
| [[NCI-H1792 (line)]] | alt | 64.3 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.310× (z -11.5) ⚠ cell-cycle shift, explains ~35% of this change |
| [[NCI-H23 (line)]] | alt | 65.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.115× (z -20.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[RPMI-7951 (line)]] | alt | 132 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.274× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[venetoclax (drug)]] 5 µM 0.190× (z -9.1) |
| [[SK-MEL-2 (line)]] | alt | 63.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +10.3) ⚠ cell-cycle shift, explains ~9% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.360× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[A-427 (line)]] | wt | 70.9 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.426× (z -9.6) ⚠ unreliable plate only |
| [[AN3 CA (line)]] | alt | 82.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.128× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change |
| [[AsPC-1 (line)]] | alt | 56.4 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.347× (z -10.2) ⚠ unreliable plate only |
| [[C32 (line)]] | wt | 46.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0654× (z -19.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[CFPAC-1 (line)]] | alt | 74.6 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.535× (z -10.3) |
| [[HCT15 (line)]] | alt | 79.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.276× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change |
| [[NCI-H2347 (line)]] | alt | 54.5 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.474× (z -12.2) |
| [[PANC-1 (line)]] | alt | 67.4 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.496× (z -9.9) ⚠ unreliable plate only |
| [[SHP-77 (line)]] | alt | 39.9 | 0 | 1 | — | [[venetoclax (drug)]] 5 µM 0.0449× (z -13.4) |
| [[SNU-423 (line)]] | alt | 135 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.526× (z -10.9) |
| [[SW1417 (line)]] | alt | 77.4 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.330× (z -12.2) ⚠ unreliable plate only |
| [[A549 (line)]] | wt | 98.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 67.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 51.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 73.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 83.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 41.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 103 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 59.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 65.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 77.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 36.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 46.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 78.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 65.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 66.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 77.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 42.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 37.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 69.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 53.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 885), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INPP5K]] | +0.73 | +0.75 / +0.80 | both halves | 7e-06 |  |
| [[CYTH2]] | +0.72 | +0.61 / +0.77 | both halves | 7e-06 |  |
| [[PAIP2]] | +0.69 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[STX5]] | +0.69 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[RAB5A]] | +0.68 | +0.68 / +0.74 | both halves | 7e-06 |  |
| [[TBC1D15]] | +0.66 | +0.50 / +0.68 | both halves | 1e-05 |  |
| [[SLU7]] | +0.64 | +0.40 / +0.67 | both halves | 5e-05 |  |
| [[MXD4]] | +0.63 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[COQ10B]] | +0.63 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[ZNF394]] | +0.62 | +0.44 / +0.68 | both halves | 3e-05 |  |
| [[OSBPL2]] | +0.62 | +0.57 / +0.73 | both halves | 1e-05 |  |
| [[YIPF3]] | +0.62 | +0.52 / +0.67 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OTUD6B]] | -0.62 | -0.57 / -0.62 | both halves | 1e-05 | same gene group; STRING 650 |
| [[ATIC]] | -0.56 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[HEATR3]] | -0.55 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[CLN6]] | -0.55 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[C12orf29]] | -0.54 | -0.40 / -0.65 | both halves | 5e-05 |  |
| [[AGPS]] | -0.54 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[STX18-AS1]] | -0.54 | -0.46 / -0.54 | both halves | 2e-05 |  |
| [[TMEM177]] | -0.54 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[DTD2]] | -0.54 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[SFXN4]] | -0.53 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[MRPL42]] | -0.53 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[ADAT2]] | -0.52 | -0.47 / -0.54 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises OTUD5's level | compounds that target MAP2K1: 3 of 4 lower it (Cobimetinib, TAK-733, Trametinib) | 75% of the class's compounds vs 4.8% of all compounds | 0.0995 | ⚠ off-target possible; 3 compounds |
| [[IQCD]] | C | IQCD activity raises OTUD5's level | lines that do not express IQCD (4) vs lines expressing it (46) | 1.46× lower at baseline in the lines without IQCD | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-occurs with TGFBR2, BRCA2; also absent: RBMS1, ENSG00000235978, FBXL2; maybe low, not absent |
| [[FXN]] | C | FXN's natural level weakens OTUD5's drug response | FXN's natural level across 46 lines (lineage-adjusted; a glimpse) | r -0.63, reverse -0.07; direction not clear | 0.092 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 145]]; 31 genes; every member is in the + arm (projection on the module's main direction 0.612). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.21; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (5.3, -41.9); signed map (-15.7, 10.0). **Vector** length 121, 33.8% of its response variance represented; |z| ≥ 3 in 1,119 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.5 | +5.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +3.3 | +2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +3.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~4% of this change | +3.0 | +3.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +1.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.4 | +3.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -13.0 | -13.1 |
|  | [[EX229 (drug)]] 5 µM |  | -8.1 | -8.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -8.1 | -8.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -7.7 | -7.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -7.5 | -7.5 |
|  | [[venetoclax (drug)]] 5 µM |  | -7.4 | -9.1 |

## What is on record

|  |  |
|---|---|
| Name | OTU deubiquitinase 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.23 — chrX:48,922,024-48,958,386 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp761A052, DUBA |
| Gene groups (HGNC) | OTU domain containing |
| Reactome | 5 pathways, smallest: Negative regulators of DDX58/IFIH1 signaling; Ovarian tumor domain proteases; DDX58/IFIH1-mediated induction of interferon-alpha/beta |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96G74](https://www.uniprot.org/uniprotkb/Q96G74) (OTU domain-containing protein 5):

> Deubiquitinating enzyme that functions as a negative regulator of the innate immune system. Has peptidase activity towards 'Lys-48'- and 'Lys-63'-linked polyubiquitin chains. Can also cleave 'Lys-11'-linked ubiquitin chains (in vitro). Acts via TRAF3 deubiquitination and subsequent suppression of type I interferon (IFN) production. Controls neuroectodermal differentiation through cleaving 'Lys-48'-linked ubiquitin chains to counteract degradation of select chromatin regulators such as ARID1A, …

**Summary**, from NCBI Gene [55593](https://www.ncbi.nlm.nih.gov/gene/55593):

> This gene encodes a member of the OTU (ovarian tumor) domain-containing cysteine protease superfamily. The OTU domain confers deubiquitinase activity and the encoded protein has been shown to suppress the type I interferon-dependent innate immune response by cleaving the polyubiquitin chain from an essential type I interferon adaptor protein. Cleavage results in disassociation of the adaptor protein from a downstream signaling complex and disruption of the type I interferon signaling cascade. …

**Accessions** — [HGNC:25402](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25402) · Entrez [55593](https://www.ncbi.nlm.nih.gov/gene/55593) · UniProt [Q96G74](https://www.uniprot.org/uniprotkb/Q96G74) · Ensembl [ENSG00000068308](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000068308)

## Data

Gene col 885: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 885); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 885, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 885]; `tensor/DDL_lfc|DDL_z.npy` [885]; `embed/gene_vectors.npy` [885]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 885 or target_col == 885). Every well: [[OTUD5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OTUD5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
