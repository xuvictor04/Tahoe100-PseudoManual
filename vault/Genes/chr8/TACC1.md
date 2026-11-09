---
symbol: "TACC1"
type: "gene"
col: 7194
ensembl_id: "ENSG00000147526"
name: "transforming acidic coiled-coil containing protein 1"
location: "8p11.22"
module: 179
arm: "-"
pooled_cpm: 77.32
n_lines_expressing: 47
n_dd_up: 21
n_dd_down: 2
n_dd_up_clean: 15
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/179"]
generated_by: "tahoemap"
---

# TACC1

*transforming acidic coiled-coil containing protein 1* — 8p11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.57× (z +24.8, q 0e+00, up in 42 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[PH-797804 (drug)]] 5 µM: 0.690× (z -5.1, q 2e-04, down in 20 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (MIA PaCa-2 0.348×, KATO III 0.400×, HT-29 0.326×; ⚠ cell-cycle shift, explains ~0% of this change); [[TAK-901 (drug)]] 0.05 µM in 2 lines (SW48 0.153×, LOX-IMVI 0.478×); [[Digitoxin (drug)]] 5 µM in 2 lines (LoVo 0.520×, NCI-H23 0.396×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (HepG2/C3A 0.291×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.220×).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GALNT10]] (+0.55, fdr 1e-05), [[WWC3]] (+0.53, fdr 2e-05), [[ABCD3]] (+0.52, fdr 5e-05); moves opposite to [[NUP54]] (-0.54, fdr 2e-05), [[LINC01118]] (-0.54, fdr 2e-05), [[PMS2P4-1]] (-0.53, fdr 5e-05).
> It sits in the **-** arm of [[Module 179]] (RHOA GTPase cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PALLD]] → it (grade B ⚠); 2 go from it, the strongest it → [[RAPH1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 13 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7194.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.57×** | +24.8 | 0e+00 | 42/45 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.53×** | +24.4 | 0e+00 | 42/45 (LOX-IMVI, SW480, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.23×** | +21.0 | 0e+00 | 41/45 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.07×** | +19.1 | 0e+00 | 39/45 (HS-578T, A498, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.66×** | +18.9 | 0e+00 | 31/45 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.04×** | +18.0 | 0e+00 | 35/39 (HS-578T, A498, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.43×** | +13.2 | 1e-37 | 38/45 (HEC-1-A, LS 180, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.71×** | +13.1 | 1e-37 | 39/45 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.70×** | +12.8 | 7e-36 | 28/42 (RPMI-7951, C-33 A, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.59×** | +12.2 | 2e-32 | 34/45 (SW480, C32, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.56×** | +11.2 | 3e-27 | 33/45 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.51×** | +10.7 | 3e-25 | 31/45 (A-172, SW480, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.13×** | +10.4 | 1e-23 | 37/46 (LOX-IMVI, HS-578T, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.36×** | +8.0 | 4e-14 | 26/45 (SW480, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.30×** | +7.0 | 1e-10 | 25/46 (HEC-1-A, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.14× | +4.8 | 6e-05 | 12/45 (SW480, PANC-1, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | 1.13× | +4.5 | 2e-04 | 11/45 (SW480, J82, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.18× | +4.2 | 7e-04 | 19/46 (NCI-H2347, Panc 03.27, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7194.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (MIA PaCa-2 0.348×, KATO III 0.400×, HT-29 0.326×; ⚠ cell-cycle shift, explains ~0% of this change); [[TAK-901 (drug)]] 0.05 µM in 2 lines (SW48 0.153×, LOX-IMVI 0.478×); [[Digitoxin (drug)]] 5 µM in 2 lines (LoVo 0.520×, NCI-H23 0.396×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (HepG2/C3A 0.291×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.220×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **0.690×** | -5.1 | 2e-04 | 20/45 (KATO III, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.700×** | -4.9 | 2e-04 | 22/46 (LoVo, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.882× | -4.8 | 4e-04 | 18/46 (MIA PaCa-2, KATO III, …) | top dose only |  |
| [[Rifaximin (drug)]] 5 µM |  | 0.851× | -4.1 | 0.005 | 14/45 (PANC-1, SW 1088, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | 0.874× | -3.6 | 0.037 | 10/46 (HS-578T, A-172, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | 0.886× | -3.1 | 0.16 | 8/46 (Hs 766T, A498, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | 0.891× | -3.1 | 0.16 | 18/45 (LOX-IMVI, A-172, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7194. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 108 | 12 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +18.2) | — |
| [[A-172 (line)]] | wt | 86.5 | 9 (1 ⚠) | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 3.70× (z +16.0) | [[Selinexor (drug)]] 5 µM 0.584× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 92.8 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +16.9) | — |
| [[RPMI-7951 (line)]] | alt | 108 | 8 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.38× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.69× (z +10.7) | — |
| [[SW480 (line)]] | alt | 123 | 8 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.17× (z +20.7) | — |
| [[hTERT-HPNE (line)]] | wt | 135 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.88× (z +18.9) | — |
| [[LOX-IMVI (line)]] | wt | 121 | 6 (1 ⚠) | 1 | [[Belinostat (drug)]] 5 µM 3.94× (z +20.4) | [[TAK-901 (drug)]] 0.05 µM 0.478× (z -10.5) |
| [[NCI-H1792 (line)]] | alt | 80.0 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +15.2) | — |
| [[KATO III (line)]] | alt | 77.1 | 4 (1 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.59× (z +12.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -13.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.182× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 66.7 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +13.3) | — |
| [[PANC-1 (line)]] | alt | 31.6 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +23.8) | — |
| [[LS 180 (line)]] | wt | 25.6 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.30× (z +12.3) | — |
| [[NCI-H1573 (line)]] | alt | 51.1 | 5 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.82× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Belinostat (drug)]] 5 µM 4.09× (z +11.5) | — |
| [[Panc 03.27 (line)]] | alt | 93.1 | 5 | 0 | [[Belinostat (drug)]] 5 µM 3.70× (z +14.8) | — |
| [[RKO (line)]] | wt | 111 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +12.5) | — |
| [[C32 (line)]] | wt | 43.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +17.1) | — |
| [[Hs 766T (line)]] | wt | 72.6 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.97× (z +10.4) | — |
| [[J82 (line)]] | alt | 162 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +14.1) | — |
| [[SK-MEL-2 (line)]] | alt | 54.4 | 4 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.49× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Belinostat (drug)]] 5 µM 3.22× (z +10.5) | — |
| [[SNU-423 (line)]] | alt | 35.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +12.4) | — |
| [[CFPAC-1 (line)]] | alt | 76.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +15.3) | — |
| [[HepG2_C3A (line)]] | wt | 57.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -11.6) |
| [[HOP62 (line)]] | alt | 170 | 3 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.12× (z +9.6) | — |
| [[A549 (line)]] | wt | 82.3 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.50× (z +10.0) | — |
| [[HCT15 (line)]] | alt | 113 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.95× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[HEC-1-A (line)]] | alt | 20.9 | 2 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 3.09× (z +11.7) | — |
| [[NCI-H2030 (line)]] | alt | 104 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.93× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Belinostat (drug)]] 5 µM 1.91× (z +8.5) | — |
| [[SW 1088 (line)]] | alt | 112 | 0 | 2 | — | [[Roxadustat (drug)]] 0.5 µM 0.0749× (z -9.9) |
| [[A-427 (line)]] | wt | 100 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -10.4) ⚠ cell-cycle shift, explains ~91% of this change |
| [[C-33 A (line)]] | alt | 63.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.22× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[H4 (line)]] | wt | 91.4 | 1 | 0 | [[Belinostat (drug)]] 5 µM 3.64× (z +9.4) | — |
| [[HT-29 (line)]] | alt | 47.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -12.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 137 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.520× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 81.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.348× (z -19.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 39.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.396× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H596 (line)]] | alt | 66.6 | 0 | 1 | — | [[Citalopram (hydrobromide) (drug)]] 0.05 µM 0.206× (z -8.5) |
| [[SW 900 (line)]] | alt | 102 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +9.6) | — |
| [[SW48 (line)]] | wt | 51.6 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.153× (z -11.1) |
| [[AN3 CA (line)]] | alt | 99.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.8 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 47.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 88.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 64.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 19.2 n.m. | — | — | — | — |
| [[NCI-H661 (line)]] | alt | 76.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 75.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 49.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.1 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7194), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*48 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GALNT10]] | +0.55 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[WWC3]] | +0.53 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[ABCD3]] | +0.52 | +0.39 / +0.57 | both halves | 5e-05 |  |
| [[ROCK2]] | +0.52 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[RBBP8]] | +0.51 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[SOAT1]] | +0.51 | +0.39 / +0.51 | both halves | 6e-05 |  |
| [[CPT1A]] | +0.51 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[DEK]] | +0.51 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[SORT1]] | +0.50 | +0.33 / +0.51 | both halves | 1e-04 |  |
| [[CHML]] | +0.50 | +0.37 / +0.44 | both halves | 7e-05 |  |
| [[ACSL4]] | +0.50 | +0.40 / +0.54 | both halves | 5e-05 |  |
| [[TJP1]] | +0.50 | +0.45 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*52 of its nearest partners move opposite, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP54]] | -0.54 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[LINC01118]] | -0.54 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[PMS2P4-1]] | -0.53 | -0.39 / -0.52 | both halves | 5e-05 |  |
| [[NGDN]] | -0.53 | -0.32 / -0.46 | both halves | 2e-04 |  |
| [[DNAJC30]] | -0.52 | -0.20 / -0.52 | both halves | 7e-04 |  |
| [[NDUFAF7]] | -0.52 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[TMEM134]] | -0.51 | -0.43 / -0.53 | both halves | 4e-05 |  |
| [[UBOX5-AS1]] | -0.50 | -0.38 / -0.42 | both halves | 7e-05 |  |
| [[KANSL1]] | -0.49 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[WDR20]] | -0.49 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[MIR4458HG]] | -0.49 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[FAM174A]] | -0.49 | -0.39 / -0.57 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PALLD]] | B | PALLD activity raises TACC1's level | lines that do not express PALLD (11) vs lines expressing it (39) | 1.46× lower at baseline in the lines without PALLD | 0.091 | ⚠ within organs, on part of the lines; also absent: DGKG, RBPMS, PAG1; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAPH1]] | C | TACC1 activity lowers RAPH1's level | lines that do not express TACC1 (3) vs lines expressing it (47) | 2.35× higher at baseline in the lines without TACC1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLEC2D, TNNI3K, COL21A1; maybe low, not absent; its own permutation p |
| [[ROCK2]] | C | TACC1 activity lowers ROCK2's level | lines that do not express TACC1 (3) vs lines expressing it (47) | 1.77× higher at baseline in the lines without TACC1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLEC2D, TNNI3K, COL21A1; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 179]] — RHOA GTPase cycle; 22 genes; this gene is in the **-** arm (projection on the module's main direction -0.546). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-49.9, 9.9); signed map (-3.5, 19.5). **Vector** length 98.5, 24.7% of its response variance represented; |z| ≥ 3 in 1,383 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +13.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.6 | +13.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.3 | +12.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.3 | +10.4 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +3.9 | +4.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.4 | +3.2 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.4 | +3.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -10.1 | -4.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -6.3 | -0.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | -4.3 | +4.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | +2.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -3.5 | -3.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.8 | -5.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.2 | -1.5 |
|  | [[Belzutifan (drug)]] 5 µM |  | -2.1 | -2.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.9 | -2.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.8 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | transforming acidic coiled-coil containing protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p11.22 — chr8:38,728,186-38,853,028 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | TACC family |
| Matched by | ensembl_id |

**Function**, from UniProt [O75410](https://www.uniprot.org/uniprotkb/O75410) (Transforming acidic coiled-coil-containing protein 1):

> Involved in transcription regulation induced by nuclear receptors, including in T3 thyroid hormone and all-trans retinoic acid pathways. Might promote the nuclear localization of the receptors. Likely involved in the processes that promote cell division prior to the formation of differentiated tissues.

**Summary**, from NCBI Gene [6867](https://www.ncbi.nlm.nih.gov/gene/6867):

> This locus may represent a breast cancer candidate gene. It is located close to FGFR1 on a region of chromosome 8 that is amplified in some breast cancers. Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jun 2017]

**Accessions** — [HGNC:11522](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11522) · Entrez [6867](https://www.ncbi.nlm.nih.gov/gene/6867) · UniProt [O75410](https://www.uniprot.org/uniprotkb/O75410) · Ensembl [ENSG00000147526](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147526)

## Data

Gene col 7194: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7194); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7194, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7194]; `tensor/DDL_lfc|DDL_z.npy` [7194]; `embed/gene_vectors.npy` [7194]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7194 or target_col == 7194). Every well: [[TACC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TACC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
