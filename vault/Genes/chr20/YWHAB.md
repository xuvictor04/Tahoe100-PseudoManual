---
symbol: "YWHAB"
type: "gene"
col: 9387
ensembl_id: "ENSG00000166913"
name: "tyrosine 3-monooxygenase/tryptophan 5-monooxygenase activation protein beta"
location: "20q13.12"
module: 78
arm: "+"
pooled_cpm: 285.02
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 1
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/078"]
generated_by: "tahoemap"
---

# YWHAB

*tyrosine 3-monooxygenase/tryptophan 5-monooxygenase activation protein beta* — 20q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.51× (z +16.8, q 0e+00, up in 49 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.01× (z +7.8, q 1e-12, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Anethole trithione (drug)]] 5 µM: 0.769× (z -4.1, q 0.020, down in 45 of 48 measured lines) ⚠ cell-cycle shift, explains ~38% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 0.455×, NCI-H2030 0.512×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CAP1]] (+0.69, fdr 7e-06), [[PSMD1]] (+0.59, fdr 1e-05), [[TPM3]] (+0.57, fdr 1e-05); moves opposite to [[TP53]] (-0.57, fdr 5e-05), [[SNHG1]] (-0.55, fdr 3e-05), [[HPS4]] (-0.54, fdr 2e-05).
> It is in [[Module 078]], a single-armed module (apical junction).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PLXNA2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 11 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9387.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **4.51×** | +16.8 | 0e+00 | 49/49 (A549, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **3.82×** | +14.4 | 3e-44 | 44/44 (A549, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.96×** | +11.2 | 8e-27 | 45/45 (SNU-423, A549, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.01×** | +7.8 | 1e-12 | 46/48 (C32, SNU-423, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | **1.68×** | +5.8 | 9e-07 | 44/48 (PANC-1, SW 900, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.59×** | +5.2 | 2e-05 | 41/48 (COLO 205, SNU-423, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~62% of this change | **1.53×** | +4.5 | 5e-04 | 35/47 (C32, NCI-H1792, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.39×** | +3.7 | 0.018 | 35/48 (SNU-423, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~92% of this change | **1.37×** | +3.5 | 0.033 | 33/48 (SW 900, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.35×** | +3.4 | 0.042 | 30/48 (PANC-1, AsPC-1, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.34×** | +3.3 | 0.052 | 30/48 (SNU-1, HCT15, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.34×** | +3.3 | 0.053 | 32/48 (CFPAC-1, SW 900, …) | rises with dose |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.33×** | +3.1 | 0.072 | 37/48 (HOP62, NCI-H460, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.31×** | +3.0 | 0.096 | 30/48 (NCI-H1792, A549, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9387.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 0.455×, NCI-H2030 0.512×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.769×** | -4.1 | 0.020 | 45/48 (SK-MEL-2, NCI-H661, …) | all doses, stronger at high dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | 0.570× | -3.3 | 0.21 | 36/50 (AsPC-1, NCI-H23, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | 0.699× | -3.3 | 0.21 | 36/50 (NCI-H23, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | 0.583× | -3.1 | 0.23 | 38/49 (A-172, RPMI-7951, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | 0.595× | -3.0 | 0.26 | 33/49 (AsPC-1, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, +0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9387. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 201 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.21× (z +16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.05× (z +9.2) | — |
| [[SNU-423 (line)]] | alt | 224 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.03× (z +16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.05× (z +9.6) | — |
| [[C32 (line)]] | wt | 168 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.02× (z +14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.44× (z +10.8) | — |
| [[NCI-H1792 (line)]] | alt | 165 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.95× (z +17.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[PANC-1 (line)]] | alt | 267 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.31× (z +15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[A-172 (line)]] | wt | 261 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.06× (z +13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[A498 (line)]] | wt | 244 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.14× (z +15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[A549 (line)]] | wt | 187 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.92× (z +19.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[CFPAC-1 (line)]] | alt | 236 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.28× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[HOP62 (line)]] | alt | 153 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.14× (z +14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[Hs 766T (line)]] | wt | 437 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.14× (z +14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[HS-578T (line)]] | alt | 241 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.72× (z +14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 207 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.16× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[KATO III (line)]] | alt | 371 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.42× (z +15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[LoVo (line)]] | wt | 207 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.89× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.82× (z +8.9) | — |
| [[LOX-IMVI (line)]] | wt | 254 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.45× (z +15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[LS 180 (line)]] | wt | 242 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.65× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H2030 (line)]] | alt | 340 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.83× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | [[Homoharringtonine (drug)]] 5 µM 0.512× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 261 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.33× (z +14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[RPMI-7951 (line)]] | alt | 302 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.07× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SW1417 (line)]] | alt | 439 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SW480 (line)]] | alt | 373 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.50× (z +15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[A-427 (line)]] | wt | 311 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.68× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | [[Homoharringtonine (drug)]] 5 µM 0.455× (z -10.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 333 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.66× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[C-33 A (line)]] | alt | 238 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.69× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[H4 (line)]] | wt | 192 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.04× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[HCT15 (line)]] | alt | 194 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.04× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[HEC-1-A (line)]] | alt | 244 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.40× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[HepG2_C3A (line)]] | wt | 274 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[HT-29 (line)]] | alt | 376 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[J82 (line)]] | alt | 510 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H2347 (line)]] | alt | 265 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.01× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H460 (line)]] | wt | 182 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.05× (z +14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SHP-77 (line)]] | alt | 184 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.72× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 309 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SNU-1 (line)]] | wt | 226 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.36× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SW 900 (line)]] | alt | 204 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.40× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SW48 (line)]] | wt | 193 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.17× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[AN3 CA (line)]] | alt | 155 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.81× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[COLO 205 (line)]] | alt | 219 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.51× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H1573 (line)]] | alt | 270 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.57× (z +13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H23 (line)]] | alt | 471 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.99× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[RKO (line)]] | wt | 310 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.61× (z +15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SW 1271 (line)]] | alt | 277 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.89× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[BT-474 (line)]] | alt | 1,078 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 151 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 204 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 253 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 370 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 231 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9387), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*40 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAP1]] | +0.69 | +0.63 / +0.61 | both halves | 7e-06 | STRING 411 |
| [[PSMD1]] | +0.59 | +0.65 / +0.53 | both halves | 1e-05 | pathway: Apoptosis |
| [[TPM3]] | +0.57 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[BZW1]] | +0.56 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[ACTR2]] | +0.55 | +0.60 / +0.57 | both halves | 9e-06 | pathway: HALLMARK_PI3K_AKT_MTOR_SIGNALING; STRING 486 |
| [[ARPC5]] | +0.54 | +0.61 / +0.51 | both halves | 1e-05 | pathway: RHO GTPase Effectors |
| [[KPNA4]] | +0.54 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[PRDX1]] | +0.53 | +0.53 / +0.53 | both halves | 1e-05 | pathway: TP53 Regulates Metabolic Genes; STRING 412 |
| [[PSMD2]] | +0.52 | +0.51 / +0.53 | both halves | 1e-05 | pathway: Apoptosis |
| [[SETX]] | +0.52 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[RNGTT]] | +0.51 | +0.60 / +0.28 | both halves | 3e-04 |  |
| [[RASAL2]] | +0.51 | +0.50 / +0.48 | both halves | 2e-05 | pathway: MAPK family signaling cascades; STRING 451 |

