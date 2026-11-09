---
symbol: "ZC3H12C"
type: "gene"
col: 7360
ensembl_id: "ENSG00000149289"
name: "zinc finger CCCH-type containing 12C"
location: "11q22.3"
module: 219
arm: "+"
pooled_cpm: 99.61
n_lines_expressing: 43
n_dd_up: 14
n_dd_down: 17
n_dd_up_clean: 13
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 7
direction_downstream: 6
tags: ["gene", "module/219"]
generated_by: "tahoemap"
---

# ZC3H12C

*zinc finger CCCH-type containing 12C* — 11q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.07× (z +22.9, q 0e+00, up in 40 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.277× (z -18.5, q 0e+00, down in 41 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZBTB38]] (+0.72, fdr 7e-06), [[HIVEP2]] (+0.70, fdr 1e-05), [[HELQ]] (+0.67, fdr 1e-05); moves opposite to [[TM9SF2]] (-0.63, fdr 1e-05), [[SCAI]] (-0.63, fdr 1e-05), [[MOSPD3]] (-0.62, fdr 1e-05).
> It is in [[Module 219]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[FJX1]] → it (grade B ⚠); 6 go from it, the strongest it → [[NEPRO-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 1 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7360.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.07×** | +22.9 | 0e+00 | 40/41 (HOP62, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.89×** | +18.2 | 0e+00 | 38/41 (LoVo, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.26×** | +11.8 | 1e-29 | 37/41 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.96×** | +10.4 | 4e-23 | 35/42 (LoVo, HS-578T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.98×** | +9.9 | 6e-21 | 35/41 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **1.36×** | +4.5 | 6e-04 | 28/42 (HOP62, J82, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.35×** | +4.4 | 0.001 | 28/41 (HOP62, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.31×** | +3.6 | 0.023 | 19/41 (NCI-H2347, HS-578T, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.28×** | +3.6 | 0.023 | 20/41 (A-172, HS-578T, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.28×** | +3.5 | 0.024 | 18/42 (HT-29, SW1417, …) | two highest doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.26×** | +3.4 | 0.034 | 17/41 (HOP62, NCI-H2347, …) | inconsistent across doses |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.55×** | +3.3 | 0.046 | 19/41 (Hs 766T, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM |  | **1.24×** | +3.1 | 0.083 | 17/41 (NCI-H460, SW 1088, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Amsacrine (drug)]] 5 µM |  | 1.16× | +3.1 | 0.083 | 13/41 (HOP62, J82, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.50×** | +3.1 | 0.083 | 17/41 (RPMI-7951, HS-578T, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7360.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.277×** | -18.5 | 0e+00 | 41/41 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.304×** | -17.1 | 0e+00 | 40/41 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.388×** | -13.6 | 5e-40 | 40/41 (SW480, C-33 A, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.489×** | -9.5 | 2e-19 | 30/39 (SHP-77, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.537×** | -8.9 | 4e-17 | 36/41 (SW 900, SK-MEL-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.543×** | -8.8 | 2e-16 | 26/42 (NCI-H1573, NCI-H460, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.586×** | -7.1 | 1e-10 | 20/37 (PANC-1, A498, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.738×** | -6.2 | 5e-08 | 25/42 (A549, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **0.712×** | -4.9 | 7e-05 | 26/41 (SW 900, SW 1271, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.714×** | -4.8 | 7e-05 | 25/41 (SW480, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.748×** | -4.2 | 0.002 | 23/41 (BT-474, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.579×** | -4.1 | 0.002 | 21/39 (SW 900, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.583×** | -4.1 | 0.002 | 23/40 (NCI-H460, H4, …) | top dose only | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.777×** | -3.6 | 0.012 | 23/41 (PANC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | 0.845× | -3.4 | 0.025 | 13/41 (C32, RKO, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.800×** | -3.2 | 0.046 | 21/41 (SW48, HepG2/C3A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7360. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 98.1 | 4 | 12 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.64× (z +22.5) | [[Dinaciclib (drug)]] 0.05 µM 0.280× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.349× (z -10.9) |
| [[A-172 (line)]] | wt | 109 | 7 (2 ⚠) | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.59× (z +22.9) | [[Dinaciclib (drug)]] 0.5 µM 0.276× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.286× (z -11.7) |
| [[H4 (line)]] | wt | 129 | 5 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.03× (z +18.9) | [[Panobinostat (drug)]] 0.5 µM 0.218× (z -11.4) |
| [[HOP62 (line)]] | alt | 42.0 | 10 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +27.5) | — |
| [[HS-578T (line)]] | alt | 97.9 | 7 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 6.41× (z +22.3) | [[Panobinostat (drug)]] 0.5 µM 0.310× (z -10.0) |
| [[A498 (line)]] | wt | 143 | 4 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +13.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -11.7) |
| [[BT-474 (line)]] | alt | 65.7 | 6 (4 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 9.07× (z +21.4) | [[Panobinostat (drug)]] 5 µM 0.248× (z -9.6) |
| [[LoVo (line)]] | wt | 88.0 | 5 | 3 | [[Harringtonine (drug)]] 5 µM 8.85× (z +20.4) | [[Panobinostat (drug)]] 5 µM 0.231× (z -14.8) |
| [[SNU-423 (line)]] | alt | 173 | 3 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +16.0) | [[Panobinostat (drug)]] 0.5 µM 0.209× (z -13.2) |
| [[HEC-1-A (line)]] | alt | 105 | 2 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +11.3) | [[Panobinostat (drug)]] 5 µM 0.264× (z -14.3) |
| [[SK-MEL-2 (line)]] | alt | 75.6 | 3 | 4 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +13.4) | [[Panobinostat (drug)]] 0.5 µM 0.138× (z -17.0) |
| [[SW 900 (line)]] | alt | 310 | 1 | 6 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 3.17× (z +10.5) | [[Panobinostat (drug)]] 5 µM 0.257× (z -12.4) |
| [[SW480 (line)]] | alt | 49.7 | 2 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +16.2) | [[Panobinostat (drug)]] 0.5 µM 0.181× (z -21.6) |
| [[Hs 766T (line)]] | wt | 155 | 2 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +12.0) | [[Panobinostat (drug)]] 0.5 µM 0.216× (z -11.5) |
| [[NCI-H460 (line)]] | wt | 158 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.211× (z -15.2) |
| [[Panc 03.27 (line)]] | alt | 135 | 3 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +15.5) | [[Lonafarnib (drug)]] 5 µM 0.103× (z -9.5) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.341× (z -8.6) |
| [[RPMI-7951 (line)]] | alt | 154 | 4 | 2 | [[Harringtonine (drug)]] 5 µM 7.52× (z +15.6) | [[Panobinostat (drug)]] 0.5 µM 0.275× (z -10.8) |
| [[SW48 (line)]] | wt | 44.7 | 4 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.20× (z +15.1) | [[Panobinostat (drug)]] 5 µM 0.136× (z -11.8) |
| [[J82 (line)]] | alt | 94.3 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.52× (z +19.4) | [[Panobinostat (drug)]] 5 µM 0.379× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 79.3 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +14.0) | [[Panobinostat (drug)]] 0.5 µM 0.159× (z -17.1) |
| [[NCI-H1792 (line)]] | alt | 379 | 1 | 4 | [[Harringtonine (drug)]] 5 µM 3.40× (z +10.0) | [[Panobinostat (drug)]] 5 µM 0.193× (z -14.4) |
| [[A549 (line)]] | wt | 245 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.216× (z -14.2) |
| [[C-33 A (line)]] | alt | 70.1 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +8.6) | [[Panobinostat (drug)]] 5 µM 0.122× (z -15.9) |
| [[C32 (line)]] | wt | 35.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.85× (z +18.9) | — |
| [[CFPAC-1 (line)]] | alt | 177 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.31× (z +24.2) | [[Dinaciclib (drug)]] 0.05 µM 0.199× (z -12.0) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 176 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.33× (z +20.6) | [[Dinaciclib (drug)]] 0.5 µM 0.309× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[NCI-H2347 (line)]] | alt | 85.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.73× (z +18.6) | — |
| [[SW 1271 (line)]] | alt | 202 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +9.0) | [[Panobinostat (drug)]] 0.5 µM 0.0807× (z -12.6) |
| [[A-427 (line)]] | wt | 35.2 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.297× (z -9.1) |
| [[HCT15 (line)]] | alt | 74.6 | 2 | 1 | [[Harringtonine (drug)]] 5 µM 4.36× (z +10.0) | [[Panobinostat (drug)]] 5 µM 0.295× (z -8.9) |
| [[HepG2_C3A (line)]] | wt | 54.7 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.43× (z +16.7) | [[Dinaciclib (drug)]] 0.5 µM 0.295× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[HT-29 (line)]] | alt | 45.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.6× (z +26.2) | — |
| [[NCI-H1573 (line)]] | alt | 117 | 1 | 2 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 3.42× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.125× (z -18.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[NCI-H2030 (line)]] | alt | 76.6 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +12.8) | [[Panobinostat (drug)]] 0.5 µM 0.340× (z -8.8) |
| [[RKO (line)]] | wt | 122 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.170× (z -17.6) |
| [[SW 1088 (line)]] | alt | 88.3 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.85× (z +9.0) | [[Ribociclib (drug)]] 0.5 µM 0.0603× (z -9.4) ⚠ unreliable plate only |
| [[NCI-H23 (line)]] | alt | 31.6 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.265× (z -10.0) |
| [[SNU-1 (line)]] | wt | 81.1 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.172× (z -12.6) |
| [[SW1417 (line)]] | alt | 48.1 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 2.22× (z +8.8) | [[Panobinostat (drug)]] 0.5 µM 0.304× (z -9.5) |
| [[SHP-77 (line)]] | alt | 86.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.257× (z -12.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 13.6 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 9.06 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 59.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.5 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 6.16 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 7.78 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 20.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 81.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.99 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7360), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBTB38]] | +0.72 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[HIVEP2]] | +0.70 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[HELQ]] | +0.67 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[ZNF620]] | +0.67 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[LACC1]] | +0.66 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[CSF3]] | +0.65 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[ST7L]] | +0.64 | +0.65 / +0.45 | both halves | 3e-05 |  |
| [[ZNF641]] | +0.64 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[PIGV]] | +0.63 | +0.70 / +0.40 | both halves | 4e-05 |  |
| [[TANK]] | +0.63 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[UTP3]] | +0.62 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[WAKMAR2]] | +0.62 | +0.67 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TM9SF2]] | -0.63 | -0.64 / -0.54 | both halves | 1e-05 |  |
| [[SCAI]] | -0.63 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[MOSPD3]] | -0.62 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[IGSF8]] | -0.61 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[CBFA2T2]] | -0.61 | -0.63 / -0.46 | both halves | 3e-05 |  |
| [[SDHAP1]] | -0.60 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[HSPA5]] | -0.60 | -0.62 / -0.46 | both halves | 2e-05 |  |
| [[GET1]] | -0.60 | -0.62 / -0.42 | both halves | 4e-05 |  |
| [[ILRUN]] | -0.60 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[GNB2]] | -0.59 | -0.60 / -0.41 | both halves | 4e-05 |  |
| [[SDHAP4]] | -0.59 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[SLC9A6]] | -0.59 | -0.53 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FJX1]] | B | FJX1 activity raises ZC3H12C's level | lines that do not express FJX1 (11) vs lines expressing it (39) | 3.78× lower at baseline in the lines without FJX1 | 0.001 | ⚠ within organs, on part of the lines; also absent: DYNC2H1, GIHCG, HDGFL3 |
| [[NALCN]] | B | NALCN activity raises ZC3H12C's level | lines that do not express NALCN (22) vs lines expressing it (28) | 2.69× lower at baseline in the lines without NALCN | 0.018 | ⚠ within organs, on part of the lines; also absent: STAC, EDIL3-DT, ZNF229 |
| [[ADAMTS9]] | B | ADAMTS9 activity raises ZC3H12C's level | lines that do not express ADAMTS9 (18) vs lines expressing it (32) | 2.48× lower at baseline in the lines without ADAMTS9 | 0.027 | ⚠ within organs, on part of the lines; also absent: PRICKLE2, FRMPD4, ADAMTS9-AS2 |
| [[NID2]] | B | NID2 activity raises ZC3H12C's level | lines that do not express NID2 (32) vs lines expressing it (18) | 2.44× lower at baseline in the lines without NID2 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C5orf46, LINC01411, COL4A1 |
| [[KLHL5]] | B | KLHL5 activity raises ZC3H12C's level | lines that do not express KLHL5 (7) vs lines expressing it (43) | 3.79× lower at baseline in the lines without KLHL5 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: SLC36A4, CCDC3, CSRP2 |
| [[PLPP3]] | B | PLPP3 activity raises ZC3H12C's level | lines that do not express PLPP3 (5) vs lines expressing it (45) | 2.64× lower at baseline in the lines without PLPP3 | 0.071 | ⚠ within organs, on part of the lines; also absent: ENSG00000284686; maybe low, not absent |
| [[PLPP4]] | B | PLPP4 activity raises ZC3H12C's level | lines that do not express PLPP4 (31) vs lines expressing it (19) | 2.26× lower at baseline in the lines without PLPP4 | 0.084 | ⚠ within organs, on part of the lines; also absent: GYPC, LINC02930, TNFAIP6 |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NEPRO-AS1]] | B | ZC3H12C activity raises NEPRO-AS1's level | lines that do not express ZC3H12C (7) vs lines expressing it (43) | 2.27× lower at baseline in the lines without ZC3H12C | 0.012 | ⚠ within organs, on part of the lines; also absent: TMOD2, KLF12, DPF1 |
| [[HIVEP2]] | B | ZC3H12C activity raises HIVEP2's level | lines that do not express ZC3H12C (7) vs lines expressing it (43) | 1.71× lower at baseline in the lines without ZC3H12C | 0.024 | ⚠ within organs, on part of the lines; also absent: TMOD2, KLF12, DPF1 |
| [[NALCN]] | B | ZC3H12C activity raises NALCN's level | lines that do not express ZC3H12C (7) vs lines expressing it (43) | 4.10× lower at baseline in the lines without ZC3H12C | 0.037 | ⚠ within organs, on part of the lines; also absent: TMOD2, KLF12, DPF1 |
| [[KLHL5]] | B | ZC3H12C activity raises KLHL5's level | lines that do not express ZC3H12C (7) vs lines expressing it (43) | 3.10× lower at baseline in the lines without ZC3H12C | 0.048 | ⚠ within organs, on part of the lines; also absent: TMOD2, KLF12, DPF1 |
| [[FJX1]] | B | ZC3H12C activity raises FJX1's level | lines that do not express ZC3H12C (7) vs lines expressing it (43) | 2.08× lower at baseline in the lines without ZC3H12C | 0.067 | ⚠ within organs, on part of the lines; also absent: TMOD2, KLF12, DPF1 |
| [[UTP3]] | B | ZC3H12C activity raises UTP3's level | lines that do not express ZC3H12C (7) vs lines expressing it (43) | 1.14× lower at baseline in the lines without ZC3H12C | 0.080 | ⚠ within organs, on part of the lines; also absent: TMOD2, KLF12, DPF1 |

