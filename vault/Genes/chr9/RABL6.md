---
symbol: "RABL6"
type: "gene"
col: 12254
ensembl_id: "ENSG00000196642"
name: "RAB, member RAS oncogene family like 6"
location: "9q34.3"
module: 158
arm: "+"
pooled_cpm: 71.53
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 6
n_dd_up_clean: 1
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/158"]
generated_by: "tahoemap"
---

# RABL6

*RAB, member RAS oncogene family like 6* — 9q34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.68× (z +12.6, q 8e-34, up in 47 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Peretinoin (drug)]] 0.05 µM: 1.30× (z +3.3, q 0.063, up in 25 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (SW480 3.75×, KATO III 3.92×, SNU-423 4.43×, HEC-1-A 3.12×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 7 lines (KATO III 4.08×, LoVo 4.08×, MIA PaCa-2 4.54×, J82 3.25×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SNU-423 3.63×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.753× (z -5.6, q 1e-05, down in 34 of 48 measured lines) ⚠ cell-cycle shift, explains ~61% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.686× (z -5.2, q 5e-05, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANP32B]] (+0.58, fdr 1e-05), [[MAZ]] (+0.56, fdr 1e-05), [[IQCE]] (+0.54, fdr 4e-05); moves opposite to [[BACH1]] (-0.58, fdr 1e-05), [[ZNF697]] (-0.53, fdr 3e-05), [[DIAPH2-AS1]] (-0.53, fdr 8e-05).
> It is in [[Module 158]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PHLDA1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 7 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12254.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (SW480 3.75×, KATO III 3.92×, SNU-423 4.43×, HEC-1-A 3.12×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 7 lines (KATO III 4.08×, LoVo 4.08×, MIA PaCa-2 4.54×, J82 3.25×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SNU-423 3.63×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.68×** | +12.6 | 8e-34 | 47/49 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.18×** | +10.4 | 9e-23 | 41/41 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.94×** | +8.5 | 4e-15 | 35/45 (SNU-423, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~51% of this change | **1.41×** | +4.8 | 3e-04 | 37/48 (Panc 03.27, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **1.37×** | +4.4 | 0.001 | 27/48 (NCI-H460, C-33 A, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **1.36×** | +4.1 | 0.004 | 30/47 (SW 900, A549, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +4.1 | 0.004 | 26/47 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.30×** | +3.3 | 0.063 | 25/48 (NCI-H460, HEC-1-A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12254.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.753×** | -5.6 | 1e-05 | 34/48 (A498, KATO III, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.686×** | -5.2 | 5e-05 | 32/48 (HT-29, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.787×** | -4.7 | 5e-04 | 34/48 (HT-29, LS 180, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.802×** | -4.3 | 0.002 | 30/48 (HT-29, A-427, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.922× | -3.7 | 0.023 | 1/50 (AN3 CA) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.784×** | -3.4 | 0.069 | 24/48 (HT-29, KATO III, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Sapanisertib (drug)]] 5 µM |  | **0.635×** | -3.3 | 0.081 | 22/49 (SHP-77, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[DTP3 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.804× | -3.0 | 0.15 | 13/48 (KATO III, A549, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | 0.660× | -3.0 | 0.15 | 21/49 (HEC-1-A, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12254. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 140 | 1 (1 ⚠) | 5 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.22× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -15.3) |
| [[MIA PaCa-2 (line)]] | alt | 71.9 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.54× (z +11.6) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 109 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.47× (z +10.4) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 50.7 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.09× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.423× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 118 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +11.5) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 84.9 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.08× (z +11.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -9.5) |
| [[Panc 03.27 (line)]] | alt | 64.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.11× (z +9.2) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 58.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.43× (z +12.0) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 83.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.51× (z +9.4) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 101 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.25× (z +11.4) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 90.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.08× (z +12.9) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 60.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.55× (z +10.7) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 75.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.97× (z +10.0) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 82.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.75× (z +13.3) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 70.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.96× (z +8.9) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 29.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.85× (z +9.3) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 68.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -8.6) ⚠ cell-cycle shift, explains ~6% of this change |
| [[H4 (line)]] | wt | 47.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.56× (z +8.5) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 52.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +8.7) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 68.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.67× (z +9.2) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 42.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.45× (z +9.0) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 84.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.61× (z +9.1) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 55.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 70.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 69.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 127 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 47.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 97.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 83.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 92.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 53.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 59.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 82.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 69.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 79.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 142 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 79.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 50.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 66.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 74.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12254), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*47 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANP32B]] | +0.58 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[MAZ]] | +0.56 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[IQCE]] | +0.54 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[USF2]] | +0.53 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[RCN2]] | +0.53 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[DNM2]] | +0.53 | +0.42 / +0.57 | both halves | 4e-05 | same gene group |
| [[PPM1B]] | +0.53 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[RSBN1L]] | +0.52 | +0.60 / +0.46 | both halves | 3e-05 |  |
| [[CEP43]] | +0.51 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[PAXBP1]] | +0.51 | +0.60 / +0.38 | both halves | 6e-05 |  |
| [[NCOA6]] | +0.49 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[HADH]] | +0.48 | +0.44 / +0.30 | both halves | 2e-04 |  |

## Genes that move opposite

*53 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BACH1]] | -0.58 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[ZNF697]] | -0.53 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[DIAPH2-AS1]] | -0.53 | -0.37 / -0.54 | both halves | 8e-05 |  |
| [[PRKG2-AS1]] | -0.52 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[ICAM2]] | -0.51 | -0.39 / -0.47 | both halves | 6e-05 |  |
| [[ZNF222]] | -0.51 | -0.51 / -0.37 | both halves | 8e-05 |  |
| [[SFR1]] | -0.50 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[KBTBD8]] | -0.50 | -0.52 / -0.33 | both halves | 1e-04 |  |
| [[SERPINB8]] | -0.49 | -0.50 / -0.39 | both halves | 5e-05 |  |
| [[ABL2]] | -0.49 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[ODC1]] | -0.49 | -0.36 / -0.55 | both halves | 9e-05 |  |
| [[CD163L1]] | -0.49 | -0.49 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PHLDA1]] | B | PHLDA1 activity lowers RABL6's level | lines that do not express PHLDA1 (5) vs lines expressing it (45) | 1.77× higher at baseline in the lines without PHLDA1 | 0.069 | ⚠ within organs, on part of the lines; also absent: DPYSL2, PARP3, C1RL; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 158]]; 27 genes; every member is in the + arm (projection on the module's main direction -0.643). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-15.3, -50.0); signed map (-40.8, -29.3). **Vector** length 71.0, 18.5% of its response variance represented; |z| ≥ 3 in 679 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +0.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +1.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | +0.6 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +2.0 | +1.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | +2.0 | +4.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.0 | +2.0 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +2.0 | +2.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.7 | +0.5 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | -6.0 | -5.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.6 | -5.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.0 | -4.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.9 | -3.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | -1.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.1 | -0.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.6 | -2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -0.5 |
|  | [[Belzutifan (drug)]] 5 µM |  | -1.8 | +0.9 |

