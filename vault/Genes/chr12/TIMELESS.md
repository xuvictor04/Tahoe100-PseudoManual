---
symbol: "TIMELESS"
type: "gene"
col: 3243
ensembl_id: "ENSG00000111602"
name: "timeless circadian regulator"
location: "12q13.3"
module: 6
arm: "+"
pooled_cpm: 24.31
n_lines_expressing: 49
n_dd_up: 17
n_dd_down: 14
n_dd_up_clean: 5
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# TIMELESS

*timeless circadian regulator* — 12q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.12× (z +20.1, q 0e+00, up in 41 of 41 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 1.57× (z +5.3, q 9e-06, up in 25 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.483× (z -12.8, q 2e-34, down in 38 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYBL2]] (+0.87, fdr 7e-06), [[HELLS]] (+0.85, fdr 7e-06), [[MCM3]] (+0.84, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[E2F2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 12 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3243.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **5.12×** | +20.1 | 0e+00 | 41/41 (A-427, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **5.38×** | +20.0 | 0e+00 | 34/34 (SW480, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **3.82×** | +15.3 | 0e+00 | 37/37 (PANC-1, A498, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.59×** | +5.7 | 1e-06 | 27/46 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | **1.61×** | +5.7 | 2e-06 | 25/42 (SW480, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.57×** | +5.3 | 9e-06 | 25/46 (LoVo, PANC-1, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~45% of this change | **1.44×** | +4.4 | 9e-04 | 19/42 (SW 900, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.27×** | +4.2 | 0.002 | 18/47 (SW480, HT-29, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.25×** | +3.9 | 0.006 | 15/47 (SW480, HOP62, …) | top dose only |  |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.35×** | +3.7 | 0.011 | 19/47 (SW480, NCI-H23, …) | two highest doses |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.73×** | +3.5 | 0.022 | 16/45 (PANC-1, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.31×** | +3.3 | 0.054 | 18/47 (Hs 766T, A-172, …) | inconsistent across doses |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | **1.30×** | +3.2 | 0.061 | 10/46 (HT-29, CFPAC-1, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.29×** | +3.1 | 0.079 | 10/47 (A498, NCI-H1573, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 1.19× | +3.0 | 0.087 | 11/47 (NCI-H23, HCT15, …) | top dose only | position effect removed |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +3.0 | 0.095 | 13/46 (SW480, PANC-1, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3243.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.483×** | -12.8 | 2e-34 | 38/46 (NCI-H23, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.424×** | -10.6 | 6e-24 | 41/46 (COLO 205, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.630×** | -5.7 | 2e-06 | 28/46 (J82, RKO, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.646×** | -4.6 | 6e-04 | 23/47 (LS 180, SHP-77, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.711×** | -4.2 | 0.002 | 18/47 (J82, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.609×** | -4.2 | 0.002 | 18/47 (SW480, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.697×** | -3.8 | 0.012 | 20/47 (CFPAC-1, SW480, …) | inconsistent across doses |  |
| [[BAY1125976 (drug)]] 5 µM |  | **0.577×** | -3.6 | 0.025 | 14/47 (LS 180, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.818×** | -3.5 | 0.025 | 18/47 (HCT15, KATO III, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.764×** | -3.3 | 0.045 | 21/47 (SNU-1, A498, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.828×** | -3.3 | 0.045 | 15/47 (HCT15, A-427, …) | rises with dose |  |
| [[AZD-8055 (drug)]] 0.5 µM |  | **0.684×** | -3.2 | 0.057 | 16/47 (A-427, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 0.834× | -3.2 | 0.061 | 17/47 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.694×** | -3.1 | 0.076 | 13/47 (NCI-H2030, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.840× | -3.1 | 0.081 | 14/47 (A-427, KATO III, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.783×** | -3.0 | 0.081 | 15/46 (SHP-77, SNU-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.74 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3243. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 85.0 | 2 (2 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.47× (z +14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -18.7) |
| [[J82 (line)]] | alt | 29.2 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 5.46× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Belinostat (drug)]] 0.5 µM 0.315× (z -9.0) |
| [[LS 180 (line)]] | wt | 18.8 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 7.87× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -12.2) |
| [[MIA PaCa-2 (line)]] | alt | 14.9 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 6.67× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -11.0) |
| [[NCI-H23 (line)]] | alt | 60.6 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.34× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -22.0) |
| [[SW480 (line)]] | alt | 49.0 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.48× (z +14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -17.2) |
| [[A498 (line)]] | wt | 24.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.45× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[HEC-1-A (line)]] | alt | 29.0 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.40× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -12.5) |
| [[HOP62 (line)]] | alt | 9.80 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.85× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[HT-29 (line)]] | alt | 22.4 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.62× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -12.0) |
| [[LOX-IMVI (line)]] | wt | 16.9 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 8.28× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.194× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 21.8 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 9.09× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -9.6) |
| [[PANC-1 (line)]] | alt | 36.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[SNU-423 (line)]] | alt | 12.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.56× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[A549 (line)]] | wt | 18.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.41× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[HS-578T (line)]] | alt | 11.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.45× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[KATO III (line)]] | alt | 19.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.37× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[LoVo (line)]] | wt | 20.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.04× (z +13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H2347 (line)]] | alt | 18.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.92× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[SNU-1 (line)]] | wt | 22.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -13.8) |
| [[C32 (line)]] | wt | 13.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.98× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[COLO 205 (line)]] | alt | 20.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0231× (z -19.4) |
| [[H4 (line)]] | wt | 16.0 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.159× (z -10.0) ⚠ cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 28.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -9.5) |
| [[Hs 766T (line)]] | wt | 9.38 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 10.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.3× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[NCI-H2030 (line)]] | alt | 29.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[Panc 03.27 (line)]] | alt | 28.4 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.302× (z -8.7) |
| [[SHP-77 (line)]] | alt | 39.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -12.3) |
| [[SW1417 (line)]] | alt | 25.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[A-172 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.62 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 57.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.12 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.84 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.30 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.66 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3243), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYBL2]] | +0.87 | +0.81 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[HELLS]] | +0.85 | +0.77 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 429 |
| [[MCM3]] | +0.84 | +0.80 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 993 |
| [[RRM1]] | +0.84 | +0.80 / +0.85 | both halves | 7e-06 |  |
| [[CENPH]] | +0.83 | +0.81 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[CSE1L]] | +0.82 | +0.82 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[MCM4]] | +0.82 | +0.77 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 993 |
| [[XRCC2]] | +0.82 | +0.77 / +0.83 | both halves | 7e-06 | pathway: DNA Double-Strand Break Repair |
| [[TYMS]] | +0.82 | +0.86 / +0.78 | both halves | 7e-06 | STRING 450 |
| [[WDR76]] | +0.81 | +0.77 / +0.83 | both halves | 7e-06 |  |
| [[FANCD2]] | +0.81 | +0.77 / +0.83 | both halves | 7e-06 | STRING 746 |
| [[ZWINT]] | +0.81 | +0.76 / +0.81 | both halves | 7e-06 | STRING 400 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F2]] | B | E2F2 activity raises TIMELESS's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 2.03× lower at baseline in the lines without E2F2 | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.869). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-36.6, -43.9); signed map (-37.4, -47.0). **Vector** length 109, 31.1% of its response variance represented; |z| ≥ 3 in 1,011 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DNA strand elongation* (reactome, mean cos +0.69 to 28); *DNA Replication* (reactome, mean cos +0.67 to 40); *E2F G1/S* (control, mean cos +0.67 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +5.3 | +5.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +4.3 | +20.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | +4.2 | +20.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +3.8 | +15.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~99% of this change | +3.3 | +3.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.3 | +5.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.3 | +1.5 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +2.2 | +3.0 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.2 | +3.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.2 | +1.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.8 | -10.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.7 | -12.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.1 | -1.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | -3.1 | -4.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.9 | -5.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.8 | -3.1 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.5 | -3.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.5 | -3.3 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.4 | -0.5 |
|  | [[Belzutifan (drug)]] 5 µM |  | -2.3 | +0.6 |

