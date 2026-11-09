---
symbol: "CAPZA1"
type: "gene"
col: 3799
ensembl_id: "ENSG00000116489"
name: "capping actin protein of muscle Z-line subunit alpha 1"
location: "1p13.2"
module: 64
arm: "+"
pooled_cpm: 192.97
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 12
n_dd_up_clean: 5
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# CAPZA1

*capping actin protein of muscle Z-line subunit alpha 1* — 1p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 1.70× (z +6.7, q 5e-09, up in 40 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.457× (z -18.4, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (82 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 18 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RTF2]] (+0.57, fdr 1e-05), [[ARPC4]] (+0.56, fdr 3e-05), [[ARPC3]] (+0.54, fdr 7e-05); moves opposite to [[ZIC2]] (-0.50, fdr 2e-05), [[ACVR2B]] (-0.47, fdr 6e-04), [[AGAP3]] (-0.45, fdr 9e-04, ⚠ not reproduced), [[GATA2]] (-0.43, fdr 4e-05).
> It sits in the **+** arm of [[Module 064]] (proteasome).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3799.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.70×** | +6.7 | 5e-09 | 40/49 (SW480, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.33×** | +6.7 | 5e-09 | 30/48 (PANC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.23×** | +5.0 | 1e-04 | 24/48 (PANC-1, SK-MEL-2, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.23×** | +4.8 | 2e-04 | 23/48 (NCI-H2030, LoVo, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.4 | 0.067 | 20/48 (SNU-423, NCI-H1792, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.070 | 23/48 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.14× | +3.1 | 0.13 | 16/48 (LoVo, NCI-H2030, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3799.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.457×** | -18.4 | 0e+00 | 47/48 (AsPC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.616×** | -16.6 | 0e+00 | 48/49 (RKO, HT-29, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.516×** | -16.1 | 0e+00 | 46/48 (AsPC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.566×** | -13.4 | 1e-38 | 46/48 (AsPC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.596×** | -10.6 | 4e-24 | 45/48 (AsPC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.701×** | -8.6 | 6e-16 | 45/48 (AsPC-1, J82, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.788×** | -8.2 | 3e-14 | 31/48 (A-172, RPMI-7951, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.712×** | -7.9 | 2e-13 | 37/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.729×** | -7.4 | 1e-11 | 39/47 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.758×** | -6.5 | 6e-09 | 29/50 (NCI-H23, NCI-H460, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.605×** | -6.4 | 9e-09 | 40/49 (AsPC-1, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.825×** | -4.7 | 2e-04 | 25/48 (NCI-H23, LOX-IMVI, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.834× | -4.2 | 1e-03 | 23/48 (NCI-H23, PANC-1, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 0.852× | -3.9 | 0.005 | 21/48 (HS-578T, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.860× | -3.7 | 0.010 | 15/48 (NCI-H23, A-172, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | 0.864× | -3.5 | 0.015 | 16/48 (PANC-1, COLO 205, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.888× | -3.4 | 0.021 | 14/48 (NCI-H23, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.865× | -3.4 | 0.021 | 12/49 (NCI-H2347, HEC-1-A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3799. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 294 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.277× (z -21.3) |
| [[A498 (line)]] | wt | 211 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.564× (z -14.7) |
| [[NCI-H1573 (line)]] | alt | 205 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.317× (z -14.0) |
| [[NCI-H23 (line)]] | alt | 498 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.514× (z -14.9) |
| [[J82 (line)]] | alt | 214 | 0 | 5 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.582× (z -12.4) |
| [[MIA PaCa-2 (line)]] | alt | 246 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 1.83× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.623× (z -10.8) |
| [[A-172 (line)]] | wt | 159 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.502× (z -11.5) |
| [[A549 (line)]] | wt | 141 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -14.5) |
| [[CFPAC-1 (line)]] | alt | 151 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.383× (z -13.2) |
| [[H4 (line)]] | wt | 148 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.359× (z -10.9) |
| [[Hs 766T (line)]] | wt | 301 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.538× (z -13.2) |
| [[HT-29 (line)]] | alt | 211 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.453× (z -17.1) |
| [[KATO III (line)]] | alt | 127 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.393× (z -13.6) |
| [[LOX-IMVI (line)]] | wt | 216 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.519× (z -14.2) |
| [[NCI-H460 (line)]] | wt | 153 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.583× (z -12.4) |
| [[PANC-1 (line)]] | alt | 171 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.480× (z -12.1) |
| [[RPMI-7951 (line)]] | alt | 195 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.409× (z -12.2) |
| [[SW1417 (line)]] | alt | 148 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.358× (z -16.1) |
| [[COLO 205 (line)]] | alt | 171 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.324× (z -14.1) |
| [[HEC-1-A (line)]] | alt | 160 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.453× (z -13.0) |
| [[HepG2_C3A (line)]] | wt | 159 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.265× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.591× (z -8.7) |
| [[HOP62 (line)]] | alt | 123 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.458× (z -10.9) |
| [[HS-578T (line)]] | alt | 211 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.435× (z -12.1) |
| [[LS 180 (line)]] | wt | 186 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.468× (z -13.3) |
| [[NCI-H1792 (line)]] | alt | 192 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.371× (z -13.6) |
| [[NCI-H2347 (line)]] | alt | 223 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.454× (z -13.3) |
| [[Panc 03.27 (line)]] | alt | 199 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.435× (z -12.2) |
| [[RKO (line)]] | wt | 319 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -22.8) |
| [[SK-MEL-2 (line)]] | alt | 255 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.514× (z -9.8) |
| [[SNU-423 (line)]] | alt | 152 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.457× (z -10.6) |
| [[SW480 (line)]] | alt | 197 | 1 | 2 | [[TAK-901 (drug)]] 5 µM 3.04× (z +9.6) | [[Panobinostat (drug)]] 0.5 µM 0.536× (z -10.2) |
| [[SW48 (line)]] | wt | 164 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.440× (z -9.1) |
| [[A-427 (line)]] | wt | 126 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.510× (z -13.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 150 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.515× (z -8.7) |
| [[C32 (line)]] | wt | 181 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.469× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 200 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.562× (z -9.9) |
| [[LoVo (line)]] | wt | 155 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.575× (z -12.5) |
| [[NCI-H2030 (line)]] | alt | 243 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.421× (z -9.3) |
| [[SNU-1 (line)]] | wt | 174 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -12.8) |
| [[SW 900 (line)]] | alt | 181 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.454× (z -9.5) |
| [[AN3 CA (line)]] | alt | 144 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 139 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 86.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 204 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 182 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 184 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 231 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 258 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 142 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3799), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 15 of them with an alert (⚠; 15 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RTF2]] | +0.57 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[ARPC4]] | +0.56 | +0.44 / +0.69 | both halves | 3e-05 |  |
| [[ARPC3]] | +0.54 | +0.74 / +0.38 | both halves | 7e-05 | STRING 579 |
| [[KYAT3]] | +0.52 | +0.63 / +0.37 | both halves | 7e-05 |  |
| [[SDHC]] | +0.52 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[RPL26L1]] | +0.51 | +0.32 / +0.45 | both halves | 1e-04 |  |
| [[IPP]] | +0.50 | +0.43 / +0.42 | both halves | 4e-05 |  |
| [[ZDHHC4]] | +0.48 | +0.23 / +0.38 | both halves | 5e-04 |  |
| [[VPS29]] | +0.48 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[MTRF1L]] | +0.48 | +0.28 / +0.53 | both halves | 3e-04 |  |
| [[PDZD11]] | +0.48 | +0.55 / +0.38 | both halves | 6e-05 |  |
| [[DMAC2]] | +0.48 | +0.39 / +0.45 | both halves | 5e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZIC2]] | -0.50 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[ACVR2B]] | -0.47 | -0.22 / -0.38 | both halves | 6e-04 |  |
| [[AGAP3]] | -0.45 | -0.19 / -0.48 | ⚠ not reproduced | 9e-04 |  |
| [[TAF4]] | -0.44 | -0.18 / -0.50 | ⚠ one half (not replicated) | 1e-03 | pathway: Affinity selection of immunoglobulins |
| [[GATA2]] | -0.43 | -0.42 / -0.47 | both halves | 4e-05 | pathway: Factors involved in megakaryocyte development and platelet production |
| [[SMAD7]] | -0.42 | -0.26 / -0.39 | both halves | 4e-04 |  |
| [[ZNNT1]] | -0.42 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[HIVEP1]] | -0.40 | -0.55 / -0.18 | ⚠ one half (not replicated) | 9e-04 |  |
| [[TLE3]] | -0.40 | -0.26 / -0.46 | both halves | 4e-04 |  |
| [[C2orf69]] | -0.40 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[ZNF706]] | -0.40 | -0.33 / -0.42 | both halves | 1e-04 |  |
| [[BCOR]] | -0.39 | -0.39 / -0.35 | both halves | 1e-04 |  |
| [[CNNM3]] | -0.39 | -0.27 / -0.44 | both halves | 3e-04 |  |
| [[MIA]] | -0.39 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[ERF]] | -0.38 | -0.52 / -0.24 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises CAPZA1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.382). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-35.7, -17.3); signed map (-19.2, -27.1). **Vector** length 85.5, 25.1% of its response variance represented; |z| ≥ 3 in 1,137 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.5 | +1.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +6.3 | +2.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +5.4 | -0.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.8 | -1.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.8 | +3.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.4 | +5.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.9 | +1.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.8 | +2.4 |
|  | [[Retinoic acid (drug)]] 5 µM |  | +1.8 | +2.3 |
|  | [[NVP-BHG712 (drug)]] 0.05 µM |  | +1.8 | +1.8 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | +1.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.2 | +0.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.0 | -8.6 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.6 | -0.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | +2.6 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -2.4 | -3.5 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -2.4 | -2.5 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | -1.9 | -1.3 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.9 | +0.4 |

## What is on record

|  |  |
|---|---|
| Name | capping actin protein of muscle Z-line subunit alpha 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.2 — chr1:112,619,805-112,671,616 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CAPPA1 |
| Gene groups (HGNC) | Dynactin subunits |
| Reactome | 29 pathways, smallest: Advanced glycosylation endproduct receptor signaling; Gene and protein expression by JAK-STAT signaling after Interleukin-12 stimulation; Interleukin-12 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P52907](https://www.uniprot.org/uniprotkb/P52907) (F-actin-capping protein subunit alpha-1):

> F-actin-capping proteins bind in a Ca(2+)-independent manner to the fast growing ends of actin filaments (barbed end) thereby blocking the exchange of subunits at these ends. Unlike other capping proteins (such as gelsolin and severin), these proteins do not sever actin filaments. May play a role in the formation of epithelial cell junctions. Forms, with CAPZB, the barbed end of the fast growing ends of actin filaments in the dynactin complex and stabilizes dynactin structure. The dynactin …

**Summary**, from NCBI Gene [829](https://www.ncbi.nlm.nih.gov/gene/829):

> CAPZA1 is a member of the F-actin capping protein alpha subunit family. This gene encodes the alpha subunit of the barbed-end actin binding protein. The protein regulates growth of the actin filament by capping the barbed end of growing actin filaments. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:1488](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1488) · Entrez [829](https://www.ncbi.nlm.nih.gov/gene/829) · UniProt [P52907](https://www.uniprot.org/uniprotkb/P52907) · Ensembl [ENSG00000116489](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116489)

## Data

Gene col 3799: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3799); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3799, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3799]; `tensor/DDL_lfc|DDL_z.npy` [3799]; `embed/gene_vectors.npy` [3799]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3799 or target_col == 3799). Every well: [[CAPZA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CAPZA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
