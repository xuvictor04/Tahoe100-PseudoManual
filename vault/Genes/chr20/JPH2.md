---
symbol: "JPH2"
type: "gene"
col: 7395
ensembl_id: "ENSG00000149596"
name: "junctophilin 2"
location: "20q13.12"
module: 139
arm: "+"
pooled_cpm: 18.83
n_lines_expressing: 31
n_dd_up: 39
n_dd_down: 30
n_dd_up_clean: 37
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 6
direction_downstream: 2
tags: ["gene", "module/139"]
generated_by: "tahoemap"
---

# JPH2

*junctophilin 2* — 20q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 39 drug-doses (2 with an alert ⚠); the strongest is [[Clobetasol propionate (drug)]] 0.05 µM: 2.39× (z +10.2, q 8e-22, up in 18 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.401× (z -10.7, q 5e-24, down in 20 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IRAK3]] (+0.69, fdr 9e-06), [[TNS2]] (+0.66, fdr 1e-05), [[MAOA]] (+0.65, fdr 7e-06); moves opposite to [[DOP1B]] (-0.53, fdr 1e-05), [[MMP1]] (-0.51, fdr 2e-05), [[ARHGAP21]] (-0.50, fdr 5e-05).
> It is in [[Module 139]], a single-armed module (Interleukin-4 and Interleukin-13 signaling).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[DNAH5]] → it (grade B ⚠); 2 go from it, the strongest it → [[BCL6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 2 with an alert ⚠; shown: the 15 strongest. 39 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7395.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **2.39×** | +10.2 | 8e-22 | 18/27 (A498, A-172, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 5 µM |  | **5.25×** | +10.2 | 8e-22 | 17/28 (PANC-1, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **2.37×** | +10.1 | 1e-21 | 19/27 (A498, Hs 766T, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **2.24×** | +9.5 | 4e-19 | 18/27 (A498, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | **1.77×** | +9.5 | 4e-19 | 20/28 (A498, HS-578T, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **2.11×** | +8.8 | 2e-16 | 20/27 (A498, HS-578T, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.5 µM |  | **2.10×** | +8.7 | 3e-16 | 20/27 (A498, HS-578T, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 5 µM |  | **1.95×** | +7.8 | 4e-13 | 19/29 (A498, HS-578T, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **2.06×** | +7.8 | 4e-13 | 17/26 (A498, HS-578T, …) | all doses, flat |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.94×** | +7.7 | 6e-13 | 16/26 (A498, HS-578T, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 5 µM |  | **1.92×** | +7.6 | 1e-12 | 18/29 (HS-578T, A498, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **1.91×** | +7.6 | 2e-12 | 19/28 (A498, HS-578T, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.90×** | +7.5 | 2e-12 | 19/29 (A498, HS-578T, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.95×** | +7.5 | 2e-12 | 19/27 (A498, HS-578T, …) | all doses, flat |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **1.89×** | +7.5 | 3e-12 | 18/29 (A498, HS-578T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7395.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.401×** | -10.7 | 5e-24 | 20/28 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.433×** | -9.8 | 3e-20 | 20/29 (NCI-H460, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.462×** | -9.1 | 2e-17 | 21/28 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.467×** | -9.0 | 5e-17 | 25/29 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.479×** | -8.3 | 1e-14 | 18/28 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.559×** | -6.8 | 8e-10 | 19/27 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.570×** | -6.6 | 3e-09 | 19/29 (NCI-H460, MIA PaCa-2, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.580×** | -6.4 | 1e-08 | 17/29 (CFPAC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.604×** | -5.9 | 2e-07 | 17/27 (HOP62, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.640×** | -5.2 | 9e-06 | 19/29 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.678×** | -4.6 | 2e-04 | 16/29 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.678×** | -4.6 | 2e-04 | 13/29 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.701×** | -3.9 | 0.004 | 19/27 (SNU-423, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.716×** | -3.9 | 0.004 | 8/27 (CFPAC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Neratinib (drug)]] 5 µM |  | **0.720×** | -3.9 | 0.004 | 9/28 (BT-474, NCI-H2030, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.804×** | -3.6 | 0.010 | 11/29 (J82, NCI-H460, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.729×** | -3.6 | 0.012 | 12/27 (SNU-423, SW 1088, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7395. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 104 | 0 | 23 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.107× (z -20.2) |
| [[NCI-H460 (line)]] | wt | 35.2 | 0 | 19 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.106× (z -15.4) |
| [[A498 (line)]] | wt | 9.91 | 18 | 0 | [[Triamcinolone (drug)]] 5 µM 5.08× (z +11.3) | — |
| [[CFPAC-1 (line)]] | alt | 29.3 | 0 | 17 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0650× (z -17.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0527× (z -13.3) |
| [[SNU-423 (line)]] | alt | 119 | 0 | 17 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.172× (z -16.2) |
| [[HepG2_C3A (line)]] | wt | 69.7 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0622× (z -20.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0887× (z -12.5) |
| [[HS-578T (line)]] | alt | 11.5 | 12 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.1× (z +13.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Triamcinolone (drug)]] 5 µM 7.46× (z +10.5) | — |
| [[RPMI-7951 (line)]] | alt | 82.4 | 4 | 6 (2 ⚠) | [[Clobetasol propionate (drug)]] 0.5 µM 3.98× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.197× (z -15.7) |
| [[Hs 766T (line)]] | wt | 54.3 | 7 | 0 | [[Clobetasol propionate (drug)]] 0.5 µM 6.79× (z +10.1) | — |
| [[J82 (line)]] | alt | 56.9 | 0 | 5 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.339× (z -11.2) |
| [[NCI-H1573 (line)]] | alt | 14.8 | 0 | 5 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0881× (z -11.4) |
| [[PANC-1 (line)]] | alt | 8.88 | 0 | 5 | — | [[Ixazomib citrate (drug)]] 5 µM 0.158× (z -10.7) |
| [[A-172 (line)]] | wt | 6.24 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.0× (z +13.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Clobetasol propionate (drug)]] 0.05 µM 16.1× (z +10.9) | — |
| [[SW 1088 (line)]] | alt | 190 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0218× (z -13.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.159× (z -9.3) |
| [[MIA PaCa-2 (line)]] | alt | 14.5 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0679× (z -11.5) |
| [[HEC-1-A (line)]] | alt | 16.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 10.4 | 0 | 1 | — | [[Doxycycline (monohydrate) (drug)]] 5 µM 0.0503× (z -13.0) |
| [[SHP-77 (line)]] | alt | 5.78 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 1.81 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 8.25 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.23 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.87 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.90 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.86 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.90 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.10 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.48 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.55 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.01 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.13 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.68 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.86 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.02 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.61 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.81 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.25 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.13 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.88 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 5.47 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7395), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IRAK3]] | +0.69 | +0.57 / +0.71 | both halves | 9e-06 | **novel candidate** |
| [[TNS2]] | +0.66 | +0.55 / +0.67 | both halves | 1e-05 | **novel candidate** |
| [[MAOA]] | +0.65 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[ADGRG2]] | +0.64 | +0.53 / +0.70 | both halves | 1e-05 | **novel candidate** |
| [[KLF9]] | +0.63 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[NNMT]] | +0.62 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[CAVIN2]] | +0.62 | +0.58 / +0.61 | both halves | 8e-06 |  |
| [[TLR2]] | +0.61 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[KCNG2]] | +0.61 | +0.58 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[SAA2]] | +0.60 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[SAA2-SAA4]] | +0.59 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[STOM]] | +0.59 | +0.59 / +0.58 | both halves | 8e-06 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DOP1B]] | -0.53 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[MMP1]] | -0.51 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[ARHGAP21]] | -0.50 | -0.55 / -0.39 | both halves | 5e-05 |  |
| [[PTHLH]] | -0.49 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[TMEM158]] | -0.48 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[LHX1-DT]] | -0.48 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[NPTX1]] | -0.46 | -0.38 / -0.45 | both halves | 7e-05 |  |
| [[SLC5A3]] | -0.46 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[WNT7B]] | -0.45 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[BEND7]] | -0.45 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[MRPS6]] | -0.44 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[ANXA10]] | -0.44 | -0.36 / -0.46 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 3, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DNAH5]] | B | DNAH5 activity raises JPH2's level | lines that do not express DNAH5 (10) vs lines expressing it (40) | 3.42× lower at baseline in the lines without DNAH5 | 0.057 | ⚠ within organs, on part of the lines; also absent: LINC02966; maybe low, not absent |
| [[NR3C1]] | B | NR3C1 activity raises JPH2's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 5.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[MT1F]] | B | MT1F activity raises JPH2's level | lines that do not express MT1F (17) vs lines expressing it (33) | 2.30× lower at baseline in the lines without MT1F | 0.077 | ⚠ within organs, on part of the lines; also absent: CDC42BPG, RASAL1, ENSG00000289862 |
| [[C3]] | C | C3 activity raises JPH2's level | lines that do not express C3 (32) vs lines expressing it (18) | 3.34× lower at baseline in the lines without C3 | 0.040 | ⚠ within organs, on part of the lines; also absent: TNFSF14, CP, CARD11; co-absent with the target |
| [[HTRA3]] | C | HTRA3 activity raises JPH2's level | lines that do not express HTRA3 (31) vs lines expressing it (19) | 2.80× lower at baseline in the lines without HTRA3 | 0.081 | ⚠ within organs, on part of the lines; also absent: PAPPA, LUM, LAYN; co-absent with the target |
| [[SRGN]] | C | SRGN activity raises JPH2's level | lines that do not express SRGN (30) vs lines expressing it (20) | 3.08× lower at baseline in the lines without SRGN | 0.092 | ⚠ within organs, on part of the lines; also absent: SIRLNT, SPOCK1, KIRREL3; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BCL6]] | B | JPH2 activity lowers BCL6's level | lines that do not express JPH2 (19) vs lines expressing it (31) | 1.20× higher at baseline in the lines without JPH2 | 0.060 | ⚠ within organs, on part of the lines; also absent: COL7A1, HDX, SRGN; maybe low, not absent |
| [[VSTM2L]] | B | JPH2 activity lowers VSTM2L's level | lines that do not express JPH2 (19) vs lines expressing it (31) | 1.00× higher at baseline in the lines without JPH2 | 0.093 | ⚠ within organs, on part of the lines; also absent: COL7A1, HDX, SRGN; maybe low, not absent |