## Genes that move opposite

*60 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TP53]] | -0.57 | -0.48 / -0.40 | both halves | 5e-05 | pathway: Activation of BH3-only proteins; STRING 828 |
| [[SNHG1]] | -0.55 | -0.58 / -0.46 | both halves | 3e-05 |  |
| [[HPS4]] | -0.54 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[CCDC115]] | -0.54 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[MAPKAPK5-AS1]] | -0.53 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[CLN5]] | -0.53 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[NEURL3]] | -0.53 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[DCP1B]] | -0.53 | -0.45 / -0.38 | both halves | 6e-05 |  |
| [[ABCA5]] | -0.53 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[C1orf43]] | -0.52 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[EEF1AKMT3]] | -0.51 | -0.49 / -0.34 | both halves | 1e-04 |  |
| [[ATP23]] | -0.51 | -0.45 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLXNA2]] | B | PLXNA2 activity lowers YWHAB's level | lines that do not express PLXNA2 (15) vs lines expressing it (35) | 1.10× higher at baseline in the lines without PLXNA2 | 0.061 | ⚠ within organs, on part of the lines; also absent: GATA6, HS3ST3B1, IFI16 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 078]] — apical junction; 58 genes; every member is in the + arm (projection on the module's main direction 0.477). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.0, 10.4); signed map (-7.6, 38.7). **Vector** length 79.8, 37.8% of its response variance represented; |z| ≥ 3 in 849 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.5 | +7.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +1.8 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +2.3 | +1.3 |
|  | [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~70% of this change | +2.2 | +3.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | +2.2 | +5.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.0 | -0.5 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +2.0 | +2.4 |
|  | [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | +2.0 | +1.5 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -6.0 | +2.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.7 | +0.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.2 | -2.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -5.2 | -2.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | -5.1 | +14.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.1 | +0.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -2.0 | +2.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.0 | +0.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.9 | -1.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -1.9 | +0.9 |

## What is on record

|  |  |
|---|---|
| Name | tyrosine 3-monooxygenase/tryptophan 5-monooxygenase activation protein beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.12 — chr20:44,885,702-44,908,532 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously YWHAA |
| Gene groups (HGNC) | 14-3-3 phospho-serine/phospho-threonine binding proteins |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING |
| Reactome | 64 pathways, smallest: ARMS-mediated activation; Gain-of-function MRAS complexes activate RAF signaling; SHOC2 M1731 mutant abolishes MRAS complex function |
| Matched by | ensembl_id |

**Function**, from UniProt [P31946](https://www.uniprot.org/uniprotkb/P31946) (14-3-3 protein beta/alpha):

> Adapter protein implicated in the regulation of a large spectrum of both general and specialized signaling pathways. Binds to a large number of partners, usually by recognition of a phosphoserine or phosphothreonine motif. Binding generally results in the modulation of the activity of the binding partner. Negative regulator of osteogenesis. Blocks the nuclear translocation of the phosphorylated form (by AKT1) of SRPK2 and antagonizes its stimulatory effect on cyclin D1 expression resulting in …

**Summary**, from NCBI Gene [7529](https://www.ncbi.nlm.nih.gov/gene/7529):

> This gene encodes a protein belonging to the 14-3-3 family of proteins, members of which mediate signal transduction by binding to phosphoserine-containing proteins. This highly conserved protein family is found in both plants and mammals. The encoded protein has been shown to interact with RAF1 and CDC25 phosphatases, suggesting that it may play a role in linking mitogenic signaling and the cell cycle machinery. Two transcript variants, which encode the same protein, have been identified for …

**Accessions** — [HGNC:12849](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12849) · Entrez [7529](https://www.ncbi.nlm.nih.gov/gene/7529) · UniProt [P31946](https://www.uniprot.org/uniprotkb/P31946) · Ensembl [ENSG00000166913](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166913)

## Data

Gene col 9387: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9387); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9387, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9387]; `tensor/DDL_lfc|DDL_z.npy` [9387]; `embed/gene_vectors.npy` [9387]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9387 or target_col == 9387). Every well: [[YWHAB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/YWHAB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
