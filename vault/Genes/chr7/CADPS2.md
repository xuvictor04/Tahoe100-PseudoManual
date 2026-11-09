---
symbol: "CADPS2"
type: "gene"
col: 1325
ensembl_id: "ENSG00000081803"
name: "calcium dependent secretion activator 2"
location: "7q31.32"
module: 49
arm: "+"
pooled_cpm: 156.22
n_lines_expressing: 36
n_dd_up: 0
n_dd_down: 40
n_dd_up_clean: 0
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 3
direction_downstream: 14
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# CADPS2

*calcium dependent secretion activator 2* — 7q31.32

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H460 2.02×, RKO 2.29×; ⚠ cell-cycle shift, explains ~0% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 2.60×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (C32 2.30×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 40 drug-doses (19 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.307× (z -18.0, q 0e+00, down in 32 of 34 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLPP5]] (+0.61, fdr 1e-05), [[SLC15A2]] (+0.60, fdr 7e-06), [[NPIPB14P]] (+0.59, fdr 1e-05); moves opposite to [[TAF1B]] (-0.44, fdr 4e-05), [[KIF3C]] (-0.44, fdr 9e-05), [[AHNAK2]] (-0.43, fdr 1e-04).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[SMARCA2]] → it (grade B ⚠); 14 go from it, the strongest it → [[PPM1K]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1325.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H460 2.02×, RKO 2.29×; ⚠ cell-cycle shift, explains ~0% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 2.60×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (C32 2.30×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Binimetinib (drug)]] 0.5 µM |  | 1.20× | +3.4 | 0.14 | 13/34 (CFPAC-1, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.4 | 0.14 | 15/35 (NCI-H460, RKO, …) | top dose only |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | 1.26× | +3.4 | 0.14 | 16/35 (NCI-H2347, SW1417, …) | top dose only | plate-row cell shift |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.24× | +3.3 | 0.14 | 14/33 (C32, CFPAC-1, …) | rises with dose |  |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | 1.26× | +3.1 | 0.19 | 14/34 (C32, CFPAC-1, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.23× | +3.0 | 0.19 | 16/33 (C32, CFPAC-1, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | 1.23× | +3.0 | 0.19 | 14/36 (NCI-H460, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 19 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 40 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1325.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.307×** | -18.0 | 0e+00 | 32/34 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.352×** | -15.9 | 0e+00 | 32/34 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.391×** | -13.2 | 9e-38 | 23/31 (SK-MEL-2, A498, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.452×** | -11.6 | 3e-29 | 30/33 (NCI-H1573, A498, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.475×** | -11.4 | 8e-28 | 31/34 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.488×** | -10.5 | 6e-24 | 27/34 (A498, J82, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **0.532×** | -9.6 | 5e-20 | 24/35 (A498, SK-MEL-2, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.307×** | -9.4 | 3e-19 | 32/35 (A498, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.550×** | -9.1 | 6e-18 | 28/34 (H4, NCI-H1573, …) | two highest doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **0.559×** | -8.9 | 5e-17 | 23/33 (NCI-H1573, KATO III, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **0.565×** | -8.4 | 3e-15 | 23/30 (A498, HCT15, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.598×** | -7.8 | 2e-13 | 25/34 (NCI-H1573, SW48, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.608×** | -7.6 | 1e-12 | 19/34 (NCI-H1573, KATO III, …) | rises with dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.747×** | -6.3 | 1e-08 | 22/34 (hTERT-HPNE, NCI-H1792, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.662×** | -6.3 | 1e-08 | 26/34 (NCI-H1573, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.541×** | -4.9 | 3e-05 | 19/34 (A-172, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.761×** | -4.2 | 9e-04 | 22/34 (NCI-H460, A498, …) | all doses, flat |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.763×** | -3.9 | 0.002 | 19/34 (SW480, BT-474, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.849× | -3.5 | 0.009 | 12/35 (BT-474, SHP-77, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.786×** | -3.5 | 0.009 | 18/33 (BT-474, A-172, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.799×** | -3.4 | 0.013 | 18/34 (KATO III, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.808×** | -3.2 | 0.023 | 16/34 (BT-474, Panc 03.27, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.811×** | -3.2 | 0.026 | 16/33 (SK-MEL-2, Panc 03.27, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1325. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 197 | 0 | 17 (11 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.148× (z -17.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.253× (z -12.9) |
| [[NCI-H460 (line)]] | wt | 153 | 2 (2 ⚠) | 14 (9 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +11.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.278× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.435× (z -9.7) |
| [[A498 (line)]] | wt | 670 | 0 | 12 (9 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.109× (z -24.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.238× (z -16.2) |
| [[KATO III (line)]] | alt | 480 | 0 | 12 (8 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0878× (z -21.1) |
| [[H4 (line)]] | wt | 259 | 0 | 9 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.157× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.191× (z -13.5) |
| [[SW 900 (line)]] | alt | 216 | 0 | 9 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.323× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.415× (z -9.6) |
| [[J82 (line)]] | alt | 131 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.256× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.269× (z -14.1) |
| [[LoVo (line)]] | wt | 483 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.141× (z -15.8) |
| [[SK-MEL-2 (line)]] | alt | 283 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.163× (z -20.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.293× (z -14.9) |
| [[NCI-H1792 (line)]] | alt | 309 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.281× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.303× (z -12.4) |
| [[SW48 (line)]] | wt | 258 | 0 | 7 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.186× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.265× (z -10.5) |
| [[SW480 (line)]] | alt | 205 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.183× (z -19.2) |
| [[A-172 (line)]] | wt | 74.7 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -16.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.228× (z -14.6) |
| [[hTERT-HPNE (line)]] | wt | 218 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.239× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.256× (z -12.2) |
| [[SW1417 (line)]] | alt | 282 | 0 | 6 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.261× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.274× (z -12.7) |
| [[RPMI-7951 (line)]] | alt | 79.2 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -11.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.222× (z -10.6) |
| [[COLO 205 (line)]] | alt | 290 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.135× (z -15.2) |
| [[RKO (line)]] | wt | 117 | 1 (1 ⚠) | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.147× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.0955× (z -8.9) |
| [[HT-29 (line)]] | alt | 77.4 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.192× (z -10.3) |
| [[LS 180 (line)]] | wt | 260 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.158× (z -12.6) |
| [[Panc 03.27 (line)]] | alt | 96.8 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.280× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.321× (z -10.5) |
| [[C32 (line)]] | wt | 110 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +8.9) ⚠ cell-cycle shift, would explain all of this change | [[Harringtonine (drug)]] 0.5 µM 0.314× (z -8.7) ⚠ cell-cycle shift, explains ~53% of this change |
| [[CFPAC-1 (line)]] | alt | 168 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.382× (z -9.4) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.416× (z -8.9) |
| [[HCT15 (line)]] | alt | 130 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0549× (z -19.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.286× (z -8.5) |
| [[HOP62 (line)]] | alt | 65.1 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.301× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.359× (z -8.7) |
| [[BT-474 (line)]] | alt | 171 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.234× (z -8.5) |
| [[HS-578T (line)]] | alt | 44.6 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.243× (z -9.8) |
| [[SHP-77 (line)]] | alt | 181 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.358× (z -10.5) |
| [[A-427 (line)]] | wt | 26.6 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 23.8 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 24.8 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 16.3 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 14.1 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 63.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.2 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 64.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 35.3 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 15.7 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.46 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 38.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.1 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 88.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.7 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 31.2 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 13.9 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 126 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1325), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLPP5]] | +0.61 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[SLC15A2]] | +0.60 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[NPIPB14P]] | +0.59 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[SERP1]] | +0.59 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[DNAJB9]] | +0.59 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[MCEE]] | +0.55 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[SLC39A7]] | +0.54 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[LARP1B]] | +0.54 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[SRPRA]] | +0.54 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[ALG11]] | +0.52 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[XBP1]] | +0.50 | +0.48 / +0.39 | both halves | 5e-05 |  |
| [[TNFSF13B]] | +0.50 | +0.40 / +0.47 | both halves | 4e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAF1B]] | -0.44 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[KIF3C]] | -0.44 | -0.40 / -0.37 | both halves | 9e-05 |  |
| [[AHNAK2]] | -0.43 | -0.40 / -0.33 | both halves | 1e-04 | STRING 410 |
| [[BCKDK]] | -0.43 | -0.43 / -0.30 | both halves | 2e-04 |  |
| [[PLBD2]] | -0.42 | -0.38 / -0.33 | both halves | 1e-04 |  |
| [[MYORG]] | -0.42 | -0.32 / -0.38 | both halves | 2e-04 |  |
| [[RAP1GAP2]] | -0.41 | -0.41 / -0.34 | both halves | 1e-04 |  |
| [[ADAMTSL5]] | -0.41 | -0.33 / -0.34 | both halves | 1e-04 |  |
| [[CEBPZOS]] | -0.41 | -0.41 / -0.35 | both halves | 1e-04 |  |
| [[CAPG]] | -0.41 | -0.33 / -0.38 | both halves | 1e-04 |  |
| [[TNK2]] | -0.41 | -0.39 / -0.19 | ⚠ not reproduced | 9e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMARCA2]] | B | SMARCA2 activity raises CADPS2's level | lines that do not express SMARCA2 (6) vs lines expressing it (44) | 4.64× lower at baseline in the lines without SMARCA2 | 0.040 | ⚠ within organs, on part of the lines; also absent: CEMIP2, S100A13, PYROXD2 |
| [[GRHL2]] | B | GRHL2 activity raises CADPS2's level | lines that do not express GRHL2 (34) vs lines expressing it (16) | 2.50× lower at baseline in the lines without GRHL2 | 0.068 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4 |
| [[CA3]] | C | CA3 activity raises CADPS2's level | lines that do not express CA3 (10) vs lines expressing it (40) | 3.87× lower at baseline in the lines without CA3 | 0.042 | ⚠ within organs, on part of the lines; also absent: CA13, NAALADL2, PLSCR2; co-absent with the target |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 13, C 1. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PPM1K]] | B | CADPS2 activity raises PPM1K's level | lines that do not express CADPS2 (14) vs lines expressing it (36) | 1.61× lower at baseline in the lines without CADPS2 | 0.025 | ⚠ within organs, on part of the lines; also absent: DGKG, RBPMS, FAM3B |
| [[PDXDC2P-NPIPB14P]] | B | CADPS2 activity raises PDXDC2P-NPIPB14P's level | lines that do not express CADPS2 (14) vs lines expressing it (36) | 1.69× lower at baseline in the lines without CADPS2 | 0.026 | ⚠ within organs, on part of the lines; also absent: DGKG, RBPMS, FAM3B |
| [[PCGF3-AS1]] | B | CADPS2 activity raises PCGF3-AS1's level | lines that do not express CADPS2 (14) vs lines expressing it (36) | 1.48× lower at baseline in the lines without CADPS2 | 0.031 | ⚠ within organs, on part of the lines; also absent: DGKG, RBPMS, FAM3B |
| [[TNFSF13B]] | B | CADPS2 activity raises TNFSF13B's level | lines that do not express CADPS2 (14) vs lines expressing it (36) | 1.72× lower at baseline in the lines without CADPS2 | 0.033 | ⚠ within organs, on part of the lines; also absent: DGKG, RBPMS, FAM3B |
| [[TAF1B]] | B | CADPS2 activity lowers TAF1B's level | lines that do not express CADPS2 (14) vs lines expressing it (36) | 1.60× higher at baseline in the lines without CADPS2 | 0.037 | ⚠ within organs, on part of the lines; also absent: DGKG, RBPMS, FAM3B |
| [[NFXL1]] | B | CADPS2 activity raises NFXL1's level | lines that do not express CADPS2 (14) vs lines expressing it (36) | 1.30× lower at baseline in the lines without CADPS2 | 0.055 | ⚠ within organs, on part of the lines; also absent: DGKG, RBPMS, FAM3B |
| [[DNAJC25]] | B | CADPS2 activity raises DNAJC25's level | lines that do not express CADPS2 (14) vs lines expressing it (36) | 1.33× lower at baseline in the lines without CADPS2 | 0.063 | ⚠ within organs, on part of the lines; also absent: DGKG, RBPMS, FAM3B |
| [[GABRR2]] | B | CADPS2 activity raises GABRR2's level | lines that do not express CADPS2 (14) vs lines expressing it (36) | 1.49× lower at baseline in the lines without CADPS2 | 0.074 | ⚠ within organs, on part of the lines; also absent: DGKG, RBPMS, FAM3B |
| [[DNAJB9]] | B | CADPS2 activity raises DNAJB9's level | lines that do not express CADPS2 (14) vs lines expressing it (36) | 1.64× lower at baseline in the lines without CADPS2 | 0.076 | ⚠ within organs, on part of the lines; also absent: DGKG, RBPMS, FAM3B |
| [[DNAJC3]] | B | CADPS2 activity raises DNAJC3's level | lines that do not express CADPS2 (14) vs lines expressing it (36) | 1.65× lower at baseline in the lines without CADPS2 | 0.078 | ⚠ within organs, on part of the lines; also absent: DGKG, RBPMS, FAM3B |
| [[MPC1]] | B | CADPS2 activity raises MPC1's level | lines that do not express CADPS2 (14) vs lines expressing it (36) | 1.61× lower at baseline in the lines without CADPS2 | 0.082 | ⚠ within organs, on part of the lines; also absent: DGKG, RBPMS, FAM3B |
| [[GRHL2]] | B | CADPS2 activity raises GRHL2's level | lines that do not express CADPS2 (14) vs lines expressing it (36) | 3.04× lower at baseline in the lines without CADPS2 | 0.087 | ⚠ within organs, on part of the lines; also absent: DGKG, RBPMS, FAM3B |

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.457). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.6, -36.1); signed map (-49.3, 13.9). **Vector** length 124, 40.5% of its response variance represented; |z| ≥ 3 in 1,160 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.4 | +3.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.1 | +3.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.7 | +2.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.9 | -1.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | +3.7 | -3.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.4 | +3.4 |
|  | [[Gefitinib (drug)]] 5 µM |  | +2.3 | +2.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.3 | +3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | -1.2 |
|  | [[Terfenadine (drug)]] 5 µM |  | +2.1 | +1.3 |
| fall | [[Selinexor (drug)]] 5 µM |  | -4.9 | -6.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -4.2 | -11.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.0 | -11.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.8 | -18.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.7 | -6.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.1 | -0.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | -9.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.9 | -4.2 |
|  | [[Belzutifan (drug)]] 5 µM |  | -2.7 | -3.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.7 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | calcium dependent secretion activator 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q31.32 — chr7:122,318,411-122,886,759 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CAPS2 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; C2 domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86UW7](https://www.uniprot.org/uniprotkb/Q86UW7) (Calcium-dependent secretion activator 2):

> Calcium-binding protein involved in exocytosis of vesicles filled with neurotransmitters and neuropeptides. Probably acts upstream of fusion in the biogenesis or maintenance of mature secretory vesicles. Regulates neurotrophin release from granule cells leading to regulate cell differentiation and survival during cerebellar development. May specifically mediate the Ca(2+)-dependent exocytosis of large dense-core vesicles (DCVs) and other dense-core vesicles (By similarity).

**Summary**, from NCBI Gene [93664](https://www.ncbi.nlm.nih.gov/gene/93664):

> This gene encodes a member of the calcium-dependent activator of secretion (CAPS) protein family, which are calcium binding proteins that regulate the exocytosis of synaptic and dense-core vesicles in neurons and neuroendocrine cells. Mutations in this gene may contribute to autism susceptibility. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Nov 2009]

**Accessions** — [HGNC:16018](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16018) · Entrez [93664](https://www.ncbi.nlm.nih.gov/gene/93664) · UniProt [Q86UW7](https://www.uniprot.org/uniprotkb/Q86UW7) · Ensembl [ENSG00000081803](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000081803)

## Data

Gene col 1325: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1325); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1325, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1325]; `tensor/DDL_lfc|DDL_z.npy` [1325]; `embed/gene_vectors.npy` [1325]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1325 or target_col == 1325). Every well: [[CADPS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CADPS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
