---
symbol: "CKMT1B"
type: "gene"
col: 14123
ensembl_id: "ENSG00000237289"
name: "creatine kinase, mitochondrial 1B"
location: "15q15.3"
module: 44
arm: "+"
pooled_cpm: 2.23
n_lines_expressing: 22
n_dd_up: 28
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 15
direction_downstream: 43
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# CKMT1B

*creatine kinase, mitochondrial 1B* — 15q15.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (16 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 7.42× (z +12.3, q 5e-32, up in 1 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 2.45× (z +8.1, q 9e-14, up in 14 of 18 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (LoVo 0.0683×, KATO III 0.164×, LS 180 0.113×; ⚠ cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (COLO 205 0.0564×; ⚠ cell-cycle shift, explains ~26% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CKMT1A]] (+0.96, fdr 7e-06), [[PPP1R1B]] (+0.71, fdr 7e-06), [[MUC3A]] (+0.70, fdr 7e-06); moves opposite to [[PPP1R3F]] (-0.50, fdr 5e-05), [[BRD1]] (-0.50, fdr 7e-05), [[MCPH1-AS1]] (-0.50, fdr 7e-05).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[LMTK3]] → it (grade B ⚠); 43 go from it, the strongest it → [[FGFR4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 16 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14123.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **7.42×** | +12.3 | 5e-32 | 1/3 (KATO III) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.83×** | +10.0 | 3e-21 | 6/8 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.97×** | +8.1 | 8e-14 | 2/5 (LoVo, KATO III) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **2.45×** | +8.1 | 9e-14 | 14/18 (NCI-H23, KATO III, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **3.29×** | +7.6 | 4e-12 | 10/19 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.88×** | +6.7 | 2e-09 | 9/18 (SW480, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.82×** | +6.6 | 3e-09 | 9/18 (SW480, NCI-H2347, …) | all doses, stronger at high dose | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.76×** | +5.1 | 2e-05 | 7/18 (HT-29, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.14×** | +4.7 | 2e-04 | 3/11 (NCI-H1573, LoVo, …) | top dose only | cell-cycle shift (explains ~20% here); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.94×** | +4.6 | 3e-04 | 0/4 | top dose only | noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.10×** | +4.5 | 3e-04 | 4/10 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.00×** | +4.4 | 5e-04 | 9/19 (SK-MEL-2, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.91×** | +4.3 | 7e-04 | 1/8 (KATO III) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.92×** | +4.2 | 0.001 | 2/10 (SW480, A-427) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.49×** | +3.6 | 0.012 | 1/13 (BT-474) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.42×** | +3.6 | 0.012 | 2/10 (SHP-77, NCI-H23) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.67×** | +3.3 | 0.033 | 5/18 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.66×** | +3.2 | 0.036 | 0/18 | top dose only | cell-cycle shift (explains ~12% here) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.63×** | +3.1 | 0.049 | 2/12 (COLO 205, SW480) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.63×** | +3.1 | 0.049 | 3/14 (A-427, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.62×** | +3.1 | 0.051 | 0/12 | inconsistent across doses | low cells (technical?); position effect removed |
| [[Bendamustine (drug)]] 5 µM |  | **1.64×** | +3.0 | 0.060 | 1/14 (SW480) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.59×** | +2.9 | 0.073 | 7/18 (A-427, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.57×** | +2.9 | 0.088 | 1/12 (NCI-H2347) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14123.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (LoVo 0.0683×, KATO III 0.164×, LS 180 0.113×; ⚠ cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (COLO 205 0.0564×; ⚠ cell-cycle shift, explains ~26% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[BAY1125976 (drug)]] 5 µM |  | 0.388× | -3.2 | 0.59 | 6/18 (BT-474, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.619× | -3.1 | 0.59 | 3/19 (SK-MEL-2, NCI-H23, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.52 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14123. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 10.1 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0564× (z -10.4) ⚠ cell-cycle shift, explains ~26% of this change |
| [[KATO III (line)]] | alt | 15.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -12.1) ⚠ cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 7.71 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0683× (z -15.7) ⚠ cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 5.56 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -11.2) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 0.179 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.83 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.144 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.363 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.368 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.213 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.224 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.228 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.232 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.206 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.282 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.270 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.244 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.212 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.176 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.174 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.219 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.151 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.210 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.344 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.186 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.84 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.534 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.281 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.242 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.618 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.213 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.218 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.397 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.236 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.445 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 9.31 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.30 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.47 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14123), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CKMT1A]] | +0.96 | +0.93 / +0.93 | both halves | 7e-06 | same gene group; STRING 999 |
| [[PPP1R1B]] | +0.71 | +0.72 / +0.62 | both halves | 7e-06 |  |
| [[MUC3A]] | +0.70 | +0.72 / +0.59 | both halves | 7e-06 |  |
| [[FGFR4]] | +0.66 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[RAB25]] | +0.66 | +0.69 / +0.48 | both halves | 2e-05 |  |
| [[CYP4F12]] | +0.65 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[PCK1]] | +0.64 | +0.69 / +0.40 | both halves | 5e-05 |  |
| [[CLDN3]] | +0.63 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[ST6GALNAC1]] | +0.63 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[KLK7]] | +0.61 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[GPA33]] | +0.61 | +0.65 / +0.47 | both halves | 2e-05 |  |
| [[SLC27A2]] | +0.61 | +0.62 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R3F]] | -0.50 | -0.39 / -0.45 | both halves | 5e-05 |  |
| [[BRD1]] | -0.50 | -0.38 / -0.44 | both halves | 7e-05 |  |
| [[MCPH1-AS1]] | -0.50 | -0.39 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 1, C 14. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LMTK3]] | B | LMTK3 activity raises CKMT1B's level | lines that do not express LMTK3 (15) vs lines expressing it (35) | 2.14× lower at baseline in the lines without LMTK3 | 0.055 | ⚠ within organs, on part of the lines; also absent: CRYBG2, CXADR, CCDC120; maybe low, not absent |
| [[CKMT1A]] | C | CKMT1A activity raises CKMT1B's level | lines that do not express CKMT1A (28) vs lines expressing it (22) | 3.38× lower at baseline in the lines without CKMT1A | 4e-04 | ⚠ within organs, on part of the lines; also absent: CKMT1B, CLDN7, EPCAM; co-absent with the target |
| [[BSPRY]] | C | BSPRY activity raises CKMT1B's level | lines that do not express BSPRY (29) vs lines expressing it (21) | 3.02× lower at baseline in the lines without BSPRY | 0.003 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPCAM, RAB25; co-absent with the target |
| [[DMKN]] | C | DMKN activity raises CKMT1B's level | lines that do not express DMKN (24) vs lines expressing it (26) | 2.41× lower at baseline in the lines without DMKN | 0.011 | ⚠ within organs, on part of the lines; also absent: SPINT1, BSPRY, SMPDL3B; co-absent with the target |
| [[SMPDL3B]] | C | SMPDL3B activity raises CKMT1B's level | lines that do not express SMPDL3B (23) vs lines expressing it (27) | 2.48× lower at baseline in the lines without SMPDL3B | 0.014 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HOOK1, BSPRY, SPINT1-AS1; co-absent with the target |
| [[EPCAM]] | C | EPCAM activity raises CKMT1B's level | lines that do not express EPCAM (28) vs lines expressing it (22) | 2.72× lower at baseline in the lines without EPCAM | 0.017 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, KDF1, CLDN3; co-absent with the target |
| [[MUC3A]] | C | MUC3A activity raises CKMT1B's level | lines that do not express MUC3A (25) vs lines expressing it (25) | 2.49× lower at baseline in the lines without MUC3A | 0.020 | ⚠ within organs, on part of the lines; also absent: HSH2D, ADGRF1, CKMT1B; co-absent with the target |
| [[PPP1R1B]] | C | PPP1R1B activity raises CKMT1B's level | lines that do not express PPP1R1B (37) vs lines expressing it (13) | 3.17× lower at baseline in the lines without PPP1R1B | 0.022 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CEACAM5, NPSR1, CDH17; co-absent with the target |
| [[HSD11B2]] | C | HSD11B2 activity raises CKMT1B's level | lines that do not express HSD11B2 (16) vs lines expressing it (34) | 2.26× lower at baseline in the lines without HSD11B2 | 0.036 | ⚠ within organs, on part of the lines; also absent: MCF2L, CHDH, IL17RB; maybe low, not absent; co-absent with the target |
| [[TJP3]] | C | TJP3 activity raises CKMT1B's level | lines that do not express TJP3 (29) vs lines expressing it (21) | 2.43× lower at baseline in the lines without TJP3 | 0.044 | ⚠ within organs, on part of the lines; also absent: KDF1, EPCAM, CDH1; co-absent with the target |
| [[CLDN3]] | C | CLDN3 activity raises CKMT1B's level | lines that do not express CLDN3 (28) vs lines expressing it (22) | 2.70× lower at baseline in the lines without CLDN3 | 0.049 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, ESRP1; co-absent with the target |
| [[PIK3AP1]] | C | PIK3AP1 activity raises CKMT1B's level | lines that do not express PIK3AP1 (28) vs lines expressing it (22) | 2.14× lower at baseline in the lines without PIK3AP1 | 0.074 | ⚠ within organs, on part of the lines; also absent: HNF4A, EPS8L3, TMEM139; co-absent with the target |

