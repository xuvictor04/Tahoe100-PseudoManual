---
symbol: "GREB1L"
type: "gene"
col: 6523
ensembl_id: "ENSG00000141449"
name: "GREB1 like retinoic acid receptor coactivator"
location: "18q11.1-q11.2"
module: 120
arm: "+"
pooled_cpm: 88.45
n_lines_expressing: 31
n_dd_up: 7
n_dd_down: 19
n_dd_up_clean: 4
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 2
tags: ["gene", "module/120"]
generated_by: "tahoemap"
---

# GREB1L

*GREB1 like retinoic acid receptor coactivator* — 18q11.1-q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.36× (z +7.0, q 2e-09, up in 20 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.585× (z -8.7, q 3e-15, down in 22 of 29 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DKK1]] (+0.57, fdr 1e-05), [[PRKG1-AS1]] (+0.57, fdr 1e-05), [[IL1R2]] (+0.50, fdr 2e-04); moves opposite to [[BAD]] (-0.53, fdr 5e-05), [[UBAC1]] (-0.46, fdr 4e-05), [[C20orf96]] (-0.45, fdr 7e-05).
> It is in [[Module 120]], a single-armed module (RHOA GTPase cycle).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 2 go from it, the strongest it → [[SLC25A23]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6523.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.36×** | +7.0 | 2e-09 | 20/29 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.44×** | +5.9 | 9e-07 | 16/29 (PANC-1, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.42×** | +5.7 | 2e-06 | 20/30 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.9 | 0.011 | 11/29 (Panc 03.27, MIA PaCa-2, …) | rises with dose | composition shift |
| [[Rapamycin (drug)]] 5 µM |  | 1.18× | +3.8 | 0.014 | 10/29 (AsPC-1, J82, …) | rises with dose |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.53×** | +3.6 | 0.029 | 14/29 (Hs 766T, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.24×** | +3.3 | 0.085 | 12/29 (J82, CFPAC-1, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.22×** | +3.2 | 0.090 | 12/29 (MIA PaCa-2, HEC-1-A, …) | inconsistent across doses |  |
| [[Larotrectinib sulfate (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.22×** | +3.2 | 0.090 | 12/29 (A498, J82, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.21× | +3.1 | 0.11 | 11/29 (HS-578T, NCI-H2347, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6523.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.585×** | -8.7 | 3e-15 | 22/29 (LS 180, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.620×** | -7.7 | 3e-12 | 25/29 (NCI-H1792, LS 180, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.627×** | -7.3 | 7e-11 | 18/29 (A498, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.646×** | -7.1 | 2e-10 | 22/29 (LS 180, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.457×** | -6.6 | 4e-09 | 25/30 (LS 180, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.692×** | -5.9 | 3e-07 | 19/29 (NCI-H1792, CFPAC-1, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~23% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.707×** | -5.6 | 2e-06 | 19/29 (SW 1271, A498, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.690×** | -5.5 | 2e-06 | 19/28 (NCI-H1792, A-172, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Radotinib (drug)]] 5 µM |  | **0.815×** | -4.7 | 2e-04 | 15/29 (LS 180, NCI-H1792, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.746×** | -4.5 | 4e-04 | 19/29 (LS 180, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.758×** | -4.5 | 4e-04 | 16/29 (LS 180, CFPAC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.774×** | -4.0 | 0.003 | 16/27 (NCI-H1792, LS 180, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.787×** | -3.9 | 0.005 | 16/30 (NCI-H1792, A-172, …) | all doses, flat | composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.644×** | -3.7 | 0.008 | 14/26 (AsPC-1, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.794×** | -3.7 | 0.008 | 17/29 (LS 180, CFPAC-1, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.663×** | -3.5 | 0.019 | 14/29 (LS 180, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **0.807×** | -3.3 | 0.029 | 11/29 (CHP-212, A498, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.816×** | -3.3 | 0.032 | 15/29 (LS 180, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 5 µM |  | 0.867× | -3.2 | 0.035 | 10/29 (A-172, SW 1271, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6523. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 632 | 0 | 16 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.127× (z -19.7) |
| [[NCI-H1792 (line)]] | alt | 418 | 0 | 13 (10 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.173× (z -21.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.209× (z -19.9) |
| [[CFPAC-1 (line)]] | alt | 214 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.277× (z -13.0) |
| [[AsPC-1 (line)]] | alt | 788 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.170× (z -18.6) |
| [[A498 (line)]] | wt | 63.9 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -13.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.346× (z -9.5) |
| [[A-172 (line)]] | wt | 123 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.199× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.317× (z -9.7) |
| [[A549 (line)]] | wt | 54.3 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -14.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.341× (z -9.4) |
| [[HEC-1-A (line)]] | alt | 65.1 | 1 | 2 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.09× (z +11.1) | [[Homoharringtonine (drug)]] 5 µM 0.477× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 110 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.121× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[NCI-H2030 (line)]] | alt | 116 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.308× (z -10.7) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 59.6 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.87× (z +9.3) | [[Digitoxin (drug)]] 0.5 µM 0.431× (z -8.8) ⚠ cell-cycle shift, explains ~80% of this change |
| [[Panc 03.27 (line)]] | alt | 62.5 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +11.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[BT-474 (line)]] | alt | 56.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.25× (z +8.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[C-33 A (line)]] | alt | 86.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.159× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[HS-578T (line)]] | alt | 31.4 | 1 | 0 | [[Clobetasol propionate (drug)]] 5 µM 4.02× (z +8.9) | — |
| [[J82 (line)]] | alt | 155 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.497× (z -8.5) |
| [[MIA PaCa-2 (line)]] | alt | 50.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SNU-1 (line)]] | wt | 95.0 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.435× (z -10.1) |
| [[SW 1271 (line)]] | alt | 66.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0568× (z -10.4) |
| [[A-427 (line)]] | wt | 114 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.3 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 10.4 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 7.94 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 38.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.86 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 9.72 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 18.5 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 69.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.77 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.7 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 7.87 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 9.26 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 9.76 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 75.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 81.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 63.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 239 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.23 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 8.09 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 7.71 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.21 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.2 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.68 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 10.3 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 7.53 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6523), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DKK1]] | +0.57 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[PRKG1-AS1]] | +0.57 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[IL1R2]] | +0.50 | +0.31 / +0.53 | both halves | 2e-04 |  |
| [[CASC19]] | +0.49 | +0.47 / +0.40 | both halves | 5e-05 |  |
| [[ASAP1]] | +0.49 | +0.54 / +0.41 | both halves | 4e-05 |  |
| [[THSD4]] | +0.49 | +0.51 / +0.46 | both halves | 3e-05 |  |
| [[SLC22A3]] | +0.47 | +0.47 / +0.35 | both halves | 1e-04 |  |
| [[FOXL1]] | +0.47 | +0.49 / +0.42 | both halves | 4e-05 |  |
| [[ZNF562]] | +0.47 | +0.46 / +0.40 | both halves | 5e-05 |  |
| [[NOP56]] | +0.46 | +0.45 / +0.40 | both halves | 5e-05 |  |
| [[CACNA1C]] | +0.46 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[LAMA3]] | +0.46 | +0.42 / +0.47 | both halves | 4e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BAD]] | -0.53 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[UBAC1]] | -0.46 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[C20orf96]] | -0.45 | -0.45 / -0.38 | both halves | 7e-05 |  |
| [[SLC25A23]] | -0.45 | -0.42 / -0.39 | both halves | 6e-05 |  |
| [[ATF6B]] | -0.43 | -0.39 / -0.44 | both halves | 5e-05 |  |
| [[TMEM183A]] | -0.43 | -0.42 / -0.32 | both halves | 2e-04 |  |
| [[COPS7B]] | -0.43 | -0.43 / -0.38 | both halves | 6e-05 |  |
| [[RAB12]] | -0.43 | -0.42 / -0.32 | both halves | 2e-04 |  |
| [[C12orf76]] | -0.43 | -0.37 / -0.38 | both halves | 8e-05 |  |
| [[CAT]] | -0.43 | -0.50 / -0.32 | both halves | 1e-04 |  |
| [[IDH1]] | -0.43 | -0.38 / -0.36 | both halves | 9e-05 |  |
| [[ABHD4]] | -0.43 | -0.47 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC25A23]] | B | GREB1L activity raises SLC25A23's level | lines that do not express GREB1L (19) vs lines expressing it (31) | 1.09× lower at baseline in the lines without GREB1L | 0.042 | ⚠ within organs, on part of the lines; also absent: ADAMTSL3, ZYG11A, CNNM1 |
| cells under [[Tucidinostat (drug)]] 5 µM | B | GREB1L activity raises the cells' numbers under Tucidinostat 5 µM (protects the cells) | lines that do not express GREB1L (19) vs lines expressing it (29) | the lines without GREB1L: 0.92× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: ADAMTSL3, ZYG11A, CNNM1 |

## Where it sits

- **Module**: [[Module 120]] — RHOA GTPase cycle; 41 genes; every member is in the + arm (projection on the module's main direction 0.438). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (38.0, 11.1); signed map (13.4, 39.5). **Vector** length 98.9, 27.8% of its response variance represented; |z| ≥ 3 in 922 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.2 | +7.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.8 | +5.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.3 | +2.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.2 | +3.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +4.1 | +5.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | -2.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.6 | +1.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.5 | +2.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.4 | +2.5 |
| fall | [[Radotinib (drug)]] 5 µM |  | -2.9 | -4.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.7 | -6.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.6 | -4.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | -2.4 | -5.9 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -1.7 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | -2.1 | -3.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.9 | -0.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | GREB1 like retinoic acid receptor coactivator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q11.1-q11.2 — chr18:21,242,232-21,526,112 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13687, C18orf6; previously KIAA1772 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9C091](https://www.uniprot.org/uniprotkb/Q9C091) (GREB1-like protein):

> Plays a major role in early metanephros and genital development.

**Summary**, from NCBI Gene [80000](https://www.ncbi.nlm.nih.gov/gene/80000):

> Acts upstream of or within kidney development. Predicted to be located in membrane. Implicated in autosomal dominant nonsyndromic deafness 80 and renal agenesis. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:31042](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31042) · Entrez [80000](https://www.ncbi.nlm.nih.gov/gene/80000) · UniProt [Q9C091](https://www.uniprot.org/uniprotkb/Q9C091) · Ensembl [ENSG00000141449](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141449)

## Data

Gene col 6523: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6523); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6523, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6523]; `tensor/DDL_lfc|DDL_z.npy` [6523]; `embed/gene_vectors.npy` [6523]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6523 or target_col == 6523). Every well: [[GREB1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GREB1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
