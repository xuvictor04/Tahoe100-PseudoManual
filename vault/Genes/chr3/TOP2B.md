---
symbol: "TOP2B"
type: "gene"
col: 1173
ensembl_id: "ENSG00000077097"
name: "DNA topoisomerase II beta"
location: "3p24.2"
module: 3
arm: "-"
pooled_cpm: 152.48
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 11
n_dd_up_clean: 6
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 129
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# TOP2B

*DNA topoisomerase II beta* — 3p24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.77× (z +14.0, q 7e-42, up in 42 of 48 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.60× (z +8.2, q 5e-14, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.601× (z -8.9, q 5e-16, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAD21]] (+0.67, fdr 7e-06), [[FH]] (+0.65, fdr 1e-05), [[MATR3]] (+0.63, fdr 7e-06); moves opposite to [[RABIF]] (-0.62, fdr 1e-05), [[C19orf25]] (-0.60, fdr 7e-06), [[VPS37C]] (-0.59, fdr 2e-05).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ALDH1A1]] → it (grade B ⚠); 129 go from it, the strongest it → [[MFSD14CP-1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1173.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.77×** | +14.0 | 7e-42 | 42/48 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.64×** | +8.2 | 5e-14 | 42/48 (PANC-1, HEC-1-A, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.60×** | +8.2 | 5e-14 | 38/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.35×** | +7.7 | 1e-12 | 44/48 (SW48, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.49×** | +6.9 | 7e-10 | 32/48 (HEC-1-A, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.48×** | +6.8 | 1e-09 | 32/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.09×** | +6.7 | 2e-09 | 43/49 (PANC-1, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +6.1 | 8e-08 | 38/47 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.34×** | +5.1 | 3e-05 | 31/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.31×** | +4.7 | 1e-04 | 32/48 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change | **1.28×** | +4.1 | 0.002 | 23/44 (NCI-H23, HT-29, …) | rises with dose | composition shift |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.26×** | +3.8 | 0.007 | 32/49 (NCI-H460, HOP62, …) | top dose only | plate-row cell shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.24×** | +3.7 | 0.010 | 26/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **1.22×** | +3.4 | 0.029 | 20/48 (LOX-IMVI, SW 1271, …) | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1173.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.601×** | -8.9 | 5e-16 | 45/48 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.642×** | -7.7 | 4e-12 | 42/48 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **0.704×** | -5.9 | 8e-07 | 39/47 (SW480, C-33 A, …) | rises with dose |  |
| [[Thymol (drug)]] 0.5 µM |  | **0.750×** | -5.0 | 8e-05 | 35/48 (HT-29, Hs 766T, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.758×** | -4.8 | 2e-04 | 30/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.837× | -4.4 | 0.001 | 21/48 (SW1417, KATO III, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.785×** | -4.2 | 0.002 | 32/48 (MIA PaCa-2, NCI-H2030, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.742×** | -3.7 | 0.015 | 33/48 (LoVo, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.671×** | -3.6 | 0.018 | 24/48 (HCT15, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.770×** | -3.3 | 0.064 | 23/48 (SW480, A-427, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.771×** | -3.2 | 0.064 | 22/47 (COLO 205, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.707×** | -3.2 | 0.075 | 20/48 (RPMI-7951, NCI-H661, …) | rises with dose | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | 0.835× | -3.1 | 0.075 | 20/48 (AN3 CA, SW48, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.838× | -3.1 | 0.081 | 17/48 (HCT15, AN3 CA, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1173. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 161 | 7 (5 ⚠) | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.01× (z +16.4) | [[Panobinostat (drug)]] 5 µM 0.428× (z -12.6) |
| [[HOP62 (line)]] | alt | 206 | 7 (6 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +12.4) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.95× (z +12.3) | [[Panobinostat (drug)]] 0.5 µM 0.466× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 121 | 6 (5 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.93× (z +15.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.59× (z +13.7) | — |
| [[PANC-1 (line)]] | alt | 91.8 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +20.3) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.14× (z +10.7) | — |
| [[LS 180 (line)]] | wt | 180 | 5 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.52× (z +16.2) | — |
| [[HEC-1-A (line)]] | alt | 216 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +17.8) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.34× (z +10.0) | — |
| [[NCI-H1792 (line)]] | alt | 173 | 4 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.01× (z +12.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.69× (z +10.9) | — |
| [[KATO III (line)]] | alt | 113 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.61× (z +12.5) | — |
| [[SHP-77 (line)]] | alt | 241 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.464× (z -10.3) |
| [[SW1417 (line)]] | alt | 250 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +11.5) ⚠ cell-cycle shift, explains ~36% of this change | [[Panobinostat (drug)]] 0.5 µM 0.506× (z -8.9) |
| [[SW48 (line)]] | wt | 253 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.22× (z +11.8) | — |
| [[A-427 (line)]] | wt | 160 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +12.1) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[A549 (line)]] | wt | 186 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +16.0) ⚠ cell-cycle shift, explains ~36% of this change | [[Dinaciclib (drug)]] 5 µM 0.420× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change |
| [[AsPC-1 (line)]] | alt | 97.4 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +9.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LoVo (line)]] | wt | 145 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.10× (z +11.1) | — |
| [[NCI-H1573 (line)]] | alt | 100 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.36× (z +10.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.78× (z +9.0) | — |
| [[A-172 (line)]] | wt | 169 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +11.3) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[A498 (line)]] | wt | 113 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +12.6) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[AN3 CA (line)]] | alt | 468 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 193 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +16.0) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[C-33 A (line)]] | alt | 280 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.443× (z -9.3) ⚠ toxic; cell-cycle shift, explains ~25% of this change |
| [[CFPAC-1 (line)]] | alt | 74.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +10.0) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[H4 (line)]] | wt | 94.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +11.2) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[HepG2_C3A (line)]] | wt | 143 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +12.2) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[HT-29 (line)]] | alt | 72.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +14.1) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 127 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2030 (line)]] | alt | 143 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.62× (z +8.6) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[NCI-H23 (line)]] | alt | 183 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +10.7) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 148 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +10.1) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[SNU-1 (line)]] | wt | 250 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.165× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change |
| [[SW 1088 (line)]] | alt | 118 | 0 | 1 | — | [[Doxycycline (monohydrate) (drug)]] 0.05 µM 0.0792× (z -9.7) |
| [[C32 (line)]] | wt | 146 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 182 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 105 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 175 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 133 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 142 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 209 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 217 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 185 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 241 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 130 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1173), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAD21]] | +0.67 | +0.63 / +0.68 | both halves | 7e-06 | pathway: SUMO E3 ligases SUMOylate target proteins; STRING 620 |
| [[FH]] | +0.65 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[MATR3]] | +0.63 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[COX11]] | +0.63 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[ANP32A]] | +0.62 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[UBR5]] | +0.62 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[CILK1]] | +0.61 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[HNRNPA1L3]] | +0.61 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[HNRNPH3]] | +0.61 | +0.45 / +0.68 | both halves | 3e-05 |  |
| [[HMGN1]] | +0.60 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[HDAC2]] | +0.59 | +0.64 / +0.55 | both halves | 1e-05 | pathway: SUMO E3 ligases SUMOylate target proteins; STRING 692 |
| [[KIF5B]] | +0.57 | +0.48 / +0.57 | both halves | 2e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RABIF]] | -0.62 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[C19orf25]] | -0.60 | -0.58 / -0.60 | both halves | 7e-06 |  |
| [[VPS37C]] | -0.59 | -0.46 / -0.57 | both halves | 2e-05 |  |
| [[POLR2J4]] | -0.58 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[ISG20L2]] | -0.57 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[GPR89B]] | -0.55 | -0.38 / -0.61 | both halves | 7e-05 |  |
| [[ZBTB43]] | -0.55 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[VRK3]] | -0.55 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[OGG1]] | -0.55 | -0.50 / -0.56 | both halves | 1e-05 | STRING 481 |
| [[RRP7BP-1]] | -0.55 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[FBXL12]] | -0.54 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[MTF1]] | -0.54 | -0.44 / -0.58 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ALDH1A1]] | B | ALDH1A1 activity lowers TOP2B's level | lines that do not express ALDH1A1 (36) vs lines expressing it (14) | 1.41× higher at baseline in the lines without ALDH1A1 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AKR1B10, FGA, GCG |

