---
symbol: "LRRC4B"
type: "gene"
col: 5206
ensembl_id: "ENSG00000131409"
name: "leucine rich repeat containing 4B"
location: "19q13.33"
module: 128
arm: "+"
pooled_cpm: 2.88
n_lines_expressing: 31
n_dd_up: 16
n_dd_down: 1
n_dd_up_clean: 9
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 12
direction_downstream: 26
tags: ["gene", "module/128"]
generated_by: "tahoemap"
---

# LRRC4B

*leucine rich repeat containing 4B* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.64× (z +15.2, q 0e+00, up in 0 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 2.33× (z +10.9, q 3e-25, up in 13 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[crizotinib (drug)]] 5 µM: 0.636× (z -4.0, q 0.040, down in 5 of 24 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 2 lines (A-172 0.125×, SK-MEL-2 0.115×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SK-MEL-2 0.189×, A-172 0.336×); [[Panobinostat (drug)]] 5 µM in 2 lines (A-172 0.218×, SK-MEL-2 0.171×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CACNA2D2]] (+0.65, fdr 1e-05), [[PAX2]] (+0.65, fdr 2e-05), [[CDH23]] (+0.61, fdr 1e-05).
> It is in [[Module 128]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[LINC00466]] → it (grade B ⚠); 26 go from it, the strongest it → [[CCDC102A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5206.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.64×** | +15.2 | 0e+00 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.33×** | +10.9 | 3e-25 | 13/26 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.06×** | +10.2 | 4e-22 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.61×** | +8.8 | 3e-16 | 12/22 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +7.5 | 6e-12 | 5/18 (HEC-1-A, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.42×** | +7.5 | 8e-12 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Saquinavir (drug)]] 5 µM |  | **1.40×** | +4.4 | 9e-04 | 3/17 (A498, NCI-H460, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.44×** | +4.3 | 0.001 | 2/4 (NCI-H23, SK-MEL-2) | top dose only | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.38×** | +4.2 | 0.002 | 5/21 (A549, CHP-212, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.75×** | +3.7 | 0.015 | 0/11 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.75×** | +3.6 | 0.015 | 0/4 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Omeprazole (drug)]] 0.5 µM |  | **1.44×** | +3.3 | 0.041 | 1/17 (C-33 A) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.43×** | +3.1 | 0.078 | 2/10 (H4, SK-MEL-2) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.41×** | +3.1 | 0.078 | 5/20 (A-427, NCI-H23, …) | rises with dose |  |
| [[Decitabine (drug)]] 0.5 µM |  | **1.40×** | +3.1 | 0.084 | 1/18 (A549) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5206.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 2 lines (A-172 0.125×, SK-MEL-2 0.115×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SK-MEL-2 0.189×, A-172 0.336×); [[Panobinostat (drug)]] 5 µM in 2 lines (A-172 0.218×, SK-MEL-2 0.171×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[crizotinib (drug)]] 5 µM |  | **0.636×** | -4.0 | 0.040 | 5/24 (C32, CHP-212, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5206. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 35.0 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.125× (z -15.8) |
| [[SK-MEL-2 (line)]] | alt | 17.6 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.189× (z -12.2) |
| [[A-427 (line)]] | wt | 3.51 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0492× (z -9.9) ⚠ cell-cycle shift, explains ~42% of this change |
| [[H4 (line)]] | wt | 37.2 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0510× (z -15.4) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.459 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.899 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.48 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.570 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.573 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.524 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.732 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.549 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.494 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.707 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.641 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.462 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.561 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.716 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.678 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.476 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.503 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.495 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.42 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.486 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.780 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.736 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.618 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.657 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.478 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.817 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.852 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.966 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5206), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CACNA2D2]] | +0.65 | +0.64 / +0.57 | both halves | 1e-05 | pathway: Neuronal System |
| [[PAX2]] | +0.65 | +0.63 / +0.48 | both halves | 2e-05 | **novel candidate** |
| [[CDH23]] | +0.61 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[LINC00466]] | +0.59 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[SPTBN4]] | +0.59 | +0.46 / +0.61 | both halves | 3e-05 |  |
| [[MYT1]] | +0.58 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[EFHD1]] | +0.57 | +0.39 / +0.61 | both halves | 6e-05 |  |
| [[ADAMTS10]] | +0.56 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[SYT9-AS1]] | +0.55 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[MAP6]] | +0.55 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[WIPF3]] | +0.55 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[HOXD11]] | +0.55 | +0.60 / +0.29 | both halves | 2e-04 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 5, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00466]] | B | LINC00466 activity raises LRRC4B's level | lines that do not express LINC00466 (15) vs lines expressing it (35) | 1.72× lower at baseline in the lines without LINC00466 | 0.049 | ⚠ within organs, on part of the lines; also absent: FAM124A, NTN1, SSPOP; maybe low, not absent |
| [[MYT1]] | B | MYT1 activity raises LRRC4B's level | lines that do not express MYT1 (25) vs lines expressing it (25) | 2.03× lower at baseline in the lines without MYT1 | 0.059 | ⚠ within organs, on part of the lines; also absent: CHGB, ENSG00000249776, PAX2 |
| [[LINC00173]] | B | LINC00173 activity raises LRRC4B's level | lines that do not express LINC00173 (18) vs lines expressing it (32) | 2.08× lower at baseline in the lines without LINC00173 | 0.079 | ⚠ within organs, on part of the lines; also absent: GBX1, RAB3C, NOVA2 |
| [[RHBDL3]] | B | RHBDL3 activity raises LRRC4B's level | lines that do not express RHBDL3 (9) vs lines expressing it (41) | 2.06× lower at baseline in the lines without RHBDL3 | 0.085 | ⚠ within organs, on part of the lines; also absent: PRDM6, DZIP1L, CACNB4; maybe low, not absent |
| [[PALM]] | B | PALM activity raises LRRC4B's level | lines that do not express PALM (21) vs lines expressing it (29) | 1.88× lower at baseline in the lines without PALM | 0.097 | ⚠ within organs, on part of the lines; also absent: CACNG4, FXYD6, BEGAIN |
| [[MSI1]] | C | MSI1 activity raises LRRC4B's level | lines that do not express MSI1 (26) vs lines expressing it (24) | 2.50× lower at baseline in the lines without MSI1 | 0.011 | ⚠ within organs, on part of the lines; also absent: KCNQ2, KIF1A, LMX1B; co-absent with the target |
| [[PAX2]] | C | PAX2 activity raises LRRC4B's level | lines that do not express PAX2 (33) vs lines expressing it (17) | 2.48× lower at baseline in the lines without PAX2 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PREX2, LINC02643, ADD2; co-absent with the target |
| [[SSPOP]] | C | SSPOP activity raises LRRC4B's level | lines that do not express SSPOP (13) vs lines expressing it (37) | 2.20× lower at baseline in the lines without SSPOP | 0.023 | ⚠ within organs, on part of the lines; also absent: SPDYE10, LRRC4B, AP3B2; co-absent with the target |
| [[ELFN1]] | C | ELFN1 activity raises LRRC4B's level | lines that do not express ELFN1 (24) vs lines expressing it (26) | 2.36× lower at baseline in the lines without ELFN1 | 0.033 | ⚠ within organs, on part of the lines; also absent: SORCS2, JAM3, ENSG00000269547; co-absent with the target |
| [[KCNQ2]] | C | KCNQ2 activity raises LRRC4B's level | lines that do not express KCNQ2 (29) vs lines expressing it (21) | 1.76× lower at baseline in the lines without KCNQ2 | 0.061 | ⚠ within organs, on part of the lines; also absent: KIF1A, SULT4A1, ANKRD20A11P; co-absent with the target |
| [[STOX2]] | C | STOX2 activity raises LRRC4B's level | lines that do not express STOX2 (22) vs lines expressing it (28) | 2.07× lower at baseline in the lines without STOX2 | 0.089 | ⚠ within organs, on part of the lines; also absent: SLC47A1, RBM11, FBXO27; co-absent with the target |
| [[LMX1B]] | C | LMX1B activity raises LRRC4B's level | lines that do not express LMX1B (24) vs lines expressing it (26) | 1.98× lower at baseline in the lines without LMX1B | 0.098 | ⚠ within organs, on part of the lines; also absent: JPH3, JAKMIP1, GABBR2; co-absent with the target |

### Downstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 14, C 12. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC102A]] | B | LRRC4B activity raises CCDC102A's level | lines that do not express LRRC4B (19) vs lines expressing it (31) | 1.87× lower at baseline in the lines without LRRC4B | 0.004 | ⚠ within organs, on part of the lines; also absent: CHRNA7, PDZD4, GNG4; maybe low, not absent |
| [[RHBDL3]] | B | LRRC4B activity raises RHBDL3's level | lines that do not express LRRC4B (19) vs lines expressing it (31) | 1.97× lower at baseline in the lines without LRRC4B | 0.009 | ⚠ within organs, on part of the lines; also absent: CHRNA7, PDZD4, GNG4; maybe low, not absent |
| [[SYT9-AS1]] | B | LRRC4B activity raises SYT9-AS1's level | lines that do not express LRRC4B (19) vs lines expressing it (31) | 1.77× lower at baseline in the lines without LRRC4B | 0.011 | ⚠ within organs, on part of the lines; also absent: CHRNA7, PDZD4, GNG4; maybe low, not absent |
| [[ATF7IP2]] | B | LRRC4B activity raises ATF7IP2's level | lines that do not express LRRC4B (19) vs lines expressing it (31) | 1.38× lower at baseline in the lines without LRRC4B | 0.019 | ⚠ within organs, on part of the lines; also absent: CHRNA7, PDZD4, GNG4; maybe low, not absent |
| [[CYS1]] | B | LRRC4B activity raises CYS1's level | lines that do not express LRRC4B (19) vs lines expressing it (31) | 1.60× lower at baseline in the lines without LRRC4B | 0.032 | ⚠ within organs, on part of the lines; also absent: CHRNA7, PDZD4, GNG4; maybe low, not absent |
| [[LINC00466]] | B | LRRC4B activity raises LINC00466's level | lines that do not express LRRC4B (19) vs lines expressing it (31) | 1.82× lower at baseline in the lines without LRRC4B | 0.033 | ⚠ within organs, on part of the lines; also absent: CHRNA7, PDZD4, GNG4; maybe low, not absent |
| [[TCF7L1]] | B | LRRC4B activity raises TCF7L1's level | lines that do not express LRRC4B (19) vs lines expressing it (31) | 2.74× lower at baseline in the lines without LRRC4B | 0.040 | ⚠ within organs, on part of the lines; also absent: CHRNA7, PDZD4, GNG4; maybe low, not absent |
| [[TUB]] | B | LRRC4B activity raises TUB's level | lines that do not express LRRC4B (19) vs lines expressing it (31) | 2.13× lower at baseline in the lines without LRRC4B | 0.043 | ⚠ within organs, on part of the lines; also absent: CHRNA7, PDZD4, GNG4; maybe low, not absent |
| [[LINC00173]] | B | LRRC4B activity raises LINC00173's level | lines that do not express LRRC4B (19) vs lines expressing it (31) | 1.85× lower at baseline in the lines without LRRC4B | 0.058 | ⚠ within organs, on part of the lines; also absent: CHRNA7, PDZD4, GNG4; maybe low, not absent |
| [[PPEF1]] | B | LRRC4B activity raises PPEF1's level | lines that do not express LRRC4B (19) vs lines expressing it (31) | 1.82× lower at baseline in the lines without LRRC4B | 0.062 | ⚠ within organs, on part of the lines; also absent: CHRNA7, PDZD4, GNG4; maybe low, not absent |
| [[KNDC1]] | B | LRRC4B activity raises KNDC1's level | lines that do not express LRRC4B (19) vs lines expressing it (31) | 2.10× lower at baseline in the lines without LRRC4B | 0.072 | ⚠ within organs, on part of the lines; also absent: CHRNA7, PDZD4, GNG4; maybe low, not absent |
| [[FBXO2]] | B | LRRC4B activity raises FBXO2's level | lines that do not express LRRC4B (19) vs lines expressing it (31) | 1.60× lower at baseline in the lines without LRRC4B | 0.080 | ⚠ within organs, on part of the lines; also absent: CHRNA7, PDZD4, GNG4; maybe low, not absent |

