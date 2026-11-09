---
symbol: "NSD2"
type: "gene"
col: 3072
ensembl_id: "ENSG00000109685"
name: "nuclear receptor binding SET domain protein 2"
location: "4p16.3"
module: 67
arm: "+"
pooled_cpm: 192.89
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 24
n_dd_up_clean: 1
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# NSD2

*nuclear receptor binding SET domain protein 2* — 4p16.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (8 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.35× (z +8.5, q 1e-14, up in 36 of 48 measured lines) ⚠ cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[Peretinoin (drug)]] 5 µM: 1.22× (z +5.4, q 4e-06, up in 25 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 4 lines (NCI-H1573 2.54×, LoVo 1.89×, NCI-H2347 1.74×, SW 900 2.06×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H1573 2.73×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (LS 180 1.89×; ⚠ cell-cycle shift, explains ~31% of this change).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.525× (z -25.8, q 0e+00, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MELK]] (+0.82, fdr 7e-06), [[VRK1]] (+0.81, fdr 7e-06), [[SPC25]] (+0.78, fdr 7e-06).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PBK]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 12 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3072.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 4 lines (NCI-H1573 2.54×, LoVo 1.89×, NCI-H2347 1.74×, SW 900 2.06×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H1573 2.73×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (LS 180 1.89×; ⚠ cell-cycle shift, explains ~31% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.35×** | +8.5 | 1e-14 | 36/48 (SW480, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.33×** | +8.1 | 2e-13 | 32/48 (NCI-H23, LS 180, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.33×** | +8.0 | 2e-13 | 29/48 (hTERT-HPNE, KATO III, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.29×** | +7.3 | 4e-11 | 35/48 (LS 180, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **1.28×** | +6.6 | 4e-09 | 24/44 (NCI-H1573, LoVo, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **1.26×** | +6.2 | 4e-08 | 32/47 (NCI-H2347, CFPAC-1, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.23×** | +5.9 | 3e-07 | 29/48 (RPMI-7951, H4, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.22×** | +5.4 | 4e-06 | 25/47 (H4, HOP62, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.21×** | +5.3 | 8e-06 | 23/47 (H4, SW 900, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | 1.20× | +5.1 | 2e-05 | 22/47 (H4, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change | 1.19× | +4.8 | 7e-05 | 23/49 (NCI-H1573, CFPAC-1, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~47% of this change | 1.16× | +4.3 | 8e-04 | 19/48 (NCI-H23, SW480, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.04× | +3.6 | 0.014 | 0/50 | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.12× | +3.3 | 0.043 | 9/48 (MIA PaCa-2, SW 900, …) | two highest doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.12× | +3.2 | 0.058 | 14/48 (NCI-H460, MIA PaCa-2, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | 1.12× | +3.0 | 0.093 | 12/48 (SK-MEL-2, H4, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 54 in all, 14 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3072.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.525×** | -25.8 | 0e+00 | 43/48 (A-172, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.446×** | -22.8 | 0e+00 | 44/48 (J82, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.454×** | -22.4 | 0e+00 | 46/48 (J82, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.592×** | -21.0 | 0e+00 | 47/48 (A-427, A-172, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.547×** | -17.1 | 0e+00 | 43/48 (J82, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.551×** | -16.9 | 0e+00 | 44/48 (A-172, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.637×** | -12.8 | 1e-35 | 45/48 (A-172, A-427, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.637×** | -12.3 | 7e-33 | 41/48 (A-172, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.740×** | -12.1 | 1e-31 | 39/48 (J82, NCI-H460, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.660×** | -11.8 | 3e-30 | 37/48 (HOP62, NCI-H460, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.676×** | -10.7 | 8e-25 | 34/47 (J82, RKO, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.728×** | -9.0 | 1e-17 | 33/48 (J82, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.746×** | -8.3 | 4e-15 | 38/49 (HOP62, J82, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.770×** | -7.4 | 5e-12 | 30/48 (A-172, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.769×** | -7.1 | 7e-11 | 29/48 (LOX-IMVI, A-172, …) | inconsistent across doses |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.877× | -5.3 | 5e-06 | 14/48 (A498, LS 180, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.878× | -5.2 | 5e-06 | 17/48 (A-427, HEC-1-A, …) | rises with dose |  |
| [[palbociclib (drug)]] 5 µM |  | **0.711×** | -5.1 | 1e-05 | 25/48 (SK-MEL-2, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3072. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 233 | 0 | 13 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -31.3) |
| [[A-427 (line)]] | wt | 299 | 0 | 13 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -23.2) |
| [[HEC-1-A (line)]] | alt | 337 | 0 | 10 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -20.5) |
| [[J82 (line)]] | alt | 520 | 0 | 10 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.272× (z -24.2) |
| [[LS 180 (line)]] | wt | 155 | 1 (1 ⚠) | 9 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 1.89× (z +8.5) ⚠ cell-cycle shift, explains ~31% of this change | [[Selinexor (drug)]] 5 µM 0.433× (z -15.7) |
| [[SK-MEL-2 (line)]] | alt | 217 | 0 | 10 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.304× (z -16.9) |
| [[HOP62 (line)]] | alt | 327 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -22.9) |
| [[LOX-IMVI (line)]] | wt | 343 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -25.6) |
| [[NCI-H460 (line)]] | wt | 166 | 0 | 9 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.401× (z -17.1) |
| [[A498 (line)]] | wt | 154 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -19.5) |
| [[HS-578T (line)]] | alt | 131 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.313× (z -15.4) |
| [[MIA PaCa-2 (line)]] | alt | 231 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -21.4) |
| [[NCI-H1573 (line)]] | alt | 136 | 2 (2 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -21.6) |
| [[NCI-H2030 (line)]] | alt | 159 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.346× (z -16.8) |
| [[NCI-H23 (line)]] | alt | 211 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -23.7) |
| [[RKO (line)]] | wt | 264 | 0 | 7 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.426× (z -17.2) |
| [[SW480 (line)]] | alt | 195 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.501× (z -17.6) |
| [[C32 (line)]] | wt | 173 | 0 | 6 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.433× (z -13.5) |
| [[PANC-1 (line)]] | alt | 185 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.418× (z -15.9) |
| [[A549 (line)]] | wt | 170 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.368× (z -13.9) |
| [[C-33 A (line)]] | alt | 324 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.314× (z -19.8) |
| [[HT-29 (line)]] | alt | 182 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -17.7) |
| [[SW 900 (line)]] | alt | 165 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 2.06× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | [[Panobinostat (drug)]] 0.5 µM 0.363× (z -12.4) |
| [[SW48 (line)]] | wt | 212 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -14.1) |
| [[H4 (line)]] | wt | 254 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -17.8) |
| [[BT-474 (line)]] | alt | 135 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.392× (z -11.4) |
| [[Panc 03.27 (line)]] | alt | 122 | 0 | 3 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.138× (z -12.0) ⚠ toxic · without an alert: [[Selinexor (drug)]] 5 µM 0.567× (z -9.3) |
| [[SHP-77 (line)]] | alt | 103 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.409× (z -10.6) |
| [[SNU-423 (line)]] | alt | 164 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.483× (z -12.3) |
| [[SW1417 (line)]] | alt | 135 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.408× (z -13.8) |
| [[LoVo (line)]] | wt | 151 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 1.89× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | [[Selinexor (drug)]] 5 µM 0.565× (z -12.1) |
| [[NCI-H2347 (line)]] | alt | 155 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 1.74× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | [[Panobinostat (drug)]] 0.5 µM 0.570× (z -9.2) |
| [[SNU-1 (line)]] | wt | 208 | 0 | 2 | — | [[Selinexor (drug)]] 5 µM 0.396× (z -15.1) |
| [[CFPAC-1 (line)]] | alt | 123 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.518× (z -10.2) |
| [[HCT15 (line)]] | alt | 266 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.539× (z -10.0) |
| [[hTERT-HPNE (line)]] | wt | 143 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -15.1) |
| [[KATO III (line)]] | alt | 138 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.559× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 127 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.486× (z -9.7) |
| [[SW 1088 (line)]] | alt | 103 | 0 | 1 | — | [[Sulfatinib (drug)]] 5 µM 0.0594× (z -9.8) |
| [[AN3 CA (line)]] | alt | 240 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 83.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 93.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 82.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 110 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 117 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 268 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3072), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MELK]] | +0.82 | +0.86 / +0.76 | both halves | 7e-06 |  |
| [[VRK1]] | +0.81 | +0.75 / +0.80 | both halves | 7e-06 |  |
| [[SPC25]] | +0.78 | +0.81 / +0.73 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[DTYMK]] | +0.78 | +0.78 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[WDR62]] | +0.77 | +0.77 / +0.73 | both halves | 7e-06 |  |
| [[CENPN]] | +0.76 | +0.72 / +0.74 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[POLE]] | +0.76 | +0.77 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[LMNB1]] | +0.76 | +0.78 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[FANCA]] | +0.76 | +0.82 / +0.71 | both halves | 7e-06 |  |
| [[CENPK]] | +0.76 | +0.82 / +0.69 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[IQGAP3]] | +0.75 | +0.73 / +0.78 | both halves | 7e-06 |  |
| [[POC1A]] | +0.74 | +0.82 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PBK]] | C | PBK activity raises NSD2's level | lines that do not express PBK (4) vs lines expressing it (46) | 1.79× lower at baseline in the lines without PBK | 0.053 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[PKP4]] | C | PKP4's natural level strengthens NSD2's drug response | PKP4's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.04; direction not clear | 0.076 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[CDCA3]] | C | CDCA3 activity raises NSD2's level | lines that do not express CDCA3 (3) vs lines expressing it (47) | 1.96× lower at baseline in the lines without CDCA3 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.734). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-35.0, -51.1); signed map (-43.8, -42.6). **Vector** length 149, 57.6% of its response variance represented; |z| ≥ 3 in 1,659 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.64 to 12); *Mitotic Prometaphase* (reactome, mean cos +0.62 to 8); *Deposition of new CENPA-containing nucleosomes at the centromere* (reactome, mean cos +0.55 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +7.6 | +2.9 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | +6.6 | +5.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | +5.8 | +6.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +5.6 | +7.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +5.6 | +8.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.8 | +5.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.7 | +3.2 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | +2.7 | +1.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.5 | +1.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.5 | +1.4 |
| fall | [[Selinexor (drug)]] 5 µM |  | -12.8 | -21.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -9.9 | -12.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.2 | -16.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.6 | -11.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.3 | -25.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.7 | -12.1 |
|  | [[palbociclib (drug)]] 5 µM |  | -4.1 | -5.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -4.1 | -3.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -4.0 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | nuclear receptor binding SET domain protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.3 — chr4:1,871,393-1,982,207 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MMSET, KMT3G; previously WHSC1 |
| Gene groups (HGNC) | PHD finger proteins; Histone lysine methyltransferases; PWWP domain containing; SET domain containing |
| Hallmark sets | G2M_CHECKPOINT |
| Reactome | 15 pathways, smallest: PKMTs methylate histone lysines; Nonhomologous End-Joining (NHEJ); Recruitment and ATM-mediated phosphorylation of repair and signaling proteins at DNA double strand breaks |
| Matched by | ensembl_id |

**Function**, from UniProt [O96028](https://www.uniprot.org/uniprotkb/O96028) (Histone-lysine N-methyltransferase NSD2):

> Histone methyltransferase which specifically dimethylates nucleosomal histone H3 at 'Lys-36' (H3K36me2). Also monomethylates nucleosomal histone H3 at 'Lys-36' (H3K36me) in vitro. Does not trimethylate nucleosomal histone H3 at 'Lys-36' (H3K36me3). However, specifically trimethylates histone H3 at 'Lys-36' (H3K36me3) at euchromatic regions in embryonic stem (ES) cells (By similarity). By methylating histone H3 at 'Lys-36', involved in the regulation of gene transcription during various …

**Summary**, from NCBI Gene [7468](https://www.ncbi.nlm.nih.gov/gene/7468):

> This gene encodes a protein that contains four domains present in other developmental proteins: a PWWP domain, an HMG box, a SET domain, and a PHD-type zinc finger. It is expressed ubiquitously in early development. Wolf-Hirschhorn syndrome (WHS) is a malformation syndrome associated with a hemizygous deletion of the distal short arm of chromosome 4. This gene maps to the 165 kb WHS critical region and has also been involved in the chromosomal translocation t(4;14)(p16.3;q32.3) in multiple …

**Accessions** — [HGNC:12766](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12766) · Entrez [7468](https://www.ncbi.nlm.nih.gov/gene/7468) · UniProt [O96028](https://www.uniprot.org/uniprotkb/O96028) · Ensembl [ENSG00000109685](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109685)

## Data

Gene col 3072: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3072); `tables/drug_effects.parquet` (70 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3072, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3072]; `tensor/DDL_lfc|DDL_z.npy` [3072]; `embed/gene_vectors.npy` [3072]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3072 or target_col == 3072). Every well: [[NSD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NSD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