## Where it sits

- **Module**: [[Module 139]] — Interleukin-4 and Interleukin-13 signaling; 34 genes; every member is in the + arm (projection on the module's main direction 0.677). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (29.1, 16.5); signed map (17.9, 30.7). **Vector** length 124, 36.2% of its response variance represented; |z| ≥ 3 in 1,230 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +6.0 | +10.2 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +5.4 | +10.1 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | +5.2 | +9.5 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +5.2 | +8.7 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +5.1 | +8.8 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +4.9 | +7.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -4.1 | -3.2 |
|  | [[Selinexor (drug)]] 5 µM |  | -4.1 | -3.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.5 | -9.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.2 | -6.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.1 | -3.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.7 | -3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | -9.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.2 | -3.4 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | junctophilin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.12 — chr20:44,106,590-44,187,188 (-) |
| Ensembl biotype | protein_coding |
| Also known as | JP-2, JP2 |
| Gene groups (HGNC) | Junctophilins; MORN repeat containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BR39](https://www.uniprot.org/uniprotkb/Q9BR39) (Junctophilin-2):

> [Junctophilin-2]: Membrane-binding protein that provides a structural bridge between the plasma membrane and the sarcoplasmic reticulum and is required for normal excitation-contraction coupling in cardiomyocytes. Provides a structural foundation for functional cross-talk between the cell surface and intracellular Ca(2+) release channels by maintaining the 12-15 nm gap between the sarcolemma and the sarcoplasmic reticulum membranes in the cardiac dyads (By similarity). Necessary for proper …

**Summary**, from NCBI Gene [57158](https://www.ncbi.nlm.nih.gov/gene/57158):

> Junctional complexes between the plasma membrane and endoplasmic/sarcoplasmic reticulum are a common feature of all excitable cell types and mediate cross talk between cell surface and intracellular ion channels. The protein encoded by this gene is a component of junctional complexes and is composed of a C-terminal hydrophobic segment spanning the endoplasmic/sarcoplasmic reticulum membrane and a remaining cytoplasmic domain that shows specific affinity for the plasma membrane. This gene is a …

**Accessions** — [HGNC:14202](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14202) · Entrez [57158](https://www.ncbi.nlm.nih.gov/gene/57158) · UniProt [Q9BR39](https://www.uniprot.org/uniprotkb/Q9BR39) · Ensembl [ENSG00000149596](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149596)

## Data

Gene col 7395: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7395); `tables/drug_effects.parquet` (71 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7395, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7395]; `tensor/DDL_lfc|DDL_z.npy` [7395]; `embed/gene_vectors.npy` [7395]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7395 or target_col == 7395). Every well: [[JPH2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/JPH2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
