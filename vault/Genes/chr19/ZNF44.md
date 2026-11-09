---
symbol: "ZNF44"
type: "gene"
col: 12476
ensembl_id: "ENSG00000197857"
name: "zinc finger protein 44"
location: "19p13.2"
module: 94
arm: "+"
pooled_cpm: 24.96
n_lines_expressing: 46
n_dd_up: 17
n_dd_down: 11
n_dd_up_clean: 15
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 10
direction_downstream: 9
tags: ["gene", "module/094"]
generated_by: "tahoemap"
---

# ZNF44

*zinc finger protein 44* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.49× (z +35.1, q 0e+00, up in 41 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.535× (z -12.4, q 1e-32, down in 30 of 41 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Peretinoin (drug)]] 5 µM: 0.762× (z -5.2, q 3e-05, down in 17 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF442]] (+0.80, fdr 7e-06), [[ZNF433]] (+0.78, fdr 7e-06), [[ZNF563]] (+0.74, fdr 7e-06, ⚠ same locus), [[CLK4]] (+0.72, fdr 7e-06); moves opposite to [[FAM20B]] (-0.65, fdr 7e-06), [[AHCY]] (-0.64, fdr 1e-05), [[IPO7]] (-0.63, fdr 1e-05).
> It is in [[Module 094]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[ZNF441]] → it (grade B ⚠); 9 go from it, the strongest it → [[ZNF20]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12476.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.49×** | +35.1 | 0e+00 | 41/44 (SW1417, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.86×** | +20.9 | 0e+00 | 38/43 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.85×** | +20.0 | 0e+00 | 42/44 (J82, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.99×** | +19.3 | 0e+00 | 41/44 (RPMI-7951, PANC-1, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.94×** | +13.1 | 3e-37 | 39/44 (RPMI-7951, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.92×** | +12.9 | 3e-36 | 40/44 (RPMI-7951, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.94×** | +11.2 | 4e-27 | 36/44 (Panc 03.27, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.71×** | +10.7 | 1e-24 | 33/44 (RKO, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.58×** | +9.1 | 7e-18 | 37/44 (PANC-1, RPMI-7951, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +7.6 | 2e-12 | 25/44 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.81×** | +6.2 | 4e-08 | 22/44 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.30×** | +5.3 | 6e-06 | 19/44 (HEC-1-A, A-427, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.31×** | +5.1 | 1e-05 | 19/43 (LoVo, C32, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.29×** | +5.0 | 3e-05 | 20/43 (SW1417, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +4.7 | 8e-05 | 16/44 (PANC-1, J82, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.26×** | +4.5 | 2e-04 | 16/44 (SW1417, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 9 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12476.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.535×** | -12.4 | 1e-32 | 30/41 (KATO III, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.653×** | -8.1 | 1e-13 | 22/31 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.701×** | -7.0 | 3e-10 | 28/44 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.762×** | -5.2 | 3e-05 | 17/43 (HEC-1-A, NCI-H23, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **0.788×** | -4.6 | 6e-04 | 17/42 (NCI-H2347, SNU-423, …) | top dose only |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.800×** | -4.4 | 9e-04 | 16/43 (HT-29, SW 900, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.796×** | -4.2 | 0.002 | 17/36 (LS 180, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[vincristine (drug)]] 0.5 µM |  | **0.746×** | -4.1 | 0.002 | 13/44 (CFPAC-1, Hs 766T, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.682×** | -4.0 | 0.005 | 11/44 (H4, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Gefitinib (drug)]] 5 µM |  | 0.835× | -3.6 | 0.020 | 7/44 (A-172, COLO 205, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 0.882× | -3.5 | 0.022 | 10/44 (COLO 205, RPMI-7951, …) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | 0.888× | -3.3 | 0.040 | 11/44 (H4, RKO, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | 0.849× | -3.3 | 0.049 | 7/44 (SW 900, SW1417, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 5 µM |  | **0.735×** | -3.2 | 0.056 | 6/41 (SW48, RKO, …) | two highest doses | noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.853× | -3.2 | 0.058 | 10/44 (MIA PaCa-2, NCI-H23, …) | two highest doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.858× | -3.0 | 0.083 | 6/44 (LoVo, SNU-1, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.859× | -3.0 | 0.084 | 12/43 (SNU-423, SW 900, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.750×** | -3.0 | 0.090 | 10/44 (HepG2/C3A, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12476. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 29.3 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.52× (z +21.5) | [[Dinaciclib (drug)]] 0.05 µM 0.274× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[SW1417 (line)]] | alt | 39.4 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.48× (z +22.3) | [[Dinaciclib (drug)]] 0.05 µM 0.341× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[SW480 (line)]] | alt | 31.8 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +20.0) | [[Dinaciclib (drug)]] 5 µM 0.197× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[Panc 03.27 (line)]] | alt | 38.2 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.45× (z +20.4) | [[Dinaciclib (drug)]] 0.05 µM 0.272× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[PANC-1 (line)]] | alt | 19.4 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +15.6) | — |
| [[A-172 (line)]] | wt | 39.4 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +15.9) | [[Dinaciclib (drug)]] 0.5 µM 0.170× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[J82 (line)]] | alt | 32.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.16× (z +20.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 25.8 | 3 | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 3.30× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.0964× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[RKO (line)]] | wt | 28.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.1× (z +20.3) | — |
| [[RPMI-7951 (line)]] | alt | 40.5 | 2 | 2 (2 ⚠) | [[Selinexor (drug)]] 5 µM 3.53× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.222× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[HEC-1-A (line)]] | alt | 32.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +15.4) | — |
| [[LS 180 (line)]] | wt | 48.7 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +9.8) | [[Dinaciclib (drug)]] 0.05 µM 0.147× (z -16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[SNU-423 (line)]] | alt | 42.9 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.278× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SW48 (line)]] | wt | 23.5 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.09× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.156× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[A-427 (line)]] | wt | 18.5 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.43× (z +10.3) | — |
| [[AsPC-1 (line)]] | alt | 25.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +15.3) | — |
| [[HCT15 (line)]] | alt | 25.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +11.4) | — |
| [[HT-29 (line)]] | alt | 17.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +12.2) | — |
| [[hTERT-HPNE (line)]] | wt | 24.4 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 5.12× (z +9.6) | — |
| [[KATO III (line)]] | alt | 19.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.48× (z +14.2) | [[Dinaciclib (drug)]] 0.5 µM 0.0866× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[LoVo (line)]] | wt | 27.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +12.0) | — |
| [[SK-MEL-2 (line)]] | alt | 29.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +13.3) | — |
| [[SNU-1 (line)]] | wt | 29.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.24× (z +10.8) | — |
| [[BT-474 (line)]] | alt | 43.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +12.6) | — |
| [[C-33 A (line)]] | alt | 16.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +10.3) | — |
| [[C32 (line)]] | wt | 22.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +11.2) | — |
| [[CFPAC-1 (line)]] | alt | 22.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +13.8) | — |
| [[CHP-212 (line)]] | wt | 38.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.22× (z +9.3) | — |
| [[HepG2_C3A (line)]] | wt | 43.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +11.5) | — |
| [[HOP62 (line)]] | alt | 16.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +9.4) | — |
| [[Hs 766T (line)]] | wt | 37.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +13.3) | — |
| [[HS-578T (line)]] | alt | 31.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +12.6) | — |
| [[NCI-H1573 (line)]] | alt | 10.00 | 1 | 0 | [[Selinexor (drug)]] 5 µM 3.17× (z +9.4) | — |
| [[SHP-77 (line)]] | alt | 26.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.118× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SW 900 (line)]] | alt | 29.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +12.2) | — |
| [[A498 (line)]] | wt | 2.11 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 6.58 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 87.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.98 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.73 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.91 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 56.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12476), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF442]] | +0.80 | +0.70 / +0.81 | both halves | 7e-06 | same gene group |
| [[ZNF433]] | +0.78 | +0.71 / +0.77 | both halves | 7e-06 | same gene group |
| [[ZNF563]] | +0.74 | +0.68 / +0.70 | both halves | 7e-06 | same gene group; ⚠ same locus (22.6 kb, same strand: neighbours can correlate without regulation) |
| [[CLK4]] | +0.72 | +0.78 / +0.66 | both halves | 7e-06 |  |
| [[SLC43A2]] | +0.70 | +0.60 / +0.72 | both halves | 7e-06 |  |
| [[ZNF627]] | +0.70 | +0.63 / +0.71 | both halves | 7e-06 | same gene group |
| [[ZNF441]] | +0.69 | +0.62 / +0.70 | both halves | 7e-06 | same gene group |
| [[BTN2A1]] | +0.69 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[CLN5]] | +0.69 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[DUSP15]] | +0.68 | +0.61 / +0.74 | both halves | 7e-06 |  |
| [[PLEKHF2]] | +0.67 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[ZNF585A]] | +0.65 | +0.66 / +0.58 | both halves | 7e-06 | same gene group |
| [[PEX12]] | +0.65 | +0.64 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM20B]] | -0.65 | -0.66 / -0.58 | both halves | 7e-06 |  |
| [[AHCY]] | -0.64 | -0.65 / -0.53 | both halves | 1e-05 |  |
| [[IPO7]] | -0.63 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[LRP8]] | -0.60 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[CHID1]] | -0.59 | -0.61 / -0.55 | both halves | 1e-05 |  |
| [[LMBR1]] | -0.58 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[SNRPA]] | -0.58 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[NUTF2]] | -0.58 | -0.64 / -0.47 | both halves | 2e-05 |  |
| [[EXOC2]] | -0.57 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[PPM1F]] | -0.56 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[TMTC4]] | -0.56 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[PSME4]] | -0.56 | -0.48 / -0.56 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 7, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF441]] | B | ZNF441 activity raises ZNF44's level | lines that do not express ZNF441 (7) vs lines expressing it (43) | 2.98× lower at baseline in the lines without ZNF441 | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000286098, ZNF442, ZNF433 |
| [[ZNF442]] | B | ZNF442 activity raises ZNF44's level | lines that do not express ZNF442 (7) vs lines expressing it (43) | 3.60× lower at baseline in the lines without ZNF442 | 0.005 | ⚠ within organs, on part of the lines; also absent: ZNF563, ENSG00000286098, ENSG00000268870 |
| [[ZNF433]] | B | ZNF433 activity raises ZNF44's level | lines that do not express ZNF433 (8) vs lines expressing it (42) | 3.11× lower at baseline in the lines without ZNF433 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000269755, ZNF563, ZNF442 |
| [[ZNF682]] | B | ZNF682 activity raises ZNF44's level | lines that do not express ZNF682 (20) vs lines expressing it (30) | 2.04× lower at baseline in the lines without ZNF682 | 0.007 | ⚠ within organs, on part of the lines; also absent: ZNF93, ZNF90, SCUBE3 |
| [[ZNF563]] | B | ZNF563 activity raises ZNF44's level | lines that do not express ZNF563 (9) vs lines expressing it (41) | 2.64× lower at baseline in the lines without ZNF563 | 0.021 | ⚠ within organs, on part of the lines; also absent: ZNF442, ZNF433, ENSG00000269755 |
| [[ZNF844]] | B | ZNF844 activity raises ZNF44's level | lines that do not express ZNF844 (23) vs lines expressing it (27) | 1.89× lower at baseline in the lines without ZNF844 | 0.041 | ⚠ within organs, on part of the lines; also absent: ENSG00000286132, ENSG00000267383, ZNF486 |
| [[ZNF625]] | B | ZNF625 activity raises ZNF44's level | lines that do not express ZNF625 (19) vs lines expressing it (31) | 1.38× lower at baseline in the lines without ZNF625 | 0.078 | ⚠ within organs, on part of the lines; also absent: ZNF415, ZNF829, ZNF347 |
| [[ZNF20]] | C | ZNF20 activity raises ZNF44's level | lines that do not express ZNF20 (4) vs lines expressing it (46) | 6.62× lower at baseline in the lines without ZNF20 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000268870, ZNF700, ZNF44; maybe low, not absent; co-absent with the target; its own permutation p |
| [[SLC43A2]] | C | SLC43A2 activity raises ZNF44's level | lines that do not express SLC43A2 (3) vs lines expressing it (47) | 4.94× lower at baseline in the lines without SLC43A2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CTDSPL, ZNF44, ITGA9-AS1; maybe low, not absent; co-absent with the target; its own permutation p |
| [[ZNF440]] | C | ZNF440 activity raises ZNF44's level | lines that do not express ZNF440 (4) vs lines expressing it (46) | 5.00× lower at baseline in the lines without ZNF440 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: ENSG00000268870, ENSG00000269755, ZNF20; its own permutation p |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 0, C 9.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF20]] | C | ZNF44 activity raises ZNF20's level | lines that do not express ZNF44 (3) vs lines expressing it (46) | 3.58× lower at baseline in the lines without ZNF44 | 2e-04 | ⚠ few lines (3 vs 46); across organs; also absent: ZNF20, ENSG00000268870, SORT1; co-absent with the target |
| [[ZNF440]] | C | ZNF44 activity raises ZNF440's level | lines that do not express ZNF44 (3) vs lines expressing it (46) | 5.07× lower at baseline in the lines without ZNF44 | 0.002 | ⚠ few lines (3 vs 46); across organs; also absent: ZNF20, ENSG00000268870, SORT1 |
| [[ZNF138]] | C | ZNF44 activity raises ZNF138's level | lines that do not express ZNF44 (3) vs lines expressing it (46) | 2.99× lower at baseline in the lines without ZNF44 | 0.019 | ⚠ few lines (3 vs 46); across organs; also absent: ZNF20, ENSG00000268870, SORT1 |
| [[ZNF563]] | C | ZNF44 activity raises ZNF563's level | lines that do not express ZNF44 (3) vs lines expressing it (46) | 3.60× lower at baseline in the lines without ZNF44 | 0.024 | ⚠ few lines (3 vs 46); across organs; also absent: ZNF20, ENSG00000268870, SORT1 |
| [[ZNF442]] | C | ZNF44 activity raises ZNF442's level | lines that do not express ZNF44 (3) vs lines expressing it (46) | 3.53× lower at baseline in the lines without ZNF44 | 0.032 | ⚠ few lines (3 vs 46); across organs; also absent: ZNF20, ENSG00000268870, SORT1 |
| [[ZNF433]] | C | ZNF44 activity raises ZNF433's level | lines that do not express ZNF44 (3) vs lines expressing it (46) | 4.45× lower at baseline in the lines without ZNF44 | 0.034 | ⚠ few lines (3 vs 46); across organs; also absent: ZNF20, ENSG00000268870, SORT1 |
| [[OSGIN2]] | C | ZNF44 activity strengthens OSGIN2's drug response | lines that do not express ZNF44 (3) vs lines expressing it (44) | the lines without ZNF44 respond 0.50× as strongly (z diff +2.69); strongest at Idarubicin (hydrochloride) 5 µM: 0.97x vs 1.64x (z diff +6.0) | 0.073 | ⚠ few lines (3 vs 46); across organs; also absent: ZNF20, ENSG00000268870, SORT1; target measured in part of the lines; artifact flags |
| [[PSME4]] | C | ZNF44 activity strengthens PSME4's drug response | lines that do not express ZNF44 (3) vs lines expressing it (44) | the lines without ZNF44 respond 0.97× as strongly (z diff +0.91); strongest at Bortezomib 0.05 µM: 1.68x vs 2.22x (z diff +3.8) | 0.081 | ⚠ few lines (3 vs 46); across organs; also absent: ZNF20, ENSG00000268870, SORT1; target measured in part of the lines; rests on the correction; artifact flags |
| [[RHBDD1]] | C | ZNF44's natural level weakens RHBDD1's drug response | ZNF44's natural level across 44 lines (lineage-adjusted; a glimpse) | r -0.65, reverse -0.06; direction not clear | 0.095 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 094]]; 49 genes; every member is in the + arm (projection on the module's main direction 0.846). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-22.0, 23.8); signed map (16.1, -16.7). **Vector** length 103, 25.1% of its response variance represented; |z| ≥ 3 in 1,028 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +13.0 | +19.3 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +9.0 | +13.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.5 | +20.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.4 | +10.7 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +6.3 | +12.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +4.8 | +9.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.4 | +5.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +1.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +2.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.5 | +1.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.7 | -7.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -1.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | +2.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.9 | -2.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.7 | +2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | -2.6 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.4 | -3.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.4 | -4.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.3 | -5.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.9 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 44 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:12,224,686-12,294,883 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KOX7, ZNF504; previously ZNF58, ZNF55 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KRAB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [P15621](https://www.uniprot.org/uniprotkb/P15621) (Zinc finger protein 44):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [51710](https://www.ncbi.nlm.nih.gov/gene/51710):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II transcription regulatory region sequence-specific DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:13110](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13110) · Entrez [51710](https://www.ncbi.nlm.nih.gov/gene/51710) · UniProt [P15621](https://www.uniprot.org/uniprotkb/P15621) · Ensembl [ENSG00000197857](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197857)

## Data

Gene col 12476: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12476); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12476, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12476]; `tensor/DDL_lfc|DDL_z.npy` [12476]; `embed/gene_vectors.npy` [12476]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12476 or target_col == 12476). Every well: [[ZNF44 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF44.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
