---
symbol: "GLUL"
type: "gene"
col: 5759
ensembl_id: "ENSG00000135821"
name: "glutamate-ammonia ligase"
location: "1q25.3"
module: 98
arm: "+"
pooled_cpm: 22.3
n_lines_expressing: 40
n_dd_up: 36
n_dd_down: 11
n_dd_up_clean: 27
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 6
direction_downstream: 4
tags: ["gene", "module/098"]
generated_by: "tahoemap"
---

# GLUL

*glutamate-ammonia ligase* — 1q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.97× (z +9.1, q 5e-17, up in 23 of 34 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.49× (z +7.5, q 9e-12, up in 25 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.449× (z -10.8, q 3e-24, down in 29 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.583× (z -7.3, q 1e-10, down in 25 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACSL1]] (+0.59, fdr 7e-06), [[TMEM43]] (+0.57, fdr 1e-05), [[TNS2]] (+0.55, fdr 1e-05); moves opposite to [[PPP1R14B]] (-0.61, fdr 1e-05), [[SIPA1L3]] (-0.50, fdr 3e-05), [[SEMA3A]] (-0.49, fdr 1e-05).
> It is in [[Module 098]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TLR2]] → it (grade B ⚠); 4 go from it, the strongest it → [[FRMD5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5759.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.97×** | +9.1 | 5e-17 | 23/34 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.87×** | +8.1 | 2e-13 | 16/26 (HepG2/C3A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.49×** | +7.5 | 9e-12 | 25/38 (Panc 03.27, J82, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.58×** | +6.2 | 1e-07 | 22/37 (NCI-H2347, HOP62, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +6.0 | 3e-07 | 22/36 (J82, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.62×** | +5.9 | 3e-07 | 20/36 (Hs 766T, HOP62, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.55×** | +5.9 | 3e-07 | 20/37 (Hs 766T, HOP62, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.35×** | +5.7 | 1e-06 | 22/38 (J82, SW480, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +5.6 | 1e-06 | 6/39 (HOP62, HepG2/C3A, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +5.4 | 3e-06 | 18/35 (CFPAC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.48×** | +5.2 | 8e-06 | 20/38 (Hs 766T, HOP62, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.48×** | +5.2 | 8e-06 | 18/37 (Hs 766T, HOP62, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.46×** | +5.1 | 2e-05 | 22/37 (HOP62, Hs 766T, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +4.7 | 1e-04 | 20/35 (SHP-77, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.43×** | +4.6 | 2e-04 | 17/37 (Hs 766T, HOP62, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.36×** | +4.1 | 0.002 | 19/37 (Hs 766T, HOP62, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.36×** | +4.1 | 0.002 | 17/37 (Hs 766T, HOP62, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | **1.35×** | +4.0 | 0.002 | 17/38 (Hs 766T, HOP62, …) | all doses, stronger at high dose |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +3.9 | 0.003 | 17/38 (Hs 766T, HOP62, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.34×** | +3.9 | 0.003 | 16/37 (Hs 766T, NCI-H1792, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5759.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.449×** | -10.8 | 3e-24 | 29/37 (NCI-H23, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.583×** | -7.3 | 1e-10 | 25/37 (SW 900, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.597×** | -6.9 | 7e-10 | 28/38 (SW 900, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.417×** | -6.1 | 1e-07 | 25/38 (RKO, SNU-423, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.654×** | -5.7 | 1e-06 | 22/37 (SW 900, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.665×** | -5.3 | 1e-05 | 22/37 (HepG2/C3A, SNU-423, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.740×** | -4.1 | 0.004 | 17/38 (SW 900, A-172, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.568×** | -4.0 | 0.005 | 18/36 (SW 900, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.776×** | -3.4 | 0.039 | 12/36 (SW 900, SNU-423, …) | all doses, stronger at high dose |  |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.781×** | -3.2 | 0.089 | 7/38 (LoVo, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.850× | -3.1 | 0.089 | 8/38 (HT-29, SW480, …) | top dose only | position effect removed |
| [[Erythromycin (drug)]] 5 µM |  | **0.795×** | -3.1 | 0.089 | 11/38 (SW 1088, SW48, …) | top dose only |  |
| [[Ferulic acid (drug)]] 5 µM |  | 0.792× | -3.0 | 0.11 | 7/36 (NCI-H2030, hTERT-HPNE, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5759. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 47.9 | 20 | 1 (1 ⚠) | [[Triamcinolone (drug)]] 5 µM 5.96× (z +15.1) | [[Digitoxin (drug)]] 5 µM 0.246× (z -8.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 22.0 | 17 | 0 | [[Clobetasol propionate (drug)]] 0.5 µM 11.0× (z +14.7) | — |
| [[NCI-H1792 (line)]] | alt | 28.3 | 14 (1 ⚠) | 1 | [[Clobetasol propionate (drug)]] 0.05 µM 6.80× (z +12.0) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.240× (z -9.0) |
| [[SW 900 (line)]] | alt | 207 | 0 | 14 (9 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.103× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.238× (z -12.1) |
| [[SNU-423 (line)]] | alt | 45.3 | 7 | 1 | [[Budesonide (drug)]] 0.5 µM 6.10× (z +10.6) | [[Verteporfin (drug)]] 5 µM 0.198× (z -9.2) |
| [[HepG2_C3A (line)]] | wt | 52.8 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.36× (z +9.6) ⚠ toxic; transcription drop | [[Verteporfin (drug)]] 5 µM 0.186× (z -11.1) |
| [[CHP-212 (line)]] | wt | 45.3 | 0 | 2 (2 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.0776× (z -11.1) ⚠ cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 22.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +10.4) | [[Digitoxin (drug)]] 5 µM 0.151× (z -12.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 8.19 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 8.48× (z +9.3) ⚠ toxic; transcription drop | [[Pemetrexed (drug)]] 5 µM 0.116× (z -9.1) |
| [[RKO (line)]] | wt | 31.8 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.141× (z -13.6) ⚠ cell-cycle shift, explains ~53% of this change |
| [[SK-MEL-2 (line)]] | alt | 58.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -17.4) ⚠ cell-cycle shift, explains ~95% of this change |
| [[A-427 (line)]] | wt | 30.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -14.8) ⚠ cell-cycle shift, explains ~95% of this change |
| [[CFPAC-1 (line)]] | alt | 35.8 | 1 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 3.90× (z +9.4) | — |
| [[HT-29 (line)]] | alt | 46.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.177× (z -11.6) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 20.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.62× (z +11.0) ⚠ cell-cycle shift, explains ~95% of this change | — |
| [[LoVo (line)]] | wt | 27.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.338× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 12.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0643× (z -14.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 28.5 | 1 | 0 | [[Selinexor (drug)]] 5 µM 2.48× (z +8.6) | — |
| [[SNU-1 (line)]] | wt | 12.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0946× (z -8.6) |
| [[SW480 (line)]] | alt | 21.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +8.9) | — |
| [[A-172 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.18 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.25 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.64 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.04 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 7.52 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.98 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.83 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.49 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 95.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5759), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACSL1]] | +0.59 | +0.60 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_FATTY_ACID_METABOLISM |
| [[TMEM43]] | +0.57 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[TNS2]] | +0.55 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[ATOH8]] | +0.55 | +0.52 / +0.46 | both halves | 2e-05 |  |
| [[KLF9]] | +0.54 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[RIPOR2]] | +0.54 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[MAOA]] | +0.54 | +0.55 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_FATTY_ACID_METABOLISM |
| [[VSTM2L]] | +0.53 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[MAFB]] | +0.53 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[FKBP5]] | +0.52 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[ZFAND5]] | +0.52 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[ADPRHL1]] | +0.52 | +0.51 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R14B]] | -0.61 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[SIPA1L3]] | -0.50 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[SEMA3A]] | -0.49 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[PPIP5K1]] | -0.48 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[CCDC85B]] | -0.47 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[TMEM158]] | -0.47 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[DRAP1]] | -0.47 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[PKIA]] | -0.47 | -0.44 / -0.37 | both halves | 8e-05 |  |
| [[UBA6]] | -0.47 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[ATP5F1E]] | -0.46 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[COX17]] | -0.46 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[ARL4C]] | -0.46 | -0.40 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TLR2]] | B | TLR2 activity raises GLUL's level | lines that do not express TLR2 (26) vs lines expressing it (24) | 2.23× lower at baseline in the lines without TLR2 | 0.019 | ⚠ within organs, on part of the lines; also absent: FYB1, DDIT4L, EDNRA |
| [[FRMD5]] | B | FRMD5 activity raises GLUL's level | lines that do not express FRMD5 (10) vs lines expressing it (40) | 3.65× lower at baseline in the lines without FRMD5 | 0.032 | ⚠ within organs, on part of the lines; also absent: ENSG00000291112; maybe low, not absent |
| [[GCNT1]] | B | GCNT1 activity raises GLUL's level | lines that do not express GCNT1 (5) vs lines expressing it (45) | 4.78× lower at baseline in the lines without GCNT1 | 0.034 | ⚠ within organs, on part of the lines; also absent: ANKH, MLLT3, TLE4; maybe low, not absent |
| [[DPF3]] | B | DPF3 activity raises GLUL's level | lines that do not express DPF3 (13) vs lines expressing it (37) | 2.82× lower at baseline in the lines without DPF3 | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000267175, RNF152, RORA; maybe low, not absent |
| [[DTNA]] | B | DTNA activity raises GLUL's level | lines that do not express DTNA (22) vs lines expressing it (28) | 1.89× lower at baseline in the lines without DTNA | 0.088 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, MMP16, ENSG00000253553 |
| [[NR3C1]] | B | NR3C1 activity raises GLUL's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 6.7% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FRMD5]] | B | GLUL activity raises FRMD5's level | lines that do not express GLUL (10) vs lines expressing it (40) | 2.51× lower at baseline in the lines without GLUL | 0.032 | ⚠ within organs, on part of the lines |
| [[PPIP5K1]] | B | GLUL activity raises PPIP5K1's level | lines that do not express GLUL (10) vs lines expressing it (40) | 1.39× lower at baseline in the lines without GLUL | 0.083 | ⚠ within organs, on part of the lines |
| [[DPF3]] | B | GLUL activity raises DPF3's level | lines that do not express GLUL (10) vs lines expressing it (40) | 2.03× lower at baseline in the lines without GLUL | 0.090 | ⚠ within organs, on part of the lines |
| [[TLR2]] | B | GLUL activity raises TLR2's level | lines that do not express GLUL (10) vs lines expressing it (40) | 2.50× lower at baseline in the lines without GLUL | 0.091 | ⚠ within organs, on part of the lines |

## Where it sits

- **Module**: [[Module 098]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.645). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (29.4, 16.7); signed map (18.8, 31.1). **Vector** length 108, 26.3% of its response variance represented; |z| ≥ 3 in 1,099 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.5 | +7.5 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | +4.4 | +5.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +4.4 | +5.2 |
|  | [[Budesonide (drug)]] 5 µM |  | +4.1 | +4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.0 | +6.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +4.0 | +4.1 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.1 | -10.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.1 | -5.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -2.9 | -4.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -1.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.3 | -1.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.0 | -1.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.0 | -1.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.9 | -1.9 |
|  | [[Brivudine (drug)]] 0.5 µM |  | -1.8 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | glutamate-ammonia ligase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q25.3 — chr1:182,378,098-182,392,206 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously GLNS |
| Gene groups (HGNC) | Ligases; Acyltransferases |
| Hallmark sets | FATTY_ACID_METABOLISM |
| Reactome | 6 pathways, smallest: Astrocytic Glutamate-Glutamine Uptake And Metabolism; Neurotransmitter uptake and metabolism In glial cells; Glutamate and glutamine metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P15104](https://www.uniprot.org/uniprotkb/P15104) (Glutamine synthetase):

> Glutamine synthetase that catalyzes the ATP-dependent conversion of glutamate and ammonia to glutamine. Its role depends on tissue localization: in the brain, it regulates the levels of toxic ammonia and converts neurotoxic glutamate to harmless glutamine, whereas in the liver, it is one of the enzymes responsible for the removal of ammonia (By similarity). Plays a key role in ammonium detoxification during erythropoiesis: the glutamine synthetase activity is required to remove ammonium …

**Summary**, from NCBI Gene [2752](https://www.ncbi.nlm.nih.gov/gene/2752):

> The protein encoded by this gene belongs to the glutamine synthetase family. It catalyzes the synthesis of glutamine from glutamate and ammonia in an ATP-dependent reaction. This protein plays a role in ammonia and glutamate detoxification, acid-base homeostasis, cell signaling, and cell proliferation. Glutamine is an abundant amino acid, and is important to the biosynthesis of several amino acids, pyrimidines, and purines. Mutations in this gene are associated with congenital glutamine …

**Accessions** — [HGNC:4341](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4341) · Entrez [2752](https://www.ncbi.nlm.nih.gov/gene/2752) · UniProt [P15104](https://www.uniprot.org/uniprotkb/P15104) · Ensembl [ENSG00000135821](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135821)

## Data

Gene col 5759: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5759); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5759, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5759]; `tensor/DDL_lfc|DDL_z.npy` [5759]; `embed/gene_vectors.npy` [5759]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5759 or target_col == 5759). Every well: [[GLUL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GLUL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
