---
symbol: "PTPRJ"
type: "gene"
col: 7345
ensembl_id: "ENSG00000149177"
name: "protein tyrosine phosphatase receptor type J"
location: "11p11.2"
module: 186
arm: "+"
pooled_cpm: 253.6
n_lines_expressing: 48
n_dd_up: 10
n_dd_down: 21
n_dd_up_clean: 8
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/186"]
generated_by: "tahoemap"
---

# PTPRJ

*protein tyrosine phosphatase receptor type J* — 11p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.33× (z +5.0, q 3e-04, up in 25 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.289× (z -21.7, q 0e+00, down in 46 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BMPR1A]] (+0.58, fdr 1e-05), [[PDS5B]] (+0.58, fdr 3e-05), [[EPB41L4B]] (+0.57, fdr 1e-05); moves opposite to [[ZNF502]] (-0.56, fdr 1e-05), [[ZNF140]] (-0.56, fdr 1e-05), [[EDC3]] (-0.55, fdr 3e-05).
> It is in [[Module 186]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LGR4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7345.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.33×** | +5.0 | 3e-04 | 25/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.29×** | +4.5 | 0.002 | 26/46 (SW480, COLO 205, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.27×** | +4.0 | 0.011 | 31/47 (PANC-1, SNU-423, …) | top dose only | plate-row cell shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.26×** | +3.8 | 0.019 | 26/45 (C32, SW480, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.23×** | +3.6 | 0.031 | 25/46 (SW480, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.22×** | +3.4 | 0.062 | 23/45 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.21×** | +3.4 | 0.062 | 20/46 (HOP62, SNU-423, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.21×** | +3.3 | 0.071 | 22/46 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Fumaric acid (drug)]] 5 µM |  | **1.21×** | +3.2 | 0.073 | 22/47 (NCI-H1573, NCI-H2030, …) | top dose only | plate-row cell shift |
| [[Tomivosertib (drug)]] 5 µM |  | **1.42×** | +3.2 | 0.082 | 23/46 (NCI-H1573, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7345.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.289×** | -21.7 | 0e+00 | 46/46 (A549, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.304×** | -20.8 | 0e+00 | 46/46 (A549, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.401×** | -15.4 | 0e+00 | 40/42 (A549, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.426×** | -14.9 | 0e+00 | 46/47 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.431×** | -14.7 | 0e+00 | 43/46 (A549, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.468×** | -12.3 | 1e-32 | 40/43 (C32, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.540×** | -10.7 | 5e-25 | 35/46 (C32, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.531×** | -10.6 | 1e-24 | 43/45 (HepG2/C3A, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.678×** | -6.8 | 8e-10 | 32/46 (C32, HT-29, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.698×** | -6.3 | 2e-08 | 35/46 (A549, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.718×** | -5.8 | 4e-07 | 35/46 (SW480, HT-29, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.803×** | -5.4 | 3e-06 | 33/46 (SW480, SW1417, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.815×** | -5.0 | 2e-05 | 27/46 (HOP62, NCI-H2030, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.772×** | -4.5 | 3e-04 | 26/46 (J82, C32, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.780×** | -4.3 | 5e-04 | 27/47 (NCI-H2347, Hs 766T, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.630×** | -4.2 | 8e-04 | 24/46 (NCI-H1573, H4, …) | top dose only | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.633×** | -4.2 | 9e-04 | 31/45 (NCI-H2347, C-33 A, …) | top dose only | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.700×** | -3.1 | 0.045 | 19/46 (HEC-1-A, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.728×** | -2.9 | 0.091 | 23/46 (A549, H4, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 0.841× | -2.9 | 0.091 | 18/46 (NCI-H2347, LS 180, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7345. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 573 | 0 | 14 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.118× (z -24.4) |
| [[A549 (line)]] | wt | 697 | 0 | 13 (8 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0468× (z -31.9) |
| [[NCI-H1573 (line)]] | alt | 451 | 0 | 13 (8 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0879× (z -22.5) |
| [[LOX-IMVI (line)]] | wt | 253 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.180× (z -19.0) |
| [[NCI-H460 (line)]] | wt | 280 | 0 | 11 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.209× (z -22.5) |
| [[A498 (line)]] | wt | 494 | 3 | 7 (4 ⚠) | [[Triamcinolone (drug)]] 0.5 µM 2.38× (z +9.2) | [[Panobinostat (drug)]] 0.5 µM 0.151× (z -19.9) |
| [[J82 (line)]] | alt | 348 | 0 | 10 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.187× (z -21.4) |
| [[NCI-H2030 (line)]] | alt | 393 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -18.3) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.300× (z -14.2) |
| [[MIA PaCa-2 (line)]] | alt | 257 | 0 | 9 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.117× (z -20.7) |
| [[SW480 (line)]] | alt | 232 | 4 (1 ⚠) | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.23× (z +10.8) | [[Panobinostat (drug)]] 5 µM 0.219× (z -20.4) |
| [[A-172 (line)]] | wt | 156 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -13.9) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.276× (z -13.7) |
| [[SW 900 (line)]] | alt | 179 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.142× (z -18.2) |
| [[LoVo (line)]] | wt | 118 | 4 (4 ⚠) | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +15.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.373× (z -12.4) |
| [[NCI-H2347 (line)]] | alt | 278 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.238× (z -16.3) |
| [[H4 (line)]] | wt | 257 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.151× (z -16.9) |
| [[HOP62 (line)]] | alt | 236 | 0 | 6 | — | [[Panobinostat (drug)]] 0.5 µM 0.192× (z -18.6) |
| [[HT-29 (line)]] | alt | 213 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.276× (z -14.9) |
| [[LS 180 (line)]] | wt | 214 | 1 (1 ⚠) | 5 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.73× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.202× (z -18.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.252× (z -16.8) |
| [[Panc 03.27 (line)]] | alt | 288 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.281× (z -15.0) |
| [[RKO (line)]] | wt | 150 | 1 (1 ⚠) | 5 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.324× (z -12.5) |
| [[SW1417 (line)]] | alt | 311 | 0 | 6 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.313× (z -15.2) |
| [[Hs 766T (line)]] | wt | 271 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.132× (z -18.8) |
| [[KATO III (line)]] | alt | 169 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.257× (z -18.5) |
| [[NCI-H1792 (line)]] | alt | 241 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.222× (z -16.3) |
| [[PANC-1 (line)]] | alt | 240 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.227× (z -17.4) |
| [[AsPC-1 (line)]] | alt | 181 | 1 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +12.4) ⚠ cell-cycle shift, explains ~48% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.292× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.369× (z -8.9) |
| [[HS-578T (line)]] | alt | 211 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.147× (z -18.3) |
| [[RPMI-7951 (line)]] | alt | 151 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.309× (z -11.5) |
| [[SNU-423 (line)]] | alt | 272 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.288× (z -12.2) |
| [[SW48 (line)]] | wt | 150 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.145× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.294× (z -9.3) |
| [[A-427 (line)]] | wt | 101 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.371× (z -11.2) |
| [[C-33 A (line)]] | alt | 131 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.271× (z -12.9) |
| [[CFPAC-1 (line)]] | alt | 214 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.314× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.343× (z -11.2) |
| [[HEC-1-A (line)]] | alt | 167 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.301× (z -15.3) |
| [[SK-MEL-2 (line)]] | alt | 153 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -14.3) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.341× (z -11.9) |
| [[SNU-1 (line)]] | wt | 181 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +10.4) ⚠ cell-cycle shift, explains ~48% of this change | [[Panobinostat (drug)]] 5 µM 0.272× (z -12.4) |
| [[AN3 CA (line)]] | alt | 209 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.225× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.274× (z -9.2) |
| [[BT-474 (line)]] | alt | 197 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +10.4) ⚠ cell-cycle shift, explains ~48% of this change | [[Panobinostat (drug)]] 0.5 µM 0.290× (z -12.3) |
| [[COLO 205 (line)]] | alt | 299 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.302× (z -11.6) |
| [[HCT15 (line)]] | alt | 238 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.496× (z -9.1) ⚠ cell-cycle shift, explains ~48% of this change |
| [[HepG2_C3A (line)]] | wt | 196 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.186× (z -16.6) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 148 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.264× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.350× (z -9.7) |
| [[hTERT-HPNE (line)]] | wt | 97.3 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[CHP-212 (line)]] | wt | 55.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 246 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 58.1 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 265 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 177 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 107 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7345), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*52 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BMPR1A]] | +0.58 | +0.66 / +0.49 | both halves | 1e-05 | same gene group |
| [[PDS5B]] | +0.58 | +0.67 / +0.46 | both halves | 3e-05 |  |
| [[EPB41L4B]] | +0.57 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[SEC61A2]] | +0.56 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[LRP5L]] | +0.56 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[ZMYM2]] | +0.55 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[POU2F1]] | +0.55 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[PDE7A]] | +0.54 | +0.69 / +0.43 | both halves | 4e-05 |  |
| [[PPP2R5E]] | +0.53 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[TBC1D12]] | +0.53 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[RXRA]] | +0.53 | +0.48 / +0.50 | both halves | 2e-05 | same gene group |
| [[SSBP2]] | +0.52 | +0.52 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*48 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF502]] | -0.56 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[ZNF140]] | -0.56 | -0.67 / -0.55 | both halves | 1e-05 |  |
| [[EDC3]] | -0.55 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[ZNF283]] | -0.55 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[ZNF268]] | -0.52 | -0.65 / -0.52 | both halves | 1e-05 |  |
| [[TRIM4]] | -0.51 | -0.65 / -0.50 | both halves | 1e-05 |  |
| [[EXOC8]] | -0.51 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[MTERF4]] | -0.51 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[ZNF23]] | -0.51 | -0.60 / -0.46 | both halves | 3e-05 |  |
| [[MDM4]] | -0.51 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[DDX18]] | -0.50 | -0.62 / -0.40 | both halves | 4e-05 |  |
| [[ZNF229]] | -0.50 | -0.43 / -0.54 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LGR4]] | B | LGR4 activity raises PTPRJ's level | lines that do not express LGR4 (7) vs lines expressing it (43) | 1.79× lower at baseline in the lines without LGR4 | 0.081 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 186]]; 20 genes; every member is in the + arm (projection on the module's main direction 0.696). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-8.0, -6.2); signed map (-20.8, 17.5). **Vector** length 100, 32.6% of its response variance represented; |z| ≥ 3 in 1,547 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +9.1 | +1.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.5 | -0.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.7 | -2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | -0.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.1 | +1.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.9 | +0.4 |
|  | [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | +2.3 | -0.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.2 | -1.6 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +2.2 | +0.8 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -7.9 | -1.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.6 | -10.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.0 | +1.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.2 | -0.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -2.8 | -10.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.6 | -0.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | -6.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.5 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | protein tyrosine phosphatase receptor type J |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p11.2 — chr11:47,980,425-48,170,839 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DEP1, HPTPeta, CD148 |
| Gene groups (HGNC) | CD molecules; Fibronectin type III domain containing; Protein tyrosine phosphatases receptor type; MicroRNA protein coding host genes |
| Hallmark sets | KRAS_SIGNALING_DN |
| Reactome | 11 pathways, smallest: Phosphorylation of CD3 and TCR zeta chains; Negative regulation of FLT3; Negative regulation of MET activity |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12913](https://www.uniprot.org/uniprotkb/Q12913) (Receptor-type tyrosine-protein phosphatase eta):

> Tyrosine phosphatase which dephosphorylates or contributes to the dephosphorylation of CTNND1, FLT3, PDGFRB, MET, KDR, LYN, SRC, MAPK1, MAPK3, EGFR, TJP1, OCLN, PIK3R1 and PIK3R2. Plays a role in cell adhesion, migration, proliferation and differentiation. Has a role in megakaryocytes and platelet formation. Involved in vascular development (By similarity). Regulator of macrophage adhesion and spreading (By similarity). Positively affects cell-matrix adhesion (By similarity). Positive regulator …

**Summary**, from NCBI Gene [5795](https://www.ncbi.nlm.nih.gov/gene/5795):

> The protein encoded by this gene is a member of the protein tyrosine phosphatase (PTP) family. PTPs are known to be signaling molecules that regulate a variety of cellular processes, including cell growth, differentiation, mitotic cycle, and oncogenic transformation. This PTP possesses an extracellular region containing five fibronectin type III repeats, a single transmembrane region, and a single intracytoplasmic catalytic domain, and thus represents a receptor-type PTP. This protein is …

**Accessions** — [HGNC:9673](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9673) · Entrez [5795](https://www.ncbi.nlm.nih.gov/gene/5795) · UniProt [Q12913](https://www.uniprot.org/uniprotkb/Q12913) · Ensembl [ENSG00000149177](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149177)

## Data

Gene col 7345: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7345); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7345, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7345]; `tensor/DDL_lfc|DDL_z.npy` [7345]; `embed/gene_vectors.npy` [7345]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7345 or target_col == 7345). Every well: [[PTPRJ — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTPRJ.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
