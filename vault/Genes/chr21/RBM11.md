---
symbol: "RBM11"
type: "gene"
col: 11652
ensembl_id: "ENSG00000185272"
name: "RNA binding motif protein 11"
location: "21q11.2"
module: 115
arm: "+"
pooled_cpm: 2.2
n_lines_expressing: 25
n_dd_up: 32
n_dd_down: 0
n_dd_up_clean: 21
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 3
tags: ["gene", "module/115"]
generated_by: "tahoemap"
---

# RBM11

*RNA binding motif protein 11* — 21q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (11 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 3.05× (z +12.4, q 2e-32, up in 18 of 21 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (CFPAC-1 0.0467×, NCI-H1573 0.164×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H1573 0.156×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM241B]] (+0.64, fdr 1e-05), [[CYB5R1]] (+0.60, fdr 2e-05), [[SOGA3]] (+0.57, fdr 1e-05); moves opposite to [[PSKH1]] (-0.55, fdr 7e-05), [[TNRC18]] (-0.55, fdr 3e-05), [[ACAD9]] (-0.54, fdr 1e-04).
> It is in [[Module 115]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[SNX10]] → it (grade B ⚠); 3 go from it, the strongest it → [[SNX10]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11652.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **3.05×** | +12.4 | 2e-32 | 18/21 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **4.59×** | +12.0 | 2e-30 | 19/21 (NCI-H1573, HOP62, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **4.55×** | +11.9 | 2e-30 | 18/20 (HOP62, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **4.40×** | +11.0 | 7e-26 | 16/17 (HOP62, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.94×** | +10.8 | 6e-25 | 20/21 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.53×** | +9.9 | 4e-21 | 19/21 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.15×** | +9.0 | 2e-17 | 19/21 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.75×** | +7.9 | 2e-13 | 18/21 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.75×** | +7.6 | 2e-12 | 1/3 (NCI-H2347) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.42×** | +6.9 | 3e-10 | 17/18 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.83×** | +6.7 | 1e-09 | 6/21 (SW480, SK-MEL-2, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.50×** | +6.6 | 1e-09 | 0/5 | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.65×** | +5.4 | 2e-06 | 3/8 (A-427, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.04×** | +5.4 | 3e-06 | 5/13 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.93×** | +5.1 | 1e-05 | 1/11 (CFPAC-1) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.52×** | +4.6 | 1e-04 | 11/19 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.77×** | +4.4 | 3e-04 | 7/16 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.70×** | +4.2 | 9e-04 | 8/21 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **2.06×** | +4.0 | 0.001 | 8/20 (HOP62, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.69×** | +3.8 | 0.004 | 5/14 (HOP62, NCI-H23, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11652.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (CFPAC-1 0.0467×, NCI-H1573 0.164×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H1573 0.156×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.668× | -3.2 | 0.39 | 2/21 (C-33 A, Panc 03.27) | all doses, flat | position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | 0.670× | -3.2 | 0.39 | 6/22 (NCI-H1573, BT-474, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11652. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 14.8 | 2 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 5.49× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.164× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[HOP62 (line)]] | alt | 2.51 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 17.4× (z +9.1) | — |
| [[CFPAC-1 (line)]] | alt | 6.68 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0467× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[PANC-1 (line)]] | alt | 1.36 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 7.62× (z +8.8) | — |
| [[SW480 (line)]] | alt | 1.14 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 9.75× (z +9.1) | — |
| [[A-172 (line)]] | wt | 0.176 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.181 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.547 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.419 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.297 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.178 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 7.99 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.446 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.344 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.199 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.187 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.211 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.292 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.177 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.246 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.200 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.144 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.151 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.855 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.189 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.355 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.159 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.196 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.270 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.427 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.733 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.500 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.230 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11652), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM241B]] | +0.64 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[CYB5R1]] | +0.60 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[SOGA3]] | +0.57 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[RAB39A]] | +0.56 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[TTLL7]] | +0.56 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[MAPRE3]] | +0.55 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[CYP2J2]] | +0.55 | +0.33 / +0.68 | both halves | 1e-04 |  |
| [[GMPR]] | +0.54 | +0.31 / +0.55 | both halves | 2e-04 |  |
| [[TSPAN33]] | +0.54 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[RNF223]] | +0.53 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[DYNC1I1]] | +0.53 | +0.59 / +0.36 | both halves | 9e-05 |  |
| [[NDRG4]] | +0.53 | +0.53 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSKH1]] | -0.55 | -0.38 / -0.46 | both halves | 7e-05 |  |
| [[TNRC18]] | -0.55 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[ACAD9]] | -0.54 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[LAMTOR5-AS1]] | -0.52 | -0.32 / -0.45 | both halves | 2e-04 |  |
| [[DIDO1]] | -0.50 | -0.36 / -0.50 | both halves | 1e-04 |  |
| [[UBAP1L]] | -0.48 | -0.22 / -0.45 | both halves | 6e-04 |  |
| [[LEMD3]] | -0.48 | -0.33 / -0.41 | both halves | 1e-04 |  |
| [[CKMT2-AS1]] | -0.48 | -0.30 / -0.26 | both halves | 4e-04 |  |
| [[MSANTD2]] | -0.47 | -0.31 / -0.42 | both halves | 2e-04 |  |
| [[HNRNPUL1]] | -0.47 | -0.31 / -0.53 | both halves | 2e-04 |  |
| [[UBTF]] | -0.47 | -0.25 / -0.45 | both halves | 4e-04 |  |
| [[ANKMY1]] | -0.46 | -0.31 / -0.44 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SNX10]] | B | SNX10 activity raises RBM11's level | lines that do not express SNX10 (11) vs lines expressing it (39) | 2.15× lower at baseline in the lines without SNX10 | 0.053 | ⚠ within organs, on part of the lines; also absent: AP3B2, LRRC4B, CCDC144CP |
| [[PTAFR]] | B | PTAFR activity raises RBM11's level | lines that do not express PTAFR (29) vs lines expressing it (21) | 1.47× lower at baseline in the lines without PTAFR | 0.064 | ⚠ within organs, on part of the lines; also absent: TJP3, BSPRY, KDF1; maybe low, not absent |
| [[WIPF3]] | C | WIPF3 activity raises RBM11's level | lines that do not express WIPF3 (21) vs lines expressing it (29) | 2.21× lower at baseline in the lines without WIPF3 | 0.031 | ⚠ within organs, on part of the lines; also absent: RBM11, EPB41L4A, COL4A3; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SNX10]] | B | RBM11 activity raises SNX10's level | lines that do not express RBM11 (25) vs lines expressing it (25) | 1.84× lower at baseline in the lines without RBM11 | 0.016 | ⚠ within organs, on part of the lines; also absent: ENSG00000268119, ANKRD20A11P, VWDE |
| [[SGSM1]] | B | RBM11 activity raises SGSM1's level | lines that do not express RBM11 (25) vs lines expressing it (25) | 1.62× lower at baseline in the lines without RBM11 | 0.038 | ⚠ within organs, on part of the lines; also absent: ENSG00000268119, ANKRD20A11P, VWDE |
| [[CCNC]] | B | RBM11 activity raises CCNC's level | lines that do not express RBM11 (25) vs lines expressing it (25) | 1.06× lower at baseline in the lines without RBM11 | 0.091 | ⚠ within organs, on part of the lines; also absent: ENSG00000268119, ANKRD20A11P, VWDE |

