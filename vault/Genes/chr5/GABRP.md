---
symbol: "GABRP"
type: "gene"
col: 1725
ensembl_id: "ENSG00000094755"
name: "gamma-aminobutyric acid type A receptor subunit pi"
location: "5q35.1"
module: 8
arm: "+"
pooled_cpm: 3.75
n_lines_expressing: 6
n_dd_up: 22
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 24
direction_downstream: 70
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# GABRP

*gamma-aminobutyric acid type A receptor subunit pi* — 5q35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.55× (z +10.5, q 8e-23, up in 1 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.36× (z +7.4, q 2e-11, up in 0 of 4 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (Panc 03.27 0.0411×, CFPAC-1 0.145×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (CFPAC-1 0.0159×, Panc 03.27 0.0578×; ⚠ cell-cycle shift, explains ~19% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (Panc 03.27 0.130×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MUC4]] (+0.73, fdr 7e-06), [[SYNPR-AS1]] (+0.72, fdr 7e-06), [[TM4SF4]] (+0.69, fdr 7e-06).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 24 arrows point to it, the strongest [[KRT20]] → it (grade C ⚠); 70 go from it, the strongest it → [[CARD14]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1725.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.55×** | +10.5 | 8e-23 | 1/2 (CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.01×** | +9.4 | 1e-18 | 1/2 (CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.00×** | +7.8 | 1e-12 | 1/2 (CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.36×** | +7.4 | 2e-11 | 0/4 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.65×** | +5.9 | 4e-07 | 0/3 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **3.23×** | +5.1 | 3e-05 | 0/3 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.67×** | +4.3 | 0.002 | 0/2 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.98×** | +4.1 | 0.002 | 0/3 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Thymol (drug)]] 0.5 µM |  | **1.97×** | +4.1 | 0.002 | 0/3 | inconsistent across doses | position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.93×** | +4.0 | 0.004 | 0/3 | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.91×** | +3.8 | 0.008 | 1/2 (CFPAC-1) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.20×** | +3.7 | 0.010 | 1/1 (CFPAC-1) | top dose only | noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.53×** | +3.6 | 0.012 | 0/3 | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.85×** | +3.6 | 0.014 | 1/3 (CFPAC-1) | top dose only | cell-cycle shift (explains ~0% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **3.06×** | +3.6 | 0.014 | 0/2 | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.51×** | +3.5 | 0.014 | 0/4 | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +3.4 | 0.023 | 0/4 | top dose only | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.05×** | +3.1 | 0.058 | 0/2 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[18β-Glycyrrhetinic acid (drug)]] 5 µM |  | **1.42×** | +3.0 | 0.075 | 0/4 | inconsistent across doses |  |
| [[Cepharanthine (drug)]] 5 µM |  | **1.42×** | +3.0 | 0.080 | 0/4 | top dose only |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (Panc 03.27 0.0411×, CFPAC-1 0.145×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (CFPAC-1 0.0159×, Panc 03.27 0.0578×; ⚠ cell-cycle shift, explains ~19% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (Panc 03.27 0.130×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1725. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Panc 03.27 (line)]] | alt | 35.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0411× (z -18.2) |
| [[CFPAC-1 (line)]] | alt | 103 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0159× (z -17.2) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.145× (z -11.4) |
| [[A-172 (line)]] | wt | 0.342 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.410 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.271 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.481 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.444 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.545 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.646 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.611 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.340 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.398 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.373 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.405 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.544 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.376 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.336 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.332 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.379 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.354 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.554 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.307 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.631 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.372 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.492 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.340 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.649 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.438 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.305 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.287 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.361 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.402 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.402 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.285 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.590 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.318 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.699 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.474 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.345 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.327 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.874 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.326 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.332 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.475 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.465 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.331 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1725), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MUC4]] | +0.73 | +0.76 / +0.66 | both halves | 7e-06 |  |
| [[SYNPR-AS1]] | +0.72 | +0.71 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[TM4SF4]] | +0.69 | +0.74 / +0.74 | both halves | 7e-06 |  |
| [[SAMD12-AS1]] | +0.67 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[PRSS51]] | +0.66 | +0.62 / +0.48 | both halves | 2e-05 | **novel candidate** |
| [[MUC16]] | +0.66 | +0.66 / +0.52 | both halves | 1e-05 | **novel candidate** |
| [[ALOX5]] | +0.65 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[SLC34A2]] | +0.65 | +0.72 / +0.46 | both halves | 3e-05 | **novel candidate** |
| [[PROM2]] | +0.65 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[LY75]] | +0.64 | +0.53 / +0.58 | both halves | 1e-05 | **novel candidate** |
| [[ADGRF1]] | +0.64 | +0.72 / +0.55 | both halves | 1e-05 |  |
| [[CRACDL]] | +0.64 | +0.60 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 0, C 24. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KRT20]] | C | KRT20 activity raises GABRP's level | lines that do not express KRT20 (46) vs lines expressing it (4) | 1.43× lower at baseline in the lines without KRT20 | 0.001 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: HEPHL1, APOB, BMP10; co-absent with the target |
| [[SIDT1]] | C | SIDT1 activity raises GABRP's level | lines that do not express SIDT1 (32) vs lines expressing it (18) | 1.76× lower at baseline in the lines without SIDT1 | 0.020 | ⚠ within organs, on part of the lines; also absent: TMEM30B, STEAP4, GRHL2; co-absent with the target |
| [[STEAP4]] | C | STEAP4 activity raises GABRP's level | lines that do not express STEAP4 (38) vs lines expressing it (12) | 2.34× lower at baseline in the lines without STEAP4 | 0.021 | ⚠ within organs, on part of the lines; also absent: ADGRF1, WFDC2, SLC5A1; co-absent with the target |
| [[HNF1B]] | C | HNF1B activity raises GABRP's level | lines that do not express HNF1B (31) vs lines expressing it (19) | 1.67× lower at baseline in the lines without HNF1B | 0.021 | ⚠ within organs, on part of the lines; also absent: ENSG00000254261, PDZK1IP1, ADGRF1; co-absent with the target |
| [[PROM1]] | C | PROM1 activity raises GABRP's level | lines that do not express PROM1 (37) vs lines expressing it (13) | 2.17× lower at baseline in the lines without PROM1 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: AZGP1, KRT23, GJB1; co-absent with the target |
| [[RAB25]] | C | RAB25 activity raises GABRP's level | lines that do not express RAB25 (33) vs lines expressing it (17) | 1.87× lower at baseline in the lines without RAB25 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, TMEM30B, PRSS8; co-absent with the target |
| [[SERPINA5]] | C | SERPINA5 activity raises GABRP's level | lines that do not express SERPINA5 (37) vs lines expressing it (13) | 2.08× lower at baseline in the lines without SERPINA5 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02899, SERPINA1, ENSG00000286546; co-absent with the target |
| [[GPR87]] | C | GPR87 activity raises GABRP's level | lines that do not express GPR87 (36) vs lines expressing it (14) | 1.95× lower at baseline in the lines without GPR87 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KLK11, MUC16, HEPHL1; co-absent with the target |
| [[MAL2]] | C | MAL2 activity raises GABRP's level | lines that do not express MAL2 (31) vs lines expressing it (19) | 1.73× lower at baseline in the lines without MAL2 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RAB25, TMEM125, CDH1; co-absent with the target |
| [[WFDC2]] | C | WFDC2 activity raises GABRP's level | lines that do not express WFDC2 (38) vs lines expressing it (12) | 2.28× lower at baseline in the lines without WFDC2 | 0.051 | ⚠ within organs, on part of the lines; also absent: STEAP4, CLIC5, ADGRF1; co-absent with the target |
| [[SLC44A4]] | C | SLC44A4 activity raises GABRP's level | lines that do not express SLC44A4 (37) vs lines expressing it (13) | 2.20× lower at baseline in the lines without SLC44A4 | 0.052 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC1, LCN2, NPSR1; co-absent with the target |
| [[MUC5B]] | C | MUC5B activity raises GABRP's level | lines that do not express MUC5B (37) vs lines expressing it (13) | 2.22× lower at baseline in the lines without MUC5B | 0.057 | ⚠ within organs, on part of the lines; also absent: DAPP1, AGR3, ENSG00000259925; co-absent with the target |

