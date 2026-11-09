---
symbol: "CCN3"
type: "gene"
col: 5955
ensembl_id: "ENSG00000136999"
name: "cellular communication network factor 3"
location: "8q24.12"
module: 9
arm: "+"
pooled_cpm: 2.9
n_lines_expressing: 30
n_dd_up: 32
n_dd_down: 0
n_dd_up_clean: 23
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 7
direction_downstream: 8
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# CCN3

*cellular communication network factor 3* — 8q24.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.50× (z +12.8, q 1e-34, up in 11 of 12 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 2.97× (z +11.5, q 2e-28, up in 23 of 27 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPNMB]] (+0.67, fdr 7e-06), [[QPCT]] (+0.60, fdr 2e-05), [[RAB38]] (+0.60, fdr 3e-05); moves opposite to [[USP20]] (-0.50, fdr 1e-04), [[SLC25A16]] (-0.50, fdr 1e-04), [[CBY1]] (-0.49, fdr 2e-04).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[CD74]] → it (grade B ⚠); 8 go from it, the strongest it → [[DDX46]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5955.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.50×** | +12.8 | 1e-34 | 11/12 (J82, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **2.97×** | +11.5 | 2e-28 | 23/27 (Panc 03.27, LS 180, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.79×** | +11.3 | 3e-27 | 4/5 (J82, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.27×** | +8.7 | 5e-16 | 14/21 (HEC-1-A, A498, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 5 µM |  | **2.25×** | +8.6 | 8e-16 | 14/26 (NCI-H2347, A498, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.05×** | +8.4 | 5e-15 | 16/23 (Panc 03.27, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.18×** | +8.0 | 8e-14 | 4/6 (J82, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.93×** | +7.0 | 2e-10 | 12/24 (A498, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.24×** | +5.8 | 4e-07 | 9/15 (SK-MEL-2, J82, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.67×** | +5.4 | 3e-06 | 10/27 (J82, A498, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.08×** | +5.3 | 6e-06 | 8/22 (HS-578T, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.96×** | +4.9 | 5e-05 | 8/14 (J82, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.90×** | +4.8 | 6e-05 | 10/27 (C32, A498, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.88×** | +4.7 | 9e-05 | 11/25 (NCI-H2347, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.81×** | +4.4 | 3e-04 | 9/25 (J82, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.79×** | +4.4 | 4e-04 | 8/22 (C32, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Radotinib (drug)]] 5 µM |  | **1.51×** | +4.4 | 4e-04 | 8/27 (C32, A498, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.82×** | +4.3 | 5e-04 | 9/24 (J82, C32, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +3.8 | 0.003 | 6/18 (SK-MEL-2, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.66×** | +3.8 | 0.004 | 4/27 (LS 180, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5955. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 8.46 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.156 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 6.24 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.282 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.377 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.218 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.931 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.223 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.27 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.81 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.202 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.16 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.929 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.218 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.620 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.46 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.245 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.423 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.989 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.161 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.678 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.289 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.463 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.283 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 8.15 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.168 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.647 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.16 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.231 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.53 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.225 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.837 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.432 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5955), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPNMB]] | +0.67 | +0.58 / +0.73 | both halves | 7e-06 |  |
| [[QPCT]] | +0.60 | +0.46 / +0.57 | both halves | 2e-05 |  |
| [[RAB38]] | +0.60 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[AGA]] | +0.58 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[PEG10]] | +0.57 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[DSC3]] | +0.54 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[DCT]] | +0.54 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[LYPD1]] | +0.53 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[PCDH17]] | +0.52 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[CPNE8]] | +0.52 | +0.49 / +0.35 | both halves | 1e-04 |  |
| [[FAM171B]] | +0.51 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[TLL1]] | +0.51 | +0.36 / +0.55 | both halves | 9e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP20]] | -0.50 | -0.37 / -0.34 | both halves | 1e-04 |  |
| [[SLC25A16]] | -0.50 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[CBY1]] | -0.49 | -0.32 / -0.44 | both halves | 2e-04 |  |
| [[RHBDF2]] | -0.49 | -0.45 / -0.38 | both halves | 7e-05 |  |
| [[DDX19A]] | -0.48 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[ANKS3]] | -0.47 | -0.45 / -0.37 | both halves | 7e-05 |  |
| [[PITPNA]] | -0.46 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[EVI5L]] | -0.46 | -0.37 / -0.28 | both halves | 3e-04 |  |
| [[ZBTB48]] | -0.46 | -0.42 / -0.29 | both halves | 3e-04 |  |
| [[SPG7]] | -0.46 | -0.48 / -0.39 | both halves | 5e-05 |  |
| [[CNOT10]] | -0.46 | -0.44 / -0.31 | both halves | 2e-04 |  |
| [[ZBED4]] | -0.46 | -0.43 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CD74]] | B | CD74 activity raises CCN3's level | lines that do not express CD74 (31) vs lines expressing it (19) | 1.66× lower at baseline in the lines without CD74 | 0.020 | ⚠ within organs, on part of the lines; also absent: HLA-DRA, SHROOM4, LAPTM5 |
| [[CPNE8]] | B | CPNE8 activity raises CCN3's level | lines that do not express CPNE8 (17) vs lines expressing it (33) | 1.59× lower at baseline in the lines without CPNE8 | 0.038 | ⚠ within organs, on part of the lines; also absent: NALCN, NT5E, MAP9 |
| [[AKR1B1]] | B | AKR1B1 activity raises CCN3's level | lines that do not express AKR1B1 (16) vs lines expressing it (34) | 2.05× lower at baseline in the lines without AKR1B1 | 0.044 | ⚠ within organs, on part of the lines; also absent: PTPRM, EHD3, SYNM |
| [[TOP2A]] | B | TOP2A activity lowers CCN3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SPOCK3]] | B | SPOCK3 activity raises CCN3's level | lines that do not express SPOCK3 (22) vs lines expressing it (28) | 2.12× lower at baseline in the lines without SPOCK3 | 0.060 | ⚠ within organs, on part of the lines; also absent: CTSF, NCAM2, LRP1B; maybe low, not absent |
| [[GPNMB]] | C | GPNMB activity raises CCN3's level | lines that do not express GPNMB (30) vs lines expressing it (20) | 2.65× lower at baseline in the lines without GPNMB | 0.012 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: IGFBP5, RUNX1T1, CNTN6; co-absent with the target |
| [[FYB1]] | C | FYB1 activity raises CCN3's level | lines that do not express FYB1 (32) vs lines expressing it (18) | 1.99× lower at baseline in the lines without FYB1 | 0.038 | ⚠ within organs, on part of the lines; also absent: AMPH, IRAG2, ENSG00000266450; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 6, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DDX46]] | B | CCN3 activity lowers DDX46's level | lines that do not express CCN3 (20) vs lines expressing it (30) | 1.25× higher at baseline in the lines without CCN3 | 0.019 | ⚠ within organs, on part of the lines; also absent: SNAI2, FAR2, ENSG00000228033 |
| [[MKLN1-AS]] | B | CCN3 activity lowers MKLN1-AS's level | lines that do not express CCN3 (20) vs lines expressing it (30) | 1.35× higher at baseline in the lines without CCN3 | 0.039 | ⚠ within organs, on part of the lines; also absent: SNAI2, FAR2, ENSG00000228033 |
| [[SPOCK3]] | B | CCN3 activity raises SPOCK3's level | lines that do not express CCN3 (20) vs lines expressing it (30) | 1.77× lower at baseline in the lines without CCN3 | 0.040 | ⚠ within organs, on part of the lines; also absent: SNAI2, FAR2, ENSG00000228033 |
| [[CD74]] | B | CCN3 activity raises CD74's level | lines that do not express CCN3 (20) vs lines expressing it (30) | 2.52× lower at baseline in the lines without CCN3 | 0.048 | ⚠ within organs, on part of the lines; also absent: SNAI2, FAR2, ENSG00000228033 |
| [[RAB38]] | B | CCN3 activity raises RAB38's level | lines that do not express CCN3 (20) vs lines expressing it (30) | 2.30× lower at baseline in the lines without CCN3 | 0.048 | ⚠ within organs, on part of the lines; also absent: SNAI2, FAR2, ENSG00000228033 |
| [[SYT9-AS1]] | B | CCN3 activity lowers SYT9-AS1's level | lines that do not express CCN3 (20) vs lines expressing it (30) | 1.49× higher at baseline in the lines without CCN3 | 0.060 | ⚠ within organs, on part of the lines; also absent: SNAI2, FAR2, ENSG00000228033 |
| [[LYPD1]] | C | CCN3 activity raises LYPD1's level | lines that do not express CCN3 (20) vs lines expressing it (30) | 2.26× lower at baseline in the lines without CCN3 | 0.035 | ⚠ within organs, on part of the lines; also absent: SNAI2, FAR2, ENSG00000228033; co-absent with the target |
| [[SLAMF7]] | C | CCN3 activity raises SLAMF7's level | lines that do not express CCN3 (20) vs lines expressing it (30) | 1.94× lower at baseline in the lines without CCN3 | 0.060 | ⚠ within organs, on part of the lines; also absent: SNAI2, FAR2, ENSG00000228033; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.425). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (33.2, 27.5); signed map (42.5, 16.8). **Vector** length 51.0, 10.9% of its response variance represented; |z| ≥ 3 in 565 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | +11.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.2 | +8.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.0 | +12.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +8.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.6 | +4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +5.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +3.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.7 | +4.4 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | +0.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.3 | -2.5 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.2 | -2.4 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.1 | -0.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.1 | -1.0 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.0 | -0.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.0 | -2.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.9 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | cellular communication network factor 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.12 — chr8:119,416,446-119,424,434 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IGFBP9; previously NOV |
| Gene groups (HGNC) | Cellular communication network factors |
| Matched by | ensembl_id |

