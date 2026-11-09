---
symbol: "LHX1-DT"
type: "gene"
col: 15890
ensembl_id: "ENSG00000277268"
name: "LHX1 divergent transcript"
location: "17q12"
module: 154
arm: "+"
pooled_cpm: 6.62
n_lines_expressing: 22
n_dd_up: 25
n_dd_down: 2
n_dd_up_clean: 17
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/154"]
generated_by: "tahoemap"
---

# LHX1-DT

*LHX1 divergent transcript* — 17q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.18× (z +22.8, q 0e+00, up in 15 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Clobetasol propionate (drug)]] 0.5 µM: 0.595× (z -4.6, q 0.002, down in 8 of 18 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Folic acid (drug)]] 5 µM in 1 line (Hs 766T 0.233×); [[Cabozantinib (S-malate) (drug)]] 0.5 µM in 1 line (A549 0.0608×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CALB2]] (+0.65, fdr 1e-05), [[C7orf57]] (+0.60, fdr 2e-05), [[GOLGA7B-DT]] (+0.60, fdr 1e-05); moves opposite to [[THRAP3]] (-0.50, fdr 3e-05), [[IL1R1]] (-0.49, fdr 4e-05), [[ATF7]] (-0.49, fdr 1e-04).
> It is in [[Module 154]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 3 go from it, the strongest it → [[TMSB15B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15890.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.18×** | +22.8 | 0e+00 | 15/16 (HOP62, A498, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.54×** | +10.7 | 2e-24 | 2/8 (SNU-423, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **2.01×** | +8.7 | 6e-16 | 14/18 (NCI-H460, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.63×** | +8.5 | 2e-15 | 5/12 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.76×** | +8.3 | 1e-14 | 3/10 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.96×** | +5.7 | 1e-06 | 5/12 (HOP62, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.88×** | +5.6 | 2e-06 | 11/18 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.86×** | +5.5 | 3e-06 | 11/17 (HOP62, MIA PaCa-2, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.65×** | +4.4 | 6e-04 | 5/18 (CFPAC-1, HOP62, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.65×** | +4.4 | 6e-04 | 7/18 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.67×** | +4.4 | 6e-04 | 6/16 (HOP62, NCI-H460, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.63×** | +4.3 | 8e-04 | 9/18 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.40×** | +4.2 | 0.001 | 5/18 (HOP62, Hs 766T, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +4.2 | 0.001 | 5/17 (HOP62, SNU-423, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +4.0 | 0.002 | 4/15 (HOP62, SNU-423, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.36×** | +3.8 | 0.004 | 3/16 (AsPC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.53×** | +3.7 | 0.006 | 7/18 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.34×** | +3.7 | 0.007 | 2/18 (CFPAC-1, PANC-1) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.52×** | +3.7 | 0.007 | 11/18 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Radotinib (drug)]] 5 µM |  | **1.33×** | +3.5 | 0.012 | 6/18 (CFPAC-1, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15890.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Folic acid (drug)]] 5 µM in 1 line (Hs 766T 0.233×); [[Cabozantinib (S-malate) (drug)]] 0.5 µM in 1 line (A549 0.0608×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.595×** | -4.6 | 0.002 | 8/18 (HOP62, SNU-423, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.662×** | -3.7 | 0.069 | 9/18 (SNU-423, C32, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15890. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 10.8 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.2× (z +17.3) | — |
| [[A549 (line)]] | wt | 2.88 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.36× (z +8.7) | [[Cabozantinib (S-malate) (drug)]] 0.5 µM 0.0608× (z -8.6) |
| [[Hs 766T (line)]] | wt | 11.7 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.45× (z +13.4) | [[Folic acid (drug)]] 5 µM 0.233× (z -8.7) |
| [[A-172 (line)]] | wt | 17.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.21× (z +9.9) | — |
| [[A498 (line)]] | wt | 52.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.75× (z +16.9) | — |
| [[NCI-H460 (line)]] | wt | 2.21 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.30× (z +10.4) | — |
| [[PANC-1 (line)]] | alt | 5.61 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.95× (z +11.4) | — |
| [[SNU-423 (line)]] | alt | 25.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.09× (z +13.1) | — |
| [[A-427 (line)]] | wt | 1.31 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.981 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.804 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.23 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.818 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.809 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.940 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.760 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.678 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.862 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.93 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.598 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.977 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.583 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.915 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.631 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.898 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.677 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.693 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.707 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.839 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.57 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15890), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CALB2]] | +0.65 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[C7orf57]] | +0.60 | +0.47 / +0.69 | both halves | 2e-05 |  |
| [[GOLGA7B-DT]] | +0.60 | +0.56 / +0.53 | both halves | 1e-05 | same gene group |
| [[LHX1]] | +0.60 | +0.63 / +0.62 | both halves | 7e-06 | ⚠ same locus (0.1 kb: neighbours can correlate without regulation) |
| [[METTL21A]] | +0.59 | +0.39 / +0.65 | both halves | 5e-05 |  |
| [[SH3GL3]] | +0.53 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[NOL4L]] | +0.52 | +0.40 / +0.49 | both halves | 5e-05 |  |
| [[GBX1]] | +0.52 | +0.33 / +0.51 | both halves | 1e-04 |  |
| [[GRK5]] | +0.51 | +0.35 / +0.57 | both halves | 1e-04 |  |
| [[NPTX1]] | +0.51 | +0.40 / +0.52 | both halves | 5e-05 |  |
| [[RASSF3]] | +0.51 | +0.42 / +0.45 | both halves | 4e-05 |  |
| [[DOCK7-DT]] | +0.50 | +0.35 / +0.58 | both halves | 1e-04 | same gene group |
| [[TNFRSF11A]] | +0.50 | +0.38 / +0.57 | both halves | 6e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THRAP3]] | -0.50 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[IL1R1]] | -0.49 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[ATF7]] | -0.49 | -0.34 / -0.55 | both halves | 1e-04 |  |
| [[JPH2]] | -0.48 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[MRFAP1]] | -0.47 | -0.38 / -0.36 | both halves | 9e-05 |  |
| [[NNMT]] | -0.47 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[SRP68]] | -0.46 | -0.34 / -0.44 | both halves | 1e-04 |  |
| [[EXOSC10]] | -0.45 | -0.39 / -0.47 | both halves | 6e-05 |  |
| [[PIGO]] | -0.45 | -0.28 / -0.47 | both halves | 3e-04 |  |
| [[ZNF512B]] | -0.45 | -0.21 / -0.53 | both halves | 7e-04 |  |
| [[CPLANE1]] | -0.45 | -0.32 / -0.46 | both halves | 2e-04 |  |
| [[ARAF]] | -0.44 | -0.19 / -0.48 | ⚠ not reproduced | 8e-04 |  |
| [[TOR1AIP1]] | -0.44 | -0.40 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers LHX1-DT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LHX1]] | C | LHX1 activity raises LHX1-DT's level | lines that do not express LHX1 (27) vs lines expressing it (23) | 2.96× lower at baseline in the lines without LHX1 | 0.001 | ⚠ within organs, on part of the lines; also absent: LHX1-DT, ADAMTS16, ECSCR; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMSB15B]] | B | LHX1-DT activity raises TMSB15B's level | lines that do not express LHX1-DT (28) vs lines expressing it (22) | 1.41× lower at baseline in the lines without LHX1-DT | 0.070 | ⚠ within organs, on part of the lines; also absent: LHX1, EYA4, CDH4 |
| [[LHX1]] | C | LHX1-DT activity raises LHX1's level | lines that do not express LHX1-DT (28) vs lines expressing it (22) | 3.49× lower at baseline in the lines without LHX1-DT | 0.001 | ⚠ within organs, on part of the lines; also absent: LHX1, EYA4, CDH4; co-absent with the target |
| [[LBH]] | C | LHX1-DT activity raises LBH's level | lines that do not express LHX1-DT (28) vs lines expressing it (22) | 3.50× lower at baseline in the lines without LHX1-DT | 0.036 | ⚠ within organs, on part of the lines; also absent: LHX1, EYA4, CDH4; co-absent with the target |

## Where it sits

- **Module**: [[Module 154]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.551). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.6, -3.9); signed map (10.8, 37.9). **Vector** length 43.3, 10.1% of its response variance represented; |z| ≥ 3 in 408 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +22.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +8.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +10.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.8 | +8.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.7 | +8.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +5.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +4.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +3.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.4 | +1.7 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.9 | -1.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.8 | -0.4 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.7 | -2.4 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.6 | -2.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.6 | -2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -2.9 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.4 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | LHX1 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 17q12 — chr17:36,861,674-36,936,670 (-) |
| Ensembl biotype | lncRNA |
| Also known as | lnc-ACACA-1 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:53778](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53778) · Entrez [102723471](https://www.ncbi.nlm.nih.gov/gene/102723471) · Ensembl [ENSG00000277268](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000277268)

## Data

Gene col 15890: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15890); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15890, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15890]; `tensor/DDL_lfc|DDL_z.npy` [15890]; `embed/gene_vectors.npy` [15890]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15890 or target_col == 15890). Every well: [[LHX1-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LHX1-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
