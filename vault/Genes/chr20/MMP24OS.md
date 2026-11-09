---
symbol: "MMP24OS"
type: "gene"
col: 4708
ensembl_id: "ENSG00000126005"
name: "MMP24 opposite strand"
location: "20q11.22"
module: 37
arm: "+"
pooled_cpm: 71.74
n_lines_expressing: 48
n_dd_up: 6
n_dd_down: 17
n_dd_up_clean: 3
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# MMP24OS

*MMP24 opposite strand* — 20q11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.41× (z +6.1, q 5e-07, up in 27 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM: 1.31× (z +4.8, q 4e-04, up in 31 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.430× (z -21.2, q 0e+00, down in 38 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CLEC4A]] (+0.58, fdr 1e-05), [[TPT1-AS1]] (+0.58, fdr 1e-05), [[SMBD1P]] (+0.57, fdr 1e-05); moves opposite to [[DCLRE1A]] (-0.51, fdr 2e-05), [[NSMCE4A]] (-0.51, fdr 2e-05), [[C2CD5]] (-0.49, fdr 4e-05).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LINC02656]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4708.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.41×** | +6.1 | 5e-07 | 27/47 (RKO, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.31×** | +4.8 | 4e-04 | 31/47 (KATO III, LS 180, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.29×** | +4.5 | 0.001 | 22/46 (RKO, SW 1271, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.16× | +3.8 | 0.023 | 13/46 (A498, SW480, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.6 | 0.037 | 22/47 (A498, LOX-IMVI, …) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.22×** | +3.5 | 0.046 | 17/46 (NCI-H2030, PANC-1, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.44×** | +3.4 | 0.052 | 15/46 (A498, HOP62, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.14× | +3.3 | 0.066 | 15/47 (LS 180, Hs 766T, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.22×** | +3.3 | 0.066 | 17/41 (HepG2/C3A, SW48, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4708.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.430×** | -21.2 | 0e+00 | 38/45 (BT-474, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.394×** | -16.5 | 0e+00 | 42/45 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.401×** | -15.6 | 0e+00 | 42/45 (BT-474, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.556×** | -10.4 | 4e-23 | 37/46 (SW480, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.549×** | -10.2 | 2e-22 | 32/45 (J82, H4, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.583×** | -9.5 | 1e-19 | 38/46 (BT-474, SW480, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.623×** | -8.4 | 4e-15 | 34/46 (SW480, HT-29, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.629×** | -8.2 | 2e-14 | 34/46 (BT-474, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.651×** | -7.6 | 2e-12 | 35/46 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.657×** | -7.4 | 6e-12 | 37/46 (BT-474, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.692×** | -6.2 | 4e-08 | 31/46 (HT-29, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.535×** | -5.8 | 3e-07 | 29/45 (BT-474, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.537×** | -5.8 | 4e-07 | 27/42 (H4, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.551×** | -5.5 | 1e-06 | 26/47 (HT-29, BT-474, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.738×** | -5.4 | 3e-06 | 27/46 (BT-474, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.781×** | -4.4 | 4e-04 | 21/46 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[Asciminib (drug)]] 0.05 µM |  | 0.842× | -3.0 | 0.076 | 13/46 (HepG2/C3A, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4708. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 321 | 0 | 15 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0773× (z -41.9) |
| [[SW480 (line)]] | alt | 106 | 0 | 11 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.218× (z -19.8) |
| [[HT-29 (line)]] | alt | 158 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -29.1) |
| [[KATO III (line)]] | alt | 175 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -30.7) |
| [[HOP62 (line)]] | alt | 72.1 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -16.0) |
| [[NCI-H460 (line)]] | wt | 59.1 | 0 | 7 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.183× (z -17.2) |
| [[H4 (line)]] | wt | 87.9 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -12.1) |
| [[J82 (line)]] | alt | 88.0 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -13.5) |
| [[COLO 205 (line)]] | alt | 137 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -23.3) |
| [[HCT15 (line)]] | alt | 137 | 0 | 5 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.203× (z -12.3) |
| [[HEC-1-A (line)]] | alt | 95.1 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -21.2) |
| [[LOX-IMVI (line)]] | wt | 47.3 | 1 (1 ⚠) | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +10.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Harringtonine (drug)]] 5 µM 0.291× (z -11.0) |
| [[Panc 03.27 (line)]] | alt | 78.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -16.1) |
| [[RPMI-7951 (line)]] | alt | 124 | 0 | 4 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.273× (z -11.7) |
| [[A549 (line)]] | wt | 53.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -22.6) |
| [[C32 (line)]] | wt | 60.0 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.277× (z -12.6) |
| [[LS 180 (line)]] | wt | 66.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -15.9) |
| [[NCI-H23 (line)]] | alt | 61.2 | 1 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.93× (z +8.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.288× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 62.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -18.0) |
| [[SW 900 (line)]] | alt | 62.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -15.7) |
| [[A498 (line)]] | wt | 46.9 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.55× (z +11.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[AsPC-1 (line)]] | alt | 61.0 | 1 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +10.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -11.9) |
| [[CFPAC-1 (line)]] | alt | 81.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -20.8) |
| [[Hs 766T (line)]] | wt | 101 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.471× (z -10.0) |
| [[hTERT-HPNE (line)]] | wt | 68.5 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.278× (z -10.1) |
| [[NCI-H1573 (line)]] | alt | 60.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.423× (z -10.7) |
| [[NCI-H1792 (line)]] | alt | 69.2 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.284× (z -11.5) |
| [[NCI-H2030 (line)]] | alt | 90.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -10.5) |
| [[PANC-1 (line)]] | alt | 49.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -15.9) |
| [[SNU-1 (line)]] | wt | 58.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -11.2) |
| [[C-33 A (line)]] | alt | 45.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.287× (z -8.9) |
| [[LoVo (line)]] | wt | 26.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.69× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2347 (line)]] | alt | 31.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -13.9) |
| [[SK-MEL-2 (line)]] | alt | 43.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.271× (z -9.1) ⚠ toxic |
| [[SW1417 (line)]] | alt | 44.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.469× (z -10.0) |
| [[SW48 (line)]] | wt | 60.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -12.1) |
| [[A-172 (line)]] | wt | 50.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 14.7 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 75.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 67.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 65.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.7 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 98.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 180 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4708), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLEC4A]] | +0.58 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[TPT1-AS1]] | +0.58 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[SMBD1P]] | +0.57 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[MUC20-OT1]] | +0.57 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[PIWIL2]] | +0.56 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[TMEM269]] | +0.56 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[ZNF586]] | +0.56 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[ADAM20P1]] | +0.56 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[TNXB]] | +0.56 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[LINC02649]] | +0.55 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[TMED7-TICAM2]] | +0.55 | +0.43 / +0.61 | both halves | 3e-05 |  |
| [[C9orf153]] | +0.55 | +0.51 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCLRE1A]] | -0.51 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[NSMCE4A]] | -0.51 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[C2CD5]] | -0.49 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[MDM1]] | -0.47 | -0.28 / -0.58 | both halves | 3e-04 |  |
| [[SSX2IP]] | -0.46 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[NBN]] | -0.46 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[USP1]] | -0.45 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[AKAP7]] | -0.45 | -0.41 / -0.55 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02656]] | C | LINC02656 activity raises MMP24OS's level | lines that do not express LINC02656 (4) vs lines expressing it (46) | 2.38× lower at baseline in the lines without LINC02656 | 0.025 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC02649, MAP3K8, ENSG00000250842; maybe low, not absent |
| [[LINC02649]] | C | LINC02649 activity raises MMP24OS's level | lines that do not express LINC02649 (3) vs lines expressing it (47) | 2.44× lower at baseline in the lines without LINC02649 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MAP3K8, LINC02656, B4GALT1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.628). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.3, -19.8); signed map (9.9, 7.3). **Vector** length 95.8, 25.9% of its response variance represented; |z| ≥ 3 in 1,125 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.3 | +4.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +4.0 | +4.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.6 | +1.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | +3.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.1 | +1.2 |
|  | [[Belzutifan (drug)]] 5 µM |  | +2.3 | +2.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.1 | +2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +3.8 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -4.9 | -15.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.4 | -7.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.4 | -10.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.8 | -16.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | -8.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.6 | -1.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.2 | -0.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -2.2 | -2.4 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.0 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | MMP24 opposite strand |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.22 — chr20:35,201,745-35,278,131 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously MMP24-AS1 |
| Matched by | ensembl_id |

UniProt [A0A0U1RRL7](https://www.uniprot.org/uniprotkb/A0A0U1RRL7) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:44421](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44421) · Entrez [101410538](https://www.ncbi.nlm.nih.gov/gene/101410538) · UniProt [A0A0U1RRL7](https://www.uniprot.org/uniprotkb/A0A0U1RRL7) · Ensembl [ENSG00000126005](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126005)

## Data

Gene col 4708: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4708); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4708, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4708]; `tensor/DDL_lfc|DDL_z.npy` [4708]; `embed/gene_vectors.npy` [4708]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4708 or target_col == 4708). Every well: [[MMP24OS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MMP24OS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
