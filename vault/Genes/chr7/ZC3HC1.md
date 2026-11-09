---
symbol: "ZC3HC1"
type: "gene"
col: 1676
ensembl_id: "ENSG00000091732"
name: "zinc finger C3HC-type containing 1"
location: "7q32.2"
module: 114
arm: "+"
pooled_cpm: 22.58
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 13
n_dd_up_clean: 17
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/114"]
generated_by: "tahoemap"
---

# ZC3HC1

*zinc finger C3HC-type containing 1* — 7q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.83× (z +17.5, q 0e+00, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.666× (z -8.3, q 5e-14, down in 23 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 0.674× (z -8.1, q 1e-13, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLR3C]] (+0.79, fdr 7e-06), [[MAU2]] (+0.77, fdr 7e-06), [[ALKBH1]] (+0.77, fdr 7e-06); moves opposite to [[SETD3]] (-0.70, fdr 7e-06), [[PAPSS1]] (-0.65, fdr 1e-05), [[TM9SF2]] (-0.63, fdr 1e-05).
> It is in [[Module 114]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CCDC102A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1676.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.83×** | +17.5 | 0e+00 | 41/47 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.99×** | +13.5 | 6e-39 | 41/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.91×** | +13.2 | 2e-37 | 40/47 (A-427, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.48×** | +11.4 | 6e-28 | 38/48 (LoVo, PANC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.54×** | +8.9 | 8e-17 | 32/48 (NCI-H1573, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.52×** | +8.6 | 8e-16 | 37/48 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +8.4 | 5e-15 | 27/45 (KATO III, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.47×** | +7.4 | 1e-11 | 29/48 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.43×** | +7.2 | 3e-11 | 28/46 (KATO III, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.35×** | +6.2 | 4e-08 | 26/48 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.35×** | +6.1 | 5e-08 | 22/48 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.33×** | +5.5 | 1e-06 | 19/48 (PANC-1, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.30×** | +5.4 | 3e-06 | 21/48 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +4.8 | 7e-05 | 13/48 (PANC-1, HOP62, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.27×** | +4.5 | 2e-04 | 14/47 (A498, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.26×** | +4.4 | 3e-04 | 15/48 (HOP62, HS-578T, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.25×** | +4.3 | 6e-04 | 17/48 (BT-474, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 8 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1676.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.666×** | -8.3 | 5e-14 | 23/43 (KATO III, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.649×** | -8.2 | 8e-14 | 18/40 (SHP-77, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.674×** | -8.1 | 1e-13 | 27/48 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.701×** | -7.0 | 4e-10 | 17/33 (NCI-H23, Hs 766T, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.718×** | -6.8 | 1e-09 | 26/48 (SW480, HOP62, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.741×** | -5.8 | 7e-07 | 22/48 (NCI-H1792, NCI-H23, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.748×** | -5.7 | 8e-07 | 23/47 (SHP-77, PANC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.823×** | -5.7 | 1e-06 | 20/48 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.761×** | -5.6 | 1e-06 | 22/48 (NCI-H460, NCI-H23, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.774×** | -4.9 | 4e-05 | 20/48 (NCI-H23, HS-578T, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.794×** | -4.6 | 3e-04 | 19/48 (SK-MEL-2, RKO, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.657×** | -4.5 | 3e-04 | 14/48 (SK-MEL-2, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.811×** | -4.2 | 0.001 | 18/47 (SW1417, NCI-H1792, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.944× | -4.0 | 0.003 | 0/48 | inconsistent across doses |  |
| [[Artemether (drug)]] 0.05 µM |  | 0.851× | -3.3 | 0.035 | 12/48 (SW1417, LoVo, …) | inconsistent across doses |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM |  | 0.854× | -3.2 | 0.042 | 12/48 (Hs 766T, SW 900, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1676. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 28.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +12.2) | — |
| [[PANC-1 (line)]] | alt | 22.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +12.5) | — |
| [[C32 (line)]] | wt | 49.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.256× (z -10.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 21.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.0834× (z -18.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 11.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.216× (z -9.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 23.8 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.173× (z -11.5) ⚠ toxic |
| [[A-427 (line)]] | wt | 22.3 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.95× (z +10.6) | — |
| [[C-33 A (line)]] | alt | 37.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.148× (z -13.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 17.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.238× (z -9.9) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 15.8 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0933× (z -11.0) |
| [[HEC-1-A (line)]] | alt | 21.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.279× (z -9.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 20.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.162× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[hTERT-HPNE (line)]] | wt | 14.3 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.0691× (z -10.9) |
| [[NCI-H1792 (line)]] | alt | 26.5 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.259× (z -9.5) ⚠ cell-cycle shift, explains ~20% of this change |
| [[NCI-H2030 (line)]] | alt | 23.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +12.4) | — |
| [[NCI-H23 (line)]] | alt | 59.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.285× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[NCI-H2347 (line)]] | alt | 13.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +8.8) | — |
| [[RKO (line)]] | wt | 36.5 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -10.4) ⚠ cell-cycle shift, explains ~36% of this change |
| [[SK-MEL-2 (line)]] | alt | 32.1 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -9.6) ⚠ cell-cycle shift, explains ~36% of this change |
| [[SW1417 (line)]] | alt | 21.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.309× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[SW48 (line)]] | wt | 17.4 | 0 | 1 | — | [[Bimatoprost (drug)]] 0.5 µM 0.127× (z -9.2) |
| [[SW480 (line)]] | alt | 27.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +8.7) | — |
| [[A-172 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1676), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR3C]] | +0.79 | +0.74 / +0.70 | both halves | 7e-06 |  |
| [[MAU2]] | +0.77 | +0.78 / +0.69 | both halves | 7e-06 |  |
| [[ALKBH1]] | +0.77 | +0.73 / +0.79 | both halves | 7e-06 |  |
| [[ZNF721]] | +0.76 | +0.79 / +0.60 | both halves | 7e-06 |  |
| [[MAPK1IP1L]] | +0.75 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[ABRAXAS2]] | +0.75 | +0.75 / +0.75 | both halves | 7e-06 |  |
| [[ZCCHC10]] | +0.75 | +0.79 / +0.61 | both halves | 7e-06 |  |
| [[RPAP1]] | +0.75 | +0.77 / +0.65 | both halves | 7e-06 |  |
| [[THUMPD2]] | +0.74 | +0.73 / +0.74 | both halves | 7e-06 |  |
| [[GMEB2]] | +0.74 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[SLC9A8]] | +0.73 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[LATS1]] | +0.73 | +0.67 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SETD3]] | -0.70 | -0.65 / -0.68 | both halves | 7e-06 |  |
| [[PAPSS1]] | -0.65 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[TM9SF2]] | -0.63 | -0.65 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC102A]] | B | CCDC102A activity raises ZC3HC1's level | lines that do not express CCDC102A (5) vs lines expressing it (45) | 1.50× lower at baseline in the lines without CCDC102A | 0.073 | ⚠ within organs, on part of the lines; also absent: CYP46A1, TMOD2, DPF1; maybe low, not absent |
| [[CTSB]] | C | CTSB activity lowers ZC3HC1's level | lines that do not express CTSB (3) vs lines expressing it (47) | 1.85× higher at baseline in the lines without CTSB | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: FUCA2, AIFM2, TRAF3IP2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 114]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.833). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-40.5, 7.1); signed map (-3.0, -15.0). **Vector** length 104, 23.6% of its response variance represented; |z| ≥ 3 in 981 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.0 | +17.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.0 | +13.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +7.4 | +8.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +7.4 | +11.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.3 | +13.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.0 | +6.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +4.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.6 | +4.5 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.5 | +2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.3 | +4.4 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.5 | -5.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -5.2 | -6.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.2 | -8.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -4.4 | -5.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.0 | -4.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.5 | -4.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -5.7 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -2.3 | -2.6 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -2.1 | -2.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.0 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger C3HC-type containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q32.2 — chr7:130,018,287-130,051,401 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NIPA |
| Gene groups (HGNC) | Zinc fingers |
| Reactome | 4 pathways, smallest: Nuclear events stimulated by ALK signaling in cancer; Signaling by ALK fusions and activated point mutants; Signaling by ALK in cancer |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86WB0](https://www.uniprot.org/uniprotkb/Q86WB0) (Zinc finger C3HC-type protein 1):

> Required for proper positioning of a substantial amount of TPR at the nuclear basket (NB) through interaction with TPR.

**Summary**, from NCBI Gene [51530](https://www.ncbi.nlm.nih.gov/gene/51530):

> This gene encodes an F-box-containing protein that is a component of an SCF-type E3 ubiquitin ligase complex that regulates the onset of cell division. The G2/M transition in the cell cycle requires the interaction of the proteins cyclin B1 and cyclin-dependent kinase 1. The activated ubiquitin ligase complex targets the protein cyclin B1 for degradation, preventing this transition to mitosis. [provided by RefSeq, Aug 2013]

**Accessions** — [HGNC:29913](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29913) · Entrez [51530](https://www.ncbi.nlm.nih.gov/gene/51530) · UniProt [Q86WB0](https://www.uniprot.org/uniprotkb/Q86WB0) · Ensembl [ENSG00000091732](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000091732)

## Data

Gene col 1676: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1676); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1676, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1676]; `tensor/DDL_lfc|DDL_z.npy` [1676]; `embed/gene_vectors.npy` [1676]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1676 or target_col == 1676). Every well: [[ZC3HC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZC3HC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
