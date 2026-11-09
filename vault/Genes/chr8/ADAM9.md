---
symbol: "ADAM9"
type: "gene"
col: 9676
ensembl_id: "ENSG00000168615"
name: "ADAM metallopeptidase domain 9"
location: "8p11.22"
module: 29
arm: "+"
pooled_cpm: 269.83
n_lines_expressing: 49
n_dd_up: 23
n_dd_down: 2
n_dd_up_clean: 13
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# ADAM9

*ADAM metallopeptidase domain 9* — 8p11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (10 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.12× (z +12.7, q 3e-34, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.760× (z -4.5, q 0.003, down in 28 of 46 measured lines) ⚠ toxic. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.771× (z -4.4, q 0.003, down in 34 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H2347 0.548×, HepG2/C3A 0.475×, KATO III 0.547×; ⚠ cell-cycle shift, explains ~71% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (PANC-1 0.517×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CNN3]] (+0.71, fdr 7e-06), [[ACTR3]] (+0.65, fdr 1e-05), [[FSTL1]] (+0.62, fdr 3e-05); moves opposite to [[ZNF593]] (-0.59, fdr 3e-05), [[MAP2K7]] (-0.59, fdr 4e-05), [[SMIM26]] (-0.57, fdr 4e-05, ⚠ SMIM26 in the vector space only through flagged drug-doses), [[ISG20L2]] (-0.56, fdr 4e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[VGLL3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9676.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.12×** | +12.7 | 3e-34 | 46/47 (NCI-H1573, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **4.04×** | +12.4 | 1e-32 | 46/48 (NCI-H23, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.97×** | +11.5 | 2e-28 | 42/48 (COLO 205, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.87×** | +10.6 | 3e-24 | 45/47 (NCI-H1573, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.86×** | +9.7 | 3e-20 | 37/44 (NCI-H1792, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.81×** | +9.6 | 5e-20 | 38/43 (SK-MEL-2, A498, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.75×** | +9.5 | 2e-19 | 45/47 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.63×** | +8.3 | 7e-15 | 42/47 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +8.3 | 1e-14 | 38/46 (LoVo, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.38×** | +7.7 | 8e-13 | 38/48 (LS 180, HT-29, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.33×** | +7.5 | 4e-12 | 40/47 (HOP62, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.51×** | +6.9 | 2e-10 | 40/47 (NCI-H1573, LS 180, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.38×** | +5.4 | 3e-06 | 33/47 (HT-29, LS 180, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.83×** | +5.3 | 4e-06 | 24/37 (NCI-H1573, SNU-423, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.34×** | +4.9 | 4e-05 | 30/47 (LS 180, COLO 205, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.35×** | +4.9 | 4e-05 | 29/46 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Peretinoin (drug)]] 5 µM |  | **1.35×** | +4.8 | 4e-05 | 29/46 (COLO 205, LS 180, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.33×** | +4.7 | 8e-05 | 29/47 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.28×** | +4.1 | 0.001 | 24/46 (COLO 205, HT-29, …) | rises with dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.24×** | +3.5 | 0.012 | 27/48 (A-172, NCI-H460, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9676.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H2347 0.548×, HepG2/C3A 0.475×, KATO III 0.547×; ⚠ cell-cycle shift, explains ~71% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (PANC-1 0.517×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.760×** | -4.5 | 0.003 | 28/46 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.771×** | -4.4 | 0.003 | 34/47 (RKO, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Bimiralisib (drug)]] 0.5 µM |  | 0.757× | -3.4 | 0.13 | 28/47 (NCI-H2347, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.824× | -3.3 | 0.13 | 25/47 (KATO III, CFPAC-1, …) | inconsistent across doses |  |
| [[Celecoxib (drug)]] 0.5 µM |  | 0.767× | -3.2 | 0.14 | 24/48 (LoVo, A549, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.781× | -3.0 | 0.20 | 22/47 (Hs 766T, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9676. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 128 | 12 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.90× (z +12.4) ⚠ toxic; transcription drop · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 1.98× (z +11.7) | — |
| [[LS 180 (line)]] | wt | 229 | 10 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.42× (z +15.5) | — |
| [[NCI-H1573 (line)]] | alt | 373 | 10 (5 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.46× (z +19.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 5.17× (z +18.9) | — |
| [[A549 (line)]] | wt | 310 | 9 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +16.6) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 9.45× (z +12.7) | — |
| [[NCI-H460 (line)]] | wt | 199 | 9 (2 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 3.18× (z +14.2) | — |
| [[PANC-1 (line)]] | alt | 163 | 8 (4 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.75× (z +14.0) | [[Panobinostat (drug)]] 5 µM 0.517× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 143 | 8 (4 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.93× (z +14.2) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.55× (z +12.9) | — |
| [[NCI-H23 (line)]] | alt | 159 | 8 (4 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 13.5× (z +16.2) | — |
| [[SW480 (line)]] | alt | 136 | 8 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.62× (z +13.2) | — |
| [[COLO 205 (line)]] | alt | 122 | 7 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.14× (z +15.9) ⚠ toxic; transcription drop · without an alert: [[Peretinoin (drug)]] 5 µM 3.10× (z +10.6) | — |
| [[NCI-H1792 (line)]] | alt | 166 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.98× (z +14.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.87× (z +10.9) | — |
| [[Hs 766T (line)]] | wt | 239 | 5 (3 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.04× (z +12.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 233 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +14.4) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 15.1× (z +12.7) | — |
| [[SK-MEL-2 (line)]] | alt | 113 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.16× (z +14.2) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 5.18× (z +8.6) | — |
| [[A-427 (line)]] | wt | 191 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +15.4) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.84× (z +11.4) | — |
| [[A498 (line)]] | wt | 448 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.61× (z +13.0) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 257 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +10.5) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 7.26× (z +9.7) | — |
| [[Panc 03.27 (line)]] | alt | 305 | 4 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.95× (z +9.3) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 3.57× (z +9.2) | — |
| [[BT-474 (line)]] | alt | 176 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.47× (z +9.2) | — |
| [[HS-578T (line)]] | alt | 321 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.48× (z +12.5) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 405 | 2 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.33× (z +9.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.12× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.547× (z -10.3) ⚠ cell-cycle shift, explains ~71% of this change |
| [[RKO (line)]] | wt | 245 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.25× (z +18.6) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.07× (z +9.3) | — |
| [[SNU-423 (line)]] | alt | 133 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.18× (z +11.0) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 233 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.75× (z +10.0) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 4.62× (z +8.5) | — |
| [[CFPAC-1 (line)]] | alt | 668 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 4.21× (z +9.8) | — |
| [[H4 (line)]] | wt | 245 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.07× (z +9.8) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 211 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.76× (z +11.3) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 342 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.67× (z +9.4) | — |
| [[J82 (line)]] | alt | 327 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.26× (z +10.0) | — |
| [[A-172 (line)]] | wt | 396 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.15× (z +8.6) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 570 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +15.7) ⚠ cell-cycle shift, explains ~71% of this change | — |
| [[HepG2_C3A (line)]] | wt | 341 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.475× (z -11.2) ⚠ cell-cycle shift, explains ~71% of this change |
| [[NCI-H2030 (line)]] | alt | 248 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.05× (z +9.2) | — |
| [[NCI-H2347 (line)]] | alt | 553 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.548× (z -11.3) ⚠ cell-cycle shift, explains ~71% of this change |
| [[SHP-77 (line)]] | alt | 139 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.60× (z +8.5) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 231 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.47× (z +9.9) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 163 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.02× (z +8.6) | — |
| [[AN3 CA (line)]] | alt | 181 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 55.9 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 162 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 347 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 503 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 289 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 254 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 567 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 170 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 323 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 184 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 97.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 96.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9676), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNN3]] | +0.71 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[ACTR3]] | +0.65 | +0.56 / +0.71 | both halves | 1e-05 |  |
| [[FSTL1]] | +0.62 | +0.45 / +0.67 | both halves | 3e-05 |  |
| [[CTSZ]] | +0.61 | +0.46 / +0.65 | both halves | 3e-05 |  |
| [[EFEMP1]] | +0.60 | +0.49 / +0.52 | both halves | 2e-05 | pathway: Extracellular matrix organization |
| [[CAV2]] | +0.60 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[DR1]] | +0.59 | +0.39 / +0.65 | both halves | 6e-05 |  |
| [[TMEM123]] | +0.59 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[ANXA2]] | +0.59 | +0.51 / +0.68 | both halves | 1e-05 |  |
| [[DHFR]] | +0.58 | +0.39 / +0.64 | both halves | 5e-05 |  |
| [[TMEM30A]] | +0.58 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[GOLM1]] | +0.57 | +0.48 / +0.57 | both halves | 2e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF593]] | -0.59 | -0.45 / -0.65 | both halves | 3e-05 |  |
| [[MAP2K7]] | -0.59 | -0.40 / -0.65 | both halves | 4e-05 |  |
| [[SMIM26]] ⚠ | -0.57 | -0.41 / -0.62 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ISG20L2]] | -0.56 | -0.42 / -0.63 | both halves | 4e-05 |  |
| [[PIAS4]] | -0.55 | -0.44 / -0.61 | both halves | 3e-05 |  |
| [[TRAPPC2B]] | -0.54 | -0.38 / -0.60 | both halves | 7e-05 |  |
| [[RPP21]] | -0.54 | -0.25 / -0.65 | both halves | 4e-04 |  |
| [[ZBTB7A]] | -0.54 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[ZNF503]] | -0.54 | -0.42 / -0.63 | both halves | 4e-05 |  |
| [[CEBPZ]] | -0.54 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[TMEM258]] | -0.54 | -0.36 / -0.57 | both halves | 9e-05 |  |
| [[CROCCP2-1]] | -0.54 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[TTF1]] | -0.53 | -0.42 / -0.58 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VGLL3]] | B | VGLL3 activity raises ADAM9's level | lines that do not express VGLL3 (30) vs lines expressing it (20) | 1.51× lower at baseline in the lines without VGLL3 | 0.093 | ⚠ within organs, on part of the lines; also absent: EDNRA, APBB1IP, LINC02882 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.617). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-55.9, 6.2); signed map (44.7, -8.6). **Vector** length 129, 48.7% of its response variance represented; |z| ≥ 3 in 1,398 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +13.9 | +9.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +13.5 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +13.2 | +11.5 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +6.3 | +5.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.5 | +2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.4 | +1.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +5.0 | +7.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +4.5 | +5.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.3 | +0.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | -0.6 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -3.8 | -4.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -3.5 | -4.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -3.5 | +3.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | +2.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.9 | +1.1 |
|  | [[Vilanterol (drug)]] 5 µM |  | -2.9 | -1.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.8 | -1.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.7 | -3.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.6 | -1.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.4 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | ADAM metallopeptidase domain 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p11.22 — chr8:38,996,754-39,105,445 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MDC9, KIAA0021, MCMP, Mltng; previously CORD9 |
| Gene groups (HGNC) | ADAM metallopeptidase domain containing |
| Hallmark sets | COAGULATION, COMPLEMENT, APICAL_JUNCTION |
| Reactome | 3 pathways, smallest: Collagen degradation; Degradation of the extracellular matrix; Extracellular matrix organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13443](https://www.uniprot.org/uniprotkb/Q13443) (Disintegrin and metalloproteinase domain-containing protein 9):

> Metalloprotease that cleaves and releases a number of molecules with important roles in tumorigenesis and angiogenesis, such as TEK, KDR, EPHB4, CD40, VCAM1 and CDH5. May mediate cell-cell, cell-matrix interactions and regulate the motility of cells via interactions with integrins.; [Isoform 2]: May act as alpha-secretase for amyloid precursor protein (APP).

**Summary**, from NCBI Gene [8754](https://www.ncbi.nlm.nih.gov/gene/8754):

> This gene encodes a member of the ADAM (a disintegrin and metalloprotease domain) family. Members of this family are membrane-anchored proteins structurally related to snake venom disintegrins, and have been implicated in a variety of biological processes involving cell-cell and cell-matrix interactions, including fertilization, muscle development, and neurogenesis. The protein encoded by this gene interacts with SH3 domain-containing proteins, binds mitotic arrest deficient 2 beta protein, and …

**Accessions** — [HGNC:216](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:216) · Entrez [8754](https://www.ncbi.nlm.nih.gov/gene/8754) · UniProt [Q13443](https://www.uniprot.org/uniprotkb/Q13443) · Ensembl [ENSG00000168615](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168615)

## Data

Gene col 9676: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9676); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9676, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9676]; `tensor/DDL_lfc|DDL_z.npy` [9676]; `embed/gene_vectors.npy` [9676]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9676 or target_col == 9676). Every well: [[ADAM9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADAM9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