## Where it sits

- **Module**: [[Module 219]]; 11 genes; every member is in the + arm (projection on the module's main direction 0.779). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.44; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.4, 9.6); signed map (16.7, -9.4). **Vector** length 136, 45.0% of its response variance represented; |z| ≥ 3 in 1,350 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +13.7 | +18.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +11.2 | +9.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +10.5 | +11.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +10.2 | +22.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +5.9 | +4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.4 | +3.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.7 | +3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | +2.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | +3.7 | +3.1 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -6.5 | -18.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -6.4 | -17.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -6.2 | -13.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.1 | -8.9 |
|  | [[NG25 (drug)]] 5 µM |  | -4.6 | -4.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.9 | -2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.5 | -2.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.5 | -2.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger CCCH-type containing 12C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q22.3 — chr11:110,093,392-110,171,841 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1726, MCPIP3 |
| Gene groups (HGNC) | Zinc fingers CCCH-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9C0D7](https://www.uniprot.org/uniprotkb/Q9C0D7) (Probable ribonuclease ZC3H12C):

> May function as RNase and regulate the levels of target RNA species.

**Summary**, from NCBI Gene [85463](https://www.ncbi.nlm.nih.gov/gene/85463):

> Predicted to enable RNA endonuclease activity and mRNA binding activity. Predicted to be involved in 3'-UTR-mediated mRNA destabilization. Predicted to be active in cytoplasmic ribonucleoprotein granule and nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29362](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29362) · Entrez [85463](https://www.ncbi.nlm.nih.gov/gene/85463) · UniProt [Q9C0D7](https://www.uniprot.org/uniprotkb/Q9C0D7) · Ensembl [ENSG00000149289](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149289)

## Data

Gene col 7360: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7360); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7360, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7360]; `tensor/DDL_lfc|DDL_z.npy` [7360]; `embed/gene_vectors.npy` [7360]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7360 or target_col == 7360). Every well: [[ZC3H12C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZC3H12C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
