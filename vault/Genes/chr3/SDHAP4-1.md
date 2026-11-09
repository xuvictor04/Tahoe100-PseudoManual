---
symbol: "SDHAP4-1"
type: "gene"
col: 16577
ensembl_id: "ENSG00000291091"
name: ""
location: ""
module: 142
arm: "+"
pooled_cpm: 43.18
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 16
n_dd_up_clean: 6
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 2
tags: ["gene", "module/142"]
generated_by: "tahoemap"
---

# SDHAP4-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.53× (z +9.7, q 1e-19, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.293× (z -28.5, q 0e+00, down in 46 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SDHAP2]] (+0.88, fdr 7e-06), [[SDHAP1]] (+0.86, fdr 7e-06), [[SDHAP4]] (+0.77, fdr 7e-06, ⚠ same locus), [[IER3IP1]] (+0.75, fdr 7e-06); moves opposite to [[HNRNPK]] (-0.70, fdr 7e-06), [[TRIM44]] (-0.67, fdr 7e-06), [[TIGD2]] (-0.65, fdr 7e-06).
> It is in [[Module 142]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 2 go from it, the strongest it → [[SDHAP1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16577.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +9.7 | 1e-19 | 32/48 (PANC-1, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.42×** | +5.7 | 3e-06 | 27/48 (NCI-H2030, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.39×** | +5.4 | 1e-05 | 27/48 (HEC-1-A, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.33×** | +4.6 | 5e-04 | 25/48 (NCI-H460, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.31×** | +4.2 | 0.003 | 25/46 (NCI-H2030, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.29×** | +4.1 | 0.004 | 20/47 (BT-474, NCI-H2347, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.055 | 18/48 (HT-29, MIA PaCa-2, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.23×** | +3.4 | 0.055 | 15/48 (LS 180, NCI-H2347, …) | inconsistent across doses |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.23×** | +3.3 | 0.057 | 14/47 (SW480, COLO 205, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠; shown: the 15 strongest. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16577.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.293×** | -28.5 | 0e+00 | 46/47 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.284×** | -20.7 | 0e+00 | 45/47 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.296×** | -19.2 | 0e+00 | 45/48 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.410×** | -14.6 | 0e+00 | 47/48 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.604×** | -8.3 | 1e-14 | 36/48 (SNU-1, A-172, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.608×** | -8.2 | 2e-14 | 32/48 (SNU-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.693×** | -5.8 | 5e-07 | 21/37 (A549, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.721×** | -5.4 | 5e-06 | 26/46 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.747×** | -4.4 | 5e-04 | 22/41 (hTERT-HPNE, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.771×** | -4.3 | 1e-03 | 20/48 (hTERT-HPNE, HOP62, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.842× | -4.0 | 0.003 | 19/48 (NCI-H23, HS-578T, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.771×** | -4.0 | 0.003 | 25/47 (LoVo, HS-578T, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.786×** | -4.0 | 0.003 | 18/48 (AsPC-1, CFPAC-1, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.782×** | -3.9 | 0.004 | 22/48 (HOP62, NCI-H2347, …) | rises with dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **0.788×** | -3.6 | 0.010 | 16/48 (SK-MEL-2, HS-578T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16577. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 75.6 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -22.6) |
| [[A-172 (line)]] | wt | 60.8 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0849× (z -34.3) |
| [[HOP62 (line)]] | alt | 74.2 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -25.8) |
| [[HEC-1-A (line)]] | alt | 78.1 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -25.9) |
| [[hTERT-HPNE (line)]] | wt | 44.9 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -20.3) |
| [[NCI-H1573 (line)]] | alt | 35.4 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -16.1) |
| [[NCI-H2347 (line)]] | alt | 67.9 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -29.6) |
| [[PANC-1 (line)]] | alt | 25.8 | 1 | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.91× (z +14.0) | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -13.5) |
| [[SW480 (line)]] | alt | 50.5 | 1 | 4 | [[Auranofin (drug)]] 5 µM 2.53× (z +10.0) | [[Harringtonine (drug)]] 5 µM 0.351× (z -10.9) |
| [[A498 (line)]] | wt | 37.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -15.5) |
| [[AsPC-1 (line)]] | alt | 28.2 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -19.1) |
| [[LS 180 (line)]] | wt | 49.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -21.3) |
| [[NCI-H460 (line)]] | wt | 16.7 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -15.4) |
| [[RPMI-7951 (line)]] | alt | 51.2 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -10.9) |
| [[A549 (line)]] | wt | 30.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -14.9) |
| [[CFPAC-1 (line)]] | alt | 58.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -23.5) |
| [[Panc 03.27 (line)]] | alt | 63.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -15.7) |
| [[SK-MEL-2 (line)]] | alt | 38.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -14.2) |
| [[SNU-423 (line)]] | alt | 48.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -18.1) |
| [[SW 900 (line)]] | alt | 40.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -16.7) |
| [[SW1417 (line)]] | alt | 42.1 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -11.0) |
| [[A-427 (line)]] | wt | 41.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -20.8) |
| [[HCT15 (line)]] | alt | 40.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.113× (z -14.3) |
| [[Hs 766T (line)]] | wt | 46.6 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.131× (z -14.9) |
| [[HT-29 (line)]] | alt | 29.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -14.3) |
| [[LOX-IMVI (line)]] | wt | 25.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -15.3) |
| [[MIA PaCa-2 (line)]] | alt | 65.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.219× (z -12.3) |
| [[SNU-1 (line)]] | wt | 57.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.159× (z -13.1) |
| [[AN3 CA (line)]] | alt | 27.2 | 0 | 1 | — | [[Drospirenone (drug)]] 0.5 µM 0.0921× (z -8.5) |
| [[BT-474 (line)]] | alt | 65.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -19.7) |
| [[CHP-212 (line)]] | wt | 26.1 | 0 | 1 | — | [[Sodium Salicylate (drug)]] 0.5 µM 0.0833× (z -8.9) |
| [[COLO 205 (line)]] | alt | 75.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -15.4) |
| [[J82 (line)]] | alt | 54.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -16.1) |
| [[KATO III (line)]] | alt | 37.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -14.7) |
| [[LoVo (line)]] | wt | 34.8 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.323× (z -9.3) |
| [[NCI-H2030 (line)]] | alt | 17.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -9.9) |
| [[NCI-H23 (line)]] | alt | 29.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +9.7) | — |
| [[RKO (line)]] | wt | 16.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.19× (z +10.9) | — |
| [[SW48 (line)]] | wt | 33.8 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.198× (z -9.3) |
| [[C-33 A (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 36.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 34.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 52.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16577), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHAP2]] | +0.88 | +0.90 / +0.90 | both halves | 7e-06 |  |
| [[SDHAP1]] | +0.86 | +0.89 / +0.85 | both halves | 7e-06 |  |
| [[SDHAP4]] | +0.77 | +0.80 / +0.72 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[IER3IP1]] | +0.75 | +0.78 / +0.72 | both halves | 7e-06 |  |
| [[MIR4458HG]] | +0.73 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[SEC11A]] | +0.72 | +0.75 / +0.65 | both halves | 7e-06 |  |
| [[RNF139-DT]] | +0.71 | +0.65 / +0.76 | both halves | 7e-06 |  |
| [[KLHL7]] | +0.71 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[NDUFAF7]] | +0.70 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[RAB6A]] | +0.70 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[CCT6P3-1]] | +0.70 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[KDELR1]] | +0.69 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[ZNF250]] | +0.69 | +0.60 / +0.72 | both halves | 7e-06 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPK]] | -0.70 | -0.63 / -0.65 | both halves | 7e-06 |  |
| [[TRIM44]] | -0.67 | -0.68 / -0.60 | both halves | 7e-06 |  |
| [[TIGD2]] | -0.65 | -0.71 / -0.58 | both halves | 7e-06 |  |
| [[CPSF2]] | -0.65 | -0.67 / -0.59 | both halves | 7e-06 |  |
| [[ZXDB]] | -0.64 | -0.68 / -0.59 | both halves | 7e-06 |  |
| [[ZNF462]] | -0.64 | -0.66 / -0.59 | both halves | 7e-06 |  |
| [[CSTF2T]] | -0.64 | -0.64 / -0.64 | both halves | 7e-06 |  |
| [[DCLRE1A]] | -0.64 | -0.69 / -0.58 | both halves | 8e-06 |  |
| [[BBS10]] | -0.63 | -0.67 / -0.64 | both halves | 7e-06 |  |
| [[LIG4]] | -0.63 | -0.67 / -0.59 | both halves | 7e-06 |  |
| [[ZC3H11A]] | -0.63 | -0.46 / -0.63 | both halves | 3e-05 |  |
| [[VEZF1]] | -0.62 | -0.55 / -0.61 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SDHAP1]] | C | SDHAP4-1's natural level strengthens SDHAP1's drug response | SDHAP4-1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.78, reverse +0.29; direction not clear | 6e-04 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[SDHAP2]] | C | SDHAP4-1's natural level strengthens SDHAP2's drug response | SDHAP4-1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.25; direction not clear | 0.073 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 142]]; 33 genes; every member is in the + arm (projection on the module's main direction 0.756). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.40; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-0.3, -14.8); signed map (-38.5, 1.0). **Vector** length 130, 37.5% of its response variance represented; |z| ≥ 3 in 921 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.9 | +4.2 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.4 | +5.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +9.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.8 | +2.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.6 | +4.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +4.2 | +3.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.5 | +2.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.2 | +2.2 |
|  | [[Pasireotide (acetate) (drug)]] 5 µM |  | +2.8 | +1.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -10.1 | -14.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -9.7 | -19.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.6 | -20.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.0 | -28.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.0 | -8.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.2 | -3.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.5 | -4.0 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | -3.1 | -2.5 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -3.0 | -2.1 |

## What is on record

> [!warning] No registry record
> SDHAP4-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16577: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16577); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16577, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16577]; `tensor/DDL_lfc|DDL_z.npy` [16577]; `embed/gene_vectors.npy` [16577]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16577 or target_col == 16577). Every well: [[SDHAP4-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SDHAP4-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
