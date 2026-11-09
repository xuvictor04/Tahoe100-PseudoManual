---
symbol: "EIF2B2"
type: "gene"
col: 4110
ensembl_id: "ENSG00000119718"
name: "eukaryotic translation initiation factor 2B subunit beta"
location: "14q24.3"
module: 7
arm: "+"
pooled_cpm: 13.3
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 1
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# EIF2B2

*eukaryotic translation initiation factor 2B subunit beta* — 14q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (12 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.48× (z +15.4, q 0e+00, up in 44 of 47 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.87× (z +14.9, q 0e+00, up in 40 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Binimetinib (drug)]] 0.05 µM: 0.847× (z -3.9, q 0.035, down in 13 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0562×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2030 0.244×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (BT-474 0.103×); [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM in 1 line (SW 900 0.127×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF408]] (+0.67, fdr 1e-05), [[RNF25]] (+0.67, fdr 1e-05), [[MRPL10]] (+0.64, fdr 3e-05); moves opposite to [[LUC7L3]] (-0.58, fdr 2e-05), [[NAP1L1]] (-0.55, fdr 3e-05), [[PABPN1]] (-0.51, fdr 4e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 15 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4110.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.48×** | +15.4 | 0e+00 | 44/47 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.45×** | +15.2 | 0e+00 | 44/47 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.87×** | +14.9 | 0e+00 | 40/47 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +14.6 | 0e+00 | 35/46 (CFPAC-1, A549, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.09×** | +12.5 | 6e-34 | 40/47 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **3.79×** | +11.8 | 3e-30 | 40/48 (SW480, HOP62, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.89×** | +10.8 | 5e-25 | 35/44 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.93×** | +10.7 | 7e-25 | 36/46 (NCI-H1573, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.54×** | +8.3 | 1e-14 | 29/44 (SW480, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.39×** | +7.8 | 3e-13 | 23/48 (CFPAC-1, HEC-1-A, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.53×** | +7.2 | 3e-11 | 29/47 (HEC-1-A, LoVo, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.57×** | +7.2 | 3e-11 | 24/47 (NCI-H2347, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.52×** | +7.1 | 5e-11 | 25/47 (SW480, BT-474, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.52×** | +7.1 | 6e-11 | 26/46 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **1.54×** | +7.0 | 1e-10 | 26/43 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.45×** | +6.3 | 1e-08 | 26/47 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.45×** | +6.3 | 1e-08 | 18/47 (CFPAC-1, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.63×** | +4.3 | 4e-04 | 11/44 (NCI-H1573, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.28×** | +4.1 | 1e-03 | 12/47 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4110.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0562×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2030 0.244×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (BT-474 0.103×); [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM in 1 line (SW 900 0.127×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Binimetinib (drug)]] 0.05 µM |  | 0.847× | -3.9 | 0.035 | 13/48 (NCI-H661, CFPAC-1, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.789×** | -3.8 | 0.035 | 9/48 (Hs 766T, A-427, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cepharanthine (drug)]] 5 µM |  | 0.867× | -3.5 | 0.086 | 14/48 (AN3 CA, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | 0.841× | -3.4 | 0.086 | 10/48 (Hs 766T, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.819× | -3.3 | 0.12 | 9/47 (NCI-H2030, HS-578T, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.832× | -3.1 | 0.14 | 5/47 (A-172, Hs 766T, …) | rises with dose |  |
| [[BI-3406 (drug)]] 5 µM |  | 0.703× | -3.1 | 0.14 | 5/47 (Panc 03.27, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.05 µM |  | 0.826× | -3.1 | 0.14 | 2/48 (MIA PaCa-2, C-33 A) | inconsistent across doses |  |
| [[Gemcitabine (drug)]] 0.5 µM |  | 0.838× | -3.0 | 0.15 | 9/48 (KATO III, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.41 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4110. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 17.5 | 5 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.41× (z +11.6) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +9.7) | — |
| [[CFPAC-1 (line)]] | alt | 18.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.86× (z +10.2) | — |
| [[HepG2_C3A (line)]] | wt | 9.70 | 0 | 2 | — | [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM 0.0562× (z -11.3) |
| [[MIA PaCa-2 (line)]] | alt | 8.04 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 8.47× (z +9.6) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H1573 (line)]] | alt | 13.3 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.59× (z +10.6) | — |
| [[NCI-H2030 (line)]] | alt | 26.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +9.6) | [[Dinaciclib (drug)]] 0.05 µM 0.244× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 14.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.28× (z +10.1) | — |
| [[BT-474 (line)]] | alt | 12.6 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.103× (z -10.8) |
| [[NCI-H1792 (line)]] | alt | 17.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +8.8) | — |
| [[NCI-H460 (line)]] | wt | 11.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +9.4) | — |
| [[PANC-1 (line)]] | alt | 11.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +10.0) | — |
| [[SNU-1 (line)]] | wt | 15.6 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0896× (z -9.2) |
| [[SW 900 (line)]] | alt | 12.8 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM 0.127× (z -10.7) |
| [[A-172 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.34 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.37 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.37 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.56 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.57 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.81 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4110), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF408]] | +0.67 | +0.72 / +0.54 | both halves | 1e-05 |  |
| [[RNF25]] | +0.67 | +0.77 / +0.49 | both halves | 1e-05 | **novel candidate** |
| [[MRPL10]] | +0.64 | +0.82 / +0.43 | both halves | 3e-05 |  |
| [[ZNF7]] | +0.59 | +0.66 / +0.45 | both halves | 3e-05 |  |
| [[TXNDC9]] | +0.58 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[ZNF805]] | +0.58 | +0.60 / +0.44 | both halves | 3e-05 |  |
| [[KCTD10]] | +0.57 | +0.61 / +0.37 | both halves | 8e-05 |  |
| [[NELFE]] | +0.56 | +0.62 / +0.40 | both halves | 5e-05 |  |
| [[TIMM22]] | +0.56 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[ZNF561]] | +0.56 | +0.66 / +0.37 | both halves | 8e-05 |  |
| [[MRPS11]] | +0.56 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[ASCC2]] | +0.55 | +0.65 / +0.36 | both halves | 1e-04 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LUC7L3]] | -0.58 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[NAP1L1]] | -0.55 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[PABPN1]] | -0.51 | -0.44 / -0.43 | both halves | 4e-05 |  |
| [[ATP1B3]] | -0.48 | -0.49 / -0.36 | both halves | 1e-04 |  |
| [[PTMA]] | -0.47 | -0.56 / -0.37 | both halves | 8e-05 |  |
| [[PNISR]] | -0.46 | -0.32 / -0.41 | both halves | 1e-04 |  |
| [[ARL15]] | -0.45 | -0.48 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers EIF2B2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.522). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-48.0, 4.1); signed map (-9.3, -25.3). **Vector** length 63.7, 10.3% of its response variance represented; |z| ≥ 3 in 1,041 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +14.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.8 | +11.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~45% of this change | +3.4 | +4.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.4 | +8.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.2 | +10.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +7.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +7.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.7 | +1.7 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.7 | +4.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.0 | -2.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | +2.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~87% of this change | -2.2 | +3.0 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -2.1 | -3.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -2.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.8 | -2.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.8 | -2.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.7 | -3.4 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -1.5 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation initiation factor 2B subunit beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.3 — chr14:75,002,921-75,012,366 (+) |
| Ensembl biotype | protein_coding |
| Also known as | EIF2B, EIF-2Bbeta, EIF2Bbeta |
| Reactome | 4 pathways, smallest: Recycling of eIF2:GDP; Cap-dependent Translation Initiation; Eukaryotic Translation Initiation |
| Matched by | ensembl_id |

**Function**, from UniProt [P49770](https://www.uniprot.org/uniprotkb/P49770) (Translation initiation factor eIF2B subunit beta):

> Acts as a component of the translation initiation factor 2B (eIF2B) complex, which catalyzes the exchange of GDP for GTP on eukaryotic initiation factor 2 (eIF2) gamma subunit. Its guanine nucleotide exchange factor activity is repressed when bound to eIF2 complex phosphorylated on the alpha subunit, thereby limiting the amount of methionyl-initiator methionine tRNA available to the ribosome and consequently global translation is repressed.

**Summary**, from NCBI Gene [8892](https://www.ncbi.nlm.nih.gov/gene/8892):

> This gene encodes the beta subunit of eukaryotic initiation factor-2B (EIF2B). EIF2B is involved in protein synthesis and exchanges GDP and GTP for its activation and deactivation. [provided by RefSeq, Aug 2011]

**Accessions** — [HGNC:3258](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3258) · Entrez [8892](https://www.ncbi.nlm.nih.gov/gene/8892) · UniProt [P49770](https://www.uniprot.org/uniprotkb/P49770) · Ensembl [ENSG00000119718](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119718)

## Data

Gene col 4110: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4110); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4110, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4110]; `tensor/DDL_lfc|DDL_z.npy` [4110]; `embed/gene_vectors.npy` [4110]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4110 or target_col == 4110). Every well: [[EIF2B2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EIF2B2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