### Downstream of this gene

*70 arrows, 70 of them with an alert ⚠; grade A 0, B 15, C 55. Shown: the 12 strongest; 58 more arrows (58 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CARD14]] | B | GABRP activity raises CARD14's level | lines that do not express GABRP (44) vs lines expressing it (6) | 2.56× lower at baseline in the lines without GABRP | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT20, FGFR2, SLC34A2 |
| [[MYH14]] | B | GABRP activity raises MYH14's level | lines that do not express GABRP (44) vs lines expressing it (6) | 5.45× lower at baseline in the lines without GABRP | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT20, FGFR2, SLC34A2 |
| [[NPEPPSP1]] | B | GABRP activity raises NPEPPSP1's level | lines that do not express GABRP (44) vs lines expressing it (6) | 3.23× lower at baseline in the lines without GABRP | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT20, FGFR2, SLC34A2 |
| [[PROM2]] | B | GABRP activity raises PROM2's level | lines that do not express GABRP (44) vs lines expressing it (6) | 3.22× lower at baseline in the lines without GABRP | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT20, FGFR2, SLC34A2 |
| [[MUC20]] | B | GABRP activity raises MUC20's level | lines that do not express GABRP (44) vs lines expressing it (6) | 4.03× lower at baseline in the lines without GABRP | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT20, FGFR2, SLC34A2 |
| [[ATAD3C]] | B | GABRP activity raises ATAD3C's level | lines that do not express GABRP (44) vs lines expressing it (6) | 2.85× lower at baseline in the lines without GABRP | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT20, FGFR2, SLC34A2 |
| [[BCL2L15]] | B | GABRP activity raises BCL2L15's level | lines that do not express GABRP (44) vs lines expressing it (6) | 3.11× lower at baseline in the lines without GABRP | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT20, FGFR2, SLC34A2 |
| [[SPATA6L]] | B | GABRP activity raises SPATA6L's level | lines that do not express GABRP (44) vs lines expressing it (6) | 4.37× lower at baseline in the lines without GABRP | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT20, FGFR2, SLC34A2 |
| [[SAMD12]] | B | GABRP activity raises SAMD12's level | lines that do not express GABRP (44) vs lines expressing it (6) | 4.99× lower at baseline in the lines without GABRP | 0.059 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT20, FGFR2, SLC34A2 |
| [[OCLN]] | B | GABRP activity raises OCLN's level | lines that do not express GABRP (44) vs lines expressing it (6) | 5.48× lower at baseline in the lines without GABRP | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT20, FGFR2, SLC34A2 |
| [[YWHAEP7-1]] | B | GABRP activity raises YWHAEP7-1's level | lines that do not express GABRP (44) vs lines expressing it (6) | 2.41× lower at baseline in the lines without GABRP | 0.084 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT20, FGFR2, SLC34A2 |
| [[GNA14]] | B | GABRP activity raises GNA14's level | lines that do not express GABRP (44) vs lines expressing it (6) | 2.12× lower at baseline in the lines without GABRP | 0.086 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT20, FGFR2, SLC34A2 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.707). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.5, 55.2); signed map (61.2, 1.3). **Vector** length 21.7, 11.0% of its response variance represented; |z| ≥ 3 in 112 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Dectin-2 family* (reactome, mean cos +0.53 to 5); *O-linked glycosylation of mucins* (reactome, mean cos +0.55 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.9 | +7.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.9 | +10.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.8 | +9.4 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +0.9 | +3.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +0.9 | +7.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.7 | +0.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +0.5 | +1.6 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +0.5 | -0.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +0.4 | +1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.4 | +2.2 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.8 | -2.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | -0.7 | +0.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.5 | -1.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -0.5 | -1.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.4 | -2.1 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -0.4 | -1.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.4 | -2.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.3 | +1.1 |