## What is on record

|  |  |
|---|---|
| Name | timeless circadian regulator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.3 — chr12:56,416,363-56,449,426 (-) |
| Ensembl biotype | protein_coding |
| Also known as | hTIM, TIM, TIM1 |
| Hallmark sets | E2F_TARGETS |
| Reactome | 5 pathways, smallest: Processing of DNA double-strand break ends; HDR through Homologous Recombination (HRR) or Single Strand Annealing (SSA); Homology Directed Repair |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UNS1](https://www.uniprot.org/uniprotkb/Q9UNS1) (Protein timeless homolog):

> Plays an important role in the control of DNA replication, maintenance of replication fork stability, maintenance of genome stability throughout normal DNA replication, DNA repair and in the regulation of the circadian clock. Required to stabilize replication forks during DNA replication by forming a complex with TIPIN: this complex regulates DNA replication processes under both normal and stress conditions, stabilizes replication forks and influences both CHEK1 phosphorylation and the intra-S …

**Summary**, from NCBI Gene [8914](https://www.ncbi.nlm.nih.gov/gene/8914):

> The protein encoded by this gene is highly conserved and is involved in cell survival after damage or stress, increase in DNA polymerase epsilon activity, maintenance of telomere length, and epithelial cell morphogenesis. The encoded protein also plays a role in the circadian rhythm autoregulatory loop, interacting with the PERIOD genes (PER1, PER2, and PER3) and others to downregulate activation of PER1 by CLOCK/ARNTL. Changes in this gene or its expression may promote prostate cancer, lung …

**Accessions** — [HGNC:11813](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11813) · Entrez [8914](https://www.ncbi.nlm.nih.gov/gene/8914) · UniProt [Q9UNS1](https://www.uniprot.org/uniprotkb/Q9UNS1) · Ensembl [ENSG00000111602](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111602)

## Data

Gene col 3243: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3243); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3243, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3243]; `tensor/DDL_lfc|DDL_z.npy` [3243]; `embed/gene_vectors.npy` [3243]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3243 or target_col == 3243). Every well: [[TIMELESS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TIMELESS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
