---
symbol: "LRP4"
type: "gene"
col: 5578
ensembl_id: "ENSG00000134569"
name: "LDL receptor related protein 4"
location: "11p11.2"
module: 44
arm: "+"
pooled_cpm: 11.11
n_lines_expressing: 34
n_dd_up: 21
n_dd_down: 8
n_dd_up_clean: 12
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 7
direction_downstream: 7
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# LRP4

*LDL receptor related protein 4* — 11p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.00× (z +9.5, q 1e-18, up in 9 of 14 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 1.90× (z +9.2, q 9e-18, up in 15 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.626× (z -6.3, q 2e-07, down in 14 of 29 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.05 µM: 0.736× (z -4.4, q 0.003, down in 15 of 32 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ILDR2]] (+0.70, fdr 7e-06), [[FRMPD3]] (+0.64, fdr 8e-06), [[MUC3A]] (+0.60, fdr 7e-05); moves opposite to [[CLDN14-AS1]] (-0.49, fdr 2e-05), [[OSMR-DT]] (-0.49, fdr 4e-05), [[SMIM12]] (-0.48, fdr 6e-05).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[LINC02058]] → it (grade B ⚠); 7 go from it, the strongest it → [[PLEKHG6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5578.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.00×** | +9.5 | 1e-18 | 9/14 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.91×** | +9.3 | 6e-18 | 16/32 (PANC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.90×** | +9.2 | 9e-18 | 15/32 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.51×** | +8.3 | 1e-14 | 16/32 (HOP62, PANC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.78×** | +8.2 | 2e-14 | 15/31 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.75×** | +8.0 | 9e-14 | 18/32 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.74×** | +7.5 | 5e-12 | 13/31 (RKO, A498, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.61×** | +6.8 | 7e-10 | 10/24 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.64×** | +6.7 | 2e-09 | 9/30 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.56×** | +6.4 | 1e-08 | 15/32 (HOP62, RKO, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.56×** | +6.3 | 1e-08 | 13/32 (PANC-1, A549, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.21×** | +5.9 | 1e-07 | 13/32 (PANC-1, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.88×** | +4.7 | 1e-04 | 5/18 (RKO, A498, …) | all doses, flat | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.25×** | +4.6 | 2e-04 | 12/32 (NCI-H1792, Hs 766T, …) | top dose only | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.36×** | +4.4 | 4e-04 | 9/32 (SW480, HCT15, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.35×** | +4.3 | 6e-04 | 9/32 (LoVo, RKO, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.48×** | +4.0 | 0.002 | 10/32 (RKO, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.18× | +3.2 | 0.044 | 5/32 (LS 180, LoVo, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.25×** | +3.2 | 0.045 | 11/32 (RKO, HOP62, …) | rises with dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.25×** | +3.1 | 0.061 | 7/31 (LoVo, LS 180, …) | inconsistent across doses |  |
| [[Arbutin (drug)]] 0.5 µM |  | **1.22×** | +2.9 | 0.099 | 0/32 | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5578.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.626×** | -6.3 | 2e-07 | 14/29 (LoVo, COLO 205, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.736×** | -4.4 | 0.003 | 15/32 (MIA PaCa-2, RKO, …) | all doses, flat |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.748×** | -4.0 | 0.013 | 7/32 (MIA PaCa-2, HCT15, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.761×** | -3.9 | 0.014 | 11/32 (RKO, LS 180, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.756×** | -3.8 | 0.014 | 8/31 (COLO 205, LoVo, …) | rises with dose | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.782×** | -3.5 | 0.038 | 11/32 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.783×** | -3.5 | 0.038 | 12/32 (COLO 205, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.792×** | -3.3 | 0.061 | 13/30 (COLO 205, LoVo, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.855× | -3.2 | 0.10 | 13/32 (COLO 205, LoVo, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.798× | -3.0 | 0.13 | 9/30 (COLO 205, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.809× | -3.0 | 0.13 | 12/32 (COLO 205, LS 180, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5578. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 158 | 0 | 15 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0531× (z -20.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.0485× (z -14.8) |
| [[LoVo (line)]] | wt | 66.2 | 0 | 14 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -20.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.217× (z -11.0) |
| [[LS 180 (line)]] | wt | 27.8 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -13.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[vincristine (drug)]] 5 µM 0.0492× (z -8.5) |
| [[PANC-1 (line)]] | alt | 5.87 | 5 (4 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 8.13× (z +11.0) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Belinostat (drug)]] 5 µM 4.99× (z +8.8) | — |
| [[RKO (line)]] | wt | 21.1 | 1 (1 ⚠) | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 4.15× (z +8.7) ⚠ cell-cycle shift, explains ~30% of this change | [[Harringtonine (drug)]] 0.5 µM 0.161× (z -11.1) |
| [[HOP62 (line)]] | alt | 3.86 | 1 (1 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 10.5× (z +9.1) ⚠ cell-cycle shift, explains ~30% of this change | [[Fingolimod (hydrochloride) (drug)]] 5 µM 0.0543× (z -11.3) ⚠ toxic |
| [[HS-578T (line)]] | alt | 3.27 | 0 | 2 | — | [[8-Hydroxyquinoline (drug)]] 0.05 µM 0.0414× (z -10.2) |
| [[HepG2_C3A (line)]] | wt | 15.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.63× (z +9.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SK-MEL-2 (line)]] | alt | 5.21 | 0 | 1 | — | [[Dihydroartemisinin (drug)]] 0.5 µM 0.0671× (z -8.5) |
| [[A-172 (line)]] | wt | 5.76 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.89 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.31 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.920 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.39 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.59 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.22 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.52 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.57 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.89 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5578), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ILDR2]] | +0.70 | +0.61 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[FRMPD3]] | +0.64 | +0.57 / +0.62 | both halves | 8e-06 |  |
| [[MUC3A]] | +0.60 | +0.58 / +0.37 | both halves | 7e-05 |  |
| [[GPA33]] | +0.60 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[PRR15L]] | +0.59 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[USH1C]] | +0.58 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[PLEKHG6]] | +0.58 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[TMPRSS2]] | +0.57 | +0.61 / +0.46 | both halves | 3e-05 |  |
| [[PIK3C2B]] | +0.57 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[RAB15]] | +0.57 | +0.57 / +0.39 | both halves | 5e-05 |  |
| [[SORL1]] | +0.57 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[UGT8]] | +0.57 | +0.49 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLDN14-AS1]] | -0.49 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[OSMR-DT]] | -0.49 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[SMIM12]] | -0.48 | -0.39 / -0.41 | both halves | 6e-05 |  |
| [[CKMT2-AS1]] | -0.47 | -0.28 / -0.43 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02058]] | B | LINC02058 activity raises LRP4's level | lines that do not express LINC02058 (34) vs lines expressing it (16) | 2.90× lower at baseline in the lines without LINC02058 | 0.032 | ⚠ within organs, on part of the lines; also absent: LINC02253, ENSG00000260573, ST18; maybe low, not absent |
| [[KSR2]] | B | KSR2 activity weakens LRP4's drug response | lines that do not express KSR2 (13) vs lines expressing it (19) | the lines without KSR2 respond 6.81× as strongly (z diff -2.64); strongest at Ixazomib citrate 5 µM: 2.80x vs 1.00x (z diff -4.4) | 0.036 | ⚠ within organs, on part of the lines; also absent: SPTB, MYT1, YBX2; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[AXIN2]] | B | AXIN2 activity raises LRP4's level | lines that do not express AXIN2 (32) vs lines expressing it (18) | 2.66× lower at baseline in the lines without AXIN2 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LGR5, LINC02253, LINC02964 |
| [[WFDC10B]] | B | WFDC10B activity lowers LRP4's level | lines that do not express WFDC10B (20) vs lines expressing it (30) | 1.96× higher at baseline in the lines without WFDC10B | 0.061 | ⚠ within organs, on part of the lines; also absent: WFDC3, QPCT, LRRN1; maybe low, not absent |
| [[ERG]] | B | ERG activity raises LRP4's level | lines that do not express ERG (30) vs lines expressing it (20) | 1.59× lower at baseline in the lines without ERG | 0.075 | ⚠ within organs, on part of the lines; also absent: FUT9, ZIC1, MDGA2; maybe low, not absent |
| [[PCK1]] | B | PCK1 activity raises LRP4's level | lines that do not express PCK1 (38) vs lines expressing it (12) | 2.51× lower at baseline in the lines without PCK1 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LGR5, GPX2, CPLX2 |
| [[ERBB3]] | B | ERBB3 activity weakens LRP4's drug response | lines that do not express ERBB3 (21) vs lines expressing it (11) | (z diff -2.96); strongest at Dinaciclib 0.5 µM: 1.65x vs 0.42x (z diff -6.1) | 0.096 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM; target measured in part of the lines; artifact flags |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLEKHG6]] | B | LRP4 activity lowers PLEKHG6's level | lines that do not express LRP4 (16) vs lines expressing it (34) | 1.83× higher at baseline in the lines without LRP4 | 0.049 | ⚠ within organs, on part of the lines |
| [[ILDR2]] | B | LRP4 activity raises ILDR2's level | lines that do not express LRP4 (16) vs lines expressing it (34) | 1.75× lower at baseline in the lines without LRP4 | 0.050 | ⚠ within organs, on part of the lines |
| [[SEMA4D]] | B | LRP4 activity weakens SEMA4D's drug response | lines that do not express LRP4 (14) vs lines expressing it (27) | the lines without LRP4 respond 1.56× as strongly (z diff -1.42); strongest at Dinaciclib 0.05 µM: 0.41x vs 0.80x (z diff -4.5) | 0.058 | ⚠ within organs, on part of the lines; target measured in part of the lines; artifact flags |
| [[ERBB3]] | B | LRP4 activity lowers ERBB3's level | lines that do not express LRP4 (16) vs lines expressing it (34) | 2.08× higher at baseline in the lines without LRP4 | 0.069 | ⚠ within organs, on part of the lines |
| cells under [[Aliskiren (drug)]] 0.5 µM | B | LRP4 activity lowers the cells' numbers under Aliskiren 0.5 µM (makes them more sensitive) | lines that do not express LRP4 (16) vs lines expressing it (32) | the lines without LRP4: 1.18× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines |
| cells under [[Terfenadine (drug)]] 0.5 µM | B | LRP4 activity lowers the cells' numbers under Terfenadine 0.5 µM (makes them more sensitive) | lines that do not express LRP4 (16) vs lines expressing it (32) | the lines without LRP4: 1.24× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines |
| cells under [[Lonafarnib (drug)]] 0.05 µM | B | LRP4 activity raises the cells' numbers under Lonafarnib 0.05 µM (protects the cells) | lines that do not express LRP4 (16) vs lines expressing it (32) | the lines without LRP4: 0.88× the cells of the other lines | 0.094 | ⚠ within organs, on part of the lines |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.649). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.3, 50.2); signed map (65.6, 3.3). **Vector** length 70.7, 13.9% of its response variance represented; |z| ≥ 3 in 869 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.7 | +9.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.6 | +6.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | +5.0 | +3.6 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +4.1 | +4.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +4.1 | +6.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +8.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.5 | +3.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.2 | +4.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.1 | +5.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.5 | +0.9 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -2.1 | -6.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | -4.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.8 | -3.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.7 | -3.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -1.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.5 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | LDL receptor related protein 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p11.2 — chr11:46,856,717-46,918,642 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MEGF7, CLSS, LRP-4, SOST2 |
| Gene groups (HGNC) | Low density lipoprotein receptors |
| Reactome | 2 pathways, smallest: ECM proteoglycans; Extracellular matrix organization |
| Matched by | ensembl_id |

**Function**, from UniProt [O75096](https://www.uniprot.org/uniprotkb/O75096) (Low-density lipoprotein receptor-related protein 4):

> Mediates SOST-dependent inhibition of bone formation. Functions as a specific facilitator of SOST-mediated inhibition of Wnt signaling. Plays a key role in the formation and the maintenance of the neuromuscular junction (NMJ), the synapse between motor neuron and skeletal muscle. Directly binds AGRIN and recruits it to the MUSK signaling complex. Mediates the AGRIN-induced phosphorylation of MUSK, the kinase of the complex. The activation of MUSK in myotubes induces the formation of NMJ by …

**Summary**, from NCBI Gene [4038](https://www.ncbi.nlm.nih.gov/gene/4038):

> This gene encodes a member of the low-density lipoprotein receptor-related protein family. The encoded protein may be a regulator of Wnt signaling. Mutations in this gene are associated with Cenani-Lenz syndrome. [provided by RefSeq, May 2010]

**Accessions** — [HGNC:6696](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6696) · Entrez [4038](https://www.ncbi.nlm.nih.gov/gene/4038) · UniProt [O75096](https://www.uniprot.org/uniprotkb/O75096) · Ensembl [ENSG00000134569](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134569)

## Data

Gene col 5578: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5578); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5578, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5578]; `tensor/DDL_lfc|DDL_z.npy` [5578]; `embed/gene_vectors.npy` [5578]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5578 or target_col == 5578). Every well: [[LRP4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRP4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
