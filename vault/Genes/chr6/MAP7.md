---
symbol: "MAP7"
type: "gene"
col: 5719
ensembl_id: "ENSG00000135525"
name: "microtubule associated protein 7"
location: "6q23.3"
module: 31
arm: "+"
pooled_cpm: 153.92
n_lines_expressing: 29
n_dd_up: 8
n_dd_down: 11
n_dd_up_clean: 3
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 20
direction_downstream: 22
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# MAP7

*microtubule associated protein 7* — 6q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.86× (z +17.5, q 0e+00, up in 10 of 27 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Bortezomib (drug)]] 0.05 µM: 1.36× (z +8.2, q 7e-14, up in 16 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.519× (z -18.5, q 0e+00, down in 22 of 27 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DSC2]] (+0.61, fdr 1e-05), [[MYO5B]] (+0.54, fdr 1e-05), [[PATJ]] (+0.53, fdr 2e-05); moves opposite to [[TMEM39B]] (-0.51, fdr 5e-05), [[LOX]] (-0.45, fdr 8e-05), [[ZHX3]] (-0.43, fdr 2e-04).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 20 arrows point to it, the strongest [[XYLT1]] → it (grade B ⚠); 22 go from it, the strongest it → [[PATJ]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5719.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.86×** | +17.5 | 0e+00 | 10/27 (A549, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.36×** | +8.2 | 5e-14 | 7/23 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.36×** | +8.2 | 7e-14 | 16/27 (KATO III, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.30×** | +7.3 | 4e-11 | 14/27 (HT-29, NCI-H1573, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.27×** | +6.8 | 2e-09 | 16/27 (HT-29, COLO 205, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.23×** | +5.5 | 5e-06 | 7/24 (RKO, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 1.15× | +5.4 | 5e-06 | 3/27 (PANC-1, A-427, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.20×** | +5.2 | 1e-05 | 4/28 (PANC-1, A-427, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | 1.12× | +4.5 | 4e-04 | 8/27 (NCI-H1573, NCI-H2030, …) | rises with dose | low cells (technical?) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.34×** | +4.3 | 9e-04 | 9/25 (CFPAC-1, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[Penfluridol (drug)]] 5 µM |  | 1.17× | +4.2 | 0.001 | 4/26 (KATO III, NCI-H460, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 1.16× | +4.1 | 0.002 | 11/26 (NCI-H460, NCI-H2030, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +4.0 | 0.002 | 7/27 (NCI-H1573, COLO 205, …) | rises with dose | composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.15× | +3.8 | 0.005 | 9/26 (NCI-H460, A549, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.14× | +3.7 | 0.009 | 3/27 (RKO, PANC-1, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.13× | +3.5 | 0.014 | 12/26 (NCI-H2030, NCI-H460, …) | rises with dose | low cells (technical?) |
| [[Bortezomib (drug)]] 0.5 µM |  | 1.17× | +3.2 | 0.050 | 3/28 (PANC-1, COLO 205, …) | all doses, flat | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 5 µM |  | 1.12× | +3.1 | 0.067 | 2/27 (NCI-H2030, NCI-H23) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5719.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.519×** | -18.5 | 0e+00 | 22/27 (NCI-H460, SW480, …) | two highest doses | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.598×** | -14.5 | 3e-45 | 22/27 (NCI-H460, LoVo, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.619×** | -13.5 | 3e-39 | 21/27 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.744×** | -8.3 | 1e-14 | 9/27 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.774×** | -7.2 | 7e-11 | 7/27 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.785×** | -6.8 | 1e-09 | 7/27 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.657×** | -6.2 | 5e-08 | 19/28 (CFPAC-1, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.674×** | -5.8 | 4e-07 | 16/27 (HEC-1-A, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 0.867× | -5.7 | 9e-07 | 18/27 (NCI-H23, A549, …) | rises with dose | composition shift |
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.838× | -5.0 | 4e-05 | 7/27 (NCI-H460, NCI-H1573, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 0.894× | -4.4 | 5e-04 | 5/27 (NCI-H2030, PANC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.855× | -4.4 | 5e-04 | 13/27 (RKO, NCI-H23, …) | rises with dose |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 0.852× | -4.3 | 6e-04 | 7/27 (NCI-H2030, SW 900, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.902× | -4.1 | 0.002 | 6/27 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.762×** | -4.0 | 0.002 | 5/27 (LoVo, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | 0.874× | -3.7 | 0.009 | 6/27 (NCI-H23, NCI-H460, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 0.05 µM |  | 0.880× | -3.6 | 0.010 | 5/27 (NCI-H1573, A549, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | 0.882× | -3.5 | 0.013 | 6/27 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | 0.919× | -3.4 | 0.022 | 3/27 (NCI-H1573, A549, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5719. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 487 | 9 (2 ⚠) | 28 (9 ⚠) | [[Cobimetinib (drug)]] 5 µM 2.52× (z +11.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.211× (z -28.9) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.165× (z -23.7) |
| [[NCI-H1573 (line)]] | alt | 412 | 4 (4 ⚠) | 23 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.63× (z +15.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -17.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Dexamethasone (drug)]] 0.5 µM 0.312× (z -14.2) |
| [[A549 (line)]] | wt | 247 | 0 | 23 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.240× (z -22.8) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.229× (z -16.7) |
| [[HT-29 (line)]] | alt | 338 | 2 | 6 (4 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 1.99× (z +9.4) | [[Panobinostat (drug)]] 5 µM 0.313× (z -15.9) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.355× (z -14.2) |
| [[LoVo (line)]] | wt | 365 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.288× (z -22.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.313× (z -21.1) |
| [[HEC-1-A (line)]] | alt | 231 | 0 | 6 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.399× (z -17.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.448× (z -15.4) |
| [[NCI-H23 (line)]] | alt | 163 | 1 (1 ⚠) | 5 (5 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 2.84× (z +8.7) ⚠ cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -24.0) ⚠ cell-cycle shift, explains ~28% of this change |
| [[RKO (line)]] | wt | 71.7 | 0 | 6 (6 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.147× (z -18.3) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 181 | 0 | 6 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.340× (z -22.5) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.356× (z -21.5) |
| [[NCI-H2030 (line)]] | alt | 163 | 2 (1 ⚠) | 3 (3 ⚠) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.62× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -13.2) ⚠ cell-cycle shift, explains ~71% of this change |
| [[SHP-77 (line)]] | alt | 257 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -15.4) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.350× (z -10.1) |
| [[BT-474 (line)]] | alt | 311 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -14.8) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.443× (z -9.4) |
| [[COLO 205 (line)]] | alt | 927 | 1 (1 ⚠) | 3 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 1.76× (z +9.0) ⚠ cell-cycle shift, explains ~41% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.303× (z -20.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.395× (z -15.6) |
| [[Panc 03.27 (line)]] | alt | 180 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.394× (z -15.1) |
| [[SW1417 (line)]] | alt | 224 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.399× (z -16.9) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.421× (z -15.9) |
| [[KATO III (line)]] | alt | 259 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.344× (z -19.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.436× (z -15.1) |
| [[LS 180 (line)]] | wt | 308 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.369× (z -18.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.413× (z -16.3) |
| [[CFPAC-1 (line)]] | alt | 106 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.567× (z -12.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.309× (z -9.3) |
| [[SW48 (line)]] | wt | 221 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.411× (z -10.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 78.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +13.6) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[AsPC-1 (line)]] | alt | 103 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +9.3) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[PANC-1 (line)]] | alt | 48.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.465× (z -10.1) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A-172 (line)]] | wt | 22.9 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 29.3 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 29.8 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 19.3 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 24.8 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 24.9 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 22.5 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 194 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.6 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 23.3 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 12.7 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 22.1 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 32.2 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 15.3 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 21.3 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 17.0 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 21.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 207 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 200 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.5 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 17.5 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.8 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 16.3 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 24.2 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 50.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5719), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DSC2]] | +0.61 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[MYO5B]] | +0.54 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[PATJ]] | +0.53 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[ALOX12P2-1]] | +0.53 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[DAPP1]] | +0.52 | +0.43 / +0.44 | both halves | 3e-05 |  |
| [[SH3D19]] | +0.49 | +0.33 / +0.52 | both halves | 1e-04 |  |
| [[EID3]] | +0.48 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[LRP1B]] | +0.48 | +0.42 / +0.42 | both halves | 4e-05 |  |
| [[RSPO3]] | +0.47 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[SLMAP]] | +0.47 | +0.48 / +0.39 | both halves | 6e-05 |  |
| [[LINC02864]] | +0.47 | +0.50 / +0.41 | both halves | 4e-05 |  |
| [[RAB22A]] | +0.46 | +0.46 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM39B]] | -0.51 | -0.47 / -0.39 | both halves | 5e-05 |  |
| [[LOX]] | -0.45 | -0.43 / -0.37 | both halves | 8e-05 |  |
| [[ZHX3]] | -0.43 | -0.32 / -0.48 | both halves | 2e-04 |  |
| [[TNS2]] | -0.42 | -0.39 / -0.37 | both halves | 7e-05 |  |
| [[ZNF850]] | -0.42 | -0.38 / -0.42 | both halves | 7e-05 |  |
| [[SEC14L2]] | -0.42 | -0.32 / -0.38 | both halves | 1e-04 |  |
| [[IKBIP]] | -0.41 | -0.42 / -0.27 | both halves | 3e-04 |  |
| [[TLR2]] | -0.40 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[CCDC7]] | -0.40 | -0.30 / -0.43 | both halves | 2e-04 |  |
| [[C8orf58]] | -0.40 | -0.35 / -0.31 | both halves | 2e-04 |  |
| [[COL6A3]] | -0.39 | -0.35 / -0.29 | both halves | 2e-04 |  |
| [[SLC2A10]] | -0.39 | -0.39 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 6, C 14. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[XYLT1]] | B | XYLT1 activity raises MAP7's level | lines that do not express XYLT1 (25) vs lines expressing it (25) | 1.97× lower at baseline in the lines without XYLT1 | 0.050 | ⚠ within organs, on part of the lines; also absent: LINC02055, CADPS, MGC32805 |
| [[ARAP2]] | B | ARAP2 activity raises MAP7's level | lines that do not express ARAP2 (10) vs lines expressing it (40) | 3.48× lower at baseline in the lines without ARAP2 | 0.057 | ⚠ within organs, on part of the lines; also absent: RAPGEF5 |
| [[PSMB5]] | B | PSMB5 activity lowers MAP7's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[RASEF]] | B | RASEF activity raises MAP7's level | lines that do not express RASEF (20) vs lines expressing it (30) | 2.42× lower at baseline in the lines without RASEF | 0.074 | ⚠ within organs, on part of the lines; also absent: LIPH, ENSG00000263325, DENND2D |
| [[VAV3]] | B | VAV3 activity raises MAP7's level | lines that do not express VAV3 (30) vs lines expressing it (20) | 1.28× lower at baseline in the lines without VAV3 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RSPO3, ENSG00000289418, NRCAM |
| [[ALOX12P2-1]] | B | ALOX12P2-1 activity raises MAP7's level | lines that do not express ALOX12P2-1 (29) vs lines expressing it (21) | 1.55× lower at baseline in the lines without ALOX12P2-1 | 0.091 | ⚠ within organs, on part of the lines; also absent: NID2, MEG8, UNC5D; maybe low, not absent |
| [[MYO5B]] | C | MYO5B activity raises MAP7's level | lines that do not express MYO5B (26) vs lines expressing it (24) | 5.14× lower at baseline in the lines without MYO5B | 0.001 | ⚠ within organs, on part of the lines; also absent: CRB3, KDF1, MARVELD3; co-absent with the target |
| [[CYP4F11]] | C | CYP4F11 activity raises MAP7's level | lines that do not express CYP4F11 (29) vs lines expressing it (21) | 3.34× lower at baseline in the lines without CYP4F11 | 0.003 | ⚠ within organs, on part of the lines; also absent: LINC01564, ENSG00000279806, TNS4; co-absent with the target |
| [[FAM83B]] | C | FAM83B activity raises MAP7's level | lines that do not express FAM83B (30) vs lines expressing it (20) | 4.54× lower at baseline in the lines without FAM83B | 0.004 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14; co-absent with the target |
| [[C1orf116]] | C | C1orf116 activity raises MAP7's level | lines that do not express C1orf116 (31) vs lines expressing it (19) | 5.18× lower at baseline in the lines without C1orf116 | 0.006 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125; co-absent with the target |
| [[MACC1]] | C | MACC1 activity raises MAP7's level | lines that do not express MACC1 (32) vs lines expressing it (18) | 7.11× lower at baseline in the lines without MACC1 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, ENSG00000243004, GRHL2; co-absent with the target |
| [[LIPH]] | C | LIPH activity raises MAP7's level | lines that do not express LIPH (27) vs lines expressing it (23) | 5.40× lower at baseline in the lines without LIPH | 0.008 | ⚠ within organs, on part of the lines; also absent: CATSPERB, TC2N, SDR16C5; co-absent with the target |

### Downstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 10, C 12. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PATJ]] | B | MAP7 activity raises PATJ's level | lines that do not express MAP7 (21) vs lines expressing it (29) | 3.52× lower at baseline in the lines without MAP7 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: MST1R, ENTPD2, TC2N |
| [[TNFRSF21]] | B | MAP7 activity raises TNFRSF21's level | lines that do not express MAP7 (21) vs lines expressing it (29) | 3.07× lower at baseline in the lines without MAP7 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: MST1R, ENTPD2, TC2N |
| [[ARAP2]] | B | MAP7 activity raises ARAP2's level | lines that do not express MAP7 (21) vs lines expressing it (29) | 3.53× lower at baseline in the lines without MAP7 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: MST1R, ENTPD2, TC2N |
| [[RASEF]] | B | MAP7 activity raises RASEF's level | lines that do not express MAP7 (21) vs lines expressing it (29) | 3.16× lower at baseline in the lines without MAP7 | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: MST1R, ENTPD2, TC2N |
| [[TMEM39B]] | B | MAP7 activity lowers TMEM39B's level | lines that do not express MAP7 (21) vs lines expressing it (29) | 1.48× higher at baseline in the lines without MAP7 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: MST1R, ENTPD2, TC2N |
| [[RASSF4]] | B | MAP7 activity lowers RASSF4's level | lines that do not express MAP7 (21) vs lines expressing it (29) | 2.12× higher at baseline in the lines without MAP7 | 0.076 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: MST1R, ENTPD2, TC2N |
| [[MYO6]] | B | MAP7 activity raises MYO6's level | lines that do not express MAP7 (21) vs lines expressing it (29) | 1.89× lower at baseline in the lines without MAP7 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: MST1R, ENTPD2, TC2N |
| [[LIX1L]] | B | MAP7 activity lowers LIX1L's level | lines that do not express MAP7 (21) vs lines expressing it (29) | 2.65× higher at baseline in the lines without MAP7 | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: MST1R, ENTPD2, TC2N |
| [[MFSD6]] | B | MAP7 activity raises MFSD6's level | lines that do not express MAP7 (21) vs lines expressing it (29) | 2.10× lower at baseline in the lines without MAP7 | 0.088 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: MST1R, ENTPD2, TC2N |
| [[PTPRK]] | B | MAP7 activity raises PTPRK's level | lines that do not express MAP7 (21) vs lines expressing it (29) | 1.66× lower at baseline in the lines without MAP7 | 0.096 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: MST1R, ENTPD2, TC2N |
| [[LIPH]] | C | MAP7 activity raises LIPH's level | lines that do not express MAP7 (21) vs lines expressing it (29) | 6.26× lower at baseline in the lines without MAP7 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: MST1R, ENTPD2, TC2N; co-absent with the target |
| [[MYO5B]] | C | MAP7 activity raises MYO5B's level | lines that do not express MAP7 (21) vs lines expressing it (29) | 5.58× lower at baseline in the lines without MAP7 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: MST1R, ENTPD2, TC2N; co-absent with the target |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.285). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.9, 57.9); signed map (54.1, 7.4). **Vector** length 102, 27.2% of its response variance represented; |z| ≥ 3 in 959 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.6 | +17.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.0 | +8.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.2 | +6.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +6.2 | +8.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.3 | +7.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.8 | +3.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +5.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +0.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.3 | +2.2 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -3.6 | -6.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.6 | -6.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.5 | -5.8 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -1.7 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.2 | -8.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.2 | -5.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.1 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | microtubule associated protein 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q23.3 — chr6:136,342,281-136,550,819 (-) |
| Ensembl biotype | protein_coding |
| Also known as | E-MAP-115 |
| Gene groups (HGNC) | Microtubule associated protein 7 family |
| Hallmark sets | SPERMATOGENESIS, ANDROGEN_RESPONSE, KRAS_SIGNALING_UP |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14244](https://www.uniprot.org/uniprotkb/Q14244) (Ensconsin):

> Microtubule-stabilizing protein that may play an important role during reorganization of microtubules during polarization and differentiation of epithelial cells. Associates with microtubules in a dynamic manner. May play a role in the formation of intercellular contacts. Colocalization with TRPV4 results in the redistribution of TRPV4 toward the membrane and may link cytoskeletal microfilaments.

**Summary**, from NCBI Gene [9053](https://www.ncbi.nlm.nih.gov/gene/9053):

> The product of this gene is a microtubule-associated protein that is predominantly expressed in cells of epithelial origin. Microtubule-associated proteins are thought to be involved in microtubule dynamics, which is essential for cell polarization and differentiation. This protein has been shown to be able to stabilize microtubules, and may serve to modulate microtubule functions. Studies of the related mouse protein also suggested an essential role in microtubule function required for …

**Accessions** — [HGNC:6869](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6869) · Entrez [9053](https://www.ncbi.nlm.nih.gov/gene/9053) · UniProt [Q14244](https://www.uniprot.org/uniprotkb/Q14244) · Ensembl [ENSG00000135525](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135525)

## Data

Gene col 5719: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5719); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5719, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5719]; `tensor/DDL_lfc|DDL_z.npy` [5719]; `embed/gene_vectors.npy` [5719]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5719 or target_col == 5719). Every well: [[MAP7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAP7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
