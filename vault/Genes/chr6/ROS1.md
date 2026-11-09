---
symbol: "ROS1"
type: "gene"
col: 527
ensembl_id: "ENSG00000047936"
name: "ROS proto-oncogene 1, receptor tyrosine kinase"
location: "6q22.1"
module: 66
arm: "+"
pooled_cpm: 2.98
n_lines_expressing: 20
n_dd_up: 26
n_dd_down: 0
n_dd_up_clean: 19
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 11
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# ROS1

*ROS proto-oncogene 1, receptor tyrosine kinase* — 6q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 10.1× (z +20.9, q 0e+00, up in 9 of 11 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PHLDB2]] (+0.75, fdr 7e-06), [[TGFB2]] (+0.71, fdr 7e-06), [[OLR1]] (+0.68, fdr 1e-05); moves opposite to [[RNF168]] (-0.57, fdr 1e-05), [[PGF]] (-0.55, fdr 4e-05), [[TMEM158]] (-0.55, fdr 2e-05).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 11 go from it, the strongest it → [[NEXN]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 527.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **10.1×** | +20.9 | 0e+00 | 9/11 (A549, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **5.99×** | +16.2 | 0e+00 | 7/12 (A-172, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.73×** | +10.7 | 1e-24 | 1/2 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.50×** | +9.6 | 1e-19 | 3/7 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **3.60×** | +8.2 | 3e-14 | 4/15 (A-172, HS-578T, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **3.67×** | +8.0 | 1e-13 | 12/15 (SNU-423, HOP62, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.23×** | +7.2 | 3e-11 | 8/17 (HOP62, SNU-423, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.21×** | +7.1 | 7e-11 | 9/17 (HOP62, J82, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.91×** | +6.8 | 5e-10 | 9/12 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.74×** | +6.4 | 7e-09 | 5/15 (J82, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.55×** | +6.0 | 8e-08 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.36×** | +5.5 | 2e-06 | 7/13 (HOP62, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.37×** | +5.3 | 5e-06 | 2/7 (NCI-H2030, NCI-H1792) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.16×** | +4.7 | 1e-04 | 3/14 (J82, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.12×** | +4.6 | 2e-04 | 0/7 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.71×** | +4.2 | 1e-03 | 10/16 (HOP62, A-172, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.78×** | +3.7 | 0.007 | 1/15 (HOP62) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.75×** | +3.6 | 0.011 | 8/17 (HOP62, A-172, …) | rises with dose | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.77×** | +3.5 | 0.013 | 10/14 (HOP62, A-172, …) | rises with dose | position effect removed |
| [[Budesonide (drug)]] 0.5 µM |  | **1.68×** | +3.3 | 0.027 | 6/15 (NCI-H2347, HS-578T, …) | inconsistent across doses |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 527. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 4.80 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 24.3× (z +10.7) | — |
| [[HOP62 (line)]] | alt | 18.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.59× (z +10.6) | — |
| [[SNU-423 (line)]] | alt | 55.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +8.5) | — |
| [[A-427 (line)]] | wt | 0.365 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.595 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.546 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.738 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.614 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.440 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.514 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.658 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.475 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.791 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.64 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.451 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.573 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.679 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.384 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.487 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.975 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.985 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.509 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.453 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.535 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.522 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.355 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.532 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.697 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.314 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.446 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.410 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.489 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.447 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.616 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.435 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.516 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.442 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 527), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHLDB2]] | +0.75 | +0.65 / +0.74 | both halves | 7e-06 |  |
| [[TGFB2]] | +0.71 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[OLR1]] | +0.68 | +0.51 / +0.70 | both halves | 1e-05 | pathway: HALLMARK_INFLAMMATORY_RESPONSE |
| [[FSTL3]] | +0.68 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[LINC02057]] | +0.66 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[TNFAIP6]] | +0.66 | +0.61 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_INFLAMMATORY_RESPONSE |
| [[DIO2]] | +0.64 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[ALPK2]] | +0.64 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[LUM]] | +0.64 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[LINC00882]] | +0.62 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[IL1R1]] | +0.61 | +0.70 / +0.50 | both halves | 1e-05 | pathway: HALLMARK_INFLAMMATORY_RESPONSE |
| [[KCNT2]] | +0.61 | +0.55 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF168]] | -0.57 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[PGF]] | -0.55 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[TMEM158]] | -0.55 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[AP3M2]] | -0.54 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[FXYD5]] | -0.51 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[WWTR1]] | -0.51 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[ABTB3]] | -0.51 | -0.51 / -0.37 | both halves | 8e-05 |  |
| [[RAC2]] | -0.51 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[ATG16L2]] | -0.50 | -0.50 / -0.37 | both halves | 8e-05 |  |
| [[ETV5]] | -0.50 | -0.47 / -0.39 | both halves | 5e-05 |  |
| [[ECI2]] | -0.49 | -0.43 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 5, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NEXN]] | B | ROS1 activity raises NEXN's level | lines that do not express ROS1 (30) vs lines expressing it (20) | 1.78× lower at baseline in the lines without ROS1 | 0.011 | ⚠ within organs, on part of the lines; also absent: COL1A1, APCDD1L, GYPC; maybe low, not absent |
| [[SOD2]] | B | ROS1 activity raises SOD2's level | lines that do not express ROS1 (30) vs lines expressing it (20) | 2.36× lower at baseline in the lines without ROS1 | 0.014 | ⚠ within organs, on part of the lines; also absent: COL1A1, APCDD1L, GYPC; maybe low, not absent |
| [[RAC2]] | B | ROS1 activity raises RAC2's level | lines that do not express ROS1 (30) vs lines expressing it (20) | 3.71× lower at baseline in the lines without ROS1 | 0.061 | ⚠ within organs, on part of the lines; also absent: COL1A1, APCDD1L, GYPC; maybe low, not absent |
| [[MGST1]] | B | ROS1 activity raises MGST1's level | lines that do not express ROS1 (30) vs lines expressing it (20) | 1.88× lower at baseline in the lines without ROS1 | 0.064 | ⚠ within organs, on part of the lines; also absent: COL1A1, APCDD1L, GYPC; maybe low, not absent |
| [[THBS3-AS1]] | B | ROS1 activity weakens THBS3-AS1's drug response | lines that do not express ROS1 (26) vs lines expressing it (17) | the lines without ROS1 respond 2.08× as strongly (z diff -1.14); strongest at Niclosamide (olamine) 5 µM: 0.29x vs 0.93x (z diff -3.3) | 0.091 | ⚠ within organs, on part of the lines; also absent: COL1A1, APCDD1L, GYPC; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[TNFAIP6]] | C | ROS1 activity raises TNFAIP6's level | lines that do not express ROS1 (30) vs lines expressing it (20) | 2.72× lower at baseline in the lines without ROS1 | 0.021 | ⚠ within organs, on part of the lines; also absent: COL1A1, APCDD1L, GYPC; maybe low, not absent; co-absent with the target |
| [[CFH]] | C | ROS1 activity raises CFH's level | lines that do not express ROS1 (30) vs lines expressing it (20) | 2.63× lower at baseline in the lines without ROS1 | 0.023 | ⚠ within organs, on part of the lines; also absent: COL1A1, APCDD1L, GYPC; maybe low, not absent; co-absent with the target |
| [[LUM]] | C | ROS1 activity raises LUM's level | lines that do not express ROS1 (30) vs lines expressing it (20) | 2.46× lower at baseline in the lines without ROS1 | 0.043 | ⚠ within organs, on part of the lines; also absent: COL1A1, APCDD1L, GYPC; maybe low, not absent; co-absent with the target |
| [[DIRAS3]] | C | ROS1 activity raises DIRAS3's level | lines that do not express ROS1 (30) vs lines expressing it (20) | 1.77× lower at baseline in the lines without ROS1 | 0.045 | ⚠ within organs, on part of the lines; also absent: COL1A1, APCDD1L, GYPC; maybe low, not absent; co-absent with the target |
| [[CCBE1]] | C | ROS1 activity raises CCBE1's level | lines that do not express ROS1 (30) vs lines expressing it (20) | 4.57× lower at baseline in the lines without ROS1 | 0.060 | ⚠ within organs, on part of the lines; also absent: COL1A1, APCDD1L, GYPC; maybe low, not absent; co-absent with the target |
| [[CSF1]] | C | ROS1 activity raises CSF1's level | lines that do not express ROS1 (30) vs lines expressing it (20) | 1.81× lower at baseline in the lines without ROS1 | 0.097 | ⚠ within organs, on part of the lines; also absent: COL1A1, APCDD1L, GYPC; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.620). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (33.8, 22.0); signed map (46.2, 21.2). **Vector** length 43.8, 12.0% of its response variance represented; |z| ≥ 3 in 412 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +10.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.0 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.7 | +6.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +20.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.1 | +16.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +7.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.2 | +4.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.1 | +3.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.0 | +3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +7.1 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | +0.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.1 | -0.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.1 | -0.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.9 | +0.1 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.9 | -2.0 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.8 | -1.9 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -0.8 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | ROS proto-oncogene 1, receptor tyrosine kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q22.1 — chr6:117,287,353-117,425,942 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MCF3, ROS, c-ros-1 |
| Gene groups (HGNC) | Fibronectin type III domain containing; ROS proto-oncogene 1, receptor tyrosine kinase family |
| Hallmark sets | INFLAMMATORY_RESPONSE |
| Matched by | ensembl_id |

