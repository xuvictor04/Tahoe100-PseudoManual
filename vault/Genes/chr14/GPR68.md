---
symbol: "GPR68"
type: "gene"
col: 4108
ensembl_id: "ENSG00000119714"
name: "G protein-coupled receptor 68"
location: "14q32.11"
module: 13
arm: "+"
pooled_cpm: 2.3
n_lines_expressing: 34
n_dd_up: 9
n_dd_down: 5
n_dd_up_clean: 3
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 27
direction_downstream: 8
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# GPR68

*G protein-coupled receptor 68* — 14q32.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.80× (z +12.4, q 9e-33, up in 2 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.52× (z +4.9, q 2e-04, up in 1 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.561× (z -4.8, q 9e-04, down in 8 of 19 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SAMD3]] (+0.81, fdr 7e-06), [[RFX8]] (+0.78, fdr 7e-06), [[GDNF]] (+0.77, fdr 7e-06).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 27 arrows point to it, the strongest [[RFX8]] → it (grade B ⚠); 8 go from it, the strongest it → [[SPOCD1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4108.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.80×** | +12.4 | 9e-33 | 2/5 (NCI-H2347, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.44×** | +10.2 | 6e-22 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.19×** | +8.5 | 4e-15 | 1/6 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +4.9 | 2e-04 | 1/16 (LoVo) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.60×** | +3.9 | 0.013 | 0/5 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.36×** | +3.6 | 0.035 | 1/16 (NCI-H2030) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +3.4 | 0.048 | 2/8 (NCI-H2347, A-172) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.76×** | +3.3 | 0.062 | 0/6 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.75×** | +3.3 | 0.065 | 1/11 (H4) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Roxadustat (drug)]] 0.05 µM |  | 1.53× | +3.1 | 0.10 | 0/10 | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 1.45× | +3.1 | 0.11 | 2/11 (hTERT-HPNE, NCI-H2347) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4108.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.561×** | -4.8 | 9e-04 | 8/19 (H4, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.580×** | -4.5 | 0.002 | 12/23 (HOP62, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.612×** | -4.1 | 0.009 | 12/24 (HOP62, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~1% here); position effect removed |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.617×** | -4.0 | 0.009 | 7/23 (H4, hTERT-HPNE, …) | two highest doses |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.665×** | -3.4 | 0.081 | 9/25 (H4, NCI-H1792, …) | two highest doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.680× | -3.2 | 0.13 | 10/24 (HOP62, HEC-1-A, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4108. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 17.2 | 0 | 10 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0891× (z -13.2) |
| [[NCI-H1792 (line)]] | alt | 15.7 | 0 | 5 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.438× (z -12.4) ⚠ position not correctable · without an alert: [[Belinostat (drug)]] 5 µM 0.102× (z -9.7) |
| [[H4 (line)]] | wt | 8.81 | 0 | 2 | — | [[Budesonide (drug)]] 0.5 µM 0.0344× (z -9.8) |
| [[A-172 (line)]] | wt | 7.59 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.103× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 11.7 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0903× (z -8.6) |
| [[A-427 (line)]] | wt | 0.645 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.313 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.544 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.385 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.642 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.394 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.692 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.385 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.731 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.429 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.490 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.895 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.430 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.89 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.599 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.941 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.846 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.96 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.408 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.505 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.617 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.767 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.599 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.383 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.746 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.528 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.783 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.727 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.458 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.677 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.567 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.389 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.437 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4108), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAMD3]] | +0.81 | +0.73 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[RFX8]] | +0.78 | +0.79 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[GDNF]] | +0.77 | +0.69 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[TMEM200A]] | +0.76 | +0.70 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[SPOCD1]] | +0.73 | +0.76 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[SHANK1]] | +0.73 | +0.74 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[ITGA11]] | +0.72 | +0.71 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[INSYN2B]] | +0.70 | +0.62 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[EVA1A]] | +0.70 | +0.63 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[SYNDIG1]] | +0.70 | +0.65 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[IL1B]] | +0.69 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[IL11]] | +0.69 | +0.59 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 27, C 0. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RFX8]] | B | RFX8 activity raises GPR68's level | lines that do not express RFX8 (35) vs lines expressing it (15) | 2.41× lower at baseline in the lines without RFX8 | 0.002 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, IRAG2, CARMN |
| [[EDNRA]] | B | EDNRA activity raises GPR68's level | lines that do not express EDNRA (32) vs lines expressing it (18) | 2.44× lower at baseline in the lines without EDNRA | 0.004 | ⚠ within organs, on part of the lines; also absent: CCBE1, G0S2, ADAMTS12 |
| [[SLC43A3]] | B | SLC43A3 activity raises GPR68's level | lines that do not express SLC43A3 (28) vs lines expressing it (22) | 2.36× lower at baseline in the lines without SLC43A3 | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000254979, FN1, ENSG00000234261 |
| [[LINC01411]] | B | LINC01411 activity raises GPR68's level | lines that do not express LINC01411 (38) vs lines expressing it (12) | 2.87× lower at baseline in the lines without LINC01411 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: VCAM1, TMPRSS15, ENSG00000222032 |
| [[SPOCD1]] | B | SPOCD1 activity raises GPR68's level | lines that do not express SPOCD1 (25) vs lines expressing it (25) | 2.07× lower at baseline in the lines without SPOCD1 | 0.019 | ⚠ within organs, on part of the lines; also absent: IL7R, ARMCX1, IDO1 |
| [[APCDD1L]] | B | APCDD1L activity raises GPR68's level | lines that do not express APCDD1L (34) vs lines expressing it (16) | 2.39× lower at baseline in the lines without APCDD1L | 0.026 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MMP2, ENSG00000222032, PHACTR1 |
| [[EVA1A-AS]] | B | EVA1A-AS activity raises GPR68's level | lines that do not express EVA1A-AS (22) vs lines expressing it (28) | 1.81× lower at baseline in the lines without EVA1A-AS | 0.029 | ⚠ within organs, on part of the lines; also absent: ENSG00000254979, RFX8, SULT1C2; maybe low, not absent |
| [[SAMD3]] | B | SAMD3 activity raises GPR68's level | lines that do not express SAMD3 (32) vs lines expressing it (18) | 2.07× lower at baseline in the lines without SAMD3 | 0.030 | ⚠ within organs, on part of the lines; also absent: TMEM200A, LINC01615, ITGA11 |
| [[TNS1]] | B | TNS1 activity raises GPR68's level | lines that do not express TNS1 (23) vs lines expressing it (27) | 1.75× lower at baseline in the lines without TNS1 | 0.031 | ⚠ within organs, on part of the lines; also absent: C5orf46, LINC02970, ENSG00000223786 |
| [[ADAMTS12]] | B | ADAMTS12 activity raises GPR68's level | lines that do not express ADAMTS12 (33) vs lines expressing it (17) | 2.24× lower at baseline in the lines without ADAMTS12 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC01411, APBB1IP, VCAM1 |
| [[WNT5A]] | B | WNT5A activity raises GPR68's level | lines that do not express WNT5A (30) vs lines expressing it (20) | 1.96× lower at baseline in the lines without WNT5A | 0.043 | ⚠ within organs, on part of the lines; also absent: APCDD1L, ABCC9, CDH13 |
| [[ITGA11]] | B | ITGA11 activity raises GPR68's level | lines that do not express ITGA11 (34) vs lines expressing it (16) | 2.29× lower at baseline in the lines without ITGA11 | 0.048 | ⚠ within organs, on part of the lines; also absent: GYPC, INSYN2B, LINC01411 |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPOCD1]] | B | GPR68 activity raises SPOCD1's level | lines that do not express GPR68 (16) vs lines expressing it (34) | 2.85× lower at baseline in the lines without GPR68 | 0.025 | ⚠ within organs, on part of the lines; also absent: ELOVL4, CPE, NOTCH3; maybe low, not absent |
| [[COL6A1]] | B | GPR68 activity raises COL6A1's level | lines that do not express GPR68 (16) vs lines expressing it (34) | 2.76× lower at baseline in the lines without GPR68 | 0.036 | ⚠ within organs, on part of the lines; also absent: ELOVL4, CPE, NOTCH3; maybe low, not absent |
| [[FAM167A]] | B | GPR68 activity raises FAM167A's level | lines that do not express GPR68 (16) vs lines expressing it (34) | 2.17× lower at baseline in the lines without GPR68 | 0.037 | ⚠ within organs, on part of the lines; also absent: ELOVL4, CPE, NOTCH3; maybe low, not absent |
| [[ARHGAP22]] | B | GPR68 activity raises ARHGAP22's level | lines that do not express GPR68 (16) vs lines expressing it (34) | 3.10× lower at baseline in the lines without GPR68 | 0.037 | ⚠ within organs, on part of the lines; also absent: ELOVL4, CPE, NOTCH3; maybe low, not absent |
| [[COL6A2]] | B | GPR68 activity raises COL6A2's level | lines that do not express GPR68 (16) vs lines expressing it (34) | 3.42× lower at baseline in the lines without GPR68 | 0.048 | ⚠ within organs, on part of the lines; also absent: ELOVL4, CPE, NOTCH3; maybe low, not absent |
| [[EDNRA]] | B | GPR68 activity raises EDNRA's level | lines that do not express GPR68 (16) vs lines expressing it (34) | 2.50× lower at baseline in the lines without GPR68 | 0.079 | ⚠ within organs, on part of the lines; also absent: ELOVL4, CPE, NOTCH3; maybe low, not absent |
| [[SAMD3]] | B | GPR68 activity raises SAMD3's level | lines that do not express GPR68 (16) vs lines expressing it (34) | 2.48× lower at baseline in the lines without GPR68 | 0.085 | ⚠ within organs, on part of the lines; also absent: ELOVL4, CPE, NOTCH3; maybe low, not absent |
| [[ADAMTS12]] | B | GPR68 activity raises ADAMTS12's level | lines that do not express GPR68 (16) vs lines expressing it (34) | 2.43× lower at baseline in the lines without GPR68 | 0.094 | ⚠ within organs, on part of the lines; also absent: ELOVL4, CPE, NOTCH3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.746). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (50.4, 13.9); signed map (19.6, 47.9). **Vector** length 58.8, 14.5% of its response variance represented; |z| ≥ 3 in 684 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Degradation of the extracellular matrix* (reactome, mean cos +0.50 to 11); *Collagen degradation* (reactome, mean cos +0.51 to 8); *Collagen chain trimerization* (reactome, mean cos +0.51 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +12.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.6 | +10.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.3 | +8.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +1.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.8 | +4.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.2 | +3.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.1 | +2.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.0 | +2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.0 | +2.1 |
| fall | [[Trametinib (drug)]] 5 µM |  | -2.3 | -2.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.0 | -4.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -2.8 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.8 | -2.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.8 | -1.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.7 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | G protein-coupled receptor 68 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.11 — chr14:91,232,532-91,253,925 (-) |
| Ensembl biotype | protein_coding |
| Also known as | OGR1 |
| Gene groups (HGNC) | G protein-coupled receptors, Class A orphans |
| Reactome | 5 pathways, smallest: Class A/1 (Rhodopsin-like receptors); G alpha (q) signalling events; GPCR ligand binding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15743](https://www.uniprot.org/uniprotkb/Q15743) (G protein-coupled receptor 68):

> Proton-sensing G protein-coupled receptor activated by extracellular pH, which is required to monitor pH changes and generate adaptive reactions. The receptor is almost silent at pH 7.8 but fully activated at pH 6.8. Ligand binding causes a conformation change that triggers signaling via guanine nucleotide-binding proteins (G proteins) and modulates the activity of downstream effectors, such as phospholipase C. GPR68 is mainly coupled to G(q) G proteins and mediates production of diacylglycerol …

**Summary**, from NCBI Gene [8111](https://www.ncbi.nlm.nih.gov/gene/8111):

> The protein encoded by this gene is a G protein-coupled receptor for sphingosylphosphorylcholine. The encoded protein is a proton-sensing receptor, inactive at pH 7.8 but active at pH 6.8. Mutations in this gene are a cause of amelogenesis imperfecta. [provided by RefSeq, Feb 2017]

**Accessions** — [HGNC:4519](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4519) · Entrez [8111](https://www.ncbi.nlm.nih.gov/gene/8111) · UniProt [Q15743](https://www.uniprot.org/uniprotkb/Q15743) · Ensembl [ENSG00000119714](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119714)

## Data

Gene col 4108: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4108); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4108, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4108]; `tensor/DDL_lfc|DDL_z.npy` [4108]; `embed/gene_vectors.npy` [4108]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4108 or target_col == 4108). Every well: [[GPR68 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPR68.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
