---
symbol: "SERPIND1"
type: "gene"
col: 1830
ensembl_id: "ENSG00000099937"
name: "serpin family D member 1"
location: "22q11.21"
module: 19
arm: "+"
pooled_cpm: 2.1
n_lines_expressing: 34
n_dd_up: 13
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 20
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# SERPIND1

*serpin family D member 1* — 22q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 6.06× (z +11.5, q 6e-28, up in 2 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.80× (z +5.5, q 5e-06, up in 2 of 13 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (HepG2/C3A 0.0797×, NCI-H460 0.217×; ⚠ cell-cycle shift, explains ~77% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 0.0401×; ⚠ cell-cycle shift, would explain all of this change); [[Adagrasib (drug)]] 0.05 µM in 1 line (NCI-H1792 0.235×; ⚠ position not correctable); [[Trametinib (drug)]] 5 µM in 1 line (NCI-H460 0.111×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ESM1]] (+0.74, fdr 7e-06), [[CRLF2]] (+0.74, fdr 7e-06), [[UNC5D]] (+0.72, fdr 7e-06); moves opposite to [[STOM]] (-0.48, fdr 4e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ESM1]] → it (grade B ⚠); 20 go from it, the strongest it → [[TIMP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 11 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1830.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.06×** | +11.5 | 6e-28 | 2/3 (HepG2/C3A, NCI-H2030) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.92×** | +10.6 | 1e-23 | 2/5 (HOP62, HepG2/C3A) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.50×** | +6.4 | 3e-08 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +5.5 | 5e-06 | 2/13 (HepG2/C3A, LS 180) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.01×** | +4.6 | 4e-04 | 0/3 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.97×** | +4.3 | 0.001 | 1/4 (HepG2/C3A) | top dose only | cell-cycle shift (explains ~3% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.44×** | +4.2 | 0.002 | 0/3 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.76×** | +3.8 | 0.012 | 0/4 | top dose only | cell-cycle shift (explains ~23% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.72×** | +3.5 | 0.033 | 0/5 | top dose only | cell-cycle shift (explains ~17% here) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **2.04×** | +3.4 | 0.041 | 0/5 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.55×** | +3.2 | 0.060 | 1/3 (HepG2/C3A) | top dose only | noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.44×** | +3.1 | 0.092 | 0/3 | rises with dose | noisy plate (z scaled) |
| [[Fingolimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +3.1 | 0.095 | 1/11 (COLO 205) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1830.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (HepG2/C3A 0.0797×, NCI-H460 0.217×; ⚠ cell-cycle shift, explains ~77% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 0.0401×; ⚠ cell-cycle shift, would explain all of this change); [[Adagrasib (drug)]] 0.05 µM in 1 line (NCI-H1792 0.235×; ⚠ position not correctable); [[Trametinib (drug)]] 5 µM in 1 line (NCI-H460 0.111×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | 0.577× | -3.5 | 0.15 | 7/27 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.511× | -3.4 | 0.15 | 6/25 (NCI-H460, NCI-H1792, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.698× | -3.4 | 0.15 | 7/26 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.668× | -3.3 | 0.16 | 8/22 (NCI-H460, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1830. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 12.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0401× (z -13.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Trametinib (drug)]] 5 µM 0.111× (z -9.3) |
| [[HepG2_C3A (line)]] | wt | 55.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0797× (z -15.1) ⚠ cell-cycle shift, explains ~77% of this change |
| [[NCI-H1792 (line)]] | alt | 4.14 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.235× (z -13.1) ⚠ position not correctable |
| [[A-172 (line)]] | wt | 0.770 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.389 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.468 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.471 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.819 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.543 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.525 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.507 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.646 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.727 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.600 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.572 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.542 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.572 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.756 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.997 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.462 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.517 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.490 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.569 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.569 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.471 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.523 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.506 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.501 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.605 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.437 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.577 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.787 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.443 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.586 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.499 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.741 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.900 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.608 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.622 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.585 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.511 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1830), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ESM1]] | +0.74 | +0.66 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[CRLF2]] | +0.74 | +0.68 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[UNC5D]] | +0.72 | +0.64 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[GTF2IP7]] | +0.71 | +0.67 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[DOCK4]] | +0.71 | +0.70 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[GJA1]] | +0.70 | +0.59 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[GNG11]] | +0.70 | +0.71 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[AADACP1]] | +0.70 | +0.57 / +0.74 | both halves | 1e-05 | **novel candidate** |
| [[AADAC]] | +0.66 | +0.57 / +0.68 | both halves | 1e-05 | **novel candidate** |
| [[SCUBE1]] | +0.65 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[SEMA3A]] | +0.65 | +0.55 / +0.72 | both halves | 1e-05 |  |
| [[STEAP1B-AS1]] | +0.64 | +0.57 / +0.70 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STOM]] | -0.48 | -0.42 / -0.51 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ESM1]] | B | ESM1 activity raises SERPIND1's level | lines that do not express ESM1 (37) vs lines expressing it (13) | 1.33× lower at baseline in the lines without ESM1 | 0.061 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, DIRAS3, ENSG00000224865 |
| [[AADAC]] | B | AADAC activity raises SERPIND1's level | lines that do not express AADAC (34) vs lines expressing it (16) | 1.32× lower at baseline in the lines without AADAC | 0.062 | ⚠ within organs, on part of the lines; also absent: AADACP1, SUCNR1, LINC01610 |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 20, C 0. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TIMP1]] | B | SERPIND1 activity raises TIMP1's level | lines that do not express SERPIND1 (16) vs lines expressing it (34) | 2.70× lower at baseline in the lines without SERPIND1 | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000254303, ENSG00000287390, LANCL3; maybe low, not absent |
| [[SERPINE2]] | B | SERPIND1 activity raises SERPINE2's level | lines that do not express SERPIND1 (16) vs lines expressing it (34) | 3.75× lower at baseline in the lines without SERPIND1 | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000254303, ENSG00000287390, LANCL3; maybe low, not absent |
| [[LINC02742]] | B | SERPIND1 activity raises LINC02742's level | lines that do not express SERPIND1 (16) vs lines expressing it (34) | 2.35× lower at baseline in the lines without SERPIND1 | 0.019 | ⚠ within organs, on part of the lines; also absent: ENSG00000254303, ENSG00000287390, LANCL3; maybe low, not absent |
| [[AMOTL1]] | B | SERPIND1 activity raises AMOTL1's level | lines that do not express SERPIND1 (16) vs lines expressing it (34) | 2.40× lower at baseline in the lines without SERPIND1 | 0.019 | ⚠ within organs, on part of the lines; also absent: ENSG00000254303, ENSG00000287390, LANCL3; maybe low, not absent |
| [[FAM107B]] | B | SERPIND1 activity raises FAM107B's level | lines that do not express SERPIND1 (16) vs lines expressing it (34) | 2.08× lower at baseline in the lines without SERPIND1 | 0.023 | ⚠ within organs, on part of the lines; also absent: ENSG00000254303, ENSG00000287390, LANCL3; maybe low, not absent |
| [[CXCL8]] | B | SERPIND1 activity raises CXCL8's level | lines that do not express SERPIND1 (16) vs lines expressing it (34) | 2.29× lower at baseline in the lines without SERPIND1 | 0.030 | ⚠ within organs, on part of the lines; also absent: ENSG00000254303, ENSG00000287390, LANCL3; maybe low, not absent |
| [[ADAMTS6]] | B | SERPIND1 activity raises ADAMTS6's level | lines that do not express SERPIND1 (16) vs lines expressing it (34) | 3.07× lower at baseline in the lines without SERPIND1 | 0.043 | ⚠ within organs, on part of the lines; also absent: ENSG00000254303, ENSG00000287390, LANCL3; maybe low, not absent |
| [[ROR2]] | B | SERPIND1 activity lowers ROR2's level | lines that do not express SERPIND1 (16) vs lines expressing it (34) | 2.20× higher at baseline in the lines without SERPIND1 | 0.057 | ⚠ within organs, on part of the lines; also absent: ENSG00000254303, ENSG00000287390, LANCL3; maybe low, not absent |
| [[SMOX]] | B | SERPIND1 activity raises SMOX's level | lines that do not express SERPIND1 (16) vs lines expressing it (34) | 2.06× lower at baseline in the lines without SERPIND1 | 0.061 | ⚠ within organs, on part of the lines; also absent: ENSG00000254303, ENSG00000287390, LANCL3; maybe low, not absent |
| [[GABRE]] | B | SERPIND1 activity raises GABRE's level | lines that do not express SERPIND1 (16) vs lines expressing it (34) | 2.68× lower at baseline in the lines without SERPIND1 | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000254303, ENSG00000287390, LANCL3; maybe low, not absent |
| [[CRLF2]] | B | SERPIND1 activity raises CRLF2's level | lines that do not express SERPIND1 (16) vs lines expressing it (34) | 1.99× lower at baseline in the lines without SERPIND1 | 0.070 | ⚠ within organs, on part of the lines; also absent: ENSG00000254303, ENSG00000287390, LANCL3; maybe low, not absent |
| [[ANTXR2]] | B | SERPIND1 activity raises ANTXR2's level | lines that do not express SERPIND1 (16) vs lines expressing it (34) | 2.41× lower at baseline in the lines without SERPIND1 | 0.073 | ⚠ within organs, on part of the lines; also absent: ENSG00000254303, ENSG00000287390, LANCL3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.582). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.4, 15.7); signed map (18.9, 52.7). **Vector** length 40.9, 9.84% of its response variance represented; |z| ≥ 3 in 490 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +2.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.9 | +11.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.9 | +10.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.6 | +5.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.2 | +1.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.0 | +2.8 |
|  | [[Entrectinib (drug)]] 5 µM |  | +0.6 | +1.8 |
|  | [[Vilanterol (drug)]] 0.5 µM |  | +0.6 | +1.5 |
|  | [[Vilanterol (drug)]] 0.05 µM |  | +0.6 | +1.3 |
| fall | [[Trametinib (drug)]] 5 µM |  | -2.3 | -3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.0 | -3.4 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.7 | -0.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.6 | -2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.6 | -2.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.5 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | serpin family D member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.21 — chr22:20,774,113-20,787,720 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HC-II, HLS2, HC2, D22S673; previously HCF2 |
| Gene groups (HGNC) | Serpin peptidase inhibitors |
| Reactome | 7 pathways, smallest: Amplification and propagation of coagulation cascade; Fibrin formation; Regulation of clotting cascade |
| Matched by | ensembl_id |