## Where it sits

- **Module**: [[Module 115]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.525). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-3.3, 11.7); signed map (-19.2, 30.4). **Vector** length 46.8, 10.2% of its response variance represented; |z| ≥ 3 in 567 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +12.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.2 | +6.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.2 | +11.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.0 | +11.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.6 | +12.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.0 | +4.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.5 | +3.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.1 | +2.4 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -1.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -0.3 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.4 | -1.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.4 | -3.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.3 | -1.8 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.2 | -1.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.1 | -3.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.0 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | RNA binding motif protein 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q11.2 — chr21:14,216,130-14,228,372 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | RNA binding motif containing |
| Matched by | ensembl_id |

**Function**, from UniProt [P57052](https://www.uniprot.org/uniprotkb/P57052) (Splicing regulator RBM11):

> Tissue-specific splicing factor with potential implication in the regulation of alternative splicing during neuron and germ cell differentiation. Antagonizes SRSF1-mediated BCL-X splicing. May affect the choice of alternative 5' splice sites by binding to specific sequences in exons and antagonizing the SR protein SRSF1.

**Summary**, from NCBI Gene [54033](https://www.ncbi.nlm.nih.gov/gene/54033):

> Enables poly(U) RNA binding activity and protein homodimerization activity. Acts upstream of or within cellular response to oxidative stress and regulation of alternative mRNA splicing, via spliceosome. Located in nuclear speck. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:9897](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9897) · Entrez [54033](https://www.ncbi.nlm.nih.gov/gene/54033) · UniProt [P57052](https://www.uniprot.org/uniprotkb/P57052) · Ensembl [ENSG00000185272](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185272)

## Data

Gene col 11652: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11652); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11652, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11652]; `tensor/DDL_lfc|DDL_z.npy` [11652]; `embed/gene_vectors.npy` [11652]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11652 or target_col == 11652). Every well: [[RBM11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBM11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
