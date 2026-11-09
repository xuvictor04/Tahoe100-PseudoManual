---
symbol: "PRH1"
type: "gene"
col: 13819
ensembl_id: "ENSG00000231887"
name: "proline rich protein HaeIII subfamily 1"
location: "12p13.2"
module: 26
arm: "+"
pooled_cpm: 80.76
n_lines_expressing: 49
n_dd_up: 1
n_dd_down: 26
n_dd_up_clean: 1
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 6
direction_downstream: 1
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# PRH1

*proline rich protein HaeIII subfamily 1* — 12p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.40× (z +3.8, q 0.075, up in 28 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (11 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.220× (z -17.1, q 0e+00, down in 45 of 46 measured lines) ⚠ toxic. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.419× (z -14.4, q 1e-44, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRR4]] (+0.88, fdr 7e-06, ⚠ read-through risk), [[COMMD10]] (+0.76, fdr 7e-06), [[SEMA6A-AS1]] (+0.75, fdr 7e-06), [[VPS13B]] (+0.69, fdr 7e-06); moves opposite to [[LINC00674]] (-0.57, fdr 3e-05), [[AHDC1]] (-0.56, fdr 1e-05), [[CEP295NL]] (-0.53, fdr 1e-05).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[PMFBP1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[TAS2R14]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13819.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.40×** | +3.8 | 0.075 | 28/46 (SW480, NCI-H1792, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.32× | +3.3 | 0.20 | 26/46 (LoVo, A549, …) | rises with dose |  |
| [[Brimonidine (drug)]] 5 µM |  | 1.32× | +3.3 | 0.20 | 21/47 (HEC-1-A, LOX-IMVI, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13819.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.220×** | -17.1 | 0e+00 | 45/46 (NCI-H1573, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.419×** | -14.4 | 1e-44 | 46/48 (NCI-H1792, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.349×** | -12.3 | 1e-32 | 47/47 (LOX-IMVI, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.351×** | -12.3 | 2e-32 | 47/47 (HCT15, HOP62, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.368×** | -11.7 | 1e-29 | 45/47 (HCT15, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.409×** | -10.5 | 1e-23 | 45/47 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.516×** | -7.7 | 8e-13 | 41/47 (LoVo, HT-29, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **0.596×** | -6.0 | 1e-07 | 31/48 (NCI-H23, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.700×** | -5.9 | 2e-07 | 29/47 (A-427, NCI-H1792, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.609×** | -5.8 | 4e-07 | 32/47 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.610×** | -5.8 | 4e-07 | 36/47 (HT-29, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~24% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.422×** | -5.3 | 6e-06 | 32/48 (A-427, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **0.628×** | -5.2 | 8e-06 | 28/46 (NCI-H1792, A-427, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | **0.646×** | -4.9 | 4e-05 | 24/43 (NCI-H23, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.694×** | -4.3 | 8e-04 | 30/47 (A-427, C32, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.511×** | -4.1 | 0.001 | 31/48 (A-427, HOP62, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.713×** | -3.9 | 0.003 | 31/47 (HEC-1-A, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.584×** | -3.9 | 0.003 | 26/47 (A-427, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.735×** | -3.6 | 0.009 | 27/47 (C-33 A, SW480, …) | rises with dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.731×** | -3.5 | 0.012 | 25/48 (LoVo, NCI-H460, …) | top dose only | plate-row cell shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.750×** | -3.3 | 0.020 | 25/47 (PANC-1, HCT15, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.592×** | -3.2 | 0.031 | 23/47 (A-427, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.37 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13819. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 137 | 0 | 14 (9 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0576× (z -26.6) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -13.5) |
| [[SW480 (line)]] | alt | 87.3 | 0 | 13 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.169× (z -17.6) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -15.4) |
| [[A-427 (line)]] | wt | 116 | 0 | 10 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.140× (z -17.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.227× (z -14.1) |
| [[HOP62 (line)]] | alt | 153 | 0 | 10 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.163× (z -17.4) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.211× (z -15.5) |
| [[HCT15 (line)]] | alt | 108 | 0 | 9 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0911× (z -18.7) ⚠ toxic · without an alert: [[Belinostat (drug)]] 5 µM 0.140× (z -15.9) |
| [[HT-29 (line)]] | alt | 123 | 0 | 9 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.191× (z -15.8) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.273× (z -12.9) |
| [[NCI-H1792 (line)]] | alt | 140 | 0 | 9 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.290× (z -16.8) |
| [[C32 (line)]] | wt | 113 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -14.0) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.169× (z -13.0) |
| [[LoVo (line)]] | wt | 146 | 0 | 8 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.203× (z -19.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -15.2) |
| [[LOX-IMVI (line)]] | wt | 118 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.178× (z -16.5) |
| [[PANC-1 (line)]] | alt | 52.5 | 0 | 8 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.187× (z -15.4) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.321× (z -14.8) |
| [[H4 (line)]] | wt | 164 | 0 | 7 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.172× (z -15.1) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.245× (z -12.6) |
| [[NCI-H23 (line)]] | alt | 272 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0464× (z -34.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.292× (z -13.9) |
| [[HepG2_C3A (line)]] | wt | 93.7 | 0 | 6 (3 ⚠) | — | [[Ponatinib (drug)]] 5 µM 0.118× (z -16.8) |
| [[NCI-H460 (line)]] | wt | 62.0 | 0 | 6 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.187× (z -13.9) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -10.3) |
| [[SNU-1 (line)]] | wt | 105 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.122× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.272× (z -12.1) |
| [[SW 900 (line)]] | alt | 165 | 0 | 6 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0695× (z -20.0) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.336× (z -12.0) |
| [[C-33 A (line)]] | alt | 148 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.305× (z -12.4) |
| [[MIA PaCa-2 (line)]] | alt | 77.8 | 0 | 5 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.250× (z -11.9) |
| [[COLO 205 (line)]] | alt | 97.8 | 0 | 4 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.151× (z -15.5) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -10.1) |
| [[J82 (line)]] | alt | 78.2 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -13.7) |
| [[KATO III (line)]] | alt | 46.8 | 0 | 4 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0881× (z -21.2) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.310× (z -10.7) |
| [[RPMI-7951 (line)]] | alt | 66.8 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.186× (z -11.5) |
| [[SK-MEL-2 (line)]] | alt | 67.5 | 0 | 4 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.188× (z -13.6) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.255× (z -11.5) |
| [[hTERT-HPNE (line)]] | wt | 71.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -11.5) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -9.0) |
| [[RKO (line)]] | wt | 65.7 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -10.5) |
| [[SW1417 (line)]] | alt | 48.3 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.194× (z -10.9) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.278× (z -8.9) |
| [[A-172 (line)]] | wt | 34.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -10.7) ⚠ cell-cycle shift, explains ~38% of this change |
| [[HEC-1-A (line)]] | alt | 99.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.321× (z -15.7) |
| [[LS 180 (line)]] | wt | 81.5 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -10.3) |
| [[A498 (line)]] | wt | 32.6 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.216× (z -10.1) ⚠ toxic |
| [[A549 (line)]] | wt | 56.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.358× (z -9.2) |
| [[AN3 CA (line)]] | alt | 68.2 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0868× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 48.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.222× (z -11.3) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 29.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -10.8) ⚠ cell-cycle shift, explains ~38% of this change |
| [[CHP-212 (line)]] | wt | 85.5 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0833× (z -11.9) ⚠ toxic |
| [[HS-578T (line)]] | alt | 51.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -10.2) ⚠ cell-cycle shift, explains ~38% of this change |
| [[Panc 03.27 (line)]] | alt | 43.1 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.185× (z -9.7) ⚠ toxic |
| [[SW48 (line)]] | wt | 85.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.293× (z -10.8) |
| [[BT-474 (line)]] | alt | 61.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 38.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 70.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.0 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 85.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 79.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 70.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 226 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13819), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRR4]] | +0.88 | +0.86 / +0.85 | both halves | 7e-06 | ⚠ **readthrough risk**: PRR4 lies 0.0 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[COMMD10]] | +0.76 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[SEMA6A-AS1]] | +0.75 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[TAS2R14]] | +0.74 | +0.67 / +0.73 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[VPS13B]] | +0.69 | +0.63 / +0.72 | both halves | 7e-06 |  |
| [[STAG1]] | +0.65 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[SLC26A7]] | +0.64 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[WARS2-AS1]] | +0.64 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[MCPH1]] | +0.63 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[THADA]] | +0.63 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[TIAM2]] | +0.62 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[FSIP2-AS1]] | +0.62 | +0.47 / +0.68 | both halves | 2e-05 |  |
| [[USP34]] | +0.62 | +0.39 / +0.66 | both halves | 5e-05 |  |
| [[BPTF]] | +0.61 | +0.55 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00674]] | -0.57 | -0.63 / -0.46 | both halves | 3e-05 |  |
| [[AHDC1]] | -0.56 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[CEP295NL]] | -0.53 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[TIMP2]] | -0.53 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[IFI27L1]] | -0.52 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[BCAS4]] | -0.52 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[IDH2]] | -0.51 | -0.53 / -0.40 | both halves | 4e-05 |  |
| [[GPR160]] | -0.51 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[RAB8B]] | -0.51 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[LMBR1L]] | -0.51 | -0.53 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PMFBP1]] | B | PMFBP1 activity raises PRH1's level | lines that do not express PMFBP1 (8) vs lines expressing it (42) | 2.15× lower at baseline in the lines without PMFBP1 | 0.031 | ⚠ within organs, on part of the lines; also absent: GALNT16, FSIP2-AS1, ENSG00000237356; maybe low, not absent |
| [[FSIP2-AS1]] | B | FSIP2-AS1 activity raises PRH1's level | lines that do not express FSIP2-AS1 (6) vs lines expressing it (44) | 2.32× lower at baseline in the lines without FSIP2-AS1 | 0.031 | ⚠ within organs, on part of the lines; also absent: PMFBP1, SPATA17, ENSG00000287621; maybe low, not absent |
| [[LINC01505]] | B | LINC01505 activity raises PRH1's level | lines that do not express LINC01505 (5) vs lines expressing it (45) | 2.18× lower at baseline in the lines without LINC01505 | 0.074 | ⚠ within organs, on part of the lines; also absent: EID2, CENPP, ENSG00000223727; maybe low, not absent |
| [[LINC02516]] | B | LINC02516 activity raises PRH1's level | lines that do not express LINC02516 (19) vs lines expressing it (31) | 1.51× lower at baseline in the lines without LINC02516 | 0.088 | ⚠ within organs, on part of the lines; also absent: ADAM23, TEK, SPOCK3 |
| [[TAS2R14]] | C | TAS2R14's natural level strengthens PRH1's drug response | TAS2R14's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.75, reverse +0.64; direction not clear | 0.002 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PRR4]] | C | PRR4's natural level strengthens PRH1's drug response | PRR4's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.67, reverse +0.63; direction not clear | 0.032 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TAS2R14]] | C | PRH1's natural level strengthens TAS2R14's drug response | PRH1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.75; direction not clear | 0.059 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.438). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-22.8, 14.1); signed map (6.8, -43.0). **Vector** length 116, 41.2% of its response variance represented; |z| ≥ 3 in 1,211 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.4 | -1.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.5 | +0.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.7 | -1.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.7 | -2.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | +4.3 | -3.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.8 | +2.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.6 | +2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.4 | -0.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.2 | -1.7 |
|  | [[Gefitinib (drug)]] 5 µM |  | +2.9 | +1.7 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.5 | -17.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -6.2 | -10.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.6 | -14.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -5.4 | -7.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | -2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | -2.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.4 | -2.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -3.3 | -4.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.3 | -4.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -3.2 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | proline rich protein HaeIII subfamily 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.2 — chr12:10,824,960-11,171,608 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Pa |
| Gene groups (HGNC) | Proline rich proteins; Proteins encoded by multiple genes |
| Matched by | ensembl_id |

