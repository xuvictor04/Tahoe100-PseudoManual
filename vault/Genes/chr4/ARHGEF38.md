---
symbol: "ARHGEF38"
type: "gene"
col: 14091
ensembl_id: "ENSG00000236699"
name: "Rho guanine nucleotide exchange factor 38"
location: "4q24"
module: 8
arm: "+"
pooled_cpm: 30.29
n_lines_expressing: 14
n_dd_up: 14
n_dd_down: 11
n_dd_up_clean: 10
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 143
direction_downstream: 186
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# ARHGEF38

*Rho guanine nucleotide exchange factor 38* — 4q24

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.92× (z +11.5, q 6e-28, up in 0 of 11 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.78× (z +9.1, q 2e-17, up in 10 of 12 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.577× (z -6.1, q 3e-07, down in 12 of 12 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Rutin (trihydrate) (drug)]] 0.05 µM: 0.658× (z -4.3, q 0.003, down in 0 of 12 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POF1B]] (+0.80, fdr 7e-06), [[LINC02253]] (+0.78, fdr 7e-06), [[TOX3]] (+0.77, fdr 7e-06).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 143 arrows point to it, the strongest [[RAPGEF5]] → it (grade B ⚠); 186 go from it, the strongest it → [[ELF3-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14091.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.92×** | +11.5 | 6e-28 | 0/11 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.53×** | +10.4 | 7e-23 | 0/12 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.78×** | +9.1 | 2e-17 | 10/12 (HT-29, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.25×** | +8.4 | 7e-15 | 1/11 (SW1417) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +8.0 | 2e-13 | 0/12 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +4.9 | 9e-05 | 0/12 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.40×** | +3.8 | 0.012 | 0/12 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.40×** | +3.6 | 0.020 | 10/12 (NCI-H1573, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.35×** | +3.4 | 0.049 | 5/12 (HT-29, KATO III, …) | two highest doses | cell-cycle shift (explains ~15% here) |
| [[BAY1125976 (drug)]] 0.5 µM |  | **1.50×** | +3.2 | 0.070 | 0/12 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.34×** | +3.1 | 0.082 | 5/12 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.32×** | +3.1 | 0.082 | 8/12 (SW1417, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.32×** | +3.1 | 0.085 | 4/12 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.46×** | +3.0 | 0.099 | 0/12 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14091.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.577×** | -6.1 | 3e-07 | 12/12 (SW480, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.578×** | -6.1 | 3e-07 | 12/12 (SW480, COLO 205, …) | all doses, stronger at high dose |  |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | **0.658×** | -4.3 | 0.003 | 0/12 | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.693×** | -4.1 | 0.006 | 12/12 (COLO 205, SW480, …) | all doses, stronger at high dose |  |
| [[BAY1125976 (drug)]] 5 µM |  | **0.514×** | -3.9 | 0.011 | 2/12 (CFPAC-1, NCI-H1573) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.709×** | -3.8 | 0.012 | 10/12 (SW480, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.718×** | -3.7 | 0.017 | 5/12 (COLO 205, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Larotrectinib (drug)]] 5 µM |  | **0.796×** | -3.6 | 0.022 | 12/12 (SW480, COLO 205, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | **0.738×** | -3.3 | 0.068 | 12/12 (SW480, CFPAC-1, …) | top dose only |  |
| [[Lucanthone (drug)]] 0.05 µM |  | **0.734×** | -3.2 | 0.079 | 0/12 | inconsistent across doses | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.757×** | -3.1 | 0.097 | 7/12 (BT-474, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14091. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 371 | 0 | 15 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0570× (z -29.5) |
| [[SW480 (line)]] | alt | 58.0 | 0 | 14 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.136× (z -21.1) |
| [[NCI-H1573 (line)]] | alt | 106 | 8 (1 ⚠) | 2 | [[Harringtonine (drug)]] 5 µM 5.10× (z +10.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.178× (z -16.4) |
| [[HT-29 (line)]] | alt | 116 | 1 | 7 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +11.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.155× (z -18.2) |
| [[BT-474 (line)]] | alt | 181 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.196× (z -14.7) |
| [[CFPAC-1 (line)]] | alt | 119 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.111× (z -15.3) |
| [[HEC-1-A (line)]] | alt | 57.7 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.120× (z -13.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.285× (z -11.5) |
| [[KATO III (line)]] | alt | 89.2 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.129× (z -21.8) |
| [[LoVo (line)]] | wt | 41.0 | 1 | 5 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 4.67× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.176× (z -15.6) |
| [[LS 180 (line)]] | wt | 93.9 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.174× (z -17.2) |
| [[SW1417 (line)]] | alt | 64.7 | 1 (1 ⚠) | 1 | [[Selinexor (drug)]] 5 µM 3.16× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.195× (z -13.4) |
| [[Panc 03.27 (line)]] | alt | 27.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.89× (z +9.7) | — |
| [[A-172 (line)]] | wt | 3.25 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.53 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.67 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.55 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.82 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 7.46 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.54 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.22 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.99 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.18 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.34 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.43 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.31 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.69 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.00 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.98 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.56 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.77 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.46 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.64 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.81 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.82 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 3.71 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.92 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.95 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.43 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.35 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.96 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.09 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.11 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.67 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.31 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.98 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 3.49 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.61 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.85 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14091), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POF1B]] | +0.80 | +0.74 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[LINC02253]] | +0.78 | +0.72 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[TOX3]] | +0.77 | +0.72 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[TNFRSF14-AS1]] | +0.76 | +0.80 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[RASSF6]] | +0.76 | +0.70 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[EPS8L3]] | +0.74 | +0.69 / +0.74 | both halves | 7e-06 | same gene group |
| [[RNF43]] | +0.74 | +0.68 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[TMPRSS2]] | +0.73 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[MACC1]] | +0.73 | +0.78 / +0.68 | both halves | 7e-06 | same gene group |
| [[PLCH1]] | +0.72 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[ANK3]] | +0.72 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[TRIM31]] | +0.70 | +0.66 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*143 arrows, 143 of them with an alert ⚠; grade A 0, B 9, C 134. Shown: the 12 strongest; 131 more arrows (131 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAPGEF5]] | B | RAPGEF5 activity raises ARHGEF38's level | lines that do not express RAPGEF5 (17) vs lines expressing it (33) | 3.32× lower at baseline in the lines without RAPGEF5 | 0.039 | ⚠ within organs, on part of the lines; also absent: HSH2D, HOOK1, SAMD12; maybe low, not absent |
| [[NOSTRIN]] | B | NOSTRIN activity raises ARHGEF38's level | lines that do not express NOSTRIN (16) vs lines expressing it (34) | 3.73× lower at baseline in the lines without NOSTRIN | 0.049 | ⚠ within organs, on part of the lines; also absent: SLC9A2, SLPI, SULT2B1; maybe low, not absent |
| [[HNF4G]] | B | HNF4G activity raises ARHGEF38's level | lines that do not express HNF4G (16) vs lines expressing it (34) | 3.39× lower at baseline in the lines without HNF4G | 0.057 | ⚠ within organs, on part of the lines; also absent: MPZL3, ELF3, ARHGEF5 |
| [[TTC28]] | B | TTC28 activity lowers ARHGEF38's level | lines that do not express TTC28 (15) vs lines expressing it (35) | 5.49× higher at baseline in the lines without TTC28 | 0.058 | ⚠ within organs, on part of the lines; also absent: SAMD11, RASSF8-AS1, AOX1 |
| [[MTUS1]] | B | MTUS1 activity raises ARHGEF38's level | lines that do not express MTUS1 (17) vs lines expressing it (33) | 2.94× lower at baseline in the lines without MTUS1 | 0.075 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, SHROOM3, ELF3 |
| [[SPATA6L]] | B | SPATA6L activity raises ARHGEF38's level | lines that do not express SPATA6L (15) vs lines expressing it (35) | 3.45× lower at baseline in the lines without SPATA6L | 0.077 | ⚠ within organs, on part of the lines; also absent: RHOV, ANO9, ELF3; maybe low, not absent |
| [[ELF3-AS1]] | B | ELF3-AS1 activity raises ARHGEF38's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 3.28× lower at baseline in the lines without ELF3-AS1 | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent |
| [[STS]] | B | STS activity raises ARHGEF38's level | lines that do not express STS (11) vs lines expressing it (39) | 2.96× lower at baseline in the lines without STS | 0.083 | ⚠ within organs, on part of the lines; also absent: FBXO39, KPNA7; maybe low, not absent |
| [[INPP4B]] | B | INPP4B activity raises ARHGEF38's level | lines that do not express INPP4B (10) vs lines expressing it (40) | 2.00× lower at baseline in the lines without INPP4B | 0.091 | ⚠ within organs, on part of the lines; also absent: RAB32, CD82, IFIT2 |
| [[TMPRSS2]] | C | TMPRSS2 activity raises ARHGEF38's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 12.32× lower at baseline in the lines without TMPRSS2 | 3e-05 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6; co-absent with the target |
| [[ITGB6]] | C | ITGB6 activity raises ARHGEF38's level | lines that do not express ITGB6 (32) vs lines expressing it (18) | 9.96× lower at baseline in the lines without ITGB6 | 7e-05 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS2, TMPRSS4; co-absent with the target |
| [[ADGRF1]] | C | ADGRF1 activity raises ARHGEF38's level | lines that do not express ADGRF1 (35) vs lines expressing it (15) | 8.67× lower at baseline in the lines without ADGRF1 | 1e-04 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4; co-absent with the target |

