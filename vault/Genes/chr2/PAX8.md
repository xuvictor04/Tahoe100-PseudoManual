---
symbol: "PAX8"
type: "gene"
col: 4632
ensembl_id: "ENSG00000125618"
name: "paired box 8"
location: "2q14.1"
module: 8
arm: "+"
pooled_cpm: 59.17
n_lines_expressing: 16
n_dd_up: 11
n_dd_down: 3
n_dd_up_clean: 6
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 5
direction_downstream: 3
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# PAX8

*paired box 8* — 2q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.12× (z +10.0, q 1e-20, up in 1 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.26× (z +4.6, q 9e-04, up in 5 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.675× (z -5.3, q 5e-05, down in 11 of 14 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DSCAML1]] (+0.51, fdr 2e-05), [[PAX8-AS1]] (+0.51, fdr 1e-05, ⚠ same locus), [[ABCA15P]] (+0.51, fdr 4e-05), [[TRIO]] (+0.46, fdr 2e-04); moves opposite to [[LIX1L]] (-0.44, fdr 1e-04), [[RCN2]] (-0.43, fdr 2e-04), [[TLE5]] (-0.42, fdr 0.002, ⚠ not reproduced), [[PIGS]] (-0.41, fdr 2e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 3 go from it, the strongest it → [[HMGA1P4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4632.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.12×** | +10.0 | 1e-20 | 1/7 (SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.88×** | +8.7 | 8e-16 | 4/10 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +4.6 | 9e-04 | 5/14 (SW480, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +4.0 | 0.011 | 2/14 (SW48, SW480) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.49×** | +3.9 | 0.011 | 1/12 (SNU-423) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.32×** | +3.8 | 0.011 | 0/12 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~2% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.31×** | +3.8 | 0.012 | 4/13 (A498, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.30×** | +3.6 | 0.019 | 4/13 (SW480, Panc 03.27, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.43×** | +3.5 | 0.026 | 2/14 (NCI-H23, AsPC-1) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.27×** | +3.3 | 0.052 | 5/13 (SW480, NCI-H23, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.29×** | +3.3 | 0.052 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.18× | +3.3 | 0.054 | 2/14 (RPMI-7951, SNU-1) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | 1.17× | +3.1 | 0.099 | 4/14 (SW480, HEC-1-A, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4632.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.675×** | -5.3 | 5e-05 | 11/14 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.695×** | -4.9 | 2e-04 | 9/13 (HEC-1-A, A498, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.904× | -4.8 | 4e-04 | 1/14 (NCI-H23) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.771×** | -3.5 | 0.062 | 4/13 (SW 1271, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4632. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 925 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.153× (z -17.3) |
| [[A498 (line)]] | wt | 481 | 0 | 6 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.123× (z -13.9) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.123× (z -13.9) |
| [[NCI-H2122 (line)]] | alt | 27.1 | 0 | 1 | — | [[Chlorhexidine (diacetate) (drug)]] 5 µM 0.241× (z -49.2) |
| [[SW480 (line)]] | alt | 19.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 10.8 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 4.47 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 7.59 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 8.99 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.28 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.92 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 6.06 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 13.7 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.85 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.66 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 11.7 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 12.2 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 8.29 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.65 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 7.95 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 12.4 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.0 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 6.13 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 11.6 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.99 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 6.25 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 11.3 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.0 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 10.6 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 12.4 n.m. | — | — | — | — |
| [[NCI-H23 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.15 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 11.3 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.81 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.84 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 8.92 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.97 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.56 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.97 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 6.87 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 16.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4632), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 6 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DSCAML1]] | +0.51 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[PAX8-AS1]] | +0.51 | +0.49 / +0.54 | both halves | 1e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[ABCA15P]] | +0.51 | +0.44 / +0.43 | both halves | 4e-05 |  |
| [[TRIO]] | +0.46 | +0.37 / +0.31 | both halves | 2e-04 |  |
| [[RHEX]] | +0.46 | +0.38 / +0.50 | both halves | 7e-05 |  |
| [[TP53BP2]] | +0.45 | +0.41 / +0.28 | both halves | 3e-04 |  |
| [[NGF]] | +0.44 | +0.38 / +0.35 | both halves | 1e-04 |  |
| [[LINC02516]] | +0.44 | +0.38 / +0.35 | both halves | 1e-04 |  |
| [[MYOM3]] | +0.44 | +0.42 / +0.30 | both halves | 2e-04 |  |
| [[ST6GALNAC5]] | +0.43 | +0.61 / +0.30 | both halves | 2e-04 |  |
| [[BSPRY]] | +0.43 | +0.48 / +0.43 | both halves | 3e-05 |  |
| [[LINC03004]] | +0.43 | +0.47 / +0.37 | both halves | 8e-05 |  |
| [[CAPN14]] | +0.43 | +0.39 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LIX1L]] | -0.44 | -0.39 / -0.33 | both halves | 1e-04 |  |
| [[RCN2]] | -0.43 | -0.33 / -0.31 | both halves | 2e-04 |  |
| [[TLE5]] | -0.42 | -0.37 / -0.14 | ⚠ not reproduced | 0.002 |  |
| [[PIGS]] | -0.41 | -0.31 / -0.36 | both halves | 2e-04 |  |
| [[HMCES]] | -0.41 | -0.30 / -0.38 | both halves | 2e-04 |  |
| [[ANAPC5]] | -0.39 | -0.26 / -0.30 | both halves | 4e-04 |  |
| [[NKTR]] | -0.39 | -0.36 / -0.20 | both halves | 7e-04 |  |
| [[NEK4]] | -0.39 | -0.35 / -0.34 | both halves | 1e-04 |  |
| [[SPAST]] | -0.39 | -0.35 / -0.29 | both halves | 3e-04 |  |
| [[PRKACA]] | -0.38 | -0.29 / -0.33 | both halves | 3e-04 | STRING 913 |
| [[ATPAF1]] | -0.38 | -0.35 / -0.23 | both halves | 5e-04 |  |
| [[NUP133]] | -0.38 | -0.42 / -0.20 | both halves | 7e-04 |  |
| [[ATP6AP2]] | -0.37 | -0.30 / -0.23 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises PAX8's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[DIO2]] | B | DIO2 activity raises PAX8's level | lines that do not express DIO2 (14) vs lines expressing it (36) | 1.01× lower at baseline in the lines without DIO2 | 0.099 | ⚠ within organs, on part of the lines; also absent: LINC01725, ENSG00000226640, RNF150 |
| [[PAX8-AS1]] | C | PAX8-AS1 activity raises PAX8's level | lines that do not express PAX8-AS1 (19) vs lines expressing it (31) | 2.65× lower at baseline in the lines without PAX8-AS1 | 0.014 | ⚠ within organs, on part of the lines; also absent: CCDC68, PAX8, PCSK5; maybe low, not absent; co-absent with the target |
| [[SHISA9]] | C | SHISA9 activity raises PAX8's level | lines that do not express SHISA9 (38) vs lines expressing it (12) | 1.88× lower at baseline in the lines without SHISA9 | 0.033 | ⚠ within organs, on part of the lines; also absent: LHFPL3-AS1, S100A1, LINC01456; maybe low, not absent; co-absent with the target |
| [[LINC00504]] | C | LINC00504 activity raises PAX8's level | lines that do not express LINC00504 (31) vs lines expressing it (19) | 1.49× lower at baseline in the lines without LINC00504 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000287598, LINC02930, ENSG00000287474; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HMGA1P4]] | B | PAX8 activity raises HMGA1P4's level | lines that do not express PAX8 (34) vs lines expressing it (16) | 1.83× lower at baseline in the lines without PAX8 | 0.044 | ⚠ within organs, on part of the lines; also absent: FGF19, RGPD2, BMP10 |
| [[PAX8-AS1]] | C | PAX8 activity raises PAX8-AS1's level | lines that do not express PAX8 (34) vs lines expressing it (16) | 3.87× lower at baseline in the lines without PAX8 | 7e-04 | ⚠ within organs, on part of the lines; also absent: FGF19, RGPD2, BMP10; co-absent with the target |
| [[SHISA9]] | C | PAX8 activity raises SHISA9's level | lines that do not express PAX8 (34) vs lines expressing it (16) | 1.87× lower at baseline in the lines without PAX8 | 0.067 | ⚠ within organs, on part of the lines; also absent: FGF19, RGPD2, BMP10; co-absent with the target |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.178). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (2.9, 50.0); signed map (51.2, 7.8). **Vector** length 29.7, 6.60% of its response variance represented; |z| ≥ 3 in 270 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +1.1 | +1.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.0 | +4.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +0.9 | +3.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +0.9 | +2.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +0.9 | +1.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +0.8 | +2.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +0.7 | +1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +0.7 | +1.8 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -0.8 | -2.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | -0.7 | -5.3 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -0.6 | -2.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -0.6 | -2.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.6 | -0.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.5 | -2.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -0.5 | +1.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -0.5 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | paired box 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q14.1 — chr2:113,215,997-113,278,921 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PAX-8 |
| Gene groups (HGNC) | PRD class homeoboxes and pseudogenes; Paired boxes |
| Reactome | 4 pathways, smallest: Formation of intermediate mesoderm; Formation of the nephric duct; Kidney development |
| Matched by | ensembl_id |

**Function**, from UniProt [Q06710](https://www.uniprot.org/uniprotkb/Q06710) (Paired box protein Pax-8):

> Transcription factor for the thyroid-specific expression of the genes exclusively expressed in the thyroid cell type, maintaining the functional differentiation of such cells.

**Summary**, from NCBI Gene [7849](https://www.ncbi.nlm.nih.gov/gene/7849):

> This gene encodes a member of the paired box (PAX) family of transcription factors. Members of this gene family typically encode proteins that contain a paired box domain, an octapeptide, and a paired-type homeodomain. This nuclear protein is involved in thyroid follicular cell development and expression of thyroid-specific genes. Mutations in this gene have been associated with thyroid dysgenesis, thyroid follicular carcinomas and atypical follicular thyroid adenomas. Alternatively spliced …

**Accessions** — [HGNC:8622](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8622) · Entrez [7849](https://www.ncbi.nlm.nih.gov/gene/7849) · UniProt [Q06710](https://www.uniprot.org/uniprotkb/Q06710) · Ensembl [ENSG00000125618](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125618)

## Data

Gene col 4632: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4632); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4632, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4632]; `tensor/DDL_lfc|DDL_z.npy` [4632]; `embed/gene_vectors.npy` [4632]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4632 or target_col == 4632). Every well: [[PAX8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PAX8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
