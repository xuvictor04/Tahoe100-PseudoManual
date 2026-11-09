---
symbol: "PDE8B"
type: "gene"
col: 3438
ensembl_id: "ENSG00000113231"
name: "phosphodiesterase 8B"
location: "5q13.3"
module: 75
arm: "+"
pooled_cpm: 6.07
n_lines_expressing: 49
n_dd_up: 30
n_dd_down: 11
n_dd_up_clean: 21
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/075"]
generated_by: "tahoemap"
---

# PDE8B

*phosphodiesterase 8B* — 5q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.33× (z +17.9, q 0e+00, up in 6 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.20× (z +14.2, q 3e-43, up in 25 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.440× (z -10.4, q 1e-22, down in 26 of 44 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NXPH1]] (+0.69, fdr 7e-06), [[TRPM3]] (+0.63, fdr 1e-05), [[LINC02269]] (+0.62, fdr 1e-05); moves opposite to [[STUB1]] (-0.52, fdr 4e-04), [[CCM2]] (-0.50, fdr 7e-05), [[SIVA1]] (-0.49, fdr 2e-04).
> It is in [[Module 075]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SCARA5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3438.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.33×** | +17.9 | 0e+00 | 6/8 (HOP62, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.03×** | +17.7 | 0e+00 | 16/19 (HOP62, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.20×** | +14.2 | 3e-43 | 25/38 (PANC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.84×** | +12.3 | 1e-32 | 8/12 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.85×** | +11.1 | 2e-26 | 25/45 (PANC-1, SW1417, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.74×** | +9.9 | 3e-21 | 20/46 (A549, NCI-H23, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~24% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.86×** | +7.9 | 2e-13 | 23/42 (HOP62, J82, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.80×** | +7.5 | 5e-12 | 21/46 (HEC-1-A, H4, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.51×** | +7.5 | 5e-12 | 19/38 (BT-474, HCT15, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.66×** | +6.5 | 5e-09 | 16/44 (SK-MEL-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.57×** | +5.6 | 1e-06 | 14/41 (NCI-H23, SW480, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.51×** | +5.3 | 6e-06 | 13/42 (HEC-1-A, A549, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +4.2 | 1e-03 | 3/21 (NCI-H2347, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.39×** | +4.2 | 0.001 | 17/44 (HEC-1-A, NCI-H23, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.32×** | +4.2 | 0.001 | 4/44 (NCI-H23, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Afatinib (drug)]] 5 µM |  | **1.40×** | +3.8 | 0.004 | 5/45 (SW480, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.6 | 0.011 | 7/46 (A-172, LOX-IMVI, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.31×** | +3.4 | 0.016 | 11/43 (NCI-H2030, HEC-1-A, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +3.3 | 0.024 | 9/34 (HEC-1-A, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3438.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.440×** | -10.4 | 1e-22 | 26/44 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.456×** | -10.0 | 6e-21 | 28/46 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.491×** | -9.0 | 3e-17 | 25/44 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.561×** | -7.3 | 3e-11 | 19/36 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.596×** | -6.6 | 6e-09 | 22/46 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.607×** | -6.3 | 3e-08 | 16/45 (NCI-H460, A549, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.628×** | -5.7 | 1e-06 | 12/41 (NCI-H460, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.680×** | -4.9 | 8e-05 | 17/38 (SHP-77, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.707×** | -4.4 | 7e-04 | 14/46 (NCI-H460, C-33 A, …) | all doses, stronger at high dose |  |
| [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | **0.737×** | -3.9 | 0.006 | 4/46 (NCI-H661, KATO III, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.763×** | -3.4 | 0.034 | 9/43 (SNU-1, NCI-H460, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3438. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 35.3 | 0 | 9 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0894× (z -15.9) |
| [[LoVo (line)]] | wt | 20.4 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.123× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.143× (z -11.6) |
| [[HOP62 (line)]] | alt | 2.92 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 20.0× (z +10.4) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 8.56 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 9.69 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.176× (z -9.0) ⚠ cell-cycle shift, explains ~42% of this change |
| [[NCI-H1573 (line)]] | alt | 4.78 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0799× (z -8.8) |
| [[SHP-77 (line)]] | alt | 7.70 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0586× (z -11.1) |
| [[SW 900 (line)]] | alt | 3.17 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 50.7× (z +10.4) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 3.46 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.60 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.88 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 39.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.93 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.44 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.51 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.07 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.30 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.00 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3438), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NXPH1]] | +0.69 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[TRPM3]] | +0.63 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[LINC02269]] | +0.62 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[LINC01257]] | +0.60 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[LINC02755]] | +0.60 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[GREB1]] | +0.60 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[DLGAP1]] | +0.59 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[ARHGEF37]] | +0.59 | +0.57 / +0.41 | both halves | 4e-05 |  |
| [[LINC00534]] | +0.59 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[PCDH15]] | +0.59 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[PPEF1]] | +0.58 | +0.61 / +0.45 | both halves | 3e-05 |  |
| [[LAMB4]] | +0.57 | +0.45 / +0.49 | both halves | 3e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STUB1]] | -0.52 | -0.44 / -0.25 | both halves | 4e-04 |  |
| [[CCM2]] | -0.50 | -0.46 / -0.38 | both halves | 7e-05 |  |
| [[SIVA1]] | -0.49 | -0.50 / -0.30 | both halves | 2e-04 |  |
| [[TRAPPC4]] | -0.48 | -0.31 / -0.38 | both halves | 2e-04 |  |
| [[HAUS3]] | -0.48 | -0.27 / -0.36 | both halves | 3e-04 |  |
| [[GGA1]] | -0.48 | -0.38 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SCARA5]] | B | SCARA5 activity raises PDE8B's level | lines that do not express SCARA5 (43) vs lines expressing it (7) | 2.00× lower at baseline in the lines without SCARA5 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000260364, GSG1L2, SLC15A5 |
| [[SMO]] | B | SMO activity raises PDE8B's level | lines that do not express SMO (17) vs lines expressing it (33) | 1.68× lower at baseline in the lines without SMO | 0.091 | ⚠ within organs, on part of the lines; also absent: RADIL, DUSP9, APBA2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 075]]; 60 genes; every member is in the + arm (projection on the module's main direction 0.563). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (19.7, 24.8); signed map (36.1, 11.0). **Vector** length 72.0, 11.7% of its response variance represented; |z| ≥ 3 in 1,082 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.4 | +12.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.3 | +17.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.2 | +17.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +14.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.3 | +11.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.9 | +4.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +7.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.9 | +1.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.7 | +0.7 |
| fall | [[Belinostat (drug)]] 5 µM |  | -3.3 | -6.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.8 | -9.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -2.7 | -2.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | -2.4 | -3.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.3 | -4.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -1.0 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.2 | -0.4 |
|  | [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | -1.2 | -3.9 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | -1.2 | -0.7 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.1 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | phosphodiesterase 8B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q13.3 — chr5:77,210,449-77,428,256 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Phosphodiesterases; PAS domain containing |
| Reactome | 3 pathways, smallest: G alpha (s) signalling events; GPCR downstream signalling; Signaling by GPCR |
| Matched by | ensembl_id |

**Function**, from UniProt [O95263](https://www.uniprot.org/uniprotkb/O95263) (High affinity cAMP-specific and IBMX-insensitive 3',5'-cyclic phosphodiesterase 8B):

> Hydrolyzes the second messenger cAMP, which is a key regulator of many important physiological processes. May be involved in specific signaling in the thyroid gland.

**Summary**, from NCBI Gene [8622](https://www.ncbi.nlm.nih.gov/gene/8622):

> The protein encoded by this gene is a cyclic nucleotide phosphodiesterase (PDE) that catalyzes the hydrolysis of the second messenger cAMP. The encoded protein, which does not hydrolyze cGMP, is resistant to several PDE inhibitors. Defects in this gene are a cause of autosomal dominant striatal degeneration (ADSD). Several transcript variants encoding different isoforms have been found for this gene.[provided by RefSeq, Jul 2010]

**Accessions** — [HGNC:8794](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8794) · Entrez [8622](https://www.ncbi.nlm.nih.gov/gene/8622) · UniProt [O95263](https://www.uniprot.org/uniprotkb/O95263) · Ensembl [ENSG00000113231](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113231)

## Data

Gene col 3438: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3438); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3438, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3438]; `tensor/DDL_lfc|DDL_z.npy` [3438]; `embed/gene_vectors.npy` [3438]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3438 or target_col == 3438). Every well: [[PDE8B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDE8B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
