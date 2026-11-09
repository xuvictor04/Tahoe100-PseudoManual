---
symbol: "PRPSAP2"
type: "gene"
col: 6491
ensembl_id: "ENSG00000141127"
name: "phosphoribosyl pyrophosphate synthetase associated protein 2"
location: "17p11.2"
module: 170
arm: "+"
pooled_cpm: 39.01
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 4
n_dd_up_clean: 7
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/170"]
generated_by: "tahoemap"
---

# PRPSAP2

*phosphoribosyl pyrophosphate synthetase associated protein 2* — 17p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.53× (z +11.3, q 6e-27, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.768× (z -5.0, q 4e-04, down in 24 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 4 lines (A-427 0.206×, RKO 0.251×, NCI-H23 0.325×, BT-474 0.281×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (C-33 A 0.0697×, H4 0.124×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~1% of this change); [[Orlistat (drug)]] 0.05 µM in 1 line (NCI-H661 0.0714×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[INTS8]] (+0.61, fdr 1e-05), [[CCDC22]] (+0.57, fdr 3e-05), [[TAF15]] (+0.56, fdr 1e-05); moves opposite to [[RABGAP1L]] (-0.53, fdr 5e-05), [[UBE2E2]] (-0.48, fdr 5e-05), [[HPSE]] (-0.48, fdr 2e-04).
> It sits in the **+** arm of [[Module 170]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6491.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.53×** | +11.3 | 6e-27 | 34/48 (LoVo, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +7.7 | 3e-12 | 34/47 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.40×** | +6.3 | 5e-08 | 29/48 (A-427, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +6.2 | 6e-08 | 30/48 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.38×** | +6.0 | 3e-07 | 28/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.25×** | +5.8 | 7e-07 | 22/48 (LoVo, LS 180, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.31×** | +5.0 | 5e-05 | 24/48 (KATO III, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.28×** | +4.4 | 8e-04 | 22/48 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.24×** | +4.0 | 0.003 | 20/48 (A549, A498, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.2 | 0.076 | 16/48 (RKO, MIA PaCa-2, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.18× | +3.1 | 0.10 | 14/48 (SW48, A-427, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.12× | +3.1 | 0.11 | 10/48 (NCI-H460, A549, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6491.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 4 lines (A-427 0.206×, RKO 0.251×, NCI-H23 0.325×, BT-474 0.281×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (C-33 A 0.0697×, H4 0.124×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~1% of this change); [[Orlistat (drug)]] 0.05 µM in 1 line (NCI-H661 0.0714×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.768×** | -5.0 | 4e-04 | 24/48 (MIA PaCa-2, NCI-H460, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.766×** | -4.6 | 0.001 | 23/45 (A-427, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.648×** | -4.3 | 0.004 | 16/33 (C32, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[Thymol (drug)]] 5 µM |  | 0.869× | -3.7 | 0.025 | 13/48 (HS-578T, LoVo, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.731×** | -3.6 | 0.038 | 14/48 (SNU-1, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Rapamycin (drug)]] 0.5 µM |  | 0.840× | -3.3 | 0.090 | 18/47 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~1% of this change | 0.841× | -3.3 | 0.090 | 20/47 (C-33 A, H4, …) | inconsistent across doses | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~11% of this change | 0.837× | -3.2 | 0.093 | 18/47 (HepG2/C3A, NCI-H460, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6491. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 46.8 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +10.7) | [[Dinaciclib (drug)]] 0.05 µM 0.206× (z -14.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 31.3 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +14.0) | — |
| [[A498 (line)]] | wt | 53.8 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.06× (z +9.4) | — |
| [[H4 (line)]] | wt | 28.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.124× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~1% of this change |
| [[LS 180 (line)]] | wt | 34.3 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.71× (z +10.5) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.51× (z +9.7) | — |
| [[NCI-H23 (line)]] | alt | 61.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.325× (z -10.6) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 46.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +10.0) | — |
| [[A549 (line)]] | wt | 58.2 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +8.6) | — |
| [[BT-474 (line)]] | alt | 25.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.281× (z -8.6) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 68.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0697× (z -24.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~1% of this change |
| [[KATO III (line)]] | alt | 53.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +8.8) | — |
| [[LOX-IMVI (line)]] | wt | 46.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +10.5) | — |
| [[NCI-H2030 (line)]] | alt | 42.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +8.8) | — |
| [[NCI-H661 (line)]] | alt | 62.1 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.0714× (z -10.6) |
| [[RKO (line)]] | wt | 48.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.251× (z -11.2) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 78.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.03× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[SW48 (line)]] | wt | 33.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.234× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 32.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 56.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 38.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 47.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 55.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 41.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 79.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 62.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 44.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6491), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INTS8]] | +0.61 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[CCDC22]] | +0.57 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[TAF15]] | +0.56 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[ZNF79]] | +0.55 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[COQ9]] | +0.55 | +0.62 / +0.42 | both halves | 4e-05 |  |
| [[DCP1B]] | +0.54 | +0.58 / +0.39 | both halves | 5e-05 |  |
| [[RC3H2]] | +0.54 | +0.56 / +0.46 | both halves | 2e-05 |  |
| [[KLHL12]] | +0.54 | +0.63 / +0.46 | both halves | 2e-05 |  |
| [[TMEM128]] | +0.53 | +0.64 / +0.32 | both halves | 2e-04 |  |
| [[CEPT1]] | +0.53 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[DDX59]] | +0.53 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[TP53]] | +0.53 | +0.63 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RABGAP1L]] | -0.53 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[UBE2E2]] | -0.48 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[HPSE]] | -0.48 | -0.47 / -0.30 | both halves | 2e-04 |  |
| [[PLPP2]] | -0.46 | -0.45 / -0.37 | both halves | 9e-05 |  |
| [[CDK14]] | -0.46 | -0.37 / -0.49 | both halves | 7e-05 |  |
| [[DIAPH2]] | -0.46 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[DNAJB1]] | -0.46 | -0.36 / -0.41 | both halves | 1e-04 |  |
| [[SGK1]] | -0.45 | -0.43 / -0.45 | both halves | 4e-05 |  |
| [[TRIB1]] | -0.44 | -0.40 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PRPSAP2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.0% of all compounds | 0.005 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[DIAPH2]] | B | DIAPH2 activity lowers PRPSAP2's level | lines that do not express DIAPH2 (7) vs lines expressing it (43) | 1.28× higher at baseline in the lines without DIAPH2 | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000271204 |
| [[TOP2B]] | B | TOP2B activity lowers PRPSAP2's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 170]]; 24 genes; this gene is in the **+** arm (projection on the module's main direction 0.578). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-20.8, 17.8); signed map (7.4, -15.8). **Vector** length 81.9, 16.4% of its response variance represented; |z| ≥ 3 in 803 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +4.6 | +6.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +7.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.7 | +6.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +6.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | +3.1 | +5.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +3.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.2 | +2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +1.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +0.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.1 | -5.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~11% of this change | -3.2 | -3.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.1 | -0.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.1 | +0.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | +0.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -0.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.4 | -1.4 |
|  | [[Thymol (drug)]] 5 µM |  | -1.4 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | phosphoribosyl pyrophosphate synthetase associated protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p11.2 — chr17:18,840,085-18,931,287 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PAP41 |
| Gene groups (HGNC) | Phosphoribosyl pyrophosphate synthetase associated protein family |
| Matched by | ensembl_id |

