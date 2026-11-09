---
symbol: "AKR7A2"
type: "gene"
col: 592
ensembl_id: "ENSG00000053371"
name: "aldo-keto reductase family 7 member A2"
location: "1p36.13"
module: 58
arm: "+"
pooled_cpm: 12.51
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 18
n_dd_up_clean: 6
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# AKR7A2

*aldo-keto reductase family 7 member A2* — 1p36.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.20× (z +8.5, q 7e-15, up in 43 of 48 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[XRK3F2 (drug)]] 0.5 µM: 1.73× (z +4.3, q 0.002, up in 23 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.497× (z -10.7, q 7e-24, down in 34 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR54]] (+0.79, fdr 7e-06), [[VKORC1]] (+0.72, fdr 1e-05), [[GAPDH]] (+0.69, fdr 1e-05); moves opposite to [[KCNMB3]] (-0.60, fdr 4e-05), [[RIPK2-DT]] (-0.58, fdr 5e-05), [[SPTY2D1OS]] (-0.58, fdr 1e-04).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ALDOC]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 9 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 592.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.20×** | +8.5 | 7e-15 | 43/48 (PANC-1, A498, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **2.16×** | +8.3 | 2e-14 | 39/48 (A-172, KATO III, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **1.95×** | +7.3 | 7e-11 | 28/38 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.70×** | +5.8 | 1e-06 | 35/47 (A498, HOP62, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **1.68×** | +5.4 | 6e-06 | 12/22 (MIA PaCa-2, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.73×** | +4.3 | 0.002 | 23/43 (NCI-H1792, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +4.0 | 0.004 | 4/48 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.68×** | +4.0 | 0.004 | 20/45 (A498, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.41×** | +3.7 | 0.011 | 15/42 (LS 180, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~23% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.61×** | +3.7 | 0.012 | 14/45 (PANC-1, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.73×** | +3.5 | 0.024 | 9/33 (LoVo, SNU-423, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[BI-78D3 (drug)]] 0.5 µM |  | **1.54×** | +3.3 | 0.036 | 14/46 (HCT15, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.36×** | +3.3 | 0.036 | 10/47 (NCI-H2347, HepG2/C3A, …) | inconsistent across doses |  |
| [[AZD-7648 (drug)]] 0.5 µM |  | **1.51×** | +3.2 | 0.058 | 14/46 (A-427, HOP62, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.22×** | +3.1 | 0.075 | 16/45 (LS 180, A549, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 592.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.497×** | -10.7 | 7e-24 | 34/46 (NCI-H23, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.588×** | -5.7 | 3e-06 | 30/45 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.592×** | -5.7 | 3e-06 | 28/46 (C-33 A, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.630×** | -5.0 | 9e-05 | 26/46 (LoVo, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.647×** | -4.7 | 3e-04 | 26/48 (SNU-1, A-427, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.670×** | -4.3 | 0.002 | 25/46 (SK-MEL-2, C-33 A, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.666×** | -4.2 | 0.002 | 21/47 (A-427, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.691×** | -4.0 | 0.005 | 19/46 (NCI-H460, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.692×** | -4.0 | 0.005 | 18/47 (C32, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.716×** | -3.6 | 0.017 | 20/45 (H4, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.439×** | -3.6 | 0.017 | 16/46 (A-427, HT-29, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.708×** | -3.5 | 0.021 | 15/46 (PANC-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~22% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.720×** | -3.4 | 0.029 | 14/41 (KATO III, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tadalafil (drug)]] 5 µM |  | **0.721×** | -3.4 | 0.029 | 18/46 (NCI-H661, hTERT-HPNE, …) | top dose only |  |
| [[Hydroxyurea (drug)]] 5 µM |  | **0.731×** | -3.2 | 0.046 | 14/47 (NCI-H2347, HCT15, …) | rises with dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.480×** | -3.2 | 0.050 | 15/42 (A-427, C-33 A, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.737×** | -3.1 | 0.065 | 13/45 (C32, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.41 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 592. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 11.4 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.101× (z -9.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.198× (z -8.9) |
| [[SNU-423 (line)]] | alt | 11.8 | 0 | 2 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0618× (z -14.3) |
| [[A-427 (line)]] | wt | 20.1 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.151× (z -10.9) |
| [[C32 (line)]] | wt | 11.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -8.8) |
| [[HS-578T (line)]] | alt | 19.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -8.8) |
| [[J82 (line)]] | alt | 14.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 13.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -10.5) |
| [[NCI-H23 (line)]] | alt | 17.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -14.2) |
| [[PANC-1 (line)]] | alt | 15.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -9.9) |
| [[A-172 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.27 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.86 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.13 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.12 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.23 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.52 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.28 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.13 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.95 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.26 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 14.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 592), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR54]] | +0.79 | +0.72 / +0.71 | both halves | 7e-06 |  |
| [[VKORC1]] | +0.72 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[GAPDH]] | +0.69 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[SLC25A11]] | +0.68 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[GLG1]] | +0.68 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[NDUFV1]] | +0.65 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[CENPX]] | +0.65 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[NDUFS7]] | +0.65 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[TRAPPC1]] | +0.64 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[UNC45A]] | +0.63 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[TMEM160]] | +0.63 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[MEA1]] | +0.63 | +0.53 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCNMB3]] | -0.60 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[RIPK2-DT]] | -0.58 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[SPTY2D1OS]] | -0.58 | -0.41 / -0.34 | both halves | 1e-04 |  |
| [[ARRDC3-AS1]] | -0.57 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[NEB]] | -0.57 | -0.48 / -0.26 | both halves | 4e-04 |  |
| [[DPH5-DT]] | -0.57 | -0.43 / -0.37 | both halves | 8e-05 |  |
| [[SLC2A9]] | -0.57 | -0.42 / -0.39 | both halves | 5e-05 |  |
| [[RFX3-DT]] | -0.57 | -0.45 / -0.28 | both halves | 3e-04 |  |
| [[CIBAR1-DT]] | -0.56 | -0.49 / -0.24 | both halves | 5e-04 |  |
| [[LINC00486]] | -0.56 | -0.48 / -0.36 | both halves | 9e-05 |  |
| [[ANKRD18B]] | -0.56 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[LINC02516]] | -0.56 | -0.45 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ALDOC]] | B | ALDOC activity lowers AKR7A2's level | lines that do not express ALDOC (7) vs lines expressing it (43) | 1.61× higher at baseline in the lines without ALDOC | 0.084 | ⚠ within organs, on part of the lines |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.595). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (9.9, -14.1); signed map (-36.0, 18.3). **Vector** length 67.4, 13.6% of its response variance represented; |z| ≥ 3 in 714 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +4.4 | +8.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +3.8 | +8.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +3.7 | +5.8 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.0 | +2.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.7 | +4.3 |
|  | [[Sinomenine (drug)]] 0.5 µM |  | +1.6 | +1.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.5 | +2.6 |
|  | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM |  | +1.5 | +1.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.5 | -4.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.3 | -10.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.0 | -5.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | -1.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.4 | -3.1 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -2.1 | -2.0 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -1.9 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | aldo-keto reductase family 7 member A2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.13 — chr1:19,303,965-19,312,144 (-) |
| Ensembl biotype | protein_coding |
| Also known as | AFAR |
| Gene groups (HGNC) | Aldo-keto reductases |
| Reactome | 2 pathways, smallest: Aflatoxin activation and detoxification; Biological oxidations |
| Matched by | ensembl_id |

