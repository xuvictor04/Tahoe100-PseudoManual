---
symbol: "LAMP3"
type: "gene"
col: 1207
ensembl_id: "ENSG00000078081"
name: "lysosome associated membrane protein 3"
location: "3q27.1"
module: 32
arm: "+"
pooled_cpm: 14.43
n_lines_expressing: 32
n_dd_up: 45
n_dd_down: 22
n_dd_up_clean: 38
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 4
direction_downstream: 2
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# LAMP3

*lysosome associated membrane protein 3* — 3q27.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 45 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.24× (z +9.2, q 3e-17, up in 3 of 15 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.69× (z +8.7, q 7e-16, up in 11 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.586× (z -8.9, q 2e-16, down in 17 of 29 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[APOL6]] (+0.74, fdr 7e-06), [[TRIM25]] (+0.72, fdr 7e-06), [[IFIH1]] (+0.71, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[PRDM16]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 45 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1207.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.24×** | +9.2 | 3e-17 | 3/15 (NCI-H2030, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.69×** | +8.7 | 7e-16 | 11/26 (CFPAC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.03×** | +8.0 | 2e-13 | 13/28 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.83×** | +7.2 | 1e-10 | 6/23 (HEC-1-A, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.92×** | +7.1 | 1e-10 | 5/19 (HEC-1-A, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Artesunate (drug)]] 5 µM |  | **1.51×** | +6.9 | 4e-10 | 15/29 (SW480, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.51×** | +6.9 | 5e-10 | 10/29 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.76×** | +6.4 | 1e-08 | 16/28 (CFPAC-1, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.62×** | +5.6 | 1e-06 | 14/29 (C-33 A, SW480, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.61×** | +5.6 | 1e-06 | 12/29 (KATO III, HCT15, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.63×** | +5.6 | 1e-06 | 16/27 (CFPAC-1, Panc 03.27, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.60×** | +5.5 | 2e-06 | 15/29 (NCI-H2347, CFPAC-1, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.59×** | +5.5 | 2e-06 | 16/29 (HEC-1-A, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~20% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.56×** | +5.2 | 7e-06 | 12/29 (CFPAC-1, LoVo, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.55×** | +5.2 | 9e-06 | 12/25 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.37×** | +5.0 | 2e-05 | 12/29 (CFPAC-1, LoVo, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.53×** | +5.0 | 2e-05 | 7/29 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.52×** | +5.0 | 2e-05 | 13/28 (NCI-H2347, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.46×** | +5.0 | 2e-05 | 11/29 (CFPAC-1, LoVo, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 1 with an alert ⚠; shown: the 15 strongest. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1207.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.586×** | -8.9 | 2e-16 | 17/29 (COLO 205, CFPAC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.640×** | -7.5 | 2e-11 | 14/29 (CFPAC-1, COLO 205, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | **0.692×** | -6.2 | 1e-07 | 16/29 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.625×** | -5.6 | 4e-06 | 17/28 (PANC-1, A549, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.640×** | -5.3 | 2e-05 | 17/29 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **0.646×** | -5.1 | 3e-05 | 15/29 (BT-474, NCI-H1573, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.652×** | -5.0 | 4e-05 | 16/29 (PANC-1, HT-29, …) | two highest doses | cell-cycle shift (explains ~20% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.666×** | -4.8 | 1e-04 | 15/29 (PANC-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.674×** | -4.7 | 2e-04 | 14/27 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.657×** | -4.6 | 2e-04 | 11/26 (PANC-1, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.707×** | -4.1 | 0.002 | 12/29 (BT-474, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.722×** | -3.9 | 0.005 | 14/26 (BT-474, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[crizotinib (drug)]] 5 µM |  | **0.719×** | -3.8 | 0.007 | 10/29 (NCI-H23, CFPAC-1, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.729×** | -3.7 | 0.007 | 13/27 (COLO 205, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.730×** | -3.7 | 0.007 | 14/26 (SNU-423, NCI-H1573, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1207. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 101 | 0 | 10 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.136× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.315× (z -13.2) |
| [[PANC-1 (line)]] | alt | 13.6 | 1 | 8 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 4.43× (z +9.1) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0791× (z -16.3) |
| [[BT-474 (line)]] | alt | 24.2 | 0 | 8 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0446× (z -13.0) |
| [[CFPAC-1 (line)]] | alt | 47.9 | 2 | 5 | [[Homoharringtonine (drug)]] 5 µM 4.96× (z +14.3) | [[Tofacitinib (drug)]] 5 µM 0.188× (z -15.1) |
| [[A-427 (line)]] | wt | 54.2 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -16.8) |
| [[HT-29 (line)]] | alt | 17.2 | 0 | 6 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0811× (z -12.6) |
| [[LoVo (line)]] | wt | 35.9 | 0 | 6 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.159× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.308× (z -10.7) |
| [[NCI-H2347 (line)]] | alt | 34.0 | 3 | 3 | [[Harringtonine (drug)]] 5 µM 7.73× (z +10.5) | [[Tofacitinib (drug)]] 5 µM 0.167× (z -13.6) |
| [[A549 (line)]] | wt | 12.9 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0218× (z -14.1) |
| [[NCI-H1573 (line)]] | alt | 36.7 | 0 | 4 | — | [[Tofacitinib (drug)]] 5 µM 0.154× (z -13.6) |
| [[COLO 205 (line)]] | alt | 45.5 | 0 | 3 | — | [[Selinexor (drug)]] 5 µM 0.186× (z -11.9) |
| [[SW480 (line)]] | alt | 10.5 | 0 | 3 | — | [[Digitoxin (drug)]] 0.5 µM 0.189× (z -10.1) |
| [[Panc 03.27 (line)]] | alt | 39.9 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +9.0) | [[Tofacitinib (drug)]] 5 µM 0.201× (z -13.0) |
| [[HEC-1-A (line)]] | alt | 6.96 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 6.43× (z +8.5) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 5.62 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.17× (z +10.0) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[A-172 (line)]] | wt | 3.14 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.39 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.46 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.35 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.44 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.91 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.54 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.50 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.25 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 6.56 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.61 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.81 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.18 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.87 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1207), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APOL6]] | +0.74 | +0.60 / +0.77 | both halves | 7e-06 |  |
| [[TRIM25]] | +0.72 | +0.60 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[IFIH1]] | +0.71 | +0.64 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[BATF2]] | +0.71 | +0.62 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[PARP14]] | +0.70 | +0.61 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[IFI35]] | +0.70 | +0.58 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[RSAD2]] | +0.70 | +0.59 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 422 |
| [[ETV7]] | +0.69 | +0.60 / +0.75 | both halves | 7e-06 |  |
| [[PARP9]] | +0.69 | +0.56 / +0.70 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[TRANK1]] | +0.69 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[XAF1]] | +0.68 | +0.50 / +0.72 | both halves | 1e-05 |  |
| [[IFIT3]] | +0.68 | +0.54 / +0.70 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers LAMP3's level | compounds that target TOP2A: 4 of 5 raise it (Amsacrine, Doxorubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.8% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FBXO39]] | B | FBXO39 activity strengthens LAMP3's drug response | lines that do not express FBXO39 (12) vs lines expressing it (17) | the lines without FBXO39 respond 0.54× as strongly (z diff +0.65); rises at some drug-doses, falls at others (38% from rises): Selinexor 5 µM: 0.86x vs 0.40x (z diff +4.5); Harringtonine 5 µM: 0.86x vs 2.13x (z diff +3.5); Tofacitinib (citrate) 5 µM: 0.90x vs 0.40x (z diff +3.4) | 0.085 | ⚠ within organs, on part of the lines; also absent: XAF1, TRIM22, SLC15A3; target measured in part of the lines; both ways; rises at some drug-doses, falls at others; artifact flags |
| [[LCN2]] | C | LCN2 activity raises LAMP3's level | lines that do not express LCN2 (33) vs lines expressing it (17) | 3.47× lower at baseline in the lines without LCN2 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS8, RAB25, TMPRSS4; co-absent with the target |
| [[BTC]] | C | BTC activity raises LAMP3's level | lines that do not express BTC (20) vs lines expressing it (30) | 3.02× lower at baseline in the lines without BTC | 0.091 | ⚠ within organs, on part of the lines; also absent: CHMP4C, SLC27A2, ENSG00000288656; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRDM16]] | B | LAMP3 activity raises PRDM16's level | lines that do not express LAMP3 (18) vs lines expressing it (32) | 2.73× lower at baseline in the lines without LAMP3 | 0.033 | ⚠ within organs, on part of the lines; also absent: OCLN, ENTPD2, LSR |
| [[BTC]] | C | LAMP3 activity raises BTC's level | lines that do not express LAMP3 (18) vs lines expressing it (32) | 2.28× lower at baseline in the lines without LAMP3 | 0.051 | ⚠ within organs, on part of the lines; also absent: OCLN, ENTPD2, LSR; co-absent with the target |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.722). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.1, 55.6); signed map (64.6, 34.0). **Vector** length 100, 27.8% of its response variance represented; |z| ≥ 3 in 970 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon gamma response* (hallmark, mean cos +0.60 to 60); *interferon* (control, mean cos +0.63 to 23); *Interferon Signaling* (reactome, mean cos +0.61 to 45).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[5-Azacytidine (drug)]] 5 µM |  | +3.5 | +5.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.4 | +5.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.0 | +8.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.0 | +8.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +2.9 | +5.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.5 | +4.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.5 | +5.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.4 | +5.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.3 | +6.4 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -5.3 | -6.2 |
|  | [[Selinexor (drug)]] 5 µM |  | -5.1 | -8.9 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -4.2 | -4.7 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -3.9 | -7.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | -3.7 | -5.1 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -3.6 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | lysosome associated membrane protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q27.1 — chr3:183,122,215-183,163,839 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LAMP, TSC403, DC-LAMP, DCLAMP, CD208 |
| Gene groups (HGNC) | CD molecules; Lysosome associated membrane proteins |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, INFLAMMATORY_RESPONSE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UQV4](https://www.uniprot.org/uniprotkb/Q9UQV4) (Lysosome-associated membrane glycoprotein 3):

> Lysosomal membrane glycoprotein which plays a role in the unfolded protein response (UPR) that contributes to protein degradation and cell survival during proteasomal dysfunction. Plays a role in the process of fusion of the lysosome with the autophagosome, thereby modulating the autophagic process. Promotes hepatocellular lipogenesis through activation of the PI3K/Akt pathway. May also play a role in dendritic cell function and in adaptive immunity.; (Microbial infection) Plays a positive role …

**Summary**, from NCBI Gene [27074](https://www.ncbi.nlm.nih.gov/gene/27074):

> This gene encodes lysosome-associated membrane glycoprotein 3, a type 1 integral membrane protein that belongs to a family of lysosome associated membrane proteins which form part of the glycoconjugate coat present on the inside of the lysosomal membrane. It is predominantly expressed in mature dendritic cells and serves as a marker of dendritic cell maturation. The encoded protein localizes primarily to late endosomes/lysosomes and the MHC class II compartment, where it contributes to antigen …

**Accessions** — [HGNC:14582](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14582) · Entrez [27074](https://www.ncbi.nlm.nih.gov/gene/27074) · UniProt [Q9UQV4](https://www.uniprot.org/uniprotkb/Q9UQV4) · Ensembl [ENSG00000078081](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000078081)

## Data

Gene col 1207: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1207); `tables/drug_effects.parquet` (68 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1207, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1207]; `tensor/DDL_lfc|DDL_z.npy` [1207]; `embed/gene_vectors.npy` [1207]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1207 or target_col == 1207). Every well: [[LAMP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LAMP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
