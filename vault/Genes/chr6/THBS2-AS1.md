---
symbol: "THBS2-AS1"
type: "gene"
col: 13533
ensembl_id: "ENSG00000226445"
name: "THBS2 antisense RNA 1"
location: "6q27"
module: 35
arm: "+"
pooled_cpm: 2.1
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 11
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# THBS2-AS1

*THBS2 antisense RNA 1* — 6q27

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.33× (z +10.0, q 6e-21, up in 2 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.52× (z +5.2, q 3e-05, up in 5 of 44 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Docetaxel (drug)]] 0.05 µM in 1 line (HOP62 0.117×; ⚠ transcription drop); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (MIA PaCa-2 0.0420×; ⚠ cell-cycle shift, explains ~26% of this change); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (HS-578T 0.0723×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DENND2A]] (+0.60, fdr 1e-05), [[ZKSCAN7-AS1]] (+0.59, fdr 1e-05), [[LINC01615]] (+0.59, fdr 1e-05); moves opposite to [[MYO5C]] (-0.48, fdr 3e-05), [[MPZL2]] (-0.45, fdr 9e-05), [[POF1B]] (-0.44, fdr 3e-04).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[PDGFRB]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 7 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13533.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.33×** | +10.0 | 6e-21 | 2/4 (A498, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.71×** | +8.7 | 1e-15 | 1/8 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.62×** | +7.7 | 2e-12 | 2/6 (PANC-1, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.89×** | +5.5 | 5e-06 | 3/10 (A498, SW480, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.52×** | +5.2 | 3e-05 | 5/44 (A-427, RKO, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.80×** | +3.7 | 0.024 | 0/6 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.50×** | +3.5 | 0.045 | 4/25 (SW480, SNU-1, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +3.3 | 0.069 | 1/14 (C32) | top dose only | cell-cycle shift (explains ~0% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | 1.95× | +3.0 | 0.16 | 0/4 | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13533.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Docetaxel (drug)]] 0.05 µM in 1 line (HOP62 0.117×; ⚠ transcription drop); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (MIA PaCa-2 0.0420×; ⚠ cell-cycle shift, explains ~26% of this change); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (HS-578T 0.0723×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 0.656× | -3.6 | 0.21 | 13/40 (SNU-423, SK-MEL-2, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.690× | -3.2 | 0.25 | 10/25 (HS-578T, HOP62, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.684× | -3.2 | 0.25 | 11/45 (MIA PaCa-2, RKO, …) | inconsistent across doses | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13533. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 6.30 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.117× (z -9.6) ⚠ transcription drop |
| [[HS-578T (line)]] | alt | 5.44 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0723× (z -8.7) |
| [[MIA PaCa-2 (line)]] | alt | 3.09 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0420× (z -9.3) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A-172 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.10 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.853 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.928 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.934 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.893 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.914 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.37 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.04 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.773 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.692 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.756 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.742 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.941 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.930 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13533), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DENND2A]] | +0.60 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[ZKSCAN7-AS1]] | +0.59 | +0.53 / +0.56 | both halves | 1e-05 | same gene group |
| [[LINC01615]] | +0.59 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[VSTM4]] | +0.58 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[SYNC]] | +0.58 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[SLC14A2]] | +0.58 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[PRRT2]] | +0.57 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[ZNF236-DT]] | +0.54 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[GDNF-AS1]] | +0.53 | +0.59 / +0.38 | both halves | 7e-05 | same gene group |
| [[DLL1]] | +0.53 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[LMO7-AS1]] | +0.53 | +0.46 / +0.43 | both halves | 3e-05 | same gene group |
| [[LINC01119]] | +0.52 | +0.45 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYO5C]] | -0.48 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[MPZL2]] | -0.45 | -0.48 / -0.36 | both halves | 9e-05 |  |
| [[POF1B]] | -0.44 | -0.49 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDGFRB]] | B | PDGFRB activity raises THBS2-AS1's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 1.73× lower at baseline in the lines without PDGFRB | 0.007 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2 |
| [[LINC01615]] | B | LINC01615 activity raises THBS2-AS1's level | lines that do not express LINC01615 (36) vs lines expressing it (14) | 1.86× lower at baseline in the lines without LINC01615 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235749, ENSG00000222032, GYPC |
| [[MYO5C]] | B | MYO5C activity lowers THBS2-AS1's level | lines that do not express MYO5C (20) vs lines expressing it (30) | 1.77× higher at baseline in the lines without MYO5C | 0.011 | ⚠ within organs, on part of the lines; also absent: ENSG00000288656, EVPL, NCMAP; maybe low, not absent |
| [[LINC01411]] | B | LINC01411 activity raises THBS2-AS1's level | lines that do not express LINC01411 (38) vs lines expressing it (12) | 1.82× lower at baseline in the lines without LINC01411 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: VCAM1, TMPRSS15, ENSG00000222032 |
| [[APCDD1L]] | B | APCDD1L activity raises THBS2-AS1's level | lines that do not express APCDD1L (34) vs lines expressing it (16) | 1.65× lower at baseline in the lines without APCDD1L | 0.039 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MMP2, ENSG00000222032, PHACTR1 |
| [[GDNF-AS1]] | B | GDNF-AS1 activity raises THBS2-AS1's level | lines that do not express GDNF-AS1 (23) vs lines expressing it (27) | 1.51× lower at baseline in the lines without GDNF-AS1 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SDC2, COLEC12, DAAM2; maybe low, not absent |
| [[PKD1L1-AS1]] | B | PKD1L1-AS1 activity raises THBS2-AS1's level | lines that do not express PKD1L1-AS1 (36) vs lines expressing it (14) | 1.79× lower at baseline in the lines without PKD1L1-AS1 | 0.064 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000222032, TMPRSS15, COL1A2 |
| [[THBS2]] | B | THBS2 activity raises THBS2-AS1's level | lines that do not express THBS2 (37) vs lines expressing it (13) | 1.67× lower at baseline in the lines without THBS2 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SPARC, ENSG00000254337, ITGA4 |
| [[DENND2A]] | B | DENND2A activity raises THBS2-AS1's level | lines that do not express DENND2A (23) vs lines expressing it (27) | 1.53× lower at baseline in the lines without DENND2A | 0.072 | ⚠ within organs, on part of the lines; also absent: PTPRN, SPARC, BAALC; maybe low, not absent |
| [[APOBEC3G]] | B | APOBEC3G activity raises THBS2-AS1's level | lines that do not express APOBEC3G (22) vs lines expressing it (28) | 1.36× lower at baseline in the lines without APOBEC3G | 0.086 | ⚠ within organs, on part of the lines; also absent: LINC02813, PTX3, PDLIM3 |
| [[COL5A1]] | B | COL5A1 activity raises THBS2-AS1's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 1.49× lower at baseline in the lines without COL5A1 | 0.096 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.374). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (54.3, 16.7); signed map (27.5, 50.1). **Vector** length 34.1, 3.31% of its response variance represented; |z| ≥ 3 in 961 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +2.2 | +5.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.9 | +7.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.4 | +10.0 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +1.1 | -0.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +1.0 | +3.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.0 | -0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.0 | +1.5 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +0.7 | +2.6 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +0.6 | +1.5 |
|  | [[Rapamycin (drug)]] 5 µM |  | +0.5 | +0.6 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -0.8 | -3.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.7 | -1.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.6 | -1.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.6 | -1.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.6 | -2.9 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -0.6 | -0.1 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.6 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | THBS2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 6q27 — chr6:169,213,254-169,245,773 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:56059](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:56059) · Entrez [101929523](https://www.ncbi.nlm.nih.gov/gene/101929523) · Ensembl [ENSG00000226445](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000226445)

## Data

Gene col 13533: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13533); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13533, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13533]; `tensor/DDL_lfc|DDL_z.npy` [13533]; `embed/gene_vectors.npy` [13533]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13533 or target_col == 13533). Every well: [[THBS2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/THBS2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
