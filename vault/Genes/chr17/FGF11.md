---
symbol: "FGF11"
type: "gene"
col: 8464
ensembl_id: "ENSG00000161958"
name: "fibroblast growth factor 11"
location: "17p13.1"
module: 103
arm: "+"
pooled_cpm: 9.03
n_lines_expressing: 41
n_dd_up: 5
n_dd_down: 22
n_dd_up_clean: 3
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 0
direction_downstream: 3
tags: ["gene", "module/103"]
generated_by: "tahoemap"
---

# FGF11

*fibroblast growth factor 11* — 17p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.80× (z +7.9, q 2e-12, up in 3 of 13 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.31× (z +5.3, q 3e-05, up in 13 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (6 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.370× (z -13.3, q 8e-38, down in 29 of 38 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RUNDC3A-AS1]] (+0.55, fdr 1e-04), [[RSPH9]] (+0.52, fdr 3e-04), [[LZTS2]] (+0.51, fdr 4e-05); moves opposite to [[ZNHIT6]] (-0.47, fdr 4e-05), [[STXBP6]] (-0.46, fdr 1e-04), [[FAF1]] (-0.46, fdr 2e-04).
> It is in [[Module 103]], a single-armed module (glycolysis).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 3 go from it, the strongest it → [[TMEM63B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8464.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.80×** | +7.9 | 2e-12 | 3/13 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +5.3 | 3e-05 | 13/32 (A549, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.41×** | +4.6 | 7e-04 | 13/36 (NCI-H23, SW 900, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.33×** | +4.0 | 0.010 | 6/29 (PANC-1, SW 900, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.47×** | +3.9 | 0.013 | 4/23 (A549, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.17× | +3.1 | 0.16 | 8/38 (NCI-H23, A549, …) | inconsistent across doses | position effect removed |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 1.17× | +3.1 | 0.16 | 4/38 (SW 900, A498, …) | top dose only |  |
| [[Cabozantinib (S-malate) (drug)]] 0.5 µM |  | 1.24× | +3.1 | 0.16 | 2/37 (NCI-H2347, SW48) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8464.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.370×** | -13.3 | 8e-38 | 29/38 (NCI-H1792, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.517×** | -13.0 | 3e-36 | 27/35 (NCI-H1573, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.416×** | -12.2 | 4e-32 | 25/36 (NCI-H1573, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.448×** | -11.2 | 5e-27 | 26/38 (NCI-H1792, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.476×** | -10.4 | 4e-23 | 26/38 (NCI-H23, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.484×** | -10.1 | 3e-22 | 27/38 (NCI-H23, SW480, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.604×** | -7.0 | 2e-10 | 16/37 (A549, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.653×** | -5.9 | 2e-07 | 16/38 (NCI-H1792, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.453×** | -5.8 | 5e-07 | 19/36 (NCI-H1573, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.673×** | -5.5 | 2e-06 | 15/32 (J82, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.686×** | -5.2 | 8e-06 | 15/38 (AsPC-1, NCI-H2030, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.697×** | -5.0 | 2e-05 | 12/37 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.524×** | -4.7 | 1e-04 | 17/36 (NCI-H1792, AsPC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | **0.789×** | -4.7 | 1e-04 | 10/37 (A498, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **0.715×** | -4.5 | 3e-04 | 14/28 (SW 900, NCI-H1792, …) | top dose only | position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **0.543×** | -4.5 | 3e-04 | 14/35 (NCI-H2030, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.732×** | -4.3 | 5e-04 | 13/38 (NCI-H1573, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **0.729×** | -4.2 | 7e-04 | 13/36 (NCI-H1573, HCT15, …) | rises with dose |  |
| [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | **0.783×** | -3.4 | 0.019 | 5/37 (Panc 03.27, A549, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8464. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 49.9 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -15.6) |
| [[NCI-H1573 (line)]] | alt | 28.4 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0449× (z -22.9) |
| [[NCI-H1792 (line)]] | alt | 21.0 | 0 | 7 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0572× (z -16.9) |
| [[AsPC-1 (line)]] | alt | 11.7 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -13.5) |
| [[NCI-H23 (line)]] | alt | 51.7 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -22.0) |
| [[SW480 (line)]] | alt | 9.16 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -11.5) |
| [[PANC-1 (line)]] | alt | 11.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.193× (z -12.1) |
| [[J82 (line)]] | alt | 9.29 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -13.5) |
| [[A549 (line)]] | wt | 3.49 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0384× (z -10.6) |
| [[NCI-H2030 (line)]] | alt | 34.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -12.4) |
| [[NCI-H460 (line)]] | wt | 4.44 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.123× (z -10.0) |
| [[A-172 (line)]] | wt | 0.946 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 6.04 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.64 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.97 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.702 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.11 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.72 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.17 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.14 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.12 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.556 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.44 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.666 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.61 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8464), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 5 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RUNDC3A-AS1]] | +0.55 | +0.52 / +0.35 | both halves | 1e-04 |  |
| [[RSPH9]] | +0.52 | +0.28 / +0.57 | both halves | 3e-04 |  |
| [[LZTS2]] | +0.51 | +0.41 / +0.61 | both halves | 4e-05 |  |
| [[SLC41A1]] | +0.51 | +0.37 / +0.47 | both halves | 9e-05 |  |
| [[SUOX]] | +0.50 | +0.34 / +0.48 | both halves | 1e-04 |  |
| [[EOLA1]] | +0.50 | +0.38 / +0.57 | both halves | 6e-05 |  |
| [[ABCB6]] | +0.50 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[NFATC4]] | +0.49 | +0.40 / +0.51 | both halves | 5e-05 |  |
| [[APH1B]] | +0.49 | +0.46 / +0.31 | both halves | 2e-04 |  |
| [[BCL2L2]] | +0.48 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[PACRG]] | +0.47 | +0.33 / +0.40 | both halves | 1e-04 |  |
| [[SPAG4]] | +0.47 | +0.46 / +0.49 | both halves | 3e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNHIT6]] | -0.47 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[STXBP6]] | -0.46 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[FAF1]] | -0.46 | -0.29 / -0.57 | both halves | 2e-04 |  |
| [[FARSB]] | -0.44 | -0.34 / -0.53 | both halves | 1e-04 |  |
| [[PYGB]] | -0.43 | -0.32 / -0.38 | both halves | 2e-04 |  |
| [[COA1]] | -0.43 | -0.25 / -0.50 | both halves | 4e-04 |  |
| [[SHLD2]] | -0.42 | -0.36 / -0.35 | both halves | 1e-04 |  |
| [[RBFA]] | -0.41 | -0.38 / -0.39 | both halves | 7e-05 |  |
| [[FAM172A]] | -0.41 | -0.33 / -0.31 | both halves | 2e-04 |  |
| [[DDX10]] | -0.41 | -0.31 / -0.47 | both halves | 2e-04 |  |
| [[NOL10]] | -0.40 | -0.35 / -0.33 | both halves | 1e-04 |  |
| [[WDR35]] | -0.40 | -0.32 / -0.43 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM63B]] | B | FGF11 activity lowers TMEM63B's level | lines that do not express FGF11 (9) vs lines expressing it (41) | 1.53× higher at baseline in the lines without FGF11 | 0.074 | ⚠ within organs, on part of the lines; also absent: C9orf64, CYB5A |
| [[SUOX]] | B | FGF11 activity raises SUOX's level | lines that do not express FGF11 (9) vs lines expressing it (41) | 1.26× lower at baseline in the lines without FGF11 | 0.089 | ⚠ within organs, on part of the lines; also absent: C9orf64, CYB5A |
| [[AJM1]] | B | FGF11 activity lowers AJM1's level | lines that do not express FGF11 (9) vs lines expressing it (41) | 1.38× higher at baseline in the lines without FGF11 | 0.096 | ⚠ within organs, on part of the lines; also absent: C9orf64, CYB5A |

## Where it sits

- **Module**: [[Module 103]] — glycolysis; 45 genes; every member is in the + arm (projection on the module's main direction 0.390). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.5, -31.4); signed map (2.2, 13.2). **Vector** length 57.9, 9.10% of its response variance represented; |z| ≥ 3 in 825 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | -0.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +1.9 | +4.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.7 | -1.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.6 | +4.6 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.4 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | -2.3 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.3 | +2.2 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -2.4 | -13.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.7 | -4.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.5 | -12.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -1.2 | -13.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.2 | -5.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.2 | -2.4 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -1.1 | -2.0 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -1.0 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | fibroblast growth factor 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.1 — chr17:7,438,273-7,444,937 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FHF3, FLJ16061, MGC45269, MGC102953 |
| Gene groups (HGNC) | Fibroblast growth factor family |
| Reactome | 3 pathways, smallest: Phase 0 - rapid depolarisation; Cardiac conduction; Muscle contraction |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92914](https://www.uniprot.org/uniprotkb/Q92914) (Fibroblast growth factor 11):

> Probably involved in nervous system development and function.

**Summary**, from NCBI Gene [2256](https://www.ncbi.nlm.nih.gov/gene/2256):

> The protein encoded by this gene is a member of the fibroblast growth factor (FGF) family. FGF family members possess broad mitogenic and cell survival activities, and are involved in a variety of biological processes, including embryonic development, cell growth, morphogenesis, tissue repair, tumor growth and invasion. The function of this gene has not yet been determined. The expression pattern of the mouse homolog implies a role in nervous system development. Alternative splicing results in …

**Accessions** — [HGNC:3667](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3667) · Entrez [2256](https://www.ncbi.nlm.nih.gov/gene/2256) · UniProt [Q92914](https://www.uniprot.org/uniprotkb/Q92914) · Ensembl [ENSG00000161958](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161958)

## Data

Gene col 8464: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8464); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8464, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8464]; `tensor/DDL_lfc|DDL_z.npy` [8464]; `embed/gene_vectors.npy` [8464]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8464 or target_col == 8464). Every well: [[FGF11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FGF11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
