---
symbol: "MDH2"
type: "gene"
col: 7114
ensembl_id: "ENSG00000146701"
name: "malate dehydrogenase 2"
location: "7q11.23"
module: 29
arm: "+"
pooled_cpm: 50.77
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 1
n_dd_up_clean: 4
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# MDH2

*malate dehydrogenase 2* — 7q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.26× (z +17.0, q 0e+00, up in 47 of 47 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Abemaciclib (drug)]] 5 µM: 1.89× (z +4.4, q 7e-04, up in 30 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.677× (z -8.0, q 7e-13, down in 38 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (A-427 0.368×, BT-474 0.405×, SW 900 0.430×, NCI-H2030 0.513×, …); [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM in 1 line (CHP-212 0.0793×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP5F1B]] (+0.77, fdr 7e-06), [[PPT1]] (+0.70, fdr 7e-06), [[COLGALT1]] (+0.66, fdr 1e-05); moves opposite to [[PPIG]] (-0.69, fdr 7e-06), [[UPF3B]] (-0.64, fdr 7e-06), [[FRG1]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PODXL2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 13 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7114.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **3.26×** | +17.0 | 0e+00 | 47/47 (NCI-H1792, SK-MEL-2, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.66×** | +12.3 | 2e-32 | 36/39 (SW480, HT-29, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.28×** | +10.9 | 1e-25 | 40/43 (C32, HEC-1-A, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.71×** | +7.6 | 3e-12 | 37/48 (A-172, HOP62, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.62×** | +6.9 | 6e-10 | 37/48 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~43% of this change | **1.52×** | +6.0 | 2e-07 | 35/47 (CFPAC-1, J82, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +5.5 | 4e-06 | 35/46 (MIA PaCa-2, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.25×** | +4.5 | 5e-04 | 27/48 (NCI-H2347, A-172, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.89×** | +4.4 | 7e-04 | 30/48 (KATO III, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | **1.34×** | +4.1 | 0.002 | 25/48 (HOP62, MIA PaCa-2, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.82×** | +4.1 | 0.002 | 21/35 (NCI-H2347, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~96% of this change | **1.31×** | +3.9 | 0.005 | 29/47 (NCI-H1573, SW480, …) | rises with dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.31×** | +3.8 | 0.006 | 22/48 (MIA PaCa-2, SW480, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.31×** | +3.4 | 0.028 | 25/48 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +3.3 | 0.038 | 17/48 (A-172, HOP62, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.40×** | +3.2 | 0.050 | 19/46 (RKO, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Sonidegib (drug)]] 0.5 µM |  | **1.40×** | +3.2 | 0.050 | 16/48 (A-427, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 1.16× | +3.0 | 0.076 | 16/48 (MIA PaCa-2, RKO, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.54×** | +3.0 | 0.085 | 18/48 (MIA PaCa-2, NCI-H1573, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7114.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (A-427 0.368×, BT-474 0.405×, SW 900 0.430×, NCI-H2030 0.513×, …); [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM in 1 line (CHP-212 0.0793×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.677×** | -8.0 | 7e-13 | 38/48 (A-427, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | 0.770× | -3.1 | 0.62 | 18/48 (LoVo, C-33 A, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7114. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 56.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.29× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[SW 900 (line)]] | alt | 53.4 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.82× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -9.6) |
| [[SW480 (line)]] | alt | 60.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.54× (z +14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[A-172 (line)]] | wt | 45.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.01× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[A-427 (line)]] | wt | 57.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.62× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -13.1) |
| [[A498 (line)]] | wt | 71.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[A549 (line)]] | wt | 47.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.22× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[C32 (line)]] | wt | 53.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.59× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[CFPAC-1 (line)]] | alt | 31.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.77× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[HEC-1-A (line)]] | alt | 63.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.91× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[HOP62 (line)]] | alt | 29.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.83× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[HT-29 (line)]] | alt | 45.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.75× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[KATO III (line)]] | alt | 92.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[LoVo (line)]] | wt | 61.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.75× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | [[Homoharringtonine (drug)]] 5 µM 0.506× (z -8.7) |
| [[LOX-IMVI (line)]] | wt | 30.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.53× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[NCI-H1792 (line)]] | alt | 56.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.88× (z +13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[NCI-H2030 (line)]] | alt | 49.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.90× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | [[Homoharringtonine (drug)]] 5 µM 0.513× (z -8.7) |
| [[NCI-H2347 (line)]] | alt | 57.3 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +9.6) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[NCI-H460 (line)]] | wt | 42.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[AsPC-1 (line)]] | alt | 36.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.90× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[BT-474 (line)]] | alt | 54.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -10.3) |
| [[C-33 A (line)]] | alt | 48.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.91× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[CHP-212 (line)]] | wt | 36.0 | 0 | 1 | — | [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM 0.0793× (z -10.1) |
| [[COLO 205 (line)]] | alt | 29.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.20× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[H4 (line)]] | wt | 45.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.48× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[Hs 766T (line)]] | wt | 61.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.74× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[HS-578T (line)]] | alt | 44.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.44× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[LS 180 (line)]] | wt | 66.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.27× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[NCI-H1573 (line)]] | alt | 39.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.73× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[NCI-H23 (line)]] | alt | 43.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.81× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[Panc 03.27 (line)]] | alt | 34.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.08× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[PANC-1 (line)]] | alt | 67.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.02× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[RKO (line)]] | wt | 53.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 46.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.81× (z +13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[SNU-1 (line)]] | wt | 38.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.89× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[SNU-423 (line)]] | alt | 25.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.11× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[AN3 CA (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 67.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 57.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 101 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7114), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP5F1B]] | +0.77 | +0.75 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 921 |
| [[PPT1]] | +0.70 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[COLGALT1]] | +0.66 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[NUTF2]] | +0.66 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[SLC25A39]] | +0.65 | +0.66 / +0.57 | both halves | 9e-06 |  |
| [[BPNT2]] | +0.65 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[TMED7]] | +0.65 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[FKBP1A]] | +0.64 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[SIGMAR1]] | +0.64 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[DPAGT1]] | +0.63 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[PRDX3]] | +0.63 | +0.58 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_ADIPOGENESIS; STRING 518 |
| [[BSG]] | +0.62 | +0.61 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPIG]] | -0.69 | -0.66 / -0.61 | both halves | 7e-06 |  |
| [[UPF3B]] | -0.64 | -0.61 / -0.59 | both halves | 7e-06 |  |
| [[FRG1]] | -0.64 | -0.64 / -0.57 | both halves | 1e-05 |  |
| [[ANKRD49]] | -0.63 | -0.62 / -0.55 | both halves | 1e-05 |  |
| [[ZBTB4]] | -0.62 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[MPHOSPH8]] | -0.62 | -0.65 / -0.54 | both halves | 1e-05 |  |
| [[CDK3]] | -0.61 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[WASHC1]] | -0.61 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[CROCCP2-1]] | -0.61 | -0.58 / -0.60 | both halves | 7e-06 |  |
| [[ZMYM5]] | -0.60 | -0.67 / -0.45 | both halves | 3e-05 |  |
| [[UBXN4]] | -0.60 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[SPATC1]] | -0.60 | -0.64 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PODXL2]] | B | PODXL2 activity raises MDH2's level | lines that do not express PODXL2 (14) vs lines expressing it (36) | 1.41× lower at baseline in the lines without PODXL2 | 0.049 | ⚠ within organs, on part of the lines |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.617). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-24.2, -24.4); signed map (-26.0, -41.1). **Vector** length 82.0, 21.8% of its response variance represented; |z| ≥ 3 in 711 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.2 | +3.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +3.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +2.9 | +7.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | +2.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.6 | +4.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.1 | +1.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.1 | +3.0 |
|  | [[EX229 (drug)]] 5 µM |  | +1.9 | +2.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -6.3 | -8.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.0 | -1.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | -0.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.1 | +1.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -0.6 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -1.9 | -1.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.9 | -2.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -1.8 | +0.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.8 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | malate dehydrogenase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q11.23 — chr7:76,048,051-76,067,508 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Malate dehydrogenases |
| Hallmark sets | FATTY_ACID_METABOLISM, GLYCOLYSIS, ADIPOGENESIS, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 5 pathways, smallest: Malate-aspartate shuttle; Citric acid cycle (TCA cycle); Mitochondrial protein degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [P40926](https://www.uniprot.org/uniprotkb/P40926) (Malate dehydrogenase, mitochondrial):

> Mitochondrial malate dehydrogenase that catalyzes the reversible conversion of malate to oxaloacetate using NAD(+) as a cofactor. Plays a central role in the tricarboxylic acid (TCA) cycle contributing to cellular respiration and energy production via the mitochondrial electron transport chain. Also participates in the malate-aspartate NADH shuttle, facilitating transfer of reducing equivalents between cytosol and mitochondria to maintain redox balance (NAD(+)/NADH homeostasis) and support …

**Summary**, from NCBI Gene [4191](https://www.ncbi.nlm.nih.gov/gene/4191):

> Malate dehydrogenase catalyzes the reversible oxidation of malate to oxaloacetate, utilizing the NAD/NADH cofactor system in the citric acid cycle. The protein encoded by this gene is localized to the mitochondria and may play pivotal roles in the malate-aspartate shuttle that operates in the metabolic coordination between cytosol and mitochondria. Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Sep 2013]

**Accessions** — [HGNC:6971](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6971) · Entrez [4191](https://www.ncbi.nlm.nih.gov/gene/4191) · UniProt [P40926](https://www.uniprot.org/uniprotkb/P40926) · Ensembl [ENSG00000146701](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146701)

## Data

Gene col 7114: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7114); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7114, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7114]; `tensor/DDL_lfc|DDL_z.npy` [7114]; `embed/gene_vectors.npy` [7114]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7114 or target_col == 7114). Every well: [[MDH2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MDH2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
