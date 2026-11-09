---
symbol: "DUXAP9"
type: "gene"
col: 13443
ensembl_id: "ENSG00000225210"
name: "double homeobox A pseudogene 9"
location: "14q11.2"
module: 33
arm: "+"
pooled_cpm: 24.24
n_lines_expressing: 42
n_dd_up: 1
n_dd_down: 11
n_dd_up_clean: 0
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 12
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# DUXAP9

*double homeobox A pseudogene 9* — 14q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 1.42× (z +4.2, q 0.016, up in 19 of 39 measured lines) ⚠ cell-cycle shift, explains ~46% of this change.
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.520× (z -12.1, q 5e-31, down in 30 of 39 measured lines) ⚠ cell-cycle shift, explains ~43% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.664× (z -7.6, q 7e-12, down in 25 of 39 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (A549 0.271×, PANC-1 0.264×, A498 0.287×, RKO 0.338×, …; ⚠ cell-cycle shift, explains ~43% of this change); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H1573 0.0546×, SNU-1 0.109×, H4 0.0581×, CHP-212 0.0816×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (RKO 0.322×, SW48 0.340×, LOX-IMVI 0.420×); [[Vandetanib (drug)]] 0.5 µM in 1 line (AN3 CA 0.101×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DUXAP8]] (+0.88, fdr 7e-06), [[DUXAP10]] (+0.81, fdr 7e-06), [[DCAF13]] (+0.61, fdr 1e-05); moves opposite to [[FBXO48]] (-0.59, fdr 1e-05), [[PKNOX1]] (-0.53, fdr 3e-05), [[EID2]] (-0.51, fdr 3e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[DUXAP8]] → it (grade C ⚠); 12 go from it, the strongest it → [[CARNMT1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13443.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.42×** | +4.2 | 0.016 | 19/39 (NCI-H1792, SNU-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 10 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13443.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (A549 0.271×, PANC-1 0.264×, A498 0.287×, RKO 0.338×, …; ⚠ cell-cycle shift, explains ~43% of this change); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H1573 0.0546×, SNU-1 0.109×, H4 0.0581×, CHP-212 0.0816×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (RKO 0.322×, SW48 0.340×, LOX-IMVI 0.420×); [[Vandetanib (drug)]] 0.5 µM in 1 line (AN3 CA 0.101×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.520×** | -12.1 | 5e-31 | 30/39 (A549, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.486×** | -9.1 | 3e-17 | 28/40 (PANC-1, NCI-H23, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.664×** | -7.6 | 7e-12 | 25/39 (RKO, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.620×** | -6.3 | 6e-08 | 21/38 (NCI-H1573, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.665×** | -5.3 | 1e-05 | 21/39 (MIA PaCa-2, KATO III, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.673×** | -5.0 | 6e-05 | 16/29 (A549, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.693×** | -4.6 | 3e-04 | 22/37 (SW 1271, HCT15, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.737×** | -4.0 | 0.005 | 19/40 (NCI-H460, A549, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.916× | -4.0 | 0.005 | 1/40 (NCI-H661) | inconsistent across doses |  |
| [[Decitabine (drug)]] 0.05 µM |  | **0.733×** | -3.7 | 0.010 | 18/38 (SW 1271, CHP-212, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~75% of this change | **0.773×** | -3.4 | 0.041 | 13/38 (NCI-H2030, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **0.772×** | -3.1 | 0.086 | 16/33 (HepG2/C3A, HEC-1-A, …) | all doses, stronger at high dose | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13443. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 25.0 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -13.3) ⚠ cell-cycle shift, explains ~43% of this change |
| [[A549 (line)]] | wt | 40.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0854× (z -18.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[HepG2_C3A (line)]] | wt | 36.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.109× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[HS-578T (line)]] | alt | 37.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -10.1) ⚠ cell-cycle shift, explains ~43% of this change |
| [[LOX-IMVI (line)]] | wt | 74.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -10.1) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -8.8) |
| [[NCI-H1573 (line)]] | alt | 37.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0546× (z -19.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[NCI-H460 (line)]] | wt | 18.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -11.8) ⚠ cell-cycle shift, explains ~43% of this change |
| [[PANC-1 (line)]] | alt | 32.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -14.0) ⚠ cell-cycle shift, explains ~43% of this change |
| [[RKO (line)]] | wt | 66.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.322× (z -13.1) |
| [[SNU-1 (line)]] | wt | 77.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.109× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[A-427 (line)]] | wt | 16.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -10.2) ⚠ cell-cycle shift, explains ~43% of this change |
| [[AN3 CA (line)]] | alt | 30.2 | 0 | 1 | — | [[Vandetanib (drug)]] 0.5 µM 0.101× (z -8.5) |
| [[C-33 A (line)]] | alt | 31.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.147× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[CHP-212 (line)]] | wt | 54.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0816× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[H4 (line)]] | wt | 62.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0581× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[NCI-H23 (line)]] | alt | 46.5 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.198× (z -10.2) ⚠ cell-cycle shift, explains ~33% of this change |
| [[SNU-423 (line)]] | alt | 27.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -9.2) ⚠ cell-cycle shift, explains ~43% of this change |
| [[SW48 (line)]] | wt | 65.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -9.6) |
| [[A-172 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.24 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.33 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 6.52 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.18 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.59 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.63 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.36 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.38 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.32 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 67.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 60.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 19.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13443), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DUXAP8]] | +0.88 | +0.84 / +0.89 | both halves | 7e-06 | same gene group |
| [[DUXAP10]] | +0.81 | +0.85 / +0.78 | both halves | 7e-06 | same gene group |
| [[DCAF13]] | +0.61 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[EBPL]] | +0.61 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[ERI3]] | +0.60 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[SORD]] | +0.59 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[SHQ1]] | +0.59 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[TMEM182]] | +0.59 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[ALG3]] | +0.58 | +0.62 / +0.40 | both halves | 5e-05 |  |
| [[WDR36]] | +0.57 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[EARS2]] | +0.56 | +0.62 / +0.46 | both halves | 3e-05 |  |
| [[MCOLN2]] | +0.56 | +0.53 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXO48]] | -0.59 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[PKNOX1]] | -0.53 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[EID2]] | -0.51 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[ERF]] | -0.51 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[HARBI1]] | -0.50 | -0.53 / -0.46 | both halves | 2e-05 |  |
| [[SP2]] | -0.49 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[LRRC57]] | -0.49 | -0.50 / -0.39 | both halves | 5e-05 |  |
| [[EMP3]] | -0.49 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[TRIM47]] | -0.48 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[TP53INP2]] | -0.48 | -0.53 / -0.38 | both halves | 6e-05 |  |
| [[GASAL1]] | -0.48 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[ARHGEF40]] | -0.48 | -0.43 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DUXAP8]] | C | DUXAP8 activity raises DUXAP9's level | lines that do not express DUXAP8 (7) vs lines expressing it (43) | 5.67× lower at baseline in the lines without DUXAP8 | 0.002 | ⚠ within organs, on part of the lines; also absent: DUXAP10, DUXAP9, TTYH2; co-absent with the target |
| [[DUXAP10]] | C | DUXAP10 activity raises DUXAP9's level | lines that do not express DUXAP10 (7) vs lines expressing it (43) | 5.84× lower at baseline in the lines without DUXAP10 | 0.003 | ⚠ within organs, on part of the lines; also absent: DUXAP8, KLRG1, DUXAP9; co-absent with the target |
| [[EID2]] | C | EID2 activity raises DUXAP9's level | lines that do not express EID2 (3) vs lines expressing it (47) | 5.67× lower at baseline in the lines without EID2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CENPP, ITPR2-AS1, ENSG00000261341; maybe low, not absent; its own permutation p |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 10, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CARNMT1]] | B | DUXAP9 activity raises CARNMT1's level | lines that do not express DUXAP9 (8) vs lines expressing it (42) | 1.41× lower at baseline in the lines without DUXAP9 | 0.016 | ⚠ within organs, on part of the lines; also absent: DUXAP8, DUXAP10, TTYH2; maybe low, not absent |
| [[ADAT2]] | B | DUXAP9 activity raises ADAT2's level | lines that do not express DUXAP9 (8) vs lines expressing it (42) | 1.75× lower at baseline in the lines without DUXAP9 | 0.025 | ⚠ within organs, on part of the lines; also absent: DUXAP8, DUXAP10, TTYH2; maybe low, not absent |
| [[PEMT]] | B | DUXAP9 activity raises PEMT's level | lines that do not express DUXAP9 (8) vs lines expressing it (42) | 1.69× lower at baseline in the lines without DUXAP9 | 0.030 | ⚠ within organs, on part of the lines; also absent: DUXAP8, DUXAP10, TTYH2; maybe low, not absent |
| [[FBXO48]] | B | DUXAP9 activity raises FBXO48's level | lines that do not express DUXAP9 (8) vs lines expressing it (42) | 1.52× lower at baseline in the lines without DUXAP9 | 0.040 | ⚠ within organs, on part of the lines; also absent: DUXAP8, DUXAP10, TTYH2; maybe low, not absent |
| [[DFFB]] | B | DUXAP9 activity raises DFFB's level | lines that do not express DUXAP9 (8) vs lines expressing it (42) | 1.45× lower at baseline in the lines without DUXAP9 | 0.044 | ⚠ within organs, on part of the lines; also absent: DUXAP8, DUXAP10, TTYH2; maybe low, not absent |
| [[KATNB1]] | B | DUXAP9 activity raises KATNB1's level | lines that do not express DUXAP9 (8) vs lines expressing it (42) | 1.50× lower at baseline in the lines without DUXAP9 | 0.045 | ⚠ within organs, on part of the lines; also absent: DUXAP8, DUXAP10, TTYH2; maybe low, not absent |
| [[TMEM161A]] | B | DUXAP9 activity raises TMEM161A's level | lines that do not express DUXAP9 (8) vs lines expressing it (42) | 1.67× lower at baseline in the lines without DUXAP9 | 0.045 | ⚠ within organs, on part of the lines; also absent: DUXAP8, DUXAP10, TTYH2; maybe low, not absent |
| [[ERI3]] | B | DUXAP9 activity raises ERI3's level | lines that do not express DUXAP9 (8) vs lines expressing it (42) | 1.51× lower at baseline in the lines without DUXAP9 | 0.053 | ⚠ within organs, on part of the lines; also absent: DUXAP8, DUXAP10, TTYH2; maybe low, not absent |
| [[SLC19A1]] | B | DUXAP9 activity raises SLC19A1's level | lines that do not express DUXAP9 (8) vs lines expressing it (42) | 1.39× lower at baseline in the lines without DUXAP9 | 0.074 | ⚠ within organs, on part of the lines; also absent: DUXAP8, DUXAP10, TTYH2; maybe low, not absent |
| [[URB1]] | B | DUXAP9 activity raises URB1's level | lines that do not express DUXAP9 (8) vs lines expressing it (42) | 1.45× lower at baseline in the lines without DUXAP9 | 0.088 | ⚠ within organs, on part of the lines; also absent: DUXAP8, DUXAP10, TTYH2; maybe low, not absent |
| [[DUXAP8]] | C | DUXAP9 activity raises DUXAP8's level | lines that do not express DUXAP9 (8) vs lines expressing it (42) | 4.67× lower at baseline in the lines without DUXAP9 | 0.001 | ⚠ within organs, on part of the lines; also absent: DUXAP8, DUXAP10, TTYH2; maybe low, not absent; co-absent with the target |
| [[DUXAP10]] | C | DUXAP9 activity raises DUXAP10's level | lines that do not express DUXAP9 (8) vs lines expressing it (42) | 6.24× lower at baseline in the lines without DUXAP9 | 0.001 | ⚠ within organs, on part of the lines; also absent: DUXAP8, DUXAP10, TTYH2; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.544). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (1.2, -19.5); signed map (-12.6, -57.3). **Vector** length 71.9, 14.9% of its response variance represented; |z| ≥ 3 in 675 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA modification in the nucleus and cytosol* (reactome, mean cos +0.52 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~46% of this change | +3.6 | +4.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +1.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +2.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | +3.1 | -3.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | +3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.7 | +2.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.6 | +1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | +1.4 |
|  | [[Terfenadine (drug)]] 5 µM |  | +1.0 | +0.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -5.1 | -12.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -4.3 | -9.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -1.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.3 | -0.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -1.6 | -5.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.2 | -2.5 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.2 | -1.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.2 | -1.2 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.2 | +0.7 |

## What is on record

|  |  |
|---|---|
| Name | double homeobox A pseudogene 9 |
| Locus type | pseudogene |
| Location | 14q11.2 — chr14:19,104,100-19,104,713 (+) |
| Ensembl biotype | transcribed_processed_pseudogene |
| Also known as | FLJ39632, lncRNA-CTD903, LNMAT1, SAN; previously LINC01296 |
| Gene groups (HGNC) | PRD class homeoboxes and pseudogenes |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [503638](https://www.ncbi.nlm.nih.gov/gene/503638):

> Homeobox genes encode DNA-binding proteins, many of which are thought to be involved in early embryonic development. Homeobox genes encode a DNA-binding domain of 60 to 63 amino acids referred to as the homeodomain. This pseudogene is a member of the DUXA homeobox gene family. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:32188](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32188) · Entrez [503638](https://www.ncbi.nlm.nih.gov/gene/503638) · Ensembl [ENSG00000225210](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000225210)

## Data

Gene col 13443: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13443); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13443, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13443]; `tensor/DDL_lfc|DDL_z.npy` [13443]; `embed/gene_vectors.npy` [13443]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13443 or target_col == 13443). Every well: [[DUXAP9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DUXAP9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
