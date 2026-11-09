---
symbol: "HOXB4"
type: "gene"
col: 11320
ensembl_id: "ENSG00000182742"
name: "homeobox B4"
location: "17q21.32"
module: 201
arm: "+"
pooled_cpm: 10.27
n_lines_expressing: 38
n_dd_up: 6
n_dd_down: 26
n_dd_up_clean: 2
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 2
direction_downstream: 7
tags: ["gene", "module/201"]
generated_by: "tahoemap"
---

# HOXB4

*homeobox B4* — 17q21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.94× (z +12.6, q 1e-33, up in 23 of 32 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SW1417 2.52×, HEC-1-A 3.78×).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.424× (z -11.5, q 5e-28, down in 25 of 36 measured lines).
> Its strongest partners by |cos| (79 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 28 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HOXB3]] (+0.79, fdr 7e-06, ⚠ same locus), [[HOXB6]] (+0.71, fdr 7e-06, ⚠ same locus), [[HOXB-AS3]] (+0.69, fdr 1e-05, ⚠ same locus), [[CDC14A]] (+0.61, fdr 3e-05), [[TIAL1]] (+0.60, fdr 5e-04), [[HOXA10]] (+0.58, fdr 9e-05); moves opposite to [[GALNS]] (-0.54, fdr 4e-04), [[FAAP100]] (-0.53, fdr 2e-04), [[BCL7B]] (-0.52, fdr 1e-04).
> It is in [[Module 201]], a single-armed module (Kidney development).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HOXC10]] → it (grade B ⚠); 7 go from it, the strongest it → [[HOXB-AS3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11320.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SW1417 2.52×, HEC-1-A 3.78×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.94×** | +12.6 | 1e-33 | 23/32 (SW1417, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.38×** | +6.1 | 2e-07 | 16/35 (C32, SW1417, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.46×** | +5.1 | 5e-05 | 8/25 (HEC-1-A, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +5.1 | 5e-05 | 14/31 (RKO, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.38×** | +4.2 | 0.004 | 1/12 (HOP62) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.31×** | +3.6 | 0.027 | 10/35 (PANC-1, A498, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.26× | +3.2 | 0.13 | 4/34 (KATO III, NCI-H1573, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11320.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.424×** | -11.5 | 5e-28 | 25/36 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.473×** | -10.0 | 3e-21 | 22/35 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.581×** | -7.3 | 6e-11 | 16/35 (AsPC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.619×** | -6.4 | 2e-08 | 19/34 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.642×** | -6.0 | 3e-07 | 18/35 (PANC-1, SW480, …) | top dose only | cell-cycle shift (explains ~20% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.660×** | -5.6 | 2e-06 | 15/34 (NCI-H1573, SW480, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.651×** | -5.5 | 3e-06 | 18/30 (RKO, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.677×** | -5.2 | 1e-05 | 18/34 (HCT15, C32, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.678×** | -5.2 | 1e-05 | 16/31 (hTERT-HPNE, A498, …) | two highest doses | cell-cycle shift (explains ~10% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.494×** | -5.0 | 4e-05 | 14/34 (PANC-1, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.698×** | -4.8 | 7e-05 | 17/35 (LoVo, PANC-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.703×** | -4.5 | 3e-04 | 14/33 (MIA PaCa-2, A498, …) | two highest doses | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.716×** | -4.5 | 3e-04 | 17/35 (NCI-H1573, SNU-423, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.718×** | -4.4 | 4e-04 | 16/33 (HOP62, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.796×** | -4.3 | 6e-04 | 15/30 (hTERT-HPNE, A498, …) | two highest doses | composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.761×** | -3.7 | 0.009 | 10/34 (C-33 A, SW48, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.594×** | -3.7 | 0.009 | 11/32 (hTERT-HPNE, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **0.765×** | -3.5 | 0.018 | 13/34 (SNU-423, PANC-1, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.767×** | -3.4 | 0.019 | 10/34 (CFPAC-1, HT-29, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.764×** | -3.4 | 0.019 | 15/34 (HCT15, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.795×** | -3.1 | 0.053 | 7/35 (HT-29, PANC-1, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11320. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 36.5 | 0 | 9 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.251× (z -14.9) |
| [[hTERT-HPNE (line)]] | wt | 29.1 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -12.0) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.163× (z -9.5) |
| [[HCT15 (line)]] | alt | 29.7 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0516× (z -15.4) |
| [[SW1417 (line)]] | alt | 25.3 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +10.2) | [[Panobinostat (drug)]] 0.5 µM 0.191× (z -12.8) |
| [[SW480 (line)]] | alt | 29.7 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.140× (z -17.5) |
| [[NCI-H1573 (line)]] | alt | 6.13 | 0 | 2 (1 ⚠) | — | [[Citalopram (hydrobromide) (drug)]] 0.5 µM 0.0874× (z -9.8) |
| [[RKO (line)]] | wt | 8.68 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -8.6) ⚠ cell-cycle shift, explains ~53% of this change |
| [[A-172 (line)]] | wt | 13.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -11.6) ⚠ cell-cycle shift, explains ~53% of this change |
| [[A498 (line)]] | wt | 15.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -11.7) ⚠ cell-cycle shift, explains ~53% of this change |
| [[C32 (line)]] | wt | 5.97 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0584× (z -10.4) |
| [[COLO 205 (line)]] | alt | 16.9 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.0340× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 6.87 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.78× (z +9.7) | — |
| [[HOP62 (line)]] | alt | 3.47 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0772× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[HT-29 (line)]] | alt | 18.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.125× (z -13.2) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 10.1 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.237× (z -8.7) ⚠ unreliable plate only |
| [[MIA PaCa-2 (line)]] | alt | 5.43 | 0 | 1 | — | [[LJI308 (drug)]] 0.05 µM 0.100× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 5.38 | 0 | 1 | — | [[Ivermectin (drug)]] 0.5 µM 0.0608× (z -9.1) |
| [[A-427 (line)]] | wt | 7.47 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.03 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.776 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.29 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.827 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.872 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.75 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.15 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.29 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.21 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.930 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.01 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11320), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 24 of them with an alert (⚠; 17 not replicated); shown: the 12 strongest and the 8 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOXB3]] | +0.79 | +0.66 / +0.77 | both halves | 7e-06 | same gene group; pathway: Activation of HOX genes during differentiation; STRING 887; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[HOXB6]] | +0.71 | +0.59 / +0.66 | both halves | 7e-06 | same gene group; STRING 915; ⚠ same locus (17.4 kb, same strand: neighbours can correlate without regulation) |
| [[HOXB-AS3]] | +0.69 | +0.61 / +0.56 | both halves | 1e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[HOXB5]] | +0.68 | +0.62 / +0.67 | both halves | 7e-06 | same gene group; STRING 958; ⚠ same locus (12.9 kb, same strand: neighbours can correlate without regulation) |
| [[HOXB7]] | +0.64 | +0.48 / +0.55 | both halves | 2e-05 | same gene group; STRING 890; ⚠ same locus (28.9 kb, same strand: neighbours can correlate without regulation) |
| [[HOXB-AS1]] | +0.62 | +0.41 / +0.57 | both halves | 4e-05 | ⚠ same locus (24.3 kb: neighbours can correlate without regulation) |
| [[CDC14A]] | +0.61 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[TIAL1]] | +0.60 | +0.24 / +0.65 | both halves | 5e-04 |  |
| [[HOXA10]] | +0.58 | +0.36 / +0.59 | both halves | 9e-05 | same gene group |
| [[PRRT1]] | +0.56 | +0.26 / +0.60 | both halves | 4e-04 |  |
| [[CD27-AS1]] | +0.56 | +0.16 / +0.55 | ⚠ one half (not replicated) | 0.001 |  |
| [[HOXB8]] | +0.56 | +0.51 / +0.40 | both halves | 5e-05 | same gene group; STRING 561; ⚠ same locus (33.0 kb, same strand: neighbours can correlate without regulation) |
| [[HOTAIR]] | +0.55 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[IRF3]] | +0.55 | +0.31 / +0.52 | both halves | 2e-04 |  |
| [[SATB2-AS1]] | +0.54 | +0.41 / +0.47 | both halves | 4e-05 |  |
| [[ZNF821]] | +0.54 | +0.26 / +0.54 | both halves | 3e-04 |  |
| [[TAPT1]] | +0.54 | +0.29 / +0.44 | both halves | 2e-04 |  |
| [[HOXC8]] | +0.54 | +0.35 / +0.46 | both halves | 1e-04 | same gene group |
| [[ARID4B]] | +0.53 | +0.30 / +0.46 | both halves | 2e-04 |  |
| [[HOXA3]] | +0.53 | +0.28 / +0.53 | both halves | 3e-04 | same gene group; pathway: Activation of HOX genes during differentiation; STRING 443 |

## Genes that move opposite

*18 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GALNS]] | -0.54 | -0.25 / -0.51 | both halves | 4e-04 |  |
| [[FAAP100]] | -0.53 | -0.30 / -0.49 | both halves | 2e-04 |  |
| [[BCL7B]] | -0.52 | -0.35 / -0.46 | both halves | 1e-04 |  |
| [[STK25]] | -0.51 | -0.26 / -0.52 | both halves | 4e-04 |  |
| [[EEFSEC]] | -0.50 | -0.26 / -0.46 | both halves | 3e-04 |  |
| [[RNF123]] | -0.50 | -0.19 / -0.46 | ⚠ not reproduced | 8e-04 |  |
| [[DTD1]] | -0.49 | -0.39 / -0.35 | both halves | 1e-04 |  |
| [[MTG1]] | -0.48 | -0.31 / -0.35 | both halves | 2e-04 |  |
| [[ACSF3]] | -0.48 | -0.14 / -0.54 | ⚠ one half (not replicated) | 0.002 |  |
| [[PRKCZ]] | -0.48 | -0.24 / -0.38 | both halves | 4e-04 |  |
| [[SLC39A3]] | -0.46 | -0.23 / -0.33 | both halves | 5e-04 |  |
| [[CLTCL1]] | -0.46 | -0.25 / -0.28 | both halves | 4e-04 |  |
| [[ATP9B]] | -0.46 | -0.25 / -0.54 | both halves | 4e-04 |  |
| [[GPRIN1]] | -0.45 | -0.22 / -0.35 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOXC10]] | B | HOXC10 activity raises HOXB4's level | lines that do not express HOXC10 (26) vs lines expressing it (24) | 1.40× lower at baseline in the lines without HOXC10 | 0.069 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: NTRK3, CES1, POTEE |
| [[MEIS2]] | C | MEIS2 activity raises HOXB4's level | lines that do not express MEIS2 (4) vs lines expressing it (46) | 1.28× lower at baseline in the lines without MEIS2 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; maybe low, not absent; its own permutation p |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOXB-AS3]] | B | HOXB4 activity raises HOXB-AS3's level | lines that do not express HOXB4 (12) vs lines expressing it (38) | 1.72× lower at baseline in the lines without HOXB4 | 0.019 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[HOXB-AS1]] | B | HOXB4 activity raises HOXB-AS1's level | lines that do not express HOXB4 (12) vs lines expressing it (38) | 1.92× lower at baseline in the lines without HOXB4 | 0.026 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[HOXB8]] | B | HOXB4 activity raises HOXB8's level | lines that do not express HOXB4 (12) vs lines expressing it (38) | 2.15× lower at baseline in the lines without HOXB4 | 0.055 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[HOXB3]] | B | HOXB4 activity raises HOXB3's level | lines that do not express HOXB4 (12) vs lines expressing it (38) | 3.54× lower at baseline in the lines without HOXB4 | 0.057 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[GALNS]] | B | HOXB4 activity raises GALNS's level | lines that do not express HOXB4 (12) vs lines expressing it (38) | 1.30× lower at baseline in the lines without HOXB4 | 0.074 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[HOXC10]] | B | HOXB4 activity raises HOXC10's level | lines that do not express HOXB4 (12) vs lines expressing it (38) | 1.59× lower at baseline in the lines without HOXB4 | 0.091 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[LINC00938]] | B | HOXB4 activity raises LINC00938's level | lines that do not express HOXB4 (12) vs lines expressing it (38) | 1.10× lower at baseline in the lines without HOXB4 | 0.0996 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 201]] — Kidney development; 15 genes; every member is in the + arm (projection on the module's main direction 0.794). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-1.0, 26.6); signed map (39.2, -4.1). **Vector** length 53.3, 7.99% of its response variance represented; |z| ≥ 3 in 797 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +12.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +3.6 | +6.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +5.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | +2.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.0 | +2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +0.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.0 | +2.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +0.9 | +2.1 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +0.8 | +0.7 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +0.8 | +1.9 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -3.6 | -11.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.4 | -10.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | -5.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.2 | -3.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.2 | -4.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.5 | -3.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.5 | -2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.2 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | homeobox B4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.32 — chr17:48,575,507-48,578,350 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously HOX2, HOX2F |
| Gene groups (HGNC) | HOXL subclass homeoboxes |
| Reactome | 4 pathways, smallest: Formation of the nephric duct; Kidney development; Activation of HOX genes during differentiation |
| Matched by | ensembl_id |

**Function**, from UniProt [P17483](https://www.uniprot.org/uniprotkb/P17483) (Homeobox protein Hox-B4):

> Sequence-specific transcription factor which is part of a developmental regulatory system that provides cells with specific positional identities on the anterior-posterior axis.

**Summary**, from NCBI Gene [3214](https://www.ncbi.nlm.nih.gov/gene/3214):

> This gene is a member of the Antp homeobox family and encodes a nuclear protein with a homeobox DNA-binding domain. It is included in a cluster of homeobox B genes located on chromosome 17. The encoded protein functions as a sequence-specific transcription factor that is involved in development. Intracellular or ectopic expression of this protein expands hematopoietic stem and progenitor cells in vivo and in vitro, making it a potential candidate for therapeutic stem cell expansion. [provided …

**Accessions** — [HGNC:5115](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5115) · Entrez [3214](https://www.ncbi.nlm.nih.gov/gene/3214) · UniProt [P17483](https://www.uniprot.org/uniprotkb/P17483) · Ensembl [ENSG00000182742](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182742)

## Data

Gene col 11320: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11320); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11320, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11320]; `tensor/DDL_lfc|DDL_z.npy` [11320]; `embed/gene_vectors.npy` [11320]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11320 or target_col == 11320). Every well: [[HOXB4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HOXB4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