**Function**, from UniProt [P48745](https://www.uniprot.org/uniprotkb/P48745) (CCN family member 3):

> Immediate-early protein playing a role in various cellular processes including proliferation, adhesion, migration, differentiation and survival. Acts by binding to integrins or membrane receptors such as NOTCH1. Essential regulator of hematopoietic stem and progenitor cell function. Inhibits myogenic differentiation through the activation of Notch-signaling pathway. Inhibits vascular smooth muscle cells proliferation by increasing expression of cell-cycle regulators such as CDKN2B or CDKN1A …

**Summary**, from NCBI Gene [4856](https://www.ncbi.nlm.nih.gov/gene/4856):

> The protein encoded by this gene is a small secreted cysteine-rich protein and a member of the CCN family of regulatory proteins. CNN family proteins associate with the extracellular matrix and play an important role in cardiovascular and skeletal development, fibrosis and cancer development. [provided by RefSeq, Feb 2009]

**Accessions** — [HGNC:7885](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7885) · Entrez [4856](https://www.ncbi.nlm.nih.gov/gene/4856) · UniProt [P48745](https://www.uniprot.org/uniprotkb/P48745) · Ensembl [ENSG00000136999](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136999)

## Data

Gene col 5955: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5955); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5955, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5955]; `tensor/DDL_lfc|DDL_z.npy` [5955]; `embed/gene_vectors.npy` [5955]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5955 or target_col == 5955). Every well: [[CCN3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCN3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
