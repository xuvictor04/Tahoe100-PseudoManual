---
symbol: "ECHDC1"
type: "gene"
col: 1720
ensembl_id: "ENSG00000093144"
name: "ethylmalonyl-CoA decarboxylase 1"
location: "6q22.33"
module: 5
arm: "+"
pooled_cpm: 68.75
n_lines_expressing: 48
n_dd_up: 9
n_dd_down: 4
n_dd_up_clean: 7
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# ECHDC1

*ethylmalonyl-CoA decarboxylase 1* — 6q22.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 1.94× (z +11.7, q 9e-29, up in 38 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.547× (z -20.4, q 0e+00, down in 39 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR12]] (+0.66, fdr 1e-05), [[TGFBRAP1]] (+0.61, fdr 1e-05), [[FAM120C]] (+0.61, fdr 2e-05); moves opposite to [[PTPRH]] (-0.64, fdr 3e-05), [[WASF2]] (-0.64, fdr 4e-05), [[SPAG9]] (-0.61, fdr 1e-04).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[NCR3LG1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 15 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1720.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.94×** | +11.7 | 9e-29 | 38/47 (LoVo, A-172, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.37×** | +10.6 | 7e-24 | 28/47 (NCI-H23, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.77×** | +10.0 | 2e-21 | 31/46 (LoVo, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.21×** | +9.0 | 2e-17 | 20/46 (NCI-H2347, A549, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.25×** | +7.4 | 1e-11 | 22/46 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.24×** | +7.2 | 7e-11 | 23/46 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +6.0 | 1e-07 | 18/46 (SW480, SW 900, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +5.1 | 2e-05 | 18/46 (SW480, LS 180, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.17× | +5.1 | 2e-05 | 15/45 (HEC-1-A, SW480, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains <1% of this change | 1.16× | +4.8 | 1e-04 | 18/45 (A-172, SK-MEL-2, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +4.7 | 2e-04 | 13/45 (LoVo, SNU-423, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.14× | +4.4 | 6e-04 | 14/46 (SW480, LS 180, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~4% of this change | 1.15× | +4.3 | 7e-04 | 18/43 (HOP62, SNU-423, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 1.14× | +4.3 | 7e-04 | 15/46 (AsPC-1, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~5% of this change | 1.14× | +4.2 | 0.001 | 17/41 (HT-29, SK-MEL-2, …) | all doses, flat | composition shift |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.25×** | +3.9 | 0.003 | 7/46 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.24×** | +3.8 | 0.004 | 7/46 (J82, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.24×** | +3.7 | 0.005 | 13/46 (J82, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 1.11× | +3.6 | 0.009 | 13/46 (LOX-IMVI, NCI-H2030, …) | top dose only |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | 1.15× | +3.3 | 0.023 | 4/46 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | 1.18× | +2.9 | 0.076 | 4/46 (LOX-IMVI, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | 1.12× | +2.8 | 0.100 | 3/46 (PANC-1, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1720.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.547×** | -20.4 | 0e+00 | 39/46 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.597×** | -17.4 | 0e+00 | 40/46 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.648×** | -14.6 | 0e+00 | 41/46 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.788×** | -8.0 | 2e-13 | 26/46 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 0.894× | -5.3 | 1e-05 | 19/46 (LoVo, SW480, …) | top dose only | composition shift |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 0.852× | -5.2 | 2e-05 | 16/45 (HS-578T, SW480, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.876× | -4.4 | 8e-04 | 14/46 (AsPC-1, SK-MEL-2, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.878× | -4.4 | 8e-04 | 18/46 (SW 1271, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.916× | -4.2 | 0.002 | 13/46 (SW480, RKO, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.885× | -4.1 | 0.002 | 13/45 (SK-MEL-2, LS 180, …) | rises with dose | low cells (technical?) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~5% of this change | 0.887× | -4.0 | 0.003 | 18/46 (SW 1271, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | 0.886× | -3.8 | 0.007 | 13/45 (CHP-212, SW1417, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.913× | -3.5 | 0.018 | 11/46 (NCI-H460, A-427, …) | two highest doses | noisy plate (z scaled) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 0.897× | -3.5 | 0.018 | 11/45 (A549, SW48, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.902× | -3.5 | 0.020 | 6/46 (KATO III, SNU-423, …) | rises with dose |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.910× | -3.2 | 0.054 | 10/46 (HCT15, NCI-H2030, …) | inconsistent across doses |  |
| [[Isocorydine (drug)]] 0.5 µM |  | 0.911× | -3.1 | 0.058 | 7/46 (MIA PaCa-2, A549, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1720. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 132 | 2 (1 ⚠) | 5 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.64× (z +9.1) | [[Panobinostat (drug)]] 0.5 µM 0.366× (z -18.5) |
| [[A-172 (line)]] | wt | 62.2 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +13.6) ⚠ cell-cycle shift, explains ~5% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.09× (z +9.2) | — |
| [[J82 (line)]] | alt | 66.8 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.56× (z +8.5) ⚠ cell-cycle shift, explains ~5% of this change | [[Panobinostat (drug)]] 0.5 µM 0.445× (z -10.8) |
| [[NCI-H460 (line)]] | wt | 58.7 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.467× (z -11.6) |
| [[RKO (line)]] | wt | 108 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.333× (z -13.6) |
| [[A-427 (line)]] | wt | 56.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.159× (z -19.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~4% of this change |
| [[KATO III (line)]] | alt | 73.3 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.255× (z -16.2) |
| [[LoVo (line)]] | wt | 73.6 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.10× (z +11.5) | [[Homoharringtonine (drug)]] 5 µM 0.522× (z -14.3) ⚠ cell-cycle shift, explains ~5% of this change |
| [[LOX-IMVI (line)]] | wt | 75.3 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.334× (z -15.0) |
| [[SW1417 (line)]] | alt | 58.0 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.362× (z -12.4) |
| [[LS 180 (line)]] | wt | 80.1 | 1 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.20× (z +10.6) | [[Panobinostat (drug)]] 0.5 µM 0.447× (z -10.7) |
| [[NCI-H2347 (line)]] | alt | 39.9 | 1 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.76× (z +9.9) ⚠ cell-cycle shift, explains ~10% of this change | [[Belinostat (drug)]] 5 µM 0.493× (z -8.7) |
| [[PANC-1 (line)]] | alt | 136 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.598× (z -9.4) |
| [[SHP-77 (line)]] | alt | 88.0 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.440× (z -9.8) |
| [[SNU-423 (line)]] | alt | 114 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +13.9) ⚠ cell-cycle shift, explains ~5% of this change | — |
| [[AN3 CA (line)]] | alt | 99.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0917× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~5% of this change |
| [[H4 (line)]] | wt | 69.5 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.280× (z -10.2) |
| [[HepG2_C3A (line)]] | wt | 75.8 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.385× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~7% of this change |
| [[HOP62 (line)]] | alt | 52.2 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.527× (z -8.8) |
| [[HS-578T (line)]] | alt | 64.2 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.448× (z -9.7) |
| [[NCI-H1792 (line)]] | alt | 71.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.512× (z -10.4) ⚠ cell-cycle shift, explains ~5% of this change |
| [[NCI-H23 (line)]] | alt | 53.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.69× (z +10.2) ⚠ toxic; transcription drop | — |
| [[NCI-H661 (line)]] | alt | 45.6 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0997× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 95.1 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.388× (z -9.0) |
| [[SNU-1 (line)]] | wt | 89.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.185× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~5% of this change |
| [[SW 1271 (line)]] | alt | 91.0 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.124× (z -9.5) ⚠ transcription drop; cell-cycle shift, explains ~5% of this change |
| [[A498 (line)]] | wt | 48.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 46.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.09 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 73.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 58.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 102 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 81.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 73.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 52.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 78.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 80.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.34 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 60.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 67.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 97.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 91.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1720), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR12]] | +0.66 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[TGFBRAP1]] | +0.61 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[FAM120C]] | +0.61 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[NAF1]] | +0.60 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[ALG8]] | +0.60 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[GTF3C6]] | +0.59 | +0.33 / +0.41 | both halves | 1e-04 |  |
| [[RMDN2]] | +0.59 | +0.42 / +0.38 | both halves | 7e-05 |  |
| [[PRR3]] | +0.59 | +0.40 / +0.42 | both halves | 5e-05 |  |
| [[MTREX]] | +0.58 | +0.36 / +0.57 | both halves | 1e-04 |  |
| [[NNT]] | +0.58 | +0.33 / +0.51 | both halves | 1e-04 |  |
| [[MRRF]] | +0.58 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[NSMAF]] | +0.58 | +0.38 / +0.51 | both halves | 7e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTPRH]] | -0.64 | -0.63 / -0.44 | both halves | 3e-05 |  |
| [[WASF2]] | -0.64 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[SPAG9]] | -0.61 | -0.53 / -0.34 | both halves | 1e-04 |  |
| [[DLGAP4]] | -0.61 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[CDKN2D]] | -0.61 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[RRAS]] | -0.59 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[OAZ1]] | -0.59 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[TMEM184B]] | -0.59 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[GNAI2]] | -0.59 | -0.38 / -0.39 | both halves | 7e-05 |  |
| [[NDRG1]] | -0.59 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[RAB11FIP1]] | -0.58 | -0.47 / -0.40 | both halves | 4e-05 |  |
| [[PORCN]] | -0.57 | -0.41 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NCR3LG1]] | B | NCR3LG1 activity raises ECHDC1's level | lines that do not express NCR3LG1 (7) vs lines expressing it (43) | 1.61× lower at baseline in the lines without NCR3LG1 | 0.023 | ⚠ within organs, on part of the lines; also absent: ENSG00000260196; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises ECHDC1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[IRF6]] | B | IRF6 activity lowers ECHDC1's level | lines that do not express IRF6 (31) vs lines expressing it (19) | 1.45× higher at baseline in the lines without IRF6 | 0.041 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.502). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (11.7, -0.7); signed map (5.1, -40.8). **Vector** length 102, 23.1% of its response variance represented; |z| ≥ 3 in 1,034 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +7.6 | +9.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~5% of this change | +6.2 | +4.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.1 | +10.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.5 | +11.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | +5.1 | +2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.3 | +10.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +0.4 |
|  | [[EX229 (drug)]] 5 µM |  | +3.6 | +3.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.5 | +2.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.2 | +1.7 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -4.9 | -17.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.8 | -20.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.1 | -14.6 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -3.1 | -3.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | -3.1 | -5.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.8 | -4.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.3 | -0.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.2 | -2.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.2 | -2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | ethylmalonyl-CoA decarboxylase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q22.33 — chr6:127,288,712-127,343,609 (-) |
| Ensembl biotype | protein_coding |
| Also known as | dJ351K20.2 |
| Gene groups (HGNC) | Decarboxylases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NTX5](https://www.uniprot.org/uniprotkb/Q9NTX5) (Ethylmalonyl-CoA decarboxylase):

> Decarboxylates ethylmalonyl-CoA, a potentially toxic metabolite, to form butyryl-CoA, suggesting it might be involved in metabolite proofreading. Acts preferentially on (S)-ethylmalonyl-CoA but also has some activity on the (R)-isomer (By similarity). Also has methylmalonyl-CoA decarboxylase activity at lower level (By similarity).

**Summary**, from NCBI Gene [55862](https://www.ncbi.nlm.nih.gov/gene/55862):

> Predicted to enable carboxy-lyase activity. Predicted to be involved in fatty acid beta-oxidation. Predicted to be active in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21489](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21489) · Entrez [55862](https://www.ncbi.nlm.nih.gov/gene/55862) · UniProt [Q9NTX5](https://www.uniprot.org/uniprotkb/Q9NTX5) · Ensembl [ENSG00000093144](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000093144)

## Data

Gene col 1720: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1720); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1720, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1720]; `tensor/DDL_lfc|DDL_z.npy` [1720]; `embed/gene_vectors.npy` [1720]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1720 or target_col == 1720). Every well: [[ECHDC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ECHDC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
