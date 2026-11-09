---
symbol: "PRKAR2A"
type: "gene"
col: 3537
ensembl_id: "ENSG00000114302"
name: "protein kinase cAMP-dependent type II regulatory subunit alpha"
location: "3p21.31"
module: 41
arm: "+"
pooled_cpm: 76.81
n_lines_expressing: 49
n_dd_up: 14
n_dd_down: 1
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# PRKAR2A

*protein kinase cAMP-dependent type II regulatory subunit alpha* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.67× (z +13.4, q 3e-38, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.852× (z -5.9, q 2e-06, down in 22 of 47 measured lines) ⚠ cell-cycle shift, explains ~46% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (SK-MEL-2 0.349×, J82 0.389×, A-172 0.435×, HOP62 0.508×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (C-33 A 0.217×, RKO 0.318×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (J82 0.348×, A-172 0.473×; ⚠ cell-cycle shift, would explain all of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (HOP62 0.623×); [[Auranofin (drug)]] 0.05 µM in 1 line (SW 1088 0.0792×); [[Cytarabine (drug)]] 0.05 µM in 1 line (SW 1088 0.0696×).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STX2]] (+0.60, fdr 2e-05), [[ARHGEF10]] (+0.56, fdr 4e-05), [[EVI5L]] (+0.56, fdr 5e-05); moves opposite to [[DLGAP1-AS2]] (-0.56, fdr 5e-05), [[HCP5]] (-0.56, fdr 1e-04), [[WAKMAR2]] (-0.54, fdr 5e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SNTA1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3537.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.67×** | +13.4 | 3e-38 | 41/47 (NCI-H2347, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.69×** | +13.2 | 2e-37 | 36/43 (SW480, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.92×** | +12.6 | 4e-34 | 39/48 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.61×** | +12.6 | 4e-34 | 38/47 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.60×** | +12.3 | 1e-32 | 38/47 (PANC-1, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.42×** | +9.1 | 7e-18 | 35/47 (SNU-423, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.39×** | +8.6 | 7e-16 | 34/47 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.28×** | +6.4 | 1e-08 | 24/47 (SW480, PANC-1, …) | rises with dose | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.58×** | +6.3 | 2e-08 | 30/48 (SK-MEL-2, HOP62, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **1.27×** | +6.1 | 5e-08 | 23/46 (HS-578T, NCI-H23, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.28×** | +6.0 | 1e-07 | 25/44 (SNU-423, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.21×** | +5.1 | 1e-05 | 24/47 (SW480, KATO III, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.21×** | +5.1 | 1e-05 | 23/47 (NCI-H460, C-33 A, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | 1.15× | +3.6 | 0.011 | 17/47 (SW480, PANC-1, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.14× | +3.5 | 0.017 | 6/48 (Panc 03.27, NCI-H2347, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.24×** | +3.0 | 0.098 | 8/47 (CFPAC-1, Panc 03.27, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3537.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (SK-MEL-2 0.349×, J82 0.389×, A-172 0.435×, HOP62 0.508×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (C-33 A 0.217×, RKO 0.318×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (J82 0.348×, A-172 0.473×; ⚠ cell-cycle shift, would explain all of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (HOP62 0.623×); [[Auranofin (drug)]] 0.05 µM in 1 line (SW 1088 0.0792×); [[Cytarabine (drug)]] 0.05 µM in 1 line (SW 1088 0.0696×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | 0.852× | -5.9 | 2e-06 | 22/47 (AsPC-1, SW 900, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.831×** | -4.8 | 4e-04 | 20/47 (SW 900, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.882× | -4.6 | 8e-04 | 20/47 (HOP62, SNU-1, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | 0.867× | -3.7 | 0.027 | 11/48 (AsPC-1, HS-578T, …) | all doses, stronger at high dose |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~2% of this change | 0.884× | -3.1 | 0.22 | 11/47 (HepG2/C3A, NCI-H2030, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3537. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 87.4 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.84× (z +14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 1.87× (z +8.9) | — |
| [[SNU-423 (line)]] | alt | 66.9 | 5 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.90× (z +14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.25× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.555× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 88.4 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.44× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 1.99× (z +9.6) | — |
| [[SW480 (line)]] | alt | 113 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.59× (z +15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[HOP62 (line)]] | alt | 80.5 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.508× (z -12.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.623× (z -8.9) |
| [[A-172 (line)]] | wt | 93.3 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.435× (z -15.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 93.3 | 1 | 2 (2 ⚠) | [[Belinostat (drug)]] 5 µM 1.96× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -18.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 110 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.02× (z +9.8) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 75.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.94× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.494× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 110 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.529× (z -12.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 118 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -18.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 69.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.85× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H460 (line)]] | wt | 60.5 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.61× (z +9.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 1.87× (z +9.2) | — |
| [[Panc 03.27 (line)]] | alt | 71.2 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.86× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.09× (z +9.4) | — |
| [[SW 1088 (line)]] | alt | 86.2 | 0 | 2 | — | [[Auranofin (drug)]] 0.05 µM 0.0792× (z -8.8) |
| [[A498 (line)]] | wt | 44.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.578× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 60.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.40× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[C-33 A (line)]] | alt | 116 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.217× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[C32 (line)]] | wt | 103 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -9.0) ⚠ cell-cycle shift, explains ~43% of this change |
| [[HCT15 (line)]] | alt | 57.2 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.200× (z -8.8) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 75.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.60× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[KATO III (line)]] | alt | 79.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.15× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[LOX-IMVI (line)]] | wt | 88.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.566× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 85.6 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.12× (z +8.7) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[NCI-H1573 (line)]] | alt | 33.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.69× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H1792 (line)]] | alt | 79.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.70× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H2030 (line)]] | alt | 95.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.19× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H23 (line)]] | alt | 79.2 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.87× (z +10.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[RKO (line)]] | wt | 108 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.318× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[RPMI-7951 (line)]] | alt | 77.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.98× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[AN3 CA (line)]] | alt | 73.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 76.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 39.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.1 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 72.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 60.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 75.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 69.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 64.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 73.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 66.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 99.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 86.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 71.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 80.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3537), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*46 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STX2]] | +0.60 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[ARHGEF10]] | +0.56 | +0.49 / +0.42 | both halves | 4e-05 |  |
| [[EVI5L]] | +0.56 | +0.40 / +0.52 | both halves | 5e-05 |  |
| [[PSMD9]] | +0.55 | +0.47 / +0.37 | both halves | 8e-05 |  |
| [[CAPN7]] | +0.54 | +0.41 / +0.48 | both halves | 4e-05 |  |
| [[NAA35]] | +0.54 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[APPL1]] | +0.54 | +0.41 / +0.46 | both halves | 4e-05 |  |
| [[ATRN]] | +0.54 | +0.43 / +0.44 | both halves | 3e-05 |  |
| [[NKTR]] | +0.54 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[SEC63]] | +0.54 | +0.39 / +0.54 | both halves | 6e-05 |  |
| [[PCMT1]] | +0.53 | +0.43 / +0.36 | both halves | 1e-04 |  |
| [[SLC25A16]] | +0.53 | +0.41 / +0.58 | both halves | 4e-05 |  |

## Genes that move opposite

*54 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DLGAP1-AS2]] | -0.56 | -0.52 / -0.39 | both halves | 5e-05 |  |
| [[HCP5]] | -0.56 | -0.34 / -0.49 | both halves | 1e-04 |  |
| [[WAKMAR2]] | -0.54 | -0.39 / -0.39 | both halves | 5e-05 |  |
| [[LINC02605]] | -0.54 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[LINC00944]] | -0.53 | -0.29 / -0.42 | both halves | 3e-04 |  |
| [[RALY-AS1]] | -0.51 | -0.43 / -0.30 | both halves | 2e-04 |  |
| [[PCED1A]] | -0.51 | -0.39 / -0.41 | both halves | 6e-05 |  |
| [[CABYR]] | -0.50 | -0.32 / -0.30 | both halves | 2e-04 | STRING 731 |
| [[ZNF341-AS1]] | -0.50 | -0.31 / -0.33 | both halves | 2e-04 |  |
| [[CFAP54]] | -0.50 | -0.43 / -0.30 | both halves | 2e-04 |  |
| [[LINC01088]] | -0.50 | -0.49 / -0.26 | both halves | 4e-04 |  |
| [[POLR2M]] | -0.50 | -0.42 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SNTA1]] | B | SNTA1 activity raises PRKAR2A's level | lines that do not express SNTA1 (5) vs lines expressing it (45) | 2.15× lower at baseline in the lines without SNTA1 | 0.057 | ⚠ within organs, on part of the lines; also absent: SACS, CLTCL1, MXRA7; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.142). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (12.1, 8.9); signed map (-41.0, 8.8). **Vector** length 112, 29.4% of its response variance represented; |z| ≥ 3 in 965 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +5.8 | +9.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.1 | +13.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.8 | +6.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.5 | +8.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.5 | +12.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.3 | +3.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.1 | +0.0 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +2.0 | +2.4 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +1.8 | +1.9 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -8.3 | -5.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.9 | -1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -7.4 | -4.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.2 | -1.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.5 | -1.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | -0.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.5 | -1.1 |
|  | [[Docetaxel (drug)]] 5 µM |  | -2.4 | -2.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.3 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | protein kinase cAMP-dependent type II regulatory subunit alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:48,744,597-48,847,874 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously PRKAR2 |
| Gene groups (HGNC) | Protein kinase A subunits |
| Hallmark sets | SPERMATOGENESIS, PI3K_AKT_MTOR_SIGNALING |
| Reactome | 48 pathways, smallest: ROBO receptors bind AKAP5; CREB1 phosphorylation through the activation of Adenylate Cyclase; PKA activation in glucagon signalling |
| Matched by | ensembl_id |

**Function**, from UniProt [P13861](https://www.uniprot.org/uniprotkb/P13861) (cAMP-dependent protein kinase type II-alpha regulatory subunit):

> Regulatory subunit of the cAMP-dependent protein kinases involved in cAMP signaling in cells. Type II regulatory chains mediate membrane association by binding to anchoring proteins, including the MAP2 kinase.

**Summary**, from NCBI Gene [5576](https://www.ncbi.nlm.nih.gov/gene/5576):

> cAMP is a signaling molecule important for a variety of cellular functions. cAMP exerts its effects by activating the cAMP-dependent protein kinase, which transduces the signal through phosphorylation of different target proteins. The inactive kinase holoenzyme is a tetramer composed of two regulatory and two catalytic subunits. cAMP causes the dissociation of the inactive holoenzyme into a dimer of regulatory subunits bound to four cAMP and two free monomeric catalytic subunits. Four different …

**Accessions** — [HGNC:9391](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9391) · Entrez [5576](https://www.ncbi.nlm.nih.gov/gene/5576) · UniProt [P13861](https://www.uniprot.org/uniprotkb/P13861) · Ensembl [ENSG00000114302](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114302)

## Data

Gene col 3537: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3537); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3537, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3537]; `tensor/DDL_lfc|DDL_z.npy` [3537]; `embed/gene_vectors.npy` [3537]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3537 or target_col == 3537). Every well: [[PRKAR2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRKAR2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
