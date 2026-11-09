---
symbol: "PPP1R10"
type: "gene"
col: 12891
ensembl_id: "ENSG00000204569"
name: "protein phosphatase 1 regulatory subunit 10"
location: "6p21.33"
module: 190
arm: "+"
pooled_cpm: 81.21
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 10
n_dd_up_clean: 8
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/190"]
generated_by: "tahoemap"
---

# PPP1R10

*protein phosphatase 1 regulatory subunit 10* — 6p21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.77× (z +21.2, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 0.521× (z -7.1, q 4e-10, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MMP25]] (+0.69, fdr 7e-06), [[THOC6]] (+0.69, fdr 7e-06), [[ZC3H4]] (+0.68, fdr 7e-06); moves opposite to [[CCZ1B]] (-0.69, fdr 7e-06), [[NAPB]] (-0.69, fdr 7e-06), [[PRKRA]] (-0.68, fdr 7e-06).
> It is in [[Module 190]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ABL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12891.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.77×** | +21.2 | 0e+00 | 44/48 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.78×** | +11.6 | 2e-28 | 44/48 (HS-578T, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.24×** | +8.7 | 5e-16 | 34/50 (PANC-1, HT-29, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.88×** | +6.8 | 1e-09 | 35/48 (HS-578T, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.77×** | +6.4 | 2e-08 | 34/48 (A-172, HT-29, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.44×** | +5.3 | 1e-05 | 33/49 (LoVo, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.21×** | +4.7 | 2e-04 | 34/48 (LoVo, LS 180, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.37×** | +3.5 | 0.031 | 24/48 (NCI-H460, LS 180, …) | all doses, stronger at high dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.33×** | +3.2 | 0.081 | 22/48 (HepG2/C3A, SW 900, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12891.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.521×** | -7.1 | 4e-10 | 41/48 (NCI-H23, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.523×** | -7.1 | 4e-10 | 40/50 (NCI-H23, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.591×** | -6.0 | 4e-07 | 34/49 (RKO, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.609×** | -5.4 | 8e-06 | 29/43 (HT-29, Hs 766T, …) | two highest doses | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Radotinib (drug)]] 5 µM |  | **0.716×** | -5.4 | 8e-06 | 40/48 (PANC-1, AsPC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.652×** | -4.7 | 3e-04 | 29/47 (NCI-H23, H4, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.703×** | -4.0 | 0.005 | 31/48 (HT-29, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.530×** | -3.8 | 0.012 | 31/47 (SHP-77, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.758×** | -3.2 | 0.097 | 24/48 (PANC-1, NCI-H23, …) | top dose only | cell-cycle shift (explains ~8% here); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.752×** | -3.1 | 0.099 | 26/48 (NCI-H23, LoVo, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12891. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 89.5 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +13.2) | [[Dinaciclib (drug)]] 5 µM 0.296× (z -10.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 100 | 3 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.25× (z +21.7) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -8.9) |
| [[HT-29 (line)]] | alt | 114 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.254× (z -11.4) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 111 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +13.7) | [[Dinaciclib (drug)]] 0.5 µM 0.351× (z -8.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 93.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.52× (z +20.0) | — |
| [[NCI-H1573 (line)]] | alt | 108 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.40× (z +20.0) | [[Dinaciclib (drug)]] 0.5 µM 0.276× (z -10.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 122 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +14.7) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.139× (z -15.3) |
| [[SK-MEL-2 (line)]] | alt | 52.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.96× (z +19.4) | — |
| [[A498 (line)]] | wt | 37.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.34× (z +19.6) | — |
| [[COLO 205 (line)]] | alt | 99.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.15× (z +19.6) | — |
| [[HS-578T (line)]] | alt | 58.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.34× (z +21.6) | — |
| [[hTERT-HPNE (line)]] | wt | 66.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.90× (z +20.3) | — |
| [[LOX-IMVI (line)]] | wt | 111 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +14.5) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.161× (z -12.0) |
| [[NCI-H460 (line)]] | wt | 63.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.47× (z +24.2) | — |
| [[A-172 (line)]] | wt | 56.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +12.8) | — |
| [[C-33 A (line)]] | alt | 116 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.210× (z -12.0) |
| [[C32 (line)]] | wt | 57.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.1× (z +16.4) | — |
| [[H4 (line)]] | wt | 70.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +10.6) | — |
| [[HOP62 (line)]] | alt | 80.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.51× (z +19.2) | — |
| [[Hs 766T (line)]] | wt | 56.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.67× (z +17.7) | [[Dinaciclib (drug)]] 5 µM 0.201× (z -11.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 75.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +15.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 100 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +13.0) | — |
| [[NCI-H2030 (line)]] | alt | 123 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +10.3) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -8.7) |
| [[NCI-H2347 (line)]] | alt | 38.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +14.7) | — |
| [[RKO (line)]] | wt | 93.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.171× (z -13.8) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 71.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.28× (z +17.6) | — |
| [[SW48 (line)]] | wt | 95.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.267× (z -9.0) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 88.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +14.7) | — |
| [[A-427 (line)]] | wt | 85.5 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.273× (z -9.5) |
| [[AN3 CA (line)]] | alt | 61.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.35× (z +11.6) | — |
| [[AsPC-1 (line)]] | alt | 53.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.93× (z +16.2) | — |
| [[BT-474 (line)]] | alt | 115 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.121× (z -8.5) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 78.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.03× (z +17.7) | — |
| [[HCT15 (line)]] | alt | 131 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +11.3) | — |
| [[HEC-1-A (line)]] | alt | 47.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +12.2) | — |
| [[HepG2_C3A (line)]] | wt | 83.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +10.0) | — |
| [[J82 (line)]] | alt | 118 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.11× (z +14.9) | — |
| [[NCI-H1792 (line)]] | alt | 112 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.61× (z +16.3) | — |
| [[Panc 03.27 (line)]] | alt | 69.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +12.4) | — |
| [[SW 1271 (line)]] | alt | 92.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.00× (z +9.6) | — |
| [[SW 900 (line)]] | alt | 61.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +9.8) | — |
| [[A549 (line)]] | wt | 62.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 107 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 78.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 75.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 70.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 65.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 56.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 68.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12891), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MMP25]] | +0.69 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[THOC6]] | +0.69 | +0.67 / +0.64 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[ZC3H4]] | +0.68 | +0.72 / +0.66 | both halves | 7e-06 | same gene group; STRING 427 |
| [[C3orf20]] | +0.67 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[PITRM1-AS1]] | +0.67 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[EPC2]] | +0.67 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[MTNR1A]] | +0.67 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[CELSR3]] | +0.66 | +0.73 / +0.55 | both halves | 1e-05 |  |
| [[ZDHHC11]] | +0.66 | +0.69 / +0.53 | both halves | 1e-05 |  |
| [[SRCAP]] | +0.66 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[NABP1]] | +0.65 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[MIS12]] | +0.65 | +0.67 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCZ1B]] | -0.69 | -0.70 / -0.65 | both halves | 7e-06 |  |
| [[NAPB]] | -0.69 | -0.68 / -0.64 | both halves | 7e-06 |  |
| [[PRKRA]] | -0.68 | -0.70 / -0.63 | both halves | 7e-06 |  |
| [[CCZ1]] | -0.67 | -0.63 / -0.68 | both halves | 7e-06 |  |
| [[DCUN1D4]] | -0.66 | -0.64 / -0.61 | both halves | 7e-06 |  |
| [[NENF]] | -0.64 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[RNF149]] | -0.63 | -0.68 / -0.57 | both halves | 1e-05 |  |
| [[SEC61A2]] | -0.63 | -0.62 / -0.58 | both halves | 7e-06 |  |
| [[SEC11A]] | -0.62 | -0.62 / -0.60 | both halves | 7e-06 |  |
| [[HINT1]] | -0.62 | -0.64 / -0.56 | both halves | 1e-05 |  |
| [[DHRS1]] | -0.61 | -0.66 / -0.54 | both halves | 1e-05 |  |
| [[GCSH]] | -0.61 | -0.69 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABL1]] | B | ABL1 activity raises PPP1R10's level | compounds that target ABL1: 3 of 6 lower it (NG25, Ponatinib, Radotinib) | 50% of the class's compounds vs 2.5% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TRIM72]] | C | TRIM72 activity raises PPP1R10's level | lines that do not express TRIM72 (4) vs lines expressing it (46) | 1.38× lower at baseline in the lines without TRIM72 | 0.078 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC02133, LYG1, LINC01762; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 190]]; 18 genes; every member is in the + arm (projection on the module's main direction -0.753). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.40; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-9.0, -9.6); signed map (20.5, 7.8). **Vector** length 138, 43.9% of its response variance represented; |z| ≥ 3 in 969 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.8 | +21.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.7 | +11.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.5 | +6.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +6.2 | +3.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.1 | +2.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.3 | +3.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.9 | +2.1 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | +3.3 | +2.2 |
| fall | [[Radotinib (drug)]] 5 µM |  | -6.9 | -5.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.8 | -7.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.4 | -7.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.3 | -4.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.2 | -3.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -3.7 | -2.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.3 | -1.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.2 | +0.8 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 1 regulatory subunit 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.33 — chr6:30,600,413-30,618,612 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PNUTS, FB19, CAT53, p99 |
| Gene groups (HGNC) | Zinc fingers CCCH-type; Protein phosphatase 1 regulatory subunits |
| Reactome | 4 pathways, smallest: mRNA Polyadenylation; mRNA 3'-end processing; Processing of Capped Intron-Containing Pre-mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96QC0](https://www.uniprot.org/uniprotkb/Q96QC0) (Serine/threonine-protein phosphatase 1 regulatory subunit 10):