## What is on record

|  |  |
|---|---|
| Name | gamma-aminobutyric acid type A receptor subunit pi |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.1 — chr5:170,763,350-170,814,047 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Gamma-aminobutyric acid type A receptor subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [O00591](https://www.uniprot.org/uniprotkb/O00591) (Gamma-aminobutyric acid receptor subunit pi):

> Pi subunit of the heteropentameric ligand-gated chloride channel gated by gamma-aminobutyric acid (GABA). GABA-gated chloride channels, also named GABA(A) receptors (GABAAR), consist of five subunits arranged around a central pore and contain GABA active binding site(s) located at the alpha and beta subunit interfaces (By similarity). When activated by GABA, GABAARs selectively allow the flow of chloride anions across the cell membrane down their electrochemical gradient. Pi-containing GABAARs …

**Summary**, from NCBI Gene [2568](https://www.ncbi.nlm.nih.gov/gene/2568):

> The gamma-aminobutyric acid (GABA) A receptor is a multisubunit chloride channel that mediates the fastest inhibitory synaptic transmission in the central nervous system. The subunit encoded by this gene is expressed in several non-neuronal tissues including the uterus and ovaries. This subunit can assemble with known GABA A receptor subunits, and the presence of this subunit alters the sensitivity of recombinant receptors to modulatory agents such as pregnanolone. Alternatively spliced …

**Accessions** — [HGNC:4089](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4089) · Entrez [2568](https://www.ncbi.nlm.nih.gov/gene/2568) · UniProt [O00591](https://www.uniprot.org/uniprotkb/O00591) · Ensembl [ENSG00000094755](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000094755)

## Data

Gene col 1725: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1725); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1725, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1725]; `tensor/DDL_lfc|DDL_z.npy` [1725]; `embed/gene_vectors.npy` [1725]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1725 or target_col == 1725). Every well: [[GABRP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GABRP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
