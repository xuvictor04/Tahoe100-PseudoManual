---
symbol: "DSEL"
type: "gene"
col: 10110
ensembl_id: "ENSG00000171451"
name: "dermatan sulfate epimerase like"
location: "18q22.1"
module: 66
arm: "+"
pooled_cpm: 8.04
n_lines_expressing: 34
n_dd_up: 50
n_dd_down: 0
n_dd_up_clean: 38
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 3
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# DSEL

*dermatan sulfate epimerase like* — 18q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 50 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.99× (z +19.0, q 0e+00, up in 25 of 30 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (A498 0.140×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ROS1]] (+0.61, fdr 1e-05), [[KITLG]] (+0.59, fdr 1e-05), [[SEMA3C]] (+0.58, fdr 1e-05); moves opposite to [[ANKRD13D]] (-0.53, fdr 1e-05), [[EFCAB11]] (-0.51, fdr 5e-05), [[DZANK1]] (-0.48, fdr 6e-04).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 3 go from it, the strongest it → [[DST]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 51 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 50 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10110.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.99×** | +19.0 | 0e+00 | 25/30 (hTERT-HPNE, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.58×** | +16.5 | 0e+00 | 17/29 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.64×** | +15.9 | 0e+00 | 29/32 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.58×** | +15.7 | 0e+00 | 28/31 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.04×** | +12.4 | 3e-33 | 26/32 (NCI-H460, A-427, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **2.69×** | +12.2 | 5e-32 | 27/31 (NCI-H2030, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.60×** | +11.3 | 1e-27 | 13/15 (HS-578T, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.28×** | +10.1 | 3e-22 | 24/32 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.22×** | +9.8 | 7e-21 | 24/29 (hTERT-HPNE, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.23×** | +9.1 | 6e-18 | 9/18 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.10×** | +8.7 | 1e-16 | 20/27 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **2.01×** | +8.6 | 4e-16 | 15/23 (HS-578T, hTERT-HPNE, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.06×** | +8.5 | 6e-16 | 19/31 (NCI-H1573, A-427, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.61×** | +8.3 | 5e-15 | 20/32 (A498, J82, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.92×** | +8.0 | 4e-14 | 18/30 (BT-474, HS-578T, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.85×** | +7.5 | 2e-12 | 17/30 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.84×** | +7.5 | 3e-12 | 18/29 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.82×** | +7.4 | 5e-12 | 20/31 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.66×** | +6.3 | 1e-08 | 14/30 (A-427, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10110.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (A498 0.140×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Hexylresorcinol (drug)]] 5 µM |  | 0.814× | -3.6 | 0.13 | 6/32 (NCI-H1792, J82, …) | inconsistent across doses |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 0.816× | -3.5 | 0.13 | 7/32 (A498, LOX-IMVI, …) | rises with dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.759× | -3.4 | 0.14 | 10/29 (SNU-423, NCI-H2030, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10110. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 10.5 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.71× (z +11.5) | — |
| [[A498 (line)]] | wt | 4.08 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.96× (z +11.6) | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.140× (z -9.1) |
| [[C32 (line)]] | wt | 2.27 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.2× (z +10.1) | — |
| [[hTERT-HPNE (line)]] | wt | 35.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.99× (z +11.7) | — |
| [[A-427 (line)]] | wt | 8.00 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.29× (z +9.7) | — |
| [[BT-474 (line)]] | alt | 5.68 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.60× (z +9.6) | — |
| [[HS-578T (line)]] | alt | 18.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +8.6) | — |
| [[LOX-IMVI (line)]] | wt | 7.50 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.86× (z +8.7) | — |
| [[NCI-H1792 (line)]] | alt | 58.7 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.64× (z +12.5) ⚠ position not correctable | — |
| [[NCI-H2030 (line)]] | alt | 7.58 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.74× (z +8.5) | — |
| [[SHP-77 (line)]] | alt | 20.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.62× (z +11.2) | — |
| [[A-172 (line)]] | wt | 4.27 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.54 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.849 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.583 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.632 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.51 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.551 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.913 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.34 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.05 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.586 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.07 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.701 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.567 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.723 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.11 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10110), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ROS1]] | +0.61 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[KITLG]] | +0.59 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[SEMA3C]] | +0.58 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[PALLD]] | +0.57 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[TMEM47]] | +0.57 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[FILIP1L]] | +0.56 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[PHLDB2]] | +0.55 | +0.38 / +0.54 | both halves | 6e-05 |  |
| [[DSG2]] | +0.55 | +0.30 / +0.47 | both halves | 2e-04 |  |
| [[TGFB2]] | +0.54 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[ABLIM1]] | +0.54 | +0.50 / +0.38 | both halves | 6e-05 |  |
| [[MAP2]] | +0.54 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[COL12A1]] | +0.54 | +0.56 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD13D]] | -0.53 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[EFCAB11]] | -0.51 | -0.40 / -0.59 | both halves | 5e-05 |  |
| [[DZANK1]] | -0.48 | -0.22 / -0.53 | both halves | 6e-04 |  |
| [[STARD3]] | -0.48 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[GLE1]] | -0.48 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[ICAM3]] | -0.47 | -0.32 / -0.51 | both halves | 2e-04 |  |
| [[CDK5RAP1]] | -0.47 | -0.51 / -0.29 | both halves | 2e-04 |  |
| [[PPIL3]] | -0.47 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[TRAIP]] | -0.46 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[THOC3]] | -0.46 | -0.47 / -0.37 | both halves | 7e-05 |  |
| [[ZBTB49]] | -0.46 | -0.32 / -0.44 | both halves | 1e-04 |  |
| [[LCMT1]] | -0.46 | -0.48 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DSEL's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 9.2% of all compounds | 0.017 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[ANGPT1]] | B | ANGPT1 activity raises DSEL's level | lines that do not express ANGPT1 (24) vs lines expressing it (26) | 2.69× lower at baseline in the lines without ANGPT1 | 0.019 | ⚠ within organs, on part of the lines; also absent: HTR1F, KC6, AK5 |
| [[MAP2]] | C | MAP2 activity raises DSEL's level | lines that do not express MAP2 (15) vs lines expressing it (35) | 3.67× lower at baseline in the lines without MAP2 | 0.013 | ⚠ within organs, on part of the lines; also absent: LRRC7, ANKRD6, DSEL; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DST]] | B | DSEL activity raises DST's level | lines that do not express DSEL (16) vs lines expressing it (34) | 2.26× lower at baseline in the lines without DSEL | 0.026 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: HDX, GLRB, AFAP1L1 |
| [[POT1-AS1]] | B | DSEL activity raises POT1-AS1's level | lines that do not express DSEL (16) vs lines expressing it (34) | 1.71× lower at baseline in the lines without DSEL | 0.042 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: HDX, GLRB, AFAP1L1 |
| [[NTRK3]] | B | DSEL activity lowers NTRK3's level | lines that do not express DSEL (16) vs lines expressing it (34) | 1.26× higher at baseline in the lines without DSEL | 0.072 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: HDX, GLRB, AFAP1L1 |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.625). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (33.8, 19.5); signed map (46.6, 20.4). **Vector** length 66.8, 14.1% of its response variance represented; |z| ≥ 3 in 833 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | +5.1 | +8.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +12.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +9.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.1 | +7.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +8.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.5 | +5.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +8.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.3 | +3.8 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.6 | -2.4 |
|  | [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | -1.1 | -1.9 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -0.9 | -1.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -0.9 | -0.9 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -0.9 | -1.4 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | -0.9 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | dermatan sulfate epimerase like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q22.1 — chr18:67,506,587-67,516,720 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NCAG1, FLJ11477, DE-epi2; previously C18orf4 |
| Reactome | 4 pathways, smallest: DS-GAG biosynthesis; Chondroitin sulfate/dermatan sulfate metabolism; Glycosaminoglycan metabolism |
| Matched by | ensembl_id |

UniProt [Q8IZU8](https://www.uniprot.org/uniprotkb/Q8IZU8) carries no function annotation.

**Summary**, from NCBI Gene [92126](https://www.ncbi.nlm.nih.gov/gene/92126):

> Predicted to enable chondroitin-glucuronate 5-epimerase activity. Predicted to be involved in chondroitin sulfate proteoglycan metabolic process and dermatan sulfate proteoglycan metabolic process. Predicted to be located in Golgi membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:18144](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18144) · Entrez [92126](https://www.ncbi.nlm.nih.gov/gene/92126) · UniProt [Q8IZU8](https://www.uniprot.org/uniprotkb/Q8IZU8) · Ensembl [ENSG00000171451](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171451)

## Data

Gene col 10110: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10110); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10110, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10110]; `tensor/DDL_lfc|DDL_z.npy` [10110]; `embed/gene_vectors.npy` [10110]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10110 or target_col == 10110). Every well: [[DSEL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DSEL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
