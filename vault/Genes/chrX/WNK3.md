---
symbol: "WNK3"
type: "gene"
col: 12251
ensembl_id: "ENSG00000196632"
name: "WNK lysine deficient protein kinase 3"
location: "Xp11.22"
module: 103
arm: "+"
pooled_cpm: 7.65
n_lines_expressing: 22
n_dd_up: 28
n_dd_down: 1
n_dd_up_clean: 18
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 4
tags: ["gene", "module/103"]
generated_by: "tahoemap"
---

# WNK3

*WNK lysine deficient protein kinase 3* — Xp11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.75× (z +22.0, q 0e+00, up in 11 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Anethole trithione (drug)]] 0.5 µM: 0.768× (z -4.0, q 0.029, down in 0 of 20 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 4 lines (A-172 0.0917×, C-33 A 0.195×, SNU-423 0.172×, AN3 CA 0.134×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SK-MEL-2 0.133×, AN3 CA 0.0600×, C32 0.232×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (A-172 0.115×, AN3 CA 0.116×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (AN3 CA 0.234×, SNU-423 0.327×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NEXMIF]] (+0.65, fdr 1e-05), [[LINGO2]] (+0.59, fdr 1e-05), [[SMAD9]] (+0.57, fdr 1e-05); moves opposite to [[LRRC28]] (-0.38, fdr 9e-04, ⚠ not reproduced).
> It is in [[Module 103]], a single-armed module (glycolysis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MDGA2]] → it (grade C ⚠); 4 go from it, the strongest it → [[TMEM45A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12251.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.75×** | +22.0 | 0e+00 | 11/18 (RPMI-7951, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.61×** | +14.2 | 3e-43 | 2/10 (NCI-H460, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.79×** | +9.0 | 5e-17 | 1/13 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.50×** | +8.8 | 2e-16 | 8/19 (SHP-77, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.50×** | +6.3 | 4e-08 | 1/18 (HOP62) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.32×** | +6.0 | 2e-07 | 7/19 (NCI-H2347, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +5.8 | 5e-07 | 9/16 (NCI-H460, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.44×** | +5.6 | 1e-06 | 8/18 (A-427, HOP62, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.43×** | +5.5 | 3e-06 | 6/18 (NCI-H2347, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.80×** | +4.7 | 1e-04 | 0/10 | top dose only | noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.70×** | +4.3 | 0.001 | 0/11 | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change | **1.33×** | +4.1 | 0.002 | 0/13 | all doses, stronger at high dose | composition shift |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | **1.28×** | +3.9 | 0.005 | 1/16 (NCI-H2347) | inconsistent across doses |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **1.28×** | +3.7 | 0.007 | 0/16 | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.27×** | +3.7 | 0.009 | 6/18 (SHP-77, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +3.6 | 0.009 | 3/20 (NCI-H460, NCI-H2030, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +3.6 | 0.012 | 4/20 (RPMI-7951, HOP62, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **1.28×** | +3.5 | 0.012 | 0/17 | inconsistent across doses | low cells (technical?) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.26×** | +3.5 | 0.012 | 0/16 | inconsistent across doses |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.24×** | +3.4 | 0.020 | 5/18 (SHP-77, NCI-H2347, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12251.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 4 lines (A-172 0.0917×, C-33 A 0.195×, SNU-423 0.172×, AN3 CA 0.134×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SK-MEL-2 0.133×, AN3 CA 0.0600×, C32 0.232×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (A-172 0.115×, AN3 CA 0.116×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (AN3 CA 0.234×, SNU-423 0.327×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.768×** | -4.0 | 0.029 | 0/20 | inconsistent across doses |  |
| [[Pexidartinib (hydrochloride) (drug)]] 0.05 µM |  | 0.790× | -3.3 | 0.15 | 1/18 (NCI-H2030) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.807× | -3.3 | 0.15 | 10/18 (C32, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tirabrutinib (drug)]] 0.05 µM |  | 0.794× | -3.3 | 0.15 | 1/19 (NCI-H2030) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.946× | -3.1 | 0.23 | 2/20 (H4, NCI-H661) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12251. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AN3 CA (line)]] | alt | 84.4 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0600× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.234× (z -10.6) |
| [[A-172 (line)]] | wt | 30.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0917× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change |
| [[C32 (line)]] | wt | 26.1 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.193× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change |
| [[SHP-77 (line)]] | alt | 54.8 | 1 | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 2.31× (z +10.1) | [[Niclosamide (olamine) (drug)]] 5 µM 0.176× (z -14.4) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 24.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.172× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.327× (z -10.0) |
| [[C-33 A (line)]] | alt | 46.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.195× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change |
| [[NCI-H2347 (line)]] | alt | 15.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +11.6) | — |
| [[NCI-H460 (line)]] | wt | 10.3 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.251× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 19.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.14× (z +8.5) | — |
| [[SK-MEL-2 (line)]] | alt | 39.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.133× (z -15.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.943 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.57 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 8.01 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.25 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.951 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.923 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.917 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.15 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.872 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.891 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.82 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.34 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.01 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12251), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NEXMIF]] | +0.65 | +0.65 / +0.51 | both halves | 1e-05 | **novel candidate** |
| [[LINGO2]] | +0.59 | +0.56 / +0.55 | both halves | 1e-05 | **novel candidate** |
| [[SMAD9]] | +0.57 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[FBXL7]] | +0.56 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[DPYSL4]] | +0.54 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[RNF150]] | +0.54 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[MDGA2]] | +0.51 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[TET1]] | +0.51 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[LIN28B]] | +0.50 | +0.27 / +0.57 | both halves | 3e-04 |  |
| [[ZNF844]] | +0.50 | +0.41 / +0.42 | both halves | 4e-05 |  |
| [[NRN1]] | +0.49 | +0.40 / +0.43 | both halves | 5e-05 |  |
| [[CCDC144NL-AS1]] | +0.49 | +0.48 / +0.52 | both halves | 2e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRC28]] | -0.38 | -0.25 / -0.19 | ⚠ not reproduced | 9e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MDGA2]] | C | MDGA2 activity raises WNK3's level | lines that do not express MDGA2 (32) vs lines expressing it (18) | 3.77× lower at baseline in the lines without MDGA2 | 0.047 | ⚠ within organs, on part of the lines; also absent: ZIC1, NLGN4X, TWIST1; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM45A]] | B | WNK3 activity raises TMEM45A's level | lines that do not express WNK3 (28) vs lines expressing it (22) | 3.48× lower at baseline in the lines without WNK3 | 0.068 | ⚠ within organs, on part of the lines; also absent: PCDH17, ZNF667, PTPRN; maybe low, not absent |
| [[CSRP2]] | B | WNK3 activity raises CSRP2's level | lines that do not express WNK3 (28) vs lines expressing it (22) | 2.41× lower at baseline in the lines without WNK3 | 0.088 | ⚠ within organs, on part of the lines; also absent: PCDH17, ZNF667, PTPRN; maybe low, not absent |
| [[MDGA2]] | C | WNK3 activity raises MDGA2's level | lines that do not express WNK3 (28) vs lines expressing it (22) | 6.15× lower at baseline in the lines without WNK3 | 0.072 | ⚠ within organs, on part of the lines; also absent: PCDH17, ZNF667, PTPRN; maybe low, not absent; co-absent with the target |
| [[TTTY14]] | C | WNK3 activity raises TTTY14's level | lines that do not express WNK3 (28) vs lines expressing it (22) | 1.96× lower at baseline in the lines without WNK3 | 0.085 | ⚠ within organs, on part of the lines; also absent: PCDH17, ZNF667, PTPRN; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 103]] — glycolysis; 45 genes; every member is in the + arm (projection on the module's main direction 0.549). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (49.2, 29.8); signed map (32.7, 40.4). **Vector** length 38.8, 7.60% of its response variance represented; |z| ≥ 3 in 458 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +22.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +5.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +2.3 | +2.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.3 | +9.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.1 | +8.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +3.6 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.2 | +0.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.2 | +6.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.0 | +3.4 |
| fall | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.1 | -2.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.5 | -3.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.4 | -2.9 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.1 | -1.9 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.0 | -2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.0 | -1.4 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.0 | -1.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -0.9 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | WNK lysine deficient protein kinase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.22 — chrX:54,192,823-54,358,642 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously PRKWNK3 |
| Gene groups (HGNC) | WNK lysine deficient protein kinases |
| Reactome | 3 pathways, smallest: Stimuli-sensing channels; Ion channel transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BYP7](https://www.uniprot.org/uniprotkb/Q9BYP7) (Serine/threonine-protein kinase WNK3):

> Serine/threonine-protein kinase component of the WNK3-SPAK/OSR1 kinase cascade, which plays an important role in the regulation of electrolyte homeostasis and regulatory volume increase in response to hyperosmotic stress. WNK3 mediates regulatory volume increase in response to hyperosmotic stress by acting as a molecular crowding sensor, which senses cell shrinkage and mediates formation of a membraneless compartment by undergoing liquid-liquid phase separation. The membraneless compartment …

**Summary**, from NCBI Gene [65267](https://www.ncbi.nlm.nih.gov/gene/65267):

> This gene encodes a protein belonging to the 'with no lysine' family of serine-threonine protein kinases. These family members lack the catalytic lysine in subdomain II, and instead have a conserved lysine in subdomain I. This family member functions as a positive regulator of the transcellular Ca2+ transport pathway, and it plays a role in the increase of cell survival in a caspase-3-dependent pathway. Alternative splicing results in multiple transcript variants. [provided by RefSeq, May 2010]

**Accessions** — [HGNC:14543](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14543) · Entrez [65267](https://www.ncbi.nlm.nih.gov/gene/65267) · UniProt [Q9BYP7](https://www.uniprot.org/uniprotkb/Q9BYP7) · Ensembl [ENSG00000196632](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196632)

## Data

Gene col 12251: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12251); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12251, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12251]; `tensor/DDL_lfc|DDL_z.npy` [12251]; `embed/gene_vectors.npy` [12251]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12251 or target_col == 12251). Every well: [[WNK3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WNK3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