**Function**, from UniProt [P02810](https://www.uniprot.org/uniprotkb/P02810) (Salivary acidic proline-rich phosphoprotein 1/2):

> PRP's act as highly potent inhibitors of crystal growth of calcium phosphates. They provide a protective and reparative environment for dental enamel which is important for the integrity of the teeth.

**Summary**, from NCBI Gene [5554](https://www.ncbi.nlm.nih.gov/gene/5554):

> This gene encodes a member of the heterogeneous family of proline-rich salivary glycoproteins. The encoded preproprotein undergoes proteolytic processing to generate one or more mature isoforms before secretion from the parotid and submandibular/sublingual glands. Multiple distinct alleles of this locus including the parotid isoelectric-focusing variant slow (PIF-s), the parotid acidic protein (Pa), and the double band slow (Db-s) isoforms have been characterized. The reference genome encodes …

**Accessions** — [HGNC:9366](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9366) · Entrez [5554](https://www.ncbi.nlm.nih.gov/gene/5554) · UniProt [P02810](https://www.uniprot.org/uniprotkb/P02810) · Ensembl [ENSG00000231887](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000231887)

## Data

Gene col 13819: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13819); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13819, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13819]; `tensor/DDL_lfc|DDL_z.npy` [13819]; `embed/gene_vectors.npy` [13819]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13819 or target_col == 13819). Every well: [[PRH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
