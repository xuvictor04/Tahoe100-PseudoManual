---
symbol: "CCDC194"
type: "gene"
col: 15630
ensembl_id: "ENSG00000269720"
name: "coiled-coil domain containing 194"
location: "19p13.11"
module: 32
arm: "+"
pooled_cpm: 5.11
n_lines_expressing: 31
n_dd_up: 11
n_dd_down: 30
n_dd_up_clean: 10
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 18
direction_downstream: 55
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# CCDC194

*coiled-coil domain containing 194* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.66× (z +10.8, q 1e-24, up in 18 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (11 with an alert ⚠); the strongest is [[Tofacitinib (drug)]] 5 µM: 0.385× (z -10.5, q 3e-23, down in 23 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FBXO39]] (+0.84, fdr 7e-06), [[NRIR]] (+0.81, fdr 7e-06), [[ZC3HAV1]] (+0.81, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 18 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 55 go from it, the strongest it → [[MVB12A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15630.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.66×** | +10.8 | 1e-24 | 18/24 (LoVo, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **3.86×** | +9.6 | 2e-19 | 19/27 (HT-29, LoVo, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.87×** | +8.0 | 3e-13 | 16/22 (A498, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.21×** | +6.0 | 3e-07 | 15/24 (RKO, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.59×** | +5.2 | 3e-05 | 12/28 (NCI-H2347, LoVo, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.73×** | +4.3 | 0.002 | 14/28 (NCI-H2347, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.69×** | +4.0 | 0.006 | 9/26 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | **1.62×** | +3.8 | 0.010 | 7/27 (CFPAC-1, A498, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +3.7 | 0.013 | 12/19 (NCI-H2347, LoVo, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.37×** | +3.4 | 0.039 | 7/26 (CFPAC-1, MIA PaCa-2, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 5 µM |  | **1.35×** | +3.3 | 0.045 | 5/29 (NCI-H2347, A-172, …) | top dose only |  |
| [[venetoclax (drug)]] 0.05 µM |  | 1.51× | +3.1 | 0.11 | 2/27 (CFPAC-1, LoVo) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15630.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tofacitinib (drug)]] 5 µM |  | **0.385×** | -10.5 | 3e-23 | 23/26 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.460×** | -8.6 | 3e-15 | 21/27 (RPMI-7951, CFPAC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.339×** | -8.5 | 5e-15 | 21/26 (RKO, MIA PaCa-2, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.533×** | -6.9 | 5e-10 | 19/27 (CFPAC-1, MIA PaCa-2, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.407×** | -6.8 | 2e-09 | 15/20 (LoVo, A-172, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.437×** | -6.5 | 1e-08 | 17/27 (MIA PaCa-2, H4, …) | all doses, flat | cell-cycle shift (explains ~19% here) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.463×** | -6.0 | 1e-07 | 15/26 (BT-474, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.451×** | -5.6 | 1e-06 | 13/28 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.492×** | -5.5 | 2e-06 | 15/27 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.493×** | -5.5 | 2e-06 | 16/27 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.506×** | -4.8 | 7e-05 | 14/25 (LoVo, A-427, …) | all doses, flat |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.511×** | -4.8 | 9e-05 | 15/27 (MIA PaCa-2, A-172, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **0.516×** | -4.7 | 1e-04 | 12/27 (A-172, LoVo, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.576×** | -4.3 | 7e-04 | 14/27 (H4, Panc 03.27, …) | all doses, stronger at high dose | position effect removed |
| [[Ixazomib (drug)]] 5 µM |  | **0.360×** | -4.2 | 0.001 | 11/23 (SHP-77, COLO 205, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.587×** | -4.2 | 0.001 | 15/28 (BT-474, A-172, …) | rises with dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.383×** | -3.9 | 0.003 | 11/24 (A-172, HepG2/C3A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **0.603×** | -3.8 | 0.004 | 8/27 (RPMI-7951, H4, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.602×** | -3.6 | 0.008 | 8/27 (SNU-1, MIA PaCa-2, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.642×** | -3.4 | 0.013 | 9/26 (SNU-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.621×** | -3.4 | 0.017 | 12/28 (LoVo, A-172, …) | all doses, flat | cell-cycle shift (explains ~13% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15630. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 20.7 | 2 | 5 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.21× (z +10.0) | [[Niclosamide (olamine) (drug)]] 5 µM 0.105× (z -13.1) ⚠ toxic · without an alert: [[Tofacitinib (drug)]] 5 µM 0.304× (z -10.1) |
| [[MIA PaCa-2 (line)]] | alt | 18.7 | 0 | 6 (2 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.121× (z -11.5) |
| [[A498 (line)]] | wt | 9.90 | 0 | 4 (3 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.200× (z -9.0) |
| [[CFPAC-1 (line)]] | alt | 16.9 | 0 | 4 (2 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.172× (z -11.0) |
| [[A-172 (line)]] | wt | 13.2 | 0 | 3 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0957× (z -9.1) |
| [[RKO (line)]] | wt | 5.08 | 1 | 1 | [[Auranofin (drug)]] 5 µM 25.7× (z +9.2) | [[Tofacitinib (drug)]] 0.5 µM 0.0478× (z -9.4) |
| [[RPMI-7951 (line)]] | alt | 14.6 | 0 | 2 | — | [[Tofacitinib (drug)]] 5 µM 0.155× (z -10.1) |
| [[SNU-1 (line)]] | wt | 15.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0736× (z -9.0) |
| [[BT-474 (line)]] | alt | 5.58 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0779× (z -9.3) ⚠ cell-cycle shift, explains ~99% of this change |
| [[COLO 205 (line)]] | alt | 19.2 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.152× (z -10.7) |
| [[HT-29 (line)]] | alt | 3.42 | 1 | 0 | [[Auranofin (drug)]] 5 µM 32.1× (z +9.6) | — |
| [[Panc 03.27 (line)]] | alt | 12.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.08× (z +9.8) | — |
| [[SHP-77 (line)]] | alt | 6.84 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0751× (z -8.5) ⚠ toxic |
| [[A-427 (line)]] | wt | 3.75 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.817 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.975 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.87 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.37 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.731 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.536 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.518 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 7.43 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.732 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.485 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.410 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.654 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.447 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.740 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.665 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.704 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.522 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.704 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15630), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXO39]] | +0.84 | +0.84 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[NRIR]] | +0.81 | +0.75 / +0.79 | both halves | 7e-06 |  |
| [[ZC3HAV1]] | +0.81 | +0.75 / +0.76 | both halves | 7e-06 |  |
| [[USP18]] | +0.80 | +0.72 / +0.81 | both halves | 7e-06 |  |
| [[IFI27]] | +0.80 | +0.72 / +0.78 | both halves | 7e-06 |  |
| [[BST2]] | +0.79 | +0.71 / +0.87 | both halves | 7e-06 | ⚠ same locus (8.7 kb, same strand: neighbours can correlate without regulation) |
| [[CMPK2]] | +0.78 | +0.72 / +0.78 | both halves | 7e-06 |  |
| [[RSAD2]] | +0.77 | +0.77 / +0.75 | both halves | 7e-06 |  |
| [[IFI6]] | +0.76 | +0.67 / +0.79 | both halves | 7e-06 |  |
| [[IFIT3]] | +0.76 | +0.73 / +0.72 | both halves | 7e-06 |  |
| [[IFI44L]] | +0.76 | +0.66 / +0.78 | both halves | 7e-06 |  |
| [[OAS2]] | +0.76 | +0.69 / +0.76 | both halves | 7e-06 |  |
| [[XAF1]] | +0.76 | +0.71 / +0.75 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 11, C 7. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CCDC194's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[OAS1]] | B | OAS1 activity raises CCDC194's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 2.45× lower at baseline in the lines without OAS1 | 0.024 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[CMPK2]] | B | CMPK2 activity raises CCDC194's level | lines that do not express CMPK2 (11) vs lines expressing it (39) | 2.41× lower at baseline in the lines without CMPK2 | 0.033 | ⚠ within organs, on part of the lines; also absent: OAS2, NRIR, OAS1 |
| [[SRMS]] | B | SRMS activity raises CCDC194's level | lines that do not express SRMS (14) vs lines expressing it (36) | 2.39× lower at baseline in the lines without SRMS | 0.042 | ⚠ within organs, on part of the lines; also absent: MX1, OAS2, RSAD2 |
| [[OAS2]] | B | OAS2 activity raises CCDC194's level | lines that do not express OAS2 (14) vs lines expressing it (36) | 2.31× lower at baseline in the lines without OAS2 | 0.047 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1 |
| [[IFI6]] | B | IFI6 activity raises CCDC194's level | lines that do not express IFI6 (13) vs lines expressing it (37) | 2.44× lower at baseline in the lines without IFI6 | 0.073 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent |
| [[MX2]] | B | MX2 activity raises CCDC194's level | lines that do not express MX2 (16) vs lines expressing it (34) | 2.31× lower at baseline in the lines without MX2 | 0.080 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: NRP1, SLC15A3, DEPP1 |
| [[PLSCR1]] | B | PLSCR1 activity raises CCDC194's level | lines that do not express PLSCR1 (8) vs lines expressing it (42) | 3.00× lower at baseline in the lines without PLSCR1 | 0.089 | ⚠ within organs, on part of the lines; also absent: PARP9, ENSG00000279320, IFI6; maybe low, not absent |
| [[RSAD2]] | B | RSAD2 activity raises CCDC194's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 2.11× lower at baseline in the lines without RSAD2 | 0.092 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[PARP9]] | B | PARP9 activity raises CCDC194's level | lines that do not express PARP9 (7) vs lines expressing it (43) | 2.86× lower at baseline in the lines without PARP9 | 0.093 | ⚠ within organs, on part of the lines; also absent: PLSCR1, OAS3, SRMS; maybe low, not absent |
| [[NRIR]] | B | NRIR activity raises CCDC194's level | lines that do not express NRIR (14) vs lines expressing it (36) | 2.14× lower at baseline in the lines without NRIR | 0.098 | ⚠ within organs, on part of the lines; also absent: CMPK2, TSPAN7 |
| [[BST2]] | C | BST2 activity raises CCDC194's level | lines that do not express BST2 (18) vs lines expressing it (32) | 4.10× lower at baseline in the lines without BST2 | 5e-05 | ⚠ within organs, on part of the lines; also absent: CCDC194, DEPP1, SLC15A3; co-absent with the target |

### Downstream of this gene

*55 arrows, 55 of them with an alert ⚠; grade A 0, B 48, C 7. Shown: the 12 strongest; 43 more arrows (43 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MVB12A]] | B | CCDC194 activity raises MVB12A's level | lines that do not express CCDC194 (19) vs lines expressing it (31) | 1.90× lower at baseline in the lines without CCDC194 | 0.001 | ⚠ within organs, on part of the lines; also absent: BST2, DEPP1, TRIM22 |
| [[LAP3]] | B | CCDC194 activity raises LAP3's level | lines that do not express CCDC194 (19) vs lines expressing it (31) | 1.73× lower at baseline in the lines without CCDC194 | 0.003 | ⚠ within organs, on part of the lines; also absent: BST2, DEPP1, TRIM22 |
| [[CMPK2]] | B | CCDC194 activity raises CMPK2's level | lines that do not express CCDC194 (19) vs lines expressing it (31) | 2.69× lower at baseline in the lines without CCDC194 | 0.006 | ⚠ within organs, on part of the lines; also absent: BST2, DEPP1, TRIM22 |
| [[OAS2]] | B | CCDC194 activity raises OAS2's level | lines that do not express CCDC194 (19) vs lines expressing it (31) | 3.59× lower at baseline in the lines without CCDC194 | 0.007 | ⚠ within organs, on part of the lines; also absent: BST2, DEPP1, TRIM22 |
| [[PARP9]] | B | CCDC194 activity raises PARP9's level | lines that do not express CCDC194 (19) vs lines expressing it (31) | 2.22× lower at baseline in the lines without CCDC194 | 0.007 | ⚠ within organs, on part of the lines; also absent: BST2, DEPP1, TRIM22 |
| [[N4BP1]] | B | CCDC194 activity raises N4BP1's level | lines that do not express CCDC194 (19) vs lines expressing it (31) | 1.34× lower at baseline in the lines without CCDC194 | 0.007 | ⚠ within organs, on part of the lines; also absent: BST2, DEPP1, TRIM22 |
| [[USP18]] | B | CCDC194 activity raises USP18's level | lines that do not express CCDC194 (19) vs lines expressing it (31) | 2.09× lower at baseline in the lines without CCDC194 | 0.007 | ⚠ within organs, on part of the lines; also absent: BST2, DEPP1, TRIM22 |
| [[NRIR]] | B | CCDC194 activity raises NRIR's level | lines that do not express CCDC194 (19) vs lines expressing it (31) | 2.13× lower at baseline in the lines without CCDC194 | 0.007 | ⚠ within organs, on part of the lines; also absent: BST2, DEPP1, TRIM22 |
| [[PARP14]] | B | CCDC194 activity raises PARP14's level | lines that do not express CCDC194 (19) vs lines expressing it (31) | 2.14× lower at baseline in the lines without CCDC194 | 0.008 | ⚠ within organs, on part of the lines; also absent: BST2, DEPP1, TRIM22 |
| [[DTX3L]] | B | CCDC194 activity raises DTX3L's level | lines that do not express CCDC194 (19) vs lines expressing it (31) | 2.03× lower at baseline in the lines without CCDC194 | 0.009 | ⚠ within organs, on part of the lines; also absent: BST2, DEPP1, TRIM22 |
| [[IFI6]] | B | CCDC194 activity raises IFI6's level | lines that do not express CCDC194 (19) vs lines expressing it (31) | 2.60× lower at baseline in the lines without CCDC194 | 0.010 | ⚠ within organs, on part of the lines; also absent: BST2, DEPP1, TRIM22 |
| [[PLSCR1]] | B | CCDC194 activity raises PLSCR1's level | lines that do not express CCDC194 (19) vs lines expressing it (31) | 2.45× lower at baseline in the lines without CCDC194 | 0.010 | ⚠ within organs, on part of the lines; also absent: BST2, DEPP1, TRIM22 |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.790). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (50.6, 53.1); signed map (66.8, 30.7). **Vector** length 80.5, 20.3% of its response variance represented; |z| ≥ 3 in 812 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon alpha response* (hallmark, mean cos +0.65 to 56); *interferon gamma response* (hallmark, mean cos +0.66 to 60); *interferon* (control, mean cos +0.73 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.8 | +9.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +5.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +8.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.1 | +10.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.0 | -0.4 |
|  | [[Docetaxel (drug)]] 5 µM |  | +1.7 | +3.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.5 | +4.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.4 | +3.0 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -4.7 | -10.5 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -3.9 | -8.6 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -3.8 | -8.5 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -3.4 | -6.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.8 | -4.8 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 194 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:17,387,196-17,394,196 (-) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

UniProt [A0A1B0GVG4](https://www.uniprot.org/uniprotkb/A0A1B0GVG4) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:53438](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53438) · Entrez [110806280](https://www.ncbi.nlm.nih.gov/gene/110806280) · UniProt [A0A1B0GVG4](https://www.uniprot.org/uniprotkb/A0A1B0GVG4) · Ensembl [ENSG00000269720](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000269720)

## Data

Gene col 15630: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15630); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15630, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15630]; `tensor/DDL_lfc|DDL_z.npy` [15630]; `embed/gene_vectors.npy` [15630]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15630 or target_col == 15630). Every well: [[CCDC194 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC194.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
