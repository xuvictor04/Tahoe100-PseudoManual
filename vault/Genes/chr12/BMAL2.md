---
symbol: "BMAL2"
type: "gene"
col: 388
ensembl_id: "ENSG00000029153"
name: "basic helix-loop-helix ARNT like 2"
location: "12p11.23"
module: 116
arm: "+"
pooled_cpm: 128.86
n_lines_expressing: 43
n_dd_up: 9
n_dd_down: 43
n_dd_up_clean: 5
n_dd_down_clean: 37
in_vector_space: true
direction_upstream: 12
direction_downstream: 6
tags: ["gene", "module/116"]
generated_by: "tahoemap"
---

# BMAL2

*basic helix-loop-helix ARNT like 2* — 12p11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Daptomycin (drug)]] 5 µM: 1.61× (z +6.7, q 1e-08, up in 29 of 41 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Vinblastine (sulfate) (drug)]] 5 µM: 1.30× (z +5.2, q 3e-05, up in 22 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 43 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.437× (z -11.7, q 6e-29, down in 35 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMCO2]] (+0.66, fdr 7e-06, ⚠ same locus), [[CAPN2]] (+0.65, fdr 7e-06), [[LAMC2]] (+0.65, fdr 7e-06), [[ITGB1-DT]] (+0.64, fdr 7e-06); moves opposite to [[KANTR]] (-0.53, fdr 1e-05), [[ATF2]] (-0.53, fdr 6e-05), [[GID8]] (-0.51, fdr 4e-05).
> It is in [[Module 116]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[LINC00707]] → it (grade B ⚠); 6 go from it, the strongest it → [[MIR31HG]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 388.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.61×** | +6.7 | 1e-08 | 29/41 (LS 180, HT-29, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.51×** | +5.8 | 2e-06 | 27/40 (LS 180, SW 900, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.30×** | +5.2 | 3e-05 | 22/42 (HT-29, LS 180, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.46×** | +5.1 | 4e-05 | 25/40 (LS 180, COLO 205, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.38×** | +4.3 | 0.002 | 21/37 (HOP62, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.31×** | +3.8 | 0.016 | 21/42 (SNU-423, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.27×** | +3.4 | 0.055 | 17/41 (HT-29, LS 180, …) | rises with dose |  |
| [[vincristine (drug)]] 5 µM |  | **1.56×** | +3.3 | 0.079 | 16/39 (LS 180, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.28×** | +3.2 | 0.085 | 19/40 (NCI-H460, AsPC-1, …) | all doses, flat | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 49 in all, 6 with an alert ⚠; shown: the 15 strongest. 43 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 388.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.437×** | -11.7 | 6e-29 | 35/41 (Hs 766T, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.475×** | -10.6 | 1e-23 | 38/41 (Hs 766T, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.594×** | -10.4 | 3e-23 | 32/41 (RKO, AsPC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.539×** | -8.8 | 3e-16 | 33/41 (Hs 766T, A549, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.576×** | -7.8 | 6e-13 | 30/41 (AsPC-1, NCI-H23, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.686×** | -7.6 | 4e-12 | 24/42 (A549, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[NG25 (drug)]] 5 µM |  | **0.385×** | -7.1 | 1e-10 | 34/41 (NCI-H23, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.646×** | -6.2 | 4e-08 | 28/42 (KATO III, RKO, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.638×** | -6.1 | 6e-08 | 29/41 (RKO, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.701×** | -5.0 | 3e-05 | 21/41 (HS-578T, NCI-H460, …) | all doses, flat |  |
| [[Entrectinib (drug)]] 5 µM |  | **0.711×** | -4.8 | 6e-05 | 29/41 (KATO III, A-172, …) | top dose only |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.787×** | -4.8 | 7e-05 | 25/41 (A498, A-172, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.709×** | -4.7 | 1e-04 | 25/43 (A549, PANC-1, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.719×** | -4.7 | 1e-04 | 22/41 (A498, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Ixazomib (drug)]] 5 µM |  | **0.550×** | -4.4 | 4e-04 | 28/41 (A-172, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 388. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 240 | 0 | 20 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.112× (z -18.4) |
| [[HT-29 (line)]] | alt | 115 | 7 (4 ⚠) | 4 | [[Homoharringtonine (drug)]] 0.5 µM 5.05× (z +14.4) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 2.42× (z +11.2) | [[Panobinostat (drug)]] 5 µM 0.235× (z -12.8) |
| [[NCI-H23 (line)]] | alt | 254 | 0 | 11 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -12.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.390× (z -11.8) |
| [[LS 180 (line)]] | wt | 94.9 | 6 (2 ⚠) | 3 | [[Daptomycin (drug)]] 5 µM 3.58× (z +11.5) ⚠ unreliable plate only · without an alert: [[Peretinoin (drug)]] 5 µM 3.64× (z +11.2) | [[Panobinostat (drug)]] 0.5 µM 0.325× (z -10.1) |
| [[A549 (line)]] | wt | 338 | 0 | 8 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.186× (z -18.6) |
| [[RKO (line)]] | wt | 199 | 0 | 8 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.311× (z -16.6) |
| [[KATO III (line)]] | alt | 79.8 | 2 (1 ⚠) | 5 | [[Homoharringtonine (drug)]] 0.5 µM 2.84× (z +9.7) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.51× (z +8.6) | [[Panobinostat (drug)]] 5 µM 0.255× (z -12.8) |
| [[NCI-H1573 (line)]] | alt | 301 | 0 | 7 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0272× (z -26.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.0896× (z -18.5) |
| [[PANC-1 (line)]] | alt | 268 | 0 | 7 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -13.4) |
| [[CFPAC-1 (line)]] | alt | 163 | 2 (2 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +11.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.404× (z -11.4) |
| [[SW48 (line)]] | wt | 175 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.169× (z -12.6) |
| [[Hs 766T (line)]] | wt | 312 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0835× (z -19.3) |
| [[LoVo (line)]] | wt | 119 | 1 (1 ⚠) | 4 (1 ⚠) | [[Daptomycin (drug)]] 5 µM 2.31× (z +8.5) ⚠ unreliable plate only | [[Selinexor (drug)]] 5 µM 0.406× (z -12.8) |
| [[LOX-IMVI (line)]] | wt | 268 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.179× (z -12.6) |
| [[NCI-H460 (line)]] | wt | 109 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.287× (z -10.6) |
| [[NCI-H596 (line)]] | alt | 100 | 2 | 2 (1 ⚠) | [[Methylthiouracil (drug)]] 0.05 µM 2.58× (z +11.5) | [[Pentoxifylline (drug)]] 0.05 µM 0.232× (z -17.8) ⚠ transcription drop · without an alert: [[Atazanavir (sulfate) (drug)]] 5 µM 0.370× (z -12.2) |
| [[Panc 03.27 (line)]] | alt | 266 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.175× (z -15.3) |
| [[COLO 205 (line)]] | alt | 34.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 9.23× (z +11.4) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[Peretinoin (drug)]] 5 µM 6.12× (z +8.9) | — |
| [[NCI-H1792 (line)]] | alt | 264 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.155× (z -13.5) |
| [[HOP62 (line)]] | alt | 138 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +10.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SNU-423 (line)]] | alt | 40.7 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +10.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW 900 (line)]] | alt | 77.8 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.85× (z +9.0) ⚠ cell-cycle shift, explains ~18% of this change | — |
| [[SW480 (line)]] | alt | 124 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.404× (z -11.8) |
| [[A-172 (line)]] | wt | 71.1 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.430× (z -10.6) |
| [[A-427 (line)]] | wt | 63.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.62× (z +8.7) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 60.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 50.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[J82 (line)]] | alt | 81.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.295× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change |
| [[A498 (line)]] | wt | 100 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.5 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 23.8 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 18.2 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 58.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 73.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.4 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 255 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 95.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 65.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.4 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.6 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 15.1 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 44.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 388), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMCO2]] | +0.66 | +0.63 / +0.67 | both halves | 7e-06 | STRING 656; ⚠ same locus (21.4 kb, same strand: neighbours can correlate without regulation) |
| [[CAPN2]] | +0.65 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[LAMC2]] | +0.65 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[ITGB1-DT]] | +0.64 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[MIR31HG]] | +0.64 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[NAV3]] | +0.63 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[CYFIP1]] | +0.61 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[TOMM34]] | +0.61 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[TBILA]] | +0.61 | +0.59 / +0.57 | both halves | 9e-06 |  |
| [[PLGRKT]] | +0.60 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[TNFRSF12A]] | +0.60 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[LINC00707]] | +0.59 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[EGFR]] | +0.59 | +0.54 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KANTR]] | -0.53 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[ATF2]] | -0.53 | -0.54 / -0.38 | both halves | 6e-05 | pathway: Circadian clock |
| [[GID8]] | -0.51 | -0.47 / -0.43 | both halves | 4e-05 |  |
| [[TENT2]] | -0.51 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[C12orf76]] | -0.51 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[TTC9C]] | -0.51 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[MED6]] | -0.50 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[BAG4]] | -0.50 | -0.39 / -0.58 | both halves | 5e-05 |  |
| [[FNTB]] | -0.50 | -0.39 / -0.51 | both halves | 6e-05 |  |
| [[MED23]] | -0.50 | -0.37 / -0.55 | both halves | 7e-05 |  |
| [[GALM]] | -0.50 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[COX14]] | -0.49 | -0.49 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 10, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00707]] | B | LINC00707 activity raises BMAL2's level | lines that do not express LINC00707 (26) vs lines expressing it (24) | 2.44× lower at baseline in the lines without LINC00707 | 0.003 | ⚠ within organs, on part of the lines; also absent: ENSG00000285845, ENSG00000285743, LINP1 |
| [[MIR31HG]] | B | MIR31HG activity raises BMAL2's level | lines that do not express MIR31HG (16) vs lines expressing it (34) | 3.15× lower at baseline in the lines without MIR31HG | 0.003 | ⚠ within organs, on part of the lines; also absent: SMCO2, POU5F1, PLA2R1 |
| [[CD59]] | B | CD59 activity raises BMAL2's level | lines that do not express CD59 (7) vs lines expressing it (43) | 2.35× lower at baseline in the lines without CD59 | 0.005 | ⚠ within organs, on part of the lines; also absent: C11orf91, ENSG00000284969, MET; maybe low, not absent |
| [[LINC00707]] | B | LINC00707 activity strengthens BMAL2's drug response | lines that do not express LINC00707 (20) vs lines expressing it (22) | the lines without LINC00707 respond 0.66× as strongly (z diff +1.86); strongest at Idarubicin (hydrochloride) 5 µM: 0.88x vs 0.46x (z diff +5.1) | 0.009 | ⚠ within organs, on part of the lines; also absent: ENSG00000285845, ENSG00000285743, LINP1; target measured in part of the lines; artifact flags |
| [[RAI14]] | B | RAI14 activity raises BMAL2's level | lines that do not express RAI14 (11) vs lines expressing it (39) | 1.64× lower at baseline in the lines without RAI14 | 0.048 | ⚠ within organs, on part of the lines; also absent: CCDC71L, LINC01828, ENSG00000285744; maybe low, not absent |
| [[ITGA2]] | B | ITGA2 activity raises BMAL2's level | lines that do not express ITGA2 (11) vs lines expressing it (39) | 2.41× lower at baseline in the lines without ITGA2 | 0.058 | ⚠ within organs, on part of the lines; also absent: GPR39, ATXN1-AS1, MET |
| [[ANTXR2]] | B | ANTXR2 activity raises BMAL2's level | lines that do not express ANTXR2 (10) vs lines expressing it (40) | 2.03× lower at baseline in the lines without ANTXR2 | 0.063 | ⚠ within organs, on part of the lines; also absent: RIN2, LINC01291, ST3GAL1; maybe low, not absent |
| [[GALM]] | B | GALM activity raises BMAL2's level | lines that do not express GALM (11) vs lines expressing it (39) | 2.28× lower at baseline in the lines without GALM | 0.063 | ⚠ within organs, on part of the lines; also absent: ACOT11, GRIN2D, STAP2; maybe low, not absent |
| [[ANTXR2]] | B | ANTXR2 activity strengthens BMAL2's drug response | lines that do not express ANTXR2 (8) vs lines expressing it (34) | the lines without ANTXR2 respond 0.45× as strongly (z diff +2.17); strongest at Idarubicin (hydrochloride) 5 µM: 0.97x vs 0.56x (z diff +3.9) | 0.069 | ⚠ within organs, on part of the lines; also absent: RIN2, LINC01291, ST3GAL1; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[SERPINB9]] | B | SERPINB9 activity raises BMAL2's level | lines that do not express SERPINB9 (24) vs lines expressing it (26) | 2.17× lower at baseline in the lines without SERPINB9 | 0.069 | ⚠ within organs, on part of the lines; also absent: MT1A, SHH, LINC02086 |
| [[SMCO2]] | C | SMCO2 activity raises BMAL2's level | lines that do not express SMCO2 (9) vs lines expressing it (41) | 4.34× lower at baseline in the lines without SMCO2 | 0.001 | ⚠ within organs, on part of the lines; also absent: BMAL2, MIR31HG, ITGA2; maybe low, not absent; co-absent with the target |
| [[SRPK1]] | C | SRPK1's natural level strengthens BMAL2's drug response | SRPK1's natural level across 42 lines (lineage-adjusted; a glimpse) | r +0.71, reverse -0.19; direction not clear | 0.040 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MIR31HG]] | B | BMAL2 activity raises MIR31HG's level | lines that do not express BMAL2 (7) vs lines expressing it (43) | 5.22× lower at baseline in the lines without BMAL2 | 0.084 | ⚠ within organs, on part of the lines; also absent: SMCO2, STXBP2, PDLIM1; maybe low, not absent; its own permutation p |
| [[ITGA2]] | B | BMAL2 activity raises ITGA2's level | lines that do not express BMAL2 (7) vs lines expressing it (43) | 5.10× lower at baseline in the lines without BMAL2 | 0.084 | ⚠ within organs, on part of the lines; also absent: SMCO2, STXBP2, PDLIM1; maybe low, not absent; its own permutation p |
| [[ZNF185]] | B | BMAL2 activity raises ZNF185's level | lines that do not express BMAL2 (7) vs lines expressing it (43) | 3.76× lower at baseline in the lines without BMAL2 | 0.084 | ⚠ within organs, on part of the lines; also absent: SMCO2, STXBP2, PDLIM1; maybe low, not absent |
| [[BMAL2-AS1]] | B | BMAL2 activity raises BMAL2-AS1's level | lines that do not express BMAL2 (7) vs lines expressing it (43) | 1.32× lower at baseline in the lines without BMAL2 | 0.084 | ⚠ within organs, on part of the lines; also absent: SMCO2, STXBP2, PDLIM1; maybe low, not absent; its own permutation p |
| [[NABP1]] | B | BMAL2 activity raises NABP1's level | lines that do not express BMAL2 (7) vs lines expressing it (43) | 2.32× lower at baseline in the lines without BMAL2 | 0.092 | ⚠ within organs, on part of the lines; also absent: SMCO2, STXBP2, PDLIM1; maybe low, not absent |
| [[SMCO2]] | C | BMAL2 activity raises SMCO2's level | lines that do not express BMAL2 (7) vs lines expressing it (43) | 2.69× lower at baseline in the lines without BMAL2 | 0.084 | ⚠ within organs, on part of the lines; also absent: SMCO2, STXBP2, PDLIM1; maybe low, not absent; co-absent with the target; its own permutation p |