### Downstream of this gene

*129 arrows, 129 of them with an alert ⚠; grade A 0, B 129, C 0. Shown: the 12 strongest; 117 more arrows (117 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MFSD14CP-1]] | B | TOP2B activity lowers MFSD14CP-1's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[HDAC4]] | B | TOP2B activity lowers HDAC4's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[APPAT]] | B | TOP2B activity lowers APPAT's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[ENSG00000227407]] | B | TOP2B activity lowers ENSG00000227407's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[GOSR2]] | B | TOP2B activity lowers GOSR2's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[LINC02018]] | B | TOP2B activity lowers LINC02018's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[PSKH1]] | B | TOP2B activity lowers PSKH1's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[RAB28]] | B | TOP2B activity lowers RAB28's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[STX16-NPEPL1]] | B | TOP2B activity lowers STX16-NPEPL1's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[UBE2S]] | B | TOP2B activity raises UBE2S's level | compounds that target TOP2B: 2 of 2 lower it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[DLD]] | B | TOP2B activity raises DLD's level | compounds that target TOP2B: 2 of 2 lower it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[DPH7]] | B | TOP2B activity raises DPH7's level | compounds that target TOP2B: 2 of 2 lower it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.488). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-35.1, -24.1); signed map (14.4, -36.2). **Vector** length 116, 40.4% of its response variance represented; |z| ≥ 3 in 1,204 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +9.5 | +2.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change | +8.8 | +4.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +8.3 | +0.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.9 | +1.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +5.3 | +14.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.9 | +1.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.2 | -0.7 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +2.5 | +0.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.5 | +1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.4 | +0.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.6 | -4.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | -5.2 | -5.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -5.0 | +3.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.8 | -2.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -4.8 | +5.1 |
|  | [[EX229 (drug)]] 5 µM |  | -4.7 | -3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.6 | -2.7 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -4.3 | -3.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.3 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | DNA topoisomerase II beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p24.2 — chr3:25,597,978-25,664,909 (-) |
| Ensembl biotype | protein_coding |
| Also known as | top2beta, TOPIIB |
| Gene groups (HGNC) | Topoisomerases |
| Reactome | 3 pathways, smallest: SUMOylation of DNA replication proteins; SUMO E3 ligases SUMOylate target proteins; SUMOylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q02880](https://www.uniprot.org/uniprotkb/Q02880) (DNA topoisomerase 2-beta):

> Key decatenating enzyme that alters DNA topology by binding to two double-stranded DNA molecules, generating a double-stranded break in one of the strands, passing the intact strand through the broken strand, and religating the broken strand. Plays a role in B-cell differentiation.

**Summary**, from NCBI Gene [7155](https://www.ncbi.nlm.nih.gov/gene/7155):

> This gene encodes a DNA topoisomerase, an enzyme that controls and alters the topologic states of DNA during transcription. This nuclear enzyme is involved in processes such as chromosome condensation, chromatid separation, and the relief of torsional stress that occurs during DNA transcription and replication. It catalyzes the transient breaking and rejoining of two strands of duplex DNA which allows the strands to pass through one another, thus altering the topology of DNA. Two forms of this …

**Accessions** — [HGNC:11990](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11990) · Entrez [7155](https://www.ncbi.nlm.nih.gov/gene/7155) · UniProt [Q02880](https://www.uniprot.org/uniprotkb/Q02880) · Ensembl [ENSG00000077097](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000077097)

## Data

Gene col 1173: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1173); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1173, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1173]; `tensor/DDL_lfc|DDL_z.npy` [1173]; `embed/gene_vectors.npy` [1173]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1173 or target_col == 1173). Every well: [[TOP2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TOP2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
