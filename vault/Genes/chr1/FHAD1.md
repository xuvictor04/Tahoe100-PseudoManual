---
symbol: "FHAD1"
type: "gene"
col: 6636
ensembl_id: "ENSG00000142621"
name: "forkhead associated phosphopeptide binding domain 1"
location: "1p36.21"
module: 140
arm: "+"
pooled_cpm: 20.05
n_lines_expressing: 36
n_dd_up: 15
n_dd_down: 4
n_dd_up_clean: 9
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 9
direction_downstream: 3
tags: ["gene", "module/140"]
generated_by: "tahoemap"
---

# FHAD1

*forkhead associated phosphopeptide binding domain 1* — 1p36.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.13× (z +11.9, q 1e-29, up in 14 of 28 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.61× (z +10.6, q 9e-24, up in 21 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.748× (z -4.6, q 0.003, down in 13 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DELEC1]] (+0.61, fdr 1e-05), [[PPP1R3B-DT]] (+0.58, fdr 1e-05), [[POU2F2]] (+0.57, fdr 1e-05).
> It is in [[Module 140]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[CDH13]] → it (grade B ⚠); 3 go from it, the strongest it → [[POU2F2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠; shown: the 15 strongest. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6636.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.13×** | +11.9 | 1e-29 | 14/28 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.14×** | +11.5 | 4e-28 | 6/15 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.61×** | +10.6 | 9e-24 | 21/34 (HT-29, SW480, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +10.2 | 2e-22 | 18/32 (A549, A498, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.80×** | +9.2 | 4e-18 | 19/34 (HT-29, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.78×** | +8.4 | 5e-15 | 10/20 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.70×** | +8.3 | 7e-15 | 19/33 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.69×** | +8.2 | 1e-14 | 17/33 (A-172, RPMI-7951, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.53×** | +6.7 | 2e-09 | 14/33 (CFPAC-1, HepG2/C3A, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.48×** | +6.2 | 3e-08 | 13/34 (CFPAC-1, SHP-77, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.48×** | +6.1 | 5e-08 | 15/34 (CFPAC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.31×** | +5.9 | 2e-07 | 11/31 (A-172, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.31×** | +4.2 | 0.001 | 5/34 (SW480, A-172, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +3.8 | 0.005 | 10/34 (HS-578T, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.27×** | +3.8 | 0.007 | 9/31 (HS-578T, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6636.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.748×** | -4.6 | 0.003 | 13/34 (KATO III, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.788×** | -3.7 | 0.051 | 9/33 (COLO 205, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.795×** | -3.6 | 0.052 | 11/33 (COLO 205, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.782×** | -3.6 | 0.052 | 10/33 (A-427, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Dexamethasone (drug)]] 5 µM |  | 0.822× | -3.1 | 0.21 | 5/33 (hTERT-HPNE, CFPAC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | 0.823× | -3.1 | 0.21 | 9/33 (NCI-H460, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6636. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 271 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.338× (z -14.0) |
| [[COLO 205 (line)]] | alt | 33.2 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.119× (z -10.4) |
| [[NCI-H460 (line)]] | wt | 56.5 | 0 | 4 (2 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.274× (z -9.7) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.294× (z -9.7) |
| [[KATO III (line)]] | alt | 77.7 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.226× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.343× (z -9.6) |
| [[hTERT-HPNE (line)]] | wt | 34.3 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.136× (z -9.6) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 103 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -10.6) |
| [[SK-MEL-2 (line)]] | alt | 81.6 | 0 | 2 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0900× (z -11.4) ⚠ toxic |
| [[HCT15 (line)]] | alt | 12.2 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.111× (z -9.0) |
| [[HT-29 (line)]] | alt | 5.96 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.51× (z +8.9) | — |
| [[NCI-H1792 (line)]] | alt | 8.15 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0866× (z -9.9) |
| [[RPMI-7951 (line)]] | alt | 124 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.282× (z -11.0) ⚠ cell-cycle shift, explains ~40% of this change |
| [[SHP-77 (line)]] | alt | 7.90 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.115× (z -8.9) |
| [[SW480 (line)]] | alt | 6.68 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.60× (z +9.7) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 7.38 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.95 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.53 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.59 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.16 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.09 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 7.87 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.40 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.50 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.93 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.72 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.43 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.32 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.83 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.91 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.15 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.95 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.94 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.37 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.89 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.69 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.01 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.35 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.42 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6636), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DELEC1]] | +0.61 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[PPP1R3B-DT]] | +0.58 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[POU2F2]] | +0.57 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[TMPRSS9]] | +0.57 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[AMZ1]] | +0.57 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[LINC00922]] | +0.57 | +0.41 / +0.62 | both halves | 4e-05 |  |
| [[PRKCG]] | +0.56 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[DGKI]] | +0.56 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[COL15A1]] | +0.55 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[LINC00243]] | +0.54 | +0.46 / +0.57 | both halves | 2e-05 |  |
| [[BACH1]] | +0.54 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[IL3RA]] | +0.53 | +0.44 / +0.58 | both halves | 3e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDH13]] | B | CDH13 activity raises FHAD1's level | lines that do not express CDH13 (35) vs lines expressing it (15) | 2.40× lower at baseline in the lines without CDH13 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMP2, APCDD1L, ENSG00000222032 |
| [[PDCD1LG2]] | B | PDCD1LG2 activity raises FHAD1's level | lines that do not express PDCD1LG2 (28) vs lines expressing it (22) | 1.68× lower at baseline in the lines without PDCD1LG2 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADAMTS12, FN1, APCDD1L |
| [[DGKI]] | B | DGKI activity raises FHAD1's level | lines that do not express DGKI (27) vs lines expressing it (23) | 1.76× lower at baseline in the lines without DGKI | 0.028 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, SPARC, LAMA1; maybe low, not absent |
| [[SHANK1]] | B | SHANK1 activity raises FHAD1's level | lines that do not express SHANK1 (22) vs lines expressing it (28) | 1.31× lower at baseline in the lines without SHANK1 | 0.062 | ⚠ within organs, on part of the lines; also absent: TRIML2, HOXD8, ENSG00000242880 |
| [[NPAS1]] | B | NPAS1 activity lowers FHAD1's level | lines that do not express NPAS1 (9) vs lines expressing it (41) | 1.94× higher at baseline in the lines without NPAS1 | 0.067 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[IL11]] | B | IL11 activity raises FHAD1's level | lines that do not express IL11 (27) vs lines expressing it (23) | 1.47× lower at baseline in the lines without IL11 | 0.075 | ⚠ within organs, on part of the lines; also absent: EDNRA, LINC00973, LINC01583 |
| [[ADAMTS6]] | B | ADAMTS6 activity raises FHAD1's level | lines that do not express ADAMTS6 (25) vs lines expressing it (25) | 1.42× lower at baseline in the lines without ADAMTS6 | 0.076 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: FLI1, PDCD1LG2, TENM2 |
| [[SHC3]] | B | SHC3 activity raises FHAD1's level | lines that do not express SHC3 (22) vs lines expressing it (28) | 1.62× lower at baseline in the lines without SHC3 | 0.089 | ⚠ within organs, on part of the lines; also absent: CCDC33, CCR3, RFX8; maybe low, not absent |
| [[SIGLEC15]] | B | SIGLEC15 activity raises FHAD1's level | lines that do not express SIGLEC15 (27) vs lines expressing it (23) | 1.61× lower at baseline in the lines without SIGLEC15 | 0.093 | ⚠ within organs, on part of the lines; also absent: LINC01615, ZNF257, NLRP1 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[POU2F2]] | B | FHAD1 activity raises POU2F2's level | lines that do not express FHAD1 (14) vs lines expressing it (36) | 2.02× lower at baseline in the lines without FHAD1 | 0.012 | ⚠ within organs, on part of the lines; also absent: LINC01798, LINC01426; maybe low, not absent |
| [[PEBP4]] | B | FHAD1 activity raises PEBP4's level | lines that do not express FHAD1 (14) vs lines expressing it (36) | 1.74× lower at baseline in the lines without FHAD1 | 0.076 | ⚠ within organs, on part of the lines; also absent: LINC01798, LINC01426; maybe low, not absent |
| cells under [[Volasertib (drug)]] 5 µM | B | FHAD1 activity raises the cells' numbers under Volasertib 5 µM (protects the cells) | lines that do not express FHAD1 (14) vs lines expressing it (34) | the lines without FHAD1: 0.91× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: LINC01798, LINC01426; maybe low, not absent |

## Where it sits

- **Module**: [[Module 140]]; 34 genes; every member is in the + arm (projection on the module's main direction 0.382). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (42.5, -12.4); signed map (20.0, 17.4). **Vector** length 63.9, 11.6% of its response variance represented; |z| ≥ 3 in 769 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.4 | +11.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.3 | +11.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.0 | +8.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.7 | +10.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +10.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.5 | +8.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +3.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.1 | +2.7 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +1.8 | +2.3 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -2.8 | -3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.5 | -2.9 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -2.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.0 | -2.8 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.0 | -3.1 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.8 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | forkhead associated phosphopeptide binding domain 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.21 — chr1:15,236,521-15,400,283 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1937 |
| Matched by | ensembl_id |

**Function**, from UniProt [B1AJZ9](https://www.uniprot.org/uniprotkb/B1AJZ9) (Forkhead-associated domain-containing protein 1):

> Regulator of sperm motility and spermatocyte meiosis.

**Summary**, from NCBI Gene [114827](https://www.ncbi.nlm.nih.gov/gene/114827):

> Predicted to act upstream of or within apoptotic process and spermatogenesis. Located in sperm flagellum. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29408](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29408) · Entrez [114827](https://www.ncbi.nlm.nih.gov/gene/114827) · UniProt [B1AJZ9](https://www.uniprot.org/uniprotkb/B1AJZ9) · Ensembl [ENSG00000142621](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142621)

## Data

Gene col 6636: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6636); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6636, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6636]; `tensor/DDL_lfc|DDL_z.npy` [6636]; `embed/gene_vectors.npy` [6636]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6636 or target_col == 6636). Every well: [[FHAD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FHAD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