**Function**, from UniProt [P05546](https://www.uniprot.org/uniprotkb/P05546) (Heparin cofactor 2):

> Thrombin inhibitor activated by the glycosaminoglycans, heparin or dermatan sulfate. In the presence of the latter, HC-II becomes the predominant thrombin inhibitor in place of antithrombin III (AT-III). Also inhibits chymotrypsin, but in a glycosaminoglycan-independent manner.; Peptides at the N-terminal of HC-II have chemotactic activity for both monocytes and neutrophils.; [Isoform 2]: Shows negligible inhibition, in vitro, of thrombin and tPA and no inhibition of factor Xa, in vitro.

**Summary**, from NCBI Gene [3053](https://www.ncbi.nlm.nih.gov/gene/3053):

> This gene belongs to the serpin gene superfamily. Serpins play roles in many processes including inflammation, blood clotting, and cancer metastasis. Members of this family have highly conserved secondary structures with a reactive center loop that interacts with the protease active site to inhibit protease activity. This gene encodes a plasma serine protease that functions as a thrombin and chymotrypsin inhibitor. The protein is activated by heparin, dermatan sulfate, and glycosaminoglycans. …

**Accessions** — [HGNC:4838](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4838) · Entrez [3053](https://www.ncbi.nlm.nih.gov/gene/3053) · UniProt [P05546](https://www.uniprot.org/uniprotkb/P05546) · Ensembl [ENSG00000099937](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099937)

## Data

Gene col 1830: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1830); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1830, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1830]; `tensor/DDL_lfc|DDL_z.npy` [1830]; `embed/gene_vectors.npy` [1830]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1830 or target_col == 1830). Every well: [[SERPIND1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SERPIND1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
