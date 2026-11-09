---
symbol: "ELF3"
type: "gene"
col: 8690
ensembl_id: "ENSG00000163435"
name: "E74 like ETS transcription factor 3"
location: "1q32.1"
module: 8
arm: "+"
pooled_cpm: 130.59
n_lines_expressing: 27
n_dd_up: 18
n_dd_down: 10
n_dd_up_clean: 13
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 84
direction_downstream: 129
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# ELF3

*E74 like ETS transcription factor 3* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.72× (z +7.8, q 3e-12, up in 21 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.434× (z -8.5, q 2e-14, down in 25 of 25 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAP3K8]] (+0.78, fdr 7e-06), [[ELF3-AS1]] (+0.72, fdr 7e-06, ⚠ same locus), [[PLEKHG6]] (+0.72, fdr 7e-06), [[TJP3]] (+0.72, fdr 7e-06); moves opposite to [[MCM3AP]] (-0.54, fdr 1e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 84 arrows point to it, the strongest [[EFNA1]] → it (grade B ⚠); 129 go from it, the strongest it → [[ATP1B1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8690.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.72×** | +7.8 | 3e-12 | 21/25 (HCT15, LS 180, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **3.88×** | +7.2 | 2e-10 | 23/26 (AsPC-1, NCI-H2347, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.59×** | +6.7 | 4e-09 | 11/25 (A498, HEC-1-A, …) | top dose only | composition shift; position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.72×** | +5.5 | 5e-06 | 21/26 (LS 180, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.71×** | +5.3 | 2e-05 | 17/25 (LS 180, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.50×** | +4.9 | 1e-04 | 21/25 (AsPC-1, A549, …) | two highest doses | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.49×** | +4.5 | 5e-04 | 20/26 (AsPC-1, LS 180, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.24×** | +4.3 | 0.001 | 10/20 (BT-474, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.51×** | +4.2 | 0.001 | 5/25 (SW 900, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.09×** | +3.9 | 0.005 | 12/25 (SW1417, SW48, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.49×** | +3.9 | 0.005 | 9/25 (NCI-H2030, HEC-1-A, …) | top dose only | composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.44×** | +3.7 | 0.010 | 14/26 (AsPC-1, A549, …) | two highest doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.37×** | +3.7 | 0.011 | 19/25 (AsPC-1, HCT15, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **1.35×** | +3.6 | 0.014 | 21/27 (AsPC-1, A549, …) | two highest doses | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.60×** | +3.4 | 0.025 | 5/25 (AsPC-1, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 5 µM |  | **1.25×** | +3.3 | 0.035 | 16/26 (HCT15, NCI-H2347, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.39×** | +3.3 | 0.035 | 15/25 (A549, AsPC-1, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.36×** | +3.0 | 0.080 | 14/25 (AsPC-1, HCT15, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8690.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.434×** | -8.5 | 2e-14 | 25/25 (Panc 03.27, SW 900, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.578×** | -5.5 | 8e-06 | 24/25 (SW 900, AsPC-1, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.684×** | -3.8 | 0.020 | 25/26 (COLO 205, LS 180, …) | inconsistent across doses | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.765×** | -3.8 | 0.020 | 22/25 (SW1417, NCI-H2347, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.696×** | -3.6 | 0.030 | 9/25 (NCI-H1573, NCI-H1792, …) | two highest doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.710×** | -3.4 | 0.053 | 9/25 (NCI-H1573, NCI-H1792, …) | rises with dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.708×** | -3.3 | 0.064 | 20/25 (HT-29, Panc 03.27, …) | top dose only | position effect removed |
| [[Budesonide (drug)]] 5 µM |  | **0.722×** | -3.3 | 0.064 | 16/25 (NCI-H1573, NCI-H1792, …) | top dose only |  |
| [[Dabrafenib (drug)]] 5 µM |  | **0.537×** | -3.3 | 0.064 | 5/26 (SW480, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.725×** | -3.2 | 0.068 | 11/25 (SW48, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.42 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8690. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 493 | 1 | 7 (6 ⚠) | [[TAK-901 (drug)]] 5 µM 9.85× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.0166× (z -35.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.240× (z -12.1) |
| [[HT-29 (line)]] | alt | 380 | 1 | 7 (6 ⚠) | [[TAK-901 (drug)]] 5 µM 7.25× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.254× (z -16.4) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.203× (z -13.5) |
| [[NCI-H1573 (line)]] | alt | 319 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.149× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 0.365× (z -9.9) |
| [[KATO III (line)]] | alt | 284 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.144× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.314× (z -8.7) |
| [[SW1417 (line)]] | alt | 370 | 2 | 5 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 10.6× (z +11.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -12.8) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.281× (z -11.5) |
| [[NCI-H2347 (line)]] | alt | 484 | 2 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 10.1× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.292× (z -11.6) |
| [[LS 180 (line)]] | wt | 210 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.174× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[A498 (line)]] | wt | 150 | 2 (2 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.19× (z +15.9) ⚠ cell-cycle shift, explains ~35% of this change | [[Auranofin (drug)]] 5 µM 0.217× (z -9.3) |
| [[AsPC-1 (line)]] | alt | 301 | 2 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 17.4× (z +11.5) | [[Auranofin (drug)]] 5 µM 0.211× (z -11.9) |
| [[CFPAC-1 (line)]] | alt | 350 | 1 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +12.6) ⚠ cell-cycle shift, explains ~35% of this change | [[Auranofin (drug)]] 5 µM 0.287× (z -10.8) |
| [[Hs 766T (line)]] | wt | 75.4 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.126× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.222× (z -9.7) |
| [[LoVo (line)]] | wt | 310 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.221× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 344 | 0 | 4 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.123× (z -17.8) |
| [[SW48 (line)]] | wt | 143 | 2 | 2 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 16.4× (z +9.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.343× (z -9.9) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.248× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 168 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.86× (z +13.4) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[SW 900 (line)]] | alt | 160 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.103× (z -16.1) |
| [[BT-474 (line)]] | alt | 211 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 15.2× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.277× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 122 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 3.27× (z +10.6) | [[Auranofin (drug)]] 5 µM 0.226× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 35.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -9.8) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Clobetasol propionate (drug)]] 0.05 µM 0.186× (z -8.5) |
| [[A549 (line)]] | wt | 161 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.159× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[NCI-H2030 (line)]] | alt | 37.1 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 8.31× (z +12.5) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[A-172 (line)]] | wt | 16.9 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 8.60 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 29.3 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 12.6 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 12.3 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 33.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.8 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 121 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.1 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 17.1 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.6 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 11.9 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 14.0 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 22.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 271 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.17 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 15.8 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.6 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 11.8 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 11.2 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 10.8 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 79.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.5 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 14.5 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 25.5 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 23.1 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 12.9 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 57.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8690), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAP3K8]] | +0.78 | +0.76 / +0.77 | both halves | 7e-06 |  |
| [[ELF3-AS1]] | +0.72 | +0.65 / +0.76 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[PLEKHG6]] | +0.72 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[TJP3]] | +0.72 | +0.63 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[TRIM31]] | +0.71 | +0.66 / +0.78 | both halves | 7e-06 | STRING 521 |
| [[EFNA1]] | +0.71 | +0.61 / +0.77 | both halves | 7e-06 |  |
| [[ATP8B1]] | +0.70 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[TMPRSS3]] | +0.69 | +0.61 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[RBM47]] | +0.68 | +0.59 / +0.74 | both halves | 7e-06 |  |
| [[RHOV]] | +0.66 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[SLC44A4]] | +0.66 | +0.57 / +0.71 | both halves | 1e-05 |  |
| [[SLC40A1]] | +0.65 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[TMPRSS2]] | +0.65 | +0.65 / +0.66 | both halves | 7e-06 | STRING 404 |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCM3AP]] | -0.54 | -0.35 / -0.59 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*84 arrows, 84 of them with an alert ⚠; grade A 0, B 21, C 63. Shown: the 12 strongest; 72 more arrows (72 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EFNA1]] | B | EFNA1 activity raises ELF3's level | lines that do not express EFNA1 (13) vs lines expressing it (37) | 4.61× lower at baseline in the lines without EFNA1 | 0.006 | ⚠ within organs, on part of the lines; also absent: ELF3-AS1, ANO9, GPRC5A; maybe low, not absent |
| [[GBP2]] | B | GBP2 activity raises ELF3's level | lines that do not express GBP2 (13) vs lines expressing it (37) | 2.85× lower at baseline in the lines without GBP2 | 0.008 | ⚠ within organs, on part of the lines; also absent: GBP1, ITGA3, SH3TC1 |
| [[ATP1B1]] | B | ATP1B1 activity raises ELF3's level | lines that do not express ATP1B1 (8) vs lines expressing it (42) | 5.06× lower at baseline in the lines without ATP1B1 | 0.008 | ⚠ within organs, on part of the lines; also absent: PYROXD2, IL15, IER3; maybe low, not absent |
| [[LINC00511]] | B | LINC00511 activity raises ELF3's level | lines that do not express LINC00511 (12) vs lines expressing it (38) | 4.15× lower at baseline in the lines without LINC00511 | 0.011 | ⚠ within organs, on part of the lines; also absent: ABLIM3, LGALS3, CDK18 |
| [[SLC28A3]] | B | SLC28A3 activity raises ELF3's level | lines that do not express SLC28A3 (34) vs lines expressing it (16) | 2.28× lower at baseline in the lines without SLC28A3 | 0.017 | ⚠ within organs, on part of the lines; also absent: CFTR, DAPP1, SLC6A14 |
| [[LNX1]] | B | LNX1 activity raises ELF3's level | lines that do not express LNX1 (20) vs lines expressing it (30) | 3.07× lower at baseline in the lines without LNX1 | 0.023 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, EGF, KLF8 |
| [[GATA6]] | B | GATA6 activity raises ELF3's level | lines that do not express GATA6 (18) vs lines expressing it (32) | 2.82× lower at baseline in the lines without GATA6 | 0.031 | ⚠ within organs, on part of the lines; also absent: ENSG00000264825, CDA, SPTLC3 |
| [[NOD2]] | B | NOD2 activity raises ELF3's level | lines that do not express NOD2 (17) vs lines expressing it (33) | 2.40× lower at baseline in the lines without NOD2 | 0.035 | ⚠ within organs, on part of the lines; also absent: STAT5A, TLR2, BDKRB2 |
| [[FUT2]] | B | FUT2 activity raises ELF3's level | lines that do not express FUT2 (12) vs lines expressing it (38) | 3.26× lower at baseline in the lines without FUT2 | 0.037 | ⚠ within organs, on part of the lines; also absent: EFNB2, SH3TC1, PTPRE; maybe low, not absent |
| [[RASGEF1B]] | B | RASGEF1B activity raises ELF3's level | lines that do not express RASGEF1B (10) vs lines expressing it (40) | 3.55× lower at baseline in the lines without RASGEF1B | 0.045 | ⚠ within organs, on part of the lines; also absent: FBXW10B; maybe low, not absent |
| [[TNFAIP2]] | B | TNFAIP2 activity raises ELF3's level | lines that do not express TNFAIP2 (22) vs lines expressing it (28) | 1.90× lower at baseline in the lines without TNFAIP2 | 0.047 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, LINC02057, DEPP1 |
| [[CGNL1]] | B | CGNL1 activity raises ELF3's level | lines that do not express CGNL1 (21) vs lines expressing it (29) | 2.28× lower at baseline in the lines without CGNL1 | 0.051 | ⚠ within organs, on part of the lines; also absent: GPRC5B, SAA4, NSUN7 |

### Downstream of this gene

*129 arrows, 129 of them with an alert ⚠; grade A 0, B 68, C 61. Shown: the 12 strongest; 117 more arrows (117 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATP1B1]] | B | ELF3 activity raises ATP1B1's level | lines that do not express ELF3 (23) vs lines expressing it (27) | 3.74× lower at baseline in the lines without ELF3 | 9e-05 | ⚠ within organs, on part of the lines; also absent: RASSF6, GOLT1A, LAMA3 |
| [[RASGEF1B]] | B | ELF3 activity raises RASGEF1B's level | lines that do not express ELF3 (23) vs lines expressing it (27) | 3.02× lower at baseline in the lines without ELF3 | 3e-04 | ⚠ within organs, on part of the lines; also absent: RASSF6, GOLT1A, LAMA3 |
| [[TUFT1]] | B | ELF3 activity raises TUFT1's level | lines that do not express ELF3 (23) vs lines expressing it (27) | 2.88× lower at baseline in the lines without ELF3 | 4e-04 | ⚠ within organs, on part of the lines; also absent: RASSF6, GOLT1A, LAMA3 |
| [[NBPF8]] | B | ELF3 activity lowers NBPF8's level | lines that do not express ELF3 (23) vs lines expressing it (27) | 2.25× higher at baseline in the lines without ELF3 | 5e-04 | ⚠ within organs, on part of the lines; also absent: RASSF6, GOLT1A, LAMA3 |
| [[RND1]] | B | ELF3 activity raises RND1's level | lines that do not express ELF3 (23) vs lines expressing it (27) | 2.99× lower at baseline in the lines without ELF3 | 6e-04 | ⚠ within organs, on part of the lines; also absent: RASSF6, GOLT1A, LAMA3 |
| [[KIAA1522]] | B | ELF3 activity raises KIAA1522's level | lines that do not express ELF3 (23) vs lines expressing it (27) | 2.78× lower at baseline in the lines without ELF3 | 8e-04 | ⚠ within organs, on part of the lines; also absent: RASSF6, GOLT1A, LAMA3 |
| [[EFNA1]] | B | ELF3 activity raises EFNA1's level | lines that do not express ELF3 (23) vs lines expressing it (27) | 3.06× lower at baseline in the lines without ELF3 | 0.001 | ⚠ within organs, on part of the lines; also absent: RASSF6, GOLT1A, LAMA3 |
| [[NEDD9]] | B | ELF3 activity raises NEDD9's level | lines that do not express ELF3 (23) vs lines expressing it (27) | 3.30× lower at baseline in the lines without ELF3 | 0.003 | ⚠ within organs, on part of the lines; also absent: RASSF6, GOLT1A, LAMA3 |
| [[LNX1]] | B | ELF3 activity raises LNX1's level | lines that do not express ELF3 (23) vs lines expressing it (27) | 3.50× lower at baseline in the lines without ELF3 | 0.003 | ⚠ within organs, on part of the lines; also absent: RASSF6, GOLT1A, LAMA3 |
| [[DTX2]] | B | ELF3 activity raises DTX2's level | lines that do not express ELF3 (23) vs lines expressing it (27) | 1.88× lower at baseline in the lines without ELF3 | 0.003 | ⚠ within organs, on part of the lines; also absent: RASSF6, GOLT1A, LAMA3 |
| [[CTNND1]] | B | ELF3 activity strengthens CTNND1's drug response | lines that do not express ELF3 (23) vs lines expressing it (25) | the lines without ELF3 respond 0.76× as strongly (z diff +1.33); strongest at Auranofin 5 µM: 0.73x vs 0.58x (z diff +4.1) | 0.004 | ⚠ within organs, on part of the lines; also absent: RASSF6, GOLT1A, LAMA3; target measured in part of the lines; artifact flags |
| [[DDR1]] | B | ELF3 activity raises DDR1's level | lines that do not express ELF3 (23) vs lines expressing it (27) | 2.36× lower at baseline in the lines without ELF3 | 0.004 | ⚠ within organs, on part of the lines; also absent: RASSF6, GOLT1A, LAMA3 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.673). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.7, 53.8); signed map (58.9, 3.4). **Vector** length 127, 45.8% of its response variance represented; |z| ≥ 3 in 939 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Dectin-2 family* (reactome, mean cos +0.51 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.1 | +7.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.5 | +5.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +5.6 | +5.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +5.0 | +4.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | +5.0 | +4.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.7 | +3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.9 | +3.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.1 | -5.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.5 | -1.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.0 | -8.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -0.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -3.6 | -3.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.5 | -2.3 |
|  | [[Budesonide (drug)]] 5 µM |  | -3.3 | -3.3 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -3.0 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | E74 like ETS transcription factor 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:202,007,945-202,017,183 (+) |
| Ensembl biotype | protein_coding |
| Also known as | EPR-1, ESE-1, ERT; previously ESX |
| Gene groups (HGNC) | ETS transcription factor family |
| Hallmark sets | GLYCOLYSIS, ESTROGEN_RESPONSE_EARLY |
| Reactome | 3 pathways, smallest: Pre-NOTCH Transcription and Translation; Pre-NOTCH Expression and Processing; Signaling by NOTCH |
| Matched by | ensembl_id |

**Function**, from UniProt [P78545](https://www.uniprot.org/uniprotkb/P78545) (ETS-related transcription factor Elf-3):

> Transcriptional activator that binds and transactivates ETS sequences containing the consensus nucleotide core sequence GGA[AT]. Acts synergistically with POU2F3 to transactivate the SPRR2A promoter and with RUNX1 to transactivate the ANGPT1 promoter. Also transactivates collagenase, CCL20, CLND7, FLG, KRT8, NOS2, PTGS2, SPRR2B, TGFBR2 and TGM3 promoters. Represses KRT4 promoter activity. Involved in mediating vascular inflammation. May play an important role in epithelial cell differentiation …

**Summary**, from NCBI Gene [1999](https://www.ncbi.nlm.nih.gov/gene/1999):

> Enables DNA-binding transcription activator activity, RNA polymerase II-specific and sequence-specific double-stranded DNA binding activity. Involved in inflammatory response; negative regulation of DNA-templated transcription; and positive regulation of transcription by RNA polymerase II. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:3318](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3318) · Entrez [1999](https://www.ncbi.nlm.nih.gov/gene/1999) · UniProt [P78545](https://www.uniprot.org/uniprotkb/P78545) · Ensembl [ENSG00000163435](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163435)

## Data

Gene col 8690: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8690); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8690, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8690]; `tensor/DDL_lfc|DDL_z.npy` [8690]; `embed/gene_vectors.npy` [8690]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8690 or target_col == 8690). Every well: [[ELF3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ELF3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
