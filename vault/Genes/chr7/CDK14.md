---
symbol: "CDK14"
type: "gene"
col: 657
ensembl_id: "ENSG00000058091"
name: "cyclin dependent kinase 14"
location: "7q21.13"
module: 151
arm: "+"
pooled_cpm: 98.92
n_lines_expressing: 39
n_dd_up: 4
n_dd_down: 10
n_dd_up_clean: 3
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 6
direction_downstream: 1
tags: ["gene", "module/151"]
generated_by: "tahoemap"
---

# CDK14

*cyclin dependent kinase 14* — 7q21.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.43× (z +8.0, q 5e-13, up in 21 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.706× (z -7.8, q 3e-12, down in 26 of 38 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 7 lines (C32 0.296×, HOP62 0.336×, NCI-H1792 0.314×, LOX-IMVI 0.363×, …); [[Homoharringtonine (drug)]] 5 µM in 5 lines (C32 0.207×, COLO 205 0.124×, LOX-IMVI 0.357×, H4 0.308×, …; ⚠ cell-cycle shift, explains ~51% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 3 lines (COLO 205 0.0936×, LOX-IMVI 0.221×, LS 180 0.170×; ⚠ toxic); [[Trametinib (drug)]] 0.5 µM in 1 line (C32 0.450×); [[Radotinib (drug)]] 5 µM in 1 line (C32 0.500×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PALM2AKAP2]] (+0.61, fdr 1e-05), [[PRKG1]] (+0.57, fdr 2e-05), [[ST3GAL6]] (+0.53, fdr 4e-05); moves opposite to [[ZNF333]] (-0.51, fdr 4e-05), [[ZNF18]] (-0.49, fdr 4e-05), [[INTS8]] (-0.49, fdr 8e-05).
> It is in [[Module 151]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[LINC02360]] → it (grade B ⚠); 1 goes from it, the strongest it → [[PRKG1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 657.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.43×** | +8.0 | 5e-13 | 21/37 (NCI-H460, CFPAC-1, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.58×** | +7.3 | 1e-10 | 22/37 (SK-MEL-2, NCI-H23, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.30×** | +4.2 | 0.004 | 18/38 (NCI-H460, Panc 03.27, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.32×** | +4.2 | 0.004 | 21/37 (HS-578T, LS 180, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | 1.20× | +4.1 | 0.006 | 19/37 (NCI-H2347, PANC-1, …) | top dose only | low cells (technical?) |
| [[BAY1125976 (drug)]] 5 µM |  | 1.46× | +3.2 | 0.14 | 18/37 (HEC-1-A, hTERT-HPNE, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 9 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 657.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 7 lines (C32 0.296×, HOP62 0.336×, NCI-H1792 0.314×, LOX-IMVI 0.363×, …); [[Homoharringtonine (drug)]] 5 µM in 5 lines (C32 0.207×, COLO 205 0.124×, LOX-IMVI 0.357×, H4 0.308×, …; ⚠ cell-cycle shift, explains ~51% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 3 lines (COLO 205 0.0936×, LOX-IMVI 0.221×, LS 180 0.170×; ⚠ toxic); [[Trametinib (drug)]] 0.5 µM in 1 line (C32 0.450×); [[Radotinib (drug)]] 5 µM in 1 line (C32 0.500×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.706×** | -7.8 | 3e-12 | 26/38 (C32, HOP62, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.636×** | -6.9 | 1e-09 | 27/36 (COLO 205, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.658×** | -6.7 | 6e-09 | 25/37 (LOX-IMVI, HOP62, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.748×** | -6.5 | 9e-09 | 21/37 (C32, COLO 205, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **0.707×** | -5.5 | 4e-06 | 27/37 (hTERT-HPNE, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.722×** | -5.2 | 2e-05 | 23/37 (COLO 205, LOX-IMVI, …) | two highest doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.731×** | -4.8 | 1e-04 | 22/39 (C32, LOX-IMVI, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.753×** | -4.3 | 0.001 | 22/37 (C32, HOP62, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.796×** | -3.6 | 0.018 | 20/37 (COLO 205, HEC-1-A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | **0.728×** | -3.3 | 0.049 | 20/37 (COLO 205, LOX-IMVI, …) | rises with dose | composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 657. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 555 | 0 | 13 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -20.4) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.296× (z -15.8) |
| [[COLO 205 (line)]] | alt | 93.3 | 0 | 10 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -20.2) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.279× (z -12.4) |
| [[LOX-IMVI (line)]] | wt | 410 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -14.4) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.363× (z -14.1) |
| [[SK-MEL-2 (line)]] | alt | 47.7 | 5 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 6.22× (z +15.0) | — |
| [[A-172 (line)]] | wt | 204 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.512× (z -10.6) |
| [[HEC-1-A (line)]] | alt | 90.9 | 1 | 3 (3 ⚠) | [[Auranofin (drug)]] 5 µM 2.14× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.500× (z -11.4) ⚠ cell-cycle shift, explains ~51% of this change |
| [[HOP62 (line)]] | alt | 200 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.336× (z -15.5) |
| [[LS 180 (line)]] | wt | 54.8 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -13.7) ⚠ cell-cycle shift, explains ~51% of this change |
| [[NCI-H460 (line)]] | wt | 31.9 | 4 (2 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 3.00× (z +14.9) | — |
| [[NCI-H1792 (line)]] | alt | 332 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.314× (z -15.0) |
| [[SHP-77 (line)]] | alt | 134 | 1 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.28× (z +8.7) ⚠ cell-cycle shift, explains ~0% of this change | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.164× (z -10.1) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 129 | 3 (3 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 3.30× (z +10.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A-427 (line)]] | wt | 25.5 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.39× (z +8.7) | [[Niclosamide (olamine) (drug)]] 5 µM 0.286× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 262 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -14.2) ⚠ cell-cycle shift, explains ~51% of this change |
| [[NCI-H1573 (line)]] | alt | 51.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.181× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 103 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.122× (z -12.1) ⚠ cell-cycle shift, explains ~24% of this change |
| [[AsPC-1 (line)]] | alt | 31.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -10.5) ⚠ cell-cycle shift, explains ~51% of this change |
| [[BT-474 (line)]] | alt | 97.9 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.139× (z -9.7) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 69.0 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.00× (z +9.1) | — |
| [[HepG2_C3A (line)]] | wt | 26.2 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.01× (z +8.5) | — |
| [[hTERT-HPNE (line)]] | wt | 237 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.362× (z -9.2) ⚠ transcription drop; cell-cycle shift, explains ~33% of this change |
| [[LoVo (line)]] | wt | 116 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.464× (z -11.4) ⚠ cell-cycle shift, explains ~51% of this change |
| [[NCI-H23 (line)]] | alt | 25.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.24× (z +10.7) | — |
| [[NCI-H2347 (line)]] | alt | 47.0 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.10× (z +9.5) ⚠ cell-cycle shift, explains ~67% of this change | — |
| [[SW 900 (line)]] | alt | 101 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -10.0) |
| [[A498 (line)]] | wt | 250 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.2 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 15.7 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 121 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.5 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 21.0 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 213 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 24.0 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 21.0 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.6 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.4 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 62.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.9 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 181 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.9 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 15.5 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 657), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PALM2AKAP2]] | +0.61 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[PRKG1]] | +0.57 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[ST3GAL6]] | +0.53 | +0.59 / +0.41 | both halves | 4e-05 |  |
| [[TUSC3]] | +0.53 | +0.46 / +0.52 | both halves | 2e-05 |  |
| [[RGS7]] | +0.52 | +0.38 / +0.53 | both halves | 6e-05 |  |
| [[LIMS1]] | +0.49 | +0.30 / +0.61 | both halves | 2e-04 |  |
| [[UBE2E2]] | +0.48 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[CD44]] | +0.48 | +0.44 / +0.48 | both halves | 3e-05 |  |
| [[COLEC12]] | +0.48 | +0.44 / +0.44 | both halves | 3e-05 |  |
| [[MPDZ]] | +0.47 | +0.33 / +0.52 | both halves | 1e-04 |  |
| [[TBX3]] | +0.47 | +0.33 / +0.46 | both halves | 1e-04 |  |
| [[LINC02930]] | +0.47 | +0.27 / +0.47 | both halves | 3e-04 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF333]] | -0.51 | -0.40 / -0.46 | both halves | 4e-05 |  |
| [[ZNF18]] | -0.49 | -0.54 / -0.40 | both halves | 4e-05 |  |
| [[INTS8]] | -0.49 | -0.37 / -0.52 | both halves | 8e-05 |  |
| [[USP20]] | -0.49 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[PGAP3]] | -0.48 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[MFSD8]] | -0.48 | -0.31 / -0.59 | both halves | 2e-04 |  |
| [[PUS10]] | -0.48 | -0.41 / -0.59 | both halves | 4e-05 |  |
| [[ELP3]] | -0.47 | -0.50 / -0.38 | both halves | 6e-05 |  |
| [[PPOX]] | -0.46 | -0.36 / -0.44 | both halves | 1e-04 |  |
| [[TUT1]] | -0.46 | -0.52 / -0.33 | both halves | 1e-04 |  |
| [[PRPSAP2]] | -0.46 | -0.37 / -0.49 | both halves | 7e-05 |  |
| [[MTIF3]] | -0.46 | -0.40 / -0.43 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02360]] | B | LINC02360 activity raises CDK14's level | lines that do not express LINC02360 (33) vs lines expressing it (17) | 3.04× lower at baseline in the lines without LINC02360 | 0.004 | ⚠ within organs, on part of the lines; also absent: MAGEB2, LINC01905, AJAP1 |
| [[CAMK4]] | B | CAMK4 activity raises CDK14's level | lines that do not express CAMK4 (21) vs lines expressing it (29) | 3.32× lower at baseline in the lines without CAMK4 | 0.017 | ⚠ within organs, on part of the lines; also absent: SNAP25, PRR16, ADAM12 |
| [[PRKG1]] | B | PRKG1 activity raises CDK14's level | lines that do not express PRKG1 (23) vs lines expressing it (27) | 2.93× lower at baseline in the lines without PRKG1 | 0.018 | ⚠ within organs, on part of the lines; also absent: NTNG1, CAMK4, DSCAM; maybe low, not absent |
| [[PLPP4]] | B | PLPP4 activity raises CDK14's level | lines that do not express PLPP4 (31) vs lines expressing it (19) | 2.59× lower at baseline in the lines without PLPP4 | 0.061 | ⚠ within organs, on part of the lines; also absent: GYPC, LINC02930, TNFAIP6 |
| [[TOP2A]] | B | TOP2A activity raises CDK14's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[SOX5]] | B | SOX5 activity raises CDK14's level | lines that do not express SOX5 (24) vs lines expressing it (26) | 2.28× lower at baseline in the lines without SOX5 | 0.069 | ⚠ within organs, on part of the lines; also absent: CTHRC1, MOXD1, AK5 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRKG1]] | B | CDK14 activity raises PRKG1's level | lines that do not express CDK14 (11) vs lines expressing it (39) | 3.58× lower at baseline in the lines without CDK14 | 0.071 | ⚠ within organs, on part of the lines; also absent: BNIP3, DYNC1I1, SPART-AS1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 151]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.517). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (29.0, 30.8); signed map (35.1, 25.8). **Vector** length 99.9, 25.5% of its response variance represented; |z| ≥ 3 in 926 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.3 | +7.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.9 | +8.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | +7.3 | +4.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +7.0 | -2.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.9 | -0.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.0 | +2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +1.4 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.4 | +2.4 |
| fall | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -2.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.3 | -2.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.9 | -2.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.8 | -1.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.7 | -0.7 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.6 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | cyclin dependent kinase 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q21.13 — chr7:90,466,424-91,210,590 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PFTAIRE1; previously PFTK1 |
| Gene groups (HGNC) | Cyclin dependent kinases |
| Matched by | ensembl_id |

