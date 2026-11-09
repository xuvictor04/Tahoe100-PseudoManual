---
symbol: "ADAMTS18"
type: "gene"
col: 6459
ensembl_id: "ENSG00000140873"
name: "ADAM metallopeptidase with thrombospondin type 1 motif 18"
location: "16q23.1"
module: 13
arm: "+"
pooled_cpm: 3.5
n_lines_expressing: 27
n_dd_up: 11
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 13
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# ADAMTS18

*ADAM metallopeptidase with thrombospondin type 1 motif 18* — 16q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.79× (z +13.2, q 3e-37, up in 3 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.62× (z +11.5, q 3e-28, up in 7 of 15 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (NCI-H23 0.0694×, SNU-423 0.125×, LOX-IMVI 0.209×); [[Panobinostat (drug)]] 0.5 µM in 2 lines (LOX-IMVI 0.103×, SNU-423 0.119×; ⚠ cell-cycle shift, explains ~86% of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (LOX-IMVI 0.134×, SNU-423 0.122×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (LOX-IMVI 0.106×); [[Harringtonine (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.0834×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NTM]] (+0.73, fdr 7e-06), [[SAMD3]] (+0.70, fdr 7e-06), [[SHANK1]] (+0.69, fdr 7e-06); moves opposite to [[B4GALT1]] (-0.44, fdr 9e-05), [[FOXG1]] (-0.41, fdr 2e-04).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[NTM]] → it (grade C ⚠); 13 go from it, the strongest it → [[HEYL]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6459.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.79×** | +13.2 | 3e-37 | 3/8 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.62×** | +11.5 | 3e-28 | 7/15 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.89×** | +11.0 | 4e-26 | 1/5 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.47×** | +9.7 | 3e-20 | 1/5 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.54×** | +5.1 | 3e-05 | 7/21 (RPMI-7951, NCI-H1573, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.80×** | +4.9 | 7e-05 | 2/17 (HS-578T, C32) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.51×** | +4.9 | 8e-05 | 2/15 (A-172, NCI-H2030) | top dose only | cell-cycle shift (explains ~12% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.30×** | +3.7 | 0.016 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +3.5 | 0.033 | 1/10 (J82) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.49×** | +3.4 | 0.044 | 2/18 (A-172, CFPAC-1) | top dose only |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.73×** | +3.3 | 0.047 | 0/6 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | 1.43× | +3.0 | 0.12 | 0/6 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6459.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (NCI-H23 0.0694×, SNU-423 0.125×, LOX-IMVI 0.209×); [[Panobinostat (drug)]] 0.5 µM in 2 lines (LOX-IMVI 0.103×, SNU-423 0.119×; ⚠ cell-cycle shift, explains ~86% of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (LOX-IMVI 0.134×, SNU-423 0.122×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (LOX-IMVI 0.106×); [[Harringtonine (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.0834×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | 0.655× | -3.5 | 0.21 | 5/21 (HOP62, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.672× | -3.4 | 0.21 | 8/21 (SW480, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6459. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 31.8 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -15.3) |
| [[NCI-H23 (line)]] | alt | 13.8 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0694× (z -13.3) |
| [[SNU-423 (line)]] | alt | 24.5 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.125× (z -12.9) |
| [[HOP62 (line)]] | alt | 5.19 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0517× (z -9.9) ⚠ toxic |
| [[A-172 (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.966 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.853 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.734 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.754 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.811 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.929 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.755 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.51 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.800 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.799 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.852 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.692 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.832 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.716 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.668 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.660 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.621 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.888 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.649 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.757 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.651 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.901 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.777 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.741 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.779 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.793 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.789 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.803 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 15.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6459), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NTM]] | +0.73 | +0.80 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[SAMD3]] | +0.70 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[SHANK1]] | +0.69 | +0.62 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[CACNA1A]] | +0.65 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[TMEM200A]] | +0.65 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[DSCAM]] | +0.62 | +0.46 / +0.64 | both halves | 3e-05 | **novel candidate** |
| [[RFX8]] | +0.62 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[VEPH1]] | +0.61 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[FAM167A]] | +0.61 | +0.57 / +0.53 | both halves | 1e-05 | **novel candidate** |
| [[NLRP3]] | +0.59 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[NETO1]] | +0.59 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[BCL11B]] | +0.58 | +0.51 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[B4GALT1]] | -0.44 | -0.40 / -0.36 | both halves | 9e-05 | pathway: Diseases of glycosylation |
| [[FOXG1]] | -0.41 | -0.38 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NTM]] | C | NTM activity raises ADAMTS18's level | lines that do not express NTM (33) vs lines expressing it (17) | 2.42× lower at baseline in the lines without NTM | 0.038 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000222032, CDH13, THY1; co-absent with the target |
| [[VAT1L]] | C | VAT1L activity raises ADAMTS18's level | lines that do not express VAT1L (23) vs lines expressing it (27) | 2.17× lower at baseline in the lines without VAT1L | 0.039 | ⚠ within organs, on part of the lines; also absent: RBM20, ENSG00000242880, CHST8; maybe low, not absent; co-absent with the target |
| [[MEG3]] | C | MEG3 activity raises ADAMTS18's level | lines that do not express MEG3 (35) vs lines expressing it (15) | 1.87× lower at baseline in the lines without MEG3 | 0.068 | ⚠ within organs, on part of the lines; also absent: MIR493HG, MEG8, MXRA8; co-absent with the target |
| [[FOXG1]] | C | FOXG1 activity raises ADAMTS18's level | lines that do not express FOXG1 (36) vs lines expressing it (14) | 2.19× lower at baseline in the lines without FOXG1 | 0.077 | ⚠ within organs, on part of the lines; co-absent genes; also absent: LINC02566, MMRN1, GCG; co-absent with the target |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 4, C 9. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HEYL]] | B | ADAMTS18 activity raises HEYL's level | lines that do not express ADAMTS18 (23) vs lines expressing it (27) | 1.70× lower at baseline in the lines without ADAMTS18 | 0.035 | ⚠ within organs, on part of the lines; also absent: TSHZ3, TWIST2, INSYN2B; maybe low, not absent |
| [[HMGA2-AS1]] | B | ADAMTS18 activity raises HMGA2-AS1's level | lines that do not express ADAMTS18 (23) vs lines expressing it (27) | 1.51× lower at baseline in the lines without ADAMTS18 | 0.056 | ⚠ within organs, on part of the lines; also absent: TSHZ3, TWIST2, INSYN2B; maybe low, not absent |
| [[LINC02454]] | B | ADAMTS18 activity raises LINC02454's level | lines that do not express ADAMTS18 (23) vs lines expressing it (27) | 2.19× lower at baseline in the lines without ADAMTS18 | 0.064 | ⚠ within organs, on part of the lines; also absent: TSHZ3, TWIST2, INSYN2B; maybe low, not absent |
| [[C2orf92]] | B | ADAMTS18 activity raises C2orf92's level | lines that do not express ADAMTS18 (23) vs lines expressing it (27) | 1.83× lower at baseline in the lines without ADAMTS18 | 0.079 | ⚠ within organs, on part of the lines; also absent: TSHZ3, TWIST2, INSYN2B; maybe low, not absent |
| [[TSHZ3]] | C | ADAMTS18 activity raises TSHZ3's level | lines that do not express ADAMTS18 (23) vs lines expressing it (27) | 8.80× lower at baseline in the lines without ADAMTS18 | 4e-04 | ⚠ within organs, on part of the lines; also absent: TSHZ3, TWIST2, INSYN2B; maybe low, not absent; co-absent with the target |
| [[INSYN2B]] | C | ADAMTS18 activity raises INSYN2B's level | lines that do not express ADAMTS18 (23) vs lines expressing it (27) | 5.64× lower at baseline in the lines without ADAMTS18 | 0.017 | ⚠ within organs, on part of the lines; also absent: TSHZ3, TWIST2, INSYN2B; maybe low, not absent; co-absent with the target |
| [[MEG3]] | C | ADAMTS18 activity raises MEG3's level | lines that do not express ADAMTS18 (23) vs lines expressing it (27) | 4.19× lower at baseline in the lines without ADAMTS18 | 0.020 | ⚠ within organs, on part of the lines; also absent: TSHZ3, TWIST2, INSYN2B; maybe low, not absent; co-absent with the target |
| [[NTNG2]] | C | ADAMTS18 activity raises NTNG2's level | lines that do not express ADAMTS18 (23) vs lines expressing it (27) | 2.36× lower at baseline in the lines without ADAMTS18 | 0.043 | ⚠ within organs, on part of the lines; also absent: TSHZ3, TWIST2, INSYN2B; maybe low, not absent; co-absent with the target |
| [[RFX8]] | C | ADAMTS18 activity raises RFX8's level | lines that do not express ADAMTS18 (23) vs lines expressing it (27) | 3.67× lower at baseline in the lines without ADAMTS18 | 0.057 | ⚠ within organs, on part of the lines; also absent: TSHZ3, TWIST2, INSYN2B; maybe low, not absent; co-absent with the target |
| [[HAS2]] | C | ADAMTS18 activity raises HAS2's level | lines that do not express ADAMTS18 (23) vs lines expressing it (27) | 3.10× lower at baseline in the lines without ADAMTS18 | 0.075 | ⚠ within organs, on part of the lines; also absent: TSHZ3, TWIST2, INSYN2B; maybe low, not absent; co-absent with the target |
| [[MGAT5B]] | C | ADAMTS18 activity raises MGAT5B's level | lines that do not express ADAMTS18 (23) vs lines expressing it (27) | 2.93× lower at baseline in the lines without ADAMTS18 | 0.075 | ⚠ within organs, on part of the lines; also absent: TSHZ3, TWIST2, INSYN2B; maybe low, not absent; co-absent with the target |
| [[VAT1L]] | C | ADAMTS18 activity raises VAT1L's level | lines that do not express ADAMTS18 (23) vs lines expressing it (27) | 2.65× lower at baseline in the lines without ADAMTS18 | 0.083 | ⚠ within organs, on part of the lines; also absent: TSHZ3, TWIST2, INSYN2B; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.517). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (50.6, 13.1); signed map (19.3, 47.3). **Vector** length 44.5, 9.25% of its response variance represented; |z| ≥ 3 in 591 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +11.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.7 | +13.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | +9.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +11.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +5.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +2.7 |
|  | [[EX229 (drug)]] 5 µM |  | +1.0 | +2.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.9 | +1.5 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +0.9 | +1.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.9 | -3.4 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.4 | -1.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -2.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.2 | -1.8 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.0 | -2.5 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.0 | -0.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -0.9 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | ADAM metallopeptidase with thrombospondin type 1 motif 18 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q23.1 — chr16:77,247,813-77,435,034 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ADAMTS21 |
| Gene groups (HGNC) | ADAM metallopeptidases with thrombospondin type 1 motif |
| Reactome | 8 pathways, smallest: Defective B3GALTL causes PpS; O-glycosylation of TSR domain-containing proteins; Diseases associated with O-glycosylation of proteins |
| Matched by | ensembl_id |

UniProt [Q8TE60](https://www.uniprot.org/uniprotkb/Q8TE60) carries no function annotation.

**Summary**, from NCBI Gene [170692](https://www.ncbi.nlm.nih.gov/gene/170692):

> This gene encodes a member of the ADAMTS (a disintegrin and metalloproteinase with thrombospondin motifs) protein family. ADAMTS family members share several distinct protein modules, including a propeptide region, a metalloproteinase domain, a disintegrin-like domain, and a thrombospondin type 1 (TS) motif. Individual members of this family differ in the number of C-terminal TS motifs, and some have unique C-terminal domains. The encoded preproprotein is proteolytically processed to generate …

**Accessions** — [HGNC:17110](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17110) · Entrez [170692](https://www.ncbi.nlm.nih.gov/gene/170692) · UniProt [Q8TE60](https://www.uniprot.org/uniprotkb/Q8TE60) · Ensembl [ENSG00000140873](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140873)

## Data

Gene col 6459: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6459); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6459, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6459]; `tensor/DDL_lfc|DDL_z.npy` [6459]; `embed/gene_vectors.npy` [6459]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6459 or target_col == 6459). Every well: [[ADAMTS18 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADAMTS18.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
