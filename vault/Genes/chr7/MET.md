---
symbol: "MET"
type: "gene"
col: 2697
ensembl_id: "ENSG00000105976"
name: "MET proto-oncogene, receptor tyrosine kinase"
location: "7q31.2"
module: 34
arm: "+"
pooled_cpm: 393.53
n_lines_expressing: 41
n_dd_up: 11
n_dd_down: 19
n_dd_up_clean: 8
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 30
direction_downstream: 25
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# MET

*MET proto-oncogene, receptor tyrosine kinase* — 7q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.66× (z +10.9, q 7e-25, up in 33 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.311× (z -24.8, q 0e+00, down in 38 of 39 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LAMA3]] (+0.63, fdr 7e-06), [[HAS3]] (+0.56, fdr 1e-05), [[IRS1]] (+0.55, fdr 2e-05); moves opposite to [[BTRC]] (-0.44, fdr 9e-05), [[PLPP5]] (-0.43, fdr 4e-05), [[GID8]] (-0.43, fdr 2e-04).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 30 arrows point to it, the strongest [[LAMC2]] → it (grade B ⚠); 25 go from it, the strongest it → [[CAB39]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠; shown: the 15 strongest. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2697.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.66×** | +10.9 | 7e-25 | 33/40 (AsPC-1, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.50×** | +8.7 | 1e-15 | 30/39 (HT-29, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.30×** | +5.6 | 3e-06 | 20/39 (PANC-1, SK-MEL-2, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.28×** | +5.3 | 2e-05 | 21/39 (HT-29, COLO 205, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.29×** | +5.2 | 3e-05 | 22/38 (HT-29, COLO 205, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.27×** | +5.0 | 4e-05 | 22/39 (HT-29, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.27×** | +4.9 | 7e-05 | 20/39 (A-172, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.53×** | +4.7 | 2e-04 | 25/39 (NCI-H2030, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.23×** | +4.5 | 4e-04 | 23/39 (HT-29, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.22×** | +4.2 | 0.001 | 20/38 (SW480, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.21×** | +4.1 | 0.002 | 20/38 (COLO 205, HT-29, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.20× | +3.9 | 0.006 | 17/39 (HT-29, SK-MEL-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.18× | +3.6 | 0.015 | 12/39 (A-172, SW48, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.18× | +3.5 | 0.017 | 16/39 (HT-29, H4, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.12× | +3.5 | 0.017 | 12/40 (HT-29, SK-MEL-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2697.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.311×** | -24.8 | 0e+00 | 38/39 (HEC-1-A, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.314×** | -24.6 | 0e+00 | 37/39 (HEC-1-A, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.445×** | -24.3 | 0e+00 | 38/40 (Panc 03.27, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.425×** | -18.2 | 0e+00 | 34/39 (HEC-1-A, A549, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.543×** | -12.5 | 1e-33 | 33/38 (CFPAC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.604×** | -10.3 | 7e-23 | 33/39 (A498, SW48, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.679×** | -7.9 | 2e-13 | 29/41 (Panc 03.27, SW 900, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.756×** | -5.9 | 2e-07 | 26/39 (LoVo, KATO III, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.773×** | -5.5 | 3e-06 | 23/39 (A498, HEC-1-A, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.620×** | -5.3 | 6e-06 | 23/38 (A498, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.779×** | -5.1 | 2e-05 | 21/39 (LoVo, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.793×** | -4.9 | 4e-05 | 20/39 (HEC-1-A, HT-29, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.795×** | -4.7 | 1e-04 | 20/35 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.804×** | -4.6 | 2e-04 | 24/40 (KATO III, RKO, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.820×** | -4.2 | 0.001 | 20/39 (KATO III, LoVo, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 0.875× | -4.0 | 0.002 | 6/40 (HS-578T, SK-MEL-2, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.887× | -3.5 | 0.015 | 12/40 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.5 µM |  | 0.850× | -3.4 | 0.016 | 10/39 (COLO 205, LOX-IMVI, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.762×** | -3.0 | 0.064 | 16/40 (HCT15, SW48, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.766×** | -3.0 | 0.072 | 18/40 (HEC-1-A, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2697. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 393 | 11 (3 ⚠) | 7 (1 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.80× (z +11.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.290× (z -19.6) |
| [[LoVo (line)]] | wt | 847 | 1 | 17 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 6.02× (z +11.8) | [[Panobinostat (drug)]] 5 µM 0.145× (z -24.4) |
| [[SW48 (line)]] | wt | 550 | 0 | 18 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.242× (z -20.2) |
| [[HOP62 (line)]] | alt | 171 | 14 (3 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +11.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Budesonide (drug)]] 5 µM 2.79× (z +11.1) | [[Panobinostat (drug)]] 0.5 µM 0.432× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 651 | 0 | 13 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.233× (z -26.9) |
| [[COLO 205 (line)]] | alt | 267 | 7 (5 ⚠) | 4 | [[Homoharringtonine (drug)]] 0.5 µM 3.47× (z +12.7) ⚠ cell-cycle shift, explains ~94% of this change · without an alert: [[Peretinoin (drug)]] 5 µM 2.95× (z +10.7) | [[Panobinostat (drug)]] 5 µM 0.272× (z -13.4) |
| [[LS 180 (line)]] | wt | 369 | 1 (1 ⚠) | 9 (3 ⚠) | [[Selinexor (drug)]] 5 µM 1.87× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.129× (z -21.5) |
| [[NCI-H1573 (line)]] | alt | 2,840 | 1 | 9 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.72× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -24.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.142× (z -20.1) |
| [[SW 900 (line)]] | alt | 509 | 0 | 10 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -19.8) |
| [[A498 (line)]] | wt | 578 | 1 (1 ⚠) | 8 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +9.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -26.2) |
| [[AsPC-1 (line)]] | alt | 593 | 3 (2 ⚠) | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +17.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.01× (z +12.0) | [[Panobinostat (drug)]] 5 µM 0.194× (z -23.3) |
| [[KATO III (line)]] | alt | 541 | 0 | 9 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.165× (z -20.0) |
| [[Panc 03.27 (line)]] | alt | 705 | 0 | 9 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.217× (z -28.1) |
| [[CFPAC-1 (line)]] | alt | 771 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.284× (z -25.1) |
| [[A-172 (line)]] | wt | 109 | 5 (3 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +18.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.41× (z +9.0) | [[Panobinostat (drug)]] 0.5 µM 0.391× (z -10.0) |
| [[J82 (line)]] | alt | 243 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.248× (z -18.9) |
| [[NCI-H1792 (line)]] | alt | 492 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.230× (z -22.0) |
| [[SW480 (line)]] | alt | 188 | 1 | 6 | [[TAK-901 (drug)]] 5 µM 5.06× (z +10.3) | [[Panobinostat (drug)]] 5 µM 0.252× (z -16.8) |
| [[A549 (line)]] | wt | 484 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.235× (z -26.1) |
| [[Hs 766T (line)]] | wt | 590 | 1 | 5 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.86× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -17.5) |
| [[NCI-H2030 (line)]] | alt | 274 | 1 | 5 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.35× (z +11.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -19.7) |
| [[PANC-1 (line)]] | alt | 233 | 2 (1 ⚠) | 4 | [[TAK-901 (drug)]] 5 µM 3.06× (z +9.8) | [[Panobinostat (drug)]] 5 µM 0.288× (z -21.0) |
| [[RKO (line)]] | wt | 200 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.411× (z -11.7) |
| [[HS-578T (line)]] | alt | 199 | 2 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +11.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Dexamethasone (drug)]] 0.5 µM 2.09× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.385× (z -11.1) |
| [[NCI-H2347 (line)]] | alt | 572 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.250× (z -16.6) |
| [[SNU-423 (line)]] | alt | 230 | 1 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +11.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.374× (z -12.4) |
| [[HCT15 (line)]] | alt | 168 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -14.8) |
| [[LOX-IMVI (line)]] | wt | 125 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.302× (z -13.2) |
| [[SW1417 (line)]] | alt | 575 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.283× (z -23.2) |
| [[HepG2_C3A (line)]] | wt | 148 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.365× (z -9.5) |
| [[BT-474 (line)]] | alt | 99.0 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.285× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 120 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -10.3) |
| [[RPMI-7951 (line)]] | alt | 157 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 6.54× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.483× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 138 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.62× (z +11.3) | — |
| [[SK-MEL-2 (line)]] | alt | 143 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -14.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 81.2 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 64.2 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 33.9 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 89.3 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 39.6 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 110 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 111 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 53.1 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 385 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 411 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 45.6 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 51.7 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 34.2 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 274 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 128 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2697), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LAMA3]] | +0.63 | +0.63 / +0.62 | both halves | 7e-06 | pathway: Bacterial Infection Pathways; STRING 511 |
| [[HAS3]] | +0.56 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[IRS1]] | +0.55 | +0.48 / +0.52 | both halves | 2e-05 | pathway: HALLMARK_UV_RESPONSE_DN; STRING 862 |
| [[DSEL]] | +0.53 | +0.39 / +0.41 | both halves | 6e-05 |  |
| [[PHLDB2]] | +0.53 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[LAMC2]] | +0.51 | +0.55 / +0.50 | both halves | 1e-05 | pathway: Bacterial Infection Pathways; STRING 531 |
| [[SEMA3C]] | +0.51 | +0.44 / +0.50 | both halves | 3e-05 | STRING 423 |
| [[SFR1]] | +0.50 | +0.42 / +0.45 | both halves | 4e-05 |  |
| [[MST1R]] | +0.50 | +0.51 / +0.49 | both halves | 1e-05 | same gene group; STRING 500 |
| [[EGFR]] | +0.49 | +0.49 / +0.47 | both halves | 2e-05 | pathway: HALLMARK_GLYCOLYSIS; STRING 996 |
| [[LMO7]] | +0.48 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[GJB3]] | +0.48 | +0.51 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BTRC]] | -0.44 | -0.39 / -0.36 | both halves | 9e-05 |  |
| [[PLPP5]] | -0.43 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[GID8]] | -0.43 | -0.42 / -0.30 | both halves | 2e-04 |  |
| [[GPR107]] | -0.43 | -0.22 / -0.37 | both halves | 6e-04 |  |
| [[NUPR1]] | -0.43 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[SNHG18]] | -0.42 | -0.23 / -0.52 | both halves | 5e-04 |  |
| [[MAX]] | -0.42 | -0.33 / -0.44 | both halves | 1e-04 |  |
| [[LIN7B]] | -0.42 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[GDNF]] | -0.41 | -0.35 / -0.35 | both halves | 1e-04 | pathway: MAPK family signaling cascades |
| [[COG7]] | -0.40 | -0.28 / -0.39 | both halves | 3e-04 |  |
| [[ALKBH7]] | -0.40 | -0.30 / -0.39 | both halves | 2e-04 |  |
| [[WHAMMP2]] | -0.40 | -0.38 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*30 arrows, 30 of them with an alert ⚠; grade A 0, B 29, C 1. Shown: the 12 strongest; 18 more arrows (18 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LAMC2]] | B | LAMC2 activity raises MET's level | lines that do not express LAMC2 (27) vs lines expressing it (23) | 3.73× lower at baseline in the lines without LAMC2 | 0.001 | ⚠ within organs, on part of the lines; also absent: ENSG00000287929, TNS4, HS3ST1 |
| [[LAMA3]] | B | LAMA3 activity raises MET's level | lines that do not express LAMA3 (22) vs lines expressing it (28) | 3.65× lower at baseline in the lines without LAMA3 | 0.001 | ⚠ within organs, on part of the lines; also absent: P2RY2, ELF3, MYO5B |
| [[IL1R2]] | B | IL1R2 activity raises MET's level | lines that do not express IL1R2 (23) vs lines expressing it (27) | 2.81× lower at baseline in the lines without IL1R2 | 0.002 | ⚠ within organs, on part of the lines; also absent: TMEM139, NMRAL2P-1, NPSR1-AS1 |
| [[HS3ST1]] | B | HS3ST1 activity raises MET's level | lines that do not express HS3ST1 (31) vs lines expressing it (19) | 3.52× lower at baseline in the lines without HS3ST1 | 0.002 | ⚠ within organs, on part of the lines; also absent: KLK10, ADGRF1, TMPRSS4 |
| [[C1orf116]] | B | C1orf116 activity raises MET's level | lines that do not express C1orf116 (31) vs lines expressing it (19) | 3.42× lower at baseline in the lines without C1orf116 | 0.002 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[ABCC3]] | B | ABCC3 activity raises MET's level | lines that do not express ABCC3 (16) vs lines expressing it (34) | 3.66× lower at baseline in the lines without ABCC3 | 0.004 | ⚠ within organs, on part of the lines; also absent: AQP3, CDC42BPG, NUP62CL |
| [[COL17A1]] | B | COL17A1 activity raises MET's level | lines that do not express COL17A1 (34) vs lines expressing it (16) | 3.36× lower at baseline in the lines without COL17A1 | 0.005 | ⚠ within organs, on part of the lines; also absent: SERPINB5, GJB3, FGFBP1 |
| [[FAM83B]] | B | FAM83B activity raises MET's level | lines that do not express FAM83B (30) vs lines expressing it (20) | 2.75× lower at baseline in the lines without FAM83B | 0.007 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14 |
| [[EHF]] | B | EHF activity raises MET's level | lines that do not express EHF (27) vs lines expressing it (23) | 2.59× lower at baseline in the lines without EHF | 0.008 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, IRF6, GJB3 |
| [[C6orf141]] | B | C6orf141 activity raises MET's level | lines that do not express C6orf141 (21) vs lines expressing it (29) | 2.20× lower at baseline in the lines without C6orf141 | 0.010 | ⚠ within organs, on part of the lines; also absent: ADAM8, ENSG00000251584, SAMD12-AS1 |
| [[GJB3]] | B | GJB3 activity raises MET's level | lines that do not express GJB3 (31) vs lines expressing it (19) | 3.24× lower at baseline in the lines without GJB3 | 0.011 | ⚠ within organs, on part of the lines; also absent: IRF6, COL17A1, KLK10 |
| [[LAMA3]] | B | LAMA3 activity strengthens MET's drug response | lines that do not express LAMA3 (15) vs lines expressing it (26) | the lines without LAMA3 respond 0.63× as strongly (z diff +2.99); strongest at Topotecan (hydrochloride) 5 µM: 0.80x vs 0.44x (z diff +5.4) | 0.013 | ⚠ within organs, on part of the lines; also absent: P2RY2, ELF3, MYO5B; target measured in part of the lines; artifact flags |

### Downstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 23, C 2. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CAB39]] | B | MET activity raises CAB39's level | lines that do not express MET (9) vs lines expressing it (41) | 1.78× lower at baseline in the lines without MET | 0.004 | ⚠ within organs, on part of the lines; also absent: TGFBR2, PHLDA2, VDR |
| [[ANXA2]] | B | MET activity raises ANXA2's level | lines that do not express MET (9) vs lines expressing it (41) | 2.58× lower at baseline in the lines without MET | 0.006 | ⚠ within organs, on part of the lines; also absent: TGFBR2, PHLDA2, VDR |
| [[ABCC3]] | B | MET activity raises ABCC3's level | lines that do not express MET (9) vs lines expressing it (41) | 5.26× lower at baseline in the lines without MET | 0.008 | ⚠ within organs, on part of the lines; also absent: TGFBR2, PHLDA2, VDR |
| [[DOCK5]] | B | MET activity raises DOCK5's level | lines that do not express MET (9) vs lines expressing it (41) | 2.35× lower at baseline in the lines without MET | 0.013 | ⚠ within organs, on part of the lines; also absent: TGFBR2, PHLDA2, VDR |
| [[LINC00707]] | B | MET activity raises LINC00707's level | lines that do not express MET (9) vs lines expressing it (41) | 3.76× lower at baseline in the lines without MET | 0.019 | ⚠ within organs, on part of the lines; also absent: TGFBR2, PHLDA2, VDR |
| [[MAP3K5]] | B | MET activity raises MAP3K5's level | lines that do not express MET (9) vs lines expressing it (41) | 2.45× lower at baseline in the lines without MET | 0.019 | ⚠ within organs, on part of the lines; also absent: TGFBR2, PHLDA2, VDR |
| [[ITGA6]] | B | MET activity raises ITGA6's level | lines that do not express MET (9) vs lines expressing it (41) | 2.53× lower at baseline in the lines without MET | 0.023 | ⚠ within organs, on part of the lines; also absent: TGFBR2, PHLDA2, VDR |
| [[LAMC2]] | B | MET activity raises LAMC2's level | lines that do not express MET (9) vs lines expressing it (41) | 4.67× lower at baseline in the lines without MET | 0.038 | ⚠ within organs, on part of the lines; also absent: TGFBR2, PHLDA2, VDR |
| [[HLA-K]] | B | MET activity raises HLA-K's level | lines that do not express MET (9) vs lines expressing it (41) | 2.68× lower at baseline in the lines without MET | 0.043 | ⚠ within organs, on part of the lines; also absent: TGFBR2, PHLDA2, VDR |
| [[MYOF]] | B | MET activity raises MYOF's level | lines that do not express MET (9) vs lines expressing it (41) | 2.21× lower at baseline in the lines without MET | 0.052 | ⚠ within organs, on part of the lines; also absent: TGFBR2, PHLDA2, VDR |
| [[ABLIM1]] | B | MET activity raises ABLIM1's level | lines that do not express MET (9) vs lines expressing it (41) | 2.49× lower at baseline in the lines without MET | 0.057 | ⚠ within organs, on part of the lines; also absent: TGFBR2, PHLDA2, VDR |
| [[GPR107]] | B | MET activity raises GPR107's level | lines that do not express MET (9) vs lines expressing it (41) | 1.19× lower at baseline in the lines without MET | 0.058 | ⚠ within organs, on part of the lines; also absent: TGFBR2, PHLDA2, VDR |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.330). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (33.4, 19.4); signed map (5.3, 41.7). **Vector** length 127, 44.2% of its response variance represented; |z| ≥ 3 in 1,626 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +5.7 | +4.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~94% of this change | +5.4 | +1.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.8 | +10.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.7 | +1.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.7 | +3.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.4 | +5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | -1.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.3 | +2.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.1 | +4.7 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~17% of this change | -4.7 | -3.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.3 | -4.6 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -0.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.9 | -5.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.9 | -24.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.8 | -2.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.4 | -3.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.4 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | MET proto-oncogene, receptor tyrosine kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q31.2 — chr7:116,672,196-116,798,377 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HGFR, RCCP2, DFNB97 |
| Gene groups (HGNC) | IPT domain containing; MET proto-oncogene, receptor tyrosine kinase family |
| Hallmark sets | INFLAMMATORY_RESPONSE, UV_RESPONSE_DN, GLYCOLYSIS |
| Reactome | 36 pathways, smallest: MET activates STAT3; MET Receptor Activation; MET activates PTPN11 |
| Matched by | ensembl_id |

**Function**, from UniProt [P08581](https://www.uniprot.org/uniprotkb/P08581) (Hepatocyte growth factor receptor):

> Receptor tyrosine kinase that transduces signals from the extracellular matrix into the cytoplasm by binding to hepatocyte growth factor/HGF ligand. Regulates many physiological processes including proliferation, scattering, morphogenesis and survival. Ligand binding at the cell surface induces autophosphorylation of MET on its intracellular domain that provides docking sites for downstream signaling molecules. Following activation by ligand, interacts with the PI3-kinase subunit PIK3R1, PLCG1, …

**Summary**, from NCBI Gene [4233](https://www.ncbi.nlm.nih.gov/gene/4233):

> This gene encodes a member of the receptor tyrosine kinase family of proteins and the product of the proto-oncogene MET. The encoded preproprotein is proteolytically processed to generate alpha and beta subunits that are linked via disulfide bonds to form the mature receptor. Further processing of the beta subunit results in the formation of the M10 peptide, which has been shown to reduce lung fibrosis. Binding of its ligand, hepatocyte growth factor, induces dimerization and activation of the …

**Accessions** — [HGNC:7029](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7029) · Entrez [4233](https://www.ncbi.nlm.nih.gov/gene/4233) · UniProt [P08581](https://www.uniprot.org/uniprotkb/P08581) · Ensembl [ENSG00000105976](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105976)

## Data

Gene col 2697: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2697); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2697, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2697]; `tensor/DDL_lfc|DDL_z.npy` [2697]; `embed/gene_vectors.npy` [2697]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2697 or target_col == 2697). Every well: [[MET — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MET.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
