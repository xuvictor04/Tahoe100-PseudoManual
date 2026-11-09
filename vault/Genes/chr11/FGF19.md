---
symbol: "FGF19"
type: "gene"
col: 8501
ensembl_id: "ENSG00000162344"
name: "fibroblast growth factor 19"
location: "11q13.3"
module: 27
arm: "+"
pooled_cpm: 3.21
n_lines_expressing: 8
n_dd_up: 12
n_dd_down: 1
n_dd_up_clean: 3
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 19
direction_downstream: 28
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# FGF19

*fibroblast growth factor 19* — 11q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 7.32× (z +8.7, q 3e-15, up in 0 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.92× (z +6.8, q 1e-09, up in 2 of 4 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.371× (z -4.2, q 0.016, down in 2 of 6 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 8 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (SW480 0.0742×, AsPC-1 0.0786×; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (SW480 0.0803×, AsPC-1 0.0392×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (SW480 0.0929×, AsPC-1 0.0389×; ⚠ cell-cycle shift, explains ~0% of this change); [[Cobimetinib (drug)]] 5 µM in 1 line (SW480 0.163×); [[Binimetinib (drug)]] 0.5 µM in 1 line (SW480 0.242×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VWA2]] (+0.72, fdr 7e-06), [[IGFL4]] (+0.71, fdr 7e-06), [[LCK]] (+0.71, fdr 7e-06).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[CACNA2D4]] → it (grade B ⚠); 28 go from it, the strongest it → [[CACNA2D4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 9 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8501.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **7.32×** | +8.7 | 3e-15 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.57×** | +7.8 | 2e-12 | 1/2 (AsPC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.92×** | +6.8 | 1e-09 | 2/4 (AsPC-1, HT-29) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.91×** | +5.7 | 2e-06 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.60×** | +4.3 | 0.002 | 0/1 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~9% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.67×** | +4.3 | 0.002 | 0/2 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.49×** | +4.1 | 0.003 | 0/3 | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.52×** | +4.0 | 0.004 | 3/3 (COLO 205, AsPC-1, …) | top dose only | cell-cycle shift (explains ~5% here); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.17×** | +3.7 | 0.012 | 0/2 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **2.14×** | +3.4 | 0.031 | 1/3 (COLO 205) | inconsistent across doses | low cells (technical?) |
| [[Carbamazepine (drug)]] 5 µM |  | **2.14×** | +3.4 | 0.031 | 2/6 (HT-29, SW480) | top dose only | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.75×** | +3.1 | 0.084 | 0/1 | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8501.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 8 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (SW480 0.0742×, AsPC-1 0.0786×; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (SW480 0.0803×, AsPC-1 0.0392×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (SW480 0.0929×, AsPC-1 0.0389×; ⚠ cell-cycle shift, explains ~0% of this change); [[Cobimetinib (drug)]] 5 µM in 1 line (SW480 0.163×); [[Binimetinib (drug)]] 0.5 µM in 1 line (SW480 0.242×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.371×** | -4.2 | 0.016 | 2/6 (SW480, AsPC-1) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | 0.488× | -3.2 | 0.31 | 3/5 (SW480, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[9-ING-41 (drug)]] 5 µM |  | 0.281× | -3.0 | 0.31 | 0/6 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8501. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 50.6 | 0 | 14 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0742× (z -19.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0803× (z -13.0) |
| [[AsPC-1 (line)]] | alt | 5.32 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0786× (z -9.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0392× (z -8.5) |
| [[A-172 (line)]] | wt | 0.270 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.251 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.217 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.298 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.687 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.276 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.323 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.250 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.587 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.407 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.338 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.295 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.300 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.299 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.511 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.416 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.277 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.841 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.397 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.221 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.260 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.254 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.465 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.693 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.244 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.249 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.221 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.329 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.225 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.267 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.588 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.235 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.279 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.221 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.370 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.248 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.275 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.325 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.561 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.356 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.458 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.493 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.353 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8501), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VWA2]] | +0.72 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[IGFL4]] | +0.71 | +0.67 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[LCK]] | +0.71 | +0.72 / +0.62 | both halves | 7e-06 | pathway: Constitutive Signaling by Aberrant PI3K in Cancer |
| [[LINC02964]] | +0.69 | +0.73 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[ADGRG5]] | +0.69 | +0.61 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[APCDD1]] | +0.68 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[CACNA2D4]] | +0.67 | +0.62 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[FGD5]] | +0.66 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[DIO3OS]] | +0.66 | +0.59 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[GJB1]] | +0.66 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[SLC30A10]] | +0.65 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[COLGALT2]] | +0.63 | +0.57 / +0.70 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 1, C 18. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CACNA2D4]] | B | CACNA2D4 activity raises FGF19's level | lines that do not express CACNA2D4 (22) vs lines expressing it (28) | 1.49× lower at baseline in the lines without CACNA2D4 | 0.085 | ⚠ within organs, on part of the lines; also absent: ARHGDIB, NRP2, RFX8; maybe low, not absent |
| [[PSG1]] | C | PSG1 activity raises FGF19's level | lines that do not express PSG1 (45) vs lines expressing it (5) | 3.07× lower at baseline in the lines without PSG1 | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, KRT5, APOB; co-absent with the target |
| [[SHISA9]] | C | SHISA9 activity raises FGF19's level | lines that do not express SHISA9 (38) vs lines expressing it (12) | 1.60× lower at baseline in the lines without SHISA9 | 0.002 | ⚠ within organs, on part of the lines; also absent: LHFPL3-AS1, S100A1, LINC01456; maybe low, not absent; co-absent with the target |
| [[TFF3]] | C | TFF3 activity raises FGF19's level | lines that do not express TFF3 (38) vs lines expressing it (12) | 2.22× lower at baseline in the lines without TFF3 | 0.009 | ⚠ within organs, on part of the lines; also absent: CEACAM5, MUC17, AGR3; co-absent with the target |
| [[CLRN3]] | C | CLRN3 activity raises FGF19's level | lines that do not express CLRN3 (40) vs lines expressing it (10) | 2.60× lower at baseline in the lines without CLRN3 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13; co-absent with the target |
| [[MIR3667HG]] | C | MIR3667HG activity raises FGF19's level | lines that do not express MIR3667HG (38) vs lines expressing it (12) | 1.57× lower at baseline in the lines without MIR3667HG | 0.038 | ⚠ within organs, on part of the lines; also absent: GTSF1, ENSG00000288098, CALCA; co-absent with the target |
| [[LINC02964]] | C | LINC02964 activity raises FGF19's level | lines that do not express LINC02964 (38) vs lines expressing it (12) | 2.19× lower at baseline in the lines without LINC02964 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53, CDKN2A; also absent: CLRN3, GPA33, EPS8L3; co-absent with the target |
| [[FGD5]] | C | FGD5 activity raises FGF19's level | lines that do not express FGD5 (37) vs lines expressing it (13) | 2.10× lower at baseline in the lines without FGD5 | 0.041 | ⚠ within organs, on part of the lines; also absent: ENSG00000265554, TFF2, KRT5; co-absent with the target |
| [[PADI1]] | C | PADI1 activity raises FGF19's level | lines that do not express PADI1 (34) vs lines expressing it (16) | 1.91× lower at baseline in the lines without PADI1 | 0.049 | ⚠ within organs, on part of the lines; also absent: CLIC5, LINC01559, EPS8L3; co-absent with the target |
| [[ADGRG5]] | C | ADGRG5 activity raises FGF19's level | lines that do not express ADGRG5 (35) vs lines expressing it (15) | 2.03× lower at baseline in the lines without ADGRG5 | 0.051 | ⚠ within organs, on part of the lines; also absent: LINC01559, RNF183, GPA33; maybe low, not absent; co-absent with the target |
| [[AZGP1]] | C | AZGP1 activity raises FGF19's level | lines that do not express AZGP1 (35) vs lines expressing it (15) | 1.96× lower at baseline in the lines without AZGP1 | 0.059 | ⚠ within organs, on part of the lines; also absent: GJB1, PROM1, LYZ; co-absent with the target |
| [[LINC01819]] | C | LINC01819 activity raises FGF19's level | lines that do not express LINC01819 (29) vs lines expressing it (21) | 1.61× lower at baseline in the lines without LINC01819 | 0.062 | ⚠ within organs, on part of the lines; also absent: MOGAT3, LGR6, A1CF; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 5, C 23. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CACNA2D4]] | B | FGF19 activity raises CACNA2D4's level | lines that do not express FGF19 (42) vs lines expressing it (8) | 2.05× lower at baseline in the lines without FGF19 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT20, SFTPA2, KRT5 |
| [[F10]] | B | FGF19 activity raises F10's level | lines that do not express FGF19 (42) vs lines expressing it (8) | 1.87× lower at baseline in the lines without FGF19 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT20, SFTPA2, KRT5 |
| [[CHST11]] | B | FGF19 activity raises CHST11's level | lines that do not express FGF19 (42) vs lines expressing it (8) | 2.44× lower at baseline in the lines without FGF19 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT20, SFTPA2, KRT5 |
| [[TLDC2]] | B | FGF19 activity raises TLDC2's level | lines that do not express FGF19 (42) vs lines expressing it (8) | 2.44× lower at baseline in the lines without FGF19 | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT20, SFTPA2, KRT5 |
| [[LEMD1]] | B | FGF19 activity raises LEMD1's level | lines that do not express FGF19 (42) vs lines expressing it (8) | 3.02× lower at baseline in the lines without FGF19 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT20, SFTPA2, KRT5 |
| [[LINC02964]] | C | FGF19 activity raises LINC02964's level | lines that do not express FGF19 (42) vs lines expressing it (8) | 4.00× lower at baseline in the lines without FGF19 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT20, SFTPA2, KRT5; co-absent with the target |
| [[ADGRG5]] | C | FGF19 activity raises ADGRG5's level | lines that do not express FGF19 (42) vs lines expressing it (8) | 2.99× lower at baseline in the lines without FGF19 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT20, SFTPA2, KRT5; co-absent with the target |
| [[FGD5]] | C | FGF19 activity raises FGD5's level | lines that do not express FGF19 (42) vs lines expressing it (8) | 4.49× lower at baseline in the lines without FGF19 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT20, SFTPA2, KRT5; co-absent with the target |
| [[LINC01169]] | C | FGF19 activity raises LINC01169's level | lines that do not express FGF19 (42) vs lines expressing it (8) | 3.24× lower at baseline in the lines without FGF19 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT20, SFTPA2, KRT5; co-absent with the target |
| [[AZGP1]] | C | FGF19 activity raises AZGP1's level | lines that do not express FGF19 (42) vs lines expressing it (8) | 3.63× lower at baseline in the lines without FGF19 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT20, SFTPA2, KRT5; co-absent with the target |
| [[SKAP1]] | C | FGF19 activity raises SKAP1's level | lines that do not express FGF19 (42) vs lines expressing it (8) | 5.41× lower at baseline in the lines without FGF19 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT20, SFTPA2, KRT5; co-absent with the target |
| [[PADI1]] | C | FGF19 activity raises PADI1's level | lines that do not express FGF19 (42) vs lines expressing it (8) | 5.19× lower at baseline in the lines without FGF19 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT20, SFTPA2, KRT5; co-absent with the target |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.491). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.0, 43.2); signed map (64.1, 15.7). **Vector** length 29.0, 13.1% of its response variance represented; |z| ≥ 3 in 165 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.5 | +8.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.3 | +6.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.3 | +7.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +1.3 | +4.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.3 | +5.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.1 | +2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.9 | +1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.6 | +0.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +0.4 | -0.2 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +0.4 | +3.4 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.5 | -0.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -1.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.8 | -0.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.8 | -4.2 |
|  | [[Trametinib (drug)]] 5 µM |  | -0.8 | -2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.6 | -1.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -0.6 | -1.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -0.6 | -1.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | -0.6 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | fibroblast growth factor 19 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.3 — chr11:69,698,238-69,704,022 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Fibroblast growth factor family |
| Reactome | 27 pathways, smallest: FGFR4 ligand binding and activation; Phospholipase C-mediated cascade; FGFR4; PI-3K cascade:FGFR4 |
| Matched by | ensembl_id |

