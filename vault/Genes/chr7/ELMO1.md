---
symbol: "ELMO1"
type: "gene"
col: 7922
ensembl_id: "ENSG00000155849"
name: "engulfment and cell motility 1"
location: "7p14.2-p14.1"
module: 19
arm: "+"
pooled_cpm: 10.57
n_lines_expressing: 33
n_dd_up: 26
n_dd_down: 5
n_dd_up_clean: 16
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# ELMO1

*engulfment and cell motility 1* — 7p14.2-p14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.67× (z +18.7, q 0e+00, up in 14 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 0.05 µM: 0.724× (z -4.0, q 0.030, down in 11 of 26 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NELL1]] (+0.60, fdr 1e-05), [[DAAM2]] (+0.59, fdr 4e-05), [[RTN1]] (+0.58, fdr 1e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[NRCAM]] → it (grade B ⚠); 1 goes from it, the strongest it → [[KCNB1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7922.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.67×** | +18.7 | 0e+00 | 14/27 (KATO III, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.58×** | +18.0 | 0e+00 | 12/27 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.90×** | +17.6 | 0e+00 | 3/12 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.74×** | +13.5 | 1e-39 | 17/29 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.94×** | +12.6 | 2e-34 | 23/29 (SW480, SW1417, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.48×** | +12.2 | 2e-32 | 7/20 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **2.14×** | +10.2 | 1e-22 | 15/27 (SW480, SW1417, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.99×** | +8.5 | 9e-16 | 2/14 (NCI-H1573, PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.69×** | +7.1 | 1e-10 | 12/29 (SNU-1, A498, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.72×** | +7.0 | 2e-10 | 11/28 (KATO III, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.44×** | +6.9 | 3e-10 | 12/29 (SNU-1, A-172, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.65×** | +6.7 | 8e-10 | 13/27 (SW480, SW1417, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.59×** | +6.3 | 2e-08 | 14/28 (SW480, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.63×** | +6.1 | 3e-08 | 15/29 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.45×** | +4.8 | 7e-05 | 6/25 (A498, A549, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.36×** | +4.1 | 0.001 | 10/27 (SW1417, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.36×** | +3.8 | 0.004 | 10/27 (HS-578T, A-172, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.31×** | +3.6 | 0.008 | 8/26 (NCI-H1792, A-172, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.30×** | +3.5 | 0.013 | 6/27 (HS-578T, A549, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.31×** | +3.4 | 0.016 | 9/28 (NCI-H1792, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Arbutin (drug)]] 0.05 µM |  | **1.27×** | +3.0 | 0.070 | 3/26 (A-172, A549, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7922.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.05 µM |  | **0.724×** | -4.0 | 0.030 | 11/26 (SW1417, SNU-1, …) | inconsistent across doses | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.825×** | -3.7 | 0.066 | 11/29 (BT-474, C32, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.756×** | -3.6 | 0.066 | 9/27 (A-427, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.764×** | -3.5 | 0.066 | 7/28 (HS-578T, CHP-212, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.780×** | -3.4 | 0.086 | 9/27 (SHP-77, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.789× | -3.2 | 0.12 | 14/29 (SHP-77, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7922. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 2.84 | 6 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 39.2× (z +14.7) | — |
| [[SW1417 (line)]] | alt | 4.18 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 18.5× (z +12.1) | — |
| [[C32 (line)]] | wt | 57.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -10.2) |
| [[SHP-77 (line)]] | alt | 59.5 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.172× (z -10.1) |
| [[KATO III (line)]] | alt | 3.78 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 16.0× (z +12.4) | — |
| [[SK-MEL-2 (line)]] | alt | 9.54 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 14.6× (z +10.2) | — |
| [[NCI-H2030 (line)]] | alt | 5.40 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 4.85× (z +8.6) | [[Cobimetinib (drug)]] 5 µM 0.0931× (z -8.7) |
| [[A498 (line)]] | wt | 3.23 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.92× (z +9.4) | — |
| [[HEC-1-A (line)]] | alt | 2.90 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.77× (z +9.9) | — |
| [[HS-578T (line)]] | alt | 45.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 28.5 | 1 | 0 | [[Bortezomib (drug)]] 0.05 µM 4.78× (z +8.6) | — |
| [[PANC-1 (line)]] | alt | 3.18 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +9.1) | — |
| [[A-172 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.92 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.46 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.08 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 46.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 136 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.05 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.87 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.29 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.52 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.40 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.18 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.91 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 54.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.59 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.12 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7922), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NELL1]] | +0.60 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[DAAM2]] | +0.59 | +0.41 / +0.63 | both halves | 4e-05 | **novel candidate** |
| [[RTN1]] | +0.58 | +0.50 / +0.54 | both halves | 1e-05 | same gene group |
| [[MTMR7]] | +0.57 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[PTPRD]] | +0.56 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[LAMB4]] | +0.54 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[GHR]] | +0.53 | +0.34 / +0.57 | both halves | 1e-04 |  |
| [[ST8SIA1]] | +0.52 | +0.40 / +0.53 | both halves | 4e-05 |  |
| [[NRCAM]] | +0.52 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[CNTN4]] | +0.52 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[GAS7]] | +0.52 | +0.29 / +0.56 | both halves | 2e-04 |  |
| [[ADGRL3]] | +0.51 | +0.38 / +0.58 | both halves | 7e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NRCAM]] | B | NRCAM activity raises ELMO1's level | lines that do not express NRCAM (36) vs lines expressing it (14) | 1.93× lower at baseline in the lines without NRCAM | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, SPP1, FGG |
| [[TOP2A]] | B | TOP2A activity lowers ELMO1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LIN7A]] | B | LIN7A activity raises ELMO1's level | lines that do not express LIN7A (34) vs lines expressing it (16) | 3.13× lower at baseline in the lines without LIN7A | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000239268, DPP10, FGL1 |
| [[SLC7A2]] | B | SLC7A2 activity raises ELMO1's level | lines that do not express SLC7A2 (30) vs lines expressing it (20) | 2.46× lower at baseline in the lines without SLC7A2 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, HGF, UNC5D |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCNB1]] | B | ELMO1 activity raises KCNB1's level | lines that do not express ELMO1 (17) vs lines expressing it (33) | 1.51× lower at baseline in the lines without ELMO1 | 0.095 | ⚠ within organs, on part of the lines; also absent: VEGFD, FRG1FP, NOVA2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.415). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (52.9, 24.9); signed map (25.6, 38.7). **Vector** length 60.1, 11.7% of its response variance represented; |z| ≥ 3 in 755 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.4 | +12.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.1 | +17.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.5 | +8.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.8 | +12.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.8 | +18.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +6.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +1.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.4 | +3.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +0.3 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.3 | -1.1 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.2 | -0.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.0 | -1.3 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.9 | -3.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.9 | -2.7 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.7 | +0.0 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.6 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | engulfment and cell motility 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p14.2-p14.1 — chr7:36,852,906-37,449,223 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0281, CED12, ELMO-1, CED-12 |
| Gene groups (HGNC) | Engulfment and cell motility proteins; MicroRNA protein coding host genes |
| Reactome | 25 pathways, smallest: Nef and signal transduction; PTK6 Regulates RHO GTPases, RAS GTPase and MAP kinases; SRC activates STAT3 in a quantitative manner, through Cadherin-11 (CDH11), RAC1 and gp130 (IL6ST) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92556](https://www.uniprot.org/uniprotkb/Q92556) (Engulfment and cell motility protein 1):

> Regulates the activity of DOCK guanine nucleotide exchange factors (GEFs). Acts in association with DOCK1, DOCK2, DOCK5 and CRK. Promotes RAC1 activation by DOCK5; the activity is stimulated by RHOG. Involved in cytoskeletal rearrangements required for phagocytosis of apoptotic cells and cell motility.

**Summary**, from NCBI Gene [9844](https://www.ncbi.nlm.nih.gov/gene/9844):

> This gene encodes a member of the engulfment and cell motility protein family. These proteins interact with dedicator of cytokinesis proteins to promote phagocytosis and cell migration. Increased expression of this gene and dedicator of cytokinesis 1 may promote glioma cell invasion, and single nucleotide polymorphisms in this gene may be associated with diabetic nephropathy. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Aug 2013]

**Accessions** — [HGNC:16286](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16286) · Entrez [9844](https://www.ncbi.nlm.nih.gov/gene/9844) · UniProt [Q92556](https://www.uniprot.org/uniprotkb/Q92556) · Ensembl [ENSG00000155849](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155849)

## Data

Gene col 7922: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7922); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7922, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7922]; `tensor/DDL_lfc|DDL_z.npy` [7922]; `embed/gene_vectors.npy` [7922]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7922 or target_col == 7922). Every well: [[ELMO1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ELMO1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
