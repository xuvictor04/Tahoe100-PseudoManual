---
symbol: "IMPDH2"
type: "gene"
col: 10889
ensembl_id: "ENSG00000178035"
name: "inosine monophosphate dehydrogenase 2"
location: "3p21.31"
module: 35
arm: "-"
pooled_cpm: 55.65
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 4
n_dd_up_clean: 7
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# IMPDH2

*inosine monophosphate dehydrogenase 2* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.15× (z +10.7, q 1e-23, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 0.463× (z -5.6, q 1e-05, down in 32 of 49 measured lines).
> Its strongest partners by |cos| (75 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 25 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EIF4A2]] (+0.63, fdr 2e-05), [[EEF2]] (+0.59, fdr 3e-05), [[IL17RD]] (+0.59, fdr 3e-05); moves opposite to [[DNAJB14]] (-0.57, fdr 5e-05), [[AP5M1]] (-0.55, fdr 2e-04), [[AP4S1]] (-0.55, fdr 2e-04).
> It sits in the **-** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[EPS15-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 9 with an alert ⚠; shown: the 15 strongest. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10889.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.15×** | +10.7 | 1e-23 | 47/48 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.04×** | +9.9 | 2e-20 | 48/48 (J82, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.94×** | +9.2 | 7e-18 | 40/46 (HT-29, NCI-H23, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.98×** | +9.1 | 1e-17 | 37/42 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.77×** | +8.0 | 2e-13 | 44/48 (J82, SW480, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **1.58×** | +6.4 | 2e-08 | 40/46 (HOP62, PANC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +5.7 | 9e-07 | 34/47 (MIA PaCa-2, KATO III, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.56×** | +5.2 | 1e-05 | 30/45 (NCI-H2347, HT-29, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.39×** | +4.5 | 4e-04 | 35/48 (KATO III, HT-29, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.37×** | +4.4 | 6e-04 | 29/48 (J82, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.72×** | +3.9 | 0.004 | 28/48 (KATO III, SK-MEL-2, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +3.8 | 0.008 | 24/48 (A498, RKO, …) | rises with dose | position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.30×** | +3.6 | 0.013 | 25/48 (NCI-H23, Panc 03.27, …) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.2 | 0.049 | 19/48 (NCI-H2347, CFPAC-1, …) | top dose only | low cells (technical?) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.44×** | +3.2 | 0.055 | 16/48 (PANC-1, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10889.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.463×** | -5.6 | 1e-05 | 32/49 (SW480, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.476×** | -5.4 | 2e-05 | 37/48 (A-427, NCI-H460, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.798×** | -4.4 | 0.002 | 27/48 (NCI-H2030, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.769×** | -3.4 | 0.082 | 23/47 (SW480, BT-474, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | 0.777× | -3.3 | 0.11 | 24/48 (LOX-IMVI, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.798× | -3.1 | 0.16 | 21/48 (C-33 A, SW 1088, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10889. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 55.7 | 3 (3 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.28× (z +9.8) ⚠ toxic | — |
| [[NCI-H460 (line)]] | wt | 68.4 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.52× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -11.3) |
| [[SW480 (line)]] | alt | 75.7 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.44× (z +9.7) | — |
| [[A-427 (line)]] | wt | 94.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.557× (z -9.1) |
| [[C-33 A (line)]] | alt | 93.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.209× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.484× (z -9.1) |
| [[J82 (line)]] | alt | 35.7 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.71× (z +8.8) | — |
| [[Panc 03.27 (line)]] | alt | 54.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.11× (z +9.6) | — |
| [[A-172 (line)]] | wt | 30.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.53× (z +9.3) | — |
| [[A549 (line)]] | wt | 53.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[CHP-212 (line)]] | wt | 68.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -10.0) |
| [[Hs 766T (line)]] | wt | 50.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.05× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[HT-29 (line)]] | alt | 38.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.86× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[KATO III (line)]] | alt | 39.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.75× (z +8.9) | — |
| [[LOX-IMVI (line)]] | wt | 60.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.497× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 80.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -11.7) |
| [[NCI-H23 (line)]] | alt | 51.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[NCI-H2347 (line)]] | alt | 77.6 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +10.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[RKO (line)]] | wt | 55.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.470× (z -9.1) |
| [[SK-MEL-2 (line)]] | alt | 73.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -12.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 117 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.460× (z -8.9) |
| [[A498 (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 35.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 48.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 62.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 57.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 41.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 56.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 91.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 64.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 64.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 57.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 65.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 85.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10889), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4A2]] | +0.63 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[EEF2]] | +0.59 | +0.69 / +0.46 | both halves | 3e-05 | STRING 426 |
| [[IL17RD]] | +0.59 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[RSAD1]] | +0.58 | +0.35 / +0.51 | both halves | 1e-04 |  |
| [[NPM3]] | +0.57 | +0.51 / +0.37 | both halves | 8e-05 |  |
| [[ARRB2]] | +0.56 | +0.34 / +0.49 | both halves | 1e-04 |  |
| [[NOB1]] | +0.54 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[PPP1CC]] | +0.54 | +0.35 / +0.50 | both halves | 1e-04 |  |
| [[SLC46A1]] | +0.54 | +0.38 / +0.52 | both halves | 6e-05 |  |
| [[MFSD10]] | +0.53 | +0.52 / +0.18 | ⚠ one half (not replicated) | 0.001 |  |
| [[SLX9]] | +0.53 | +0.37 / +0.39 | both halves | 9e-05 |  |
| [[GALNT11]] | +0.52 | +0.35 / +0.51 | both halves | 1e-04 |  |
| [[TTLL12]] | +0.52 | +0.48 / +0.29 | both halves | 2e-04 |  |

## Genes that move opposite

*49 of its nearest partners move opposite, 19 of them with an alert (⚠; 19 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJB14]] | -0.57 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[AP5M1]] | -0.55 | -0.34 / -0.31 | both halves | 2e-04 |  |
| [[AP4S1]] | -0.55 | -0.32 / -0.38 | both halves | 2e-04 |  |
| [[EPS15-AS1]] | -0.54 | -0.31 / -0.35 | both halves | 2e-04 |  |
| [[SMG1-DT]] | -0.52 | -0.38 / -0.37 | both halves | 9e-05 |  |
| [[NAA60]] | -0.52 | -0.47 / -0.36 | both halves | 9e-05 |  |
| [[ATXN7L3-AS1]] | -0.51 | -0.32 / -0.33 | both halves | 1e-04 |  |
| [[ANXA2R-AS1]] | -0.50 | -0.20 / -0.27 | ⚠ not reproduced | 8e-04 |  |
| [[FBXL19-AS1]] | -0.49 | -0.26 / -0.28 | both halves | 4e-04 |  |
| [[NINJ2]] | -0.49 | -0.29 / -0.05 | ⚠ not reproduced | 0.005 |  |
| [[ANKHD1-DT]] | -0.49 | -0.29 / -0.11 | ⚠ not reproduced | 0.002 |  |
| [[PNISR-AS1]] | -0.49 | -0.21 / -0.28 | both halves | 6e-04 |  |
| [[ANXA2R-OT1]] | -0.49 | -0.23 / -0.35 | both halves | 5e-04 |  |
| [[CCNO-DT]] | -0.48 | -0.28 / -0.29 | both halves | 3e-04 |  |
| [[HFE]] | -0.48 | -0.26 / -0.35 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPS15-AS1]] | B | EPS15-AS1 activity lowers IMPDH2's level | lines that do not express EPS15-AS1 (12) vs lines expressing it (38) | 1.29× higher at baseline in the lines without EPS15-AS1 | 0.050 | ⚠ within organs, on part of the lines; also absent: RND1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **-** arm (projection on the module's main direction -0.477). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (9.5, -5.7); signed map (-38.0, -20.5). **Vector** length 92.4, 25.7% of its response variance represented; |z| ≥ 3 in 878 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.7 | +4.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.8 | +10.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.8 | +9.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +3.8 | +8.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +3.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.1 | +3.9 |
|  | [[EX229 (drug)]] 5 µM |  | +2.5 | +1.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.1 | +1.9 |
|  | [[EX229 (drug)]] 0.05 µM |  | +1.9 | +2.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.0 | -0.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.2 | -5.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.0 | -1.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.8 | -1.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.6 | -4.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.9 | -5.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.0 | -0.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.6 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | inosine monophosphate dehydrogenase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:49,024,325-49,029,447 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Inosine monophosphate dehydrogenase family |
| Hallmark sets | DNA_REPAIR, MYC_TARGETS_V1 |
| Reactome | 10 pathways, smallest: Purine ribonucleoside monophosphate biosynthesis; Nucleotide biosynthesis; Azathioprine ADME |
| Matched by | ensembl_id |

**Function**, from UniProt [P12268](https://www.uniprot.org/uniprotkb/P12268) (Inosine-5'-monophosphate dehydrogenase 2):

> Catalyzes the conversion of inosine 5'-phosphate (IMP) to xanthosine 5'-phosphate (XMP), the first committed and rate-limiting step in the de novo synthesis of guanine nucleotides, and therefore plays an important role in the regulation of cell growth. Could also have a single-stranded nucleic acid-binding activity and could play a role in RNA and/or DNA metabolism. It may also have a role in the development of malignancy and the growth progression of some tumors.

**Summary**, from NCBI Gene [3615](https://www.ncbi.nlm.nih.gov/gene/3615):

> This gene encodes the rate-limiting enzyme in the de novo guanine nucleotide biosynthesis. It is thus involved in maintaining cellular guanine deoxy- and ribonucleotide pools needed for DNA and RNA synthesis. The encoded protein catalyzes the NAD-dependent oxidation of inosine-5'-monophosphate into xanthine-5'-monophosphate, which is then converted into guanosine-5'-monophosphate. This gene is up-regulated in some neoplasms, suggesting it may play a role in malignant transformation. [provided …

**Accessions** — [HGNC:6053](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6053) · Entrez [3615](https://www.ncbi.nlm.nih.gov/gene/3615) · UniProt [P12268](https://www.uniprot.org/uniprotkb/P12268) · Ensembl [ENSG00000178035](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178035)

## Data

Gene col 10889: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10889); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10889, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10889]; `tensor/DDL_lfc|DDL_z.npy` [10889]; `embed/gene_vectors.npy` [10889]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10889 or target_col == 10889). Every well: [[IMPDH2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IMPDH2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