### Downstream of this gene

*43 arrows, 43 of them with an alert ⚠; grade A 0, B 18, C 25. Shown: the 12 strongest; 31 more arrows (31 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FGFR4]] | B | CKMT1B activity raises FGFR4's level | lines that do not express CKMT1B (28) vs lines expressing it (22) | 1.94× lower at baseline in the lines without CKMT1B | 0.003 | ⚠ within organs, on part of the lines; also absent: CKMT1A, SYK, PPP1R1B |
| [[HDHD3]] | B | CKMT1B activity raises HDHD3's level | lines that do not express CKMT1B (28) vs lines expressing it (22) | 1.76× lower at baseline in the lines without CKMT1B | 0.026 | ⚠ within organs, on part of the lines; also absent: CKMT1A, SYK, PPP1R1B |
| cells under [[Clofarabine (drug)]] 0.5 µM | B | CKMT1B activity raises the cells' numbers under Clofarabine 0.5 µM (protects the cells) | lines that do not express CKMT1B (28) vs lines expressing it (20) | the lines without CKMT1B: 0.83× the cells of the other lines | 0.070 | ⚠ within organs, on part of the lines; also absent: CKMT1A, SYK, PPP1R1B |
| [[CYP2J2]] | B | CKMT1B activity raises CYP2J2's level | lines that do not express CKMT1B (28) vs lines expressing it (22) | 1.91× lower at baseline in the lines without CKMT1B | 0.071 | ⚠ within organs, on part of the lines; also absent: CKMT1A, SYK, PPP1R1B |
| cells under [[Penfluridol (drug)]] 0.5 µM | B | CKMT1B activity raises the cells' numbers under Penfluridol 0.5 µM (protects the cells) | lines that do not express CKMT1B (28) vs lines expressing it (20) | the lines without CKMT1B: 0.75× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: CKMT1A, SYK, PPP1R1B |
| cells under [[Sulfatinib (drug)]] 0.5 µM | B | CKMT1B activity raises the cells' numbers under Sulfatinib 0.5 µM (protects the cells) | lines that do not express CKMT1B (28) vs lines expressing it (20) | the lines without CKMT1B: 0.84× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; also absent: CKMT1A, SYK, PPP1R1B |
| [[CISD3]] | B | CKMT1B activity raises CISD3's level | lines that do not express CKMT1B (28) vs lines expressing it (22) | 1.45× lower at baseline in the lines without CKMT1B | 0.077 | ⚠ within organs, on part of the lines; also absent: CKMT1A, SYK, PPP1R1B |
| [[PLS1]] | B | CKMT1B activity raises PLS1's level | lines that do not express CKMT1B (28) vs lines expressing it (22) | 3.03× lower at baseline in the lines without CKMT1B | 0.080 | ⚠ within organs, on part of the lines; also absent: CKMT1A, SYK, PPP1R1B |
| [[LMTK3]] | B | CKMT1B activity raises LMTK3's level | lines that do not express CKMT1B (28) vs lines expressing it (22) | 2.44× lower at baseline in the lines without CKMT1B | 0.087 | ⚠ within organs, on part of the lines; also absent: CKMT1A, SYK, PPP1R1B |
| cells under [[Clopidogrel (drug)]] 0.05 µM | B | CKMT1B activity lowers the cells' numbers under Clopidogrel 0.05 µM (makes them more sensitive) | lines that do not express CKMT1B (28) vs lines expressing it (20) | the lines without CKMT1B: 1.24× the cells of the other lines | 0.088 | ⚠ within organs, on part of the lines; also absent: CKMT1A, SYK, PPP1R1B |
| cells under [[9-ING-41 (drug)]] 0.05 µM | B | CKMT1B activity lowers the cells' numbers under 9-ING-41 0.05 µM (makes them more sensitive) | lines that do not express CKMT1B (28) vs lines expressing it (20) | the lines without CKMT1B: 1.17× the cells of the other lines | 0.088 | ⚠ within organs, on part of the lines; also absent: CKMT1A, SYK, PPP1R1B |
| cells under [[Dihydroartemisinin (drug)]] 5 µM | B | CKMT1B activity raises the cells' numbers under Dihydroartemisinin 5 µM (protects the cells) | lines that do not express CKMT1B (28) vs lines expressing it (20) | the lines without CKMT1B: 0.76× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: CKMT1A, SYK, PPP1R1B |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.682). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.4, 52.2); signed map (64.5, 5.9). **Vector** length 36.3, 7.94% of its response variance represented; |z| ≥ 3 in 373 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Defective GALNT12 causes CRCS1* (reactome, mean cos +0.51 to 5); *Defective GALNT3 causes HFTC* (reactome, mean cos +0.51 to 5); *Defective C1GALT1C1 causes TNPS* (reactome, mean cos +0.51 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +5.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.9 | +12.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.8 | +10.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.6 | +3.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.1 | +8.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.2 | +2.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.0 | +1.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.9 | +1.2 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +0.9 | +1.2 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -0.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -1.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.0 | -0.7 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.0 | -3.2 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.0 | -2.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -1.8 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.9 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | creatine kinase, mitochondrial 1B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.3 — chr15:43,593,054-43,604,901 (+) |
| Ensembl biotype | protein_coding |
| Also known as | UMTCK; previously CKMT, CKMT1 |
| Gene groups (HGNC) | Proteins encoded by multiple genes; Creatine kinase family |
| Matched by | ensembl_id |

