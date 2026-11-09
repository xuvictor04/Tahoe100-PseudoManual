---
symbol: "PAPLN"
type: "gene"
col: 2020
ensembl_id: "ENSG00000100767"
name: "papilin, proteoglycan like sulfated glycoprotein"
location: "14q24.2"
module: 61
arm: "+"
pooled_cpm: 5.32
n_lines_expressing: 34
n_dd_up: 14
n_dd_down: 4
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 5
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# PAPLN

*papilin, proteoglycan like sulfated glycoprotein* — 14q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.93× (z +11.1, q 1e-25, up in 7 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.608× (z -5.9, q 2e-06, down in 19 of 31 measured lines) ⚠ cell-cycle shift, explains ~49% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 7 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Harringtonine (drug)]] 5 µM in 2 lines (A-427 0.0579×, NCI-H2030 0.0696×; ⚠ cell-cycle shift, explains ~59% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A-427 0.117×, SK-MEL-2 0.146×; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 0.05 µM in 1 line (NCI-H2030 0.0612×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CPEB1]] (+0.62, fdr 1e-05), [[APH1B]] (+0.59, fdr 1e-05), [[APBB1]] (+0.56, fdr 1e-05); moves opposite to [[GSTCD]] (-0.45, fdr 2e-04), [[MTERF3]] (-0.45, fdr 1e-04), [[SLF1]] (-0.44, fdr 2e-04).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[RIPOR3]] → it (grade B ⚠); 5 go from it, the strongest it → [[LINC03002]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2020.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.93×** | +11.1 | 1e-25 | 7/27 (HEC-1-A, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.15×** | +8.6 | 2e-15 | 3/10 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.55×** | +7.4 | 2e-11 | 17/29 (SW480, HS-578T, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.86×** | +7.4 | 2e-11 | 10/29 (SW480, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.54×** | +7.2 | 6e-11 | 10/27 (LoVo, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.49×** | +6.8 | 1e-09 | 14/28 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.63×** | +5.8 | 4e-07 | 2/19 (A498, SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.58×** | +5.5 | 3e-06 | 15/28 (SW480, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.57×** | +5.3 | 6e-06 | 13/27 (J82, SW 900, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.50×** | +4.4 | 5e-04 | 1/14 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Rapamycin (drug)]] 5 µM |  | **1.25×** | +3.8 | 0.008 | 7/28 (A549, RPMI-7951, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.25×** | +3.6 | 0.012 | 9/29 (A-427, NCI-H2347, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.36×** | +3.6 | 0.012 | 7/29 (J82, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.33×** | +3.4 | 0.027 | 6/30 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2020.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 7 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Harringtonine (drug)]] 5 µM in 2 lines (A-427 0.0579×, NCI-H2030 0.0696×; ⚠ cell-cycle shift, explains ~59% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A-427 0.117×, SK-MEL-2 0.146×; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 0.05 µM in 1 line (NCI-H2030 0.0612×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.608×** | -5.9 | 2e-06 | 19/31 (PANC-1, NCI-H2030, …) | inconsistent across doses | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.663×** | -4.6 | 1e-03 | 13/29 (A-427, NCI-H2030, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.715×** | -4.0 | 0.012 | 9/29 (LOX-IMVI, A-427, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.738×** | -3.6 | 0.042 | 16/28 (PANC-1, NCI-H23, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 0.602× | -3.1 | 0.20 | 10/28 (NCI-H23, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2020. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 19.0 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.170× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 10.2 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 0.05 µM 0.0612× (z -12.3) |
| [[A-427 (line)]] | wt | 13.8 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0579× (z -15.4) ⚠ cell-cycle shift, explains ~59% of this change |
| [[LoVo (line)]] | wt | 2.64 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.00× (z +10.0) | — |
| [[NCI-H23 (line)]] | alt | 18.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.116× (z -11.3) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 12.1 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.146× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.985 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.920 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.32 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.79 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.42 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.778 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.761 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.844 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.05 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.21 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.851 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.700 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.795 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.49 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.956 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.23 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2020), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPEB1]] | +0.62 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[APH1B]] | +0.59 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[APBB1]] | +0.56 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[CCDC3]] | +0.56 | +0.57 / +0.43 | both halves | 3e-05 |  |
| [[JPH3]] | +0.56 | +0.40 / +0.52 | both halves | 4e-05 |  |
| [[FMN2]] | +0.55 | +0.50 / +0.46 | both halves | 2e-05 |  |
| [[ELFN1]] | +0.55 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[SNAP91]] | +0.55 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[RGS7]] | +0.53 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[RNLS]] | +0.51 | +0.54 / +0.41 | both halves | 4e-05 |  |
| [[ADGRB1]] | +0.51 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[CCDC144CP]] | +0.51 | +0.54 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GSTCD]] | -0.45 | -0.30 / -0.47 | both halves | 2e-04 |  |
| [[MTERF3]] | -0.45 | -0.43 / -0.36 | both halves | 1e-04 |  |
| [[SLF1]] | -0.44 | -0.31 / -0.45 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RIPOR3]] | B | RIPOR3 activity raises PAPLN's level | lines that do not express RIPOR3 (5) vs lines expressing it (45) | 2.50× lower at baseline in the lines without RIPOR3 | 0.008 | ⚠ within organs, on part of the lines; also absent: SYNPO2, PER3, ENSG00000274265; maybe low, not absent |
| [[CCDC3]] | B | CCDC3 activity raises PAPLN's level | lines that do not express CCDC3 (6) vs lines expressing it (44) | 2.58× lower at baseline in the lines without CCDC3 | 0.030 | ⚠ within organs, on part of the lines; also absent: KLHL5, RIPOR3, SLC36A4; maybe low, not absent |
| [[LHFPL4]] | B | LHFPL4 activity raises PAPLN's level | lines that do not express LHFPL4 (33) vs lines expressing it (17) | 2.36× lower at baseline in the lines without LHFPL4 | 0.089 | ⚠ within organs, on part of the lines; also absent: SLC6A11, INA, ENSG00000251652 |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC03002]] | B | PAPLN activity lowers LINC03002's level | lines that do not express PAPLN (16) vs lines expressing it (34) | 1.42× higher at baseline in the lines without PAPLN | 0.021 | ⚠ within organs, on part of the lines; also absent: BEX2, AFAP1L1, BEX4; maybe low, not absent |
| [[CCDC3]] | B | PAPLN activity raises CCDC3's level | lines that do not express PAPLN (16) vs lines expressing it (34) | 1.83× lower at baseline in the lines without PAPLN | 0.027 | ⚠ within organs, on part of the lines; also absent: BEX2, AFAP1L1, BEX4; maybe low, not absent |
| [[ARL14EP-DT]] | B | PAPLN activity lowers ARL14EP-DT's level | lines that do not express PAPLN (16) vs lines expressing it (34) | 1.19× higher at baseline in the lines without PAPLN | 0.080 | ⚠ within organs, on part of the lines; also absent: BEX2, AFAP1L1, BEX4; maybe low, not absent |
| [[FSIP1]] | B | PAPLN activity raises FSIP1's level | lines that do not express PAPLN (16) vs lines expressing it (34) | 1.65× lower at baseline in the lines without PAPLN | 0.092 | ⚠ within organs, on part of the lines; also absent: BEX2, AFAP1L1, BEX4; maybe low, not absent |
| [[SYNPO2]] | B | PAPLN activity raises SYNPO2's level | lines that do not express PAPLN (16) vs lines expressing it (34) | 2.13× lower at baseline in the lines without PAPLN | 0.099 | ⚠ within organs, on part of the lines; also absent: BEX2, AFAP1L1, BEX4; maybe low, not absent |

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.513). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.7, 36.2); signed map (24.2, 20.5). **Vector** length 49.4, 8.62% of its response variance represented; |z| ≥ 3 in 656 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.1 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.5 | +5.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.3 | +7.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.0 | +4.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.0 | +7.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +7.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +2.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.4 | +1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +1.6 |
| fall | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.2 | +0.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | -1.1 | -3.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.1 | -2.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.1 | -2.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.0 | -1.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.0 | -1.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.0 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | papilin, proteoglycan like sulfated glycoprotein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.2 — chr14:73,237,497-73,274,640 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC50452 |
| Gene groups (HGNC) | I-set domain containing; ADAMTS like |
| Matched by | ensembl_id |

UniProt [O95428](https://www.uniprot.org/uniprotkb/O95428) carries no function annotation.

**Summary**, from NCBI Gene [89932](https://www.ncbi.nlm.nih.gov/gene/89932):

> Predicted to enable serine-type endopeptidase inhibitor activity. Predicted to be involved in extracellular matrix organization and nervous system development. Predicted to be located in basement membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19262](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19262) · Entrez [89932](https://www.ncbi.nlm.nih.gov/gene/89932) · UniProt [O95428](https://www.uniprot.org/uniprotkb/O95428) · Ensembl [ENSG00000100767](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100767)

## Data

Gene col 2020: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2020); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2020, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2020]; `tensor/DDL_lfc|DDL_z.npy` [2020]; `embed/gene_vectors.npy` [2020]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2020 or target_col == 2020). Every well: [[PAPLN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PAPLN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