### Downstream of this gene

*186 arrows, 186 of them with an alert ⚠; grade A 0, B 49, C 137. Shown: the 12 strongest; 174 more arrows (174 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ELF3-AS1]] | B | ARHGEF38 activity raises ELF3-AS1's level | lines that do not express ARHGEF38 (36) vs lines expressing it (14) | 4.46× lower at baseline in the lines without ARHGEF38 | 5e-04 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, TMEM125, SLC5A1 |
| [[STX19]] | B | ARHGEF38 activity raises STX19's level | lines that do not express ARHGEF38 (36) vs lines expressing it (14) | 2.75× lower at baseline in the lines without ARHGEF38 | 0.001 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, TMEM125, SLC5A1 |
| [[SLC44A3]] | B | ARHGEF38 activity raises SLC44A3's level | lines that do not express ARHGEF38 (36) vs lines expressing it (14) | 3.60× lower at baseline in the lines without ARHGEF38 | 0.001 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, TMEM125, SLC5A1 |
| [[STS]] | B | ARHGEF38 activity raises STS's level | lines that do not express ARHGEF38 (36) vs lines expressing it (14) | 3.86× lower at baseline in the lines without ARHGEF38 | 0.002 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, TMEM125, SLC5A1 |
| [[HGD]] | B | ARHGEF38 activity raises HGD's level | lines that do not express ARHGEF38 (36) vs lines expressing it (14) | 3.08× lower at baseline in the lines without ARHGEF38 | 0.002 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, TMEM125, SLC5A1 |
| [[SLC12A2]] | B | ARHGEF38 activity raises SLC12A2's level | lines that do not express ARHGEF38 (36) vs lines expressing it (14) | 3.22× lower at baseline in the lines without ARHGEF38 | 0.003 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, TMEM125, SLC5A1 |
| [[GAREM1]] | B | ARHGEF38 activity raises GAREM1's level | lines that do not express ARHGEF38 (36) vs lines expressing it (14) | 3.51× lower at baseline in the lines without ARHGEF38 | 0.003 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, TMEM125, SLC5A1 |
| [[TMEM184A]] | B | ARHGEF38 activity raises TMEM184A's level | lines that do not express ARHGEF38 (36) vs lines expressing it (14) | 2.83× lower at baseline in the lines without ARHGEF38 | 0.004 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, TMEM125, SLC5A1 |
| [[C4orf19]] | B | ARHGEF38 activity raises C4orf19's level | lines that do not express ARHGEF38 (36) vs lines expressing it (14) | 3.49× lower at baseline in the lines without ARHGEF38 | 0.005 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, TMEM125, SLC5A1 |
| [[MROH7]] | B | ARHGEF38 activity raises MROH7's level | lines that do not express ARHGEF38 (36) vs lines expressing it (14) | 2.81× lower at baseline in the lines without ARHGEF38 | 0.007 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, TMEM125, SLC5A1 |
| [[LINC00857]] | B | ARHGEF38 activity raises LINC00857's level | lines that do not express ARHGEF38 (36) vs lines expressing it (14) | 3.08× lower at baseline in the lines without ARHGEF38 | 0.007 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, TMEM125, SLC5A1 |
| [[TNFRSF21]] | B | ARHGEF38 activity raises TNFRSF21's level | lines that do not express ARHGEF38 (36) vs lines expressing it (14) | 4.39× lower at baseline in the lines without ARHGEF38 | 0.009 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, TMEM125, SLC5A1 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.780). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.6, 50.3); signed map (58.3, 3.9). **Vector** length 82.4, 36.3% of its response variance represented; |z| ≥ 3 in 511 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.2 | +9.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.6 | +8.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +11.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.4 | +10.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +2.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.8 | +2.9 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.7 | +2.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.7 | +2.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.6 | +1.7 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.3 | -3.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.8 | -1.6 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.7 | -3.9 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.7 | -2.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.6 | -3.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | Rho guanine nucleotide exchange factor 38 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q24 — chr4:105,552,620-105,708,093 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20184 |
| Gene groups (HGNC) | Dbl family Rho GEFs; BAR and Dbl domain containing; SH3 domain containing |
| Reactome | 7 pathways, smallest: NRAGE signals death through JNK; G alpha (12/13) signalling events; Cell death signalling via NRAGE, NRIF and NADE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NXL2](https://www.uniprot.org/uniprotkb/Q9NXL2) (Rho guanine nucleotide exchange factor 38):

> May act as a guanine-nucleotide releasing factor.

**Summary**, from NCBI Gene [54848](https://www.ncbi.nlm.nih.gov/gene/54848):

> Predicted to enable guanyl-nucleotide exchange factor activity. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25968](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25968) · Entrez [54848](https://www.ncbi.nlm.nih.gov/gene/54848) · UniProt [Q9NXL2](https://www.uniprot.org/uniprotkb/Q9NXL2) · Ensembl [ENSG00000236699](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000236699)

## Data

Gene col 14091: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14091); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14091, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14091]; `tensor/DDL_lfc|DDL_z.npy` [14091]; `embed/gene_vectors.npy` [14091]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14091 or target_col == 14091). Every well: [[ARHGEF38 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARHGEF38.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
