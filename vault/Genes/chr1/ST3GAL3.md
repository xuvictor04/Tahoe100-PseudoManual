---
symbol: "ST3GAL3"
type: "gene"
col: 4715
ensembl_id: "ENSG00000126091"
name: "ST3 beta-galactoside alpha-2,3-sialyltransferase 3"
location: "1p34.1"
module: 31
arm: "+"
pooled_cpm: 116.41
n_lines_expressing: 48
n_dd_up: 1
n_dd_down: 24
n_dd_up_clean: 1
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 29
direction_downstream: 0
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# ST3GAL3

*ST3 beta-galactoside alpha-2,3-sialyltransferase 3* — 1p34.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[5-Azacytidine (drug)]] 5 µM: 1.26× (z +4.0, q 0.031, up in 26 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A-172 2.91×, LoVo 2.87×, HepG2/C3A 2.83×; ⚠ cell-cycle shift, explains ~75% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (LoVo 4.04×, A-172 2.14×; ⚠ cell-cycle shift, would explain all of this change); [[Auranofin (drug)]] 5 µM in 2 lines (LoVo 4.01×, HT-29 2.70×); [[Harringtonine (drug)]] 5 µM in 1 line (A-172 2.45×); [[Tucidinostat (drug)]] 5 µM in 1 line (LoVo 1.92×).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (15 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.399× (z -16.1, q 0e+00, down in 35 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.274× (z -11.9, q 2e-30, down in 43 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZRANB3]] (+0.57, fdr 8e-06), [[ZNF544]] (+0.56, fdr 3e-05), [[EEFSEC]] (+0.55, fdr 1e-05); moves opposite to [[ANXA11]] (-0.65, fdr 7e-06), [[INAVA]] (-0.57, fdr 1e-05), [[EPB41L1]] (-0.55, fdr 1e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 29 arrows point to it, the strongest [[ST14]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4715.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A-172 2.91×, LoVo 2.87×, HepG2/C3A 2.83×; ⚠ cell-cycle shift, explains ~75% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (LoVo 4.04×, A-172 2.14×; ⚠ cell-cycle shift, would explain all of this change); [[Auranofin (drug)]] 5 µM in 2 lines (LoVo 4.01×, HT-29 2.70×); [[Harringtonine (drug)]] 5 µM in 1 line (A-172 2.45×); [[Tucidinostat (drug)]] 5 µM in 1 line (LoVo 1.92×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[5-Azacytidine (drug)]] 5 µM |  | **1.26×** | +4.0 | 0.031 | 26/46 (H4, A-427, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +3.8 | 0.039 | 0/48 | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.21× | +3.4 | 0.14 | 21/47 (RKO, LoVo, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 18 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4715.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.399×** | -16.1 | 0e+00 | 35/47 (PANC-1, J82, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.401×** | -14.9 | 0e+00 | 34/43 (NCI-H23, H4, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.489×** | -12.1 | 2e-31 | 32/41 (A-427, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.274×** | -11.9 | 2e-30 | 43/47 (PANC-1, C-33 A, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.523×** | -10.9 | 8e-26 | 36/46 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.368×** | -9.2 | 4e-18 | 39/46 (HOP62, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.695×** | -9.0 | 1e-17 | 36/46 (RKO, J82, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.612×** | -8.3 | 8e-15 | 35/45 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.670×** | -7.0 | 1e-10 | 34/46 (PANC-1, A-427, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.687×** | -6.6 | 2e-09 | 29/46 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.692×** | -6.5 | 5e-09 | 30/46 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.699×** | -6.3 | 2e-08 | 30/46 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.738×** | -5.3 | 4e-06 | 26/46 (PANC-1, SW480, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.743×** | -5.2 | 7e-06 | 34/46 (SW480, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.755×** | -4.9 | 3e-05 | 28/46 (SW480, PANC-1, …) | top dose only | composition shift |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.831×** | -3.3 | 0.026 | 15/46 (AsPC-1, SNU-423, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.878× | -3.2 | 0.028 | 14/46 (HOP62, A-427, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4715. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 259 | 0 | 19 (14 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.170× (z -27.2) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.101× (z -18.5) |
| [[HOP62 (line)]] | alt | 270 | 0 | 16 (11 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.177× (z -19.5) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.131× (z -12.5) |
| [[NCI-H460 (line)]] | wt | 144 | 0 | 14 (11 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.191× (z -19.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.215× (z -17.5) |
| [[J82 (line)]] | alt | 223 | 0 | 13 (9 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.150× (z -25.0) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.348× (z -13.9) |
| [[SW480 (line)]] | alt | 97.3 | 0 | 12 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.241× (z -18.2) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.395× (z -11.9) |
| [[A-427 (line)]] | wt | 123 | 0 | 11 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0836× (z -29.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.372× (z -11.6) |
| [[MIA PaCa-2 (line)]] | alt | 181 | 0 | 10 (9 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.227× (z -18.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.341× (z -13.3) |
| [[H4 (line)]] | wt | 226 | 0 | 9 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.118× (z -18.6) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.134× (z -9.9) |
| [[SNU-423 (line)]] | alt | 152 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.201× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.181× (z -10.0) |
| [[C32 (line)]] | wt | 128 | 0 | 7 (3 ⚠) | — | [[Ponatinib (drug)]] 5 µM 0.303× (z -11.7) |
| [[A549 (line)]] | wt | 88.4 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -18.6) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.307× (z -12.2) |
| [[AN3 CA (line)]] | alt | 143 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0647× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.229× (z -9.5) |
| [[HS-578T (line)]] | alt | 202 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.209× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.107× (z -11.9) |
| [[NCI-H23 (line)]] | alt | 227 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.154× (z -24.1) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.184× (z -12.3) |
| [[C-33 A (line)]] | alt | 191 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.243× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.126× (z -12.4) |
| [[HEC-1-A (line)]] | alt | 88.0 | 0 | 5 (2 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.197× (z -9.8) |
| [[NCI-H1792 (line)]] | alt | 114 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.239× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.322× (z -12.4) |
| [[NCI-H2030 (line)]] | alt | 113 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.187× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 0.5 µM 0.400× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 159 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.273× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.198× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 165 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.278× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.569× (z -8.9) |
| [[A-172 (line)]] | wt | 112 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +17.5) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.45× (z +10.0) | [[Niclosamide (olamine) (drug)]] 5 µM 0.426× (z -9.5) ⚠ toxic |
| [[A498 (line)]] | wt | 108 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.313× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.320× (z -9.7) |
| [[HepG2_C3A (line)]] | wt | 82.5 | 1 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +12.4) ⚠ cell-cycle shift, explains ~75% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.272× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Ponatinib (drug)]] 5 µM 0.322× (z -9.6) |
| [[Hs 766T (line)]] | wt | 130 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.286× (z -13.3) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 138 | 0 | 4 (4 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.128× (z -9.8) ⚠ toxic |
| [[LoVo (line)]] | wt | 32.6 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +14.1) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Auranofin (drug)]] 5 µM 4.01× (z +13.1) | — |
| [[SHP-77 (line)]] | alt | 114 | 0 | 4 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.304× (z -11.5) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 119 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.352× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.139× (z -10.2) |
| [[RKO (line)]] | wt | 121 | 0 | 3 | — | [[Selinexor (drug)]] 5 µM 0.366× (z -13.7) |
| [[HT-29 (line)]] | alt | 43.1 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.87× (z +9.1) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.70× (z +8.5) | — |
| [[SW 900 (line)]] | alt | 75.0 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.344× (z -9.3) |
| [[BT-474 (line)]] | alt | 66.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.208× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[HCT15 (line)]] | alt | 90.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.320× (z -8.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 37.8 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.90× (z +9.5) ⚠ cell-cycle shift, explains ~57% of this change | — |
| [[SNU-1 (line)]] | wt | 62.2 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.273× (z -8.6) ⚠ cell-cycle shift, explains ~46% of this change |
| [[SW 1088 (line)]] | alt | 175 | 0 | 1 | — | [[Dimethyl fumarate (drug)]] 5 µM 0.112× (z -8.9) |
| [[SW1417 (line)]] | alt | 47.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -11.8) ⚠ cell-cycle shift, explains ~75% of this change |
| [[SW48 (line)]] | wt | 42.5 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.189× (z -8.5) |
| [[AsPC-1 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 62.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 21.2 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 67.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 22.4 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 87.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 149 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4715), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*39 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZRANB3]] | +0.57 | +0.60 / +0.58 | both halves | 8e-06 |  |
| [[ZNF544]] | +0.56 | +0.44 / +0.61 | both halves | 3e-05 |  |
| [[EEFSEC]] | +0.55 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[PARVB]] | +0.55 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[CCDC18]] | +0.53 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[SCMH1]] | +0.53 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[TTC17]] | +0.52 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[TTC7B]] | +0.52 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[FAM120B]] | +0.52 | +0.49 / +0.55 | both halves | 1e-05 | same gene group |
| [[PIGL]] | +0.51 | +0.54 / +0.46 | both halves | 3e-05 | same gene group |
| [[METTL2B]] | +0.50 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[TANGO6]] | +0.50 | +0.57 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*61 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANXA11]] | -0.65 | -0.66 / -0.62 | both halves | 7e-06 |  |
| [[INAVA]] | -0.57 | -0.62 / -0.54 | both halves | 1e-05 |  |
| [[EPB41L1]] | -0.55 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[KIAA1522]] | -0.55 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[JUP]] | -0.54 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[FOXO4]] | -0.54 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[SPINT1]] | -0.54 | -0.61 / -0.46 | both halves | 3e-05 |  |
| [[OCLN]] | -0.53 | -0.62 / -0.47 | both halves | 2e-05 |  |
| [[LMBRD1]] | -0.53 | -0.52 / -0.49 | both halves | 1e-05 | pathway: Diseases of metabolism |
| [[BPNT1]] | -0.53 | -0.33 / -0.56 | both halves | 1e-04 |  |
| [[NPEPPSP1]] | -0.52 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[ERBB2]] | -0.52 | -0.48 / -0.56 | both halves | 2e-05 | same gene group |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*29 arrows, 29 of them with an alert ⚠; grade A 0, B 29, C 0. Shown: the 12 strongest; 17 more arrows (17 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ST14]] | B | ST14 activity lowers ST3GAL3's level | lines that do not express ST14 (32) vs lines expressing it (18) | 2.82× higher at baseline in the lines without ST14 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1 |
| [[MAL2]] | B | MAL2 activity lowers ST3GAL3's level | lines that do not express MAL2 (31) vs lines expressing it (19) | 2.53× higher at baseline in the lines without MAL2 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RAB25, TMEM125, CDH1 |
| [[INAVA]] | B | INAVA activity lowers ST3GAL3's level | lines that do not express INAVA (29) vs lines expressing it (21) | 2.49× higher at baseline in the lines without INAVA | 2e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[SCNN1A]] | B | SCNN1A activity lowers ST3GAL3's level | lines that do not express SCNN1A (27) vs lines expressing it (23) | 2.43× higher at baseline in the lines without SCNN1A | 4e-04 | ⚠ within organs, on part of the lines; also absent: KDF1, PLEKHG6, CDH1 |
| [[TC2N]] | B | TC2N activity lowers ST3GAL3's level | lines that do not express TC2N (28) vs lines expressing it (22) | 2.55× higher at baseline in the lines without TC2N | 6e-04 | ⚠ within organs, on part of the lines; also absent: CATSPERB, ESRP1, ST14 |
| [[ERBB3]] | B | ERBB3 activity lowers ST3GAL3's level | lines that do not express ERBB3 (27) vs lines expressing it (23) | 2.38× higher at baseline in the lines without ERBB3 | 7e-04 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM |
| [[SLC44A4]] | B | SLC44A4 activity lowers ST3GAL3's level | lines that do not express SLC44A4 (37) vs lines expressing it (13) | 2.65× higher at baseline in the lines without SLC44A4 | 0.001 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC1, LCN2, NPSR1 |
| [[JUP]] | B | JUP activity lowers ST3GAL3's level | lines that do not express JUP (16) vs lines expressing it (34) | 2.20× higher at baseline in the lines without JUP | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: ELF3, SHROOM3, ENSG00000253671 |
| [[SPINT1]] | B | SPINT1 activity lowers ST3GAL3's level | lines that do not express SPINT1 (25) vs lines expressing it (25) | 2.28× higher at baseline in the lines without SPINT1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: MARVELD3, CRB3, SPINT1-AS1 |
| [[ATP8B1]] | B | ATP8B1 activity lowers ST3GAL3's level | lines that do not express ATP8B1 (14) vs lines expressing it (36) | 2.03× higher at baseline in the lines without ATP8B1 | 0.006 | ⚠ within organs, on part of the lines; also absent: LGALS9, CDA, KRT86 |
| [[FRK]] | B | FRK activity weakens ST3GAL3's drug response | lines that do not express FRK (21) vs lines expressing it (26) | the lines without FRK respond 1.56× as strongly (z diff -2.63); strongest at Panobinostat 0.5 µM: 0.61x vs 1.04x (z diff -4.7) | 0.006 | ⚠ within organs, on part of the lines; also absent: GOLT1A, MYO5B, NCMAP; target measured in part of the lines; artifact flags |
| [[WNT5B]] | B | WNT5B activity raises ST3GAL3's level | lines that do not express WNT5B (22) vs lines expressing it (28) | 2.24× lower at baseline in the lines without WNT5B | 0.008 | ⚠ within organs, on part of the lines; also absent: DPY19L2, TRIML2, VASH1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction -0.413). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (7.9, 56.9); signed map (4.9, -56.1). **Vector** length 121, 39.7% of its response variance represented; |z| ≥ 3 in 1,187 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.2 | +1.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.0 | +0.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.9 | +4.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +0.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.4 | -0.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.3 | +1.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +0.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.5 | +1.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.5 | -0.6 |
| fall | [[Selinexor (drug)]] 5 µM |  | -9.0 | -9.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | -6.9 | -11.9 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -6.3 | -5.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -6.0 | -9.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.7 | -7.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.9 | -1.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.8 | -0.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.7 | -3.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.4 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | ST3 beta-galactoside alpha-2,3-sialyltransferase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.1 — chr1:43,705,824-43,931,165 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously SIAT6, MRT12 |
| Gene groups (HGNC) | Sialyltransferases; MicroRNA protein coding host genes |
| Reactome | 33 pathways, smallest: Maturation of protein 3a_9683673; Maturation of protein 3a_9694719; Lewis blood group biosynthesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q11203](https://www.uniprot.org/uniprotkb/Q11203) (CMP-N-acetylneuraminate-beta-1,4-galactoside alpha-2,3-sialyltransferase):

> Catalyzes the formation of the NeuAc-alpha-2,3-Gal-beta-1,4-GlcNAc-, NeuAc-alpha-2,3-Gal-beta-1,3-GlcNAc- and NeuAc-alpha-2,3-Gal-beta-1,3-GalNAc- sequences found in terminal carbohydrate groups of glycoproteins and glycolipids. The highest activity is toward Gal-beta-1,3-GlcNAc and the lowest toward Gal-beta-1,3-GalNAc.

**Summary**, from NCBI Gene [6487](https://www.ncbi.nlm.nih.gov/gene/6487):

> The protein encoded by this gene is a type II membrane protein that catalyzes the transfer of sialic acid from CMP-sialic acid to galactose-containing substrates. The encoded protein is normally found in the Golgi apparatus but can be proteolytically processed to a soluble form. This protein is a member of glycosyltransferase family 29. Mutations in this gene have been associated with a form of autosomal recessive nonsymdromic cognitive disability as well as infantile epileptic encephalopathy. …

**Accessions** — [HGNC:10866](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10866) · Entrez [6487](https://www.ncbi.nlm.nih.gov/gene/6487) · UniProt [Q11203](https://www.uniprot.org/uniprotkb/Q11203) · Ensembl [ENSG00000126091](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126091)

## Data

Gene col 4715: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4715); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4715, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4715]; `tensor/DDL_lfc|DDL_z.npy` [4715]; `embed/gene_vectors.npy` [4715]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4715 or target_col == 4715). Every well: [[ST3GAL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ST3GAL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
