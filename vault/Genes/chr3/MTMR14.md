---
symbol: "MTMR14"
type: "gene"
col: 8764
ensembl_id: "ENSG00000163719"
name: "myotubularin related protein 14"
location: "3p25.3"
module: 76
arm: "+"
pooled_cpm: 58.48
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 24
n_dd_up_clean: 8
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/076"]
generated_by: "tahoemap"
---

# MTMR14

*myotubularin related protein 14* — 3p25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 1.89× (z +9.8, q 5e-20, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.360× (z -15.6, q 0e+00, down in 45 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.638× (z -6.9, q 7e-10, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[INPP5K]] (+0.75, fdr 7e-06), [[MARF1]] (+0.74, fdr 7e-06), [[ABTB1]] (+0.71, fdr 7e-06); moves opposite to [[PHACTR2]] (-0.66, fdr 1e-05), [[ZNF280D]] (-0.66, fdr 1e-05), [[FGF2]] (-0.64, fdr 3e-05).
> It is in [[Module 076]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8764.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.89×** | +9.8 | 5e-20 | 43/48 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.85×** | +9.5 | 6e-19 | 42/48 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.65×** | +7.8 | 8e-13 | 39/49 (SW480, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.51×** | +6.3 | 3e-08 | 32/48 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.06×** | +5.8 | 6e-07 | 37/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.27×** | +3.7 | 0.022 | 22/48 (NCI-H460, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | **1.54×** | +3.5 | 0.040 | 20/49 (CHP-212, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 1.16× | +3.3 | 0.076 | 14/48 (RPMI-7951, J82, …) | rises with dose |  |
| [[ULK-101 (drug)]] 0.05 µM |  | **1.24×** | +3.2 | 0.094 | 14/48 (LOX-IMVI, SNU-423, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 1.22× | +3.1 | 0.11 | 22/48 (NCI-H460, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 1.22× | +3.1 | 0.11 | 17/47 (A549, J82, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8764.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.360×** | -15.6 | 0e+00 | 45/49 (SK-MEL-2, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.362×** | -14.9 | 0e+00 | 39/42 (NCI-H460, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.422×** | -12.2 | 7e-32 | 37/45 (NCI-H2347, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.593×** | -7.8 | 7e-13 | 40/48 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.614×** | -7.2 | 1e-10 | 40/47 (HepG2/C3A, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.638×** | -6.9 | 7e-10 | 36/48 (LOX-IMVI, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.691×** | -5.4 | 5e-06 | 35/48 (A549, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.723×** | -4.7 | 2e-04 | 29/48 (NCI-H1573, SNU-423, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **0.563×** | -4.6 | 3e-04 | 27/48 (AsPC-1, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.574×** | -4.4 | 5e-04 | 27/48 (NCI-H2347, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.741×** | -4.4 | 6e-04 | 24/47 (A549, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.752×** | -4.3 | 7e-04 | 30/48 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.760×** | -4.2 | 0.001 | 28/49 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.767×** | -4.0 | 0.002 | 24/48 (HS-578T, A549, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.770×** | -4.0 | 0.003 | 25/47 (AsPC-1, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.797×** | -3.9 | 0.003 | 27/48 (AsPC-1, A549, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.780×** | -3.8 | 0.005 | 21/47 (AsPC-1, A549, …) | all doses, stronger at high dose |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.852× | -3.4 | 0.018 | 16/48 (A549, HOP62, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.654×** | -3.4 | 0.019 | 22/48 (NCI-H2347, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.663×** | -3.3 | 0.028 | 22/48 (NCI-H2347, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8764. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 78.6 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.148× (z -17.1) ⚠ toxic; transcription drop · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.286× (z -11.2) |
| [[AsPC-1 (line)]] | alt | 81.4 | 1 | 4 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.91× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.273× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.305× (z -10.5) |
| [[HEC-1-A (line)]] | alt | 62.6 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.30× (z +12.3) | [[Dinaciclib (drug)]] 0.05 µM 0.333× (z -10.5) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 34.2 | 4 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.44× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.0629× (z -23.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 48.0 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.92× (z +13.4) | [[Dinaciclib (drug)]] 0.5 µM 0.367× (z -12.5) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 85.7 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.198× (z -15.5) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 116 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -18.3) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 94.3 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.122× (z -17.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.358× (z -9.0) |
| [[SW1417 (line)]] | alt | 84.1 | 1 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.22× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.284× (z -13.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 63.0 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.364× (z -9.6) ⚠ toxic; transcription drop · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.352× (z -9.5) |
| [[HOP62 (line)]] | alt | 72.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.188× (z -16.1) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 58.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.297× (z -11.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 49.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.184× (z -12.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 46.7 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.185× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.284× (z -9.9) |
| [[Panc 03.27 (line)]] | alt | 70.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0727× (z -22.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 50.4 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.98× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.313× (z -10.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 115 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0393× (z -27.4) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 54.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.130× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Glycyrrhizic acid (drug)]] 0.05 µM 0.121× (z -8.8) |
| [[Hs 766T (line)]] | wt | 68.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.232× (z -10.9) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 69.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.257× (z -11.4) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 56.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.163× (z -12.4) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 63.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.231× (z -12.9) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 39.6 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.35× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.0896× (z -17.7) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 103 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.311× (z -10.7) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 45.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.180× (z -10.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 63.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.214× (z -13.3) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 34.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.126× (z -13.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 42.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.283× (z -10.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 32.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.250× (z -9.1) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 59.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0682× (z -16.4) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 38.6 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.107× (z -14.2) ⚠ toxic |
| [[HT-29 (line)]] | alt | 35.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.334× (z -9.4) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 39.1 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.70× (z +10.4) | — |
| [[LoVo (line)]] | wt | 33.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.51× (z +10.9) | — |
| [[NCI-H2030 (line)]] | alt | 61.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.289× (z -11.0) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 45.2 | 0 | 1 | — | [[Roxadustat (drug)]] 0.05 µM 0.0683× (z -8.6) |
| [[SW 900 (line)]] | alt | 40.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.254× (z -10.3) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 44.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.168× (z -9.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 42.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 41.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 64.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 60.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 61.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 47.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 87.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8764), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INPP5K]] | +0.75 | +0.68 / +0.69 | both halves | 7e-06 | same gene group; pathway: PI Metabolism |
| [[MARF1]] | +0.74 | +0.73 / +0.65 | both halves | 7e-06 |  |
| [[ABTB1]] | +0.71 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[GNAI3]] | +0.69 | +0.75 / +0.59 | both halves | 7e-06 |  |
| [[TRPT1]] | +0.69 | +0.71 / +0.50 | both halves | 1e-05 |  |
| [[ADIPOR1]] | +0.68 | +0.71 / +0.57 | both halves | 9e-06 |  |
| [[SPSB3]] | +0.66 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[WASF2]] | +0.66 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[MYO9B]] | +0.66 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[MOSPD3]] | +0.65 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[LINC01881]] | +0.64 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[FBXO33]] | +0.64 | +0.54 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHACTR2]] | -0.66 | -0.70 / -0.50 | both halves | 1e-05 |  |
| [[ZNF280D]] | -0.66 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[FGF2]] | -0.64 | -0.64 / -0.43 | both halves | 3e-05 |  |
| [[YTHDC2]] | -0.62 | -0.68 / -0.59 | both halves | 7e-06 |  |
| [[TIA1]] | -0.61 | -0.64 / -0.40 | both halves | 5e-05 |  |
| [[GCFC2]] | -0.61 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[MGST1]] | -0.61 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[ABCC2]] | -0.60 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[ZNF260]] | -0.59 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[UBQLN2]] | -0.59 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[POGLUT1]] | -0.59 | -0.62 / -0.42 | both halves | 4e-05 |  |
| [[FUBP1]] | -0.58 | -0.39 / -0.42 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises MTMR14's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 3.9% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds |
| [[HDAC6]] | B | HDAC6 activity lowers MTMR14's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 076]]; 59 genes; every member is in the + arm (projection on the module's main direction 0.675). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (5.4, -44.5); signed map (-20.4, 11.8). **Vector** length 116, 36.8% of its response variance represented; |z| ≥ 3 in 1,177 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +9.2 | +9.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +9.0 | +9.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +6.9 | +6.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | +0.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.4 | +0.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +2.4 | +2.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.1 | -0.6 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | +2.1 | +3.2 |
|  | [[Retinoic acid (drug)]] 5 µM |  | +1.9 | +2.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.7 | -4.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.5 | -7.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.9 | -6.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -5.8 | -4.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.7 | +0.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -5.1 | -4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.7 | -4.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.7 | -4.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.6 | -4.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.5 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | myotubularin related protein 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.3 — chr3:9,649,433-9,702,393 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22405, FLJ90311, hJumpy, hEDTP; previously C3orf29 |
| Gene groups (HGNC) | Myotubularins; Phosphoinositide phosphatases |
| Reactome | 6 pathways, smallest: Synthesis of PIPs at the plasma membrane; PI Metabolism; Macroautophagy |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NCE2](https://www.uniprot.org/uniprotkb/Q8NCE2) (Phosphatidylinositol-3,5-bisphosphate 3-phosphatase MTMR14):

> Lipid phosphatase that specifically dephosphorylates the D-3 position of phosphatidylinositol 3-phosphate and phosphatidylinositol 3,5-bisphosphate, generating phosphatidylinositol and phosphatidylinositol 5-phosphate.

**Summary**, from NCBI Gene [64419](https://www.ncbi.nlm.nih.gov/gene/64419):

> This gene encodes a myotubularin-related protein. The encoded protein is a phosphoinositide phosphatase that specifically dephosphorylates phosphatidylinositol 3,5-biphosphate and phosphatidylinositol 3-phosphate. Mutations in this gene are correlated with autosomal dominant centronuclear myopathy. Alternate splicing results in multiple transcript variants. A pseudogene of this gene is found on chromosome 18.[provided by RefSeq, Apr 2010]

**Accessions** — [HGNC:26190](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26190) · Entrez [64419](https://www.ncbi.nlm.nih.gov/gene/64419) · UniProt [Q8NCE2](https://www.uniprot.org/uniprotkb/Q8NCE2) · Ensembl [ENSG00000163719](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163719)

## Data

Gene col 8764: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8764); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8764, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8764]; `tensor/DDL_lfc|DDL_z.npy` [8764]; `embed/gene_vectors.npy` [8764]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8764 or target_col == 8764). Every well: [[MTMR14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTMR14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
