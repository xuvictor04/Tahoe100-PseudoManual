---
symbol: "RHEBL1"
type: "gene"
col: 9486
ensembl_id: "ENSG00000167550"
name: "RHEB like 1"
location: "12q13.12"
module: 69
arm: "+"
pooled_cpm: 6.32
n_lines_expressing: 49
n_dd_up: 17
n_dd_down: 4
n_dd_up_clean: 5
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# RHEBL1

*RHEB like 1* — 12q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (12 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 3.31× (z +8.6, q 5e-15, up in 31 of 37 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.17× (z +7.8, q 9e-13, up in 32 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.348× (z -7.6, q 1e-11, down in 33 of 46 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.346× (z -4.0, q 0.015, down in 19 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CNNM2]] (+0.66, fdr 1e-05), [[HACL1]] (+0.64, fdr 2e-05), [[SRP54-AS1]] (+0.63, fdr 7e-06); moves opposite to [[TAF2]] (-0.65, fdr 7e-06), [[DNAJC11]] (-0.65, fdr 1e-05), [[PTPN11]] (-0.65, fdr 1e-05).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MICB]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 12 with an alert ⚠; shown: the 15 strongest. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9486.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **3.31×** | +8.6 | 5e-15 | 31/37 (NCI-H460, PANC-1, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.15×** | +7.9 | 6e-13 | 26/28 (LoVo, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.17×** | +7.8 | 9e-13 | 32/40 (NCI-H2347, LoVo, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **2.50×** | +6.6 | 7e-09 | 29/46 (SW480, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **2.38×** | +6.2 | 6e-08 | 30/46 (SW480, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **2.29×** | +5.9 | 3e-07 | 29/46 (SW480, RKO, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.79×** | +5.9 | 3e-07 | 22/39 (NCI-H460, SW1417, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **2.24×** | +5.8 | 6e-07 | 25/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.08×** | +5.1 | 3e-05 | 21/40 (A-427, NCI-H23, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.02×** | +4.8 | 8e-05 | 15/33 (A-427, LOX-IMVI, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **1.90×** | +4.4 | 5e-04 | 13/33 (NCI-H460, J82, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.75×** | +4.0 | 0.003 | 19/45 (J82, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.63×** | +3.5 | 0.020 | 15/39 (NCI-H23, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Retinoic acid (drug)]] 5 µM |  | **1.41×** | +3.4 | 0.025 | 16/46 (Panc 03.27, NCI-H23, …) | all doses, stronger at high dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.54×** | +3.1 | 0.073 | 16/45 (A-427, PANC-1, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9486.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.348×** | -7.6 | 1e-11 | 33/46 (NCI-H460, HS-578T, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.346×** | -4.0 | 0.015 | 19/41 (A-172, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | **0.582×** | -3.9 | 0.015 | 14/46 (HEC-1-A, Panc 03.27, …) | top dose only |  |
| [[Tirabrutinib (drug)]] 0.5 µM |  | **0.619×** | -3.5 | 0.066 | 13/46 (NCI-H460, LS 180, …) | inconsistent across doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.656× | -3.1 | 0.24 | 11/46 (HCT15, NCI-H2347, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.52 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9486. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 18.8 | 6 (6 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 23.9× (z +15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.129× (z -9.8) ⚠ unreliable plate only |
| [[HS-578T (line)]] | alt | 7.01 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0568× (z -9.6) ⚠ unreliable plate only |
| [[LS 180 (line)]] | wt | 8.86 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 19.7× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[PANC-1 (line)]] | alt | 6.55 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 8.01× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[SHP-77 (line)]] | alt | 10.1 | 0 | 1 | — | [[Sulfisoxazole (drug)]] 0.5 µM 0.0822× (z -9.3) |
| [[A-172 (line)]] | wt | 8.40 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.98 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.62 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.49 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.69 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.55 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.64 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.21 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.17 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.67 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.18 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.08 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.89 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9486), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNNM2]] | +0.66 | +0.51 / +0.70 | both halves | 1e-05 |  |
| [[HACL1]] | +0.64 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[SRP54-AS1]] | +0.63 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[ELF2]] | +0.63 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[ELP2]] | +0.63 | +0.57 / +0.58 | both halves | 9e-06 |  |
| [[TBC1D22A-DT]] | +0.63 | +0.47 / +0.68 | both halves | 2e-05 |  |
| [[LMBR1L]] | +0.63 | +0.51 / +0.64 | both halves | 1e-05 | ⚠ same locus (27.1 kb, same strand: neighbours can correlate without regulation) |
| [[MAX]] | +0.63 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[TAF5]] | +0.63 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[STK32C]] | +0.62 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[ANKRD37]] | +0.62 | +0.46 / +0.68 | both halves | 3e-05 |  |
| [[GNRH1]] | +0.61 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[LINC01881]] | +0.61 | +0.47 / +0.61 | both halves | 2e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAF2]] | -0.65 | -0.58 / -0.67 | both halves | 7e-06 |  |
| [[DNAJC11]] | -0.65 | -0.55 / -0.68 | both halves | 1e-05 |  |
| [[PTPN11]] | -0.65 | -0.50 / -0.66 | both halves | 1e-05 |  |
| [[EIF4G1]] | -0.63 | -0.52 / -0.64 | both halves | 1e-05 |  |
| [[ZNF655]] | -0.61 | -0.47 / -0.63 | both halves | 2e-05 |  |
| [[EIF2S1]] | -0.61 | -0.56 / -0.63 | both halves | 1e-05 |  |
| [[COMMD10]] | -0.60 | -0.54 / -0.61 | both halves | 1e-05 |  |
| [[RBM12]] | -0.59 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[UTP20]] | -0.59 | -0.46 / -0.62 | both halves | 3e-05 |  |
| [[MGA]] | -0.58 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[DPP8]] | -0.58 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[SNX19]] | -0.58 | -0.52 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MICB]] | B | MICB activity raises RHEBL1's level | lines that do not express MICB (13) vs lines expressing it (37) | 1.65× lower at baseline in the lines without MICB | 0.028 | ⚠ within organs, on part of the lines; also absent: SPHK1, ENSG00000234405, MYL9 |
| [[PAX6]] | B | PAX6 activity raises RHEBL1's level | lines that do not express PAX6 (30) vs lines expressing it (20) | 1.48× lower at baseline in the lines without PAX6 | 0.037 | ⚠ within organs, on part of the lines; also absent: LINC02643, WT1-AS, CHRDL1 |
| [[TOP2A]] | B | TOP2A activity lowers RHEBL1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.514). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (1.5, -39.9); signed map (-41.2, 13.3). **Vector** length 76.9, 15.6% of its response variance represented; |z| ≥ 3 in 838 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.5 | +7.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.4 | +7.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +2.3 | +4.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +1.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.0 | +2.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.0 | +2.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.5 | +1.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.8 | -7.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.8 | -4.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | -0.5 |
|  | [[EX229 (drug)]] 5 µM |  | -3.6 | -2.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | +0.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.3 | -2.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.9 | -2.7 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.7 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | RHEB like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.12 — chr12:49,064,676-49,070,025 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC34869, FLJ25797, RHEB2 |
| Gene groups (HGNC) | RAS type GTPase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TAI7](https://www.uniprot.org/uniprotkb/Q8TAI7) (GTPase RhebL1):

> Binds GTP and exhibits intrinsic GTPase activity (By similarity). May activate NF-kappa-B-mediated gene transcription. Promotes signal transduction through MTOR, activates RPS6KB1, and is a downstream target of the small GTPase-activating proteins TSC1 and TSC2.

**Summary**, from NCBI Gene [121268](https://www.ncbi.nlm.nih.gov/gene/121268):

> Enables GTP binding activity. Involved in TOR signaling. Located in cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21166](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21166) · Entrez [121268](https://www.ncbi.nlm.nih.gov/gene/121268) · UniProt [Q8TAI7](https://www.uniprot.org/uniprotkb/Q8TAI7) · Ensembl [ENSG00000167550](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167550)

## Data

Gene col 9486: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9486); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9486, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9486]; `tensor/DDL_lfc|DDL_z.npy` [9486]; `embed/gene_vectors.npy` [9486]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9486 or target_col == 9486). Every well: [[RHEBL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RHEBL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
