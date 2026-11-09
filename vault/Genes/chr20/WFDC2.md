---
symbol: "WFDC2"
type: "gene"
col: 2138
ensembl_id: "ENSG00000101443"
name: "WAP four-disulfide core domain 2"
location: "20q13.12"
module: 8
arm: "+"
pooled_cpm: 14.18
n_lines_expressing: 12
n_dd_up: 15
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 40
direction_downstream: 85
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# WFDC2

*WAP four-disulfide core domain 2* — 20q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.77× (z +9.1, q 4e-17, up in 4 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.42× (z +7.6, q 7e-12, up in 4 of 10 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H2347 0.191×, Panc 03.27 0.244×, SW480 0.263×; ⚠ cell-cycle shift, explains ~36% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H2347 0.239×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDZK1IP1]] (+0.74, fdr 7e-06), [[MMP7]] (+0.71, fdr 7e-06), [[TACSTD2]] (+0.68, fdr 7e-06); moves opposite to [[DCTD]] (-0.51, fdr 4e-05), [[MCM3AP]] (-0.45, fdr 5e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 40 arrows point to it, the strongest [[CFB]] → it (grade B ⚠); 85 go from it, the strongest it → [[MUC20]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 9 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2138.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.77×** | +9.1 | 4e-17 | 4/9 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.15×** | +8.6 | 2e-15 | 4/9 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.42×** | +7.6 | 7e-12 | 4/10 (SW 900, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.05×** | +6.3 | 5e-08 | 4/9 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.72×** | +4.6 | 4e-04 | 0/10 | top dose only | composition shift |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **2.03×** | +4.3 | 0.002 | 10/10 (CFPAC-1, SW 900, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.98×** | +4.1 | 0.003 | 3/10 (KATO III, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Decitabine (drug)]] 0.5 µM |  | **1.78×** | +3.5 | 0.032 | 0/10 | inconsistent across doses | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.82×** | +3.5 | 0.032 | 1/10 (KATO III) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.72×** | +3.3 | 0.057 | 5/10 (COLO 205, SW1417, …) | top dose only | position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.68×** | +3.1 | 0.086 | 0/10 | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.67×** | +3.1 | 0.086 | 6/10 (SW1417, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +3.1 | 0.086 | 2/10 (HT-29, COLO 205) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.17× | +3.1 | 0.086 | 1/10 (SW480) | inconsistent across doses |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.65×** | +3.0 | 0.092 | 0/10 | top dose only |  |
| [[Omeprazole (drug)]] 0.5 µM |  | **1.64×** | +3.0 | 0.099 | 3/10 (SW 900, SW1417, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2138.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H2347 0.191×, Panc 03.27 0.244×, SW480 0.263×; ⚠ cell-cycle shift, explains ~36% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H2347 0.239×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.530× | -3.6 | 0.10 | 4/10 (NCI-H2347, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.532× | -3.6 | 0.10 | 7/10 (Panc 03.27, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | 0.563× | -3.2 | 0.22 | 1/10 (SW1417) | inconsistent across doses |  |
| [[Ciclopirox (drug)]] 0.5 µM |  | 0.608× | -3.0 | 0.31 | 0/10 | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2138. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 11.9 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 9.64× (z +12.7) | — |
| [[NCI-H2347 (line)]] | alt | 110 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -14.0) ⚠ cell-cycle shift, explains ~36% of this change |
| [[Panc 03.27 (line)]] | alt | 207 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -10.9) ⚠ cell-cycle shift, explains ~36% of this change |
| [[SW480 (line)]] | alt | 13.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -8.6) ⚠ cell-cycle shift, explains ~36% of this change |
| [[A-172 (line)]] | wt | 0.653 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.565 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.588 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.546 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 9.64 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.933 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.718 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.708 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.840 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.683 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.985 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.783 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.759 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.805 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.890 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.677 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.898 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.93 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.643 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.93 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.629 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.834 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.657 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.62 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.851 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.793 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.902 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2138), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDZK1IP1]] | +0.74 | +0.67 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[MMP7]] | +0.71 | +0.76 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[TACSTD2]] | +0.68 | +0.72 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[HLA-DRB1]] | +0.65 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[LCN2]] | +0.64 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[GABRP]] | +0.59 | +0.74 / +0.37 | both halves | 8e-05 |  |
| [[SLC34A2]] | +0.59 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[MUC1]] | +0.58 | +0.59 / +0.57 | both halves | 1e-05 | STRING 509 |
| [[LRG1]] | +0.57 | +0.40 / +0.58 | both halves | 5e-05 |  |
| [[FXYD3]] | +0.57 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[SLPI]] | +0.57 | +0.49 / +0.56 | both halves | 1e-05 | same gene group; STRING 648 |
| [[SLC44A4]] | +0.57 | +0.61 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCTD]] | -0.51 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[MCM3AP]] | -0.45 | -0.40 / -0.47 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*40 arrows, 40 of them with an alert ⚠; grade A 0, B 1, C 39. Shown: the 12 strongest; 28 more arrows (28 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CFB]] | B | CFB activity raises WFDC2's level | lines that do not express CFB (20) vs lines expressing it (30) | 2.29× lower at baseline in the lines without CFB | 0.079 | ⚠ within organs, on part of the lines; also absent: SAA4, RHBDL2, IL2RG |
| [[STEAP4]] | C | STEAP4 activity raises WFDC2's level | lines that do not express STEAP4 (38) vs lines expressing it (12) | 8.11× lower at baseline in the lines without STEAP4 | 0.001 | ⚠ within organs, on part of the lines; also absent: ADGRF1, WFDC2, SLC5A1; co-absent with the target |
| [[ADGRF1]] | C | ADGRF1 activity raises WFDC2's level | lines that do not express ADGRF1 (35) vs lines expressing it (15) | 6.10× lower at baseline in the lines without ADGRF1 | 0.002 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4; co-absent with the target |
| [[RNF39]] | C | RNF39 activity raises WFDC2's level | lines that do not express RNF39 (30) vs lines expressing it (20) | 4.54× lower at baseline in the lines without RNF39 | 0.003 | ⚠ within organs, on part of the lines; also absent: CDH1, TNNT2, TRIM15; maybe low, not absent; co-absent with the target |
| [[C11orf52]] | C | C11orf52 activity raises WFDC2's level | lines that do not express C11orf52 (23) vs lines expressing it (27) | 3.16× lower at baseline in the lines without C11orf52 | 0.005 | ⚠ within organs, on part of the lines; also absent: TNNT2, MPZL3, RNF39; co-absent with the target |
| [[SLC44A4]] | C | SLC44A4 activity raises WFDC2's level | lines that do not express SLC44A4 (37) vs lines expressing it (13) | 4.79× lower at baseline in the lines without SLC44A4 | 0.008 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC1, LCN2, NPSR1; co-absent with the target |
| [[ALOX5]] | C | ALOX5 activity raises WFDC2's level | lines that do not express ALOX5 (28) vs lines expressing it (22) | 3.23× lower at baseline in the lines without ALOX5 | 0.008 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ADGRF1, RASSF6; co-absent with the target |
| [[KRT23]] | C | KRT23 activity raises WFDC2's level | lines that do not express KRT23 (40) vs lines expressing it (10) | 5.41× lower at baseline in the lines without KRT23 | 0.010 | ⚠ within organs, on part of the lines; also absent: PROM1, HSD17B2, GABRP; co-absent with the target |
| [[TACSTD2]] | C | TACSTD2 activity raises WFDC2's level | lines that do not express TACSTD2 (34) vs lines expressing it (16) | 4.38× lower at baseline in the lines without TACSTD2 | 0.016 | ⚠ within organs, on part of the lines; also absent: SLC5A1, PRKCH-AS1, KCNE3; co-absent with the target |
| [[LCN2]] | C | LCN2 activity raises WFDC2's level | lines that do not express LCN2 (33) vs lines expressing it (17) | 3.69× lower at baseline in the lines without LCN2 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS8, RAB25, TMPRSS4; co-absent with the target |
| [[MUC4]] | C | MUC4 activity raises WFDC2's level | lines that do not express MUC4 (41) vs lines expressing it (9) | 6.78× lower at baseline in the lines without MUC4 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, SLC34A2, CST6; co-absent with the target |
| [[RHOV]] | C | RHOV activity raises WFDC2's level | lines that do not express RHOV (23) vs lines expressing it (27) | 3.10× lower at baseline in the lines without RHOV | 0.019 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SULT2B1, PLEKHG6; co-absent with the target |

