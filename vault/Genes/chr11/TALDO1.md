---
symbol: "TALDO1"
type: "gene"
col: 10797
ensembl_id: "ENSG00000177156"
name: "transaldolase 1"
location: "11p15.5"
module: 72
arm: "+"
pooled_cpm: 38.29
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 3
n_dd_up_clean: 7
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# TALDO1

*transaldolase 1* — 11p15.5

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.88× (z +17.7, q 0e+00, up in 42 of 43 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.23× (z +10.5, q 2e-23, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.728× (z -5.9, q 3e-06, down in 27 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (AsPC-1 0.182×, NCI-H460 0.331×, HT-29 0.432×, SNU-1 0.362×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 0.387×); [[Selinexor (drug)]] 5 µM in 1 line (A498 0.514×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[USP14]] (+0.77, fdr 7e-06), [[PSMB3]] (+0.72, fdr 7e-06), [[HERC2]] (+0.72, fdr 7e-06); moves opposite to [[POLR1H]] (-0.61, fdr 1e-05), [[HLA-A]] (-0.59, fdr 1e-05), [[UNK]] (-0.58, fdr 3e-05).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[PSMB7]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 11 with an alert ⚠. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10797.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **3.88×** | +17.7 | 0e+00 | 42/43 (A498, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.50×** | +15.7 | 0e+00 | 34/36 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.23×** | +10.5 | 2e-23 | 43/48 (LoVo, SW1417, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.51×** | +10.0 | 2e-21 | 37/40 (SNU-423, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.15×** | +10.0 | 2e-21 | 43/47 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.19×** | +9.7 | 4e-20 | 42/48 (HT-29, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.06×** | +9.4 | 3e-19 | 42/48 (HOP62, HEC-1-A, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~44% of this change | **1.58×** | +6.0 | 2e-07 | 33/45 (SW 900, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.52×** | +5.4 | 3e-06 | 37/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.49×** | +5.2 | 1e-05 | 34/48 (SW480, HCT15, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~47% of this change | **1.46×** | +4.7 | 1e-04 | 28/47 (HOP62, LoVo, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.42×** | +4.5 | 3e-04 | 28/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.26×** | +4.3 | 7e-04 | 25/48 (HT-29, SW480, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.06×** | +4.2 | 1e-03 | 24/41 (SW1417, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.34×** | +3.8 | 0.006 | 22/47 (SW480, A-172, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.52×** | +3.2 | 0.049 | 18/48 (HOP62, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.51×** | +3.1 | 0.058 | 12/47 (MIA PaCa-2, NCI-H1573, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.27×** | +3.1 | 0.058 | 17/45 (AsPC-1, COLO 205, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10797.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (AsPC-1 0.182×, NCI-H460 0.331×, HT-29 0.432×, SNU-1 0.362×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 0.387×); [[Selinexor (drug)]] 5 µM in 1 line (A498 0.514×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.728×** | -5.9 | 3e-06 | 27/47 (NCI-H460, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.734×** | -5.7 | 3e-06 | 28/47 (AsPC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.821×** | -3.6 | 0.054 | 21/48 (A498, KATO III, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 0.772× | -3.4 | 0.10 | 21/48 (NCI-H460, HT-29, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.780× | -3.2 | 0.14 | 22/48 (LS 180, SW 1088, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.846× | -3.1 | 0.20 | 20/48 (KATO III, NCI-H460, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10797. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 80.1 | 5 (1 ⚠) | 1 | [[Auranofin (drug)]] 5 µM 2.87× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.432× (z -11.3) |
| [[HOP62 (line)]] | alt | 31.9 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.91× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.86× (z +10.4) | — |
| [[SW480 (line)]] | alt | 36.8 | 5 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.01× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.85× (z +10.0) | — |
| [[A498 (line)]] | wt | 92.0 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.18× (z +15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Selinexor (drug)]] 5 µM 0.514× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 44.9 | 3 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.19× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.85× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -19.6) |
| [[C32 (line)]] | wt | 23.9 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.89× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 4.35× (z +8.7) | — |
| [[HEC-1-A (line)]] | alt | 46.3 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.01× (z +9.4) | — |
| [[NCI-H460 (line)]] | wt | 41.4 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 5.55× (z +13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -12.7) |
| [[SNU-423 (line)]] | alt | 39.0 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.82× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.66× (z +8.6) | — |
| [[A549 (line)]] | wt | 34.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.67× (z +14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[CFPAC-1 (line)]] | alt | 21.0 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.49× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.57× (z +8.7) | — |
| [[COLO 205 (line)]] | alt | 36.0 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.46× (z +9.4) | — |
| [[KATO III (line)]] | alt | 34.4 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.67× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.08× (z +9.0) | — |
| [[LoVo (line)]] | wt | 24.2 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.53× (z +11.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 4.36× (z +10.5) | — |
| [[NCI-H1792 (line)]] | alt | 23.0 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.2× (z +13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.95× (z +8.5) | — |
| [[A-172 (line)]] | wt | 46.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.24× (z +11.4) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 45.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.02× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[HS-578T (line)]] | alt | 27.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.21× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[LOX-IMVI (line)]] | wt | 22.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.56× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[PANC-1 (line)]] | alt | 43.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.57× (z +14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[SW1417 (line)]] | alt | 50.6 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.00× (z +10.5) | — |
| [[C-33 A (line)]] | alt | 25.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.16× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 23.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.17× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[J82 (line)]] | alt | 62.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.10× (z +9.3) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 52.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 35.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.34× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H1573 (line)]] | alt | 22.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.54× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H2030 (line)]] | alt | 27.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.26× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H2347 (line)]] | alt | 47.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.90× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[SNU-1 (line)]] | wt | 34.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -8.6) |
| [[A-427 (line)]] | wt | 42.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 53.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 32.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 39.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10797), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP14]] | +0.77 | +0.75 / +0.69 | both halves | 7e-06 |  |
| [[PSMB3]] | +0.72 | +0.78 / +0.64 | both halves | 7e-06 | pathway: Cellular response to chemical stress |
| [[HERC2]] | +0.72 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[GSR]] | +0.70 | +0.74 / +0.71 | both halves | 7e-06 | pathway: Cellular response to chemical stress; STRING 530 |
| [[PSMB2]] | +0.68 | +0.79 / +0.70 | both halves | 7e-06 | pathway: Cellular response to chemical stress |
| [[CCT3]] | +0.67 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[PSMD1]] | +0.67 | +0.63 / +0.70 | both halves | 7e-06 | pathway: Cellular response to chemical stress |
| [[PTGES3]] | +0.66 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[NXPE3]] | +0.66 | +0.65 / +0.45 | both halves | 3e-05 |  |
| [[USP5]] | +0.66 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[PLAA]] | +0.65 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[EXOC2]] | +0.64 | +0.64 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR1H]] | -0.61 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[HLA-A]] | -0.59 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[UNK]] | -0.58 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[NBPF19]] | -0.58 | -0.62 / -0.55 | both halves | 1e-05 |  |
| [[TNRC6C]] | -0.58 | -0.68 / -0.44 | both halves | 3e-05 |  |
| [[INTS6L]] | -0.57 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[HELQ]] | -0.56 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[ZC3H6]] | -0.56 | -0.54 / -0.38 | both halves | 6e-05 |  |
| [[LRCH3]] | -0.56 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[OFD1]] | -0.56 | -0.62 / -0.39 | both halves | 5e-05 |  |
| [[ZNF330]] | -0.56 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[ABCA5]] | -0.55 | -0.54 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB7]] | C | TALDO1's natural level weakens PSMB7's drug response | TALDO1's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.64, reverse -0.09; direction not clear | 0.046 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.662). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-20.4, -12.9); signed map (-27.6, -27.0). **Vector** length 92.2, 25.4% of its response variance represented; |z| ≥ 3 in 870 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *ABC-family protein mediated transport* (reactome, mean cos +0.50 to 12); *Ribosome Quality Control (RQC) complex extracts and degrades nascent peptide* (reactome, mean cos +0.50 to 12); *Antigen processing: Ub, ATP-independent proteasomal degradation* (reactome, mean cos +0.53 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +8.5 | +9.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +8.1 | +9.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +8.0 | +10.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.7 | +10.5 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +4.1 | +4.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.1 | +3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.3 | +1.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.6 | +0.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.6 | -5.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.1 | -5.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.0 | -3.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -1.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -0.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.0 | -3.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.9 | -0.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.7 | +0.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.6 | -2.3 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -1.5 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | transaldolase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.5 — chr11:747,415-765,012 (+) |
| Ensembl biotype | protein_coding |
| Hallmark sets | SPERMATOGENESIS, GLYCOLYSIS, ADIPOGENESIS |
| Reactome | 16 pathways, smallest: NFE2L2 regulates pentose phosphate pathway genes; Pentose phosphate pathway; Diseases of carbohydrate metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P37837](https://www.uniprot.org/uniprotkb/P37837) (Transaldolase):

> Catalyzes the rate-limiting step of the non-oxidative phase in the pentose phosphate pathway. Catalyzes the reversible conversion of sedoheptulose-7-phosphate and D-glyceraldehyde 3-phosphate into erythrose-4-phosphate and beta-D-fructose 6-phosphate. Not only acts as a pentose phosphate pathway enzyme, but also affects other metabolite pathways by altering its subcellular localization between the nucleus and the cytoplasm (By similarity).

**Summary**, from NCBI Gene [6888](https://www.ncbi.nlm.nih.gov/gene/6888):

> Transaldolase 1 is a key enzyme of the nonoxidative pentose phosphate pathway providing ribose-5-phosphate for nucleic acid synthesis and NADPH for lipid biosynthesis. This pathway can also maintain glutathione at a reduced state and thus protect sulfhydryl groups and cellular integrity from oxygen radicals. The functional gene of transaldolase 1 is located on chromosome 11 and a pseudogene is identified on chromosome 1 but there are conflicting map locations. The second and third exon of this …

**Accessions** — [HGNC:11559](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11559) · Entrez [6888](https://www.ncbi.nlm.nih.gov/gene/6888) · UniProt [P37837](https://www.uniprot.org/uniprotkb/P37837) · Ensembl [ENSG00000177156](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177156)

## Data

Gene col 10797: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10797); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10797, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10797]; `tensor/DDL_lfc|DDL_z.npy` [10797]; `embed/gene_vectors.npy` [10797]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10797 or target_col == 10797). Every well: [[TALDO1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TALDO1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
