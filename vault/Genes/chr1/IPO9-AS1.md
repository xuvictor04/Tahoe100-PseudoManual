---
symbol: "IPO9-AS1"
type: "gene"
col: 13818
ensembl_id: "ENSG00000231871"
name: "IPO9 antisense RNA 1"
location: "1q32.1"
module: 80
arm: "+"
pooled_cpm: 9.46
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 3
n_dd_up_clean: 8
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 15
direction_downstream: 0
tags: ["gene", "module/080"]
generated_by: "tahoemap"
---

# IPO9-AS1

*IPO9 antisense RNA 1* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.23× (z +15.2, q 0e+00, up in 35 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.546× (z -8.1, q 3e-13, down in 27 of 47 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01500]] (+0.76, fdr 7e-06), [[C2orf92]] (+0.74, fdr 7e-06), [[PAMR1]] (+0.69, fdr 1e-05); moves opposite to [[RSAD1]] (-0.57, fdr 1e-04).
> It is in [[Module 080]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[NAV1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13818.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.23×** | +15.2 | 0e+00 | 35/43 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.13×** | +14.3 | 4e-44 | 32/45 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.07×** | +9.8 | 2e-20 | 23/31 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.60×** | +8.9 | 8e-17 | 33/47 (HEC-1-A, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.72×** | +7.0 | 3e-10 | 8/16 (MIA PaCa-2, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.51×** | +5.5 | 4e-06 | 15/41 (CFPAC-1, HEC-1-A, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.45×** | +5.0 | 4e-05 | 17/43 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.47×** | +4.8 | 1e-04 | 5/21 (SW 900, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +4.8 | 1e-04 | 15/39 (NCI-H2030, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +4.6 | 2e-04 | 18/42 (SW480, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Rapamycin (drug)]] 0.5 µM |  | **1.26×** | +3.1 | 0.093 | 4/44 (PANC-1, SHP-77, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.27×** | +3.1 | 0.093 | 8/44 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +3.1 | 0.093 | 16/43 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13818.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.546×** | -8.1 | 3e-13 | 27/47 (A-172, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.586×** | -7.2 | 2e-10 | 25/48 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.666×** | -5.5 | 9e-06 | 21/48 (NCI-H1792, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.782× | -3.3 | 0.13 | 12/46 (hTERT-HPNE, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | 0.787× | -3.2 | 0.13 | 7/48 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.788× | -3.2 | 0.13 | 6/46 (Hs 766T, HOP62, …) | two highest doses |  |
| [[Phenytoin (sodium) (drug)]] 0.05 µM |  | 0.779× | -3.1 | 0.15 | 6/45 (HCT15, SK-MEL-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13818. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 21.4 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +9.6) | [[Panobinostat (drug)]] 5 µM 0.225× (z -9.8) |
| [[SW480 (line)]] | alt | 8.03 | 3 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.11× (z +10.6) | [[Panobinostat (drug)]] 0.5 µM 0.255× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 7.56 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.91× (z +9.8) | — |
| [[A-172 (line)]] | wt | 31.8 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.157× (z -11.9) |
| [[A498 (line)]] | wt | 9.44 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +10.0) | — |
| [[A549 (line)]] | wt | 6.31 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.23× (z +8.6) | — |
| [[BT-474 (line)]] | alt | 7.06 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 5 µM 0.0860× (z -8.5) |
| [[C32 (line)]] | wt | 17.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +11.4) | — |
| [[CFPAC-1 (line)]] | alt | 7.23 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +10.1) | — |
| [[hTERT-HPNE (line)]] | wt | 26.9 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.157× (z -9.1) |
| [[J82 (line)]] | alt | 14.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +9.9) | — |
| [[KATO III (line)]] | alt | 5.05 | 0 | 1 | — | [[Ivermectin (drug)]] 0.5 µM 0.0814× (z -8.8) |
| [[LoVo (line)]] | wt | 6.17 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.66× (z +9.7) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 14.7 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.183× (z -9.2) |
| [[NCI-H1573 (line)]] | alt | 5.65 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +9.4) | — |
| [[NCI-H1792 (line)]] | alt | 10.2 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0502× (z -14.7) |
| [[NCI-H2030 (line)]] | alt | 5.89 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.126× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 6.49 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +11.1) | — |
| [[PANC-1 (line)]] | alt | 6.39 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.76× (z +9.8) | — |
| [[SK-MEL-2 (line)]] | alt | 10.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.28× (z +9.9) | — |
| [[SNU-423 (line)]] | alt | 14.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.183× (z -8.8) |
| [[SW 900 (line)]] | alt | 8.98 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.16× (z +8.5) | — |
| [[A-427 (line)]] | wt | 5.13 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.91 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.48 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.12 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.45 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.62 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.81 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.49 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.26 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.20 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.20 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13818), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01500]] | +0.76 | +0.78 / +0.63 | both halves | 7e-06 |  |
| [[C2orf92]] | +0.74 | +0.75 / +0.64 | both halves | 7e-06 |  |
| [[PAMR1]] | +0.69 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[SOCS2-AS1]] | +0.68 | +0.66 / +0.47 | both halves | 2e-05 | same gene group |
| [[DENND2A]] | +0.66 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[GRK4]] | +0.66 | +0.68 / +0.47 | both halves | 2e-05 |  |
| [[GPR137]] | +0.66 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[APCDD1L-DT]] | +0.65 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[CFAP20DC-DT]] | +0.64 | +0.67 / +0.43 | both halves | 3e-05 |  |
| [[WNT5B]] | +0.64 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[LINC01358]] | +0.63 | +0.64 / +0.35 | both halves | 1e-04 |  |
| [[LINC00863]] | +0.63 | +0.60 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RSAD1]] | -0.57 | -0.49 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 14, C 1. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NAV1]] | B | NAV1 activity raises IPO9-AS1's level | lines that do not express NAV1 (22) vs lines expressing it (28) | 1.78× lower at baseline in the lines without NAV1 | 0.003 | ⚠ within organs, on part of the lines; also absent: NAV2, ENSG00000287622, CDK15; maybe low, not absent |
| [[APCDD1L]] | B | APCDD1L activity raises IPO9-AS1's level | lines that do not express APCDD1L (34) vs lines expressing it (16) | 1.85× lower at baseline in the lines without APCDD1L | 0.007 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MMP2, ENSG00000222032, PHACTR1 |
| [[JAM2]] | B | JAM2 activity raises IPO9-AS1's level | lines that do not express JAM2 (28) vs lines expressing it (22) | 1.64× lower at baseline in the lines without JAM2 | 0.010 | ⚠ within organs, on part of the lines; also absent: ITGA4, RORB, IL7R |
| [[TOP2A]] | B | TOP2A activity lowers IPO9-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises IPO9-AS1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[LRRC17]] | B | LRRC17 activity raises IPO9-AS1's level | lines that do not express LRRC17 (27) vs lines expressing it (23) | 1.30× lower at baseline in the lines without LRRC17 | 0.042 | ⚠ within organs, on part of the lines; also absent: AEBP1, ARHGAP6, LINC02240; maybe low, not absent |
| [[MIR137HG]] | B | MIR137HG activity raises IPO9-AS1's level | lines that do not express MIR137HG (28) vs lines expressing it (22) | 1.49× lower at baseline in the lines without MIR137HG | 0.045 | ⚠ within organs, on part of the lines; also absent: EDNRA, CCBE1, ARMCX2 |
| [[DENND2A]] | B | DENND2A activity raises IPO9-AS1's level | lines that do not express DENND2A (23) vs lines expressing it (27) | 1.61× lower at baseline in the lines without DENND2A | 0.053 | ⚠ within organs, on part of the lines; also absent: PTPRN, SPARC, BAALC; maybe low, not absent |
| [[PRRX1]] | B | PRRX1 activity raises IPO9-AS1's level | lines that do not express PRRX1 (34) vs lines expressing it (16) | 1.51× lower at baseline in the lines without PRRX1 | 0.054 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, LINC00383, DCN |
| [[LINC01615]] | B | LINC01615 activity strengthens IPO9-AS1's drug response | lines that do not express LINC01615 (36) vs lines expressing it (12) | the lines without LINC01615 respond 0.88× as strongly (z diff +0.18); strongest at Belinostat 5 µM: 0.63x vs 0.26x (z diff +4.7) | 0.055 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235749, ENSG00000222032, GYPC; target measured in part of the lines; both ways; artifact flags |
| [[LINC01615]] | B | LINC01615 activity raises IPO9-AS1's level | lines that do not express LINC01615 (36) vs lines expressing it (14) | 1.82× lower at baseline in the lines without LINC01615 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235749, ENSG00000222032, GYPC |
| [[ADAMTS2]] | B | ADAMTS2 activity raises IPO9-AS1's level | lines that do not express ADAMTS2 (29) vs lines expressing it (21) | 1.53× lower at baseline in the lines without ADAMTS2 | 0.077 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZNF667, ZNF667-AS1, COL3A1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 080]]; 57 genes; every member is in the + arm (projection on the module's main direction 0.667). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (30.0, -6.1); signed map (26.2, 8.8). **Vector** length 84.9, 15.8% of its response variance represented; |z| ≥ 3 in 996 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.9 | +15.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +9.9 | +14.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.8 | +8.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | +7.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.6 | +9.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +2.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.0 | +1.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.6 | +0.9 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.3 | +2.0 |
| fall | [[Belinostat (drug)]] 5 µM |  | -3.3 | -8.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.0 | -5.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.3 | -7.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.2 | -3.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | -2.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -3.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.5 | -2.2 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.3 | -1.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.3 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | IPO9 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1q32.1 — chr1:201,688,259-201,829,559 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40892](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40892) · Entrez [100873949](https://www.ncbi.nlm.nih.gov/gene/100873949) · Ensembl [ENSG00000231871](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000231871)

## Data

Gene col 13818: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13818); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13818, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13818]; `tensor/DDL_lfc|DDL_z.npy` [13818]; `embed/gene_vectors.npy` [13818]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13818 or target_col == 13818). Every well: [[IPO9-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IPO9-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
