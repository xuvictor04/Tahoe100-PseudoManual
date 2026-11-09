---
symbol: "MAP3K20"
type: "gene"
col: 1663
ensembl_id: "ENSG00000091436"
name: "mitogen-activated protein kinase kinase kinase 20"
location: "2q31.1"
module: 44
arm: "+"
pooled_cpm: 233.39
n_lines_expressing: 49
n_dd_up: 1
n_dd_down: 20
n_dd_up_clean: 0
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# MAP3K20

*mitogen-activated protein kinase kinase kinase 20* — 2q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.21× (z +6.8, q 7e-09, up in 23 of 48 measured lines) ⚠ toxic; transcription drop.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 14 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Vinblastine (sulfate) (drug)]] 5 µM in 4 lines (LS 180 1.74×, CFPAC-1 1.73×, LoVo 1.52×, KATO III 1.61×); [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 2 lines (H4 3.37×, NCI-H2030 1.76×); [[Daptomycin (drug)]] 5 µM in 2 lines (LS 180 2.21×, LoVo 1.84×; ⚠ unreliable plate only); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (AsPC-1 2.14×, BT-474 2.66×).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.289× (z -44.9, q 0e+00, down in 47 of 47 measured lines).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BMAL2]] (+0.57, fdr 2e-05), [[OSMR]] (+0.55, fdr 2e-05), [[PLGRKT]] (+0.48, fdr 1e-04); moves opposite to [[VIPR1]] (-0.53, fdr 2e-05), [[TJP3]] (-0.48, fdr 2e-05), [[GPRC5C]] (-0.48, fdr 1e-04).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[RSPO3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1663.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 14 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Vinblastine (sulfate) (drug)]] 5 µM in 4 lines (LS 180 1.74×, CFPAC-1 1.73×, LoVo 1.52×, KATO III 1.61×); [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 2 lines (H4 3.37×, NCI-H2030 1.76×); [[Daptomycin (drug)]] 5 µM in 2 lines (LS 180 2.21×, LoVo 1.84×; ⚠ unreliable plate only); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (AsPC-1 2.14×, BT-474 2.66×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.21×** | +6.8 | 7e-09 | 23/48 (A-427, HS-578T, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.19× | +6.4 | 5e-08 | 21/47 (LS 180, LoVo, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.17× | +5.8 | 1e-06 | 18/46 (H4, NCI-H2030, …) | rises with dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 1.18× | +5.6 | 2e-06 | 19/46 (H4, LOX-IMVI, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | 1.17× | +5.5 | 4e-06 | 20/46 (LS 180, LoVo, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.15× | +4.9 | 8e-05 | 18/47 (SW480, KATO III, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.10× | +4.8 | 2e-04 | 14/48 (LS 180, CFPAC-1, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.14× | +4.6 | 3e-04 | 15/46 (LS 180, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.10× | +3.2 | 0.084 | 17/43 (Hs 766T, HOP62, …) | two highest doses | composition shift |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.09× | +3.2 | 0.090 | 13/47 (LS 180, CFPAC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 14 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1663.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.289×** | -44.9 | 0e+00 | 47/47 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.292×** | -44.5 | 0e+00 | 47/47 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.337×** | -39.3 | 0e+00 | 47/47 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.576×** | -19.9 | 0e+00 | 44/47 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.681×** | -19.6 | 0e+00 | 39/48 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.607×** | -18.0 | 0e+00 | 38/47 (NCI-H460, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.703×** | -18.0 | 0e+00 | 32/47 (NCI-H1573, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.665×** | -14.7 | 0e+00 | 42/47 (HEC-1-A, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.762×** | -13.9 | 4e-42 | 32/47 (LOX-IMVI, NCI-H2347, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.572×** | -10.5 | 3e-24 | 36/48 (NCI-H460, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.822×** | -10.0 | 8e-22 | 26/47 (LS 180, SW1417, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.775×** | -9.2 | 2e-18 | 30/48 (LOX-IMVI, NCI-H23, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.769×** | -9.1 | 4e-18 | 27/47 (LOX-IMVI, NCI-H460, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.814×** | -7.4 | 4e-12 | 24/47 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~49% of this change | **0.807×** | -7.4 | 4e-12 | 23/46 (LOX-IMVI, A498, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.767×** | -5.0 | 1e-05 | 22/47 (NCI-H23, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | 0.879× | -4.6 | 8e-05 | 14/47 (C32, SW 900, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1663. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 605 | 1 (1 ⚠) | 20 (6 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 2.01× (z +9.8) ⚠ cell-cycle shift, explains ~21% of this change | [[Panobinostat (drug)]] 0.5 µM 0.115× (z -31.5) |
| [[AsPC-1 (line)]] | alt | 309 | 1 | 16 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.14× (z +10.9) | [[Panobinostat (drug)]] 5 µM 0.200× (z -23.2) |
| [[NCI-H460 (line)]] | wt | 407 | 1 (1 ⚠) | 15 (7 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 1.67× (z +8.7) ⚠ cell-cycle shift, explains ~21% of this change | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -29.5) |
| [[LoVo (line)]] | wt | 141 | 7 (4 ⚠) | 5 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.72× (z +14.3) | [[Panobinostat (drug)]] 0.5 µM 0.425× (z -15.0) |
| [[C32 (line)]] | wt | 213 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -23.6) |
| [[LS 180 (line)]] | wt | 183 | 6 (2 ⚠) | 5 | [[Daptomycin (drug)]] 5 µM 2.21× (z +11.3) ⚠ unreliable plate only · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 1.74× (z +11.2) | [[Panobinostat (drug)]] 0.5 µM 0.261× (z -19.2) |
| [[NCI-H2030 (line)]] | alt | 631 | 2 (1 ⚠) | 9 (2 ⚠) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 1.76× (z +8.8) | [[Panobinostat (drug)]] 5 µM 0.227× (z -23.0) |
| [[H4 (line)]] | wt | 257 | 4 (2 ⚠) | 6 | [[Pitavastatin (Calcium) (drug)]] 5 µM 3.98× (z +14.0) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Pitavastatin (Calcium) (drug)]] 0.5 µM 3.37× (z +12.8) | [[Panobinostat (drug)]] 5 µM 0.223× (z -15.8) |
| [[SNU-423 (line)]] | alt | 200 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -20.1) |
| [[HEC-1-A (line)]] | alt | 172 | 0 | 9 | — | [[Panobinostat (drug)]] 5 µM 0.235× (z -24.7) |
| [[NCI-H1573 (line)]] | alt | 441 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -31.2) |
| [[A-172 (line)]] | wt | 205 | 1 (1 ⚠) | 7 (1 ⚠) | [[Trametinib (drug)]] 5 µM 1.54× (z +8.5) ⚠ cell-cycle shift, explains ~38% of this change | [[Panobinostat (drug)]] 5 µM 0.292× (z -21.6) |
| [[A498 (line)]] | wt | 299 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.292× (z -24.6) |
| [[A549 (line)]] | wt | 324 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.188× (z -21.7) |
| [[J82 (line)]] | alt | 211 | 0 | 8 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.312× (z -21.7) |
| [[NCI-H23 (line)]] | alt | 301 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -27.1) |
| [[CFPAC-1 (line)]] | alt | 145 | 2 (1 ⚠) | 5 | [[Vinblastine (sulfate) (drug)]] 5 µM 1.73× (z +10.6) | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -18.6) |
| [[COLO 205 (line)]] | alt | 275 | 0 | 7 | — | [[Belinostat (drug)]] 5 µM 0.166× (z -18.4) |
| [[HOP62 (line)]] | alt | 189 | 1 (1 ⚠) | 6 | [[Trametinib (drug)]] 5 µM 1.72× (z +10.2) ⚠ cell-cycle shift, explains ~38% of this change | [[Panobinostat (drug)]] 0.5 µM 0.279× (z -21.7) |
| [[hTERT-HPNE (line)]] | wt | 251 | 2 (1 ⚠) | 5 (1 ⚠) | [[Trametinib (drug)]] 5 µM 2.13× (z +10.8) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 1.92× (z +8.5) | [[Belinostat (drug)]] 5 µM 0.228× (z -20.2) |
| [[NCI-H2347 (line)]] | alt | 122 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.298× (z -18.8) |
| [[RKO (line)]] | wt | 209 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.310× (z -20.6) |
| [[MIA PaCa-2 (line)]] | alt | 171 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -30.4) |
| [[NCI-H1792 (line)]] | alt | 254 | 0 | 6 | — | [[Panobinostat (drug)]] 0.5 µM 0.226× (z -22.2) |
| [[SW1417 (line)]] | alt | 213 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.289× (z -22.9) |
| [[HCT15 (line)]] | alt | 184 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.373× (z -12.3) |
| [[KATO III (line)]] | alt | 148 | 1 | 4 | [[Vinblastine (sulfate) (drug)]] 5 µM 1.61× (z +9.2) | [[Panobinostat (drug)]] 0.5 µM 0.295× (z -16.9) |
| [[Panc 03.27 (line)]] | alt | 146 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.217× (z -21.6) |
| [[SW 900 (line)]] | alt | 200 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.263× (z -21.0) |
| [[Hs 766T (line)]] | wt | 94.2 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.17× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.379× (z -11.8) |
| [[HT-29 (line)]] | alt | 185 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.292× (z -15.5) |
| [[PANC-1 (line)]] | alt | 318 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.179× (z -23.1) |
| [[RPMI-7951 (line)]] | alt | 175 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -16.5) |
| [[SW 1271 (line)]] | alt | 414 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.182× (z -11.4) |
| [[SW48 (line)]] | wt | 299 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -16.0) |
| [[SW480 (line)]] | alt | 156 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.238× (z -30.7) |
| [[A-427 (line)]] | wt | 103 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.385× (z -13.4) |
| [[BT-474 (line)]] | alt | 93.0 | 2 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.01× (z +8.8) | [[Dinaciclib (drug)]] 0.05 µM 0.341× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 142 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.287× (z -16.4) |
| [[HS-578T (line)]] | alt | 174 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.329× (z -15.3) |
| [[AN3 CA (line)]] | alt | 179 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.280× (z -11.1) |
| [[CHP-212 (line)]] | wt | 133 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.240× (z -10.4) |
| [[HepG2_C3A (line)]] | wt | 95.3 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.337× (z -9.7) |
| [[SHP-77 (line)]] | alt | 69.8 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.405× (z -8.8) |
| [[SNU-1 (line)]] | wt | 157 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.424× (z -10.6) |
| [[NCI-H2122 (line)]] | alt | 263 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 212 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 76.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 34.4 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 234 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1663), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*36 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BMAL2]] | +0.57 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[OSMR]] | +0.55 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[PLGRKT]] | +0.48 | +0.36 / +0.38 | both halves | 1e-04 |  |
| [[CYFIP1]] | +0.46 | +0.20 / +0.59 | ⚠ one half (not replicated) | 8e-04 |  |
| [[PHLDB2]] | +0.46 | +0.39 / +0.49 | both halves | 5e-05 |  |
| [[CTNNAL1]] | +0.45 | +0.34 / +0.36 | both halves | 1e-04 |  |
| [[LINC00707]] | +0.44 | +0.40 / +0.53 | both halves | 5e-05 |  |
| [[KPNA4]] | +0.44 | +0.35 / +0.48 | both halves | 1e-04 |  |
| [[SEMA3C]] | +0.44 | +0.30 / +0.39 | both halves | 2e-04 |  |
| [[GLIPR1]] | +0.44 | +0.35 / +0.44 | both halves | 1e-04 |  |
| [[SAMD4A]] | +0.43 | +0.21 / +0.48 | both halves | 7e-04 |  |
| [[BCAP29]] | +0.43 | +0.37 / +0.48 | both halves | 8e-05 |  |
| [[RAI14]] | +0.42 | +0.48 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*64 of its nearest partners move opposite, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VIPR1]] | -0.53 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[TJP3]] | -0.48 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[GPRC5C]] | -0.48 | -0.43 / -0.36 | both halves | 1e-04 |  |
| [[PRR15L]] | -0.47 | -0.50 / -0.37 | both halves | 8e-05 |  |
| [[IGFL2-AS1]] | -0.46 | -0.46 / -0.38 | both halves | 7e-05 |  |
| [[PRR15]] | -0.46 | -0.50 / -0.39 | both halves | 6e-05 |  |
| [[PKDCC]] | -0.46 | -0.44 / -0.34 | both halves | 1e-04 |  |
| [[MANSC1]] | -0.45 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[PRR15-DT]] | -0.45 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[SEMA4G]] | -0.44 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[ABO]] | -0.44 | -0.38 / -0.37 | both halves | 8e-05 |  |
| [[PLEKHG6]] | -0.44 | -0.53 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RSPO3]] | B | RSPO3 activity raises MAP3K20's level | lines that do not express RSPO3 (39) vs lines expressing it (11) | 1.87× lower at baseline in the lines without RSPO3 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, TBXT, GSG1L2 |
| [[SLC43A1]] | B | SLC43A1 activity lowers MAP3K20's level | lines that do not express SLC43A1 (9) vs lines expressing it (41) | 1.94× higher at baseline in the lines without SLC43A1 | 0.041 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[OSMR]] | B | OSMR activity raises MAP3K20's level | lines that do not express OSMR (13) vs lines expressing it (37) | 1.24× lower at baseline in the lines without OSMR | 0.081 | ⚠ within organs, on part of the lines; co-occurs with ACVR2A, APC, SETD1B; also absent: OSMR-DT, LIFR, IL1R1 |
| [[EGFR]] | B | EGFR activity raises MAP3K20's level | lines that do not express EGFR (7) vs lines expressing it (43) | 1.97× lower at baseline in the lines without EGFR | 0.095 | ⚠ within organs, on part of the lines; also absent: C1RL-AS1, PSD4, RNASEL |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction -0.461). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (29.2, 48.2); signed map (11.1, 24.8). **Vector** length 104, 30.7% of its response variance represented; |z| ≥ 3 in 1,945 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +7.4 | +3.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.3 | +6.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +5.8 | +5.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.8 | +0.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.5 | +2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.7 | +4.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.3 | +4.9 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +3.5 | +0.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.5 | +0.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.0 | -18.0 |
|  | [[Selinexor (drug)]] 5 µM |  | -4.3 | -13.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.5 | -14.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~3% of this change | -3.3 | -6.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -3.2 | -3.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | -2.0 |
|  | [[Cepharanthine (drug)]] 5 µM |  | -2.1 | -1.4 |
|  | [[Entrectinib (drug)]] 5 µM |  | -1.9 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | mitogen-activated protein kinase kinase kinase 20 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.1 — chr2:173,075,435-173,268,015 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MLTKalpha, MLTKbeta, ZAK, MLTK, MLK7, MRK |
| Gene groups (HGNC) | Mitogen-activated protein kinase kinase kinases; Mixed lineage kinase family |
| Hallmark sets | APICAL_JUNCTION, G2M_CHECKPOINT |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NYL2](https://www.uniprot.org/uniprotkb/Q9NYL2) (Mitogen-activated protein kinase kinase kinase 20):

> Stress-activated component of a protein kinase signal transduction cascade that promotes programmed cell death in response to various stress, such as ribosomal stress, osmotic shock and ionizing radiation. Acts by catalyzing phosphorylation of MAP kinase kinases, leading to activation of the JNK (MAPK8/JNK1, MAPK9/JNK2 and/or MAPK10/JNK3) and MAP kinase p38 (MAPK11, MAPK12, MAPK13 and/or MAPK14) pathways. Activates JNK through phosphorylation of MAP2K4/MKK4 and MAP2K7/MKK7, and MAP kinase p38 …

**Summary**, from NCBI Gene [51776](https://www.ncbi.nlm.nih.gov/gene/51776):

> This gene is a member of the MAPKKK family of signal transduction molecules and encodes a protein with an N-terminal kinase catalytic domain, followed by a leucine zipper motif and a sterile-alpha motif (SAM). This magnesium-binding protein forms homodimers and is located in the cytoplasm. The protein mediates gamma radiation signaling leading to cell cycle arrest and activity of this protein plays a role in cell cycle checkpoint regulation in cells. The protein also has pro-apoptotic activity. …

**Accessions** — [HGNC:17797](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17797) · Entrez [51776](https://www.ncbi.nlm.nih.gov/gene/51776) · UniProt [Q9NYL2](https://www.uniprot.org/uniprotkb/Q9NYL2) · Ensembl [ENSG00000091436](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000091436)

## Data

Gene col 1663: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1663); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1663, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1663]; `tensor/DDL_lfc|DDL_z.npy` [1663]; `embed/gene_vectors.npy` [1663]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1663 or target_col == 1663). Every well: [[MAP3K20 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAP3K20.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
