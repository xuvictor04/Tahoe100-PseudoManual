---
symbol: "UTRN"
type: "gene"
col: 7662
ensembl_id: "ENSG00000152818"
name: "utrophin"
location: "6q24.2"
module: 3
arm: "-"
pooled_cpm: 224.39
n_lines_expressing: 47
n_dd_up: 8
n_dd_down: 37
n_dd_up_clean: 8
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 2
direction_downstream: 5
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# UTRN

*utrophin* — 6q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (none with an alert); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 1.37× (z +4.6, q 0.002, up in 25 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.372× (z -14.8, q 0e+00, down in 42 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MBNL1]] (+0.71, fdr 7e-06), [[SEPTIN11]] (+0.59, fdr 2e-05), [[CAV1]] (+0.57, fdr 1e-05); moves opposite to [[VPS37C]] (-0.59, fdr 3e-05), [[PPP2R5B]] (-0.55, fdr 4e-05), [[NGLY1]] (-0.54, fdr 5e-05).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CAV1]] → it (grade B ⚠); 5 go from it, the strongest it → [[PTPN14]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7662.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +4.6 | 0.002 | 25/45 (HOP62, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.36×** | +4.5 | 0.002 | 28/44 (RKO, NCI-H23, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.33×** | +4.3 | 0.004 | 26/45 (PANC-1, NCI-H1573, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.31×** | +4.0 | 0.008 | 29/45 (HS-578T, PANC-1, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.20×** | +3.9 | 0.010 | 22/45 (SW480, HOP62, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.28×** | +3.7 | 0.023 | 23/45 (PANC-1, NCI-H1573, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.24×** | +3.2 | 0.091 | 24/44 (RKO, NCI-H23, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.24×** | +3.2 | 0.091 | 23/45 (RKO, SW 900, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | 1.23× | +3.1 | 0.11 | 22/46 (NCI-H23, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7662.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.372×** | -14.8 | 0e+00 | 42/45 (SW480, COLO 205, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.412×** | -12.7 | 1e-34 | 44/44 (HT-29, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.430×** | -12.6 | 5e-34 | 43/45 (SW480, COLO 205, …) | two highest doses | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.481×** | -10.9 | 1e-25 | 38/45 (HS-578T, SW480, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.492×** | -10.6 | 5e-24 | 42/45 (HT-29, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.572×** | -8.3 | 9e-15 | 36/45 (SW480, LoVo, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.583×** | -8.0 | 8e-14 | 39/45 (NCI-H460, LoVo, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.588×** | -7.9 | 2e-13 | 32/45 (SW480, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.601×** | -7.6 | 2e-12 | 39/45 (HT-29, NCI-H460, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.602×** | -7.1 | 5e-11 | 39/45 (HT-29, AN3 CA, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.642×** | -6.6 | 2e-09 | 32/45 (SW480, PANC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.643×** | -6.5 | 3e-09 | 38/45 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.473×** | -5.8 | 2e-07 | 35/46 (LoVo, COLO 205, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.683×** | -5.7 | 6e-07 | 29/45 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.498×** | -5.4 | 2e-06 | 36/45 (NCI-H460, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.782×** | -5.1 | 9e-06 | 30/46 (HT-29, CFPAC-1, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.521×** | -5.1 | 1e-05 | 34/45 (LoVo, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.542×** | -4.8 | 6e-05 | 34/45 (Hs 766T, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.558×** | -4.5 | 2e-04 | 32/45 (LoVo, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.629×** | -3.6 | 0.008 | 26/45 (RKO, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vilanterol (drug)]] 5 µM |  | 0.845× | -3.5 | 0.010 | 16/46 (LOX-IMVI, HOP62, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7662. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 254 | 3 (1 ⚠) | 22 (12 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.34× (z +13.7) | [[Panobinostat (drug)]] 5 µM 0.148× (z -21.6) |
| [[LoVo (line)]] | wt | 280 | 1 | 16 (12 ⚠) | [[BAY1125976 (drug)]] 5 µM 4.49× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -20.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.267× (z -16.9) |
| [[NCI-H460 (line)]] | wt | 205 | 0 | 12 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.266× (z -17.4) |
| [[PANC-1 (line)]] | alt | 355 | 1 | 11 (6 ⚠) | [[Clobetasol propionate (drug)]] 0.05 µM 1.98× (z +8.6) | [[Digitoxin (drug)]] 5 µM 0.327× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.351× (z -13.1) |
| [[NCI-H1792 (line)]] | alt | 192 | 0 | 11 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.259× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.284× (z -14.8) |
| [[HT-29 (line)]] | alt | 430 | 0 | 10 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.142× (z -17.5) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.217× (z -14.2) |
| [[COLO 205 (line)]] | alt | 297 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -28.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.120× (z -19.7) |
| [[NCI-H2030 (line)]] | alt | 637 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -16.2) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.331× (z -11.7) |
| [[SW48 (line)]] | wt | 255 | 0 | 7 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.268× (z -9.9) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.288× (z -9.7) |
| [[Hs 766T (line)]] | wt | 369 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.169× (z -17.1) |
| [[A498 (line)]] | wt | 175 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.243× (z -16.9) |
| [[HepG2_C3A (line)]] | wt | 293 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -15.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.349× (z -10.7) |
| [[HS-578T (line)]] | alt | 258 | 1 | 4 (1 ⚠) | [[Clobetasol propionate (drug)]] 5 µM 2.18× (z +8.7) | [[Panobinostat (drug)]] 0.5 µM 0.201× (z -17.8) |
| [[J82 (line)]] | alt | 291 | 1 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +8.8) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 0.5 µM 0.289× (z -14.0) |
| [[SW 900 (line)]] | alt | 155 | 0 | 5 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.305× (z -13.1) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.446× (z -9.3) |
| [[A-172 (line)]] | wt | 212 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.277× (z -15.7) |
| [[BT-474 (line)]] | alt | 137 | 3 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.66× (z +20.8) ⚠ cell-cycle shift, would explain all of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.392× (z -8.6) ⚠ toxic |
| [[C32 (line)]] | wt | 467 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.486× (z -10.5) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.426× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 415 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.292× (z -16.8) |
| [[NCI-H23 (line)]] | alt | 123 | 3 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +19.7) ⚠ cell-cycle shift, would explain all of this change | [[Ixazomib citrate (drug)]] 5 µM 0.389× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 158 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.357× (z -11.6) |
| [[RKO (line)]] | wt | 140 | 3 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +12.2) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 2.89× (z +10.6) | [[Digitoxin (drug)]] 5 µM 0.423× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SNU-423 (line)]] | alt | 377 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.244× (z -15.3) |
| [[A-427 (line)]] | wt | 252 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.278× (z -16.4) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.389× (z -12.6) |
| [[A549 (line)]] | wt | 145 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.317× (z -10.9) |
| [[MIA PaCa-2 (line)]] | alt | 129 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +18.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SK-MEL-2 (line)]] | alt | 195 | 1 (1 ⚠) | 2 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.37× (z +9.6) ⚠ cell-cycle shift, explains ~43% of this change | [[Panobinostat (drug)]] 0.5 µM 0.371× (z -11.5) |
| [[HCT15 (line)]] | alt | 251 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.374× (z -9.4) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.391× (z -9.3) |
| [[LOX-IMVI (line)]] | wt | 175 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +8.5) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 0.5 µM 0.350× (z -9.7) |
| [[LS 180 (line)]] | wt | 88.6 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.10× (z +10.2) | — |
| [[RPMI-7951 (line)]] | alt | 269 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +14.8) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 0.5 µM 0.425× (z -8.9) |
| [[AN3 CA (line)]] | alt | 620 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.260× (z -11.0) |
| [[CFPAC-1 (line)]] | alt | 171 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 122 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.385× (z -9.7) ⚠ cell-cycle shift, explains ~43% of this change |
| [[KATO III (line)]] | alt | 104 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.353× (z -9.6) |
| [[SNU-1 (line)]] | wt | 115 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.164× (z -14.7) ⚠ toxic |
| [[SW 1088 (line)]] | alt | 230 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.134× (z -9.5) |
| [[SW 1271 (line)]] | alt | 381 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.117× (z -12.9) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 22.7 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 88.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 71.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 110 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 205 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 86.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 202 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 556 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.3 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 31.4 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7662), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MBNL1]] | +0.71 | +0.59 / +0.71 | both halves | 7e-06 |  |
| [[SEPTIN11]] | +0.59 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[CAV1]] | +0.57 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[PPP3CA]] | +0.55 | +0.50 / +0.63 | both halves | 1e-05 | STRING 576 |
| [[OXCT1]] | +0.55 | +0.50 / +0.41 | both halves | 4e-05 |  |
| [[HNRNPK]] | +0.55 | +0.38 / +0.45 | both halves | 7e-05 |  |
| [[HNRNPH3]] | +0.55 | +0.46 / +0.38 | both halves | 7e-05 |  |
| [[ADGRG6]] | +0.54 | +0.30 / +0.58 | both halves | 2e-04 | pathway: EGR2 and SOX10-mediated initiation of Schwann cell myelination |
| [[YAP1]] | +0.54 | +0.38 / +0.46 | both halves | 7e-05 | pathway: EGR2 and SOX10-mediated initiation of Schwann cell myelination |
| [[NID1]] | +0.54 | +0.39 / +0.51 | both halves | 5e-05 | pathway: Extracellular matrix organization; STRING 488 |
| [[NAB1]] | +0.53 | +0.50 / +0.48 | both halves | 2e-05 | pathway: EGR2 and SOX10-mediated initiation of Schwann cell myelination |
| [[RDX]] | +0.53 | +0.50 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS37C]] | -0.59 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[PPP2R5B]] | -0.55 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[NGLY1]] | -0.54 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[RPP21]] | -0.53 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[CYB561D1]] | -0.53 | -0.38 / -0.47 | both halves | 7e-05 |  |
| [[KXD1]] | -0.52 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[PIGU]] | -0.51 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[HSDL1]] | -0.51 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[VRK3]] | -0.50 | -0.49 / -0.38 | both halves | 7e-05 |  |
| [[NEIL2]] | -0.50 | -0.38 / -0.38 | both halves | 7e-05 |  |
| [[ATAT1]] | -0.50 | -0.37 / -0.45 | both halves | 7e-05 |  |
| [[CIAO2B]] | -0.50 | -0.39 / -0.43 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CAV1]] | B | CAV1 activity raises UTRN's level | lines that do not express CAV1 (13) vs lines expressing it (37) | 1.66× lower at baseline in the lines without CAV1 | 0.066 | ⚠ within organs, on part of the lines; also absent: AFAP1L1, MDFIC, CACNG6 |
| [[TOP2B]] | B | TOP2B activity lowers UTRN's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTPN14]] | C | UTRN activity raises PTPN14's level | lines that do not express UTRN (3) vs lines expressing it (47) | 2.64× lower at baseline in the lines without UTRN | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ENSG00000286162, CLEC2D, MPP4; its own permutation p |
| [[ROCK2]] | C | UTRN activity lowers ROCK2's level | lines that do not express UTRN (3) vs lines expressing it (47) | 1.94× higher at baseline in the lines without UTRN | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ENSG00000286162, CLEC2D, MPP4; its own permutation p |
| [[LCMT1]] | C | UTRN activity lowers LCMT1's level | lines that do not express UTRN (3) vs lines expressing it (47) | 1.57× higher at baseline in the lines without UTRN | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ENSG00000286162, CLEC2D, MPP4; its own permutation p |
| [[ADGRG6]] | C | UTRN activity raises ADGRG6's level | lines that do not express UTRN (3) vs lines expressing it (47) | 2.41× lower at baseline in the lines without UTRN | 0.085 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ENSG00000286162, CLEC2D, MPP4 |
| [[WNK1]] | C | UTRN activity raises WNK1's level | lines that do not express UTRN (3) vs lines expressing it (47) | 1.75× lower at baseline in the lines without UTRN | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ENSG00000286162, CLEC2D, MPP4; its own permutation p |

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.516). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-50.2, 20.9); signed map (20.8, -35.0). **Vector** length 116, 38.8% of its response variance represented; |z| ≥ 3 in 1,942 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.8 | +3.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.8 | +3.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +4.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +4.0 | +4.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +3.9 | -4.5 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +3.5 | +2.9 |
|  | [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | +3.3 | +2.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.2 | +4.3 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -11.3 | -12.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -7.4 | -14.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | -6.8 | -12.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -6.0 | -10.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.9 | -8.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.6 | -5.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.4 | -5.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.3 | -5.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.2 | -4.5 |
|  | [[EX229 (drug)]] 5 µM |  | -3.9 | -4.8 |

## What is on record

|  |  |
|---|---|
| Name | utrophin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q24.2 — chr6:144,285,335-144,853,034 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DRP, DRP1; previously DMDL |
| Gene groups (HGNC) | Zinc fingers ZZ-type; Spectrin repeat containing |
| Reactome | 5 pathways, smallest: EGR2 and SOX10-mediated initiation of Schwann cell myelination; Formation of the dystrophin-glycoprotein complex (DGC); Non-integrin membrane-ECM interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [P46939](https://www.uniprot.org/uniprotkb/P46939) (Utrophin):

> May play a role in anchoring the cytoskeleton to the plasma membrane.

**Summary**, from NCBI Gene [7402](https://www.ncbi.nlm.nih.gov/gene/7402):

> This gene shares both structural and functional similarities with the dystrophin gene. It contains an actin-binding N-terminus, a triple coiled-coil repeat central region, and a C-terminus that consists of protein-protein interaction motifs which interact with dystroglycan protein components. The protein encoded by this gene is located at the neuromuscular synapse and myotendinous junctions, where it participates in post-synaptic membrane maintenance and acetylcholine receptor clustering. Mouse …

**Accessions** — [HGNC:12635](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12635) · Entrez [7402](https://www.ncbi.nlm.nih.gov/gene/7402) · UniProt [P46939](https://www.uniprot.org/uniprotkb/P46939) · Ensembl [ENSG00000152818](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152818)

## Data

Gene col 7662: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7662); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7662, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7662]; `tensor/DDL_lfc|DDL_z.npy` [7662]; `embed/gene_vectors.npy` [7662]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7662 or target_col == 7662). Every well: [[UTRN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UTRN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
