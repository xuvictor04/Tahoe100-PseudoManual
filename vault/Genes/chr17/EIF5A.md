---
symbol: "EIF5A"
type: "gene"
col: 5331
ensembl_id: "ENSG00000132507"
name: "eukaryotic translation initiation factor 5A"
location: "17p13.1"
module: 20
arm: "+"
pooled_cpm: 124.27
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 2
n_dd_up_clean: 3
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# EIF5A

*eukaryotic translation initiation factor 5A* — 17p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 7.12× (z +18.1, q 0e+00, up in 49 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.00× (z +6.4, q 2e-08, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.747× (z -3.9, q 0.064, down in 29 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (RKO 0.235×, NCI-H23 0.283×, A-427 0.337×, SW480 0.362×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VMA21]] (+0.71, fdr 7e-06), [[SIGMAR1]] (+0.67, fdr 1e-05), [[RANBP1]] (+0.65, fdr 7e-06); moves opposite to [[RBMX2]] (-0.71, fdr 7e-06), [[SNHG32]] (-0.71, fdr 7e-06), [[MPHOSPH8]] (-0.70, fdr 7e-06).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 14 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5331.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **7.12×** | +18.1 | 0e+00 | 49/49 (A549, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **6.08×** | +16.0 | 0e+00 | 44/44 (KATO III, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **4.16×** | +12.1 | 1e-31 | 45/45 (HOP62, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **2.40×** | +8.0 | 1e-13 | 47/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **2.18×** | +7.2 | 9e-11 | 46/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.00×** | +6.4 | 2e-08 | 43/48 (C32, SW480, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.87×** | +5.5 | 3e-06 | 41/47 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~54% of this change | **1.81×** | +5.2 | 1e-05 | 42/47 (C32, A549, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~64% of this change | **1.77×** | +5.2 | 1e-05 | 42/48 (SW 900, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.64×** | +4.7 | 2e-04 | 31/38 (NCI-H2347, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.61×** | +4.4 | 6e-04 | 42/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.59×** | +4.3 | 1e-03 | 38/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +3.8 | 0.006 | 34/48 (HOP62, A-172, …) | top dose only | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.47×** | +3.4 | 0.025 | 25/50 (MIA PaCa-2, SNU-423, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.45×** | +3.4 | 0.025 | 27/48 (SW 900, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **1.65×** | +3.3 | 0.039 | 30/48 (HCT15, MIA PaCa-2, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5331.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (RKO 0.235×, NCI-H23 0.283×, A-427 0.337×, SW480 0.362×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.747×** | -3.9 | 0.064 | 29/48 (RKO, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Bimiralisib (drug)]] 5 µM |  | **0.476×** | -3.6 | 0.088 | 38/50 (HEC-1-A, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | 0.499× | -3.4 | 0.14 | 34/49 (J82, SHP-77, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.05 µM |  | 0.706× | -3.1 | 0.24 | 31/49 (SW480, NCI-H23, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.45 per unit of S-phase module lfc, +0.61 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5331. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 114 | 7 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.3× (z +18.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SW480 (line)]] | alt | 164 | 6 (6 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 11.2× (z +16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -10.0) |
| [[SNU-423 (line)]] | alt | 77.3 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.2× (z +15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[C32 (line)]] | wt | 62.7 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.7× (z +16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.84× (z +8.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 113 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.0× (z +16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H1573 (line)]] | alt | 59.5 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.7× (z +15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[PANC-1 (line)]] | alt | 136 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.42× (z +15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[A-427 (line)]] | wt | 168 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.94× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -11.3) |
| [[A549 (line)]] | wt | 138 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 13.0× (z +18.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[HOP62 (line)]] | alt | 72.5 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 14.3× (z +17.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H23 (line)]] | alt | 203 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 7.03× (z +14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -13.4) |
| [[NCI-H2347 (line)]] | alt | 102 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.01× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SW 900 (line)]] | alt | 157 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.52× (z +16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[A-172 (line)]] | wt | 131 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.89× (z +15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[A498 (line)]] | wt | 298 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.02× (z +14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[CFPAC-1 (line)]] | alt | 63.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.92× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[Hs 766T (line)]] | wt | 97.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.22× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[HS-578T (line)]] | alt | 173 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.87× (z +15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[HT-29 (line)]] | alt | 82.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.84× (z +16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 109 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.26× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[J82 (line)]] | alt | 184 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.13× (z +13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[KATO III (line)]] | alt | 135 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.01× (z +16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[LoVo (line)]] | wt | 108 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.12× (z +16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[LOX-IMVI (line)]] | wt | 113 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.34× (z +15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[LS 180 (line)]] | wt | 118 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.1× (z +14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H1792 (line)]] | alt | 50.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 13.3× (z +14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H2030 (line)]] | alt | 175 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.67× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[Panc 03.27 (line)]] | alt | 64.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.0× (z +16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[RPMI-7951 (line)]] | alt | 129 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.56× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 70.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.57× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SW1417 (line)]] | alt | 93.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.77× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[AN3 CA (line)]] | alt | 124 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.11× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[AsPC-1 (line)]] | alt | 86.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.44× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[C-33 A (line)]] | alt | 122 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.21× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[CHP-212 (line)]] | wt | 110 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.60× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[H4 (line)]] | wt | 114 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.97× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[HCT15 (line)]] | alt | 107 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.88× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[HEC-1-A (line)]] | alt | 112 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.06× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[HepG2_C3A (line)]] | wt | 65.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.24× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[RKO (line)]] | wt | 185 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.62× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -15.3) |
| [[SNU-1 (line)]] | wt | 81.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.26× (z +14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SW48 (line)]] | wt | 127 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.43× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[COLO 205 (line)]] | alt | 61.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.43× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SHP-77 (line)]] | alt | 148 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.16× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[BT-474 (line)]] | alt | 84.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 76.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 189 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 87.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5331), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*35 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VMA21]] | +0.71 | +0.77 / +0.60 | both halves | 7e-06 |  |
| [[SIGMAR1]] | +0.67 | +0.72 / +0.50 | both halves | 1e-05 | STRING 403 |
| [[RANBP1]] | +0.65 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[CFL1]] | +0.64 | +0.61 / +0.65 | both halves | 7e-06 | STRING 522 |
| [[PSME3]] | +0.63 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[HNRNPAB]] | +0.62 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[PRKDC]] | +0.62 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[TUBA1B]] | +0.62 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[SNRPB]] | +0.61 | +0.69 / +0.51 | both halves | 1e-05 |  |
| [[NME1]] | +0.60 | +0.70 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_ALLOGRAFT_REJECTION; STRING 568 |
| [[WDR77]] | +0.60 | +0.70 / +0.43 | both halves | 4e-05 |  |
| [[CHID1]] | +0.59 | +0.70 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*65 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBMX2]] | -0.71 | -0.68 / -0.63 | both halves | 7e-06 |  |
| [[SNHG32]] | -0.71 | -0.70 / -0.61 | both halves | 7e-06 |  |
| [[MPHOSPH8]] | -0.70 | -0.68 / -0.67 | both halves | 7e-06 |  |
| [[NFKBIL1]] | -0.69 | -0.65 / -0.58 | both halves | 7e-06 |  |
| [[UBE2B]] | -0.69 | -0.74 / -0.61 | both halves | 7e-06 |  |
| [[LINC00888-1]] | -0.68 | -0.69 / -0.61 | both halves | 7e-06 |  |
| [[EPB41L4A-AS1]] | -0.67 | -0.68 / -0.59 | both halves | 7e-06 |  |
| [[NKAP]] | -0.66 | -0.62 / -0.58 | both halves | 8e-06 |  |
| [[MTIF3]] | -0.65 | -0.63 / -0.57 | both halves | 1e-05 |  |
| [[CCDC174]] | -0.64 | -0.62 / -0.55 | both halves | 1e-05 |  |
| [[ZMYM5]] | -0.63 | -0.64 / -0.56 | both halves | 1e-05 |  |
| [[SUGP1]] | -0.63 | -0.64 / -0.57 | both halves | 9e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.610). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-34.7, -29.2); signed map (-28.4, -41.9). **Vector** length 78.4, 31.9% of its response variance represented; |z| ≥ 3 in 1,113 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.3 | +3.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~72% of this change | +4.0 | +4.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | +3.3 | +7.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | +2.9 | +4.4 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +2.9 | +2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +6.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.3 | +0.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.1 | +0.3 |
|  | [[Demeclocycline (drug)]] 5 µM |  | +2.1 | -0.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -4.8 | -3.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | +1.2 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -1.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.3 | +0.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | -2.2 | +18.1 |
|  | [[Adagrasib (drug)]] 5 µM |  | -1.9 | -0.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.8 | -0.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.8 | +0.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -1.7 | +0.8 |
|  | [[Temsirolimus (drug)]] 5 µM |  | -1.7 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation initiation factor 5A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.1 — chr17:7,306,999-7,312,463 (+) |
| Ensembl biotype | protein_coding |
| Also known as | eIF-4D, EIF5A1, EIF-5A, MGC99547, MGC104255 |
| Hallmark sets | ALLOGRAFT_REJECTION |
| Reactome | 2 pathways, smallest: Hypusine synthesis from eIF5A-lysine; Gamma carboxylation, hypusinylation, hydroxylation, and arylsulfatase activation |
| Matched by | ensembl_id |

