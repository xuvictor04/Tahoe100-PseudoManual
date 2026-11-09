---
symbol: "ZC3HAV1"
type: "gene"
col: 2690
ensembl_id: "ENSG00000105939"
name: "zinc finger CCCH-type containing, antiviral 1"
location: "7q34"
module: 32
arm: "+"
pooled_cpm: 304.05
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 30
n_dd_up_clean: 5
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 38
direction_downstream: 0
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# ZC3HAV1

*zinc finger CCCH-type containing, antiviral 1* — 7q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 2.20× (z +8.2, q 1e-13, up in 30 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.285× (z -25.0, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RIGI]] (+0.88, fdr 7e-06), [[PARP14]] (+0.87, fdr 7e-06), [[IFIT3]] (+0.87, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 38 arrows point to it, the strongest [[PLAAT4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2690.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.20×** | +8.2 | 1e-13 | 30/49 (NCI-H460, NCI-H2030, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.48×** | +7.9 | 1e-12 | 26/48 (HEC-1-A, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[venetoclax (drug)]] 0.05 µM |  | **1.30×** | +5.0 | 1e-04 | 27/49 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.59×** | +4.9 | 2e-04 | 25/48 (LS 180, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[OTS514 (drug)]] 5 µM |  | **1.51×** | +4.3 | 0.002 | 23/46 (PANC-1, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 1.15× | +4.1 | 0.005 | 21/49 (AsPC-1, RKO, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.13× | +3.5 | 0.029 | 16/48 (RKO, SW1417, …) | top dose only |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 1.19× | +3.5 | 0.029 | 11/48 (RKO, NCI-H1573, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.3 | 0.069 | 22/48 (HEC-1-A, NCI-H460, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.17× | +3.1 | 0.081 | 12/49 (AsPC-1, Panc 03.27, …) | all doses, flat | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 1.18× | +3.1 | 0.081 | 17/50 (C32, PANC-1, …) | top dose only |  |
| [[Omeprazole (drug)]] 0.05 µM |  | 1.17× | +3.1 | 0.081 | 16/48 (A-172, H4, …) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.11× | +3.1 | 0.083 | 5/48 (A-172, SW 1271, …) | top dose only |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 1.16× | +3.1 | 0.090 | 14/48 (A498, C32, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 1.16× | +3.0 | 0.093 | 14/48 (A-172, SW1417, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.17× | +3.0 | 0.093 | 16/47 (J82, AsPC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 56 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2690.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.285×** | -25.0 | 0e+00 | 48/48 (NCI-H23, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.320×** | -22.6 | 0e+00 | 48/48 (NCI-H23, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.371×** | -19.7 | 0e+00 | 47/48 (NCI-H23, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.665×** | -11.4 | 5e-28 | 32/49 (NCI-H23, C-33 A, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.612×** | -9.7 | 3e-20 | 34/49 (NCI-H23, A549, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.618×** | -9.5 | 2e-19 | 31/49 (LoVo, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.626×** | -9.3 | 1e-18 | 41/48 (SNU-423, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.729×** | -8.9 | 6e-17 | 36/49 (A-172, RKO, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.632×** | -8.7 | 2e-16 | 32/47 (RKO, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.647×** | -8.6 | 4e-16 | 32/48 (NCI-H23, SNU-423, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.662×** | -8.2 | 1e-14 | 39/48 (NCI-H23, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.746×** | -8.2 | 1e-14 | 31/49 (C-33 A, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.754×** | -7.9 | 1e-13 | 32/48 (NCI-H1573, A549, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.687×** | -7.4 | 4e-12 | 29/49 (C-33 A, SNU-423, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.706×** | -6.9 | 2e-10 | 34/48 (NCI-H23, H4, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.718×** | -6.6 | 2e-09 | 33/48 (LoVo, SNU-423, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.544×** | -6.3 | 9e-09 | 36/49 (SNU-423, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.735×** | -6.1 | 4e-08 | 28/48 (H4, NCI-H460, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2690. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 313 | 0 | 16 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -28.2) ⚠ cell-cycle shift, explains ~11% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.204× (z -17.5) |
| [[NCI-H460 (line)]] | wt | 1,026 | 9 (6 ⚠) | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.62× (z +24.7) ⚠ cell-cycle shift, explains ~11% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 13.9× (z +15.7) | [[Panobinostat (drug)]] 5 µM 0.315× (z -13.1) |
| [[NCI-H23 (line)]] | alt | 231 | 0 | 15 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.106× (z -22.9) |
| [[SNU-423 (line)]] | alt | 245 | 0 | 14 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.170× (z -21.4) |
| [[HEC-1-A (line)]] | alt | 185 | 9 (6 ⚠) | 3 | [[Homoharringtonine (drug)]] 0.5 µM 5.10× (z +18.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 4.78× (z +18.0) | [[Panobinostat (drug)]] 5 µM 0.288× (z -14.2) |
| [[RKO (line)]] | wt | 247 | 2 (1 ⚠) | 9 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +12.6) ⚠ cell-cycle shift, explains ~9% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.57× (z +10.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.249× (z -15.0) ⚠ toxic · without an alert: [[Tofacitinib (citrate) (drug)]] 5 µM 0.525× (z -10.2) |
| [[LoVo (line)]] | wt | 556 | 0 | 9 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.237× (z -15.8) |
| [[C-33 A (line)]] | alt | 303 | 0 | 8 | — | [[Belinostat (drug)]] 5 µM 0.142× (z -19.4) |
| [[J82 (line)]] | alt | 254 | 6 (4 ⚠) | 2 | [[Ixazomib citrate (drug)]] 5 µM 3.37× (z +11.5) ⚠ cell-cycle shift, explains ~12% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.99× (z +10.4) | [[Panobinostat (drug)]] 5 µM 0.355× (z -9.7) |
| [[LS 180 (line)]] | wt | 298 | 4 (2 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +14.6) ⚠ cell-cycle shift, explains ~11% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 9.05× (z +10.3) | [[Panobinostat (drug)]] 5 µM 0.237× (z -12.8) |
| [[A-172 (line)]] | wt | 540 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.133× (z -14.7) |
| [[AsPC-1 (line)]] | alt | 283 | 2 (2 ⚠) | 5 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +13.5) ⚠ cell-cycle shift, explains ~9% of this change | [[Panobinostat (drug)]] 5 µM 0.288× (z -14.5) |
| [[NCI-H1573 (line)]] | alt | 137 | 0 | 7 | — | [[Selinexor (drug)]] 5 µM 0.382× (z -13.7) |
| [[COLO 205 (line)]] | alt | 259 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.182× (z -14.0) |
| [[HOP62 (line)]] | alt | 128 | 4 (3 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 5.81× (z +18.8) ⚠ cell-cycle shift, explains ~11% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 9.46× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.216× (z -11.5) |
| [[HS-578T (line)]] | alt | 293 | 1 | 5 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 3.30× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.138× (z -14.0) |
| [[KATO III (line)]] | alt | 207 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.249× (z -14.8) |
| [[MIA PaCa-2 (line)]] | alt | 354 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.235× (z -12.9) |
| [[NCI-H2347 (line)]] | alt | 260 | 1 | 5 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.33× (z +10.0) | [[Panobinostat (drug)]] 0.5 µM 0.396× (z -11.0) |
| [[CFPAC-1 (line)]] | alt | 338 | 1 (1 ⚠) | 4 | [[Harringtonine (drug)]] 5 µM 2.72× (z +10.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.406× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 246 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.92× (z +24.6) ⚠ cell-cycle shift, explains ~11% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 15.0× (z +12.7) | — |
| [[SK-MEL-2 (line)]] | alt | 195 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.256× (z -12.2) |
| [[SW480 (line)]] | alt | 120 | 2 (1 ⚠) | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.75× (z +11.1) ⚠ cell-cycle shift, explains ~9% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.13× (z +10.6) | [[Panobinostat (drug)]] 5 µM 0.273× (z -18.0) |
| [[H4 (line)]] | wt | 579 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.167× (z -10.0) |
| [[Hs 766T (line)]] | wt | 609 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.332× (z -10.2) |
| [[RPMI-7951 (line)]] | alt | 326 | 1 | 3 | [[TAK-901 (drug)]] 5 µM 8.98× (z +10.8) | [[Panobinostat (drug)]] 5 µM 0.250× (z -13.0) |
| [[SHP-77 (line)]] | alt | 145 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.254× (z -14.1) |
| [[A498 (line)]] | wt | 412 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.372× (z -9.1) |
| [[BT-474 (line)]] | alt | 158 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.234× (z -13.9) |
| [[LOX-IMVI (line)]] | wt | 147 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +8.9) ⚠ cell-cycle shift, explains ~11% of this change | [[Panobinostat (drug)]] 5 µM 0.178× (z -11.5) |
| [[Panc 03.27 (line)]] | alt | 353 | 2 (2 ⚠) | 1 | [[Harringtonine (drug)]] 5 µM 2.54× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.412× (z -8.9) |
| [[HT-29 (line)]] | alt | 286 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.238× (z -9.9) |
| [[hTERT-HPNE (line)]] | wt | 209 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.234× (z -9.6) |
| [[PANC-1 (line)]] | alt | 178 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 2.09× (z +10.1) | — |
| [[SW1417 (line)]] | alt | 279 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.380× (z -12.5) |
| [[SW48 (line)]] | wt | 134 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.15× (z +16.7) ⚠ cell-cycle shift, explains ~11% of this change | — |
| [[HCT15 (line)]] | alt | 230 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +9.2) ⚠ cell-cycle shift, explains ~11% of this change | — |
| [[HepG2_C3A (line)]] | wt | 134 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.471× (z -9.1) |
| [[NCI-H1792 (line)]] | alt | 234 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.329× (z -11.4) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 166 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -10.2) ⚠ cell-cycle shift, explains ~11% of this change |
| [[A-427 (line)]] | wt | 78.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 154 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 196 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 184 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 422 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 283 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 347 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 885 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 569 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 377 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2690), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RIGI]] | +0.88 | +0.87 / +0.87 | both halves | 7e-06 | STRING 971 |
| [[PARP14]] | +0.87 | +0.82 / +0.86 | both halves | 7e-06 | same gene group; STRING 519 |
| [[IFIT3]] | +0.87 | +0.82 / +0.86 | both halves | 7e-06 | STRING 513 |
| [[OASL]] | +0.86 | +0.84 / +0.89 | both halves | 7e-06 | STRING 646 |
| [[IFIT2]] | +0.85 | +0.81 / +0.81 | both halves | 7e-06 | STRING 482 |
| [[IFIT1]] | +0.84 | +0.84 / +0.84 | both halves | 7e-06 | STRING 496 |
| [[IFIH1]] | +0.83 | +0.81 / +0.82 | both halves | 7e-06 | STRING 638 |
| [[CMPK2]] | +0.82 | +0.79 / +0.85 | both halves | 7e-06 | STRING 439 |
| [[RSAD2]] | +0.82 | +0.80 / +0.83 | both halves | 7e-06 | STRING 605 |
| [[HERC6]] | +0.82 | +0.80 / +0.80 | both halves | 7e-06 |  |
| [[USP18]] | +0.82 | +0.80 / +0.81 | both halves | 7e-06 | STRING 474 |
| [[OAS2]] | +0.82 | +0.74 / +0.86 | both halves | 7e-06 | STRING 507 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*38 arrows, 38 of them with an alert ⚠; grade A 0, B 25, C 13. Shown: the 12 strongest; 26 more arrows (26 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLAAT4]] | B | PLAAT4 activity raises ZC3HAV1's level | lines that do not express PLAAT4 (21) vs lines expressing it (29) | 1.86× lower at baseline in the lines without PLAAT4 | 0.001 | ⚠ within organs, on part of the lines; also absent: PTPRB, TNFSF10, EPSTI1 |
| [[OASL]] | B | OASL activity raises ZC3HAV1's level | lines that do not express OASL (10) vs lines expressing it (40) | 1.93× lower at baseline in the lines without OASL | 0.003 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, GBP2, TENT5A; maybe low, not absent |
| [[OAS2]] | B | OAS2 activity strengthens ZC3HAV1's drug response | lines that do not express OAS2 (14) vs lines expressing it (35) | the lines without OAS2 respond 0.52× as strongly (z diff +2.04); strongest at Dinaciclib 0.5 µM: 0.89x vs 0.54x (z diff +4.9) | 0.006 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1; target measured in part of the lines; artifact flags |
| [[RSAD2]] | B | RSAD2 activity raises ZC3HAV1's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 1.73× lower at baseline in the lines without RSAD2 | 0.012 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[EPSTI1]] | B | EPSTI1 activity raises ZC3HAV1's level | lines that do not express EPSTI1 (25) vs lines expressing it (25) | 1.60× lower at baseline in the lines without EPSTI1 | 0.014 | ⚠ within organs, on part of the lines; also absent: UGT1A6, PKP1, ENSG00000271933 |
| [[IFIT3]] | B | IFIT3 activity raises ZC3HAV1's level | lines that do not express IFIT3 (8) vs lines expressing it (42) | 1.74× lower at baseline in the lines without IFIT3 | 0.020 | ⚠ within organs, on part of the lines; also absent: GBP2, IFIT2, TRIM38; maybe low, not absent |
| [[IFI44]] | B | IFI44 activity raises ZC3HAV1's level | lines that do not express IFI44 (12) vs lines expressing it (38) | 1.69× lower at baseline in the lines without IFI44 | 0.022 | ⚠ within organs, on part of the lines; also absent: SAMD9, GBP1, BMP2 |
| [[CTSS]] | B | CTSS activity raises ZC3HAV1's level | lines that do not express CTSS (15) vs lines expressing it (35) | 1.63× lower at baseline in the lines without CTSS | 0.027 | ⚠ within organs, on part of the lines; also absent: LINC02257, NMRAL2P-1, CSF2; maybe low, not absent |
| [[IFIT2]] | B | IFIT2 activity raises ZC3HAV1's level | lines that do not express IFIT2 (8) vs lines expressing it (42) | 1.79× lower at baseline in the lines without IFIT2 | 0.034 | ⚠ within organs, on part of the lines; also absent: IFIT3, ENSG00000235609, TRIM38 |
| [[TRIM34]] | B | TRIM34 activity raises ZC3HAV1's level | lines that do not express TRIM34 (6) vs lines expressing it (44) | 1.79× lower at baseline in the lines without TRIM34 | 0.037 | ⚠ within organs, on part of the lines; also absent: BIRC3, FXYD5, TFAP2A; maybe low, not absent |
| [[SAMD9]] | B | SAMD9 activity raises ZC3HAV1's level | lines that do not express SAMD9 (11) vs lines expressing it (39) | 1.70× lower at baseline in the lines without SAMD9 | 0.045 | ⚠ within organs, on part of the lines; also absent: IFI44, GBP1, TLR6 |
| [[DDX60L]] | B | DDX60L activity strengthens ZC3HAV1's drug response | lines that do not express DDX60L (7) vs lines expressing it (42) | the lines without DDX60L respond 0.54× as strongly (z diff +2.20); strongest at Dinaciclib 0.5 µM: 1.06x vs 0.57x (z diff +5.1) | 0.046 | ⚠ within organs, on part of the lines; also absent: ENSG00000287188, ENSG00000291144; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.862). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (47.4, 53.8); signed map (63.8, 32.2). **Vector** length 146, 49.8% of its response variance represented; |z| ≥ 3 in 1,631 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon alpha response* (hallmark, mean cos +0.71 to 56); *interferon gamma response* (hallmark, mean cos +0.73 to 60); *interferon* (control, mean cos +0.80 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +9.1 | +3.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.7 | +2.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | +6.5 | +3.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.3 | +8.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.3 | +7.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.9 | +4.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.8 | +3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.7 | +1.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.5 | +3.1 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -8.9 | -11.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -8.1 | -8.9 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -7.8 | -8.2 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -7.0 | -8.6 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -6.7 | -7.4 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger CCCH-type containing, antiviral 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q34 — chr7:139,043,515-139,132,122 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ZAP, FLB6421, FLJ13288, MGC48898, ZC3HDC2, ZC3H2, PARP13, ARTD13 |
| Gene groups (HGNC) | Zinc fingers CCCH-type; Poly(ADP-ribose) polymerases |
| Reactome | 3 pathways, smallest: Signaling by BRAF and RAF1 fusions; Oncogenic MAPK signaling; Diseases of signal transduction by growth factor receptors and second messengers |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z2W4](https://www.uniprot.org/uniprotkb/Q7Z2W4) (Zinc finger CCCH-type antiviral protein 1):

> Antiviral protein which inhibits the replication of viruses by recruiting the cellular RNA degradation machineries to degrade the viral mRNAs. Binds to a ZAP-responsive element (ZRE) present in the target viral mRNA, recruits cellular poly(A)-specific ribonuclease PARN to remove the poly(A) tail, and the 3'-5' exoribonuclease complex exosome to degrade the RNA body from the 3'-end. It also recruits the decapping complex DCP1-DCP2 through RNA helicase p72 (DDX17) to remove the cap structure of …

**Summary**, from NCBI Gene [56829](https://www.ncbi.nlm.nih.gov/gene/56829):

> This gene encodes a CCCH-type zinc finger protein. This antiviral protein inhibits viral replication by recruiting cellular RNA degradation machineries to degrade viral mRNAs. The encoded protein plays an important role in the innate immune response against multiple DNA and RNA viruses, including Ebola virus, HIV and SARS-CoV-2 (which causes COVID-19). [provided by RefSeq, Sep 2021]

**Accessions** — [HGNC:23721](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23721) · Entrez [56829](https://www.ncbi.nlm.nih.gov/gene/56829) · UniProt [Q7Z2W4](https://www.uniprot.org/uniprotkb/Q7Z2W4) · Ensembl [ENSG00000105939](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105939)

## Data

Gene col 2690: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2690); `tables/drug_effects.parquet` (72 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2690, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2690]; `tensor/DDL_lfc|DDL_z.npy` [2690]; `embed/gene_vectors.npy` [2690]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2690 or target_col == 2690). Every well: [[ZC3HAV1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZC3HAV1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
