---
symbol: "OSBP"
type: "gene"
col: 3106
ensembl_id: "ENSG00000110048"
name: "oxysterol binding protein"
location: "11q12.1"
module: 41
arm: "+"
pooled_cpm: 140.82
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 11
n_dd_up_clean: 4
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# OSBP

*oxysterol binding protein* — 11q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 3.55× (z +13.0, q 1e-35, up in 46 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.453× (z -14.9, q 0e+00, down in 40 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 0.703× (z -9.4, q 6e-19, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACBD3]] (+0.81, fdr 7e-06), [[GOLGA2]] (+0.78, fdr 7e-06), [[SPTY2D1]] (+0.77, fdr 7e-06); moves opposite to [[VMA21]] (-0.62, fdr 1e-05), [[ZNF300]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3106.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.55×** | +13.0 | 1e-35 | 46/49 (SW480, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.99×** | +11.2 | 1e-26 | 39/48 (SW480, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.23×** | +4.1 | 0.009 | 24/48 (NCI-H460, LS 180, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.22×** | +3.9 | 0.013 | 22/48 (NCI-H460, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~9% of this change | 1.19× | +3.4 | 0.089 | 21/48 (PANC-1, SNU-1, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 1.18× | +3.2 | 0.11 | 21/48 (NCI-H1573, A-427, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.2 | 0.11 | 18/48 (Panc 03.27, A-427, …) | inconsistent across doses |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 1.18× | +3.2 | 0.11 | 13/48 (A-427, LOX-IMVI, …) | rises with dose | plate-row cell shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3106.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.453×** | -14.9 | 0e+00 | 40/44 (LoVo, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.536×** | -11.3 | 4e-27 | 39/45 (HOP62, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.564×** | -11.2 | 6e-27 | 39/49 (RKO, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.703×** | -9.4 | 6e-19 | 41/48 (SNU-423, LS 180, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.723×** | -6.1 | 1e-07 | 40/48 (J82, RKO, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.738×** | -5.7 | 9e-07 | 36/48 (A498, SW 900, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.822×** | -5.3 | 9e-06 | 29/48 (HS-578T, A498, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.790×** | -4.4 | 6e-04 | 29/47 (SW1417, NCI-H661, …) | rises with dose |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.827×** | -3.7 | 0.012 | 22/48 (LS 180, HT-29, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.870× | -3.7 | 0.012 | 15/48 (NCI-H2347, SW480, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.871× | -3.7 | 0.012 | 10/48 (HOP62, CHP-212, …) | top dose only | position effect removed |
| [[Busulfan (drug)]] 0.05 µM |  | **0.830×** | -3.7 | 0.012 | 21/49 (LS 180, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.836× | -3.5 | 0.019 | 20/48 (LoVo, SW48, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 0.840× | -3.4 | 0.024 | 21/48 (HOP62, SW480, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.843× | -3.3 | 0.031 | 19/48 (NCI-H1792, RKO, …) | inconsistent across doses |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | 0.844× | -3.3 | 0.031 | 15/49 (LS 180, HT-29, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.845× | -3.3 | 0.031 | 18/48 (SW 900, PANC-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.852× | -3.1 | 0.055 | 16/48 (SW 900, HOP62, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.859× | -3.0 | 0.084 | 18/48 (COLO 205, HT-29, …) | inconsistent across doses |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.749×** | -3.0 | 0.084 | 17/49 (AsPC-1, SW 900, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3106. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 150 | 2 | 4 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 3.91× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.328× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.563× (z -10.3) |
| [[A-427 (line)]] | wt | 114 | 3 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.42× (z +14.5) | [[Dinaciclib (drug)]] 5 µM 0.444× (z -11.6) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 119 | 2 | 3 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 4.73× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.357× (z -13.4) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 185 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.335× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.607× (z -8.6) |
| [[LS 180 (line)]] | wt | 185 | 2 | 2 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 6.97× (z +11.5) | [[Selinexor (drug)]] 5 µM 0.489× (z -10.9) |
| [[NCI-H1792 (line)]] | alt | 153 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.333× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.529× (z -9.5) |
| [[SW480 (line)]] | alt | 189 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.27× (z +14.6) | [[Dinaciclib (drug)]] 5 µM 0.426× (z -12.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 170 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.519× (z -12.9) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.484× (z -10.1) |
| [[A549 (line)]] | wt | 147 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +9.8) ⚠ cell-cycle shift, explains ~86% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.393× (z -11.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 159 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.307× (z -14.3) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 95.5 | 2 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 4.45× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.443× (z -9.5) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 207 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.328× (z -12.5) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 145 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.235× (z -14.1) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 166 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.444× (z -11.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 140 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.49× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.239× (z -16.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 124 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +8.6) ⚠ cell-cycle shift, explains ~86% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.21× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.403× (z -9.9) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 135 | 2 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 6.40× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.189× (z -19.1) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 164 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.334× (z -11.2) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 168 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.318× (z -12.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 112 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.417× (z -10.1) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 159 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 4.09× (z +9.9) | — |
| [[C32 (line)]] | wt | 105 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.381× (z -9.0) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 157 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 8.23× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.358× (z -9.7) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 181 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.170× (z -17.1) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 241 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.312× (z -11.1) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 127 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.88× (z +9.9) | — |
| [[NCI-H1573 (line)]] | alt | 125 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 0.5 µM 2.25× (z +9.4) ⚠ cell-cycle shift, explains ~33% of this change | [[Selinexor (drug)]] 5 µM 0.578× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 132 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.540× (z -10.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 83.9 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.08× (z +9.2) | — |
| [[Panc 03.27 (line)]] | alt | 173 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.99× (z +9.6) | [[Dinaciclib (drug)]] 0.05 µM 0.461× (z -9.5) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 111 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.174× (z -15.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 127 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.431× (z -10.0) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 205 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.313× (z -12.4) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 144 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.422× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 101 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.167× (z -9.1) ⚠ toxic; cell-cycle shift, explains ~29% of this change |
| [[SNU-423 (line)]] | alt | 125 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.509× (z -11.8) |
| [[SW1417 (line)]] | alt | 182 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.514× (z -9.4) ⚠ toxic; cell-cycle shift, explains ~29% of this change |
| [[AN3 CA (line)]] | alt | 110 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 64.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 131 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 89.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 198 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 80.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 118 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3106), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACBD3]] | +0.81 | +0.83 / +0.74 | both halves | 7e-06 | STRING 786 |
| [[GOLGA2]] | +0.78 | +0.76 / +0.76 | both halves | 7e-06 |  |
| [[SPTY2D1]] | +0.77 | +0.75 / +0.72 | both halves | 7e-06 |  |
| [[YIPF5]] | +0.77 | +0.76 / +0.74 | both halves | 7e-06 |  |
| [[GOLGA5]] | +0.76 | +0.80 / +0.72 | both halves | 7e-06 |  |
| [[COG3]] | +0.75 | +0.83 / +0.62 | both halves | 7e-06 |  |
| [[SRP54]] | +0.75 | +0.80 / +0.66 | both halves | 7e-06 |  |
| [[HM13]] | +0.75 | +0.75 / +0.70 | both halves | 7e-06 |  |
| [[RAB5A]] | +0.75 | +0.80 / +0.69 | both halves | 7e-06 |  |
| [[MCEE]] | +0.74 | +0.74 / +0.72 | both halves | 7e-06 |  |
| [[COPE]] | +0.74 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[EIF2AK3]] | +0.74 | +0.78 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VMA21]] | -0.62 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[ZNF300]] | -0.60 | -0.50 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.833). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (11.6, -36.9); signed map (-51.3, 13.8). **Vector** length 124, 43.1% of its response variance represented; |z| ≥ 3 in 1,058 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Intra-Golgi and retrograde Golgi-to-ER traffic* (reactome, mean cos +0.60 to 12); *Asparagine N-linked glycosylation* (reactome, mean cos +0.60 to 12); *ER to Golgi Anterograde Transport* (reactome, mean cos +0.66 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +4.9 | +13.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | -1.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.1 | +11.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +3.1 | -2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +1.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.4 | -0.2 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +2.4 | +1.4 |
| fall | [[Selinexor (drug)]] 5 µM |  | -8.2 | -9.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.4 | -6.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.3 | +2.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.0 | -3.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.9 | -2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | -5.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -3.0 | -2.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -3.0 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | oxysterol binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.1 — chr11:59,574,398-59,615,774 (-) |
| Ensembl biotype | protein_coding |
| Also known as | OSBP1 |
| Gene groups (HGNC) | Oxysterol binding proteins; Pleckstrin homology domain containing; MicroRNA protein coding host genes |
| Reactome | 6 pathways, smallest: Synthesis of bile acids and bile salts; Bile acid and bile salt metabolism; Sphingolipid de novo biosynthesis |
| Matched by | ensembl_id |

**Function**, from UniProt [P22059](https://www.uniprot.org/uniprotkb/P22059) (Oxysterol-binding protein 1):

> Lipid transporter involved in lipid countertransport between the Golgi complex and membranes of the endoplasmic reticulum: specifically exchanges sterol (cholesterol) with phosphatidylinositol 4-phosphate (PI4P, 1,2-diacyl-sn-glycero-3-phospho-(1D-myo-inositol 4-phosphate)), delivering sterol to the Golgi in exchange for PI4P, which is subsequently degraded by the SAC1/SACM1L phosphatase in the endoplasmic reticulum. Binds cholesterol and a range of oxysterols including 25-hydroxycholesterol. …

**Summary**, from NCBI Gene [5007](https://www.ncbi.nlm.nih.gov/gene/5007):

> Oxysterol binding protein is an intracellular protein that is believed to transport sterols from lysosomes to the nucleus where the sterol down-regulates the genes for the LDL receptor, HMG-CoA reductase, and HMG synthetase [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:8503](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8503) · Entrez [5007](https://www.ncbi.nlm.nih.gov/gene/5007) · UniProt [P22059](https://www.uniprot.org/uniprotkb/P22059) · Ensembl [ENSG00000110048](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110048)

## Data

Gene col 3106: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3106); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3106, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3106]; `tensor/DDL_lfc|DDL_z.npy` [3106]; `embed/gene_vectors.npy` [3106]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3106 or target_col == 3106). Every well: [[OSBP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OSBP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