**Function**, from UniProt [O43488](https://www.uniprot.org/uniprotkb/O43488) (Aflatoxin B1 aldehyde reductase member 2):

> Catalyzes the NADPH-dependent reduction of succinic semialdehyde to gamma-hydroxybutyrate. May have an important role in producing the neuromodulator gamma-hydroxybutyrate (GHB). Has broad substrate specificity. Has NADPH-dependent aldehyde reductase activity towards 2-carboxybenzaldehyde, 2-nitrobenzaldehyde and pyridine-2-aldehyde (in vitro). Can reduce 1,2-naphthoquinone and 9,10-phenanthrenequinone (in vitro). Can reduce the dialdehyde protein-binding form of aflatoxin B1 (AFB1) to the …

**Summary**, from NCBI Gene [8574](https://www.ncbi.nlm.nih.gov/gene/8574):

> The protein encoded by this gene belongs to the aldo/keto reductase (AKR) superfamily and AKR7 family, which are involved in the detoxification of aldehydes and ketones. The AKR7 family consists of 3 genes that are present in a cluster on the p arm of chromosome 1. This protein, thought to be localized in the golgi, catalyzes the NADPH-dependent reduction of succinic semialdehyde to the endogenous neuromodulator, gamma-hydroxybutyrate. It may also function as a detoxication enzyme in the …

**Accessions** — [HGNC:389](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:389) · Entrez [8574](https://www.ncbi.nlm.nih.gov/gene/8574) · UniProt [O43488](https://www.uniprot.org/uniprotkb/O43488) · Ensembl [ENSG00000053371](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000053371)

## Data

Gene col 592: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 592); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 592, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 592]; `tensor/DDL_lfc|DDL_z.npy` [592]; `embed/gene_vectors.npy` [592]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 592 or target_col == 592). Every well: [[AKR7A2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AKR7A2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
