---
symbol: "PTPRG"
type: "gene"
col: 6919
ensembl_id: "ENSG00000144724"
name: "protein tyrosine phosphatase receptor type G"
location: "3p14.2"
module: 5
arm: "+"
pooled_cpm: 219.81
n_lines_expressing: 42
n_dd_up: 19
n_dd_down: 13
n_dd_up_clean: 16
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 4
direction_downstream: 2
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# PTPRG

*protein tyrosine phosphatase receptor type G* — 3p14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.23× (z +19.4, q 0e+00, up in 35 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.366× (z -17.2, q 0e+00, down in 38 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SIPA1L1]] (+0.69, fdr 7e-06), [[ENOX2]] (+0.67, fdr 1e-05), [[DGKH]] (+0.66, fdr 1e-05); moves opposite to [[FAM229B]] (-0.61, fdr 1e-05), [[CCDC127]] (-0.60, fdr 1e-05), [[RAB3A]] (-0.60, fdr 4e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → cells under [[Tirabrutinib (hydrochloride) (drug)]] 0.05 µM (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6919.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.23×** | +19.4 | 0e+00 | 35/41 (A-172, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.23×** | +13.2 | 3e-37 | 37/40 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.54×** | +10.4 | 4e-23 | 34/40 (A-172, HEC-1-A, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +9.6 | 2e-19 | 32/42 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.67×** | +8.8 | 2e-16 | 36/40 (NCI-H460, HEC-1-A, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.36×** | +5.3 | 1e-05 | 31/40 (RPMI-7951, HS-578T, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.32×** | +4.5 | 5e-04 | 25/40 (C32, A-172, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.28×** | +4.3 | 0.001 | 26/40 (RPMI-7951, HS-578T, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.58×** | +4.1 | 0.003 | 19/38 (NCI-H1792, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.27×** | +4.1 | 0.003 | 22/40 (A-172, HepG2/C3A, …) | rises with dose |  |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.25×** | +3.8 | 0.006 | 23/40 (COLO 205, SNU-1, …) | inconsistent across doses |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **1.25×** | +3.8 | 0.006 | 19/42 (RPMI-7951, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.25×** | +3.7 | 0.010 | 23/40 (NCI-H2347, SW480, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.24×** | +3.7 | 0.010 | 21/40 (RPMI-7951, HS-578T, …) | all doses, flat |  |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | **1.24×** | +3.6 | 0.012 | 22/40 (RPMI-7951, COLO 205, …) | inconsistent across doses |  |
| [[Penfluridol (drug)]] 5 µM |  | **1.24×** | +3.6 | 0.014 | 21/39 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Budesonide (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.018 | 20/40 (RPMI-7951, hTERT-HPNE, …) | rises with dose |  |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | **1.22×** | +3.4 | 0.019 | 20/41 (COLO 205, LS 180, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6919.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.366×** | -17.2 | 0e+00 | 38/40 (SNU-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.397×** | -15.8 | 0e+00 | 40/40 (C32, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.452×** | -13.6 | 9e-40 | 39/40 (LoVo, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.655×** | -7.0 | 5e-10 | 30/39 (LOX-IMVI, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | **0.710×** | -5.9 | 5e-07 | 28/40 (KATO III, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **0.573×** | -5.0 | 6e-05 | 27/41 (SNU-1, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **0.830×** | -4.5 | 5e-04 | 22/40 (C32, NCI-H23, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.781×** | -4.2 | 0.002 | 19/40 (KATO III, SW48, …) | top dose only | composition shift |
| [[Retinoic acid (drug)]] 5 µM |  | 0.842× | -4.2 | 0.002 | 19/41 (RPMI-7951, HS-578T, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.801×** | -3.8 | 0.009 | 22/40 (LoVo, SK-MEL-2, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.658×** | -3.7 | 0.009 | 24/39 (H4, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.804×** | -3.7 | 0.009 | 24/41 (KATO III, HEC-1-A, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.823×** | -3.3 | 0.037 | 19/40 (LoVo, LS 180, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.815×** | -3.2 | 0.048 | 19/39 (HEC-1-A, RKO, …) | all doses, stronger at high dose |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.881× | -3.1 | 0.084 | 8/41 (Panc 03.27, SW1417, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6919. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 613 | 1 | 12 (7 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +12.2) | [[Panobinostat (drug)]] 0.5 µM 0.153× (z -20.8) |
| [[RPMI-7951 (line)]] | alt | 554 | 11 | 2 | [[Clobetasol propionate (drug)]] 0.05 µM 3.75× (z +13.5) | [[Panobinostat (drug)]] 5 µM 0.380× (z -9.9) |
| [[C32 (line)]] | wt | 562 | 2 | 10 (7 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.62× (z +10.0) | [[Panobinostat (drug)]] 0.5 µM 0.213× (z -22.8) |
| [[LOX-IMVI (line)]] | wt | 1,106 | 0 | 12 (8 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.197× (z -20.3) |
| [[NCI-H460 (line)]] | wt | 177 | 4 (1 ⚠) | 7 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.66× (z +20.7) | [[Harringtonine (drug)]] 5 µM 0.287× (z -13.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.303× (z -13.5) |
| [[A-172 (line)]] | wt | 102 | 10 (5 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.33× (z +22.6) | — |
| [[HepG2_C3A (line)]] | wt | 320 | 4 | 6 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.59× (z +21.4) | [[Panobinostat (drug)]] 0.5 µM 0.295× (z -14.5) |
| [[HOP62 (line)]] | alt | 316 | 7 (1 ⚠) | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +17.0) | [[Panobinostat (drug)]] 5 µM 0.395× (z -11.9) |
| [[HEC-1-A (line)]] | alt | 150 | 6 (1 ⚠) | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.11× (z +21.0) | [[Panobinostat (drug)]] 5 µM 0.395× (z -12.3) |
| [[hTERT-HPNE (line)]] | wt | 308 | 7 | 2 | [[Clobetasol propionate (drug)]] 0.05 µM 3.19× (z +10.0) | [[Panobinostat (drug)]] 0.5 µM 0.328× (z -9.6) |
| [[HS-578T (line)]] | alt | 438 | 5 | 3 | [[Clobetasol propionate (drug)]] 0.05 µM 2.53× (z +11.3) | [[Panobinostat (drug)]] 5 µM 0.290× (z -15.0) |
| [[LS 180 (line)]] | wt | 269 | 3 | 5 (1 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 3.81× (z +12.7) | [[Panobinostat (drug)]] 0.5 µM 0.281× (z -12.5) |
| [[RKO (line)]] | wt | 441 | 3 | 5 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +12.2) | [[Panobinostat (drug)]] 0.5 µM 0.188× (z -18.8) |
| [[SNU-1 (line)]] | wt | 529 | 1 | 7 (3 ⚠) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 1.66× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.162× (z -21.8) |
| [[SW48 (line)]] | wt | 302 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -13.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.334× (z -10.5) |
| [[A549 (line)]] | wt | 75.0 | 3 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.97× (z +15.4) | [[Panobinostat (drug)]] 5 µM 0.317× (z -11.6) |
| [[KATO III (line)]] | alt | 249 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.216× (z -16.8) |
| [[C-33 A (line)]] | alt | 467 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.167× (z -20.3) |
| [[SK-MEL-2 (line)]] | alt | 514 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -22.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.406× (z -11.7) |
| [[Hs 766T (line)]] | wt | 92.2 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.41× (z +12.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 59.7 | 2 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.95× (z +13.0) | [[Adagrasib (drug)]] 0.05 µM 0.552× (z -17.4) ⚠ position not correctable · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.322× (z -9.7) |
| [[NCI-H2030 (line)]] | alt | 334 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.462× (z -12.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.368× (z -11.5) |
| [[NCI-H2347 (line)]] | alt | 84.2 | 5 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.27× (z +16.4) | — |
| [[Panc 03.27 (line)]] | alt | 157 | 3 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.84× (z +15.4) | [[Panobinostat (drug)]] 5 µM 0.312× (z -12.1) |
| [[SW480 (line)]] | alt | 91.9 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +11.6) | [[Panobinostat (drug)]] 5 µM 0.242× (z -14.2) |
| [[A-427 (line)]] | wt | 127 | 1 | 2 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 1.89× (z +11.5) | [[Panobinostat (drug)]] 0.5 µM 0.466× (z -9.7) |
| [[A498 (line)]] | wt | 184 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.388× (z -9.7) |
| [[J82 (line)]] | alt | 450 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.321× (z -13.6) |
| [[NCI-H23 (line)]] | alt | 82.3 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.199× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change · without an alert: [[Binimetinib (drug)]] 5 µM 0.391× (z -8.6) |
| [[SNU-423 (line)]] | alt | 142 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +13.9) | — |
| [[SW1417 (line)]] | alt | 84.3 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.04× (z +15.7) | — |
| [[BT-474 (line)]] | alt | 157 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +9.1) | [[Panobinostat (drug)]] 0.5 µM 0.350× (z -10.4) |
| [[COLO 205 (line)]] | alt | 65.0 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.58× (z +12.4) | — |
| [[HCT15 (line)]] | alt | 226 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.54× (z +11.4) | [[Homoharringtonine (drug)]] 5 µM 0.493× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 146 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.53× (z +12.4) | — |
| [[CHP-212 (line)]] | wt | 236 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -9.6) ⚠ cell-cycle shift, would explain all of this change |
| [[SW 1088 (line)]] | alt | 173 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.0986× (z -8.5) |
| [[SW 1271 (line)]] | alt | 181 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.169× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change |
| [[AN3 CA (line)]] | alt | 43.9 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 52.9 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 18.0 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 373 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.8 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 19.3 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 86.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 239 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.8 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 33.5 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 15.3 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6919), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIPA1L1]] | +0.69 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[ENOX2]] | +0.67 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[DGKH]] | +0.66 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[E2F3]] | +0.66 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[PRMT3]] | +0.65 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[EPM2A]] | +0.63 | +0.57 / +0.43 | both halves | 3e-05 |  |
| [[MSANTD2]] | +0.63 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[PRR5L]] | +0.63 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[NHSL1]] | +0.63 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[PIGW]] | +0.62 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[GABPB1-AS1]] | +0.62 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[STXBP5]] | +0.62 | +0.55 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM229B]] | -0.61 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[CCDC127]] | -0.60 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[RAB3A]] | -0.60 | -0.51 / -0.40 | both halves | 4e-05 |  |
| [[KBTBD3]] | -0.59 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[ALAD]] | -0.59 | -0.43 / -0.44 | both halves | 3e-05 | pathway: HALLMARK_FATTY_ACID_METABOLISM |
| [[DBP]] | -0.59 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[IFT172]] | -0.58 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[AHDC1]] | -0.58 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[IFT52]] | -0.58 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[DDAH2]] | -0.58 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[GOLPH3L]] | -0.57 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[USP30]] | -0.57 | -0.52 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PTPRG's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[COL27A1]] | B | COL27A1 activity raises PTPRG's level | lines that do not express COL27A1 (12) vs lines expressing it (38) | 2.61× lower at baseline in the lines without COL27A1 | 0.058 | ⚠ within organs, on part of the lines; also absent: C13orf46, ENSG00000285804, GSDME; maybe low, not absent |
| [[GPRC5B]] | B | GPRC5B activity lowers PTPRG's level | lines that do not express GPRC5B (27) vs lines expressing it (23) | 1.24× higher at baseline in the lines without GPRC5B | 0.094 | ⚠ within organs, on part of the lines; also absent: PALMD, FYB1, AK5 |
| [[MSRB3]] | B | MSRB3 activity raises PTPRG's level | lines that do not express MSRB3 (20) vs lines expressing it (30) | 1.81× lower at baseline in the lines without MSRB3 | 0.095 | ⚠ within organs, on part of the lines; also absent: ARHGEF6, KCNG1, FHL1 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Tirabrutinib (hydrochloride) (drug)]] 0.05 µM | B | PTPRG activity raises the cells' numbers under Tirabrutinib (hydrochloride) 0.05 µM (protects the cells) | lines that do not express PTPRG (8) vs lines expressing it (40) | the lines without PTPRG: 0.83× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines |
| [[PCNX1]] | B | PTPRG activity raises PCNX1's level | lines that do not express PTPRG (8) vs lines expressing it (42) | 1.21× lower at baseline in the lines without PTPRG | 0.0995 | ⚠ within organs, on part of the lines |

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.664). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (8.1, -6.8); signed map (15.7, -6.6). **Vector** length 150, 50.4% of its response variance represented; |z| ≥ 3 in 1,488 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +12.3 | +19.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +11.0 | +13.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +10.0 | +10.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +9.8 | +9.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +8.8 | +8.8 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +5.9 | +5.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +4.7 | +4.3 |
|  | [[Budesonide (drug)]] 5 µM |  | +4.6 | +3.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.5 | +3.7 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -9.1 | -15.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | -7.7 | -17.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -7.0 | -13.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -5.4 | -4.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.8 | -7.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.5 | -3.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.4 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.1 | -2.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.7 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | protein tyrosine phosphatase receptor type G |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p14.2 — chr3:61,561,569-62,297,609 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RPTPG; previously PTPG |
| Gene groups (HGNC) | Fibronectin type III domain containing; Protein tyrosine phosphatases receptor type |
| Hallmark sets | FATTY_ACID_METABOLISM |
| Matched by | ensembl_id |

**Function**, from UniProt [P23470](https://www.uniprot.org/uniprotkb/P23470) (Receptor-type tyrosine-protein phosphatase gamma):

> Possesses tyrosine phosphatase activity.

**Summary**, from NCBI Gene [5793](https://www.ncbi.nlm.nih.gov/gene/5793):

> The protein encoded by this gene is a member of the protein tyrosine phosphatase (PTP) family. PTPs are known to be signaling molecules that regulate a variety of cellular processes including cell growth, differentiation, mitotic cycle, and oncogenic transformation. This PTP possesses an extracellular region, a single transmembrane region, and two tandem intracytoplasmic catalytic domains, and thus represents a receptor-type PTP. The extracellular region of this PTP contains a carbonic …

**Accessions** — [HGNC:9671](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9671) · Entrez [5793](https://www.ncbi.nlm.nih.gov/gene/5793) · UniProt [P23470](https://www.uniprot.org/uniprotkb/P23470) · Ensembl [ENSG00000144724](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144724)

## Data

Gene col 6919: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6919); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6919, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6919]; `tensor/DDL_lfc|DDL_z.npy` [6919]; `embed/gene_vectors.npy` [6919]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6919 or target_col == 6919). Every well: [[PTPRG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTPRG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