**Function**, from UniProt [O60256](https://www.uniprot.org/uniprotkb/O60256) (Phosphoribosyl pyrophosphate synthase-associated protein 2):

> Seems to play a negative regulatory role in 5-phosphoribose 1-diphosphate synthesis.

**Summary**, from NCBI Gene [5636](https://www.ncbi.nlm.nih.gov/gene/5636):

> This gene encodes a protein that associates with the enzyme phosphoribosylpyrophosphate synthetase (PRS). PRS catalyzes the formation of phosphoribosylpyrophosphate which is a substrate for synthesis of purine and pyrimidine nucleotides, histidine, tryptophan and NAD. PRS exists as a complex with two catalytic subunits and two associated subunits. This gene encodes a non-catalytic associated subunit of PRS. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Sep …

**Accessions** — [HGNC:9467](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9467) · Entrez [5636](https://www.ncbi.nlm.nih.gov/gene/5636) · UniProt [O60256](https://www.uniprot.org/uniprotkb/O60256) · Ensembl [ENSG00000141127](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141127)

## Data

Gene col 6491: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6491); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6491, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6491]; `tensor/DDL_lfc|DDL_z.npy` [6491]; `embed/gene_vectors.npy` [6491]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6491 or target_col == 6491). Every well: [[PRPSAP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRPSAP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
