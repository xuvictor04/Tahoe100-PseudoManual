---
symbol: "TAGAP-AS1"
type: "gene"
col: 15701
ensembl_id: "ENSG00000271913"
name: "TAGAP antisense RNA 1"
location: "6q25.3"
module: 15
arm: "+"
pooled_cpm: 10.91
n_lines_expressing: 50
n_dd_up: 32
n_dd_down: 30
n_dd_up_clean: 28
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# TAGAP-AS1

*TAGAP antisense RNA 1* — 6q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.65× (z +16.7, q 0e+00, up in 41 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (11 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.340× (z -13.2, q 8e-37, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DDX59-AS1]] (+0.70, fdr 7e-06), [[DMXL1-DT]] (+0.68, fdr 9e-06), [[BRPF3-AS1]] (+0.67, fdr 7e-06); moves opposite to [[IPO9]] (-0.57, fdr 9e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15701.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.65×** | +16.7 | 0e+00 | 41/45 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.00×** | +8.4 | 2e-14 | 35/48 (HEC-1-A, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +6.2 | 1e-07 | 24/44 (A498, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.62×** | +5.9 | 7e-07 | 25/48 (A-172, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.56×** | +5.4 | 9e-06 | 25/48 (A498, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.53×** | +4.9 | 8e-05 | 17/46 (NCI-H23, A-172, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +4.8 | 1e-04 | 20/48 (KATO III, A-172, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.48×** | +4.7 | 2e-04 | 20/47 (A498, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.55×** | +4.6 | 2e-04 | 13/48 (A498, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.31×** | +4.6 | 2e-04 | 19/48 (A-427, AsPC-1, …) | rises with dose | low cells (technical?) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.45×** | +4.5 | 3e-04 | 17/47 (A-172, CFPAC-1, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.45×** | +4.5 | 3e-04 | 10/46 (A-172, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +4.5 | 3e-04 | 12/48 (HOP62, Panc 03.27, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +4.4 | 4e-04 | 21/46 (SW480, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.42×** | +4.2 | 9e-04 | 12/48 (SW480, C-33 A, …) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.36×** | +3.9 | 0.004 | 9/48 (MIA PaCa-2, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15701.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.340×** | -13.2 | 8e-37 | 42/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.406×** | -11.0 | 1e-25 | 36/47 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.447×** | -9.4 | 7e-19 | 29/47 (PANC-1, LOX-IMVI, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.477×** | -8.7 | 5e-16 | 28/41 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.492×** | -8.7 | 5e-16 | 29/45 (NCI-H23, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.500×** | -8.5 | 3e-15 | 32/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.515×** | -8.1 | 4e-14 | 28/47 (Panc 03.27, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.353×** | -6.6 | 2e-09 | 24/48 (A-427, SNU-423, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.607×** | -6.1 | 7e-08 | 21/47 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.423×** | -5.5 | 2e-06 | 19/43 (PANC-1, SNU-423, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.628×** | -5.0 | 3e-05 | 16/48 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.693×** | -4.5 | 3e-04 | 18/47 (MIA PaCa-2, SNU-423, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.707×** | -4.2 | 9e-04 | 16/45 (SNU-1, COLO 205, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.784×** | -4.2 | 9e-04 | 19/48 (Panc 03.27, NCI-H23, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change | **0.722×** | -4.0 | 0.003 | 14/37 (SW480, A-172, …) | inconsistent across doses | composition shift; position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.573×** | -3.6 | 0.011 | 10/46 (HCT15, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.738×** | -3.5 | 0.012 | 14/46 (AN3 CA, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.683×** | -3.3 | 0.023 | 9/48 (NCI-H23, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.613×** | -3.1 | 0.045 | 8/44 (SK-MEL-2, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.776×** | -3.1 | 0.046 | 9/47 (NCI-H2030, NCI-H23, …) | rises with dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.774×** | -3.0 | 0.056 | 5/47 (PANC-1, A498, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15701. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 17.8 | 1 | 10 (7 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.0465× (z -23.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.135× (z -15.9) |
| [[A-172 (line)]] | wt | 22.8 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -11.2) ⚠ cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 26.6 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.140× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.225× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 23.9 | 1 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +8.5) ⚠ cell-cycle shift, would explain all of this change | [[Digitoxin (drug)]] 5 µM 0.0828× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.210× (z -10.0) |
| [[SW480 (line)]] | alt | 13.8 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.38× (z +12.3) | [[Dinaciclib (drug)]] 0.5 µM 0.147× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.275× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 16.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -10.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.223× (z -9.4) |
| [[LOX-IMVI (line)]] | wt | 6.48 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0556× (z -11.3) ⚠ cell-cycle shift, explains ~35% of this change |
| [[RKO (line)]] | wt | 5.85 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.62× (z +9.5) | [[Vismodegib (drug)]] 0.5 µM 0.0612× (z -9.3) |
| [[SNU-423 (line)]] | alt | 17.9 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.166× (z -8.8) ⚠ cell-cycle shift, explains ~41% of this change |
| [[A498 (line)]] | wt | 5.30 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.96× (z +10.2) | — |
| [[A549 (line)]] | wt | 4.53 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0786× (z -8.9) |
| [[HOP62 (line)]] | alt | 9.11 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.47× (z +8.6) | — |
| [[HS-578T (line)]] | alt | 9.67 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0384× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[LoVo (line)]] | wt | 7.81 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.4× (z +17.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[LS 180 (line)]] | wt | 7.92 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.22× (z +8.5) | — |
| [[NCI-H460 (line)]] | wt | 5.60 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.94× (z +9.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[Panc 03.27 (line)]] | alt | 11.2 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.161× (z -8.7) |
| [[SW 900 (line)]] | alt | 8.08 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0960× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[A-427 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.57 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.41 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.53 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.81 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.64 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.82 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.33 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.46 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.95 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15701), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX59-AS1]] | +0.70 | +0.75 / +0.66 | both halves | 7e-06 | same gene group |
| [[DMXL1-DT]] | +0.68 | +0.76 / +0.57 | both halves | 9e-06 |  |
| [[BRPF3-AS1]] | +0.67 | +0.66 / +0.63 | both halves | 7e-06 | same gene group |
| [[NIFK-AS1]] | +0.67 | +0.72 / +0.61 | both halves | 7e-06 | same gene group |
| [[EPM2A-DT]] | +0.67 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[UPP2]] | +0.67 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[CCDC18-AS1]] | +0.66 | +0.66 / +0.62 | both halves | 7e-06 | same gene group |
| [[C4orf47]] | +0.66 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[FKBP14-AS1]] | +0.66 | +0.66 / +0.55 | both halves | 1e-05 | same gene group |
| [[ELOA-AS1]] | +0.65 | +0.62 / +0.68 | both halves | 7e-06 | same gene group |
| [[LINC01301]] | +0.64 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[NSMCE1-DT]] | +0.64 | +0.75 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IPO9]] | -0.57 | -0.36 / -0.61 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TAGAP-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[DLK2]] | B | DLK2 activity raises TAGAP-AS1's level | lines that do not express DLK2 (13) vs lines expressing it (37) | 1.52× lower at baseline in the lines without DLK2 | 0.075 | ⚠ within organs, on part of the lines; also absent: ETNK2, CHROMR, DUSP15 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.596). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (4.5, 22.5); signed map (31.6, -6.3). **Vector** length 62.0, 10.6% of its response variance represented; |z| ≥ 3 in 1,147 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +16.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.5 | +6.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +3.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +5.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.7 | +1.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.5 | +4.2 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.5 | -8.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change | -3.2 | -4.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -2.8 | -9.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.8 | -6.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -2.7 | +0.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.4 | -1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.1 | -4.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.1 | -3.0 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -1.1 | -0.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.0 | +2.3 |

## What is on record

|  |  |
|---|---|
| Name | TAGAP antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 6q25.3 — chr6:158,988,178-159,088,114 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55239](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55239) · Entrez [105378083](https://www.ncbi.nlm.nih.gov/gene/105378083) · Ensembl [ENSG00000271913](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000271913)

## Data

Gene col 15701: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15701); `tables/drug_effects.parquet` (63 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15701, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15701]; `tensor/DDL_lfc|DDL_z.npy` [15701]; `embed/gene_vectors.npy` [15701]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15701 or target_col == 15701). Every well: [[TAGAP-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TAGAP-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