## What is on record

|  |  |
|---|---|
| Name | RAB, member RAS oncogene family like 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.3 — chr9:136,807,943-136,841,187 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10101, FLJ13045, pp8875, bA216L13.9, Parf, RBEL1; previously C9orf86 |
| Gene groups (HGNC) | RAB like GTPases; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q3YEC7](https://www.uniprot.org/uniprotkb/Q3YEC7) (Rab-like protein 6):

> Small GTPase involved in the regulation of cell growth and survival. Promotes cellular proliferation. May reduce growth inhibitory activity of CDKN2A.

**Summary**, from NCBI Gene [55684](https://www.ncbi.nlm.nih.gov/gene/55684):

> This gene encodes a member of the Ras superfamily of small GTPases. The encoded protein binds to both GTP and GDP and may play a role in cell growth and survival. Overexpression of this gene may play a role in breast cancer tumorigenesis, and pseudogenes of this gene are located on the long arm of chromosome 2 and the short arm of chromosome 18. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Dec 2011]

**Accessions** — [HGNC:24703](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24703) · Entrez [55684](https://www.ncbi.nlm.nih.gov/gene/55684) · UniProt [Q3YEC7](https://www.uniprot.org/uniprotkb/Q3YEC7) · Ensembl [ENSG00000196642](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196642)

## Data

Gene col 12254: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12254); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12254, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12254]; `tensor/DDL_lfc|DDL_z.npy` [12254]; `embed/gene_vectors.npy` [12254]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12254 or target_col == 12254). Every well: [[RABL6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RABL6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