**Function**, from UniProt [P08922](https://www.uniprot.org/uniprotkb/P08922) (Proto-oncogene tyrosine-protein kinase ROS):

> Receptor tyrosine kinase (RTK) that plays a role in epithelial cell differentiation and regionalization of the proximal epididymal epithelium. NELL2 is an endogenous ligand for ROS1. Upon endogenous stimulation by NELL2, ROS1 activates the intracellular signaling pathway and triggers epididymal epithelial differentiation and subsequent sperm maturation (By similarity). May activate several downstream signaling pathways related to cell differentiation, proliferation, growth and survival …

**Summary**, from NCBI Gene [6098](https://www.ncbi.nlm.nih.gov/gene/6098):

> This proto-oncogene, highly-expressed in a variety of tumor cell lines, belongs to the sevenless subfamily of tyrosine kinase insulin receptor genes. The protein encoded by this gene is a type I integral membrane protein with tyrosine kinase activity. The protein may function as a growth or differentiation factor receptor. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:10261](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10261) · Entrez [6098](https://www.ncbi.nlm.nih.gov/gene/6098) · UniProt [P08922](https://www.uniprot.org/uniprotkb/P08922) · Ensembl [ENSG00000047936](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000047936)

## Data

Gene col 527: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 527); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 527, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 527]; `tensor/DDL_lfc|DDL_z.npy` [527]; `embed/gene_vectors.npy` [527]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 527 or target_col == 527). Every well: [[ROS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ROS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
