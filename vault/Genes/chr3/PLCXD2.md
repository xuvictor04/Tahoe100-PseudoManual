---
symbol: "PLCXD2"
type: "gene"
col: 14253
ensembl_id: "ENSG00000240891"
name: "phosphatidylinositol specific phospholipase C X domain containing 2"
location: "3q13.2"
module: 184
arm: "+"
pooled_cpm: 14.06
n_lines_expressing: 43
n_dd_up: 35
n_dd_down: 14
n_dd_up_clean: 25
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 4
direction_downstream: 7
tags: ["gene", "module/184"]
generated_by: "tahoemap"
---

# PLCXD2

*phosphatidylinositol specific phospholipase C X domain containing 2* — 3q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (10 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 5.02× (z +20.8, q 0e+00, up in 38 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (none with an alert); the strongest is [[Phenylephrine (hydrochloride) (drug)]] 5 µM: 0.685× (z -4.9, q 3e-04, down in 18 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARHGAP29]] (+0.70, fdr 7e-06), [[RAB3B]] (+0.62, fdr 1e-05), [[PKIA]] (+0.58, fdr 2e-05); moves opposite to [[EFCAB2]] (-0.52, fdr 4e-05), [[ZRANB2-DT]] (-0.51, fdr 4e-05), [[FAM76B]] (-0.50, fdr 4e-05).
> It sits in the **+** arm of [[Module 184]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ZBED2]] → it (grade B ⚠); 7 go from it, the strongest it → [[OCIAD2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14253.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **5.02×** | +20.8 | 0e+00 | 38/41 (J82, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.35×** | +18.9 | 0e+00 | 39/41 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **4.29×** | +18.8 | 0e+00 | 37/41 (HS-578T, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.47×** | +16.0 | 0e+00 | 37/41 (A-172, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.70×** | +12.8 | 1e-35 | 34/37 (J82, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.90×** | +11.7 | 1e-29 | 31/41 (J82, BT-474, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.94×** | +8.5 | 1e-15 | 23/41 (COLO 205, HT-29, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.00×** | +8.4 | 2e-15 | 22/38 (COLO 205, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **3.41×** | +8.3 | 9e-15 | 28/39 (Panc 03.27, A-172, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.85×** | +7.9 | 1e-13 | 29/40 (J82, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.69×** | +6.8 | 7e-10 | 21/40 (COLO 205, HT-29, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.68×** | +6.7 | 9e-10 | 23/41 (A-172, A549, …) | two highest doses | cell-cycle shift (explains ~22% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.56×** | +5.7 | 4e-07 | 21/41 (NCI-H1573, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.55×** | +5.6 | 8e-07 | 19/41 (NCI-H1573, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.30×** | +5.6 | 8e-07 | 20/40 (A498, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **1.51×** | +5.1 | 1e-05 | 16/41 (NCI-H1573, J82, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.46×** | +4.9 | 3e-05 | 18/41 (SNU-423, HS-578T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 1 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14253.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.685×** | -4.9 | 3e-04 | 18/41 (Hs 766T, A-172, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.680×** | -4.8 | 3e-04 | 14/41 (AsPC-1, J82, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.771×** | -4.7 | 3e-04 | 20/39 (SW1417, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.693×** | -4.7 | 3e-04 | 13/41 (AsPC-1, H4, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 0.5 µM |  | **0.697×** | -4.7 | 4e-04 | 16/41 (AsPC-1, Hs 766T, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.697×** | -4.3 | 0.002 | 13/38 (AsPC-1, NCI-H460, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.735×** | -4.0 | 0.006 | 13/41 (AsPC-1, Hs 766T, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.743×** | -3.8 | 0.009 | 15/41 (AsPC-1, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.917× | -3.7 | 0.012 | 6/41 (NCI-H2030, NCI-H23, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.771×** | -3.4 | 0.045 | 13/40 (AsPC-1, HS-578T, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.834× | -3.3 | 0.047 | 10/41 (AsPC-1, SW 900, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.781×** | -3.2 | 0.068 | 13/41 (NCI-H1573, Hs 766T, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.779×** | -3.1 | 0.075 | 15/37 (SW1417, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.787×** | -3.1 | 0.075 | 9/35 (NCI-H1573, Panc 03.27, …) | inconsistent across doses |  |
| [[Omeprazole (drug)]] 0.05 µM |  | **0.787×** | -3.1 | 0.075 | 5/41 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | **0.788×** | -3.1 | 0.075 | 9/40 (H4, KATO III, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14253. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 45.9 | 0 | 7 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.103× (z -17.2) |
| [[A-172 (line)]] | wt | 9.01 | 5 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 17.1× (z +10.6) | — |
| [[J82 (line)]] | alt | 25.4 | 5 | 0 | [[Belinostat (drug)]] 5 µM 5.77× (z +10.7) | — |
| [[HS-578T (line)]] | alt | 6.35 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 17.6× (z +10.1) | — |
| [[A498 (line)]] | wt | 5.37 | 3 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 9.45× (z +9.4) | — |
| [[CFPAC-1 (line)]] | alt | 7.08 | 3 | 0 | [[Belinostat (drug)]] 5 µM 8.00× (z +8.9) | — |
| [[COLO 205 (line)]] | alt | 8.73 | 2 | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 12.1× (z +8.7) | [[Dimethyl fumarate (drug)]] 0.05 µM 0.0704× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 4.96 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 8.64× (z +9.6) | — |
| [[NCI-H460 (line)]] | wt | 16.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0992× (z -11.3) |
| [[PANC-1 (line)]] | alt | 4.85 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 10.3× (z +10.6) | — |
| [[SNU-423 (line)]] | alt | 6.29 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 14.7× (z +9.3) | — |
| [[HepG2_C3A (line)]] | wt | 22.5 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.144× (z -12.1) |
| [[SW480 (line)]] | alt | 14.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.381× (z -9.7) |
| [[A-427 (line)]] | wt | 63.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0738× (z -17.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 6.89 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.90× (z +9.9) | — |
| [[HEC-1-A (line)]] | alt | 8.84 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.163× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 18.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.243× (z -10.2) |
| [[LOX-IMVI (line)]] | wt | 18.6 | 1 | 0 | [[Belinostat (drug)]] 5 µM 5.64× (z +8.5) | — |
| [[LS 180 (line)]] | wt | 37.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.164× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[Panc 03.27 (line)]] | alt | 18.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.157× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[RKO (line)]] | wt | 7.64 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.0914× (z -9.0) |
| [[SHP-77 (line)]] | alt | 6.81 | 0 | 1 | — | [[Thymol (drug)]] 0.05 µM 0.0965× (z -8.5) |
| [[SW1417 (line)]] | alt | 43.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.177× (z -17.5) |
| [[A549 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.42 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.77 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.01 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.46 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.59 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.29 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.71 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.31 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.55 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14253), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGAP29]] | +0.70 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[RAB3B]] | +0.62 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[PKIA]] | +0.58 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[ANOS1]] | +0.58 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[AMOTL1]] | +0.57 | +0.64 / +0.46 | both halves | 3e-05 |  |
| [[CPA4]] | +0.57 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[F2RL2]] | +0.56 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[WNT7A]] | +0.55 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[CMIP]] | +0.54 | +0.48 / +0.43 | both halves | 3e-05 |  |
| [[NF2]] | +0.54 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[UCHL3]] | +0.53 | +0.44 / +0.48 | both halves | 3e-05 |  |
| [[OSBPL3]] | +0.53 | +0.44 / +0.57 | both halves | 3e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFCAB2]] | -0.52 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[ZRANB2-DT]] | -0.51 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[FAM76B]] | -0.50 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[EFCAB6]] | -0.49 | -0.42 / -0.38 | both halves | 7e-05 |  |
| [[CMC4]] | -0.49 | -0.50 / -0.33 | both halves | 1e-04 |  |
| [[PUS10]] | -0.48 | -0.37 / -0.37 | both halves | 7e-05 |  |
| [[RBKS]] | -0.48 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[CCDC30]] | -0.48 | -0.39 / -0.27 | both halves | 3e-04 |  |
| [[UBAP2L]] | -0.47 | -0.39 / -0.34 | both halves | 1e-04 |  |
| [[PKN2-AS1]] | -0.47 | -0.41 / -0.26 | both halves | 4e-04 |  |
| [[DNAI4]] | -0.47 | -0.39 / -0.28 | both halves | 3e-04 |  |
| [[METTL6]] | -0.47 | -0.38 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZBED2]] | B | ZBED2 activity raises PLCXD2's level | lines that do not express ZBED2 (39) vs lines expressing it (11) | 2.67× lower at baseline in the lines without ZBED2 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SPON1, ENSG00000289850, KLK11 |
| [[NR3C1]] | B | NR3C1 activity lowers PLCXD2's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 2.8% of all compounds | 0.028 | ⚠ off-target possible; 3 compounds |
| [[ITGA6]] | B | ITGA6 activity raises PLCXD2's level | lines that do not express ITGA6 (9) vs lines expressing it (41) | 2.27× lower at baseline in the lines without ITGA6 | 0.034 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[LINP1]] | B | LINP1 activity raises PLCXD2's level | lines that do not express LINP1 (29) vs lines expressing it (21) | 1.80× lower at baseline in the lines without LINP1 | 0.044 | ⚠ within organs, on part of the lines; also absent: ENSG00000285743, LINC00707, IGFN1 |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OCIAD2]] | B | PLCXD2 activity raises OCIAD2's level | lines that do not express PLCXD2 (7) vs lines expressing it (43) | 2.26× lower at baseline in the lines without PLCXD2 | 0.017 | ⚠ within organs, on part of the lines; also absent: SOX4; maybe low, not absent |
| [[ITGA6]] | B | PLCXD2 activity raises ITGA6's level | lines that do not express PLCXD2 (7) vs lines expressing it (43) | 1.99× lower at baseline in the lines without PLCXD2 | 0.025 | ⚠ within organs, on part of the lines; also absent: SOX4; maybe low, not absent |
| [[LAMC2]] | B | PLCXD2 activity raises LAMC2's level | lines that do not express PLCXD2 (7) vs lines expressing it (43) | 2.79× lower at baseline in the lines without PLCXD2 | 0.060 | ⚠ within organs, on part of the lines; also absent: SOX4; maybe low, not absent |
| [[LINP1]] | B | PLCXD2 activity raises LINP1's level | lines that do not express PLCXD2 (7) vs lines expressing it (43) | 1.94× lower at baseline in the lines without PLCXD2 | 0.068 | ⚠ within organs, on part of the lines; also absent: SOX4; maybe low, not absent |
| [[YOD1]] | B | PLCXD2 activity raises YOD1's level | lines that do not express PLCXD2 (7) vs lines expressing it (43) | 1.98× lower at baseline in the lines without PLCXD2 | 0.073 | ⚠ within organs, on part of the lines; also absent: SOX4; maybe low, not absent |
| [[OSBPL3]] | B | PLCXD2 activity raises OSBPL3's level | lines that do not express PLCXD2 (7) vs lines expressing it (43) | 1.50× lower at baseline in the lines without PLCXD2 | 0.087 | ⚠ within organs, on part of the lines; also absent: SOX4; maybe low, not absent |
| [[EFCAB2]] | B | PLCXD2 activity lowers EFCAB2's level | lines that do not express PLCXD2 (7) vs lines expressing it (43) | 1.46× higher at baseline in the lines without PLCXD2 | 0.090 | ⚠ within organs, on part of the lines; also absent: SOX4; maybe low, not absent |

## Where it sits

- **Module**: [[Module 184]]; 20 genes; this gene is in the **+** arm (projection on the module's main direction 0.506). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.39).
- **Nodal map** (x, y) = (43.8, 13.8); signed map (3.7, 53.7). **Vector** length 106, 26.0% of its response variance represented; |z| ≥ 3 in 1,241 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.2 | +11.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.7 | +16.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.2 | +7.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.8 | +12.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.7 | +4.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.0 | +5.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.9 | +4.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.7 | +8.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.7 | -4.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -3.0 | -2.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.9 | +4.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.8 | -3.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.8 | -3.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.7 | -2.2 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.7 | -3.4 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -2.6 | -4.8 |

## What is on record

|  |  |
|---|---|
| Name | phosphatidylinositol specific phospholipase C X domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q13.2 — chr3:111,674,676-111,846,447 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ31579 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q0VAA5](https://www.uniprot.org/uniprotkb/Q0VAA5) (PI-PLC X domain-containing protein 2):

> Catalyzes the hydrolysis of inositol from phosphatidylinositol (1,2-diacyl-sn-glycero-3-phospho-(1D-myo-inositol), PI). Could also hydrolyze various multi-phosphorylated derivatives of PI, such as phosphatidylinositol-4,5 bisphosphate (PIP2), releasing inositol-1,4,5-trisphosphate (IP3) and the protein kinase C activator diacylglycerol (DAG), therefore mediating cell signaling (Probable).

**Summary**, from NCBI Gene [257068](https://www.ncbi.nlm.nih.gov/gene/257068):

> Predicted to enable phosphoric diester hydrolase activity. Predicted to be involved in lipid catabolic process and signal transduction. Predicted to be located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26462](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26462) · Entrez [257068](https://www.ncbi.nlm.nih.gov/gene/257068) · UniProt [Q0VAA5](https://www.uniprot.org/uniprotkb/Q0VAA5) · Ensembl [ENSG00000240891](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000240891)

## Data

Gene col 14253: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14253); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14253, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14253]; `tensor/DDL_lfc|DDL_z.npy` [14253]; `embed/gene_vectors.npy` [14253]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14253 or target_col == 14253). Every well: [[PLCXD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLCXD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
