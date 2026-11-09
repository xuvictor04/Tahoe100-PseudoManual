---
symbol: "SERTAD1"
type: "gene"
col: 12322
ensembl_id: "ENSG00000197019"
name: "SERTA domain containing 1"
location: "19q13.2"
module: 20
arm: "-"
pooled_cpm: 15.97
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 2
n_dd_up_clean: 4
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# SERTAD1

*SERTA domain containing 1* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.51× (z +19.7, q 0e+00, up in 43 of 47 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 4.59× (z +12.5, q 4e-33, up in 42 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Ponatinib (drug)]] 5 µM: 0.554× (z -4.9, q 6e-04, down in 35 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Cobimetinib (drug)]] 5 µM in 1 line (NCI-H23 0.0641×); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H2347 0.173×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Belinostat (drug)]] 0.5 µM in 1 line (SW48 0.0886×); [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM in 1 line (SNU-1 0.0853×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IER5]] (+0.71, fdr 7e-06), [[BTG1]] (+0.69, fdr 7e-06), [[KCTD11]] (+0.67, fdr 7e-06); moves opposite to [[POLR2B]] (-0.62, fdr 7e-06), [[NAA50]] (-0.62, fdr 7e-06), [[RBBP4]] (-0.60, fdr 7e-06).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[KLF5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 11 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12322.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **5.51×** | +19.7 | 0e+00 | 43/47 (AsPC-1, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.59×** | +12.5 | 4e-33 | 42/46 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **5.26×** | +12.0 | 1e-30 | 41/46 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **4.09×** | +11.5 | 2e-28 | 44/46 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **3.99×** | +11.3 | 1e-27 | 46/46 (NCI-H460, SW480, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **3.37×** | +9.9 | 3e-21 | 44/48 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.91×** | +7.7 | 1e-12 | 40/43 (HepG2/C3A, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.34×** | +6.9 | 3e-10 | 37/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.34×** | +6.9 | 3e-10 | 40/47 (NCI-H460, SW480, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.02×** | +5.7 | 5e-07 | 31/47 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.88×** | +4.3 | 9e-04 | 28/48 (NCI-H2030, SW480, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.57×** | +3.7 | 0.011 | 25/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~84% of this change | **1.56×** | +3.6 | 0.013 | 24/44 (NCI-H2030, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.49×** | +3.2 | 0.050 | 21/47 (HEC-1-A, A-427, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.47×** | +3.1 | 0.069 | 16/37 (PANC-1, A549, …) | inconsistent across doses | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12322.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Cobimetinib (drug)]] 5 µM in 1 line (NCI-H23 0.0641×); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H2347 0.173×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Belinostat (drug)]] 0.5 µM in 1 line (SW48 0.0886×); [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM in 1 line (SNU-1 0.0853×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **0.554×** | -4.9 | 6e-04 | 35/48 (HT-29, RKO, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.727×** | -3.7 | 0.067 | 24/48 (SW480, HepG2/C3A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.75 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12322. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 10.5 | 11 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.76× (z +15.6) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 15.0× (z +13.8) | — |
| [[AsPC-1 (line)]] | alt | 22.6 | 8 (6 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 12.4× (z +21.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 7.25× (z +11.8) | [[Selinexor (drug)]] 5 µM 0.366× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 16.3 | 7 (6 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 10.2× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 5.53× (z +9.4) | — |
| [[PANC-1 (line)]] | alt | 8.39 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.05× (z +18.3) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 12.9× (z +15.0) | — |
| [[KATO III (line)]] | alt | 16.1 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.98× (z +14.8) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.33× (z +9.3) | — |
| [[LoVo (line)]] | wt | 14.1 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.47× (z +15.4) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.45× (z +8.7) | — |
| [[SW1417 (line)]] | alt | 23.4 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.92× (z +15.4) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.05× (z +9.9) | — |
| [[A549 (line)]] | wt | 30.4 | 4 (2 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 10.5× (z +13.8) | — |
| [[LOX-IMVI (line)]] | wt | 14.3 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.01× (z +14.3) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 8.89× (z +10.6) | — |
| [[LS 180 (line)]] | wt | 10.1 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.76× (z +13.9) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 11.7× (z +11.1) | — |
| [[NCI-H1573 (line)]] | alt | 14.5 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.69× (z +16.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 10.4× (z +12.4) | — |
| [[NCI-H2347 (line)]] | alt | 18.5 | 3 (1 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 4.21× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.173× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 9.06 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 34.3× (z +16.1) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 13.9× (z +8.5) | — |
| [[HEC-1-A (line)]] | alt | 12.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.61× (z +12.9) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 8.99× (z +10.6) | — |
| [[HT-29 (line)]] | alt | 30.3 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.93× (z +13.8) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.58× (z +9.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 12.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.62× (z +11.8) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 9.46× (z +9.9) | — |
| [[NCI-H1792 (line)]] | alt | 15.2 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.22× (z +13.4) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 7.91× (z +9.3) | — |
| [[NCI-H2030 (line)]] | alt | 24.8 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.03× (z +13.7) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.18× (z +9.8) | — |
| [[SNU-1 (line)]] | wt | 11.6 | 2 (1 ⚠) | 1 | [[Harringtonine (drug)]] 0.5 µM 12.9× (z +9.1) | [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM 0.0853× (z -8.7) |
| [[A498 (line)]] | wt | 9.31 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.42× (z +16.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.29× (z +9.4) | — |
| [[C32 (line)]] | wt | 18.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.00× (z +11.8) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 11.9× (z +10.6) | — |
| [[HOP62 (line)]] | alt | 24.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.63× (z +12.5) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 5.52× (z +8.7) | — |
| [[SW 900 (line)]] | alt | 19.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.48× (z +12.8) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.19× (z +8.9) | — |
| [[A-427 (line)]] | wt | 18.8 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 4.69× (z +8.8) | — |
| [[CFPAC-1 (line)]] | alt | 24.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.67× (z +14.6) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[Hs 766T (line)]] | wt | 7.78 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +12.6) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[HS-578T (line)]] | alt | 16.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.46× (z +10.2) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 14.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.35× (z +10.4) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[J82 (line)]] | alt | 12.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +8.7) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H23 (line)]] | alt | 12.7 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0641× (z -11.5) |
| [[Panc 03.27 (line)]] | alt | 16.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.44× (z +11.4) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[RPMI-7951 (line)]] | alt | 17.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.01× (z +9.8) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 12.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.65× (z +11.1) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[SNU-423 (line)]] | alt | 7.73 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.50× (z +11.0) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[SW48 (line)]] | wt | 17.0 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0886× (z -9.0) |
| [[A-172 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.31 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.50 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12322), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IER5]] | +0.71 | +0.66 / +0.73 | both halves | 7e-06 | STRING 430 |
| [[BTG1]] | +0.69 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[KCTD11]] | +0.67 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[FAM43A]] | +0.67 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[C21orf91]] | +0.66 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[H3-3B]] | +0.66 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[IER2]] | +0.64 | +0.76 / +0.63 | both halves | 7e-06 |  |
| [[DUSP14]] | +0.62 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[MCL1]] | +0.62 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[ZNF335]] | +0.61 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[MAFF]] | +0.60 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[MIDN]] | +0.60 | +0.66 / +0.59 | both halves | 7e-06 | STRING 478 |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR2B]] | -0.62 | -0.62 / -0.61 | both halves | 7e-06 |  |
| [[NAA50]] | -0.62 | -0.64 / -0.66 | both halves | 7e-06 |  |
| [[RBBP4]] | -0.60 | -0.61 / -0.63 | both halves | 7e-06 |  |
| [[KDM1A]] | -0.59 | -0.63 / -0.53 | both halves | 1e-05 |  |
| [[STT3B]] | -0.59 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[PHB2]] | -0.58 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[FAR1]] | -0.58 | -0.58 / -0.57 | both halves | 1e-05 |  |
| [[NAPB]] | -0.57 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[HTT]] | -0.57 | -0.58 / -0.59 | both halves | 7e-06 |  |
| [[COPS7B]] | -0.57 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[HACD3]] | -0.56 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[RPA1]] | -0.56 | -0.58 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLF5]] | B | KLF5 activity strengthens SERTAD1's drug response | lines that do not express KLF5 (18) vs lines expressing it (30) | the lines without KLF5 respond 0.73× as strongly (z diff +1.18); strongest at Ouabain (Octahydrate) 5 µM: 2.95x vs 4.41x (z diff +1.8) | 0.068 | ⚠ within organs, on part of the lines; also absent: LAMA3, IFNLR1, NCMAP; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[PLK2]] | B | PLK2 activity strengthens SERTAD1's drug response | lines that do not express PLK2 (6) vs lines expressing it (42) | the lines without PLK2 respond 0.56× as strongly (z diff +1.91); strongest at Homoharringtonine 5 µM: 2.14x vs 5.25x (z diff +4.0) | 0.097 | ⚠ within organs, on part of the lines; co-occurs with ZFHX3, POLE; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.581). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-2.6, -22.7); signed map (4.0, 24.0). **Vector** length 103, 31.4% of its response variance represented; |z| ≥ 3 in 1,029 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +6.8 | +11.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.1 | +12.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +5.6 | +12.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.0 | +5.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.8 | +7.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +2.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.9 | +2.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.3 | +1.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.2 | +2.4 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -6.5 | +1.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -5.5 | +0.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.9 | -0.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.1 | +1.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -3.9 | +0.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.7 | +1.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.6 | -1.8 |
|  | [[EX229 (drug)]] 5 µM |  | -2.5 | -0.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.4 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | SERTA domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:40,421,589-40,425,992 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SEI1, TRIP-Br1 |
| Gene groups (HGNC) | SERTA domain containing |
| Hallmark sets | XENOBIOTIC_METABOLISM |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UHV2](https://www.uniprot.org/uniprotkb/Q9UHV2) (SERTA domain-containing protein 1):

> Acts at E2F-responsive promoters as coregulator to integrate signals provided by PHD- and/or bromodomain-containing transcription factors. Stimulates E2F1/TFDP1 transcriptional activity. Renders the activity of cyclin D1/CDK4 resistant to the inhibitory effects of CDKN2A/p16INK4A.

**Summary**, from NCBI Gene [29950](https://www.ncbi.nlm.nih.gov/gene/29950):

> Predicted to enable transcription coactivator activity. Acts upstream of or within negative regulation of cell growth. Located in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17932](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17932) · Entrez [29950](https://www.ncbi.nlm.nih.gov/gene/29950) · UniProt [Q9UHV2](https://www.uniprot.org/uniprotkb/Q9UHV2) · Ensembl [ENSG00000197019](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197019)

## Data

Gene col 12322: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12322); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12322, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12322]; `tensor/DDL_lfc|DDL_z.npy` [12322]; `embed/gene_vectors.npy` [12322]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12322 or target_col == 12322). Every well: [[SERTAD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SERTAD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
