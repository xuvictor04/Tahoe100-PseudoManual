---
symbol: "PFKFB4"
type: "gene"
col: 3534
ensembl_id: "ENSG00000114268"
name: "6-phosphofructo-2-kinase/fructose-2,6-biphosphatase 4"
location: "3p21.31"
module: 99
arm: "+"
pooled_cpm: 158.13
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 38
n_dd_up_clean: 6
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 8
direction_downstream: 3
tags: ["gene", "module/099"]
generated_by: "tahoemap"
---

# PFKFB4

*6-phosphofructo-2-kinase/fructose-2,6-biphosphatase 4* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Dimethyl fumarate (drug)]] 5 µM: 1.46× (z +4.7, q 0.001, up in 41 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 38 drug-doses (14 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.211× (z -19.4, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[INSIG2]] (+0.81, fdr 7e-06), [[PDK3]] (+0.80, fdr 7e-06), [[HILPDA]] (+0.77, fdr 7e-06); moves opposite to [[AVEN]] (-0.65, fdr 4e-05), [[ITPA]] (-0.58, fdr 1e-04), [[SLC25A13]] (-0.57, fdr 2e-05).
> It is in [[Module 099]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 3 go from it, the strongest it → [[CEP250]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3534.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.46×** | +4.7 | 0.001 | 41/49 (COLO 205, NCI-H460, …) | top dose only | plate-row cell shift |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.25×** | +4.1 | 0.012 | 26/48 (SNU-1, COLO 205, …) | rises with dose |  |
| [[Fumaric acid (drug)]] 5 µM |  | **1.36×** | +3.8 | 0.018 | 36/49 (HT-29, NCI-H2347, …) | top dose only | plate-row cell shift |
| [[Anethole trithione (drug)]] 5 µM |  | **1.23×** | +3.8 | 0.018 | 23/48 (SHP-77, LS 180, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **1.35×** | +3.8 | 0.018 | 31/48 (PANC-1, NCI-H2347, …) | top dose only | plate-row cell shift |
| [[Pimitespib (drug)]] 0.05 µM |  | **1.32×** | +3.4 | 0.057 | 24/48 (SNU-423, A-172, …) | all doses, flat | position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **1.31×** | +3.3 | 0.066 | 31/49 (C-33 A, HepG2/C3A, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.27× | +3.0 | 0.18 | 24/47 (LoVo, LOX-IMVI, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 15 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 38 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3534.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.211×** | -19.4 | 0e+00 | 44/48 (MIA PaCa-2, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.373×** | -18.1 | 0e+00 | 48/49 (RPMI-7951, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.235×** | -18.1 | 0e+00 | 46/47 (NCI-H23, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.267×** | -17.1 | 0e+00 | 43/49 (CHP-212, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.355×** | -12.9 | 2e-36 | 38/44 (A-172, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.369×** | -12.9 | 2e-36 | 40/48 (NCI-H2347, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.384×** | -11.9 | 6e-31 | 42/47 (RPMI-7951, HOP62, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.537×** | -11.4 | 3e-28 | 31/48 (C32, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.567×** | -10.4 | 1e-23 | 46/48 (NCI-H2347, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.438×** | -9.9 | 2e-21 | 35/45 (NCI-H23, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.611×** | -9.0 | 9e-18 | 43/48 (Hs 766T, AN3 CA, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.495×** | -8.8 | 9e-17 | 41/48 (SNU-423, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.591×** | -6.8 | 4e-10 | 43/48 (SW 900, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.585×** | -6.7 | 9e-10 | 36/50 (RPMI-7951, HS-578T, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.622×** | -6.2 | 3e-08 | 40/48 (AN3 CA, C32, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.628×** | -6.0 | 5e-08 | 39/48 (C-33 A, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.648×** | -5.6 | 6e-07 | 34/48 (LS 180, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.681×** | -5.0 | 2e-05 | 29/48 (HEC-1-A, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.693×** | -4.8 | 5e-05 | 33/48 (C32, MIA PaCa-2, …) | top dose only |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.779×** | -4.6 | 1e-04 | 35/48 (HOP62, NCI-H1792, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.717×** | -4.3 | 4e-04 | 31/48 (SK-MEL-2, RPMI-7951, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.719×** | -4.3 | 4e-04 | 27/48 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.40 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3534. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 660 | 0 | 16 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -23.4) |
| [[HS-578T (line)]] | alt | 237 | 1 | 13 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.160× (z -22.9) |
| [[HEC-1-A (line)]] | alt | 185 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -19.3) |
| [[NCI-H2347 (line)]] | alt | 212 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -20.4) |
| [[RPMI-7951 (line)]] | alt | 467 | 0 | 12 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0951× (z -31.2) |
| [[SK-MEL-2 (line)]] | alt | 587 | 0 | 11 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.227× (z -17.2) |
| [[SNU-423 (line)]] | alt | 289 | 0 | 11 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.152× (z -24.5) |
| [[CFPAC-1 (line)]] | alt | 189 | 0 | 10 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.263× (z -18.5) |
| [[HCT15 (line)]] | alt | 294 | 0 | 9 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0665× (z -19.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.151× (z -13.2) |
| [[Hs 766T (line)]] | wt | 138 | 0 | 9 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.118× (z -16.7) |
| [[MIA PaCa-2 (line)]] | alt | 207 | 0 | 9 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0492× (z -26.2) |
| [[NCI-H1792 (line)]] | alt | 239 | 0 | 9 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.165× (z -25.4) |
| [[AN3 CA (line)]] | alt | 186 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -17.1) |
| [[SW480 (line)]] | alt | 116 | 0 | 8 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.173× (z -16.2) |
| [[A-172 (line)]] | wt | 140 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0628× (z -23.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -10.6) |
| [[HOP62 (line)]] | alt | 406 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.196× (z -20.5) |
| [[LOX-IMVI (line)]] | wt | 143 | 0 | 7 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.103× (z -19.5) |
| [[SW 900 (line)]] | alt | 137 | 0 | 7 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.121× (z -18.3) |
| [[C-33 A (line)]] | alt | 212 | 0 | 6 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.118× (z -13.4) |
| [[H4 (line)]] | wt | 204 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.177× (z -17.0) |
| [[HepG2_C3A (line)]] | wt | 174 | 0 | 5 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.140× (z -16.1) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -14.8) |
| [[J82 (line)]] | alt | 192 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +11.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.257× (z -19.7) |
| [[LS 180 (line)]] | wt | 75.2 | 0 | 5 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.140× (z -14.7) |
| [[NCI-H23 (line)]] | alt | 116 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.108× (z -19.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.132× (z -17.9) |
| [[BT-474 (line)]] | alt | 93.2 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.175× (z -12.8) |
| [[CHP-212 (line)]] | wt | 308 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0369× (z -20.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.232× (z -12.7) |
| [[HT-29 (line)]] | alt | 63.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -15.7) |
| [[hTERT-HPNE (line)]] | wt | 150 | 0 | 4 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.161× (z -12.1) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -11.3) |
| [[NCI-H1573 (line)]] | alt | 87.9 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0863× (z -18.2) |
| [[NCI-H2030 (line)]] | alt | 82.7 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.221× (z -14.0) |
| [[NCI-H460 (line)]] | wt | 119 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.142× (z -15.2) |
| [[Panc 03.27 (line)]] | alt | 83.3 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -16.0) |
| [[PANC-1 (line)]] | alt | 90.4 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.214× (z -12.6) |
| [[SHP-77 (line)]] | alt | 110 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -10.7) |
| [[SNU-1 (line)]] | wt | 155 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.130× (z -12.7) |
| [[A-427 (line)]] | wt | 62.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.221× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.309× (z -8.7) |
| [[A549 (line)]] | wt | 105 | 0 | 3 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.288× (z -10.2) ⚠ toxic · without an alert: [[Selinexor (drug)]] 5 µM 0.442× (z -9.9) |
| [[AsPC-1 (line)]] | alt | 58.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -9.6) |
| [[KATO III (line)]] | alt | 44.9 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.138× (z -14.2) |
| [[RKO (line)]] | wt | 79.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -17.7) |
| [[LoVo (line)]] | wt | 56.4 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.323× (z -9.6) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.336× (z -9.2) |
| [[NCI-H661 (line)]] | alt | 93.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0981× (z -14.5) |
| [[SW 1088 (line)]] | alt | 316 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.195× (z -11.3) |
| [[SW 1271 (line)]] | alt | 119 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.107× (z -9.6) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 83.4 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.223× (z -9.1) |
| [[COLO 205 (line)]] | alt | 46.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.174× (z -11.4) ⚠ toxic |
| [[SW1417 (line)]] | alt | 94.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.450× (z -10.9) |
| [[A498 (line)]] | wt | 47.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 194 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 197 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3534), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INSIG2]] | +0.81 | +0.80 / +0.75 | both halves | 7e-06 |  |
| [[PDK3]] | +0.80 | +0.76 / +0.81 | both halves | 7e-06 |  |
| [[HILPDA]] | +0.77 | +0.74 / +0.75 | both halves | 7e-06 |  |
| [[GPI]] | +0.76 | +0.76 / +0.74 | both halves | 7e-06 | pathway: Glucose metabolism; STRING 745 |
| [[WDR45B]] | +0.75 | +0.73 / +0.74 | both halves | 7e-06 |  |
| [[CABIN1]] | +0.74 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[YEATS2]] | +0.74 | +0.74 / +0.71 | both halves | 7e-06 |  |
| [[FAM162A]] | +0.74 | +0.73 / +0.72 | both halves | 7e-06 |  |
| [[ERO1A]] | +0.72 | +0.75 / +0.63 | both halves | 7e-06 |  |
| [[ABCB9]] | +0.72 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[ANKRD37]] | +0.71 | +0.77 / +0.58 | both halves | 7e-06 | STRING 400 |
| [[GYS1]] | +0.71 | +0.70 / +0.61 | both halves | 7e-06 | pathway: Metabolism of carbohydrates and carbohydrate derivatives |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AVEN]] | -0.65 | -0.66 / -0.42 | both halves | 4e-05 |  |
| [[ITPA]] | -0.58 | -0.59 / -0.35 | both halves | 1e-04 |  |
| [[SLC25A13]] | -0.57 | -0.61 / -0.47 | both halves | 2e-05 | same gene group |
| [[ARAP2]] | -0.56 | -0.60 / -0.36 | both halves | 1e-04 |  |
| [[REEP3]] | -0.56 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[DPH5-DT]] | -0.56 | -0.57 / -0.34 | both halves | 1e-04 |  |
| [[ATE1]] | -0.56 | -0.51 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PFKFB4's level | compounds that target TOP2A: 5 of 5 lower it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 7.0% of all compounds | 0.009 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[SLC2A3]] | B | SLC2A3 activity raises PFKFB4's level | lines that do not express SLC2A3 (15) vs lines expressing it (35) | 1.98× lower at baseline in the lines without SLC2A3 | 0.015 | ⚠ within organs, on part of the lines; also absent: SLC16A2, DPY19L2P2-1, LGALS1 |
| [[RAB20]] | B | RAB20 activity raises PFKFB4's level | lines that do not express RAB20 (8) vs lines expressing it (42) | 1.53× lower at baseline in the lines without RAB20 | 0.055 | ⚠ within organs, on part of the lines; also absent: RPS6KA2, PRDX2, YPEL3; maybe low, not absent |
| [[NRN1]] | B | NRN1 activity raises PFKFB4's level | lines that do not express NRN1 (27) vs lines expressing it (23) | 1.46× lower at baseline in the lines without NRN1 | 0.057 | ⚠ within organs, on part of the lines; also absent: ILDR2, PHACTR1, ENSG00000250137 |
| [[EPHA3]] | B | EPHA3 activity raises PFKFB4's level | lines that do not express EPHA3 (26) vs lines expressing it (24) | 1.83× lower at baseline in the lines without EPHA3 | 0.060 | ⚠ within organs, on part of the lines; also absent: ADGRB3, MARCHF1, LINC00491 |
| [[VLDLR]] | B | VLDLR activity raises PFKFB4's level | lines that do not express VLDLR (8) vs lines expressing it (42) | 2.24× lower at baseline in the lines without VLDLR | 0.073 | ⚠ within organs, on part of the lines; also absent: NEURL3, ALK, ENSG00000258989 |
| [[ZNF254]] | B | ZNF254 activity strengthens PFKFB4's drug response | lines that do not express ZNF254 (6) vs lines expressing it (43) | the lines without ZNF254 respond 0.83× as strongly (z diff +1.83); strongest at Dinaciclib 5 µM: 0.69x vs 0.32x (z diff +5.4) | 0.082 | ⚠ within organs, on part of the lines; also absent: ENSG00000283201, ZNF571, ZNF613; target measured in part of the lines; artifact flags |
| [[ZNF292]] | C | ZNF292's natural level strengthens PFKFB4's drug response | ZNF292's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.67, reverse +0.45; direction not clear | 0.027 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CEP250]] | C | PFKFB4's natural level strengthens CEP250's drug response | PFKFB4's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.45; direction not clear | 0.061 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[USP37]] | C | PFKFB4's natural level strengthens USP37's drug response | PFKFB4's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.62, reverse +0.31; direction not clear | 0.084 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| [[PIAS2]] | C | PFKFB4's natural level strengthens PIAS2's drug response | PFKFB4's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.61, reverse +0.46; direction not clear | 0.097 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 099]] — hypoxia; 48 genes; every member is in the + arm (projection on the module's main direction 0.828). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.0, -16.3); signed map (-36.3, 24.3). **Vector** length 135, 52.4% of its response variance represented; |z| ≥ 3 in 1,422 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *hypoxia* (hallmark, mean cos +0.58 to 17); *mTORC1 signaling* (hallmark, mean cos +0.55 to 15); *hypoxia* (control, mean cos +0.56 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | +7.9 | -5.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | +7.8 | -3.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | +7.0 | -5.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.9 | -1.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +4.0 | +3.0 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +3.5 | +4.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.2 | +3.3 |
|  | [[Fumaric acid (drug)]] 5 µM |  | +3.2 | +3.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.1 | +0.2 |
| fall | [[Selinexor (drug)]] 5 µM |  | -8.7 | -10.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -7.3 | -18.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.5 | -9.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -5.3 | -6.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -5.2 | -6.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.8 | -3.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -4.6 | -3.3 |
|  | [[Rapamycin (drug)]] 5 µM |  | -4.5 | -2.4 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -4.2 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | 6-phosphofructo-2-kinase/fructose-2,6-biphosphatase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:48,517,684-48,562,015 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | 6-phosphofructo-2-kinase/fructose-2,6-biphosphatase family; MicroRNA protein coding host genes |
| Reactome | 4 pathways, smallest: Regulation of glycolysis by fructose 2,6-bisphosphate metabolism; Glycolysis; Glucose metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16877](https://www.uniprot.org/uniprotkb/Q16877) (6-phosphofructo-2-kinase/fructose-2,6-bisphosphatase 4):

> Synthesis and degradation of fructose 2,6-bisphosphate.

**Summary**, from NCBI Gene [5210](https://www.ncbi.nlm.nih.gov/gene/5210):

> The protein encoded by this gene is one of four bifunctional kinase/phosphatases that regulate the concentration of the glycolytic byproduct fructose-2,6-bisphosphate (F2,6BP). The encoded protein is highly expressed in cancer cells and is induced by hypoxia. This protein is essential to the survival of cancer cells under conditions of hypoxia, because it increases the amount of F2,6BP and ATP at a time when the cell cannot produce much of them. This finding suggests that this protein may be a …

**Accessions** — [HGNC:8875](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8875) · Entrez [5210](https://www.ncbi.nlm.nih.gov/gene/5210) · UniProt [Q16877](https://www.uniprot.org/uniprotkb/Q16877) · Ensembl [ENSG00000114268](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114268)

## Data

Gene col 3534: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3534); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3534, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3534]; `tensor/DDL_lfc|DDL_z.npy` [3534]; `embed/gene_vectors.npy` [3534]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3534 or target_col == 3534). Every well: [[PFKFB4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PFKFB4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
