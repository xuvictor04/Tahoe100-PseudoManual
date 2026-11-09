---
symbol: "TAF12"
type: "gene"
col: 4196
ensembl_id: "ENSG00000120656"
name: "TATA-box binding protein associated factor 12"
location: "1p35.3"
module: 49
arm: "+"
pooled_cpm: 31.4
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 7
n_dd_up_clean: 17
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# TAF12

*TATA-box binding protein associated factor 12* — 1p35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.47× (z +20.6, q 0e+00, up in 44 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[PH-797804 (drug)]] 5 µM: 0.487× (z -6.4, q 7e-08, down in 32 of 47 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLPP5]] (+0.64, fdr 1e-05), [[NMNAT1]] (+0.64, fdr 7e-06), [[ZBTB8OS]] (+0.62, fdr 7e-06); moves opposite to [[TBL1XR1]] (-0.60, fdr 7e-06), [[DHX9]] (-0.59, fdr 4e-05), [[YWHAQ]] (-0.58, fdr 1e-05).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4196.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.47×** | +20.6 | 0e+00 | 44/47 (AsPC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.41×** | +15.2 | 0e+00 | 46/48 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.27×** | +14.2 | 2e-43 | 46/48 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.20×** | +13.7 | 3e-40 | 43/48 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.24×** | +13.4 | 4e-39 | 45/48 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.24×** | +13.4 | 6e-39 | 43/47 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.94×** | +11.0 | 3e-26 | 40/44 (RKO, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.48×** | +8.4 | 2e-15 | 35/48 (HOP62, A-172, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.47×** | +6.7 | 2e-09 | 27/47 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.46×** | +6.3 | 2e-08 | 19/38 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.43×** | +6.2 | 4e-08 | 32/48 (MIA PaCa-2, J82, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.42×** | +6.1 | 5e-08 | 29/48 (HOP62, SW480, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.42×** | +6.1 | 5e-08 | 35/47 (BT-474, J82, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.41×** | +5.9 | 1e-07 | 24/43 (NCI-H23, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.37×** | +5.5 | 2e-06 | 24/44 (PANC-1, NCI-H2347, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.37×** | +5.4 | 2e-06 | 29/48 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.31×** | +4.7 | 7e-05 | 23/48 (CFPAC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.21×** | +4.2 | 9e-04 | 23/47 (CFPAC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +3.6 | 0.007 | 10/48 (SK-MEL-2, A498, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4196.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **0.487×** | -6.4 | 7e-08 | 32/47 (SW 900, PANC-1, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.514×** | -6.0 | 7e-07 | 33/48 (PANC-1, HS-578T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.751×** | -4.9 | 1e-04 | 17/48 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.593×** | -4.7 | 4e-04 | 14/30 (NCI-H1573, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Trifluridine (drug)]] 0.5 µM |  | **0.823×** | -3.4 | 0.087 | 12/48 (A498, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.827×** | -3.3 | 0.087 | 12/48 (A498, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.822×** | -3.3 | 0.087 | 18/47 (RPMI-7951, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4196. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 34.5 | 6 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.08× (z +12.9) | — |
| [[SW480 (line)]] | alt | 33.7 | 6 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.00× (z +11.4) | — |
| [[HOP62 (line)]] | alt | 29.2 | 5 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.26× (z +12.4) | — |
| [[HEC-1-A (line)]] | alt | 27.0 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.84× (z +11.4) | — |
| [[NCI-H23 (line)]] | alt | 51.3 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.69× (z +12.5) | — |
| [[NCI-H460 (line)]] | wt | 28.2 | 4 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.80× (z +10.2) | — |
| [[HS-578T (line)]] | alt | 42.7 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.98× (z +12.5) | — |
| [[A-427 (line)]] | wt | 39.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.217× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change |
| [[CFPAC-1 (line)]] | alt | 20.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.43× (z +11.8) | — |
| [[HT-29 (line)]] | alt | 36.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +9.8) | — |
| [[J82 (line)]] | alt | 28.3 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.92× (z +9.1) | — |
| [[RKO (line)]] | wt | 33.5 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.71× (z +10.0) | — |
| [[RPMI-7951 (line)]] | alt | 34.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +8.7) | [[Niclosamide (olamine) (drug)]] 5 µM 0.199× (z -10.6) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 27.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.14× (z +12.9) | — |
| [[C-33 A (line)]] | alt | 80.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.110× (z -19.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change |
| [[C32 (line)]] | wt | 20.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +8.5) | — |
| [[COLO 205 (line)]] | alt | 31.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.01× (z +8.8) | — |
| [[Hs 766T (line)]] | wt | 38.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +8.9) | — |
| [[KATO III (line)]] | alt | 33.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +9.4) | — |
| [[LS 180 (line)]] | wt | 25.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.252× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change |
| [[NCI-H1573 (line)]] | alt | 29.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +8.8) | — |
| [[NCI-H1792 (line)]] | alt | 21.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.72× (z +10.1) | — |
| [[NCI-H2347 (line)]] | alt | 17.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +8.5) | — |
| [[PANC-1 (line)]] | alt | 52.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +10.2) | — |
| [[SNU-423 (line)]] | alt | 21.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +8.9) | — |
| [[SW 900 (line)]] | alt | 21.7 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0389× (z -10.1) |
| [[SW1417 (line)]] | alt | 28.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +9.1) | — |
| [[A-172 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 33.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 35.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4196), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLPP5]] | +0.64 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[NMNAT1]] | +0.64 | +0.74 / +0.58 | both halves | 7e-06 |  |
| [[ZBTB8OS]] | +0.62 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[ZNF778]] | +0.60 | +0.70 / +0.47 | both halves | 2e-05 |  |
| [[TMEM165]] | +0.59 | +0.30 / +0.58 | both halves | 2e-04 |  |
| [[MFSD8]] | +0.59 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[GOSR2]] | +0.59 | +0.44 / +0.61 | both halves | 3e-05 |  |
| [[ORMDL1]] | +0.58 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[CDC37L1]] | +0.58 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[ALG2]] | +0.56 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[FHIP2B]] | +0.56 | +0.35 / +0.62 | both halves | 1e-04 |  |
| [[FBXO28]] | +0.56 | +0.38 / +0.51 | both halves | 6e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBL1XR1]] | -0.60 | -0.60 / -0.63 | both halves | 7e-06 | pathway: Chromatin modifying enzymes |
| [[DHX9]] | -0.59 | -0.42 / -0.62 | both halves | 4e-05 |  |
| [[YWHAQ]] | -0.58 | -0.64 / -0.57 | both halves | 1e-05 |  |
| [[G3BP1]] | -0.56 | -0.36 / -0.55 | both halves | 1e-04 |  |
| [[SMG7]] | -0.54 | -0.47 / -0.66 | both halves | 2e-05 |  |
| [[PARP1]] | -0.54 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[DNAH7]] | -0.53 | -0.17 / -0.48 | ⚠ not reproduced | 0.001 |  |
| [[DLD]] | -0.53 | -0.37 / -0.53 | both halves | 8e-05 |  |
| [[PFKM]] | -0.52 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[PLPP2]] | -0.51 | -0.46 / -0.32 | both halves | 2e-04 |  |
| [[TTC5]] | -0.50 | -0.28 / -0.42 | both halves | 3e-04 | pathway: Regulation of TP53 Activity |
| [[SPTBN1]] | -0.50 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[GSTM4]] | -0.50 | -0.48 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TAF12's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.401). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-10.9, 25.1); signed map (0.1, 1.6). **Vector** length 76.2, 16.4% of its response variance represented; |z| ≥ 3 in 1,015 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +13.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +13.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.8 | +6.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.2 | +1.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.2 | +20.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.1 | +2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +2.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.9 | +6.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +6.1 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | -4.8 | +2.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.1 | -6.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.8 | -3.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | -3.5 | +6.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.4 | -6.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | +3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | -1.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.8 | -1.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.8 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | TATA-box binding protein associated factor 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.3 — chr1:28,587,829-28,648,291 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TAFII20; previously TAF2J |
| Gene groups (HGNC) | SAGA complex; General transcription factor IID complex subunits |
| Hallmark sets | DNA_REPAIR |
| Reactome | 22 pathways, smallest: HIV Transcription Initiation; RNA Polymerase II HIV Promoter Escape; RNA Polymerase II Promoter Escape |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16514](https://www.uniprot.org/uniprotkb/Q16514) (Transcription initiation factor TFIID subunit 12):

> The TFIID basal transcription factor complex plays a major role in the initiation of RNA polymerase II (Pol II)-dependent transcription. TFIID recognizes and binds promoters with or without a TATA box via its subunit TBP, a TATA-box-binding protein, and promotes assembly of the pre-initiation complex (PIC). The TFIID complex consists of TBP and TBP-associated factors (TAFs), including TAF1, TAF2, TAF3, TAF4, TAF5, TAF6, TAF7, TAF8, TAF9, TAF10, TAF11, TAF12 and TAF13. Component of the …

**Summary**, from NCBI Gene [6883](https://www.ncbi.nlm.nih.gov/gene/6883):

> Control of transcription by RNA polymerase II involves the basal transcription machinery which is a collection of proteins. These proteins with RNA polymerase II, assemble into complexes which are modulated by transactivator proteins that bind to cis-regulatory elements located adjacent to the transcription start site. Some modulators interact directly with the basal complex, whereas others may act as bridging proteins linking transactivators to the basal transcription factors. Some of these …

**Accessions** — [HGNC:11545](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11545) · Entrez [6883](https://www.ncbi.nlm.nih.gov/gene/6883) · UniProt [Q16514](https://www.uniprot.org/uniprotkb/Q16514) · Ensembl [ENSG00000120656](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120656)

## Data

Gene col 4196: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4196); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4196, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4196]; `tensor/DDL_lfc|DDL_z.npy` [4196]; `embed/gene_vectors.npy` [4196]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4196 or target_col == 4196). Every well: [[TAF12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TAF12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
