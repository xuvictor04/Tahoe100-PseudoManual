---
symbol: "HCFC1"
type: "gene"
col: 10267
ensembl_id: "ENSG00000172534"
name: "host cell factor C1"
location: "Xq28"
module: 126
arm: "+"
pooled_cpm: 58.09
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 13
n_dd_up_clean: 13
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/126"]
generated_by: "tahoemap"
---

# HCFC1

*host cell factor C1* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (10 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 3.00× (z +15.0, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.297× (z -16.7, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KMT2D]] (+0.74, fdr 7e-06), [[PRDM10]] (+0.74, fdr 7e-06), [[TOR1A]] (+0.73, fdr 7e-06); moves opposite to [[RP9]] (-0.77, fdr 7e-06), [[PITPNA-AS1]] (-0.73, fdr 7e-06), [[POLR2I]] (-0.68, fdr 3e-05).
> It is in [[Module 126]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10267.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.00×** | +15.0 | 0e+00 | 47/48 (AsPC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.38×** | +11.4 | 1e-27 | 37/43 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.20×** | +10.8 | 8e-25 | 44/48 (NCI-H460, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.11×** | +10.2 | 3e-22 | 42/47 (COLO 205, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.07×** | +9.9 | 4e-21 | 45/48 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +9.3 | 1e-18 | 37/48 (NCI-H2347, KATO III, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.17×** | +8.1 | 3e-14 | 40/48 (SW480, SW1417, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.79×** | +7.4 | 1e-11 | 33/45 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.62×** | +6.6 | 3e-09 | 40/48 (PANC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.61×** | +6.4 | 6e-09 | 42/48 (NCI-H460, CFPAC-1, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.60×** | +6.4 | 1e-08 | 41/48 (SK-MEL-2, A-172, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.38×** | +6.2 | 2e-08 | 39/48 (HOP62, SW1417, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.41×** | +4.7 | 1e-04 | 33/48 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | **1.42×** | +4.6 | 2e-04 | 31/47 (SNU-423, COLO 205, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.41×** | +4.5 | 2e-04 | 30/48 (HOP62, Hs 766T, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.34×** | +3.9 | 0.003 | 26/47 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.34×** | +3.9 | 0.003 | 29/48 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.33×** | +3.7 | 0.007 | 22/48 (PANC-1, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Pentoxifylline (drug)]] 0.5 µM |  | **1.27×** | +3.3 | 0.030 | 23/48 (HT-29, RKO, …) | inconsistent across doses | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.26×** | +3.0 | 0.069 | 24/47 (KATO III, Hs 766T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, none with an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10267.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.297×** | -16.7 | 0e+00 | 48/48 (BT-474, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.304×** | -16.4 | 0e+00 | 48/48 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.331×** | -15.2 | 0e+00 | 47/48 (KATO III, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.463×** | -10.6 | 3e-24 | 45/48 (SK-MEL-2, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.630×** | -9.1 | 2e-17 | 47/48 (SW1417, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.520×** | -9.0 | 2e-17 | 40/48 (HCT15, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.529×** | -8.5 | 2e-15 | 35/48 (A-427, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.552×** | -8.2 | 2e-14 | 46/48 (SK-MEL-2, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.345×** | -7.7 | 1e-12 | 45/48 (SK-MEL-2, HT-29, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.541×** | -6.6 | 3e-09 | 36/48 (A-427, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.739×** | -5.9 | 1e-07 | 29/48 (RKO, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.654×** | -5.9 | 2e-07 | 36/48 (SK-MEL-2, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Sulfisoxazole (drug)]] 5 µM |  | **0.827×** | -3.8 | 0.007 | 24/48 (MIA PaCa-2, LoVo, …) | top dose only | position effect removed |
| [[Radotinib (drug)]] 5 µM |  | 0.857× | -3.1 | 0.085 | 19/48 (KATO III, LOX-IMVI, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10267. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 73.8 | 5 (1 ⚠) | 7 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.49× (z +13.9) | [[Panobinostat (drug)]] 0.5 µM 0.132× (z -19.0) |
| [[PANC-1 (line)]] | alt | 75.8 | 5 (1 ⚠) | 6 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.26× (z +12.4) | [[Panobinostat (drug)]] 0.5 µM 0.241× (z -15.1) |
| [[LoVo (line)]] | wt | 52.3 | 4 (1 ⚠) | 6 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.56× (z +14.5) | [[Panobinostat (drug)]] 5 µM 0.266× (z -12.8) |
| [[SW480 (line)]] | alt | 66.4 | 7 (4 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.90× (z +14.0) | [[Panobinostat (drug)]] 5 µM 0.323× (z -11.9) |
| [[KATO III (line)]] | alt | 62.8 | 5 (1 ⚠) | 4 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.40× (z +14.1) | [[Belinostat (drug)]] 5 µM 0.162× (z -17.5) |
| [[NCI-H1573 (line)]] | alt | 102 | 4 (1 ⚠) | 5 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.85× (z +13.0) | [[Panobinostat (drug)]] 5 µM 0.191× (z -16.2) |
| [[NCI-H460 (line)]] | wt | 46.7 | 6 (2 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.26× (z +13.7) | [[Belinostat (drug)]] 5 µM 0.206× (z -15.0) |
| [[SK-MEL-2 (line)]] | alt | 77.5 | 1 (1 ⚠) | 8 | [[Dinaciclib (drug)]] 5 µM 2.94× (z +9.7) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.191× (z -15.4) |
| [[HOP62 (line)]] | alt | 40.0 | 5 (2 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.90× (z +11.0) | [[Panobinostat (drug)]] 0.5 µM 0.276× (z -10.4) |
| [[LS 180 (line)]] | wt | 44.7 | 4 (1 ⚠) | 4 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.32× (z +16.2) | [[Belinostat (drug)]] 5 µM 0.296× (z -10.8) |
| [[A-427 (line)]] | wt | 74.0 | 0 | 7 | — | [[Harringtonine (drug)]] 5 µM 0.213× (z -13.0) |
| [[AsPC-1 (line)]] | alt | 44.6 | 4 (1 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 8.51× (z +16.6) | [[Panobinostat (drug)]] 5 µM 0.275× (z -10.0) |
| [[LOX-IMVI (line)]] | wt | 70.7 | 3 | 4 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.53× (z +11.4) | [[Panobinostat (drug)]] 5 µM 0.221× (z -13.8) |
| [[RKO (line)]] | wt | 84.8 | 3 | 4 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.84× (z +12.7) | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -16.8) |
| [[SW 900 (line)]] | alt | 45.3 | 2 | 4 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.60× (z +9.1) | [[Harringtonine (drug)]] 5 µM 0.158× (z -12.4) |
| [[SW1417 (line)]] | alt | 59.1 | 2 (1 ⚠) | 4 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.30× (z +13.7) | [[Panobinostat (drug)]] 0.5 µM 0.280× (z -12.1) |
| [[A498 (line)]] | wt | 66.2 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 2.68× (z +9.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.274× (z -12.5) |
| [[C-33 A (line)]] | alt | 105 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.199× (z -14.0) |
| [[MIA PaCa-2 (line)]] | alt | 60.7 | 0 | 5 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.156× (z -15.0) |
| [[NCI-H23 (line)]] | alt | 94.8 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.189× (z -15.1) |
| [[SW48 (line)]] | wt | 69.4 | 0 | 5 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.116× (z -15.3) |
| [[HCT15 (line)]] | alt | 71.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.111× (z -16.1) |
| [[J82 (line)]] | alt | 73.5 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.257× (z -13.0) |
| [[SNU-1 (line)]] | wt | 64.4 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.77× (z +10.9) | — |
| [[SNU-423 (line)]] | alt | 44.6 | 3 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +11.1) | [[Belinostat (drug)]] 5 µM 0.279× (z -9.6) |
| [[A-172 (line)]] | wt | 52.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.172× (z -14.1) |
| [[C32 (line)]] | wt | 52.5 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.263× (z -10.2) |
| [[CFPAC-1 (line)]] | alt | 28.6 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +8.7) | — |
| [[COLO 205 (line)]] | alt | 45.3 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 9.51× (z +14.7) | — |
| [[HEC-1-A (line)]] | alt | 58.3 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.286× (z -11.5) |
| [[HS-578T (line)]] | alt | 36.8 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.281× (z -10.7) |
| [[NCI-H2347 (line)]] | alt | 35.8 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.98× (z +13.5) | [[Panobinostat (drug)]] 0.5 µM 0.273× (z -11.3) |
| [[SHP-77 (line)]] | alt | 69.6 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.255× (z -12.2) |
| [[BT-474 (line)]] | alt | 51.4 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0787× (z -20.0) |
| [[H4 (line)]] | wt | 69.0 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.205× (z -10.7) |
| [[Hs 766T (line)]] | wt | 40.1 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.96× (z +11.4) | [[Panobinostat (drug)]] 5 µM 0.284× (z -9.5) |
| [[NCI-H1792 (line)]] | alt | 26.3 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +9.4) | [[Thymol (drug)]] 0.5 µM 0.286× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 55.6 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.356× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 42.7 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.246× (z -9.1) |
| [[Panc 03.27 (line)]] | alt | 41.4 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.318× (z -8.7) |
| [[SW 1271 (line)]] | alt | 65.5 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0775× (z -9.7) ⚠ toxic |
| [[A549 (line)]] | wt | 39.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 91.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 42.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 45.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 80.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10267), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*43 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KMT2D]] | +0.74 | +0.62 / +0.77 | both halves | 7e-06 | pathway: Chromatin modifying enzymes; STRING 599 |
| [[PRDM10]] | +0.74 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[TOR1A]] | +0.73 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[TARDBP]] | +0.72 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[SUMO3]] | +0.71 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[CERS2]] | +0.71 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[PSME3]] | +0.70 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[LY6G5B]] | +0.69 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[PRDM15]] | +0.68 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[MFN2]] | +0.68 | +0.56 / +0.77 | both halves | 1e-05 |  |
| [[C2CD3]] | +0.68 | +0.64 / +0.47 | both halves | 2e-05 | pathway: Organelle biogenesis and maintenance |
| [[MOB1A]] | +0.68 | +0.56 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*57 of its nearest partners move opposite, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RP9]] | -0.77 | -0.77 / -0.71 | both halves | 7e-06 |  |
| [[PITPNA-AS1]] | -0.73 | -0.60 / -0.69 | both halves | 7e-06 |  |
| [[POLR2I]] | -0.68 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[ZNF14]] | -0.67 | -0.62 / -0.63 | both halves | 7e-06 |  |
| [[UBE2B]] | -0.67 | -0.60 / -0.60 | both halves | 7e-06 |  |
| [[MTLN]] ⚠ | -0.67 | -0.56 / -0.59 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[AFTPH]] | -0.67 | -0.61 / -0.68 | both halves | 7e-06 |  |
| [[FAM133B]] | -0.66 | -0.61 / -0.58 | both halves | 8e-06 |  |
| [[PIGH]] | -0.64 | -0.40 / -0.60 | both halves | 5e-05 |  |
| [[LINC00888-1]] | -0.64 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[TRAPPC5]] | -0.64 | -0.45 / -0.60 | both halves | 3e-05 |  |
| [[C18orf21]] | -0.64 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[RPS26]] | -0.63 | -0.38 / -0.64 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers HCFC1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MT1G]] | B | MT1G activity lowers HCFC1's level | lines that do not express MT1G (31) vs lines expressing it (19) | 1.27× higher at baseline in the lines without MT1G | 0.065 | ⚠ within organs, on part of the lines; also absent: TFF2, PROM1, FOXQ1 |
| [[MT1F]] | B | MT1F activity lowers HCFC1's level | lines that do not express MT1F (17) vs lines expressing it (33) | 1.22× higher at baseline in the lines without MT1F | 0.089 | ⚠ within organs, on part of the lines; also absent: CDC42BPG, RASAL1, ENSG00000289862 |
| [[CTSZ]] | B | CTSZ activity lowers HCFC1's level | lines that do not express CTSZ (8) vs lines expressing it (42) | 1.30× higher at baseline in the lines without CTSZ | 0.093 | ⚠ within organs, on part of the lines; also absent: LRRK1, CAV2, PIWIL4; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises HCFC1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises HCFC1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[FUCA2]] | C | FUCA2 activity lowers HCFC1's level | lines that do not express FUCA2 (3) vs lines expressing it (47) | 1.85× higher at baseline in the lines without FUCA2 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GPX1, AIFM2, SP100; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 126]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.723). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-34.3, -15.3); signed map (-13.5, -36.4). **Vector** length 144, 51.0% of its response variance represented; |z| ≥ 3 in 1,383 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +16.3 | +9.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +12.3 | +11.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +11.3 | +6.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +10.6 | +8.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +9.6 | +4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +8.4 | +6.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.7 | +4.7 |
|  | [[Demeclocycline (drug)]] 5 µM |  | +3.4 | +1.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.3 | +2.2 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -8.5 | -8.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -8.5 | -6.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.2 | -9.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -6.6 | -15.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.1 | -9.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.8 | -2.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -4.5 | -2.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.9 | -7.7 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -3.1 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | host cell factor C1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 — chrX:153,947,557-153,971,818 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HCF-1, HCF1, CFF, VCAF, MGC70925, PPP1R89; previously HFC1, MRX3 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; ATAC complex; NSL histone acetyltransferase complex |
| Reactome | 11 pathways, smallest: Formation of WDR5-containing histone-modifying complexes; Transcriptional activation of mitochondrial biogenesis; UCH proteinases |
| Matched by | ensembl_id |

**Function**, from UniProt [P51610](https://www.uniprot.org/uniprotkb/P51610) (Host cell factor 1):

> Transcriptional coregulator (By similarity). Serves as a scaffold protein, bridging interactions between transcription factors, including THAP11 and ZNF143, and transcriptional coregulators. Involved in control of the cell cycle. Also antagonizes transactivation by ZBTB17 and GABP2; represses ZBTB17 activation of the p15(INK4b) promoter and inhibits its ability to recruit p300. Coactivator for EGR2 and GABP2. Tethers the chromatin modifying Set1/Ash2 histone H3 'Lys-4' methyltransferase …

**Summary**, from NCBI Gene [3054](https://www.ncbi.nlm.nih.gov/gene/3054):

> This gene is a member of the host cell factor family and encodes a protein with five Kelch repeats, a fibronectin-like motif, and six HCF repeats, each of which contains a highly specific cleavage signal. This nuclear coactivator is proteolytically cleaved at one of the six possible sites, resulting in the creation of an N-terminal chain and the corresponding C-terminal chain. The final form of this protein consists of noncovalently bound N- and C-terminal chains. The protein is involved in …

**Accessions** — [HGNC:4839](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4839) · Entrez [3054](https://www.ncbi.nlm.nih.gov/gene/3054) · UniProt [P51610](https://www.uniprot.org/uniprotkb/P51610) · Ensembl [ENSG00000172534](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172534)

## Data

Gene col 10267: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10267); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10267, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10267]; `tensor/DDL_lfc|DDL_z.npy` [10267]; `embed/gene_vectors.npy` [10267]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10267 or target_col == 10267). Every well: [[HCFC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HCFC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
