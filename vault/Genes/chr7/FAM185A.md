---
symbol: "FAM185A"
type: "gene"
col: 13332
ensembl_id: "ENSG00000222011"
name: "family with sequence similarity 185 member A"
location: "7q22.1"
module: 15
arm: "+"
pooled_cpm: 12.94
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 13
n_dd_up_clean: 13
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# FAM185A

*family with sequence similarity 185 member A* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.59× (z +7.6, q 2e-11, up in 27 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.403× (z -10.4, q 1e-22, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CSNK1G1]] (+0.60, fdr 5e-05), [[GPALPP1]] (+0.59, fdr 1e-05), [[TMEM68]] (+0.59, fdr 7e-05); moves opposite to [[NCAM1]] (-0.52, fdr 5e-04), [[ATP1A3]] (-0.52, fdr 1e-04), [[ALAS1]] (-0.52, fdr 1e-04).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13332.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +7.6 | 2e-11 | 27/45 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.57×** | +7.4 | 5e-11 | 33/48 (A498, NCI-H2347, …) | rises with dose | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +6.7 | 5e-09 | 29/46 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.67×** | +5.9 | 6e-07 | 29/48 (LoVo, LS 180, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.63×** | +5.6 | 2e-06 | 25/48 (Hs 766T, A-172, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.48×** | +4.5 | 6e-04 | 26/47 (HT-29, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +4.5 | 6e-04 | 20/48 (A-172, A549, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.44×** | +4.2 | 0.002 | 15/47 (A498, RKO, …) | two highest doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.47×** | +3.5 | 0.025 | 16/48 (CFPAC-1, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +3.4 | 0.043 | 17/46 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.26×** | +3.3 | 0.043 | 12/48 (LS 180, SW480, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.40×** | +3.3 | 0.043 | 14/46 (A549, A498, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 0.05 µM |  | **1.35×** | +3.2 | 0.053 | 7/48 (SW480, H4, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.32×** | +3.2 | 0.060 | 8/47 (LoVo, SNU-423, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.65×** | +3.0 | 0.100 | 8/48 (HT-29, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13332.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.403×** | -10.4 | 1e-22 | 40/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.410×** | -10.2 | 6e-22 | 35/46 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.688×** | -6.0 | 3e-07 | 23/44 (C32, A-172, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.601×** | -5.8 | 9e-07 | 29/47 (SNU-423, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.536×** | -5.7 | 1e-06 | 26/47 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~21% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.597×** | -5.7 | 1e-06 | 24/47 (NCI-H460, SNU-423, …) | rises with dose | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.550×** | -5.5 | 3e-06 | 23/46 (SW480, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.654×** | -4.7 | 2e-04 | 21/41 (LoVo, SK-MEL-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.650×** | -3.9 | 0.005 | 18/48 (HEC-1-A, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.519×** | -3.9 | 0.005 | 14/34 (HEC-1-A, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.681×** | -3.7 | 0.010 | 14/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.726×** | -3.6 | 0.013 | 14/45 (RPMI-7951, C32, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.741×** | -3.4 | 0.028 | 17/48 (SW1417, BT-474, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.57 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13332. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 22.4 | 2 | 4 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.23× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -16.2) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 14.1 | 2 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.74× (z +12.4) | [[Digitoxin (drug)]] 5 µM 0.128× (z -13.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 17.6 | 1 | 2 (2 ⚠) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 3.18× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -12.0) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 13.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.52× (z +12.8) | — |
| [[A549 (line)]] | wt | 12.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.47× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -9.1) ⚠ cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 17.3 | 0 | 2 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0922× (z -10.9) |
| [[PANC-1 (line)]] | alt | 13.9 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.186× (z -12.6) |
| [[SW480 (line)]] | alt | 24.8 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.197× (z -14.3) |
| [[J82 (line)]] | alt | 6.57 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0816× (z -10.5) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 20.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.183× (z -10.8) |
| [[LoVo (line)]] | wt | 12.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.22× (z +10.3) | — |
| [[NCI-H1573 (line)]] | alt | 7.24 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0711× (z -11.6) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 12.9 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0992× (z -11.5) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 10.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0602× (z -11.2) ⚠ cell-cycle shift, explains ~63% of this change |
| [[SNU-423 (line)]] | alt | 14.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -9.1) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 8.64 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.45 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.84 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.06 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.29 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.17 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13332), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSNK1G1]] | +0.60 | +0.39 / +0.55 | both halves | 5e-05 |  |
| [[GPALPP1]] | +0.59 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[TMEM68]] | +0.59 | +0.37 / +0.62 | both halves | 7e-05 |  |
| [[SUPV3L1]] | +0.58 | +0.33 / +0.60 | both halves | 1e-04 |  |
| [[TRMT61B]] | +0.58 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[POLR1HASP]] | +0.58 | +0.60 / +0.39 | both halves | 6e-05 |  |
| [[NIFK-AS1]] | +0.56 | +0.58 / +0.41 | both halves | 4e-05 |  |
| [[NADSYN1]] | +0.56 | +0.30 / +0.54 | both halves | 2e-04 |  |
| [[NAF1]] | +0.56 | +0.54 / +0.37 | both halves | 8e-05 |  |
| [[MAIP1]] | +0.56 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[VPS13B-DT]] | +0.55 | +0.58 / +0.43 | both halves | 3e-05 |  |
| [[NDUFAF6]] | +0.55 | +0.53 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCAM1]] | -0.52 | -0.24 / -0.36 | both halves | 5e-04 |  |
| [[ATP1A3]] | -0.52 | -0.36 / -0.34 | both halves | 1e-04 |  |
| [[ALAS1]] | -0.52 | -0.33 / -0.44 | both halves | 1e-04 |  |
| [[PLEKHO2]] | -0.51 | -0.47 / -0.34 | both halves | 1e-04 |  |
| [[SLC9A3R1]] | -0.51 | -0.39 / -0.37 | both halves | 9e-05 |  |
| [[CSRP1]] | -0.51 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[SLFN11]] | -0.50 | -0.32 / -0.36 | both halves | 2e-04 |  |
| [[BMAL1]] | -0.50 | -0.22 / -0.54 | both halves | 6e-04 |  |
| [[SOCS3]] | -0.49 | -0.22 / -0.52 | both halves | 6e-04 |  |
| [[RAB3IP]] | -0.49 | -0.34 / -0.41 | both halves | 1e-04 |  |
| [[GDF11]] | -0.47 | -0.21 / -0.38 | both halves | 7e-04 |  |
| [[OLFM1]] | -0.47 | -0.30 / -0.33 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers FAM185A's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SLC4A8]] | B | SLC4A8 activity raises FAM185A's level | lines that do not express SLC4A8 (11) vs lines expressing it (39) | 1.30× lower at baseline in the lines without SLC4A8 | 0.074 | ⚠ within organs, on part of the lines; also absent: DNAH2; maybe low, not absent |
| [[OLFM1]] | B | OLFM1 activity raises FAM185A's level | lines that do not express OLFM1 (27) vs lines expressing it (23) | 1.19× lower at baseline in the lines without OLFM1 | 0.075 | ⚠ within organs, on part of the lines; also absent: JPH3, DPYSL5, CHST8 |
| [[PINCR]] | B | PINCR activity strengthens FAM185A's drug response | lines that do not express PINCR (29) vs lines expressing it (19) | the lines without PINCR respond 0.79× as strongly (z diff +0.65); strongest at Idarubicin (hydrochloride) 5 µM: 1.39x vs 2.33x (z diff +3.3) | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1; target measured in part of the lines; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises FAM185A's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PDLIM3]] | B | PDLIM3 activity raises FAM185A's level | lines that do not express PDLIM3 (18) vs lines expressing it (32) | 1.11× lower at baseline in the lines without PDLIM3 | 0.096 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, SOX5, PTX3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.594). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-5.4, 25.0); signed map (-1.3, -3.6). **Vector** length 64.0, 11.0% of its response variance represented; |z| ≥ 3 in 951 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +6.7 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | -2.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +3.5 | +7.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.4 | -1.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +2.5 | +3.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +5.9 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.5 | +3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +4.5 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.3 | +1.9 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.1 | -2.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | -0.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | +2.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.0 | -6.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.5 | +5.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.8 | -2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | -3.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.2 | +3.0 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.2 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 185 member A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:102,748,971-102,809,225 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC35361 |
| Matched by | ensembl_id |

UniProt [Q8N0U4](https://www.uniprot.org/uniprotkb/Q8N0U4) carries no function annotation.

**Summary**, from NCBI Gene [222234](https://www.ncbi.nlm.nih.gov/gene/222234):

> Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:22412](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22412) · Entrez [222234](https://www.ncbi.nlm.nih.gov/gene/222234) · UniProt [Q8N0U4](https://www.uniprot.org/uniprotkb/Q8N0U4) · Ensembl [ENSG00000222011](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000222011)

## Data

Gene col 13332: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13332); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13332, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13332]; `tensor/DDL_lfc|DDL_z.npy` [13332]; `embed/gene_vectors.npy` [13332]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13332 or target_col == 13332). Every well: [[FAM185A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM185A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
