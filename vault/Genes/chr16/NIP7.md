---
symbol: "NIP7"
type: "gene"
col: 5345
ensembl_id: "ENSG00000132603"
name: "nucleolar pre-rRNA processing protein NIP7"
location: "16q22.1"
module: 5
arm: "+"
pooled_cpm: 12.42
n_lines_expressing: 50
n_dd_up: 54
n_dd_down: 5
n_dd_up_clean: 32
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# NIP7

*nucleolar pre-rRNA processing protein NIP7* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 54 drug-doses (22 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 3.20× (z +14.8, q 0e+00, up in 38 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.717× (z -4.2, q 0.007, down in 17 of 48 measured lines) ⚠ cell-cycle shift, explains ~44% of this change. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 0.718× (z -4.2, q 0.007, down in 11 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPATCH4]] (+0.78, fdr 7e-06), [[DHX37]] (+0.78, fdr 7e-06), [[RRS1]] (+0.78, fdr 7e-06); moves opposite to [[NUCB2]] (-0.74, fdr 7e-06), [[ARL3]] (-0.68, fdr 7e-06), [[GTF2IP4]] (-0.67, fdr 7e-06).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ADD3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 56 in all, 23 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 54 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 22 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5345.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.20×** | +14.8 | 0e+00 | 38/46 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.80×** | +13.1 | 1e-36 | 43/46 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.60×** | +11.7 | 3e-29 | 36/45 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.89×** | +11.4 | 4e-28 | 35/45 (PANC-1, A549, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +9.0 | 2e-17 | 31/47 (NCI-H1792, A549, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.96×** | +8.5 | 1e-15 | 31/47 (SW480, PANC-1, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.93×** | +8.4 | 5e-15 | 36/47 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **1.90×** | +8.1 | 3e-14 | 30/46 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | **1.88×** | +7.7 | 6e-13 | 12/21 (NCI-H1792, A498, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.83×** | +7.7 | 9e-13 | 30/47 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.81×** | +7.5 | 3e-12 | 32/47 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.84×** | +7.5 | 4e-12 | 32/46 (NCI-H1792, LoVo, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.79×** | +7.4 | 6e-12 | 31/47 (HOP62, PANC-1, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change | **1.78×** | +7.3 | 8e-12 | 25/36 (NCI-H1792, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.78×** | +7.0 | 8e-11 | 29/37 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.70×** | +6.7 | 5e-10 | 30/47 (NCI-H2030, HS-578T, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +5.6 | 7e-07 | 20/48 (HOP62, NCI-H2347, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.47×** | +4.6 | 9e-05 | 20/45 (NCI-H2347, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.97×** | +4.5 | 2e-04 | 16/43 (CFPAC-1, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.92×** | +4.3 | 3e-04 | 15/41 (NCI-H1573, J82, …) | top dose only | noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.39×** | +4.2 | 6e-04 | 15/44 (C32, SW1417, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.77×** | +3.8 | 0.003 | 10/45 (SW480, NCI-H2030, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5345.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.717×** | -4.2 | 0.007 | 17/48 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.718×** | -4.2 | 0.007 | 11/47 (LoVo, NCI-H2030, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **0.743×** | -3.8 | 0.030 | 13/47 (C32, CFPAC-1, …) | all doses, flat |  |
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | **0.751×** | -3.5 | 0.064 | 7/47 (AN3 CA, J82, …) | top dose only | plate-row cell shift |
| [[Trametinib (drug)]] 0.5 µM |  | **0.809×** | -3.4 | 0.066 | 13/48 (HEC-1-A, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.777× | -3.2 | 0.12 | 8/47 (MIA PaCa-2, LoVo, …) | inconsistent across doses | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | 0.803× | -3.2 | 0.13 | 12/48 (SW480, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | 0.781× | -3.0 | 0.18 | 17/46 (J82, NCI-H2030, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.53 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5345. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 12.0 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.87× (z +10.4) | — |
| [[A549 (line)]] | wt | 11.5 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +9.4) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 5.20× (z +8.6) | — |
| [[NCI-H1792 (line)]] | alt | 8.83 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 12.6× (z +11.4) | — |
| [[NCI-H2030 (line)]] | alt | 25.1 | 3 | 0 | [[Harringtonine (drug)]] 0.5 µM 3.50× (z +9.5) | — |
| [[CFPAC-1 (line)]] | alt | 5.72 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 8.12× (z +8.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 18.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.05 µM 4.46× (z +8.7) | [[Adagrasib (drug)]] 0.05 µM 0.636× (z -9.2) ⚠ position not correctable |
| [[SW480 (line)]] | alt | 26.4 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 4.61× (z +11.5) | — |
| [[BT-474 (line)]] | alt | 8.10 | 0 | 1 | — | [[Irinotecan (hydrochloride) (drug)]] 0.05 µM 0.0719× (z -9.5) |
| [[C32 (line)]] | wt | 5.52 | 0 | 1 | — | [[Tetracycline (hydrochloride) (drug)]] 0.05 µM 0.0567× (z -9.4) |
| [[HepG2_C3A (line)]] | wt | 13.0 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.106× (z -8.9) |
| [[HOP62 (line)]] | alt | 8.02 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.12× (z +8.8) | — |
| [[J82 (line)]] | alt | 14.4 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.213× (z -8.7) |
| [[LOX-IMVI (line)]] | wt | 13.0 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.05× (z +8.5) | — |
| [[SHP-77 (line)]] | alt | 28.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.143× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change |
| [[A-172 (line)]] | wt | 7.16 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.78 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.33 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.15 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.09 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.08 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5345), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPATCH4]] | +0.78 | +0.81 / +0.76 | both halves | 7e-06 |  |
| [[DHX37]] | +0.78 | +0.82 / +0.71 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 609 |
| [[RRS1]] | +0.78 | +0.77 / +0.83 | both halves | 7e-06 | same gene group; STRING 987 |
| [[GRWD1]] | +0.77 | +0.73 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2; STRING 919 |
| [[TRMT61A]] | +0.77 | +0.75 / +0.80 | both halves | 7e-06 | STRING 587 |
| [[CCDC86]] | +0.76 | +0.75 / +0.76 | both halves | 7e-06 | STRING 655 |
| [[PUS1]] | +0.76 | +0.81 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2 |
| [[BYSL]] | +0.75 | +0.71 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2; STRING 952 |
| [[MRTO4]] | +0.75 | +0.70 / +0.79 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MYC_TARGETS_V2; STRING 999 |
| [[NOP16]] | +0.74 | +0.73 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2; STRING 823 |
| [[PPIL1]] | +0.74 | +0.73 / +0.75 | both halves | 7e-06 |  |
| [[NDUFAF4]] | +0.74 | +0.70 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2 |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUCB2]] | -0.74 | -0.70 / -0.71 | both halves | 7e-06 |  |
| [[ARL3]] | -0.68 | -0.74 / -0.58 | both halves | 7e-06 |  |
| [[GTF2IP4]] | -0.67 | -0.62 / -0.64 | both halves | 7e-06 |  |
| [[PLEKHH3]] | -0.66 | -0.74 / -0.55 | both halves | 1e-05 |  |
| [[SRP54-AS1]] | -0.65 | -0.72 / -0.58 | both halves | 7e-06 |  |
| [[KDELR1]] | -0.64 | -0.69 / -0.55 | both halves | 1e-05 |  |
| [[ANG]] | -0.64 | -0.65 / -0.53 | both halves | 1e-05 |  |
| [[SARAF]] | -0.63 | -0.60 / -0.60 | both halves | 7e-06 |  |
| [[SLC25A23]] | -0.63 | -0.66 / -0.54 | both halves | 1e-05 |  |
| [[PJA2]] | -0.62 | -0.71 / -0.51 | both halves | 1e-05 |  |
| [[PPP1R2]] | -0.62 | -0.70 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADD3]] | B | ADD3 activity lowers NIP7's level | lines that do not express ADD3 (5) vs lines expressing it (45) | 1.59× higher at baseline in the lines without ADD3 | 0.025 | ⚠ within organs, on part of the lines; also absent: LINC02842, ADD3-AS1, WWC3 |
| [[PUDP]] | C | PUDP activity lowers NIP7's level | lines that do not express PUDP (4) vs lines expressing it (46) | 1.84× higher at baseline in the lines without PUDP | 0.087 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF264, ENSG00000287188 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.781). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-15.9, -36.4); signed map (-0.7, -45.6). **Vector** length 82.9, 18.3% of its response variance represented; |z| ≥ 3 in 1,071 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA modification in the nucleus and cytosol* (reactome, mean cos +0.64 to 11); *tRNA modification in the nucleus and cytosol* (reactome, mean cos +0.60 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +6.2 | +13.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.2 | +14.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.9 | +6.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.9 | +7.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.0 | +7.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | +5.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +8.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.7 | +3.3 |
| fall | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -2.5 | -4.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.3 | -1.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.0 | -3.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.0 | -0.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | -2.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.9 | -3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | nucleolar pre-rRNA processing protein NIP7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:69,337,996-69,343,106 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-37, FLJ10296, HSPC031, KD93 |
| Gene groups (HGNC) | Ribosome biogenesis factors |
| Hallmark sets | MYC_TARGETS_V2 |
| Reactome | 4 pathways, smallest: Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol; rRNA processing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y221](https://www.uniprot.org/uniprotkb/Q9Y221) (60S ribosome subunit biogenesis protein NIP7 homolog):

> Required for proper 34S pre-rRNA processing and 60S ribosome subunit assembly.

**Summary**, from NCBI Gene [51388](https://www.ncbi.nlm.nih.gov/gene/51388):

> Enables RNA binding activity. Predicted to be involved in ribosomal large subunit biogenesis. Located in nucleolus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24328](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24328) · Entrez [51388](https://www.ncbi.nlm.nih.gov/gene/51388) · UniProt [Q9Y221](https://www.uniprot.org/uniprotkb/Q9Y221) · Ensembl [ENSG00000132603](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132603)

## Data

Gene col 5345: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5345); `tables/drug_effects.parquet` (64 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5345, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5345]; `tensor/DDL_lfc|DDL_z.npy` [5345]; `embed/gene_vectors.npy` [5345]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5345 or target_col == 5345). Every well: [[NIP7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NIP7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
