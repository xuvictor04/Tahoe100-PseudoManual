---
symbol: "LIPG"
type: "gene"
col: 2164
ensembl_id: "ENSG00000101670"
name: "lipase G, endothelial type"
location: "18q21.1"
module: 86
arm: "+"
pooled_cpm: 18.12
n_lines_expressing: 25
n_dd_up: 34
n_dd_down: 12
n_dd_up_clean: 17
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 6
direction_downstream: 16
tags: ["gene", "module/086"]
generated_by: "tahoemap"
---

# LIPG

*lipase G, endothelial type* — 18q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (17 with an alert ⚠); the strongest is [[Berbamine (drug)]] 5 µM: 1.80× (z +9.2, q 2e-17, up in 20 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.597× (z -5.3, q 7e-05, down in 15 of 23 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LDLR]] (+0.71, fdr 7e-06), [[FGFBP1]] (+0.67, fdr 1e-05), [[HMGCS1]] (+0.64, fdr 9e-06); moves opposite to [[PHC3]] (-0.51, fdr 4e-05), [[COPS5]] (-0.49, fdr 4e-05), [[CEPT1]] (-0.47, fdr 2e-04).
> It is in [[Module 086]], a single-armed module (cholesterol synthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[ZNF365]] → it (grade B ⚠); 16 go from it, the strongest it → [[ZNF365]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 17 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2164.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Berbamine (drug)]] 5 µM |  | **1.80×** | +9.2 | 2e-17 | 20/23 (LoVo, HEC-1-A, …) | rises with dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | **1.78×** | +9.0 | 1e-16 | 22/23 (LoVo, HEC-1-A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **2.15×** | +8.1 | 1e-13 | 3/14 (NCI-H1792, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **1.95×** | +7.3 | 3e-11 | 4/20 (Panc 03.27, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.91×** | +7.1 | 1e-10 | 8/22 (SNU-423, NCI-H460, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.90×** | +7.1 | 1e-10 | 12/22 (NCI-H460, SNU-423, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.94×** | +7.0 | 2e-10 | 12/21 (NCI-H1792, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.53×** | +6.6 | 2e-09 | 9/23 (BT-474, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.82×** | +6.6 | 2e-09 | 12/22 (NCI-H460, SNU-423, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.73×** | +6.0 | 1e-07 | 11/22 (NCI-H1573, Panc 03.27, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.72×** | +6.0 | 1e-07 | 12/22 (NCI-H460, SNU-423, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.42×** | +5.5 | 2e-06 | 6/23 (HEC-1-A, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **1.66×** | +5.2 | 9e-06 | 3/19 (Panc 03.27, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Entrectinib (drug)]] 5 µM |  | **1.55×** | +4.8 | 5e-05 | 12/22 (COLO 205, SNU-423, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.30×** | +4.8 | 6e-05 | 11/21 (BT-474, HCT15, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.57×** | +4.7 | 1e-04 | 10/22 (NCI-H460, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Posaconazole (drug)]] 5 µM |  | **1.55×** | +4.6 | 1e-04 | 14/22 (HEC-1-A, COLO 205, …) | rises with dose | plate-row cell shift |
| [[Adagrasib (drug)]] 5 µM |  | **1.53×** | +4.5 | 2e-04 | 9/22 (NCI-H460, HT-29, …) | top dose only |  |
| [[(S)-Crizotinib (drug)]] 5 µM |  | **1.49×** | +4.2 | 7e-04 | 11/22 (SNU-423, HEC-1-A, …) | top dose only |  |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | **1.47×** | +4.1 | 0.001 | 11/22 (NCI-H460, LS 180, …) | top dose only | plate-row cell shift |
| [[Belzutifan (drug)]] 5 µM |  | **1.92×** | +3.8 | 0.004 | 8/21 (NCI-H460, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | **1.38×** | +3.4 | 0.013 | 12/22 (HEC-1-A, COLO 205, …) | top dose only | plate-row cell shift |
| [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +3.3 | 0.022 | 9/23 (LS 180, Panc 03.27, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.34×** | +3.2 | 0.025 | 6/22 (SW48, COLO 205, …) | two highest doses | low cells (technical?) |
| [[Ritonavir (drug)]] 5 µM |  | **1.22×** | +3.1 | 0.032 | 10/22 (HEC-1-A, KATO III, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2164.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | **0.597×** | -5.3 | 7e-05 | 15/23 (LoVo, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | **0.741×** | -4.7 | 8e-04 | 13/22 (Panc 03.27, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.764×** | -4.2 | 0.005 | 11/23 (BT-474, LS 180, …) | top dose only | low cells (technical?) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.734×** | -4.1 | 0.006 | 12/23 (BT-474, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.768×** | -4.0 | 0.006 | 8/22 (BT-474, LoVo, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.701×** | -3.9 | 0.008 | 10/22 (LS 180, NCI-H1792, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.719×** | -3.8 | 0.011 | 10/23 (BT-474, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.722×** | -3.6 | 0.024 | 11/22 (LoVo, LS 180, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.546×** | -3.5 | 0.031 | 11/22 (Panc 03.27, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.786×** | -3.3 | 0.053 | 13/23 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.752×** | -3.1 | 0.081 | 12/22 (KATO III, SW48, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.735×** | -3.1 | 0.081 | 7/22 (SW48, BT-474, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.59 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2164. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 13.3 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Neratinib (drug)]] 5 µM 0.0691× (z -9.6) |
| [[KATO III (line)]] | alt | 54.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.157× (z -10.0) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.202× (z -8.7) |
| [[LoVo (line)]] | wt | 33.8 | 2 | 1 | [[Cepharanthine (drug)]] 5 µM 3.06× (z +9.8) | [[5-Azacytidine (drug)]] 5 µM 0.239× (z -8.8) |
| [[NCI-H1792 (line)]] | alt | 83.6 | 0 | 3 | — | [[Budesonide (drug)]] 5 µM 0.224× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 8.94 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 4.48× (z +9.3) | — |
| [[NCI-H460 (line)]] | wt | 5.28 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 8.15× (z +8.5) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[Panc 03.27 (line)]] | alt | 61.8 | 0 | 1 | — | [[Clobetasol propionate (drug)]] 0.05 µM 0.299× (z -8.8) |
| [[PANC-1 (line)]] | alt | 27.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.285× (z -11.1) ⚠ cell-cycle shift, explains ~40% of this change |
| [[SW48 (line)]] | wt | 28.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -13.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 3.19 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.941 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.949 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 112 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.03 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.47 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.82 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.21 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.23 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 68.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.74 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.41 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 66.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.26 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.57 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.07 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 8.00 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.25 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2164), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LDLR]] | +0.71 | +0.71 / +0.67 | both halves | 7e-06 | pathway: Plasma lipoprotein assembly, remodeling, and clearance |
| [[FGFBP1]] | +0.67 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[HMGCS1]] | +0.64 | +0.57 / +0.61 | both halves | 9e-06 |  |
| [[LPIN1]] | +0.63 | +0.60 / +0.54 | both halves | 1e-05 | STRING 749 |
| [[DHCR7]] | +0.62 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[INSIG1]] | +0.58 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[LRP8]] | +0.58 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[PCSK9]] | +0.58 | +0.58 / +0.53 | both halves | 1e-05 | pathway: Plasma lipoprotein assembly, remodeling, and clearance; STRING 589 |
| [[EBP]] | +0.57 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[HMGCR]] | +0.57 | +0.52 / +0.50 | both halves | 1e-05 | STRING 453 |
| [[ADIPOR2]] | +0.56 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[NPC1]] | +0.56 | +0.55 / +0.49 | both halves | 1e-05 | pathway: Plasma lipoprotein assembly, remodeling, and clearance |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHC3]] | -0.51 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[COPS5]] | -0.49 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[CEPT1]] | -0.47 | -0.55 / -0.31 | both halves | 2e-04 |  |
| [[BRAP]] | -0.47 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[KCTD18]] | -0.46 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[CCDC25]] | -0.46 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[TRIM23]] | -0.45 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[PPIL4]] | -0.45 | -0.43 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 3, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF365]] | B | ZNF365 activity raises LIPG's level | lines that do not express ZNF365 (24) vs lines expressing it (26) | 1.31× lower at baseline in the lines without ZNF365 | 0.028 | ⚠ within organs, on part of the lines; also absent: ENSG00000285837, CHSY3, FLT1 |
| [[ST3GAL1]] | B | ST3GAL1 activity raises LIPG's level | lines that do not express ST3GAL1 (11) vs lines expressing it (39) | 2.43× lower at baseline in the lines without ST3GAL1 | 0.039 | ⚠ within organs, on part of the lines; also absent: IL1RAP, FBXO32, PLSCR2 |
| [[MAP2K2]] | B | MAP2K2 activity raises LIPG's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[CLDN4]] | C | CLDN4 activity raises LIPG's level | lines that do not express CLDN4 (26) vs lines expressing it (24) | 4.38× lower at baseline in the lines without CLDN4 | 0.023 | ⚠ within organs, on part of the lines; also absent: CDH1, SCNN1A, ITGB6; co-absent with the target |
| [[TMEM154]] | C | TMEM154 activity raises LIPG's level | lines that do not express TMEM154 (26) vs lines expressing it (24) | 1.89× lower at baseline in the lines without TMEM154 | 0.040 | ⚠ within organs, on part of the lines; also absent: ENSG00000287003, SYNPR-AS1, MMP13; co-absent with the target |
| [[TINAGL1]] | C | TINAGL1 activity raises LIPG's level | lines that do not express TINAGL1 (26) vs lines expressing it (24) | 3.52× lower at baseline in the lines without TINAGL1 | 0.050 | ⚠ within organs, on part of the lines; also absent: IL20RA, MSLN, KRT19; co-absent with the target |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 8, C 8. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF365]] | B | LIPG activity raises ZNF365's level | lines that do not express LIPG (25) vs lines expressing it (25) | 1.72× lower at baseline in the lines without LIPG | 0.010 | ⚠ within organs, on part of the lines; also absent: GALNT3, GRHL2, LIPH |
| [[VPS37B]] | B | LIPG activity raises VPS37B's level | lines that do not express LIPG (25) vs lines expressing it (25) | 1.44× lower at baseline in the lines without LIPG | 0.011 | ⚠ within organs, on part of the lines; also absent: GALNT3, GRHL2, LIPH |
| [[ST3GAL1]] | B | LIPG activity raises ST3GAL1's level | lines that do not express LIPG (25) vs lines expressing it (25) | 1.86× lower at baseline in the lines without LIPG | 0.054 | ⚠ within organs, on part of the lines; also absent: GALNT3, GRHL2, LIPH |
| [[CD58]] | B | LIPG activity raises CD58's level | lines that do not express LIPG (25) vs lines expressing it (25) | 1.42× lower at baseline in the lines without LIPG | 0.062 | ⚠ within organs, on part of the lines; also absent: GALNT3, GRHL2, LIPH |
| [[SHB]] | B | LIPG activity raises SHB's level | lines that do not express LIPG (25) vs lines expressing it (25) | 1.73× lower at baseline in the lines without LIPG | 0.067 | ⚠ within organs, on part of the lines; also absent: GALNT3, GRHL2, LIPH |
| [[CDCP1]] | B | LIPG activity raises CDCP1's level | lines that do not express LIPG (25) vs lines expressing it (25) | 2.47× lower at baseline in the lines without LIPG | 0.074 | ⚠ within organs, on part of the lines; also absent: GALNT3, GRHL2, LIPH |
| [[LAMA3]] | B | LIPG activity raises LAMA3's level | lines that do not express LIPG (25) vs lines expressing it (25) | 3.26× lower at baseline in the lines without LIPG | 0.088 | ⚠ within organs, on part of the lines; also absent: GALNT3, GRHL2, LIPH |
| [[KRT15]] | B | LIPG activity raises KRT15's level | lines that do not express LIPG (25) vs lines expressing it (25) | 2.15× lower at baseline in the lines without LIPG | 0.095 | ⚠ within organs, on part of the lines; also absent: GALNT3, GRHL2, LIPH |
| [[CLDN4]] | C | LIPG activity raises CLDN4's level | lines that do not express LIPG (25) vs lines expressing it (25) | 5.03× lower at baseline in the lines without LIPG | 0.004 | ⚠ within organs, on part of the lines; also absent: GALNT3, GRHL2, LIPH; co-absent with the target |
| [[PRSS22]] | C | LIPG activity raises PRSS22's level | lines that do not express LIPG (25) vs lines expressing it (25) | 4.96× lower at baseline in the lines without LIPG | 0.006 | ⚠ within organs, on part of the lines; also absent: GALNT3, GRHL2, LIPH; co-absent with the target |
| [[EPHA1]] | C | LIPG activity raises EPHA1's level | lines that do not express LIPG (25) vs lines expressing it (25) | 2.54× lower at baseline in the lines without LIPG | 0.009 | ⚠ within organs, on part of the lines; also absent: GALNT3, GRHL2, LIPH; co-absent with the target |
| [[S100A14]] | C | LIPG activity raises S100A14's level | lines that do not express LIPG (25) vs lines expressing it (25) | 4.23× lower at baseline in the lines without LIPG | 0.029 | ⚠ within organs, on part of the lines; also absent: GALNT3, GRHL2, LIPH; co-absent with the target |

## Where it sits

- **Module**: [[Module 086]] — cholesterol synthesis; 51 genes; every member is in the + arm (projection on the module's main direction 0.610). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (20.8, -48.7); signed map (-51.7, 33.3). **Vector** length 84.6, 25.0% of its response variance represented; |z| ≥ 3 in 748 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | +6.0 | +8.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | +5.3 | +7.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | +4.4 | +5.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +6.6 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +4.1 | +9.0 |
|  | [[Berbamine (drug)]] 5 µM |  | +3.4 | +9.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | +3.0 | +4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +2.5 |
| fall | [[Trametinib (drug)]] 5 µM |  | -2.9 | -5.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.7 | -3.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.6 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.5 | -3.1 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -2.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.3 | -4.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.2 | -0.9 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.1 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | lipase G, endothelial type |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q21.1 — chr18:49,560,699-49,599,185 (+) |
| Ensembl biotype | protein_coding |
| Also known as | EDL |
| Gene groups (HGNC) | Lipases |
| Reactome | 4 pathways, smallest: HDL remodeling; Plasma lipoprotein remodeling; Plasma lipoprotein assembly, remodeling, and clearance |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5X9](https://www.uniprot.org/uniprotkb/Q9Y5X9) (Endothelial lipase):

> Exerts both phospholipase and triglyceride lipase activities. More active as a phospholipase than a triglyceride lipase. Hydrolyzes triglycerides, both with short-chain fatty acyl groups (tributyrin) and long-chain fatty acyl groups (triolein) with similar levels of activity toward both types of substrates. Hydrolyzes high density lipoproteins (HDL) more efficiently than other lipoproteins.

**Summary**, from NCBI Gene [9388](https://www.ncbi.nlm.nih.gov/gene/9388):

> The protein encoded by this gene has substantial phospholipase activity and may be involved in lipoprotein metabolism and vascular biology. This protein is designated a member of the TG lipase family by its sequence and characteristic lid region which provides substrate specificity for enzymes of the TG lipase family. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6623](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6623) · Entrez [9388](https://www.ncbi.nlm.nih.gov/gene/9388) · UniProt [Q9Y5X9](https://www.uniprot.org/uniprotkb/Q9Y5X9) · Ensembl [ENSG00000101670](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101670)

## Data

Gene col 2164: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2164); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2164, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2164]; `tensor/DDL_lfc|DDL_z.npy` [2164]; `embed/gene_vectors.npy` [2164]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2164 or target_col == 2164). Every well: [[LIPG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LIPG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