### Downstream of this gene

*85 arrows, 85 of them with an alert ⚠; grade A 0, B 33, C 52. Shown: the 12 strongest; 73 more arrows (73 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MUC20]] | B | WFDC2 activity raises MUC20's level | lines that do not express WFDC2 (38) vs lines expressing it (12) | 4.49× lower at baseline in the lines without WFDC2 | 7e-04 | ⚠ within organs, on part of the lines; also absent: STEAP4, CLIC5, ADGRF1 |
| [[BCL2L15]] | B | WFDC2 activity raises BCL2L15's level | lines that do not express WFDC2 (38) vs lines expressing it (12) | 3.66× lower at baseline in the lines without WFDC2 | 0.001 | ⚠ within organs, on part of the lines; also absent: STEAP4, CLIC5, ADGRF1 |
| [[B4GALT5]] | B | WFDC2 activity raises B4GALT5's level | lines that do not express WFDC2 (38) vs lines expressing it (12) | 2.17× lower at baseline in the lines without WFDC2 | 0.001 | ⚠ within organs, on part of the lines; also absent: STEAP4, CLIC5, ADGRF1 |
| [[BMF]] | B | WFDC2 activity raises BMF's level | lines that do not express WFDC2 (38) vs lines expressing it (12) | 2.04× lower at baseline in the lines without WFDC2 | 0.002 | ⚠ within organs, on part of the lines; also absent: STEAP4, CLIC5, ADGRF1 |
| [[NPEPPS]] | B | WFDC2 activity raises NPEPPS's level | lines that do not express WFDC2 (38) vs lines expressing it (12) | 1.71× lower at baseline in the lines without WFDC2 | 0.002 | ⚠ within organs, on part of the lines; also absent: STEAP4, CLIC5, ADGRF1 |
| [[LGALS9]] | B | WFDC2 activity raises LGALS9's level | lines that do not express WFDC2 (38) vs lines expressing it (12) | 3.66× lower at baseline in the lines without WFDC2 | 0.003 | ⚠ within organs, on part of the lines; also absent: STEAP4, CLIC5, ADGRF1 |
| [[FAM83E]] | B | WFDC2 activity raises FAM83E's level | lines that do not express WFDC2 (38) vs lines expressing it (12) | 3.73× lower at baseline in the lines without WFDC2 | 0.003 | ⚠ within organs, on part of the lines; also absent: STEAP4, CLIC5, ADGRF1 |
| [[VAMP8]] | B | WFDC2 activity raises VAMP8's level | lines that do not express WFDC2 (38) vs lines expressing it (12) | 3.07× lower at baseline in the lines without WFDC2 | 0.006 | ⚠ within organs, on part of the lines; also absent: STEAP4, CLIC5, ADGRF1 |
| [[FCGRT]] | B | WFDC2 activity raises FCGRT's level | lines that do not express WFDC2 (38) vs lines expressing it (12) | 2.95× lower at baseline in the lines without WFDC2 | 0.007 | ⚠ within organs, on part of the lines; also absent: STEAP4, CLIC5, ADGRF1 |
| [[PRRG4]] | B | WFDC2 activity raises PRRG4's level | lines that do not express WFDC2 (38) vs lines expressing it (12) | 3.23× lower at baseline in the lines without WFDC2 | 0.008 | ⚠ within organs, on part of the lines; also absent: STEAP4, CLIC5, ADGRF1 |
| [[CFB]] | B | WFDC2 activity raises CFB's level | lines that do not express WFDC2 (38) vs lines expressing it (12) | 3.03× lower at baseline in the lines without WFDC2 | 0.009 | ⚠ within organs, on part of the lines; also absent: STEAP4, CLIC5, ADGRF1 |
| [[B4GALT5]] | B | WFDC2 activity strengthens B4GALT5's drug response | lines that do not express WFDC2 (38) vs lines expressing it (11) | the lines without WFDC2 respond 0.87× as strongly (z diff +0.84); strongest at Panobinostat 5 µM: 0.66x vs 0.37x (z diff +4.5) | 0.012 | ⚠ within organs, on part of the lines; also absent: STEAP4, CLIC5, ADGRF1; target measured in part of the lines; both ways; artifact flags |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.585). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (31.4, 54.9); signed map (61.3, -2.2). **Vector** length 40.1, 18.0% of its response variance represented; |z| ≥ 3 in 194 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +7.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +3.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.1 | +2.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.7 | +8.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.5 | +9.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +0.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.1 | +4.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.1 | +2.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.1 | +1.4 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -1.4 | +0.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -1.7 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.2 | -1.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.2 | -2.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.1 | -0.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.0 | -1.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.0 | -1.5 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.0 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | WAP four-disulfide core domain 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.12 — chr20:45,469,753-45,481,532 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HE4, WAP5, dJ461P17.6, EDDM4 |
| Gene groups (HGNC) | WAP four-disulfide core domain containing |
| Reactome | 2 pathways, smallest: Formation of the nephric duct; Kidney development |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14508](https://www.uniprot.org/uniprotkb/Q14508) (WAP four-disulfide core domain protein 2):

> Plays a critical role in lung development (By similarity). Required for terminal differentiation of bronchiole club cells (By similarity). Required for development of airway barrier mechanisms, such as lamellar body formation in type II alveolar epithelial cells and cilia formation on ciliated epithelial cells following initiation of respiration at birth (By similarity). Required for type I alveolar epithelial cell and vascular endothelial development in the lungs, thereby mediating blood-air …

**Summary**, from NCBI Gene [10406](https://www.ncbi.nlm.nih.gov/gene/10406):

> This gene encodes a protein that is a member of the WFDC domain family. The WFDC domain, or WAP Signature motif, contains eight cysteines forming four disulfide bonds at the core of the protein, and functions as a protease inhibitor in many family members. This gene is expressed in pulmonary epithelial cells, and was also found to be expressed in some ovarian cancers. The encoded protein is a small secretory protein, which may be involved in sperm maturation. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:15939](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15939) · Entrez [10406](https://www.ncbi.nlm.nih.gov/gene/10406) · UniProt [Q14508](https://www.uniprot.org/uniprotkb/Q14508) · Ensembl [ENSG00000101443](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101443)

## Data

Gene col 2138: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2138); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2138, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2138]; `tensor/DDL_lfc|DDL_z.npy` [2138]; `embed/gene_vectors.npy` [2138]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2138 or target_col == 2138). Every well: [[WFDC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WFDC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