## Where it sits

- **Module**: [[Module 116]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.687). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (39.8, 8.1); signed map (7.0, 42.8). **Vector** length 149, 52.3% of its response variance represented; |z| ≥ 3 in 1,651 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +7.6 | +6.7 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +7.2 | +5.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +7.0 | +5.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +6.7 | +5.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | +6.6 | +2.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +5.6 | +3.4 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +5.1 | +3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.8 | +2.7 |
| fall | [[NG25 (drug)]] 5 µM |  | -7.0 | -7.1 |
|  | [[Selinexor (drug)]] 5 µM |  | -6.0 | -10.4 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -4.9 | -4.8 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -4.5 | -4.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -4.4 | -6.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | -4.4 | -4.8 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -4.4 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | basic helix-loop-helix ARNT like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p11.23 — chr12:27,332,836-27,425,289 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MOP9, CLIF, PASD9, bHLHe6; previously ARNTL2 |
| Gene groups (HGNC) | Basic helix-loop-helix proteins; PAS domain containing |
| Reactome | 2 pathways, smallest: BMAL1:CLOCK,NPAS2 activates circadian expression; Circadian clock |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WYA1](https://www.uniprot.org/uniprotkb/Q8WYA1) (Basic helix-loop-helix ARNT-like protein 2):

> Transcriptional activator which forms a core component of the circadian clock. The circadian clock, an internal time-keeping system, regulates various physiological processes through the generation of approximately 24 hour circadian rhythms in gene expression, which are translated into rhythms in metabolism and behavior. It is derived from the Latin roots 'circa' (about) and 'diem' (day) and acts as an important regulator of a wide array of physiological functions including metabolism, sleep, …

**Summary**, from NCBI Gene [56938](https://www.ncbi.nlm.nih.gov/gene/56938):

> This gene encodes a basic helix-loop-helix transcription factor belonging to the PAS (PER, ARNT, SIM) superfamily. The PAS proteins play important roles in adaptation to low atmospheric and cellular oxygen levels, exposure to certain environmental pollutants, and diurnal oscillations in light and temperature. This protein forms a transcriptionally active heterodimer with the circadian CLOCK protein, the structurally related MOP4, and hypoxia-inducible factors, such as HIF1alpha. Consistent with …

**Accessions** — [HGNC:18984](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18984) · Entrez [56938](https://www.ncbi.nlm.nih.gov/gene/56938) · UniProt [Q8WYA1](https://www.uniprot.org/uniprotkb/Q8WYA1) · Ensembl [ENSG00000029153](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000029153)

## Data

Gene col 388: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 388); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 388, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 388]; `tensor/DDL_lfc|DDL_z.npy` [388]; `embed/gene_vectors.npy` [388]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 388 or target_col == 388). Every well: [[BMAL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BMAL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