**Function**, from UniProt [O95750](https://www.uniprot.org/uniprotkb/O95750) (Fibroblast growth factor 19):

> Involved in the suppression of bile acid biosynthesis through down-regulation of CYP7A1 expression, following positive regulation of the JNK and ERK1/2 cascades. Stimulates glucose uptake in adipocytes. Activity requires the presence of KLB and FGFR4.

**Summary**, from NCBI Gene [9965](https://www.ncbi.nlm.nih.gov/gene/9965):

> The protein encoded by this gene is a member of the fibroblast growth factor (FGF) family. FGF family members possess broad mitogenic and cell survival activities, and are involved in a variety of biological processes including embryonic development cell growth, morphogenesis, tissue repair, tumor growth and invasion. This growth factor is a high affinity, heparin dependent ligand for FGFR4. Expression of this gene was detected only in fetal but not adult brain tissue. Synergistic interaction …

**Accessions** — [HGNC:3675](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3675) · Entrez [9965](https://www.ncbi.nlm.nih.gov/gene/9965) · UniProt [O95750](https://www.uniprot.org/uniprotkb/O95750) · Ensembl [ENSG00000162344](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162344)

## Data

Gene col 8501: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8501); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8501, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8501]; `tensor/DDL_lfc|DDL_z.npy` [8501]; `embed/gene_vectors.npy` [8501]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8501 or target_col == 8501). Every well: [[FGF19 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FGF19.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