## Where it sits

- **Module**: [[Module 128]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.657). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (11.1, 38.4); signed map (24.1, 28.1). **Vector** length 34.8, 5.21% of its response variance represented; |z| ≥ 3 in 570 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +15.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +10.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.4 | +8.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +10.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.7 | +7.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.4 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +3.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.9 | +1.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +0.9 | +3.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -1.3 | -0.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.2 | -2.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.1 | -2.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -1.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.0 | -1.0 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.8 | -1.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.8 | +0.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.8 | -2.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -0.8 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeat containing 4B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:50,516,892-50,568,435 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp761A179, HSM, NGL-3; previously LRIG4 |
| Gene groups (HGNC) | Receptor ligands; I-set domain containing; Ig-like cell adhesion molecule family |
| Reactome | 3 pathways, smallest: Receptor-type tyrosine-protein phosphatases; Protein-protein interactions at synapses; Neuronal System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NT99](https://www.uniprot.org/uniprotkb/Q9NT99) (Leucine-rich repeat-containing protein 4B):

> Synaptic adhesion protein. Regulates the formation of excitatory synapses. The trans-synaptic adhesion between LRRC4B and PTPRF regulates the formation of excitatory synapses in a bidirectional manner (By similarity).

**Summary**, from NCBI Gene [94030](https://www.ncbi.nlm.nih.gov/gene/94030):

> Predicted to enable cell-cell adhesion mediator activity. Predicted to be involved in regulation of synapse assembly and synaptic membrane adhesion. Predicted to be located in cerebellar mossy fiber and presynaptic membrane. Predicted to be active in glutamatergic synapse and postsynaptic density membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25042](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25042) · Entrez [94030](https://www.ncbi.nlm.nih.gov/gene/94030) · UniProt [Q9NT99](https://www.uniprot.org/uniprotkb/Q9NT99) · Ensembl [ENSG00000131409](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131409)

## Data

Gene col 5206: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5206); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5206, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5206]; `tensor/DDL_lfc|DDL_z.npy` [5206]; `embed/gene_vectors.npy` [5206]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5206 or target_col == 5206). Every well: [[LRRC4B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRRC4B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
