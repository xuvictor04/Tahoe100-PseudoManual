---
symbol: "NFE2L3"
type: "gene"
col: 563
ensembl_id: "ENSG00000050344"
name: "NFE2 like bZIP transcription factor 3"
location: "7p15.2"
module: 78
arm: "+"
pooled_cpm: 34.85
n_lines_expressing: 49
n_dd_up: 13
n_dd_down: 30
n_dd_up_clean: 1
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/078"]
generated_by: "tahoemap"
---

# NFE2L3

*NFE2 like bZIP transcription factor 3* — 7p15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.02× (z +10.0, q 1e-20, up in 32 of 42 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.29× (z +5.1, q 2e-05, up in 23 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (Panc 03.27 3.25×, HOP62 3.93×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HOP62 4.69×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H1792 6.06×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (4 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.540× (z -8.8, q 8e-16, down in 35 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMAD3]] (+0.64, fdr 7e-06), [[ITGA6]] (+0.62, fdr 1e-05), [[SHB]] (+0.62, fdr 7e-06); moves opposite to [[MED10]] (-0.52, fdr 2e-05), [[NUDT16-DT]] (-0.51, fdr 3e-05), [[NOXRED1]] (-0.51, fdr 3e-05).
> It is in [[Module 078]], a single-armed module (apical junction).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[EPB41L2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 12 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 563.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (Panc 03.27 3.25×, HOP62 3.93×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HOP62 4.69×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H1792 6.06×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **2.02×** | +10.0 | 1e-20 | 32/42 (Panc 03.27, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **1.88×** | +8.6 | 2e-15 | 27/33 (NCI-H1792, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **1.67×** | +6.7 | 3e-09 | 23/37 (HOP62, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.48×** | +5.5 | 5e-06 | 30/47 (NCI-H1792, A498, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.45×** | +5.3 | 1e-05 | 23/47 (J82, NCI-H1792, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.44×** | +5.2 | 2e-05 | 24/47 (A498, NCI-H1792, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +5.1 | 2e-05 | 23/47 (NCI-H460, RPMI-7951, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.39×** | +4.6 | 3e-04 | 21/47 (A498, NCI-H1792, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~64% of this change | **1.35×** | +4.3 | 0.001 | 20/44 (HOP62, SNU-423, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.32×** | +3.9 | 0.004 | 20/47 (J82, NCI-H460, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.22×** | +3.9 | 0.004 | 18/46 (NCI-H460, NCI-H1573, …) | top dose only | composition shift |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.69×** | +3.9 | 0.004 | 19/47 (LS 180, Panc 03.27, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.54×** | +3.2 | 0.060 | 12/31 (Panc 03.27, HS-578T, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 563.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.540×** | -8.8 | 8e-16 | 35/47 (H4, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.600×** | -7.3 | 9e-11 | 30/47 (LoVo, MIA PaCa-2, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.670×** | -5.5 | 5e-06 | 26/46 (NCI-H2030, SW480, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.665×** | -5.5 | 5e-06 | 27/47 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.763×** | -5.5 | 5e-06 | 31/47 (Hs 766T, SW 1088, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **0.767×** | -5.4 | 7e-06 | 25/47 (MIA PaCa-2, SW480, …) | rises with dose | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.715×** | -4.8 | 1e-04 | 18/47 (PANC-1, HOP62, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | **0.723×** | -4.6 | 2e-04 | 22/47 (Panc 03.27, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.729×** | -4.5 | 4e-04 | 22/47 (LoVo, KATO III, …) | top dose only |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.734×** | -4.4 | 6e-04 | 23/47 (Panc 03.27, SW 1088, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.729×** | -4.3 | 0.001 | 20/47 (MIA PaCa-2, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.751×** | -4.1 | 0.002 | 21/47 (Panc 03.27, H4, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.822×** | -4.0 | 0.003 | 19/47 (LoVo, KATO III, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.762×** | -3.9 | 0.004 | 21/47 (hTERT-HPNE, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.766×** | -3.8 | 0.005 | 20/47 (SW480, MIA PaCa-2, …) | two highest doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.773×** | -3.7 | 0.008 | 15/47 (H4, LoVo, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.775×** | -3.6 | 0.009 | 20/46 (SW480, SK-MEL-2, …) | rises with dose | low cells (technical?) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.781×** | -3.5 | 0.013 | 16/46 (Hs 766T, SW 900, …) | two highest doses |  |
| [[Budesonide (drug)]] 0.5 µM |  | **0.781×** | -3.5 | 0.013 | 16/47 (Panc 03.27, H4, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 563. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 92.8 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -11.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.378× (z -9.3) |
| [[HOP62 (line)]] | alt | 20.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.69× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | — |
| [[SW480 (line)]] | alt | 57.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.339× (z -11.0) |
| [[LoVo (line)]] | wt | 45.9 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.340× (z -9.3) |
| [[MIA PaCa-2 (line)]] | alt | 63.7 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.159× (z -11.2) |
| [[RKO (line)]] | wt | 14.7 | 0 | 2 | — | [[Harringtonine (drug)]] 0.05 µM 0.0818× (z -12.0) |
| [[A-427 (line)]] | wt | 25.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.178× (z -12.6) |
| [[AN3 CA (line)]] | alt | 24.0 | 0 | 1 | — | [[Posaconazole (drug)]] 0.05 µM 0.0549× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 8.73 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.31× (z +8.6) ⚠ cell-cycle shift, explains ~97% of this change | — |
| [[H4 (line)]] | wt | 58.4 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.110× (z -12.4) |
| [[Hs 766T (line)]] | wt | 19.3 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.165× (z -11.1) |
| [[LS 180 (line)]] | wt | 75.6 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.261× (z -10.6) |
| [[NCI-H1792 (line)]] | alt | 16.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.06× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | — |
| [[NCI-H23 (line)]] | alt | 29.4 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.166× (z -11.8) ⚠ cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 62.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.25× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | — |
| [[SHP-77 (line)]] | alt | 9.05 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.102× (z -9.0) |
| [[A-172 (line)]] | wt | 57.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.59 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 37.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.96 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.57 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 35.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 563), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMAD3]] | +0.64 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[ITGA6]] | +0.62 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[SHB]] | +0.62 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[NCEH1]] | +0.61 | +0.57 / +0.58 | both halves | 9e-06 |  |
| [[PODXL]] | +0.58 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[ECE1]] | +0.58 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[UXS1]] | +0.57 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[SOX9]] | +0.56 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[JAG1]] | +0.56 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[NAB1]] | +0.55 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[PKM]] | +0.55 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[EHD1]] | +0.54 | +0.55 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED10]] | -0.52 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[NUDT16-DT]] | -0.51 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[NOXRED1]] | -0.51 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[TMEM101]] | -0.50 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[ELMOD3]] | -0.50 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[RWDD3]] | -0.49 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[EPB41L4A-AS1]] | -0.49 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[CRYAB]] | -0.49 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[CMKLR2]] | -0.49 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[NGDN]] | -0.49 | -0.49 / -0.38 | both halves | 7e-05 |  |
| [[PEX11A]] | -0.49 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[COMMD1]] | -0.48 | -0.38 / -0.45 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPB41L2]] | B | EPB41L2 activity raises NFE2L3's level | lines that do not express EPB41L2 (6) vs lines expressing it (44) | 1.81× lower at baseline in the lines without EPB41L2 | 0.053 | ⚠ within organs, on part of the lines; also absent: SLC26A2, CRTAP, FAM216A; maybe low, not absent |
| [[IQGAP2]] | B | IQGAP2 activity strengthens NFE2L3's drug response | lines that do not express IQGAP2 (24) vs lines expressing it (23) | the lines without IQGAP2 respond 0.80× as strongly (z diff +0.67); strongest at Selinexor 5 µM: 0.81x vs 0.64x (z diff +2.3) | 0.067 | ⚠ within organs, on part of the lines; also absent: KLHL13, KCNQ2, CHD5; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[NR3C1]] | B | NR3C1 activity lowers NFE2L3's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 5.9% of all compounds | 0.079 | ⚠ off-target possible; 3 compounds |
| [[IQGAP2]] | B | IQGAP2 activity raises NFE2L3's level | lines that do not express IQGAP2 (25) vs lines expressing it (25) | 1.50× lower at baseline in the lines without IQGAP2 | 0.082 | ⚠ within organs, on part of the lines; also absent: KLHL13, KCNQ2, CHD5; maybe low, not absent |
| [[CCND1]] | B | CCND1 activity raises NFE2L3's level | lines that do not express CCND1 (7) vs lines expressing it (43) | 1.57× lower at baseline in the lines without CCND1 | 0.091 | ⚠ within organs, on part of the lines; also absent: FSTL3, ADAMTSL5; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 078]] — apical junction; 58 genes; every member is in the + arm (projection on the module's main direction 0.578). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (41.1, 14.9); signed map (3.3, 43.1). **Vector** length 116, 30.1% of its response variance represented; |z| ≥ 3 in 1,224 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | +5.3 | +8.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +5.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | +4.8 | +10.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | +4.8 | +5.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | +4.8 | +6.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.0 | +2.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.9 | +2.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.1 | +2.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +2.0 | +1.5 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | -5.9 | -5.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -5.9 | -8.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.7 | -7.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.6 | -4.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | -4.2 | -5.4 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -4.2 | -5.5 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -3.9 | -3.0 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -3.8 | -3.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.5 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | NFE2 like bZIP transcription factor 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p15.2 — chr7:26,152,198-26,187,137 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Nrf3 |
| Gene groups (HGNC) | NFE2 family bZIP transcription factors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y4A8](https://www.uniprot.org/uniprotkb/Q9Y4A8) (Nuclear factor erythroid 2-related factor 3):

> Activates erythroid-specific, globin gene expression.

**Summary**, from NCBI Gene [9603](https://www.ncbi.nlm.nih.gov/gene/9603):

> This gene encodes a member of the cap 'n' collar basic-region leucine zipper family of transcription factors. The encoded protein heterodimerizes with small musculoaponeurotic fibrosarcoma factors to bind antioxidant response elements in target genes. This protein is a membrane bound glycoprotein that is targeted to the endoplasmic reticulum and the nuclear envelope. Pseudogenes of this gene are found on chromosomes 16, 17, and 18. [provided by RefSeq, Mar 2009]

**Accessions** — [HGNC:7783](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7783) · Entrez [9603](https://www.ncbi.nlm.nih.gov/gene/9603) · UniProt [Q9Y4A8](https://www.uniprot.org/uniprotkb/Q9Y4A8) · Ensembl [ENSG00000050344](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000050344)

## Data

Gene col 563: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 563); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 563, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 563]; `tensor/DDL_lfc|DDL_z.npy` [563]; `embed/gene_vectors.npy` [563]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 563 or target_col == 563). Every well: [[NFE2L3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NFE2L3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