**Function**, from UniProt [O94921](https://www.uniprot.org/uniprotkb/O94921) (Cyclin-dependent kinase 14):

> Serine/threonine-protein kinase involved in the control of the eukaryotic cell cycle, whose activity is controlled by an associated cyclin. Acts as a cell-cycle regulator of Wnt signaling pathway during G2/M phase by mediating the phosphorylation of LRP6 at 'Ser-1490', leading to the activation of the Wnt signaling pathway. Acts as a regulator of cell cycle progression and cell proliferation via its interaction with CCDN3. Phosphorylates RB1 in vitro, however the relevance of such result …

**Summary**, from NCBI Gene [5218](https://www.ncbi.nlm.nih.gov/gene/5218):

> Enables cyclin binding activity and cyclin-dependent protein serine/threonine kinase activity. Involved in G2/M transition of mitotic cell cycle and regulation of canonical Wnt signaling pathway. Located in cytosol; nucleoplasm; and plasma membrane. Part of cytoplasmic cyclin-dependent protein kinase holoenzyme complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:8883](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8883) · Entrez [5218](https://www.ncbi.nlm.nih.gov/gene/5218) · UniProt [O94921](https://www.uniprot.org/uniprotkb/O94921) · Ensembl [ENSG00000058091](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000058091)

## Data

Gene col 657: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 657); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 657, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 657]; `tensor/DDL_lfc|DDL_z.npy` [657]; `embed/gene_vectors.npy` [657]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 657 or target_col == 657). Every well: [[CDK14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDK14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
