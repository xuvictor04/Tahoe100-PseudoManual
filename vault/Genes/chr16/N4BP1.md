---
symbol: "N4BP1"
type: "gene"
col: 2291
ensembl_id: "ENSG00000102921"
name: "NEDD4 binding protein 1"
location: "16q12.1"
module: 32
arm: "+"
pooled_cpm: 106.81
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 19
n_dd_up_clean: 0
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 21
direction_downstream: 1
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# N4BP1

*NEDD4 binding protein 1* — 16q12.1

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 1 line (Panc 03.27 5.86×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.338× (z -23.4, q 0e+00, down in 42 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.577× (z -13.4, q 1e-38, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADPRS]] (+0.71, fdr 7e-06), [[IFI6]] (+0.68, fdr 1e-05), [[TDRD7]] (+0.68, fdr 7e-06); moves opposite to [[CRTAP]] (-0.54, fdr 4e-05), [[HNRNPA3]] (-0.49, fdr 1e-04).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 21 arrows point to it, the strongest [[OAS1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[USP18]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2291.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 1 line (Panc 03.27 5.86×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 1.16× | +3.2 | 0.77 | 9/48 (SNU-423, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 23 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2291.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.338×** | -23.4 | 0e+00 | 42/44 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.440×** | -19.9 | 0e+00 | 47/49 (A-172, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.546×** | -13.6 | 8e-40 | 39/45 (MIA PaCa-2, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.535×** | -13.5 | 3e-39 | 43/47 (HepG2/C3A, AsPC-1, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.577×** | -13.4 | 1e-38 | 43/48 (MIA PaCa-2, BT-474, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.674×** | -9.6 | 9e-20 | 37/48 (NCI-H460, KATO III, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.694×** | -7.9 | 2e-13 | 27/48 (NCI-H1792, A-172, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.725×** | -7.8 | 4e-13 | 32/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.814×** | -7.1 | 8e-11 | 24/48 (A-172, NCI-H1792, …) | top dose only | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.727×** | -6.9 | 3e-10 | 27/50 (MIA PaCa-2, BT-474, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.782×** | -6.0 | 1e-07 | 25/48 (A-172, A549, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.769×** | -5.7 | 8e-07 | 30/48 (A-172, BT-474, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.775×** | -5.5 | 2e-06 | 28/48 (RPMI-7951, A549, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.802×** | -4.7 | 8e-05 | 24/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.945× | -4.7 | 1e-04 | 0/50 | inconsistent across doses |  |
| [[Tofacitinib (drug)]] 5 µM |  | 0.874× | -4.6 | 1e-04 | 19/49 (SK-MEL-2, COLO 205, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.827×** | -4.6 | 1e-04 | 23/49 (A-172, RPMI-7951, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.822×** | -4.5 | 2e-04 | 23/48 (CFPAC-1, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 0.894× | -3.9 | 0.003 | 16/49 (COLO 205, RPMI-7951, …) | rises with dose |  |
| [[Gefitinib (drug)]] 5 µM |  | 0.873× | -3.3 | 0.019 | 12/48 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.05 µM |  | 0.879× | -3.1 | 0.033 | 13/48 (A498, A549, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.789×** | -3.0 | 0.047 | 12/48 (NCI-H460, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | 0.882× | -2.9 | 0.065 | 10/48 (CFPAC-1, SK-MEL-2, …) | inconsistent across doses |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | 0.890× | -2.8 | 0.076 | 19/49 (SK-MEL-2, RKO, …) | all doses, stronger at high dose |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | 0.893× | -2.8 | 0.094 | 11/48 (Hs 766T, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2291. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 162 | 0 | 13 (11 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.135× (z -26.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.410× (z -11.9) |
| [[HOP62 (line)]] | alt | 101 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.294× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.505× (z -9.3) |
| [[MIA PaCa-2 (line)]] | alt | 161 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.107× (z -27.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.307× (z -16.5) |
| [[NCI-H460 (line)]] | wt | 82.5 | 0 | 7 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.287× (z -19.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[AsPC-1 (line)]] | alt | 123 | 0 | 6 (5 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.280× (z -12.7) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.401× (z -10.3) |
| [[RKO (line)]] | wt | 114 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0984× (z -24.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.409× (z -9.3) |
| [[SNU-423 (line)]] | alt | 112 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.130× (z -19.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.344× (z -11.6) |
| [[A498 (line)]] | wt | 153 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.285× (z -20.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[BT-474 (line)]] | alt | 177 | 0 | 5 (4 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0723× (z -15.8) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.292× (z -14.1) |
| [[HS-578T (line)]] | alt | 86.3 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.257× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.384× (z -9.8) |
| [[LoVo (line)]] | wt | 119 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.317× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.486× (z -10.7) |
| [[NCI-H1792 (line)]] | alt | 110 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -20.3) ⚠ cell-cycle shift, explains ~55% of this change |
| [[SW 900 (line)]] | alt | 112 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -12.6) ⚠ cell-cycle shift, explains ~55% of this change |
| [[A549 (line)]] | wt | 136 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[CFPAC-1 (line)]] | alt | 120 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -18.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[hTERT-HPNE (line)]] | wt | 65.5 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -12.6) ⚠ cell-cycle shift, explains ~55% of this change |
| [[A-427 (line)]] | wt | 86.8 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.353× (z -12.6) ⚠ toxic |
| [[C32 (line)]] | wt | 86.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -13.1) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.376× (z -11.1) |
| [[HEC-1-A (line)]] | alt | 90.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.303× (z -16.5) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 184 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.260× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[KATO III (line)]] | alt | 111 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.332× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[NCI-H2347 (line)]] | alt | 95.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.381× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[Panc 03.27 (line)]] | alt | 112 | 1 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.86× (z +11.4) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.375× (z -10.7) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 134 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.134× (z -19.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.429× (z -9.0) |
| [[SHP-77 (line)]] | alt | 126 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.218× (z -19.5) ⚠ toxic; transcription drop · without an alert: [[IQ 1 (drug)]] 5 µM 0.278× (z -9.6) |
| [[SW480 (line)]] | alt | 85.6 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.219× (z -22.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.443× (z -13.2) |
| [[COLO 205 (line)]] | alt | 155 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.297× (z -10.3) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 134 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.309× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[NCI-H2030 (line)]] | alt | 102 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.223× (z -17.4) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 92.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -20.8) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 118 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.233× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.416× (z -9.9) |
| [[SW1417 (line)]] | alt | 94.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.396× (z -10.7) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 98.5 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.220× (z -9.7) |
| [[C-33 A (line)]] | alt | 127 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.328× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[CHP-212 (line)]] | wt | 134 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.261× (z -9.3) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 91.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0813× (z -21.6) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 104 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.326× (z -11.9) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 79.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.460× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[J82 (line)]] | alt | 103 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.485× (z -11.5) ⚠ cell-cycle shift, explains ~55% of this change |
| [[LOX-IMVI (line)]] | wt | 71.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.399× (z -10.1) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 107 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.388× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[PANC-1 (line)]] | alt | 50.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.485× (z -9.4) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 91.0 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.343× (z -9.7) |
| [[SW 1088 (line)]] | alt | 119 | 0 | 1 | — | [[Flumatinib (mesylate) (drug)]] 0.05 µM 0.0948× (z -9.1) |
| [[SW 1271 (line)]] | alt | 72.7 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0960× (z -9.5) |
| [[SW48 (line)]] | wt | 80.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.246× (z -11.0) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 79.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 66.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2291), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADPRS]] | +0.71 | +0.73 / +0.67 | both halves | 7e-06 |  |
| [[IFI6]] | +0.68 | +0.52 / +0.76 | both halves | 1e-05 |  |
| [[TDRD7]] | +0.68 | +0.60 / +0.72 | both halves | 7e-06 |  |
| [[HELZ2]] | +0.66 | +0.48 / +0.74 | both halves | 2e-05 |  |
| [[IFI27]] | +0.66 | +0.54 / +0.75 | both halves | 1e-05 |  |
| [[ZNFX1]] | +0.66 | +0.53 / +0.73 | both halves | 1e-05 |  |
| [[ISG15]] | +0.66 | +0.48 / +0.74 | both halves | 2e-05 |  |
| [[PML]] | +0.65 | +0.54 / +0.72 | both halves | 1e-05 |  |
| [[UBE2L6]] | +0.64 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[USP18]] | +0.64 | +0.53 / +0.72 | both halves | 1e-05 | pathway: Interleukin-1 family signaling |
| [[OAS1]] | +0.63 | +0.52 / +0.69 | both halves | 1e-05 |  |
| [[SP110]] | +0.63 | +0.49 / +0.68 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRTAP]] | -0.54 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[HNRNPA3]] | -0.49 | -0.34 / -0.46 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 21, C 0. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OAS1]] | B | OAS1 activity raises N4BP1's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 1.48× lower at baseline in the lines without OAS1 | 3e-04 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[OAS2]] | B | OAS2 activity raises N4BP1's level | lines that do not express OAS2 (14) vs lines expressing it (36) | 1.42× lower at baseline in the lines without OAS2 | 0.001 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1 |
| [[IFI27]] | B | IFI27 activity raises N4BP1's level | lines that do not express IFI27 (21) vs lines expressing it (29) | 1.37× lower at baseline in the lines without IFI27 | 0.001 | ⚠ within organs, on part of the lines; also absent: TRIM22, OAS2, RSAD2 |
| [[XAF1]] | B | XAF1 activity raises N4BP1's level | lines that do not express XAF1 (14) vs lines expressing it (36) | 1.29× lower at baseline in the lines without XAF1 | 0.001 | ⚠ within organs, on part of the lines; also absent: SLC15A3, TRIM22, FBXO39 |
| [[TRIM22]] | B | TRIM22 activity raises N4BP1's level | lines that do not express TRIM22 (18) vs lines expressing it (32) | 1.31× lower at baseline in the lines without TRIM22 | 0.002 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1 |
| [[SLC15A3]] | B | SLC15A3 activity raises N4BP1's level | lines that do not express SLC15A3 (16) vs lines expressing it (34) | 1.26× lower at baseline in the lines without SLC15A3 | 0.003 | ⚠ within organs, on part of the lines; also absent: XAF1, MX2, GBP4 |
| [[CCDC194]] | B | CCDC194 activity raises N4BP1's level | lines that do not express CCDC194 (19) vs lines expressing it (31) | 1.34× lower at baseline in the lines without CCDC194 | 0.007 | ⚠ within organs, on part of the lines; also absent: BST2, DEPP1, TRIM22 |
| [[CMPK2]] | B | CMPK2 activity raises N4BP1's level | lines that do not express CMPK2 (11) vs lines expressing it (39) | 1.39× lower at baseline in the lines without CMPK2 | 0.007 | ⚠ within organs, on part of the lines; also absent: OAS2, NRIR, OAS1 |
| [[RSAD2]] | B | RSAD2 activity raises N4BP1's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 1.36× lower at baseline in the lines without RSAD2 | 0.008 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[BST2]] | B | BST2 activity raises N4BP1's level | lines that do not express BST2 (18) vs lines expressing it (32) | 1.30× lower at baseline in the lines without BST2 | 0.012 | ⚠ within organs, on part of the lines; also absent: CCDC194, DEPP1, SLC15A3 |
| [[IFI6]] | B | IFI6 activity raises N4BP1's level | lines that do not express IFI6 (13) vs lines expressing it (37) | 1.31× lower at baseline in the lines without IFI6 | 0.016 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent |
| [[MX1]] | B | MX1 activity raises N4BP1's level | lines that do not express MX1 (19) vs lines expressing it (31) | 1.30× lower at baseline in the lines without MX1 | 0.028 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[USP18]] | C | N4BP1's natural level strengthens USP18's drug response | N4BP1's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.67, reverse +0.27; direction not clear | 0.059 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.623). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (50.2, 52.6); signed map (66.3, 30.1). **Vector** length 107, 31.3% of its response variance represented; |z| ≥ 3 in 1,140 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon alpha response* (hallmark, mean cos +0.53 to 56); *interferon gamma response* (hallmark, mean cos +0.54 to 60); *interferon* (control, mean cos +0.58 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.8 | -0.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.5 | +0.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.5 | +1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.2 | +1.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.7 | -2.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.0 | +1.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | -0.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.4 | -0.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | +2.4 | +0.3 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.2 | -23.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | -6.2 | -19.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.8 | -13.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.6 | -13.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.4 | -13.4 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -4.5 | -4.6 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -4.3 | -2.7 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -3.7 | -3.9 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -3.5 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | NEDD4 binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q12.1 — chr16:48,538,726-48,620,148 (-) |
| Ensembl biotype | protein_coding |
| Reactome | 23 pathways, smallest: Regulation of NF-kappa B signaling; TAK1-dependent IKK and NF-kappa-B activation; MyD88 cascade initiated on plasma membrane |
| Matched by | ensembl_id |

**Function**, from UniProt [O75113](https://www.uniprot.org/uniprotkb/O75113) (NEDD4-binding protein 1):

> Potent suppressor of cytokine production that acts as a regulator of innate immune signaling and inflammation. Acts as a key negative regulator of select cytokine and chemokine responses elicited by TRIF-independent Toll-like receptors (TLRs), thereby limiting inflammatory cytokine responses to minor insults. In response to more threatening pathogens, cleaved by CASP8 downstream of TLR3 or TLR4, leading to its inactivation, thereby allowing production of inflammatory cytokines (By similarity). …

**Summary**, from NCBI Gene [9683](https://www.ncbi.nlm.nih.gov/gene/9683):

> Enables RNA nuclease activity; mRNA binding activity; and ubiquitin binding activity. Involved in cellular response to UV and negative regulation of viral genome replication. Predicted to be located in cytosol and nucleolus. Predicted to be active in PML body. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29850](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29850) · Entrez [9683](https://www.ncbi.nlm.nih.gov/gene/9683) · UniProt [O75113](https://www.uniprot.org/uniprotkb/O75113) · Ensembl [ENSG00000102921](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102921)

## Data

Gene col 2291: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2291); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2291, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2291]; `tensor/DDL_lfc|DDL_z.npy` [2291]; `embed/gene_vectors.npy` [2291]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2291 or target_col == 2291). Every well: [[N4BP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/N4BP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