**Function**, from UniProt [P63241](https://www.uniprot.org/uniprotkb/P63241) (Eukaryotic translation initiation factor 5A-1):

> Translation factor that promotes translation elongation and termination, particularly upon ribosome stalling at specific amino acid sequence contexts. Binds between the exit (E) and peptidyl (P) site of the ribosome and promotes rescue of stalled ribosome: specifically required for efficient translation of polyproline-containing peptides as well as other motifs that stall the ribosome (By similarity). Acts as a ribosome quality control (RQC) cofactor by joining the RQC complex to facilitate …

**Summary**, from NCBI Gene [1984](https://www.ncbi.nlm.nih.gov/gene/1984):

> Enables U6 snRNA binding activity. Involved in several processes, including cellular response to virus; positive regulation of intrinsic apoptotic signaling pathway by p53 class mediator; and tumor necrosis factor-mediated signaling pathway. Located in annulate lamellae; cytosol; and nucleoplasm. Part of nuclear pore. Biomarker of colorectal cancer. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:3300](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3300) · Entrez [1984](https://www.ncbi.nlm.nih.gov/gene/1984) · UniProt [P63241](https://www.uniprot.org/uniprotkb/P63241) · Ensembl [ENSG00000132507](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132507)

## Data

Gene col 5331: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5331); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5331, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5331]; `tensor/DDL_lfc|DDL_z.npy` [5331]; `embed/gene_vectors.npy` [5331]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5331 or target_col == 5331). Every well: [[EIF5A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EIF5A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
