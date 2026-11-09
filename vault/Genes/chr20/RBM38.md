---
symbol: "RBM38"
type: "gene"
col: 5375
ensembl_id: "ENSG00000132819"
name: "RNA binding motif protein 38"
location: "20q13.31"
module: 215
arm: "+"
pooled_cpm: 10.7
n_lines_expressing: 49
n_dd_up: 22
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/215"]
generated_by: "tahoemap"
---

# RBM38

*RNA binding motif protein 38* — 20q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.40× (z +14.3, q 2e-43, up in 46 of 46 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2030 0.118×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (Hs 766T 0.0970×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (CFPAC-1 0.120×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Cobimetinib (drug)]] 5 µM in 1 line (SK-MEL-2 0.0806×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RALGDS]] (+0.72, fdr 5e-05), [[CDC34]] (+0.69, fdr 1e-05), [[ARID3A]] (+0.65, fdr 3e-05); moves opposite to [[PUS7L]] (-0.67, fdr 1e-04), [[MBTPS2]] (-0.66, fdr 3e-05), [[UCHL5]] (-0.63, fdr 2e-05).
> It is in [[Module 215]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[HES6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5375.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.40×** | +14.3 | 2e-43 | 46/46 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.01×** | +12.9 | 2e-35 | 43/46 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.10×** | +12.2 | 6e-32 | 33/43 (A549, A498, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.47×** | +10.5 | 8e-24 | 38/46 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.63×** | +8.1 | 8e-14 | 26/44 (A498, HOP62, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.70×** | +6.2 | 7e-08 | 26/43 (NCI-H460, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +6.1 | 8e-08 | 27/47 (Hs 766T, HOP62, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.72×** | +6.1 | 8e-08 | 18/36 (A498, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **1.53×** | +5.0 | 4e-05 | 19/39 (J82, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.94×** | +4.5 | 3e-04 | 14/40 (LoVo, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | **1.41×** | +3.8 | 0.008 | 16/38 (HepG2/C3A, PANC-1, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.63×** | +3.3 | 0.035 | 8/43 (COLO 205, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.37×** | +3.3 | 0.035 | 11/42 (NCI-H2030, SW 900, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.35×** | +3.3 | 0.035 | 15/44 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.61×** | +3.3 | 0.040 | 8/40 (LoVo, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.35×** | +3.2 | 0.046 | 7/42 (SHP-77, NCI-H2030, …) | inconsistent across doses |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.30×** | +3.0 | 0.066 | 10/45 (NCI-H23, NCI-H2030, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5375.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2030 0.118×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (Hs 766T 0.0970×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (CFPAC-1 0.120×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Cobimetinib (drug)]] 5 µM in 1 line (SK-MEL-2 0.0806×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.747× | -3.2 | 0.55 | 4/47 (SW 1088, J82, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5375. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 17.0 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.31× (z +12.5) | — |
| [[A498 (line)]] | wt | 8.11 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.48× (z +11.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.51× (z +10.3) | — |
| [[Hs 766T (line)]] | wt | 8.88 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 8.05× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.0970× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 6.32 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.35× (z +10.2) | — |
| [[PANC-1 (line)]] | alt | 7.28 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.49× (z +9.9) | — |
| [[SW1417 (line)]] | alt | 24.9 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.96× (z +11.1) | — |
| [[A549 (line)]] | wt | 6.02 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.55× (z +11.4) | — |
| [[C-33 A (line)]] | alt | 15.9 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.131× (z -8.8) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 6.39 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.120× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 4.51 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.92× (z +9.3) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[KATO III (line)]] | alt | 14.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.64× (z +8.6) | — |
| [[NCI-H2030 (line)]] | alt | 14.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.118× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 7.38 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0806× (z -9.2) |
| [[A-172 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.13 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.73 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.10 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.45 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.19 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.78 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.76 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.70 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.43 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.18 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.88 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5375), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RALGDS]] | +0.72 | +0.39 / +0.78 | both halves | 5e-05 |  |
| [[CDC34]] | +0.69 | +0.51 / +0.70 | both halves | 1e-05 | STRING 485 |
| [[ARID3A]] | +0.65 | +0.44 / +0.71 | both halves | 3e-05 |  |
| [[PRKCD]] | +0.65 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[METRNL]] | +0.64 | +0.57 / +0.63 | both halves | 9e-06 |  |
| [[DGAT1]] | +0.63 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[CNNM4]] | +0.62 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[HIC2]] | +0.62 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[ZBTB7A]] | +0.61 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[PPP1R13B]] | +0.61 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[BCORL1]] | +0.61 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[FGFR3]] | +0.60 | +0.60 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PUS7L]] | -0.67 | -0.35 / -0.77 | both halves | 1e-04 |  |
| [[MBTPS2]] | -0.66 | -0.44 / -0.72 | both halves | 3e-05 |  |
| [[UCHL5]] | -0.63 | -0.48 / -0.60 | both halves | 2e-05 |  |
| [[MTMR2]] | -0.62 | -0.49 / -0.63 | both halves | 1e-05 |  |
| [[SRP9]] | -0.60 | -0.43 / -0.68 | both halves | 3e-05 |  |
| [[PDAP1]] | -0.60 | -0.36 / -0.61 | both halves | 1e-04 |  |
| [[XRCC5]] | -0.60 | -0.41 / -0.64 | both halves | 4e-05 |  |
| [[UBQLN1]] | -0.60 | -0.49 / -0.63 | both halves | 1e-05 |  |
| [[IPO8]] | -0.59 | -0.43 / -0.65 | both halves | 3e-05 |  |
| [[ATP5PB]] | -0.59 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[CAPRIN1]] | -0.58 | -0.36 / -0.66 | both halves | 9e-05 |  |
| [[XRCC6]] | -0.58 | -0.45 / -0.61 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HES6]] | B | HES6 activity raises RBM38's level | lines that do not express HES6 (8) vs lines expressing it (42) | 1.83× lower at baseline in the lines without HES6 | 0.026 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[JAG2]] | B | JAG2 activity raises RBM38's level | lines that do not express JAG2 (10) vs lines expressing it (40) | 1.90× lower at baseline in the lines without JAG2 | 0.037 | ⚠ within organs, on part of the lines; also absent: CRACD, RHPN1, PTP4A3; maybe low, not absent |
| [[CAMSAP3]] | B | CAMSAP3 activity raises RBM38's level | lines that do not express CAMSAP3 (16) vs lines expressing it (34) | 1.90× lower at baseline in the lines without CAMSAP3 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: CGN, FGFR4, UNC5A; maybe low, not absent |
| [[SBK1]] | B | SBK1 activity raises RBM38's level | lines that do not express SBK1 (16) vs lines expressing it (34) | 1.83× lower at baseline in the lines without SBK1 | 0.093 | ⚠ within organs, on part of the lines; also absent: CASZ1, LAMP3, CAMSAP3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 215]]; 13 genes; every member is in the + arm (projection on the module's main direction -0.711). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-33.5, -25.6); signed map (-27.1, 15.4). **Vector** length 72.9, 14.4% of its response variance represented; |z| ≥ 3 in 751 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +6.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.8 | +4.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.4 | +12.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.3 | +14.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | +2.8 | +6.2 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.4 | +2.6 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.3 | +3.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.2 | +2.3 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -1.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.0 | -0.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -0.6 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.9 | -3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -2.8 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.9 | -2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.9 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | RNA binding motif protein 38 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.31 — chr20:57,391,396-57,409,333 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSRNASEB, SEB4D, seb4B, dJ800J21.2; previously RNPC1 |
| Gene groups (HGNC) | RNA binding motif containing |
| Hallmark sets | HEME_METABOLISM |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H0Z9](https://www.uniprot.org/uniprotkb/Q9H0Z9) (RNA-binding protein 38):

> RNA-binding protein that specifically bind the 3'-UTR of CDKN1A transcripts, leading to maintain the stability of CDKN1A transcripts, thereby acting as a mediator of the p53/TP53 family to regulate CDKN1A. CDKN1A is a cyclin-dependent kinase inhibitor transcriptionally regulated by the p53/TP53 family to induce cell cycle arrest. Isoform 1, but not isoform 2, has the ability to induce cell cycle arrest in G1 and maintain the stability of CDKN1A transcripts induced by p53/TP53. Also acts as a …

**Summary**, from NCBI Gene [55544](https://www.ncbi.nlm.nih.gov/gene/55544):

> Enables mRNA 3'-UTR binding activity. Involved in several processes, including DNA damage response, signal transduction by p53 class mediator; negative regulation of cell population proliferation; and regulation of gene expression. Located in cytosol and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:15818](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15818) · Entrez [55544](https://www.ncbi.nlm.nih.gov/gene/55544) · UniProt [Q9H0Z9](https://www.uniprot.org/uniprotkb/Q9H0Z9) · Ensembl [ENSG00000132819](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132819)

## Data

Gene col 5375: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5375); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5375, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5375]; `tensor/DDL_lfc|DDL_z.npy` [5375]; `embed/gene_vectors.npy` [5375]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5375 or target_col == 5375). Every well: [[RBM38 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBM38.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
