---
symbol: "SPTBN4"
type: "gene"
col: 8353
ensembl_id: "ENSG00000160460"
name: "spectrin beta, non-erythrocytic 4"
location: "19q13.2"
module: 100
arm: "+"
pooled_cpm: 5.8
n_lines_expressing: 49
n_dd_up: 20
n_dd_down: 9
n_dd_up_clean: 15
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/100"]
generated_by: "tahoemap"
---

# SPTBN4

*spectrin beta, non-erythrocytic 4* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.76× (z +23.3, q 0e+00, up in 33 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.564× (z -7.1, q 7e-10, down in 20 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM266]] (+0.72, fdr 7e-06), [[CELF5]] (+0.66, fdr 8e-06), [[CDH23]] (+0.64, fdr 1e-05); moves opposite to [[MTOR]] (-0.53, fdr 1e-05), [[ATR]] (-0.51, fdr 2e-04), [[RNASEH1]] (-0.49, fdr 2e-04).
> It is in [[Module 100]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[DNAI1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8353.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.76×** | +23.3 | 0e+00 | 33/39 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **4.12×** | +17.6 | 0e+00 | 43/45 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.99×** | +17.2 | 0e+00 | 42/44 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.48×** | +16.0 | 0e+00 | 38/44 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **2.83×** | +12.9 | 4e-36 | 35/44 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.63×** | +12.0 | 2e-31 | 34/43 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.60×** | +11.4 | 2e-28 | 2/10 (HOP62, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.45×** | +11.1 | 5e-27 | 12/26 (C-33 A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.07×** | +9.1 | 8e-18 | 30/45 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.24×** | +5.2 | 9e-06 | 11/43 (SW480, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.46×** | +4.7 | 1e-04 | 13/43 (NCI-H460, HEC-1-A, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.30×** | +4.6 | 2e-04 | 12/39 (NCI-H2030, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.48×** | +4.5 | 2e-04 | 4/15 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.44×** | +4.4 | 5e-04 | 12/41 (NCI-H460, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.82×** | +3.9 | 0.004 | 5/25 (A549, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.024 | 9/43 (HT-29, C-33 A, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +3.3 | 0.030 | 9/45 (HOP62, LOX-IMVI, …) | top dose only |  |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | **1.30×** | +3.2 | 0.039 | 2/41 (NCI-H661, A-172) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.29×** | +3.2 | 0.043 | 10/44 (SW480, SHP-77, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8353.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.564×** | -7.1 | 7e-10 | 20/43 (HCT15, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.619×** | -5.9 | 8e-07 | 19/45 (C-33 A, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.670×** | -5.0 | 1e-04 | 18/43 (C-33 A, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.695×** | -4.5 | 8e-04 | 12/45 (C-33 A, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.696×** | -4.5 | 8e-04 | 17/41 (NCI-H23, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.725×** | -4.0 | 0.006 | 11/41 (A-427, KATO III, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.732×** | -3.9 | 0.009 | 13/45 (MIA PaCa-2, NCI-H1792, …) | inconsistent across doses |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | **0.766×** | -3.3 | 0.067 | 11/42 (AsPC-1, HOP62, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.774×** | -3.2 | 0.095 | 4/45 (AN3 CA, MIA PaCa-2, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | 0.778× | -3.1 | 0.11 | 13/34 (PANC-1, A549, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8353. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 8.34 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 4.46× (z +11.9) | — |
| [[PANC-1 (line)]] | alt | 4.14 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 7.40× (z +9.4) | [[Dinaciclib (drug)]] 0.05 µM 0.115× (z -9.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 13.4 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.113× (z -11.4) ⚠ cell-cycle shift, explains ~76% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.199× (z -8.8) |
| [[A549 (line)]] | wt | 8.98 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.89× (z +9.0) | — |
| [[HOP62 (line)]] | alt | 3.54 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.04× (z +10.2) | — |
| [[NCI-H460 (line)]] | wt | 3.86 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.16× (z +10.9) | — |
| [[A-172 (line)]] | wt | 7.56 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0878× (z -10.2) ⚠ toxic; cell-cycle shift, explains ~20% of this change |
| [[HCT15 (line)]] | alt | 7.38 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0404× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 8.36 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.99× (z +10.1) | — |
| [[HT-29 (line)]] | alt | 3.24 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 8.25× (z +8.8) | — |
| [[KATO III (line)]] | alt | 5.04 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0737× (z -9.3) ⚠ toxic; cell-cycle shift, explains ~20% of this change |
| [[LoVo (line)]] | wt | 1.76 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.0× (z +9.7) | — |
| [[LOX-IMVI (line)]] | wt | 3.59 | 0 | 1 | — | [[vincristine (drug)]] 0.05 µM 0.0575× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 6.89 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.129× (z -9.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 4.75 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.13 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.74 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.31 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.16 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.80 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8353), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM266]] | +0.72 | +0.72 / +0.73 | both halves | 7e-06 |  |
| [[CELF5]] | +0.66 | +0.58 / +0.68 | both halves | 8e-06 |  |
| [[CDH23]] | +0.64 | +0.53 / +0.70 | both halves | 1e-05 |  |
| [[COL26A1]] | +0.63 | +0.50 / +0.74 | both halves | 1e-05 |  |
| [[UPK1A-AS1]] | +0.63 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[DNAI1]] | +0.61 | +0.48 / +0.70 | both halves | 2e-05 |  |
| [[SLC26A5]] | +0.61 | +0.45 / +0.72 | both halves | 3e-05 |  |
| [[ETFBKMT]] | +0.60 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[RUNDC3B]] | +0.60 | +0.51 / +0.69 | both halves | 1e-05 |  |
| [[ADAM7-AS1]] | +0.60 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[MAST1]] | +0.60 | +0.43 / +0.74 | both halves | 3e-05 |  |
| [[CRLF1]] | +0.60 | +0.42 / +0.64 | both halves | 4e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTOR]] | -0.53 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[ATR]] | -0.51 | -0.31 / -0.50 | both halves | 2e-04 |  |
| [[RNASEH1]] | -0.49 | -0.30 / -0.54 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DNAI1]] | B | DNAI1 activity raises SPTBN4's level | lines that do not express DNAI1 (5) vs lines expressing it (45) | 2.27× lower at baseline in the lines without DNAI1 | 0.059 | ⚠ within organs, on part of the lines; also absent: FBXO15, KCNK15-AS1, CRB1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 100]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.668). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (13.9, 34.4); signed map (26.5, 19.0). **Vector** length 65.5, 10.3% of its response variance represented; |z| ≥ 3 in 1,080 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.8 | +16.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.5 | +12.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.8 | +11.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.7 | +23.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.1 | +11.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +4.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +3.3 | +3.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +2.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.4 | +0.8 |
| fall | [[Digitoxin (drug)]] 0.05 µM |  | -3.2 | -4.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.1 | -7.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | -2.4 | -4.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.0 | -3.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.5 | -0.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.5 | -1.5 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.4 | -2.0 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.4 | -0.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.3 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | spectrin beta, non-erythrocytic 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:40,466,241-40,576,464 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SPTBN3, KIAA1642 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Spectrins |
| Reactome | 14 pathways, smallest: Interaction between L1 and Ankyrins; NCAM signaling for neurite out-growth; COPI-mediated anterograde transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H254](https://www.uniprot.org/uniprotkb/Q9H254) (Spectrin beta chain, non-erythrocytic 4):

> Cytoskeletal adapter/scaffold involved in the organization of select excitable membrane microdomains (nodes of Ranvier, axon initial segment, cardiomyocyte intercalated disk), where it contributes to the targeting and stabilization of selected structural and regulatory proteins and ion-channel complexes, and supports ion-channel clustering in association with ANK3-dependent domain organization. In heart, supports SCN5A clustering in association with ANK3 at cardiomyocyte intercalated disk and …

**Summary**, from NCBI Gene [57731](https://www.ncbi.nlm.nih.gov/gene/57731):

> Spectrin is an actin crosslinking and molecular scaffold protein that links the plasma membrane to the actin cytoskeleton, and functions in the determination of cell shape, arrangement of transmembrane proteins, and organization of organelles. It is composed of two antiparallel dimers of alpha- and beta- subunits. This gene is one member of a family of beta-spectrin genes. The encoded protein localizes to the nuclear matrix, PML nuclear bodies, and cytoplasmic vesicles. A highly similar gene in …

**Accessions** — [HGNC:14896](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14896) · Entrez [57731](https://www.ncbi.nlm.nih.gov/gene/57731) · UniProt [Q9H254](https://www.uniprot.org/uniprotkb/Q9H254) · Ensembl [ENSG00000160460](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160460)

## Data

Gene col 8353: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8353); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8353, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8353]; `tensor/DDL_lfc|DDL_z.npy` [8353]; `embed/gene_vectors.npy` [8353]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8353 or target_col == 8353). Every well: [[SPTBN4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPTBN4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
