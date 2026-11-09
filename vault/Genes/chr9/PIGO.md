---
symbol: "PIGO"
type: "gene"
col: 9101
ensembl_id: "ENSG00000165282"
name: "phosphatidylinositol glycan anchor biosynthesis class O"
location: "9p13.3"
module: 96
arm: "+"
pooled_cpm: 7.4
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 22
n_dd_up_clean: 1
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/096"]
generated_by: "tahoemap"
---

# PIGO

*phosphatidylinositol glycan anchor biosynthesis class O* — 9p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.07× (z +10.1, q 5e-21, up in 11 of 13 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 1.34× (z +4.0, q 0.006, up in 11 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.446× (z -16.5, q 0e+00, down in 35 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARAF]] (+0.81, fdr 7e-06), [[PRRC2A]] (+0.75, fdr 7e-06), [[BACE1-AS]] (+0.74, fdr 7e-06); moves opposite to [[OST4]] (-0.64, fdr 1e-05), [[TBC1D20]] (-0.64, fdr 1e-05), [[QPCTL]] (-0.63, fdr 2e-05).
> It is in [[Module 096]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9101.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.07×** | +10.1 | 5e-21 | 11/13 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.93×** | +9.5 | 6e-19 | 22/28 (CFPAC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.94×** | +8.9 | 2e-16 | 16/21 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.44×** | +5.3 | 2e-05 | 12/35 (NCI-H460, NCI-H1792, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.34×** | +4.0 | 0.006 | 11/44 (LS 180, PANC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.2 | 0.12 | 9/41 (A498, RKO, …) | inconsistent across doses | composition shift |
| [[Busulfan (drug)]] 0.05 µM |  | 1.24× | +3.1 | 0.16 | 1/46 (Hs 766T) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9101.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.446×** | -16.5 | 0e+00 | 35/43 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.506×** | -9.9 | 2e-20 | 27/47 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.525×** | -9.0 | 6e-17 | 26/39 (SW480, H4, …) | top dose only | cell-cycle shift (explains ~15% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.583×** | -7.8 | 9e-13 | 22/47 (SW480, SNU-423, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.604×** | -7.3 | 3e-11 | 23/45 (BT-474, SK-MEL-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.634×** | -6.6 | 4e-09 | 18/47 (AsPC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.655×** | -5.9 | 3e-07 | 23/43 (NCI-H2030, SNU-423, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.672×** | -5.7 | 6e-07 | 18/45 (SW480, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.682×** | -5.5 | 2e-06 | 19/42 (SW1417, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.688×** | -5.4 | 3e-06 | 15/45 (BT-474, SW48, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.698×** | -5.2 | 1e-05 | 18/46 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.794×** | -4.7 | 1e-04 | 15/47 (NCI-H460, SK-MEL-2, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.731×** | -4.5 | 2e-04 | 12/44 (SNU-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.549×** | -4.5 | 2e-04 | 6/45 (PANC-1, RPMI-7951, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.742×** | -4.3 | 6e-04 | 16/47 (SW480, BT-474, …) | all doses, flat | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.830×** | -3.8 | 0.004 | 9/47 (BT-474, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.783×** | -3.5 | 0.012 | 14/44 (BT-474, C32, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.844× | -3.5 | 0.013 | 11/45 (PANC-1, NCI-H23, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9101. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 5.09 | 0 | 4 (1 ⚠) | — | [[Daptomycin (drug)]] 0.5 µM 0.0716× (z -11.8) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.194× (z -10.3) |
| [[BT-474 (line)]] | alt | 37.0 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.242× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.404× (z -9.5) |
| [[PANC-1 (line)]] | alt | 13.7 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -10.2) |
| [[C-33 A (line)]] | alt | 9.16 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0866× (z -9.5) |
| [[H4 (line)]] | wt | 10.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.182× (z -8.8) |
| [[HCT15 (line)]] | alt | 10.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.143× (z -10.5) |
| [[KATO III (line)]] | alt | 10.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -9.1) |
| [[LS 180 (line)]] | wt | 7.37 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.230× (z -9.9) |
| [[MIA PaCa-2 (line)]] | alt | 4.14 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.170× (z -9.3) |
| [[NCI-H460 (line)]] | wt | 6.59 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.218× (z -13.5) |
| [[RKO (line)]] | wt | 8.11 | 0 | 1 | — | [[Canagliflozin (drug)]] 5 µM 0.0705× (z -10.0) |
| [[SK-MEL-2 (line)]] | alt | 5.89 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0924× (z -9.0) |
| [[SW1417 (line)]] | alt | 7.61 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.176× (z -11.3) |
| [[SW480 (line)]] | alt | 8.24 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.188× (z -14.8) |
| [[A-172 (line)]] | wt | 5.41 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.87 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.50 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.82 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.38 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.36 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.43 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.77 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.33 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.00 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.42 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.44 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9101), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARAF]] | +0.81 | +0.63 / +0.83 | both halves | 7e-06 |  |
| [[PRRC2A]] | +0.75 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[BACE1-AS]] | +0.74 | +0.63 / +0.72 | both halves | 7e-06 |  |
| [[ATP13A1]] | +0.74 | +0.76 / +0.69 | both halves | 7e-06 |  |
| [[ZNF512B]] | +0.72 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[SAYSD1]] | +0.72 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[CHTOP]] | +0.72 | +0.58 / +0.75 | both halves | 7e-06 |  |
| [[CELSR3]] | +0.70 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[OCRL]] | +0.70 | +0.53 / +0.73 | both halves | 1e-05 |  |
| [[EWSR1]] | +0.70 | +0.52 / +0.74 | both halves | 1e-05 |  |
| [[WIZ]] | +0.70 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[N6AMT1]] | +0.69 | +0.57 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OST4]] | -0.64 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[TBC1D20]] | -0.64 | -0.51 / -0.67 | both halves | 1e-05 |  |
| [[QPCTL]] | -0.63 | -0.47 / -0.64 | both halves | 2e-05 |  |
| [[TPTEP2-CSNK1E]] | -0.63 | -0.44 / -0.66 | both halves | 3e-05 |  |
| [[ATP5MK]] | -0.62 | -0.59 / -0.57 | both halves | 9e-06 |  |
| [[SEC61G]] | -0.62 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[COMMD6]] | -0.62 | -0.57 / -0.58 | both halves | 9e-06 |  |
| [[KLHL7]] | -0.62 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[UBL5]] | -0.61 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[RAB6A]] | -0.61 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[RPS29]] | -0.61 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[UBA52]] | -0.61 | -0.51 / -0.58 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PIGO's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 096]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.834). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-18.3, -2.4); signed map (0.3, -33.7). **Vector** length 65.3, 9.65% of its response variance represented; |z| ≥ 3 in 1,012 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.2 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.8 | +9.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +8.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.0 | +3.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | +1.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.2 | +4.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +1.8 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.5 | +2.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | -0.1 |
|  | [[Folic acid (drug)]] 5 µM |  | +1.4 | +0.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.6 | -16.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.5 | -9.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -2.2 | -2.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.1 | -5.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.0 | -7.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.8 | -4.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.7 | -5.9 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.5 | -1.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.3 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | phosphatidylinositol glycan anchor biosynthesis class O |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p13.3 — chr9:35,087,237-35,096,619 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp434M222, FLJ00135, PIG-O |
| Gene groups (HGNC) | Phosphatidylinositol glycan anchor biosynthesis |
| Reactome | 2 pathways, smallest: Synthesis of glycosylphosphatidylinositol (GPI); Post-translational modification: synthesis of GPI-anchored proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TEQ8](https://www.uniprot.org/uniprotkb/Q8TEQ8) (GPI ethanolamine phosphate transferase 3, catalytic subunit):

> Catalytic subunit of the ethanolamine phosphate transferase 3 complex that transfers an ethanolamine phosphate (EtNP) from a phosphatidylethanolamine (PE) to the 6-OH position of the third alpha-1,2-linked mannose of the a 2-acyl-6-[alpha-D-mannosyl-(1->2)-alpha-D-mannosyl-(1->6)-2-phosphoethanolamine-alpha-D-mannosyl-(1->4)-alpha-D-glucosaminyl]-1-(1-radyl,2-acyl-sn-glycero-3-phospho)-1D-myo-inositol (also termed H6) intermediate to generate a a …

**Summary**, from NCBI Gene [84720](https://www.ncbi.nlm.nih.gov/gene/84720):

> This gene encodes a protein that is involved in glycosylphosphatidylinositol (GPI)-anchor biosynthesis. The GPI-anchor is a glycolipid which contains three mannose molecules in its core backbone. The GPI-anchor is found on many blood cells and serves to anchor proteins to the cell surface. This protein is involved in the transfer of ethanolaminephosphate (EtNP) to the third mannose in GPI. At least three alternatively spliced transcripts encoding two distinct isoforms have been found for this …

**Accessions** — [HGNC:23215](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23215) · Entrez [84720](https://www.ncbi.nlm.nih.gov/gene/84720) · UniProt [Q8TEQ8](https://www.uniprot.org/uniprotkb/Q8TEQ8) · Ensembl [ENSG00000165282](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165282)

## Data

Gene col 9101: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9101); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9101, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9101]; `tensor/DDL_lfc|DDL_z.npy` [9101]; `embed/gene_vectors.npy` [9101]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9101 or target_col == 9101). Every well: [[PIGO — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIGO.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
