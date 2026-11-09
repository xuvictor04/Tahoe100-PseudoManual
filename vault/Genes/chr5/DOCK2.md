---
symbol: "DOCK2"
type: "gene"
col: 5571
ensembl_id: "ENSG00000134516"
name: "dedicator of cytokinesis 2"
location: "5q35.1"
module: 13
arm: "+"
pooled_cpm: 4.48
n_lines_expressing: 29
n_dd_up: 18
n_dd_down: 3
n_dd_up_clean: 9
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 20
direction_downstream: 18
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# DOCK2

*dedicator of cytokinesis 2* — 5q35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.26× (z +17.8, q 0e+00, up in 12 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Artesunate (drug)]] 5 µM: 0.752× (z -4.3, q 0.009, down in 6 of 24 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZPLD1]] (+0.72, fdr 7e-06), [[SETBP1]] (+0.66, fdr 1e-05), [[MIR4280HG]] (+0.65, fdr 2e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 20 arrows point to it, the strongest [[HHIP]] → it (grade B ⚠); 18 go from it, the strongest it → [[CHST14]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5571.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.26×** | +17.8 | 0e+00 | 12/19 (A498, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.88×** | +14.4 | 1e-44 | 7/12 (SNU-423, SW 900, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.60×** | +13.1 | 8e-37 | 7/9 (A498, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.53×** | +12.4 | 4e-33 | 5/10 (C32, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.67×** | +7.7 | 2e-12 | 7/23 (PANC-1, HS-578T, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.85×** | +6.5 | 6e-09 | 7/22 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.62×** | +5.1 | 3e-05 | 1/11 (A498) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~17% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.40×** | +5.0 | 3e-05 | 7/21 (HS-578T, SHP-77, …) | top dose only | composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.35×** | +4.7 | 1e-04 | 4/8 (SNU-423, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +4.1 | 0.002 | 6/21 (A-172, NCI-H460, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.46×** | +4.0 | 0.003 | 1/18 (A549) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +3.9 | 0.005 | 6/17 (HS-578T, SNU-423, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +3.9 | 0.005 | 1/14 (SK-MEL-2) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +3.8 | 0.007 | 8/23 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Naproxen (drug)]] 0.05 µM |  | **1.38×** | +3.1 | 0.067 | 1/16 (NCI-H1573) | inconsistent across doses | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.50×** | +3.1 | 0.067 | 0/19 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.33×** | +3.0 | 0.085 | 2/21 (NCI-H1573, NCI-H460) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5571.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM |  | **0.752×** | -4.3 | 0.009 | 6/24 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Artesunate (drug)]] 0.5 µM |  | **0.698×** | -3.8 | 0.033 | 2/23 (A498, NCI-H2030) | rises with dose |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.704×** | -3.8 | 0.033 | 2/25 (AN3 CA, SHP-77) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.808× | -3.2 | 0.17 | 7/25 (NCI-H460, C32, …) | top dose only |  |
| [[LY-2584702 (tosylate salt) (drug)]] 0.05 µM |  | 0.730× | -3.2 | 0.17 | 3/22 (HEC-1-A, NCI-H2030, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5571. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 1.96 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.49× (z +10.0) | — |
| [[RPMI-7951 (line)]] | alt | 20.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0916× (z -14.7) ⚠ cell-cycle shift, explains ~27% of this change |
| [[A-172 (line)]] | wt | 37.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.851 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.944 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.966 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 7.27 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.988 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.66 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.950 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 7.34 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.969 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.856 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.857 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.884 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.979 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.995 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5571), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZPLD1]] | +0.72 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[SETBP1]] | +0.66 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[MIR4280HG]] | +0.65 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[SORCS2]] | +0.65 | +0.58 / +0.61 | both halves | 7e-06 | same gene group |
| [[LAMA4]] | +0.65 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[COL15A1]] | +0.65 | +0.57 / +0.67 | both halves | 9e-06 |  |
| [[APCDD1L]] | +0.64 | +0.69 / +0.58 | both halves | 7e-06 |  |
| [[EVA1A]] | +0.64 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[CTHRC1]] | +0.63 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[DIRC3-AS1]] | +0.61 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[RDUR]] | +0.60 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[FGF1]] | +0.60 | +0.49 / +0.67 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 7, C 13. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HHIP]] | B | HHIP activity raises DOCK2's level | lines that do not express HHIP (33) vs lines expressing it (17) | 1.68× lower at baseline in the lines without HHIP | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL5A1, PLPP4, LINC01411; maybe low, not absent |
| [[TMEM200A]] | B | TMEM200A activity raises DOCK2's level | lines that do not express TMEM200A (29) vs lines expressing it (21) | 2.27× lower at baseline in the lines without TMEM200A | 0.015 | ⚠ within organs, on part of the lines; also absent: SAMD3, ITGA11, LINC01615 |
| [[TOP2A]] | B | TOP2A activity lowers DOCK2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SAMD3]] | B | SAMD3 activity raises DOCK2's level | lines that do not express SAMD3 (32) vs lines expressing it (18) | 2.32× lower at baseline in the lines without SAMD3 | 0.020 | ⚠ within organs, on part of the lines; also absent: TMEM200A, LINC01615, ITGA11 |
| [[C12orf75-AS1]] | B | C12orf75-AS1 activity raises DOCK2's level | lines that do not express C12orf75-AS1 (22) vs lines expressing it (28) | 1.89× lower at baseline in the lines without C12orf75-AS1 | 0.041 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, FOXC2, GLIPR1 |
| [[ANGPTL2]] | B | ANGPTL2 activity raises DOCK2's level | lines that do not express ANGPTL2 (29) vs lines expressing it (21) | 1.86× lower at baseline in the lines without ANGPTL2 | 0.091 | ⚠ within organs, on part of the lines; also absent: LINC01611, ENSG00000189229, CDH13; maybe low, not absent |
| [[EVA1A]] | B | EVA1A activity raises DOCK2's level | lines that do not express EVA1A (21) vs lines expressing it (29) | 2.05× lower at baseline in the lines without EVA1A | 0.099 | ⚠ within organs, on part of the lines; also absent: NLRP1, MILR1, SNAI2 |
| [[INSYN2B]] | C | INSYN2B activity raises DOCK2's level | lines that do not express INSYN2B (31) vs lines expressing it (19) | 3.34× lower at baseline in the lines without INSYN2B | 0.004 | ⚠ within organs, on part of the lines; also absent: MMP2, ITGA11, FGF5; co-absent with the target |
| [[ITGA11]] | C | ITGA11 activity raises DOCK2's level | lines that do not express ITGA11 (34) vs lines expressing it (16) | 3.02× lower at baseline in the lines without ITGA11 | 0.006 | ⚠ within organs, on part of the lines; also absent: GYPC, INSYN2B, LINC01411; co-absent with the target |
| [[COL15A1]] | C | COL15A1 activity raises DOCK2's level | lines that do not express COL15A1 (28) vs lines expressing it (22) | 2.93× lower at baseline in the lines without COL15A1 | 0.008 | ⚠ within organs, on part of the lines; also absent: LINC01583, PHACTR1, GYPC; co-absent with the target |
| [[FRMD4A]] | C | FRMD4A activity raises DOCK2's level | lines that do not express FRMD4A (24) vs lines expressing it (26) | 2.71× lower at baseline in the lines without FRMD4A | 0.011 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, PTGFR, TNFAIP6; co-absent with the target |
| [[MIR3681HG]] | C | MIR3681HG activity raises DOCK2's level | lines that do not express MIR3681HG (27) vs lines expressing it (23) | 2.18× lower at baseline in the lines without MIR3681HG | 0.014 | ⚠ within organs, on part of the lines; also absent: ENSG00000225649, BAALC, LINC02930; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 6, C 12. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CHST14]] | B | DOCK2 activity raises CHST14's level | lines that do not express DOCK2 (21) vs lines expressing it (29) | 1.71× lower at baseline in the lines without DOCK2 | 0.032 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, KCTD16; maybe low, not absent |
| [[C2orf92]] | B | DOCK2 activity raises C2orf92's level | lines that do not express DOCK2 (21) vs lines expressing it (29) | 1.83× lower at baseline in the lines without DOCK2 | 0.039 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, KCTD16; maybe low, not absent |
| [[ARNT2]] | B | DOCK2 activity raises ARNT2's level | lines that do not express DOCK2 (21) vs lines expressing it (29) | 2.09× lower at baseline in the lines without DOCK2 | 0.054 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, KCTD16; maybe low, not absent |
| [[MYOSLID]] | B | DOCK2 activity raises MYOSLID's level | lines that do not express DOCK2 (21) vs lines expressing it (29) | 2.29× lower at baseline in the lines without DOCK2 | 0.059 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, KCTD16; maybe low, not absent |
| [[LOXL1]] | B | DOCK2 activity raises LOXL1's level | lines that do not express DOCK2 (21) vs lines expressing it (29) | 2.06× lower at baseline in the lines without DOCK2 | 0.073 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, KCTD16; maybe low, not absent |
| cells under [[Pravastatin (sodium) (drug)]] 5 µM | B | DOCK2 activity raises the cells' numbers under Pravastatin (sodium) 5 µM (protects the cells) | lines that do not express DOCK2 (21) vs lines expressing it (27) | the lines without DOCK2: 0.87× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, KCTD16; maybe low, not absent |
| [[ANTXR1]] | C | DOCK2 activity raises ANTXR1's level | lines that do not express DOCK2 (21) vs lines expressing it (29) | 6.06× lower at baseline in the lines without DOCK2 | 0.020 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, KCTD16; maybe low, not absent; co-absent with the target |
| [[CNRIP1]] | C | DOCK2 activity raises CNRIP1's level | lines that do not express DOCK2 (21) vs lines expressing it (29) | 5.65× lower at baseline in the lines without DOCK2 | 0.021 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, KCTD16; maybe low, not absent; co-absent with the target |
| [[INSYN2B]] | C | DOCK2 activity raises INSYN2B's level | lines that do not express DOCK2 (21) vs lines expressing it (29) | 5.55× lower at baseline in the lines without DOCK2 | 0.025 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, KCTD16; maybe low, not absent; co-absent with the target |
| [[HTR7]] | C | DOCK2 activity raises HTR7's level | lines that do not express DOCK2 (21) vs lines expressing it (29) | 3.73× lower at baseline in the lines without DOCK2 | 0.036 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, KCTD16; maybe low, not absent; co-absent with the target |
| [[DENND2A]] | C | DOCK2 activity raises DENND2A's level | lines that do not express DOCK2 (21) vs lines expressing it (29) | 3.30× lower at baseline in the lines without DOCK2 | 0.040 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, KCTD16; maybe low, not absent; co-absent with the target |
| [[ADAM12]] | C | DOCK2 activity raises ADAM12's level | lines that do not express DOCK2 (21) vs lines expressing it (29) | 7.57× lower at baseline in the lines without DOCK2 | 0.054 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, KCTD16; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.611). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (50.2, 15.9); signed map (21.2, 45.8). **Vector** length 50.6, 10.9% of its response variance represented; |z| ≥ 3 in 567 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.6 | +13.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.4 | +14.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.8 | +12.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +17.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +7.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +2.9 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.5 | +2.5 |
|  | [[vincristine (drug)]] 5 µM |  | +1.2 | -0.2 |
| fall | [[Artesunate (drug)]] 5 µM |  | -1.5 | -4.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -2.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -3.8 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -1.7 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.3 | -1.3 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.2 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | dedicator of cytokinesis 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.1 — chr5:169,637,268-170,083,382 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0209 |
| Gene groups (HGNC) | Armadillo like helical domain containing; DOCK family Rho GEFs; MicroRNA protein coding host genes; SH3 domain containing |
| Hallmark sets | KRAS_SIGNALING_UP, MITOTIC_SPINDLE |
| Reactome | 16 pathways, smallest: Nef and signal transduction; The role of Nef in HIV-1 replication and disease pathogenesis; RHOG GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92608](https://www.uniprot.org/uniprotkb/Q92608) (Dedicator of cytokinesis protein 2):

> Guanine nucleotide exchange factor (GEF) that activates monomeric GTPases by catalysing the release of bound GDP in exchange for free GTP. Activates RAC1 and RAC2, but not CDC42. Involved in cytoskeletal rearrangements required for lymphocyte migration in response of chemokines. May also participate in IL2 transcriptional activation via the activation of RAC2.

**Summary**, from NCBI Gene [1794](https://www.ncbi.nlm.nih.gov/gene/1794):

> The protein encoded by this gene belongs to the CDM protein family. It is specifically expressed in hematopoietic cells and is predominantly expressed in peripheral blood leukocytes. The protein is involved in remodeling of the actin cytoskeleton required for lymphocyte migration in response to chemokine signaling. It activates members of the Rho family of GTPases, for example RAC1 and RAC2, by acting as a guanine nucleotide exchange factor (GEF) to exchange bound GDP for free GTP. Mutations in …

**Accessions** — [HGNC:2988](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2988) · Entrez [1794](https://www.ncbi.nlm.nih.gov/gene/1794) · UniProt [Q92608](https://www.uniprot.org/uniprotkb/Q92608) · Ensembl [ENSG00000134516](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134516)

## Data

Gene col 5571: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5571); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5571, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5571]; `tensor/DDL_lfc|DDL_z.npy` [5571]; `embed/gene_vectors.npy` [5571]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5571 or target_col == 5571). Every well: [[DOCK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DOCK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
