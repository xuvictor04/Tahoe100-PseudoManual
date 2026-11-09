---
symbol: "MUC16"
type: "gene"
col: 11169
ensembl_id: "ENSG00000181143"
name: "mucin 16, cell surface associated"
location: "19p13.2"
module: 8
arm: "+"
pooled_cpm: 18.04
n_lines_expressing: 12
n_dd_up: 19
n_dd_down: 0
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 55
direction_downstream: 67
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# MUC16

*mucin 16, cell surface associated* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.22× (z +12.6, q 1e-33, up in 2 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.96× (z +7.2, q 6e-11, up in 0 of 11 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (CFPAC-1 0.0846×, HT-29 0.0877×, Panc 03.27 0.216×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (HT-29 0.0437×, CFPAC-1 0.125×); [[Belinostat (drug)]] 5 µM in 1 line (LoVo 0.0654×; ⚠ cell-cycle shift, explains ~44% of this change); [[Selinexor (drug)]] 5 µM in 1 line (LoVo 0.219×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MUC4]] (+0.80, fdr 7e-06), [[ADGRF1]] (+0.69, fdr 7e-06), [[SLC34A2]] (+0.67, fdr 7e-06); moves opposite to [[LINC02985]] (-0.48, fdr 5e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 55 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 67 go from it, the strongest it → [[EFNA1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11169.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.22×** | +12.6 | 1e-33 | 2/10 (NCI-H2347, NCI-H1573) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.69×** | +9.6 | 2e-19 | 2/7 (Hs 766T, NCI-H2347) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.46×** | +8.8 | 4e-16 | 0/9 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.96×** | +7.2 | 6e-11 | 0/11 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **2.20×** | +7.2 | 9e-11 | 9/10 (NCI-H23, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.81×** | +6.4 | 2e-08 | 3/10 (LoVo, HT-29, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.97×** | +5.2 | 2e-05 | 8/11 (NCI-H23, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.93×** | +4.8 | 1e-04 | 8/10 (A549, NCI-H23, …) | rises with dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.70×** | +4.0 | 0.004 | 0/10 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.41×** | +3.7 | 0.013 | 0/10 | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.65×** | +3.7 | 0.013 | 10/10 (NCI-H23, A549, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.54×** | +3.3 | 0.047 | 6/11 (NCI-H23, CFPAC-1, …) | rises with dose | position effect removed |
| [[Trametinib (drug)]] 5 µM |  | **1.45×** | +3.2 | 0.061 | 7/11 (NCI-H23, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.52×** | +3.2 | 0.061 | 1/11 (A549) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.34×** | +3.1 | 0.063 | 9/10 (NCI-H23, A549, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.35×** | +3.1 | 0.063 | 6/11 (CFPAC-1, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Pimozide (drug)]] 0.05 µM |  | **1.51×** | +3.1 | 0.063 | 3/10 (LoVo, NCI-H2347, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.53×** | +3.0 | 0.090 | 1/10 (LoVo) | inconsistent across doses | position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.47×** | +2.9 | 0.098 | 1/10 (NCI-H23) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11169.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (CFPAC-1 0.0846×, HT-29 0.0877×, Panc 03.27 0.216×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (HT-29 0.0437×, CFPAC-1 0.125×); [[Belinostat (drug)]] 5 µM in 1 line (LoVo 0.0654×; ⚠ cell-cycle shift, explains ~44% of this change); [[Selinexor (drug)]] 5 µM in 1 line (LoVo 0.219×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | 0.627× | -3.6 | 0.18 | 7/10 (LoVo, CFPAC-1, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.645× | -3.4 | 0.21 | 10/10 (HT-29, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.41 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11169. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 20.5 | 0 | 3 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0654× (z -11.1) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.219× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 171 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0846× (z -14.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.125× (z -8.5) |
| [[HT-29 (line)]] | alt | 25.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0877× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0437× (z -10.1) |
| [[NCI-H23 (line)]] | alt | 16.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 2.19× (z +9.3) ⚠ position not correctable | [[Digitoxin (drug)]] 5 µM 0.0589× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 423 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 2.19 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.869 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.916 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 8.16 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.965 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.929 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.05 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.971 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.933 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.816 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.953 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.13 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.692 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.746 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.962 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 226 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.30 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.985 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.962 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.848 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.926 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.44 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11169), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MUC4]] | +0.80 | +0.76 / +0.77 | both halves | 7e-06 | same gene group; pathway: C-type lectin receptors (CLRs); STRING 969 |
| [[ADGRF1]] | +0.69 | +0.67 / +0.70 | both halves | 7e-06 | same gene group |
| [[SLC34A2]] | +0.67 | +0.59 / +0.63 | both halves | 7e-06 | pathway: Diseases of metabolism |
| [[ST14]] | +0.66 | +0.65 / +0.65 | both halves | 7e-06 | same gene group |
| [[GABRP]] | +0.66 | +0.66 / +0.52 | both halves | 1e-05 | **novel candidate** |
| [[GPRIN2]] | +0.65 | +0.64 / +0.56 | both halves | 1e-05 | STRING 472 |
| [[CLIC5]] | +0.64 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[SLC15A1]] | +0.64 | +0.51 / +0.62 | both halves | 1e-05 | **novel candidate** |
| [[TC2N]] | +0.64 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[MYH14]] | +0.64 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[MAL2]] | +0.63 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[ALOX5]] | +0.63 | +0.60 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02985]] | -0.48 | -0.49 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*55 arrows, 55 of them with an alert ⚠; grade A 0, B 3, C 52. Shown: the 12 strongest; 43 more arrows (43 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers MUC16's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.1% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[BCL2L15]] | B | BCL2L15 activity raises MUC16's level | lines that do not express BCL2L15 (20) vs lines expressing it (30) | 2.88× lower at baseline in the lines without BCL2L15 | 0.079 | ⚠ within organs, on part of the lines; also absent: SYK, NOS3, CASC8; maybe low, not absent |
| [[SLC44A3-AS1]] | B | SLC44A3-AS1 activity raises MUC16's level | lines that do not express SLC44A3-AS1 (13) vs lines expressing it (37) | 2.51× lower at baseline in the lines without SLC44A3-AS1 | 0.093 | ⚠ within organs, on part of the lines; also absent: SLC44A3, CRYBG2, ENSG00000287306; maybe low, not absent |
| [[STEAP4]] | C | STEAP4 activity raises MUC16's level | lines that do not express STEAP4 (38) vs lines expressing it (12) | 9.07× lower at baseline in the lines without STEAP4 | 7e-04 | ⚠ within organs, on part of the lines; also absent: ADGRF1, WFDC2, SLC5A1; co-absent with the target |
| [[MAL2]] | C | MAL2 activity raises MUC16's level | lines that do not express MAL2 (31) vs lines expressing it (19) | 4.01× lower at baseline in the lines without MAL2 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RAB25, TMEM125, CDH1; co-absent with the target |
| [[TMEM30B]] | C | TMEM30B activity raises MUC16's level | lines that do not express TMEM30B (35) vs lines expressing it (15) | 5.78× lower at baseline in the lines without TMEM30B | 0.003 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ANKRD22, RAB25; co-absent with the target |
| [[PROM1]] | C | PROM1 activity raises MUC16's level | lines that do not express PROM1 (37) vs lines expressing it (13) | 4.79× lower at baseline in the lines without PROM1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: AZGP1, KRT23, GJB1; co-absent with the target |
| [[CLIC5]] | C | CLIC5 activity raises MUC16's level | lines that do not express CLIC5 (37) vs lines expressing it (13) | 6.89× lower at baseline in the lines without CLIC5 | 0.004 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, KLK11, CLRN3; co-absent with the target |
| [[ADGRF1]] | C | ADGRF1 activity raises MUC16's level | lines that do not express ADGRF1 (35) vs lines expressing it (15) | 6.16× lower at baseline in the lines without ADGRF1 | 0.004 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4; co-absent with the target |
| [[ITGB6]] | C | ITGB6 activity raises MUC16's level | lines that do not express ITGB6 (32) vs lines expressing it (18) | 4.41× lower at baseline in the lines without ITGB6 | 0.006 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS2, TMPRSS4; co-absent with the target |
| [[TMPRSS4]] | C | TMPRSS4 activity raises MUC16's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 4.85× lower at baseline in the lines without TMPRSS4 | 0.007 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B; co-absent with the target |
| [[GABRP]] | C | GABRP activity raises MUC16's level | lines that do not express GABRP (44) vs lines expressing it (6) | 14.40× lower at baseline in the lines without GABRP | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT20, FGFR2, SLC34A2; co-absent with the target |

### Downstream of this gene

*67 arrows, 67 of them with an alert ⚠; grade A 0, B 17, C 50. Shown: the 12 strongest; 55 more arrows (55 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EFNA1]] | B | MUC16 activity raises EFNA1's level | lines that do not express MUC16 (38) vs lines expressing it (12) | 2.82× lower at baseline in the lines without MUC16 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSDMC, S100A9, STEAP4 |
| [[SLC44A3-AS1]] | B | MUC16 activity raises SLC44A3-AS1's level | lines that do not express MUC16 (38) vs lines expressing it (12) | 2.62× lower at baseline in the lines without MUC16 | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSDMC, S100A9, STEAP4 |
| [[KIAA1522]] | B | MUC16 activity raises KIAA1522's level | lines that do not express MUC16 (38) vs lines expressing it (12) | 2.28× lower at baseline in the lines without MUC16 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSDMC, S100A9, STEAP4 |
| [[NPEPPSP1]] | B | MUC16 activity raises NPEPPSP1's level | lines that do not express MUC16 (38) vs lines expressing it (12) | 2.09× lower at baseline in the lines without MUC16 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSDMC, S100A9, STEAP4 |
| [[EPS8L1]] | B | MUC16 activity raises EPS8L1's level | lines that do not express MUC16 (38) vs lines expressing it (12) | 2.33× lower at baseline in the lines without MUC16 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSDMC, S100A9, STEAP4 |
| [[RBM47]] | B | MUC16 activity raises RBM47's level | lines that do not express MUC16 (38) vs lines expressing it (12) | 4.01× lower at baseline in the lines without MUC16 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSDMC, S100A9, STEAP4 |
| [[NHSL1-AS1]] | B | MUC16 activity weakens NHSL1-AS1's drug response | lines that do not express MUC16 (28) vs lines expressing it (8) | the lines without MUC16 respond 1.92× as strongly (z diff -1.81); strongest at Panobinostat 0.5 µM: 0.31x vs 0.76x (z diff -3.5) | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSDMC, S100A9, STEAP4; target measured in part of the lines; artifact flags |
| [[JUP]] | B | MUC16 activity raises JUP's level | lines that do not express MUC16 (38) vs lines expressing it (12) | 3.35× lower at baseline in the lines without MUC16 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSDMC, S100A9, STEAP4 |
| [[NPEPPSP1]] | B | MUC16 activity weakens NPEPPSP1's drug response | lines that do not express MUC16 (36) vs lines expressing it (9) | the lines without MUC16 respond 1.03× as strongly (z diff -0.30); strongest at Dinaciclib 5 µM: 2.96x vs 0.61x (z diff -6.5) | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSDMC, S100A9, STEAP4; target measured in part of the lines; both ways; artifact flags |
| [[STYK1]] | B | MUC16 activity raises STYK1's level | lines that do not express MUC16 (38) vs lines expressing it (12) | 3.95× lower at baseline in the lines without MUC16 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSDMC, S100A9, STEAP4 |
| [[OCLN]] | B | MUC16 activity raises OCLN's level | lines that do not express MUC16 (38) vs lines expressing it (12) | 3.73× lower at baseline in the lines without MUC16 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSDMC, S100A9, STEAP4 |
| [[MYH14]] | B | MUC16 activity raises MYH14's level | lines that do not express MUC16 (38) vs lines expressing it (12) | 2.68× lower at baseline in the lines without MUC16 | 0.066 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSDMC, S100A9, STEAP4 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.706). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.6, 55.8); signed map (61.7, 1.3). **Vector** length 52.2, 22.9% of its response variance represented; |z| ≥ 3 in 308 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | +12.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.4 | +8.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +6.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.3 | +7.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.0 | +5.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.9 | +4.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.7 | +3.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.6 | -2.1 |
|  | [[Selinexor (drug)]] 5 µM |  | -1.4 | -2.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.3 | -3.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.1 | -2.0 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.1 | -2.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.1 | -1.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -3.0 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.1 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | mucin 16, cell surface associated |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:8,848,844-9,010,390 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CA125, FLJ14303, CA-125 |
| Gene groups (HGNC) | Mucins; SEA domain containing |
| Reactome | 12 pathways, smallest: Defective GALNT12 causes CRCS1; Defective GALNT3 causes HFTC; Defective C1GALT1C1 causes TNPS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WXI7](https://www.uniprot.org/uniprotkb/Q8WXI7) (Mucin-16):

> Thought to provide a protective, lubricating barrier against particles and infectious agents at mucosal surfaces.

**Summary**, from NCBI Gene [94025](https://www.ncbi.nlm.nih.gov/gene/94025):

> This gene encodes a protein that is a member of the mucin family. Mucins are high molecular weight, O-glycosylated proteins that play an important role in forming a protective mucous barrier, and are found on the apical surfaces of the epithelia. The encoded protein is a membrane-tethered mucin that contains an extracellular domain at its amino terminus, a large tandem repeat domain, and a transmembrane domain with a short cytoplasmic domain. The amino terminus is highly glycosylated, while the …

**Accessions** — [HGNC:15582](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15582) · Entrez [94025](https://www.ncbi.nlm.nih.gov/gene/94025) · UniProt [Q8WXI7](https://www.uniprot.org/uniprotkb/Q8WXI7) · Ensembl [ENSG00000181143](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000181143)

## Data

Gene col 11169: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11169); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11169, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11169]; `tensor/DDL_lfc|DDL_z.npy` [11169]; `embed/gene_vectors.npy` [11169]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11169 or target_col == 11169). Every well: [[MUC16 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MUC16.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
