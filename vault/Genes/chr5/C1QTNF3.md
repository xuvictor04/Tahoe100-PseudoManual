---
symbol: "C1QTNF3"
type: "gene"
col: 1339
ensembl_id: "ENSG00000082196"
name: "C1q and TNF related 3"
location: "5p13.2"
module: 3
arm: "-"
pooled_cpm: 3.72
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 29
n_dd_up_clean: 0
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 8
direction_downstream: 1
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# C1QTNF3

*C1q and TNF related 3* — 5p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.90× (z +4.5, q 0.004, up in 1 of 7 measured lines) ⚠ toxic; transcription drop.
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.327× (z -11.5, q 1e-27, down in 29 of 33 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C1QTNF3-AMACR]] (+0.77, fdr 7e-06, ⚠ read-through risk), [[PMFBP1]] (+0.61, fdr 1e-05), [[LINC01876]] (+0.55, fdr 3e-05), [[BACE1-AS]] (+0.51, fdr 5e-05); moves opposite to [[IL17RA]] (-0.48, fdr 3e-05), [[TAF12]] (-0.48, fdr 3e-04), [[SAMD8]] (-0.48, fdr 1e-04).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[FSIP2-AS1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[C1QTNF3-AMACR]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1339.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.90×** | +4.5 | 0.004 | 1/7 (HT-29) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.61× | +3.5 | 0.14 | 11/42 (NCI-H23, AsPC-1, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.58× | +3.2 | 0.23 | 9/37 (SW480, LoVo, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 12 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1339.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.327×** | -11.5 | 1e-27 | 29/33 (SW 900, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.292×** | -8.9 | 1e-16 | 34/47 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.340×** | -7.8 | 9e-13 | 35/45 (HT-29, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.391×** | -6.8 | 1e-09 | 24/29 (HOP62, COLO 205, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.405×** | -6.6 | 6e-09 | 27/43 (HepG2/C3A, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.530×** | -6.5 | 8e-09 | 25/36 (CFPAC-1, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.398×** | -6.4 | 1e-08 | 28/41 (BT-474, PANC-1, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.445×** | -5.9 | 3e-07 | 24/35 (HOP62, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.446×** | -5.9 | 3e-07 | 28/46 (MIA PaCa-2, A-427, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.440×** | -5.7 | 6e-07 | 15/18 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.458×** | -5.7 | 7e-07 | 23/42 (HT-29, SW 900, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.465×** | -5.5 | 1e-06 | 27/46 (CFPAC-1, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.476×** | -5.4 | 3e-06 | 24/44 (A498, A-427, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.488×** | -5.2 | 8e-06 | 22/42 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.472×** | -5.1 | 1e-05 | 22/40 (HEC-1-A, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.555×** | -4.3 | 7e-04 | 22/42 (HepG2/C3A, HEC-1-A, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.349×** | -4.0 | 0.002 | 19/39 (HT-29, BT-474, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~25% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.586×** | -3.9 | 0.003 | 16/40 (A-172, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.688×** | -3.8 | 0.004 | 15/43 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.411×** | -3.4 | 0.018 | 10/38 (PANC-1, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.640×** | -3.2 | 0.028 | 11/43 (BT-474, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM |  | **0.637×** | -3.1 | 0.038 | 13/43 (SNU-423, HT-29, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Retinoic acid (drug)]] 5 µM |  | **0.745×** | -3.0 | 0.056 | 6/46 (NCI-H1573, SHP-77, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.39 per unit of S-phase module lfc, -0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1339. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 6.37 | 0 | 6 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0246× (z -17.0) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.171× (z -11.5) |
| [[HOP62 (line)]] | alt | 4.12 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0294× (z -12.6) |
| [[HT-29 (line)]] | alt | 5.72 | 0 | 4 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0509× (z -10.6) |
| [[BT-474 (line)]] | alt | 12.6 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.171× (z -9.7) |
| [[HepG2_C3A (line)]] | wt | 8.09 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0335× (z -10.6) |
| [[CFPAC-1 (line)]] | alt | 3.00 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0421× (z -12.3) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0413× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 7.55 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0467× (z -13.5) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.170× (z -11.5) |
| [[PANC-1 (line)]] | alt | 2.32 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0562× (z -10.5) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.180× (z -8.8) |
| [[A-427 (line)]] | wt | 6.38 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0820× (z -9.5) |
| [[A498 (line)]] | wt | 2.95 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0283× (z -11.5) |
| [[COLO 205 (line)]] | alt | 12.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.182× (z -9.3) |
| [[LOX-IMVI (line)]] | wt | 3.64 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0497× (z -9.3) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H23 (line)]] | alt | 6.35 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0608× (z -9.4) |
| [[SHP-77 (line)]] | alt | 17.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.235× (z -9.5) |
| [[SW 900 (line)]] | alt | 4.77 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0544× (z -11.6) |
| [[A-172 (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.984 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.60 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.99 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.937 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.11 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.83 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.74 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1339), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C1QTNF3-AMACR]] | +0.77 | +0.74 / +0.76 | both halves | 7e-06 | ⚠ **readthrough risk**: this gene lies 0.0 kb 3′ of C1QTNF3-AMACR on the same strand (can correlate by spillover, not regulation) |
| [[PMFBP1]] | +0.61 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[LINC01876]] | +0.55 | +0.54 / +0.46 | both halves | 3e-05 |  |
| [[BACE1-AS]] | +0.51 | +0.39 / +0.46 | both halves | 5e-05 |  |
| [[SPATA17]] | +0.51 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[AIG1]] | +0.50 | +0.47 / +0.37 | both halves | 8e-05 |  |
| [[SORL1]] | +0.48 | +0.50 / +0.39 | both halves | 6e-05 |  |
| [[MIR4500HG]] | +0.48 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[HNRNPDL]] | +0.48 | +0.28 / +0.48 | both halves | 3e-04 |  |
| [[MAP2K6]] | +0.48 | +0.43 / +0.36 | both halves | 9e-05 |  |
| [[PDK2]] | +0.48 | +0.48 / +0.34 | both halves | 1e-04 |  |
| [[TBL1XR1]] | +0.46 | +0.44 / +0.41 | both halves | 4e-05 |  |
| [[HNRNPD]] | +0.46 | +0.40 / +0.41 | both halves | 5e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IL17RA]] | -0.48 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[TAF12]] | -0.48 | -0.27 / -0.41 | both halves | 3e-04 |  |
| [[SAMD8]] | -0.48 | -0.54 / -0.34 | both halves | 1e-04 |  |
| [[GLTP]] | -0.48 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[PAQR7]] | -0.47 | -0.32 / -0.48 | both halves | 2e-04 |  |
| [[DENR]] | -0.47 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[SERPINB6]] | -0.47 | -0.28 / -0.47 | both halves | 3e-04 |  |
| [[ZSWIM3]] | -0.47 | -0.25 / -0.42 | both halves | 4e-04 |  |
| [[TUBGCP5]] | -0.46 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[TRNAU1AP]] | -0.46 | -0.32 / -0.45 | both halves | 2e-04 |  |
| [[FBXO28]] | -0.46 | -0.36 / -0.39 | both halves | 9e-05 |  |
| [[PLEKHH1]] | -0.45 | -0.41 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FSIP2-AS1]] | B | FSIP2-AS1 activity raises C1QTNF3's level | lines that do not express FSIP2-AS1 (6) vs lines expressing it (44) | 1.99× lower at baseline in the lines without FSIP2-AS1 | 0.028 | ⚠ within organs, on part of the lines; also absent: PMFBP1, SPATA17, ENSG00000287621; maybe low, not absent |
| [[LINC01876]] | B | LINC01876 activity strengthens C1QTNF3's drug response | lines that do not express LINC01876 (23) vs lines expressing it (24) | the lines without LINC01876 respond 0.65× as strongly (z diff +1.35); strongest at Homoharringtonine 5 µM: 0.49x vs 0.26x (z diff +3.2) | 0.033 | ⚠ within organs, on part of the lines; also absent: TOX3, TFF1, TMEM45B; target measured in part of the lines; artifact flags |
| [[MROH7]] | B | MROH7 activity raises C1QTNF3's level | lines that do not express MROH7 (15) vs lines expressing it (35) | 1.25× lower at baseline in the lines without MROH7 | 0.051 | ⚠ within organs, on part of the lines; also absent: ACOT11, PLEKHG1, FCGRT; maybe low, not absent |
| [[LINC01876]] | B | LINC01876 activity raises C1QTNF3's level | lines that do not express LINC01876 (24) vs lines expressing it (26) | 1.47× lower at baseline in the lines without LINC01876 | 0.060 | ⚠ within organs, on part of the lines; also absent: TOX3, TFF1, TMEM45B |
| [[FMN1]] | B | FMN1 activity raises C1QTNF3's level | lines that do not express FMN1 (17) vs lines expressing it (33) | 1.26× lower at baseline in the lines without FMN1 | 0.061 | ⚠ within organs, on part of the lines; also absent: ENSG00000278266, LINC02405, ENSG00000286016; maybe low, not absent |
| [[SORL1]] | B | SORL1 activity raises C1QTNF3's level | lines that do not express SORL1 (21) vs lines expressing it (29) | 1.46× lower at baseline in the lines without SORL1 | 0.074 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PLEKHG6, SLC52A3 |
| [[PKHD1]] | B | PKHD1 activity raises C1QTNF3's level | lines that do not express PKHD1 (25) vs lines expressing it (25) | 1.44× lower at baseline in the lines without PKHD1 | 0.094 | ⚠ within organs, on part of the lines; also absent: ENSG00000231317, SLC30A10, SLC24A3; maybe low, not absent |
| [[C1QTNF3-AMACR]] | C | C1QTNF3-AMACR's natural level strengthens C1QTNF3's drug response | C1QTNF3-AMACR's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.71, reverse +0.75; direction not clear | 0.013 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C1QTNF3-AMACR]] | C | C1QTNF3's natural level strengthens C1QTNF3-AMACR's drug response | C1QTNF3's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.75, reverse +0.71; direction not clear | 0.002 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.247). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-22.4, 32.7); signed map (41.6, -12.1). **Vector** length 57.9, 8.39% of its response variance represented; |z| ≥ 3 in 1,229 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.7 | +2.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.8 | +0.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +4.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.4 | -0.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +2.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.3 | +3.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.3 | +1.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.3 | +2.1 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.1 | +3.5 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -3.4 | -5.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.3 | -11.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -2.3 | -5.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -2.1 | -3.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.8 | -5.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.4 | -2.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -0.6 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | -1.4 | +0.3 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.4 | -0.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.3 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | C1q and TNF related 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p13.2 — chr5:34,017,858-34,043,213 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CTRP3, Cors, Corcs, 2310005P21Rik, Cors-26 |
| Gene groups (HGNC) | C1q and TNF related |
| Matched by | ensembl_id |

UniProt [Q9BXJ4](https://www.uniprot.org/uniprotkb/Q9BXJ4) carries no function annotation.

**Summary**, from NCBI Gene [114899](https://www.ncbi.nlm.nih.gov/gene/114899):

> Enables identical protein binding activity. Involved in several processes, including intracellular triglyceride homeostasis; negative regulation of non-canonical NF-kappaB signal transduction; and regulation of cytokine production. Acts upstream of or within negative regulation of gluconeogenesis. Located in extracellular exosome and membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:14326](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14326) · Entrez [114899](https://www.ncbi.nlm.nih.gov/gene/114899) · UniProt [Q9BXJ4](https://www.uniprot.org/uniprotkb/Q9BXJ4) · Ensembl [ENSG00000082196](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000082196)

## Data

Gene col 1339: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1339); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1339, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1339]; `tensor/DDL_lfc|DDL_z.npy` [1339]; `embed/gene_vectors.npy` [1339]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1339 or target_col == 1339). Every well: [[C1QTNF3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C1QTNF3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
