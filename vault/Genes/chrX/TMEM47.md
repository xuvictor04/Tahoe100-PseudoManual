---
symbol: "TMEM47"
type: "gene"
col: 7139
ensembl_id: "ENSG00000147027"
name: "transmembrane protein 47"
location: "Xp21.1"
module: 66
arm: "+"
pooled_cpm: 19.55
n_lines_expressing: 23
n_dd_up: 22
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 3
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# TMEM47

*transmembrane protein 47* — Xp21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.37× (z +13.5, q 2e-38, up in 11 of 20 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.76× (z +8.8, q 1e-16, up in 9 of 21 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SW1417 0.516×, A-427 0.413×); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.431×; ⚠ cell-cycle shift, explains ~38% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-427 0.520×); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (AN3 CA 0.0898×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DMD]] (+0.63, fdr 1e-05), [[PDLIM3]] (+0.59, fdr 2e-05), [[AKR1B1]] (+0.59, fdr 1e-05); moves opposite to [[WDR37]] (-0.54, fdr 2e-05), [[RPGRIP1L]] (-0.49, fdr 6e-05), [[ZNF875]] (-0.49, fdr 4e-05).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 3 go from it, the strongest it → [[EPHA5]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7139.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.37×** | +13.5 | 2e-38 | 11/20 (SW1417, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.69×** | +10.1 | 1e-21 | 8/19 (HS-578T, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.56×** | +10.0 | 2e-21 | 8/17 (SW480, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +8.8 | 1e-16 | 9/21 (NCI-H460, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.59×** | +7.3 | 3e-11 | 10/21 (A549, CFPAC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.58×** | +7.2 | 5e-11 | 12/20 (NCI-H460, hTERT-HPNE, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.85×** | +6.6 | 4e-09 | 10/20 (SNU-423, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +6.2 | 3e-08 | 9/21 (SNU-423, J82, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.59×** | +5.1 | 2e-05 | 9/21 (NCI-H460, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.52×** | +4.5 | 4e-04 | 13/21 (NCI-H460, J82, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.47×** | +4.3 | 0.001 | 9/20 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.45×** | +4.2 | 0.001 | 10/21 (SW480, C32, …) | two highest doses | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +4.1 | 0.001 | 11/20 (SNU-423, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.41×** | +3.9 | 0.004 | 8/21 (SW480, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.42×** | +3.9 | 0.004 | 4/20 (HS-578T, A-427, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.42×** | +3.8 | 0.006 | 10/20 (SW480, C32, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.38×** | +3.4 | 0.021 | 8/20 (SW480, C32, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.31×** | +3.0 | 0.078 | 7/20 (SW1417, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.30×** | +2.9 | 0.092 | 6/21 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.55×** | +2.9 | 0.093 | 5/20 (SW480, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7139.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SW1417 0.516×, A-427 0.413×); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.431×; ⚠ cell-cycle shift, explains ~38% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-427 0.520×); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (AN3 CA 0.0898×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.716× | -3.4 | 0.17 | 1/21 (CFPAC-1) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.721× | -3.4 | 0.17 | 10/20 (AN3 CA, SW480, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.914× | -3.3 | 0.17 | 1/21 (NCI-H661) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7139. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 13.7 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +13.5) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.48× (z +10.8) | — |
| [[A-427 (line)]] | wt | 108 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -12.6) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.520× (z -9.8) |
| [[SW1417 (line)]] | alt | 166 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.57× (z +9.6) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.516× (z -9.5) |
| [[AN3 CA (line)]] | alt | 36.0 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0898× (z -9.0) |
| [[HS-578T (line)]] | alt | 44.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +8.9) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 38.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +11.1) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[J82 (line)]] | alt | 24.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +9.3) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[SNU-423 (line)]] | alt | 52.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.37× (z +9.0) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 76.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.35× (z +8.7) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 3.16 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 34.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.46 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 34.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 55.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.34 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.82 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.972 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 8.85 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.76 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.43 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 66.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.59 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.59 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.59 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7139), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DMD]] | +0.63 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[PDLIM3]] | +0.59 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[AKR1B1]] | +0.59 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[DSEL]] | +0.57 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[OLR1]] | +0.56 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[RPS6KA6]] | +0.54 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[TRIML2]] | +0.54 | +0.41 / +0.47 | both halves | 4e-05 |  |
| [[TMEM52B]] | +0.53 | +0.38 / +0.49 | both halves | 7e-05 |  |
| [[EPHA5]] | +0.53 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[MRAS]] | +0.52 | +0.42 / +0.46 | both halves | 4e-05 |  |
| [[KCNT2]] | +0.52 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[LUM]] | +0.52 | +0.41 / +0.53 | both halves | 4e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR37]] | -0.54 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[RPGRIP1L]] | -0.49 | -0.44 / -0.39 | both halves | 6e-05 |  |
| [[ZNF875]] | -0.49 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[C13orf46]] | -0.49 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[THOC3]] | -0.48 | -0.48 / -0.30 | both halves | 2e-04 |  |
| [[HERC2P3]] | -0.48 | -0.37 / -0.38 | both halves | 8e-05 |  |
| [[GNAS-AS1]] | -0.48 | -0.53 / -0.37 | both halves | 8e-05 |  |
| [[RASA3]] | -0.48 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[CDK5RAP1]] | -0.47 | -0.55 / -0.34 | both halves | 1e-04 |  |
| [[HERC2P9]] | -0.47 | -0.42 / -0.37 | both halves | 8e-05 |  |
| [[DGKG]] | -0.47 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[ZNF70]] | -0.47 | -0.40 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 1, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers TMEM47's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.5% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |
| [[EPHA5]] | C | EPHA5 activity raises TMEM47's level | lines that do not express EPHA5 (30) vs lines expressing it (20) | 3.59× lower at baseline in the lines without EPHA5 | 0.039 | ⚠ within organs, on part of the lines; also absent: EPHA5-AS1, CDH10, TRPC4; co-absent with the target |
| [[POU3F2]] | C | POU3F2 activity raises TMEM47's level | lines that do not express POU3F2 (32) vs lines expressing it (18) | 3.38× lower at baseline in the lines without POU3F2 | 0.053 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MSR1, AMPH, SPARC; co-absent with the target |
| [[FMN2]] | C | FMN2 activity raises TMEM47's level | lines that do not express FMN2 (26) vs lines expressing it (24) | 3.64× lower at baseline in the lines without FMN2 | 0.088 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, TRPC4, HECW2; maybe low, not absent; co-absent with the target |
| [[PEG10]] | C | PEG10 activity raises TMEM47's level | lines that do not express PEG10 (17) vs lines expressing it (33) | 3.31× lower at baseline in the lines without PEG10 | 0.099 | ⚠ within organs, on part of the lines; also absent: ZNF569, ZNF570, MAP1B; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPHA5]] | C | TMEM47 activity raises EPHA5's level | lines that do not express TMEM47 (27) vs lines expressing it (23) | 3.53× lower at baseline in the lines without TMEM47 | 0.031 | ⚠ within organs, on part of the lines; also absent: KCNE4, ENSG00000280241, ENSG00000225649; co-absent with the target |
| [[LUM]] | C | TMEM47 activity raises LUM's level | lines that do not express TMEM47 (27) vs lines expressing it (23) | 2.75× lower at baseline in the lines without TMEM47 | 0.042 | ⚠ within organs, on part of the lines; also absent: KCNE4, ENSG00000280241, ENSG00000225649; co-absent with the target |
| [[PEG10]] | C | TMEM47 activity raises PEG10's level | lines that do not express TMEM47 (27) vs lines expressing it (23) | 3.68× lower at baseline in the lines without TMEM47 | 0.089 | ⚠ within organs, on part of the lines; also absent: KCNE4, ENSG00000280241, ENSG00000225649; co-absent with the target |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.492). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (33.8, 22.7); signed map (45.9, 20.8). **Vector** length 51.0, 12.3% of its response variance represented; |z| ≥ 3 in 473 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +7.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.9 | +13.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +3.7 | +7.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +10.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.6 | +5.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.2 | +4.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.0 | +3.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.0 | +3.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.8 | +3.4 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.6 | -0.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.3 | -0.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -1.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.2 | -1.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -0.7 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.0 | -2.1 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -0.8 | -2.0 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -0.8 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 47 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp21.1 — chrX:34,627,075-34,657,285 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BCMP1, DKFZP761J17121, DKFZp564E153, VAB-9; previously TM4SF10 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BQJ4](https://www.uniprot.org/uniprotkb/Q9BQJ4) (Transmembrane protein 47):

> Regulates cell junction organization in epithelial cells. May play a role in the transition from adherens junction to tight junction assembly. May regulate F-actin polymerization required for tight junctional localization dynamics and affect the junctional localization of PARD6B. During podocyte differentiation may negatively regulate activity of FYN and subsequently the abundance of nephrin (By similarity).

**Summary**, from NCBI Gene [83604](https://www.ncbi.nlm.nih.gov/gene/83604):

> This gene encodes a member of the PMP22/EMP/claudin protein family. The encoded protein is localized to the ER and the plasma membrane. In dogs, transcripts of this gene exist at high levels in the brain. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:18515](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18515) · Entrez [83604](https://www.ncbi.nlm.nih.gov/gene/83604) · UniProt [Q9BQJ4](https://www.uniprot.org/uniprotkb/Q9BQJ4) · Ensembl [ENSG00000147027](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147027)

## Data

Gene col 7139: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7139); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7139, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7139]; `tensor/DDL_lfc|DDL_z.npy` [7139]; `embed/gene_vectors.npy` [7139]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7139 or target_col == 7139). Every well: [[TMEM47 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM47.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
