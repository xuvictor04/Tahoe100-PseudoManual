---
symbol: "PLEKHH2"
type: "gene"
col: 7640
ensembl_id: "ENSG00000152527"
name: "pleckstrin homology, MyTH4 and FERM domain containing H2"
location: "2p21"
module: 1
arm: "-"
pooled_cpm: 34.19
n_lines_expressing: 36
n_dd_up: 18
n_dd_down: 38
n_dd_up_clean: 11
n_dd_down_clean: 28
in_vector_space: true
direction_upstream: 1
direction_downstream: 5
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# PLEKHH2

*pleckstrin homology, MyTH4 and FERM domain containing H2* — 2p21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 4.34× (z +29.5, q 0e+00, up in 34 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 38 drug-doses (10 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.475× (z -14.9, q 0e+00, down in 25 of 34 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TOX2]] (+0.58, fdr 1e-05), [[F11R]] (+0.58, fdr 4e-05), [[RAB11FIP1]] (+0.56, fdr 5e-05); moves opposite to [[MAPKAPK5]] (-0.55, fdr 9e-05), [[RGS5]] (-0.54, fdr 5e-05), [[ZNF507]] (-0.53, fdr 1e-04).
> It sits in the **-** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TSPAN33]] → it (grade B ⚠); 5 go from it, the strongest it → [[GAMT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7640.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **4.34×** | +29.5 | 0e+00 | 34/34 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **4.33×** | +29.5 | 0e+00 | 33/34 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.67×** | +28.0 | 0e+00 | 33/34 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **3.48×** | +25.1 | 0e+00 | 34/34 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.92×** | +21.6 | 0e+00 | 33/34 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.85×** | +21.1 | 0e+00 | 34/34 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Brivudine (drug)]] 5 µM |  | **3.47×** | +13.1 | 3e-37 | 30/34 (SW480, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.89×** | +12.8 | 8e-36 | 28/34 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.48×** | +8.0 | 1e-13 | 16/34 (SW480, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.30×** | +7.5 | 4e-12 | 12/33 (HOP62, SW480, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.03×** | +7.4 | 5e-12 | 13/29 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); noisy plate (z scaled) |
| [[Brivudine (drug)]] 0.5 µM |  | **1.48×** | +5.6 | 9e-07 | 11/34 (SW480, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **1.21×** | +5.5 | 2e-06 | 12/34 (J82, NCI-H23, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.33×** | +5.4 | 3e-06 | 14/34 (LoVo, HOP62, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.27×** | +4.9 | 4e-05 | 13/34 (LoVo, HOP62, …) | top dose only |  |
| [[Tofacitinib (drug)]] 5 µM |  | 1.15× | +4.1 | 0.001 | 8/34 (PANC-1, SW 900, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.19× | +3.6 | 0.009 | 12/34 (HS-578T, J82, …) | rises with dose |  |
| [[Cytarabine (drug)]] 0.05 µM |  | **1.21×** | +3.6 | 0.010 | 5/34 (A-427, NCI-H460, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.19× | +3.5 | 0.014 | 8/34 (J82, hTERT-HPNE, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.18× | +3.4 | 0.019 | 9/34 (LoVo, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 38 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7640.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.475×** | -14.9 | 0e+00 | 25/34 (NCI-H1792, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.501×** | -13.8 | 6e-41 | 23/33 (NCI-H1792, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.503×** | -13.8 | 9e-41 | 30/34 (NCI-H1792, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.505×** | -13.6 | 3e-40 | 24/34 (NCI-H1792, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.523×** | -13.0 | 2e-36 | 24/34 (NCI-H1792, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.527×** | -12.8 | 1e-35 | 24/34 (A498, PANC-1, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.572×** | -11.1 | 6e-27 | 24/34 (NCI-H1792, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.348×** | -11.1 | 1e-26 | 30/33 (Panc 03.27, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.615×** | -9.7 | 2e-20 | 21/34 (NCI-H1792, SK-MEL-2, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **0.713×** | -9.5 | 9e-20 | 21/34 (NCI-H1792, HEC-1-A, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.404×** | -9.5 | 1e-19 | 23/34 (NCI-H1792, HT-29, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.630×** | -9.2 | 1e-18 | 19/34 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.630×** | -8.9 | 4e-17 | 22/34 (NCI-H1792, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.648×** | -8.6 | 2e-16 | 17/33 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[EX229 (drug)]] 5 µM |  | **0.481×** | -7.7 | 7e-13 | 20/33 (NCI-H1792, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.773×** | -7.2 | 2e-11 | 20/34 (A-172, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.706×** | -6.9 | 1e-10 | 19/34 (H4, HT-29, …) | all doses, stronger at high dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.533×** | -6.6 | 1e-09 | 16/33 (NCI-H1792, A498, …) | top dose only | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **0.641×** | -6.3 | 6e-09 | 18/32 (HT-29, SW 900, …) | all doses, stronger at high dose | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7640. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 107 | 0 | 18 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -26.6) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.135× (z -20.0) |
| [[SW480 (line)]] | alt | 28.2 | 9 (1 ⚠) | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 4.57× (z +21.6) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.338× (z -10.8) |
| [[HEC-1-A (line)]] | alt | 30.7 | 3 | 6 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.84× (z +12.7) | [[Homoharringtonine (drug)]] 0.5 µM 0.174× (z -14.9) |
| [[HT-29 (line)]] | alt | 156 | 0 | 9 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.335× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.389× (z -10.6) |
| [[NCI-H23 (line)]] | alt | 28.3 | 5 | 4 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 8.69× (z +13.4) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0634× (z -16.3) ⚠ toxic; cell-cycle shift, explains ~21% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.126× (z -12.7) |
| [[A498 (line)]] | wt | 42.5 | 5 | 3 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 5.51× (z +12.7) | [[Homoharringtonine (drug)]] 0.5 µM 0.230× (z -11.0) |
| [[LoVo (line)]] | wt | 92.6 | 4 (1 ⚠) | 4 (3 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.97× (z +11.0) | [[Dinaciclib (drug)]] 0.05 µM 0.224× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.384× (z -9.7) |
| [[PANC-1 (line)]] | alt | 62.2 | 2 | 6 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.14× (z +9.0) | [[Homoharringtonine (drug)]] 0.5 µM 0.267× (z -10.4) |
| [[SK-MEL-2 (line)]] | alt | 82.4 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.143× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.268× (z -11.6) |
| [[A-427 (line)]] | wt | 37.3 | 4 | 3 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.90× (z +12.7) | [[Dinaciclib (drug)]] 0.5 µM 0.132× (z -17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~8% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.336× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 49.1 | 4 | 3 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.54× (z +12.2) | [[Homoharringtonine (drug)]] 0.5 µM 0.248× (z -12.9) |
| [[HOP62 (line)]] | alt | 13.0 | 7 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 7.63× (z +12.8) | — |
| [[Panc 03.27 (line)]] | alt | 81.3 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.153× (z -19.0) |
| [[HepG2_C3A (line)]] | wt | 42.1 | 6 | 0 | [[Panobinostat (drug)]] 0.5 µM 10.1× (z +12.6) | — |
| [[NCI-H460 (line)]] | wt | 11.3 | 6 | 0 | [[Tucidinostat (drug)]] 5 µM 6.78× (z +16.8) | — |
| [[A549 (line)]] | wt | 13.5 | 5 | 0 | [[Panobinostat (drug)]] 0.5 µM 10.0× (z +11.8) | — |
| [[Hs 766T (line)]] | wt | 49.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -10.9) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.333× (z -9.1) |
| [[hTERT-HPNE (line)]] | wt | 20.9 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 5.51× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.154× (z -8.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 12.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 9.89× (z +10.9) | — |
| [[RPMI-7951 (line)]] | alt | 22.0 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.22× (z +8.9) | — |
| [[C32 (line)]] | wt | 65.2 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.25× (z +9.3) | — |
| [[H4 (line)]] | wt | 19.2 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 7.05× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -9.7) ⚠ cell-cycle shift, explains ~78% of this change |
| [[J82 (line)]] | alt | 16.3 | 2 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 3.13× (z +10.2) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 3.99× (z +8.7) | — |
| [[LOX-IMVI (line)]] | wt | 9.43 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 4.06× (z +9.3) | — |
| [[SHP-77 (line)]] | alt | 134 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.325× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[SW 900 (line)]] | alt | 105 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.396× (z -8.6) ⚠ transcription drop; cell-cycle shift, explains ~50% of this change |
| [[A-172 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.52 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.71 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.35 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.91 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.58 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.67 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 7.17 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 6.04 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.91 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.90 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.22 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 6.95 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.00 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.37 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7640), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TOX2]] | +0.58 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[F11R]] | +0.58 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[RAB11FIP1]] | +0.56 | +0.40 / +0.53 | both halves | 5e-05 |  |
| [[BEX4]] | +0.53 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[RADX]] | +0.53 | +0.30 / +0.54 | both halves | 2e-04 |  |
| [[ABHD3]] | +0.53 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[FBXO33]] | +0.53 | +0.37 / +0.47 | both halves | 9e-05 |  |
| [[RTN3]] | +0.52 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[ASAP3]] | +0.52 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[TMEM41B]] | +0.52 | +0.44 / +0.41 | both halves | 4e-05 |  |
| [[SLC22A17]] | +0.51 | +0.42 / +0.49 | both halves | 4e-05 |  |
| [[WASF2]] | +0.51 | +0.46 / +0.19 | ⚠ not reproduced | 9e-04 |  |
| [[CACNG7]] | +0.51 | +0.41 / +0.45 | both halves | 4e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPKAPK5]] | -0.55 | -0.37 / -0.54 | both halves | 9e-05 |  |
| [[RGS5]] | -0.54 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[ZNF507]] | -0.53 | -0.36 / -0.45 | both halves | 1e-04 |  |
| [[ZMYND11]] | -0.53 | -0.39 / -0.48 | both halves | 5e-05 |  |
| [[UTP15]] | -0.53 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[DNAJC11]] | -0.52 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[ST7L]] | -0.52 | -0.34 / -0.40 | both halves | 1e-04 |  |
| [[ITPA]] | -0.51 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[DPH5-DT]] | -0.51 | -0.36 / -0.34 | both halves | 1e-04 |  |
| [[NSD1]] | -0.50 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[SCO1]] | -0.50 | -0.45 / -0.39 | both halves | 6e-05 |  |
| [[ZC3H7B]] | -0.50 | -0.38 / -0.42 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TSPAN33]] | B | TSPAN33 activity raises PLEKHH2's level | lines that do not express TSPAN33 (12) vs lines expressing it (38) | 1.67× lower at baseline in the lines without TSPAN33 | 0.085 | ⚠ within organs, on part of the lines; also absent: SRCIN1, CRACD, GNAZ; maybe low, not absent |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GAMT]] | B | PLEKHH2 activity raises GAMT's level | lines that do not express PLEKHH2 (14) vs lines expressing it (36) | 1.64× lower at baseline in the lines without PLEKHH2 | 0.018 | ⚠ within organs, on part of the lines; also absent: PDLIM3, ENSG00000259363, AKT3 |
| [[WARS2-AS1]] | B | PLEKHH2 activity raises WARS2-AS1's level | lines that do not express PLEKHH2 (14) vs lines expressing it (36) | 1.35× lower at baseline in the lines without PLEKHH2 | 0.030 | ⚠ within organs, on part of the lines; also absent: PDLIM3, ENSG00000259363, AKT3 |
| [[MBOAT2]] | B | PLEKHH2 activity lowers MBOAT2's level | lines that do not express PLEKHH2 (14) vs lines expressing it (36) | 1.62× higher at baseline in the lines without PLEKHH2 | 0.036 | ⚠ within organs, on part of the lines; also absent: PDLIM3, ENSG00000259363, AKT3 |
| [[LMTK2]] | B | PLEKHH2 activity lowers LMTK2's level | lines that do not express PLEKHH2 (14) vs lines expressing it (36) | 1.74× higher at baseline in the lines without PLEKHH2 | 0.042 | ⚠ within organs, on part of the lines; also absent: PDLIM3, ENSG00000259363, AKT3 |
| [[DPH5-DT]] | B | PLEKHH2 activity raises DPH5-DT's level | lines that do not express PLEKHH2 (14) vs lines expressing it (36) | 1.19× lower at baseline in the lines without PLEKHH2 | 0.075 | ⚠ within organs, on part of the lines; also absent: PDLIM3, ENSG00000259363, AKT3 |

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **-** arm (projection on the module's main direction -0.477). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (10.8, -0.2); signed map (-25.4, 19.6). **Vector** length 98.4, 24.4% of its response variance represented; |z| ≥ 3 in 1,333 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.5 | +28.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +9.3 | +21.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.8 | +21.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | +4.4 | +4.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +4.0 | +8.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.8 | -0.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.2 | +13.1 |
|  | [[Retinoic acid (drug)]] 5 µM |  | +2.5 | +2.4 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.7 | -13.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.0 | -12.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.9 | -13.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.2 | -9.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | -3.1 | -9.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.9 | -1.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.8 | -11.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.8 | -6.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.7 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | pleckstrin homology, MyTH4 and FERM domain containing H2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p21 — chr2:43,637,260-43,767,987 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA2028, PLEKHH1L |
| Gene groups (HGNC) | Pleckstrin homology domain containing; FERM domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IVE3](https://www.uniprot.org/uniprotkb/Q8IVE3) (Pleckstrin homology domain-containing family H member 2):

> In the kidney glomerulus may play a role in linking podocyte foot processes to the glomerular basement membrane. May be involved in stabilization of F-actin by attenuating its depolymerization. Can recruit TGFB1I1 from focal adhesions to podocyte lamellipodia.

**Summary**, from NCBI Gene [130271](https://www.ncbi.nlm.nih.gov/gene/130271):

> Predicted to enable actin binding activity. Predicted to be involved in negative regulation of actin filament depolymerization. Located in cytoplasm; lamellipodium; and plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30506](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30506) · Entrez [130271](https://www.ncbi.nlm.nih.gov/gene/130271) · UniProt [Q8IVE3](https://www.uniprot.org/uniprotkb/Q8IVE3) · Ensembl [ENSG00000152527](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152527)

## Data

Gene col 7640: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7640); `tables/drug_effects.parquet` (71 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7640, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7640]; `tensor/DDL_lfc|DDL_z.npy` [7640]; `embed/gene_vectors.npy` [7640]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7640 or target_col == 7640). Every well: [[PLEKHH2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLEKHH2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
