---
symbol: "HEATR3"
type: "gene"
col: 7894
ensembl_id: "ENSG00000155393"
name: "HEAT repeat containing 3"
location: "16q12.1"
module: 18
arm: "+"
pooled_cpm: 15.42
n_lines_expressing: 49
n_dd_up: 30
n_dd_down: 6
n_dd_up_clean: 19
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# HEATR3

*HEAT repeat containing 3* — 16q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.11× (z +12.0, q 2e-30, up in 35 of 46 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 1.53× (z +6.8, q 8e-10, up in 27 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.761× (z -4.4, q 0.006, down in 16 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FXN]] (+0.77, fdr 7e-06), [[PGAM5]] (+0.73, fdr 7e-06), [[GOT2]] (+0.71, fdr 7e-06); moves opposite to [[SLU7]] (-0.65, fdr 1e-05), [[OSER1-DT]] (-0.63, fdr 3e-05), [[FAM117A]] (-0.62, fdr 3e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TSEN2]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 12 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7894.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.11×** | +12.0 | 2e-30 | 35/46 (SW480, A-172, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.09×** | +11.4 | 2e-27 | 21/28 (LoVo, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **2.01×** | +11.2 | 8e-27 | 27/39 (MIA PaCa-2, A498, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.95×** | +10.7 | 1e-24 | 39/46 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.92×** | +10.5 | 2e-23 | 34/46 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.85×** | +9.9 | 5e-21 | 36/46 (SW480, A-172, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **1.63×** | +7.6 | 4e-12 | 27/40 (SW480, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.53×** | +6.8 | 8e-10 | 27/46 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +6.7 | 2e-09 | 20/44 (SW480, SNU-423, …) | top dose only | cell-cycle shift (explains ~25% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.39×** | +5.3 | 8e-06 | 18/45 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[venetoclax (drug)]] 5 µM |  | **1.73×** | +4.6 | 2e-04 | 12/42 (NCI-H460, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.72×** | +4.5 | 3e-04 | 11/46 (NCI-H460, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.31×** | +4.4 | 5e-04 | 16/46 (HT-29, C32, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +4.3 | 6e-04 | 18/47 (LOX-IMVI, SW480, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.30×** | +4.2 | 0.001 | 12/44 (NCI-H1573, NCI-H2030, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | **1.20×** | +4.2 | 0.001 | 14/47 (PANC-1, CHP-212, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.63×** | +4.1 | 0.001 | 13/45 (NCI-H460, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.61×** | +4.0 | 0.002 | 10/45 (A498, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.60×** | +4.0 | 0.002 | 12/45 (NCI-H460, A498, …) | top dose only | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.58×** | +3.8 | 0.004 | 9/47 (HT-29, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.26×** | +3.5 | 0.012 | 15/46 (NCI-H23, NCI-H1792, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.25×** | +3.5 | 0.012 | 16/45 (SW480, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.24×** | +3.5 | 0.013 | 9/46 (NCI-H1573, SW 1271, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7894.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.761×** | -4.4 | 0.006 | 16/46 (KATO III, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.774×** | -4.1 | 0.007 | 18/46 (SW1417, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Artesunate (drug)]] 0.5 µM |  | **0.774×** | -4.1 | 0.007 | 9/47 (H4, KATO III, …) | two highest doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.789×** | -3.8 | 0.019 | 11/47 (PANC-1, CFPAC-1, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.653×** | -3.6 | 0.037 | 12/46 (A-427, COLO 205, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | 0.858× | -3.5 | 0.043 | 13/47 (PANC-1, LS 180, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.864× | -3.4 | 0.063 | 20/45 (NCI-H460, NCI-H2030, …) | top dose only | composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.821×** | -3.2 | 0.099 | 13/46 (A-427, SW480, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.877× | -3.0 | 0.16 | 15/46 (SNU-1, NCI-H23, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.44 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7894. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 28.0 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.128× (z -14.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.123× (z -10.7) |
| [[NCI-H460 (line)]] | wt | 22.0 | 1 (1 ⚠) | 2 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.90× (z +8.5) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -15.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.280× (z -10.3) |
| [[A498 (line)]] | wt | 15.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.04× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | [[Selinexor (drug)]] 5 µM 0.463× (z -8.5) ⚠ cell-cycle shift, explains ~55% of this change |
| [[AN3 CA (line)]] | alt | 30.6 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0884× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 19.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.174× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change |
| [[J82 (line)]] | alt | 19.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 15.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.328× (z -11.8) ⚠ cell-cycle shift, explains ~55% of this change |
| [[LOX-IMVI (line)]] | wt | 13.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 26.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.65× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[NCI-H2030 (line)]] | alt | 26.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -14.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 13.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 22.4 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.44× (z +9.7) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[A-172 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.59 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.36 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.44 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.22 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.76 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.05 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7894), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FXN]] | +0.77 | +0.71 / +0.76 | both halves | 7e-06 |  |
| [[PGAM5]] | +0.73 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[GOT2]] | +0.71 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[PTGES2]] | +0.70 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[RIOX2]] | +0.69 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[LETM1]] | +0.68 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[TCOF1]] | +0.68 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[VWA8]] | +0.68 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[MRPL3]] | +0.68 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[PPP5C]] | +0.67 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[PMS1]] | +0.67 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[POLR3B]] | +0.66 | +0.61 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLU7]] | -0.65 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[OSER1-DT]] | -0.63 | -0.43 / -0.57 | both halves | 3e-05 |  |
| [[FAM117A]] | -0.62 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[HLA-A]] | -0.60 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[MICU1]] | -0.59 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[GCC2]] | -0.59 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[HLA-E]] | -0.58 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[AAMDC]] | -0.58 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[RSRP1]] | -0.57 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[YPEL5]] | -0.57 | -0.44 / -0.61 | both halves | 3e-05 |  |
| [[ZFYVE1]] | -0.57 | -0.64 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TSEN2]] | C | TSEN2 activity raises HEATR3's level | lines that do not express TSEN2 (3) vs lines expressing it (47) | 2.40× lower at baseline in the lines without TSEN2 | 0.094 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TMEM9B-AS1, NDC80, CSPG5; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.665). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-10.6, -39.7); signed map (-9.3, -52.4). **Vector** length 88.4, 18.4% of its response variance represented; |z| ≥ 3 in 883 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.1 | +10.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +3.2 | +6.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.9 | +3.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.9 | +4.1 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.9 | +4.6 |
|  | [[EX229 (drug)]] 5 µM |  | +2.8 | +4.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.7 | +4.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.1 | -3.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.5 | -3.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | -3.7 | -1.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | -2.6 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | -3.1 | -3.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.9 | -1.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.7 | -3.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -4.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.7 | -0.9 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.5 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | HEAT repeat containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q12.1 — chr16:50,065,967-50,107,272 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20718 |
| Gene groups (HGNC) | Armadillo like helical domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z4Q2](https://www.uniprot.org/uniprotkb/Q7Z4Q2) (HEAT repeat-containing protein 3):

> Plays a role in ribosome biogenesis and in nuclear import of the 60S ribosomal protein L5/large ribosomal subunit protein uL18 (RPL5). Required for proper erythrocyte maturation.

**Summary**, from NCBI Gene [55027](https://www.ncbi.nlm.nih.gov/gene/55027):

> The protein encoded by this gene plays a role in ribosomal protein transport and in the assembly of the 5S ribonucleoprotein particle (5S RNP). The encoded protein also may be involved in NOD2-mediated NF-kappaB signaling. [provided by RefSeq, Jul 2016]

**Accessions** — [HGNC:26087](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26087) · Entrez [55027](https://www.ncbi.nlm.nih.gov/gene/55027) · UniProt [Q7Z4Q2](https://www.uniprot.org/uniprotkb/Q7Z4Q2) · Ensembl [ENSG00000155393](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155393)

## Data

Gene col 7894: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7894); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7894, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7894]; `tensor/DDL_lfc|DDL_z.npy` [7894]; `embed/gene_vectors.npy` [7894]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7894 or target_col == 7894). Every well: [[HEATR3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HEATR3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
