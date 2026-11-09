---
symbol: "STAU1"
type: "gene"
col: 4501
ensembl_id: "ENSG00000124214"
name: "staufen double-stranded RNA binding protein 1"
location: "20q13.13"
module: 85
arm: "+"
pooled_cpm: 264.31
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 7
n_dd_up_clean: 5
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/085"]
generated_by: "tahoemap"
---

# STAU1

*staufen double-stranded RNA binding protein 1* — 20q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.36× (z +9.6, q 7e-19, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.698× (z -10.9, q 7e-25, down in 41 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 0.822× (z -6.2, q 9e-08, down in 26 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADAM10]] (+0.60, fdr 1e-05), [[RALY]] (+0.58, fdr 3e-05), [[TSEN34]] (+0.56, fdr 3e-05); moves opposite to [[MYLK-AS1]] (-0.57, fdr 6e-05), [[TYW3]] (-0.54, fdr 4e-05), [[STPG1]] (-0.52, fdr 3e-05).
> It sits in the **+** arm of [[Module 085]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4501.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.36×** | +9.6 | 7e-19 | 34/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.34×** | +9.2 | 1e-17 | 36/48 (SW480, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.23×** | +9.0 | 3e-17 | 27/48 (NCI-H460, SK-MEL-2, …) | top dose only | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.32×** | +8.7 | 7e-16 | 37/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.28×** | +7.8 | 1e-12 | 31/48 (SNU-423, NCI-H460, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.56×** | +7.3 | 3e-11 | 32/49 (SW480, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.38×** | +5.3 | 1e-05 | 28/48 (SW480, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 1.18× | +5.2 | 2e-05 | 21/48 (J82, NCI-H1792, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | 1.17× | +4.8 | 1e-04 | 22/47 (LoVo, PANC-1, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 1.16× | +4.6 | 2e-04 | 19/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | 1.16× | +4.5 | 3e-04 | 20/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 1.15× | +4.4 | 5e-04 | 5/49 (A-172, NCI-H1573, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 1.14× | +4.1 | 0.002 | 16/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.28×** | +4.0 | 0.003 | 23/48 (J82, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | 1.13× | +3.9 | 0.004 | 13/48 (SNU-423, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | 1.13× | +3.5 | 0.016 | 4/48 (HT-29, KATO III, …) | inconsistent across doses |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 1.08× | +3.5 | 0.016 | 1/49 (CHP-212) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4501.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.698×** | -10.9 | 7e-25 | 41/47 (RKO, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.827×** | -8.5 | 6e-15 | 24/48 (C32, NCI-H2347, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.790×** | -6.9 | 1e-09 | 28/45 (NCI-H2030, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.822×** | -6.2 | 9e-08 | 26/48 (NCI-H23, A-427, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.817×** | -5.9 | 5e-07 | 27/47 (hTERT-HPNE, A-427, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.858× | -4.8 | 1e-04 | 19/48 (A-427, A498, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.874× | -4.1 | 0.004 | 21/44 (A-427, NCI-H23, …) | inconsistent across doses | composition shift |
| [[Radotinib (drug)]] 5 µM |  | 0.913× | -4.1 | 0.004 | 5/48 (A-427, NCI-H23, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.787×** | -4.0 | 0.005 | 26/48 (HepG2/C3A, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.884× | -3.9 | 0.006 | 14/48 (NCI-H23, HT-29, …) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | 0.873× | -3.9 | 0.006 | 13/48 (AsPC-1, COLO 205, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.886× | -3.8 | 0.006 | 12/48 (C32, NCI-H2347, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.886× | -3.7 | 0.010 | 14/48 (SW 1271, NCI-H23, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.922× | -3.7 | 0.010 | 12/49 (BT-474, C32, …) | top dose only |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.899× | -3.4 | 0.027 | 4/48 (HOP62, COLO 205, …) | rises with dose |  |
| [[ULK-101 (drug)]] 0.5 µM |  | 0.861× | -3.4 | 0.027 | 9/49 (Hs 766T, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.823×** | -3.2 | 0.042 | 15/48 (COLO 205, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Menadione (drug)]] 0.05 µM |  | 0.900× | -3.1 | 0.058 | 3/48 (KATO III, SW 1088, …) | inconsistent across doses |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | 0.899× | -3.0 | 0.062 | 4/48 (CHP-212, AsPC-1, …) | inconsistent across doses | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | 0.922× | -2.9 | 0.099 | 5/48 (HOP62, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4501. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 283 | 7 (4 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.22× (z +17.5) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 2.48× (z +10.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.650× (z -9.0) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 184 | 7 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +17.6) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 1.95× (z +11.5) | — |
| [[AsPC-1 (line)]] | alt | 401 | 3 (3 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.63× (z +16.5) ⚠ cell-cycle shift, explains ~21% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.519× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 326 | 0 | 5 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.328× (z -15.4) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 243 | 2 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +16.0) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 1.63× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.533× (z -10.2) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 384 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.436× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 182 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.02× (z +15.5) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 2.10× (z +8.5) | — |
| [[SW1417 (line)]] | alt | 477 | 1 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.55× (z +8.8) ⚠ cell-cycle shift, explains ~21% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.592× (z -10.1) ⚠ toxic |
| [[BT-474 (line)]] | alt | 548 | 1 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.74× (z +9.6) ⚠ cell-cycle shift, explains ~21% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.528× (z -15.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 202 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.58× (z +11.8) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[KATO III (line)]] | alt | 304 | 1 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.65× (z +9.0) ⚠ cell-cycle shift, explains ~21% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.508× (z -11.8) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 309 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.468× (z -11.4) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 331 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.444× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 274 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.515× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 277 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.439× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 213 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 1.62× (z +8.6) | — |
| [[A549 (line)]] | wt | 199 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +12.5) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[CFPAC-1 (line)]] | alt | 286 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.56× (z +11.6) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[Hs 766T (line)]] | wt | 380 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.583× (z -8.8) ⚠ toxic |
| [[HT-29 (line)]] | alt | 345 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 2.29× (z +8.7) | — |
| [[hTERT-HPNE (line)]] | wt | 147 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.428× (z -10.1) |
| [[LOX-IMVI (line)]] | wt | 227 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 1.69× (z +9.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 230 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.51× (z +10.2) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H1573 (line)]] | alt | 214 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.621× (z -8.5) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 227 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +13.4) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[RKO (line)]] | wt | 331 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.280× (z -22.4) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 263 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.560× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 245 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 1.66× (z +9.0) ⚠ cell-cycle shift, explains ~15% of this change | — |
| [[A-172 (line)]] | wt | 192 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 184 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 278 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 182 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 164 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 205 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 191 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 573 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 177 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 490 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 188 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 201 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 257 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 298 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 252 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 274 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 226 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 220 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 233 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 256 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 178 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4501), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAM10]] | +0.60 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[RALY]] | +0.58 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[TSEN34]] | +0.56 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[FAM89B]] | +0.54 | +0.49 / +0.33 | both halves | 1e-04 |  |
| [[DNM2]] | +0.53 | +0.41 / +0.44 | both halves | 4e-05 |  |
| [[RALGAPA2]] | +0.52 | +0.42 / +0.32 | both halves | 2e-04 |  |
| [[PPP1R13B]] | +0.52 | +0.42 / +0.42 | both halves | 4e-05 | same gene group |
| [[FAM234A]] | +0.52 | +0.46 / +0.42 | both halves | 4e-05 |  |
| [[EML4]] | +0.51 | +0.48 / +0.34 | both halves | 1e-04 |  |
| [[DHTKD1]] | +0.51 | +0.40 / +0.28 | both halves | 3e-04 |  |
| [[ADIPOR2]] | +0.51 | +0.53 / +0.41 | both halves | 4e-05 |  |
| [[KHDRBS1]] | +0.51 | +0.50 / +0.33 | both halves | 1e-04 |  |

## Genes that move opposite

*47 of its nearest partners move opposite, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYLK-AS1]] | -0.57 | -0.45 / -0.38 | both halves | 6e-05 |  |
| [[TYW3]] | -0.54 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[STPG1]] | -0.52 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[AMMECR1]] | -0.51 | -0.42 / -0.36 | both halves | 9e-05 |  |
| [[FAM169A]] | -0.51 | -0.42 / -0.37 | both halves | 8e-05 |  |
| [[MTHFSD]] | -0.51 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[TSSK3]] | -0.51 | -0.36 / -0.39 | both halves | 1e-04 |  |
| [[MIX23]] | -0.50 | -0.39 / -0.42 | both halves | 5e-05 |  |
| [[FAIM]] | -0.50 | -0.42 / -0.22 | both halves | 6e-04 |  |
| [[PYGO1]] | -0.50 | -0.44 / -0.29 | both halves | 3e-04 |  |
| [[SMYD5]] | -0.49 | -0.34 / -0.42 | both halves | 1e-04 |  |
| [[KCNRG]] | -0.49 | -0.38 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers STAU1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 085]]; 52 genes; this gene is in the **+** arm (projection on the module's main direction 0.430). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (12.7, 0.9); signed map (-26.7, 30.5). **Vector** length 124, 37.8% of its response variance represented; |z| ≥ 3 in 1,198 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | +6.7 | +7.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +6.4 | +9.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.3 | +8.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | +4.1 | +5.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | +3.5 | +3.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.5 | +4.0 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.4 | +0.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | +1.9 |
|  | [[Arbutin (drug)]] 5 µM |  | +2.2 | +1.1 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +2.0 | +1.5 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -9.1 | -8.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -9.0 | -10.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.2 | -4.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -5.8 | +0.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.5 | -3.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.2 | -6.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.2 | -0.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -5.1 | -5.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.8 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | staufen double-stranded RNA binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.13 — chr20:49,113,339-49,188,367 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PPP1R150; previously STAU |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits |
| Hallmark sets | MITOTIC_SPINDLE |
| Matched by | ensembl_id |

**Function**, from UniProt [O95793](https://www.uniprot.org/uniprotkb/O95793) (Double-stranded RNA-binding protein Staufen homolog 1):

> Binds double-stranded RNA (regardless of the sequence) and tubulin. May play a role in specific positioning of mRNAs at given sites in the cell by cross-linking cytoskeletal and RNA components, and in stimulating their translation at the site.; (Microbial infection) Plays a role in virus particles production of many viruses including of HIV-1, HERV-K, ebola virus and influenza virus. Acts by interacting with various viral proteins involved in particle budding process.

**Summary**, from NCBI Gene [6780](https://www.ncbi.nlm.nih.gov/gene/6780):

> Staufen is a member of the family of double-stranded RNA (dsRNA)-binding proteins involved in the transport and/or localization of mRNAs to different subcellular compartments and/or organelles. These proteins are characterized by the presence of multiple dsRNA-binding domains which are required to bind RNAs having double-stranded secondary structures. The human homologue of staufen encoded by STAU, in addition contains a microtubule- binding domain similar to that of microtubule-associated …

**Accessions** — [HGNC:11370](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11370) · Entrez [6780](https://www.ncbi.nlm.nih.gov/gene/6780) · UniProt [O95793](https://www.uniprot.org/uniprotkb/O95793) · Ensembl [ENSG00000124214](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124214)

## Data

Gene col 4501: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4501); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4501, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4501]; `tensor/DDL_lfc|DDL_z.npy` [4501]; `embed/gene_vectors.npy` [4501]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4501 or target_col == 4501). Every well: [[STAU1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STAU1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