> Substrate-recognition component of the PNUTS-PP1 protein phosphatase complex, a protein phosphatase 1 (PP1) complex that promotes RNA polymerase II transcription pause-release, allowing transcription elongation. Promoter-proximal pausing by RNA polymerase II is a transcription halt following transcription initiation but prior to elongation, which acts as a checkpoint to control that transcripts are favorably configured for transcriptional elongation. The PNUTS-PP1 complex mediates the release …

**Summary**, from NCBI Gene [5514](https://www.ncbi.nlm.nih.gov/gene/5514):

> This gene encodes a protein phosphatase 1 binding protein. The encoded protein plays a role in many cellular processes including cell cycle progression, DNA repair and apoptosis by regulating the activity of protein phosphatase 1. This gene lies within the major histocompatibility complex class I region on chromosome 6, and alternatively spliced transcript variants have been observed for this gene. [provided by RefSeq, Jul 2012]

**Accessions** — [HGNC:9284](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9284) · Entrez [5514](https://www.ncbi.nlm.nih.gov/gene/5514) · UniProt [Q96QC0](https://www.uniprot.org/uniprotkb/Q96QC0) · Ensembl [ENSG00000204569](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204569)

## Data

Gene col 12891: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12891); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12891, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12891]; `tensor/DDL_lfc|DDL_z.npy` [12891]; `embed/gene_vectors.npy` [12891]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12891 or target_col == 12891). Every well: [[PPP1R10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP1R10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