**Function**, from UniProt [P12532](https://www.uniprot.org/uniprotkb/P12532) (Creatine kinase U-type, mitochondrial):

> Reversibly catalyzes the transfer of phosphate between ATP and various phosphogens (e.g. creatine phosphate). Creatine kinase isoenzymes play a central role in energy transduction in tissues with large, fluctuating energy demands, such as skeletal muscle, heart, brain and spermatozoa.

**Summary**, from NCBI Gene [1159](https://www.ncbi.nlm.nih.gov/gene/1159):

> Mitochondrial creatine (MtCK) kinase is responsible for the transfer of high energy phosphate from mitochondria to the cytosolic carrier, creatine. It belongs to the creatine kinase isoenzyme family. It exists as two isoenzymes, sarcomeric MtCK and ubiquitous MtCK, encoded by separate genes. Mitochondrial creatine kinase occurs in two different oligomeric forms: dimers and octamers, in contrast to the exclusively dimeric cytosolic creatine kinase isoenzymes. Many malignant cancers with poor …

**Accessions** — [HGNC:1995](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1995) · Entrez [1159](https://www.ncbi.nlm.nih.gov/gene/1159) · UniProt [P12532](https://www.uniprot.org/uniprotkb/P12532) · Ensembl [ENSG00000237289](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000237289)

## Data

Gene col 14123: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14123); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14123, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14123]; `tensor/DDL_lfc|DDL_z.npy` [14123]; `embed/gene_vectors.npy` [14123]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14123 or target_col == 14123). Every well: [[CKMT1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CKMT1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
