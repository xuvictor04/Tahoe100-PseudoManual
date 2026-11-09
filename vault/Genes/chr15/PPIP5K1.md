---
symbol: "PPIP5K1"
type: "gene"
col: 9698
ensembl_id: "ENSG00000168781"
name: "diphosphoinositol pentakisphosphate kinase 1"
location: "15q15.3"
module: 43
arm: "+"
pooled_cpm: 20.38
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 7
n_dd_up_clean: 13
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# PPIP5K1

*diphosphoinositol pentakisphosphate kinase 1* — 15q15.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.60× (z +9.2, q 3e-17, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.608× (z -9.4, q 4e-18, down in 22 of 30 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.692× (z -7.2, q 7e-11, down in 28 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CATSPER2]] (+0.82, fdr 7e-06, ⚠ same locus), [[RPL36]] (+0.62, fdr 7e-05), [[MAP2K7]] (+0.60, fdr 1e-05), [[EML2]] (+0.60, fdr 4e-05); moves opposite to [[EIF4G2]] (-0.67, fdr 1e-05), [[MOB1A]] (-0.65, fdr 3e-05), [[ADI1]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[GLUL]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9698.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.60×** | +9.2 | 3e-17 | 35/48 (A498, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.58×** | +8.9 | 2e-16 | 30/48 (LS 180, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.37×** | +8.6 | 1e-15 | 30/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.50×** | +7.9 | 4e-13 | 31/47 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.42×** | +6.9 | 8e-10 | 30/48 (LS 180, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.36×** | +5.9 | 3e-07 | 21/46 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +5.7 | 1e-06 | 22/42 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.71×** | +5.5 | 3e-06 | 16/48 (LoVo, LS 180, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.44×** | +5.1 | 2e-05 | 20/44 (MIA PaCa-2, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~2% of this change | 1.20× | +5.0 | 4e-05 | 19/47 (NCI-H460, NCI-H23, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.24×** | +4.2 | 0.001 | 17/46 (LS 180, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.23×** | +4.1 | 0.002 | 11/47 (KATO III, HS-578T, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.23×** | +4.0 | 0.002 | 17/47 (RPMI-7951, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.21×** | +3.4 | 0.024 | 10/47 (C32, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.19× | +3.4 | 0.027 | 8/48 (BT-474, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 0.5 µM |  | **1.27×** | +3.3 | 0.031 | 3/48 (LS 180, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | 1.19× | +3.3 | 0.035 | 4/47 (Panc 03.27, A-427, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9698.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.608×** | -9.4 | 4e-18 | 22/30 (LoVo, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.620×** | -9.0 | 6e-17 | 29/41 (NCI-H460, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.669×** | -7.3 | 6e-11 | 21/34 (HT-29, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.692×** | -7.2 | 7e-11 | 28/47 (SW480, HepG2/C3A, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.728×** | -6.0 | 2e-07 | 22/48 (RKO, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.761×** | -5.2 | 2e-05 | 23/46 (HEC-1-A, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.782×** | -4.8 | 1e-04 | 15/46 (hTERT-HPNE, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.872× | -3.8 | 0.010 | 18/48 (J82, HEC-1-A, …) | top dose only | low cells (technical?) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 0.834× | -3.6 | 0.023 | 19/47 (LoVo, LS 180, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 0.842× | -3.4 | 0.040 | 4/48 (SW 1088, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9698. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 13.6 | 3 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +13.1) ⚠ cell-cycle shift, explains ~2% of this change | [[Niclosamide (olamine) (drug)]] 5 µM 0.194× (z -13.3) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 41.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -12.1) ⚠ cell-cycle shift, explains ~2% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.414× (z -8.9) |
| [[SW1417 (line)]] | alt | 46.6 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.423× (z -11.6) ⚠ cell-cycle shift, explains ~29% of this change |
| [[A-172 (line)]] | wt | 15.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.221× (z -9.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 41.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.264× (z -13.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 25.7 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.37× (z +9.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A-427 (line)]] | wt | 14.3 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.33× (z +9.6) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[HCT15 (line)]] | alt | 40.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.184× (z -11.6) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 7.72 | 0 | 1 | — | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM 0.0883× (z -10.1) |
| [[HT-29 (line)]] | alt | 29.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.212× (z -11.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 13.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.167× (z -10.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 16.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.232× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 18.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +12.6) ⚠ cell-cycle shift, explains ~2% of this change | — |
| [[Panc 03.27 (line)]] | alt | 22.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.298× (z -8.6) ⚠ toxic |
| [[RKO (line)]] | wt | 25.9 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.238× (z -9.2) |
| [[RPMI-7951 (line)]] | alt | 29.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.112× (z -13.4) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 30.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.193× (z -8.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.33 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.78 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.07 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9698), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 11 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CATSPER2]] | +0.82 | +0.79 / +0.82 | both halves | 7e-06 | STRING 930; ⚠ same locus (38.3 kb, same strand: neighbours can correlate without regulation) |
| [[RPL36]] | +0.62 | +0.37 / +0.66 | both halves | 7e-05 |  |
| [[MAP2K7]] | +0.60 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[RPL18]] ⚠ | +0.60 | +0.40 / +0.61 | both halves | 5e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[EML2]] | +0.60 | +0.42 / +0.61 | both halves | 4e-05 |  |
| [[TOMM7]] | +0.60 | +0.36 / +0.59 | both halves | 9e-05 |  |
| [[SNHG6]] | +0.59 | +0.42 / +0.66 | both halves | 4e-05 |  |
| [[RPL36AL]] ⚠ | +0.59 | +0.43 / +0.58 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[COX17]] | +0.59 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[USP42]] | +0.58 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[C4orf48]] | +0.58 | +0.39 / +0.58 | both halves | 6e-05 |  |
| [[ATP5MJ]] | +0.58 | +0.37 / +0.58 | both halves | 9e-05 |  |
| [[LIN7B]] | +0.58 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[ATP5MC2]] | +0.58 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[DENND6B]] | +0.58 | +0.43 / +0.55 | both halves | 3e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4G2]] | -0.67 | -0.49 / -0.70 | both halves | 1e-05 |  |
| [[MOB1A]] | -0.65 | -0.45 / -0.71 | both halves | 3e-05 |  |
| [[ADI1]] | -0.62 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[AP2M1]] | -0.59 | -0.53 / -0.66 | both halves | 1e-05 |  |
| [[DR1]] | -0.58 | -0.41 / -0.60 | both halves | 4e-05 |  |
| [[ZNF460]] | -0.58 | -0.39 / -0.63 | both halves | 5e-05 |  |
| [[CAPRIN1]] | -0.57 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[PSME3]] | -0.57 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[NXT2]] | -0.57 | -0.38 / -0.58 | both halves | 6e-05 |  |
| [[U2AF2]] | -0.56 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[HNRNPK]] | -0.55 | -0.43 / -0.58 | both halves | 3e-05 |  |
| [[TUG1]] | -0.55 | -0.30 / -0.57 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GLUL]] | B | GLUL activity raises PPIP5K1's level | lines that do not express GLUL (10) vs lines expressing it (40) | 1.39× lower at baseline in the lines without GLUL | 0.083 | ⚠ within organs, on part of the lines |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.470). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-34.2, -22.4); signed map (-57.5, -1.9). **Vector** length 88.8, 17.4% of its response variance represented; |z| ≥ 3 in 894 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 0.5 µM |  | +4.3 | +5.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +8.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.9 | +6.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +5.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.8 | +3.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.2 | +3.2 |
|  | [[Brivudine (drug)]] 0.5 µM |  | +2.0 | +3.3 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -6.3 | -9.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.6 | -6.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.9 | -5.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.1 | -7.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.9 | -2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.8 | -7.2 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.7 | -2.2 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.5 | -2.8 |
|  | [[Benproperine (phosphate) (drug)]] 0.05 µM |  | -1.4 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | diphosphoinositol pentakisphosphate kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.3 — chr15:43,533,462-43,590,208 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0377, IPS1, VIP1; previously HISPPD2A |
| Gene groups (HGNC) | Diphosphoinositol pentakisphosphate kinase family |
| Reactome | 2 pathways, smallest: Synthesis of pyrophosphates in the cytosol; Inositol phosphate metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6PFW1](https://www.uniprot.org/uniprotkb/Q6PFW1) (Inositol hexakisphosphate and diphosphoinositol-pentakisphosphate kinase 1):

> Bifunctional inositol kinase that acts in concert with the IP6K kinases IP6K1, IP6K2 and IP6K3 to synthesize the diphosphate group-containing inositol pyrophosphates diphosphoinositol pentakisphosphate, PP-InsP5, and bis-diphosphoinositol tetrakisphosphate, (PP)2-InsP4. PP-InsP5 and (PP)2-InsP4, also respectively called InsP7 and InsP8, regulate a variety of cellular processes, including apoptosis, vesicle trafficking, cytoskeletal dynamics, exocytosis, insulin signaling and neutrophil …

**Summary**, from NCBI Gene [9677](https://www.ncbi.nlm.nih.gov/gene/9677):

> This gene encodes a dual functional inositol kinase. The encoded enzyme converts inositol hexakisphosphate to diphosphoinositol pentakisphosphate and diphosphoinositol pentakisphosphate to bis-diphosphoinositol tetrakisphosphate. This protein may be important for intracellular signaling pathways. Alternate splicing results in multiple transcript variants. A pseudogene of this gene is found on chromosome 15.[provided by RefSeq, Jun 2010]

**Accessions** — [HGNC:29023](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29023) · Entrez [9677](https://www.ncbi.nlm.nih.gov/gene/9677) · UniProt [Q6PFW1](https://www.uniprot.org/uniprotkb/Q6PFW1) · Ensembl [ENSG00000168781](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168781)

## Data

Gene col 9698: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9698); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9698, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9698]; `tensor/DDL_lfc|DDL_z.npy` [9698]; `embed/gene_vectors.npy` [9698]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9698 or target_col == 9698). Every well: [[PPIP5K1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPIP5K1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
