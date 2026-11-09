---
symbol: "PIAS2"
type: "gene"
col: 1203
ensembl_id: "ENSG00000078043"
name: "protein inhibitor of activated STAT 2"
location: "18q21.1"
module: 144
arm: "+"
pooled_cpm: 152.5
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 14
n_dd_up_clean: 4
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/144"]
generated_by: "tahoemap"
---

# PIAS2

*protein inhibitor of activated STAT 2* — 18q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.69× (z +9.0, q 1e-16, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.405× (z -15.6, q 0e+00, down in 46 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.634× (z -7.9, q 4e-13, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDK3]] (+0.67, fdr 7e-06), [[NDUFB8]] (+0.66, fdr 1e-05), [[PRELID2]] (+0.64, fdr 1e-05); moves opposite to [[C3orf62]] (-0.49, fdr 3e-05), [[BNIP2]] (-0.45, fdr 4e-05).
> It is in [[Module 144]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[NRN1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1203.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.69×** | +9.0 | 1e-16 | 39/48 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.68×** | +4.7 | 5e-04 | 32/49 (C32, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.31×** | +4.7 | 5e-04 | 29/48 (PANC-1, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.26×** | +4.0 | 0.007 | 24/48 (KATO III, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.26×** | +4.0 | 0.007 | 28/48 (PANC-1, SW1417, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.20× | +3.2 | 0.13 | 22/48 (AsPC-1, CFPAC-1, …) | inconsistent across doses |  |
| [[Roxadustat (drug)]] 5 µM |  | 1.21× | +3.1 | 0.15 | 22/48 (SHP-77, NCI-H460, …) | top dose only |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 1.13× | +3.1 | 0.16 | 5/48 (SHP-77, SW 900, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1203.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.405×** | -15.6 | 0e+00 | 46/49 (MIA PaCa-2, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.424×** | -14.3 | 1e-43 | 42/44 (NCI-H1792, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.496×** | -11.2 | 7e-27 | 39/45 (SK-MEL-2, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.536×** | -10.4 | 5e-23 | 44/47 (MIA PaCa-2, J82, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.634×** | -7.9 | 4e-13 | 39/48 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.639×** | -7.7 | 9e-13 | 34/48 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.753×** | -6.9 | 4e-10 | 32/49 (NCI-H1792, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.684×** | -6.6 | 4e-09 | 37/48 (C32, HOP62, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.717×** | -5.8 | 6e-07 | 39/48 (PANC-1, C32, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.718×** | -5.5 | 2e-06 | 27/47 (C32, SNU-423, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.762×** | -4.7 | 1e-04 | 29/48 (MIA PaCa-2, C32, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.770×** | -4.5 | 3e-04 | 27/48 (C32, NCI-H460, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.795×** | -4.0 | 0.003 | 26/48 (NCI-H1792, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.859× | -3.7 | 0.008 | 19/48 (HepG2/C3A, NCI-H2347, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.873× | -3.3 | 0.034 | 7/48 (SW 1088, SK-MEL-2, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.731×** | -3.2 | 0.054 | 25/48 (NCI-H661, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.840× | -3.0 | 0.085 | 21/48 (H4, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1203. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 342 | 0 | 15 (9 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.260× (z -15.6) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.307× (z -14.2) |
| [[MIA PaCa-2 (line)]] | alt | 499 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.191× (z -20.4) ⚠ toxic; transcription drop · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.361× (z -12.5) |
| [[NCI-H1792 (line)]] | alt | 452 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.123× (z -23.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -18.0) |
| [[NCI-H460 (line)]] | wt | 182 | 3 | 5 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.25× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.373× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.441× (z -9.8) |
| [[HepG2_C3A (line)]] | wt | 161 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.319× (z -9.7) |
| [[PANC-1 (line)]] | alt | 118 | 4 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.93× (z +15.3) | [[Dinaciclib (drug)]] 5 µM 0.462× (z -10.6) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 189 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.242× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -13.5) |
| [[J82 (line)]] | alt | 255 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.221× (z -18.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.471× (z -9.1) |
| [[SW480 (line)]] | alt | 73.1 | 1 | 4 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.87× (z +9.8) | [[Dinaciclib (drug)]] 0.05 µM 0.444× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.532× (z -9.9) |
| [[H4 (line)]] | wt | 225 | 2 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.68× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.298× (z -11.4) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 203 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.364× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.394× (z -9.4) |
| [[Hs 766T (line)]] | wt | 144 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.232× (z -13.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 88.3 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.98× (z +12.8) | — |
| [[NCI-H2347 (line)]] | alt | 135 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.277× (z -13.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 191 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.282× (z -14.4) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 84.6 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +11.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.57× (z +11.0) | [[Dinaciclib (drug)]] 0.05 µM 0.449× (z -8.6) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 405 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.242× (z -13.9) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 116 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.383× (z -10.0) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 125 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.06× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.473× (z -9.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 150 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.151× (z -20.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.430× (z -13.6) |
| [[SNU-1 (line)]] | wt | 230 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.180× (z -16.2) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 113 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.366× (z -9.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 140 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.334× (z -10.4) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 304 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 205 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.247× (z -9.3) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 52.5 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.78× (z +10.2) | — |
| [[HS-578T (line)]] | alt | 141 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.405× (z -9.9) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 107 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.194× (z -12.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 138 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.23× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.389× (z -11.4) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 242 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.258× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.521× (z -9.9) |
| [[RPMI-7951 (line)]] | alt | 203 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.256× (z -13.3) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 255 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.334× (z -11.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 104 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.225× (z -17.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 38.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +20.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[AsPC-1 (line)]] | alt | 67.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +9.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[BT-474 (line)]] | alt | 187 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.492× (z -10.4) |
| [[HEC-1-A (line)]] | alt | 136 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.399× (z -11.2) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 70.8 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.392× (z -10.0) |
| [[SW 1088 (line)]] | alt | 189 | 0 | 1 | — | [[Decitabine (drug)]] 0.5 µM 0.0841× (z -11.6) |
| [[SW48 (line)]] | wt | 191 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.345× (z -10.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 66.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 83.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 97.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 126 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 67.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 95.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1203), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDK3]] | +0.67 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[NDUFB8]] | +0.66 | +0.70 / +0.52 | both halves | 1e-05 |  |
| [[PRELID2]] | +0.64 | +0.57 / +0.66 | both halves | 1e-05 | **novel candidate** |
| [[PEX3]] | +0.64 | +0.70 / +0.54 | both halves | 1e-05 |  |
| [[RBPJ]] | +0.61 | +0.66 / +0.57 | both halves | 9e-06 |  |
| [[PDK1]] | +0.61 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[FAM162A]] | +0.61 | +0.70 / +0.54 | both halves | 1e-05 |  |
| [[HELZ]] | +0.60 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[ZMYM2]] | +0.60 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[SMAD9]] | +0.59 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[EGLN1]] | +0.59 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[TET1]] | +0.59 | +0.59 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C3orf62]] | -0.49 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[BNIP2]] | -0.45 | -0.45 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NRN1]] | B | NRN1 activity strengthens PIAS2's drug response | lines that do not express NRN1 (27) vs lines expressing it (22) | the lines without NRN1 respond 0.78× as strongly (z diff +1.28); strongest at Panobinostat 5 µM: 0.79x vs 0.57x (z diff +3.7) | 0.041 | ⚠ within organs, on part of the lines; also absent: ILDR2, PHACTR1, ENSG00000250137; target measured in part of the lines; artifact flags |
| [[TET1]] | B | TET1 activity raises PIAS2's level | lines that do not express TET1 (12) vs lines expressing it (38) | 1.79× lower at baseline in the lines without TET1 | 0.072 | ⚠ within organs, on part of the lines; also absent: PLEKHO1, MCAM, KCNK13; maybe low, not absent |
| [[APLN]] | B | APLN activity raises PIAS2's level | lines that do not express APLN (13) vs lines expressing it (37) | 1.30× lower at baseline in the lines without APLN | 0.073 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[NRN1]] | B | NRN1 activity raises PIAS2's level | lines that do not express NRN1 (27) vs lines expressing it (23) | 1.28× lower at baseline in the lines without NRN1 | 0.076 | ⚠ within organs, on part of the lines; also absent: ILDR2, PHACTR1, ENSG00000250137 |
| [[SMAD9]] | B | SMAD9 activity raises PIAS2's level | lines that do not express SMAD9 (11) vs lines expressing it (39) | 1.66× lower at baseline in the lines without SMAD9 | 0.081 | ⚠ within organs, on part of the lines; also absent: FAM184A, SAMD11, HHIPL2 |
| [[SAP30]] | C | SAP30's natural level strengthens PIAS2's drug response | SAP30's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.62, reverse -0.11; direction not clear | 0.074 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PFKFB4]] | C | PFKFB4's natural level strengthens PIAS2's drug response | PFKFB4's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.61, reverse +0.46; direction not clear | 0.097 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 144]]; 32 genes; every member is in the + arm (projection on the module's main direction 0.649). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.4, -18.2); signed map (-37.9, 23.7). **Vector** length 110, 37.4% of its response variance represented; |z| ≥ 3 in 1,125 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | +1.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | -6.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | +0.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.2 | -15.6 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.2 | +1.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.7 | +1.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | -1.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.5 | +1.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.4 | +0.5 |
| fall | [[GSK1059615 (drug)]] 5 µM |  | -5.1 | -1.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.6 | -1.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | -1.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.7 | -5.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.6 | -4.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.1 | -1.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.7 | -2.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.4 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | protein inhibitor of activated STAT 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q21.1 — chr18:46,803,218-46,920,160 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PIASX-BETA, miz, PIASX-ALPHA, ZMIZ4, ARIP3 |
| Gene groups (HGNC) | Zinc fingers MIZ-type |
| Hallmark sets | SPERMATOGENESIS |
| Reactome | 10 pathways, smallest: SUMOylation of transcription factors; SUMOylation of intracellular receptors; SUMOylation of ubiquitinylation proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [O75928](https://www.uniprot.org/uniprotkb/O75928) (E3 SUMO-protein ligase PIAS2):

> Functions as an E3-type small ubiquitin-like modifier (SUMO) ligase, stabilizing the interaction between UBE2I and the substrate, and as a SUMO-tethering factor. Plays a crucial role as a transcriptional coregulator in various cellular pathways, including the STAT pathway, the p53 pathway and the steroid hormone signaling pathway. The effects of this transcriptional coregulation, transactivation or silencing may vary depending upon the biological context and the PIAS2 isoform studied. However, …

**Summary**, from NCBI Gene [9063](https://www.ncbi.nlm.nih.gov/gene/9063):

> This gene encodes a member of the protein inhibitor of activated STAT family, which function as SUMO E3 ligases and play important roles in many cellular processes by mediating the sumoylation of target proteins. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. Isoforms of the encoded protein enhance the sumoylation of specific target proteins including the p53 tumor suppressor protein, c-Jun, and the androgen receptor. A pseudogene of this …

**Accessions** — [HGNC:17311](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17311) · Entrez [9063](https://www.ncbi.nlm.nih.gov/gene/9063) · UniProt [O75928](https://www.uniprot.org/uniprotkb/O75928) · Ensembl [ENSG00000078043](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000078043)

## Data

Gene col 1203: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1203); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1203, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1203]; `tensor/DDL_lfc|DDL_z.npy` [1203]; `embed/gene_vectors.npy` [1203]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1203 or target_col == 1203). Every well: [[PIAS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIAS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
