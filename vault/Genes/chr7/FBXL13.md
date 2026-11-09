---
symbol: "FBXL13"
type: "gene"
col: 8413
ensembl_id: "ENSG00000161040"
name: "F-box and leucine rich repeat protein 13"
location: "7q22.1"
module: 26
arm: "+"
pooled_cpm: 49.18
n_lines_expressing: 46
n_dd_up: 15
n_dd_down: 23
n_dd_up_clean: 12
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# FBXL13

*F-box and leucine rich repeat protein 13* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.48× (z +20.8, q 0e+00, up in 34 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (8 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.410× (z -7.5, q 1e-11, down in 29 of 45 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AADACL2-AS1]] (+0.58, fdr 1e-05), [[PIPOX]] (+0.53, fdr 3e-05), [[CCDC90B-AS1]] (+0.52, fdr 3e-05); moves opposite to [[ASB13]] (-0.52, fdr 3e-05), [[ZNF639]] (-0.51, fdr 4e-05), [[FYCO1]] (-0.51, fdr 3e-05).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[RABL2A]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8413.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.48×** | +20.8 | 0e+00 | 34/44 (LoVo, RKO, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.45×** | +8.6 | 3e-15 | 26/44 (MIA PaCa-2, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.50×** | +6.5 | 1e-08 | 22/44 (A498, HT-29, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +6.4 | 2e-08 | 22/43 (A498, SW480, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +5.8 | 9e-07 | 22/45 (SW480, RKO, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.39×** | +5.3 | 9e-06 | 21/44 (KATO III, HT-29, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.34×** | +4.5 | 5e-04 | 11/31 (LoVo, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.28×** | +3.9 | 0.008 | 14/43 (LS 180, A-172, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.27×** | +3.8 | 0.008 | 15/44 (A549, A-427, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.26×** | +3.7 | 0.012 | 16/44 (HT-29, A498, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Afatinib (drug)]] 0.5 µM |  | 1.17× | +3.4 | 0.038 | 6/45 (C-33 A, KATO III, …) | all doses, flat | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.23×** | +3.3 | 0.042 | 11/41 (RPMI-7951, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Brimonidine (drug)]] 5 µM |  | **1.22×** | +3.3 | 0.046 | 6/44 (NCI-H1573, CFPAC-1, …) | top dose only |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.22×** | +3.3 | 0.047 | 6/45 (HOP62, NCI-H1573, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.21×** | +3.1 | 0.068 | 9/44 (HT-29, A-172, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.20×** | +3.0 | 0.088 | 12/44 (KATO III, LS 180, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8413.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.410×** | -7.5 | 1e-11 | 29/45 (HS-578T, SK-MEL-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.617×** | -7.5 | 1e-11 | 28/44 (NCI-H1792, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.628×** | -7.5 | 1e-11 | 29/44 (HS-578T, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.632×** | -7.4 | 2e-11 | 28/44 (HS-578T, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.624×** | -7.3 | 3e-11 | 27/41 (NCI-H23, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.649×** | -7.0 | 3e-10 | 26/44 (HS-578T, SW 1088, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.671×** | -6.4 | 1e-08 | 21/44 (HS-578T, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.695×** | -5.9 | 3e-07 | 26/44 (NCI-H23, CFPAC-1, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.534×** | -5.3 | 7e-06 | 22/40 (HS-578T, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.720×** | -5.3 | 7e-06 | 25/43 (CFPAC-1, PANC-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.793×** | -5.3 | 7e-06 | 22/45 (NCI-H1573, NCI-H23, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.724×** | -5.2 | 9e-06 | 21/43 (HS-578T, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.744×** | -4.6 | 2e-04 | 18/43 (A-427, HT-29, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.764×** | -4.3 | 6e-04 | 18/43 (HOP62, HT-29, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.787×** | -3.9 | 0.004 | 19/44 (HS-578T, PANC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.799×** | -3.6 | 0.010 | 9/44 (PANC-1, C32, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.818×** | -3.2 | 0.038 | 13/44 (LOX-IMVI, HS-578T, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.821×** | -3.1 | 0.063 | 11/44 (NCI-H23, CFPAC-1, …) | top dose only | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.820×** | -3.0 | 0.071 | 13/44 (HS-578T, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.826×** | -3.0 | 0.081 | 4/45 (A-172, SW 900, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8413. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 312 | 0 | 15 (9 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.117× (z -17.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.288× (z -15.4) |
| [[NCI-H1792 (line)]] | alt | 575 | 0 | 14 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -30.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.188× (z -20.1) |
| [[NCI-H460 (line)]] | wt | 173 | 0 | 11 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.173× (z -20.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.314× (z -13.4) |
| [[A498 (line)]] | wt | 18.5 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.66× (z +13.3) | — |
| [[PANC-1 (line)]] | alt | 27.6 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +10.2) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.364× (z -9.3) ⚠ cell-cycle shift, explains ~30% of this change |
| [[COLO 205 (line)]] | alt | 29.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.166× (z -10.6) ⚠ cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 15.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.37× (z +9.1) | [[Docetaxel (drug)]] 0.05 µM 0.140× (z -8.6) ⚠ transcription drop; cell-cycle shift, explains ~93% of this change |
| [[KATO III (line)]] | alt | 26.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.49× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 14.2 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.25× (z +17.2) | — |
| [[NCI-H23 (line)]] | alt | 36.8 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0701× (z -18.8) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.311× (z -8.6) |
| [[RKO (line)]] | wt | 17.6 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.81× (z +14.9) | [[Hydroxyurea (drug)]] 0.05 µM 0.165× (z -9.2) |
| [[A-172 (line)]] | wt | 32.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +9.4) | — |
| [[A549 (line)]] | wt | 21.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.81× (z +9.6) | — |
| [[AsPC-1 (line)]] | alt | 24.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.91× (z +8.6) | — |
| [[C-33 A (line)]] | alt | 30.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.179× (z -10.0) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 58.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.01× (z +10.1) | — |
| [[CHP-212 (line)]] | wt | 31.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0702× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[H4 (line)]] | wt | 60.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.171× (z -8.7) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 14.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.30× (z +13.1) | — |
| [[HOP62 (line)]] | alt | 23.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +11.0) | — |
| [[Hs 766T (line)]] | wt | 21.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.01× (z +8.9) | — |
| [[HT-29 (line)]] | alt | 28.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -9.1) ⚠ cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 18.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.54× (z +11.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 17.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.62× (z +14.5) | — |
| [[NCI-H1573 (line)]] | alt | 26.7 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.121× (z -13.9) ⚠ cell-cycle shift, explains ~36% of this change |
| [[Panc 03.27 (line)]] | alt | 59.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.35× (z +9.4) | — |
| [[RPMI-7951 (line)]] | alt | 14.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.19× (z +9.4) | — |
| [[SK-MEL-2 (line)]] | alt | 80.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.332× (z -9.6) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 13.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.81× (z +11.3) | — |
| [[SW48 (line)]] | wt | 13.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.66× (z +8.5) | — |
| [[SW480 (line)]] | alt | 31.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.97× (z +14.6) | — |
| [[A-427 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.94 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.4 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.5 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.98 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 79.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 31.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8413), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AADACL2-AS1]] | +0.58 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[PIPOX]] | +0.53 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[CCDC90B-AS1]] | +0.52 | +0.62 / +0.43 | both halves | 3e-05 |  |
| [[CCNT2-AS1]] | +0.52 | +0.61 / +0.37 | both halves | 8e-05 |  |
| [[LINC02018]] | +0.52 | +0.45 / +0.41 | both halves | 4e-05 |  |
| [[STARD4-AS1]] | +0.52 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[EHBP1-AS1]] | +0.51 | +0.40 / +0.48 | both halves | 5e-05 |  |
| [[NRL]] | +0.50 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[TTC41P]] | +0.50 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[FANK1]] | +0.50 | +0.44 / +0.48 | both halves | 3e-05 |  |
| [[USP34-DT]] | +0.50 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[MAP3K20-AS1]] | +0.49 | +0.47 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASB13]] | -0.52 | -0.48 / -0.43 | both halves | 3e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[ZNF639]] | -0.51 | -0.40 / -0.47 | both halves | 4e-05 |  |
| [[FYCO1]] | -0.51 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[SAAL1]] | -0.51 | -0.37 / -0.50 | both halves | 8e-05 |  |
| [[GTF2H2C]] | -0.50 | -0.19 / -0.49 | ⚠ not reproduced | 8e-04 |  |
| [[ZNF74]] | -0.48 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[SLC46A1]] | -0.47 | -0.29 / -0.40 | both halves | 3e-04 |  |
| [[PTPN3]] | -0.47 | -0.47 / -0.35 | both halves | 1e-04 |  |
| [[TTLL4]] | -0.47 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[SRI]] | -0.47 | -0.39 / -0.38 | both halves | 6e-05 |  |
| [[METTL5]] | -0.47 | -0.30 / -0.39 | both halves | 2e-04 |  |
| [[GNPTAB]] | -0.46 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[FGD4]] | -0.46 | -0.38 / -0.44 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers FBXL13's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RABL2A]] | C | FBXL13 activity raises RABL2A's level | lines that do not express FBXL13 (4) vs lines expressing it (46) | 1.54× lower at baseline in the lines without FBXL13 | 0.0999 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FBXO38-DT, MIAT; maybe low, not absent |

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.465). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (13.7, 20.1); signed map (26.6, -1.3). **Vector** length 73.7, 13.8% of its response variance represented; |z| ≥ 3 in 1,087 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.1 | +20.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.4 | +8.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.3 | -1.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +5.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +6.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +0.9 |
|  | [[Afatinib (drug)]] 0.5 µM |  | +1.3 | +3.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.3 | +0.9 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.2 | +1.6 |
| fall | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.8 | -5.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.7 | -7.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -0.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.6 | -5.3 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -2.3 | -5.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | +0.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.1 | -4.6 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -2.0 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | F-box and leucine rich repeat protein 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:102,811,189-103,074,839 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC21636, Fbl13, DRC6, CFAP169 |
| Gene groups (HGNC) | F-box and leucine rich repeat proteins; Dynein regulatory complex; Cilia and flagella associated |
| Reactome | 4 pathways, smallest: Neddylation; Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NEE6](https://www.uniprot.org/uniprotkb/Q8NEE6) (F-box and leucine-rich repeat protein 13):

> Substrate-recognition component of the SCF (SKP1-CUL1-F-box protein)-type E3 ubiquitin ligase complex. Component of the nexin-dynein regulatory complex (N-DRC), a key regulator of ciliary/flagellar motility which maintains the alignment and integrity of the distal axoneme and regulates microtubule sliding in motile axonemes. Specifically targets CEP192 isoform 3 for ubiquitin-mediated proteolysis and thereby acts as a regulator of microtubule nucleation activity.

**Summary**, from NCBI Gene [222235](https://www.ncbi.nlm.nih.gov/gene/222235):

> Members of the F-box protein family, such as FBXL13, are characterized by an approximately 40-amino acid F-box motif. SCF complexes, formed by SKP1 (MIM 601434), cullin (see CUL1; MIM 603134), and F-box proteins, act as protein-ubiquitin ligases. F-box proteins interact with SKP1 through the F box, and they interact with ubiquitination targets through other protein interaction domains (Jin et al., 2004 [PubMed 15520277]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:21658](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21658) · Entrez [222235](https://www.ncbi.nlm.nih.gov/gene/222235) · UniProt [Q8NEE6](https://www.uniprot.org/uniprotkb/Q8NEE6) · Ensembl [ENSG00000161040](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161040)

## Data

Gene col 8413: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8413); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8413, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8413]; `tensor/DDL_lfc|DDL_z.npy` [8413]; `embed/gene_vectors.npy` [8413]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8413 or target_col == 8413). Every well: [[FBXL13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBXL13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
