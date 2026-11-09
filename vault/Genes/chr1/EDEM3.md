---
symbol: "EDEM3"
type: "gene"
col: 3794
ensembl_id: "ENSG00000116406"
name: "ER degradation enhancing alpha-mannosidase like protein 3"
location: "1q25.3"
module: 42
arm: "+"
pooled_cpm: 70.37
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 20
n_dd_up_clean: 8
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# EDEM3

*ER degradation enhancing alpha-mannosidase like protein 3* — 1q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 1.52× (z +8.9, q 3e-16, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.594× (z -11.0, q 1e-25, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SRPRA]] (+0.53, fdr 2e-05), [[SSR1]] (+0.51, fdr 3e-05), [[DAP]] (+0.51, fdr 6e-05); moves opposite to [[FAXDC2]] (-0.52, fdr 9e-05), [[KANSL1]] (-0.51, fdr 2e-05), [[ATP6V1H]] (-0.51, fdr 9e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3794.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.52×** | +8.9 | 3e-16 | 37/48 (A-172, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.52×** | +8.8 | 3e-16 | 37/48 (A-172, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.51×** | +8.5 | 4e-15 | 35/48 (A-172, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.32×** | +8.3 | 2e-14 | 28/48 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.46×** | +8.1 | 7e-14 | 37/48 (A-172, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.33×** | +6.0 | 2e-07 | 30/48 (SW 900, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.50×** | +4.5 | 5e-04 | 25/49 (J82, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.21×** | +4.1 | 0.003 | 18/49 (A-172, NCI-H2347, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.13× | +3.6 | 0.022 | 16/48 (PANC-1, A498, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.3 | 0.046 | 20/47 (NCI-H1573, SW480, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 1.17× | +3.3 | 0.057 | 10/49 (A498, H4, …) | inconsistent across doses |  |
| [[Lumateperone (tosylate) (drug)]] 5 µM |  | 1.11× | +3.0 | 0.11 | 1/49 (J82) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3794.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.594×** | -11.0 | 1e-25 | 40/48 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.525×** | -7.2 | 2e-10 | 31/49 (PANC-1, NCI-H1573, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.796×** | -6.8 | 1e-09 | 29/48 (HOP62, SW 900, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change | **0.763×** | -5.7 | 1e-06 | 26/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.772×** | -5.5 | 4e-06 | 26/48 (PANC-1, NCI-H460, …) | rises with dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.768×** | -5.3 | 1e-05 | 24/48 (NCI-H460, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.783×** | -5.2 | 2e-05 | 26/48 (HT-29, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.794×** | -4.9 | 7e-05 | 24/47 (NCI-H1573, COLO 205, …) | two highest doses | cell-cycle shift (explains ~10% here); composition shift |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.670×** | -4.4 | 6e-04 | 18/47 (C32, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.813×** | -4.4 | 6e-04 | 23/48 (SW 1271, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.684×** | -4.2 | 0.001 | 16/45 (NCI-H1573, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.759×** | -4.2 | 0.001 | 20/49 (A498, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.824×** | -4.1 | 0.002 | 23/48 (HOP62, A-172, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.769×** | -4.0 | 0.003 | 21/48 (A498, C-33 A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.703×** | -3.9 | 0.003 | 15/34 (SK-MEL-2, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.716×** | -3.7 | 0.007 | 19/48 (RPMI-7951, LOX-IMVI, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.717×** | -3.7 | 0.007 | 16/48 (NCI-H460, CHP-212, …) | top dose only | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.894× | -3.3 | 0.022 | 12/48 (RKO, CHP-212, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.858× | -3.2 | 0.028 | 11/48 (NCI-H2030, HepG2/C3A, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.747×** | -3.2 | 0.028 | 14/48 (NCI-H460, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Decitabine (drug)]] 0.05 µM |  | 0.850× | -3.2 | 0.032 | 18/47 (CHP-212, J82, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3794. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 165 | 0 | 12 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.274× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.380× (z -11.2) |
| [[PANC-1 (line)]] | alt | 75.4 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.249× (z -20.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~11% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.556× (z -9.1) |
| [[A498 (line)]] | wt | 144 | 1 | 4 (3 ⚠) | [[Panobinostat (drug)]] 0.5 µM 1.78× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.271× (z -18.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~11% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.559× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 92.5 | 1 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.13× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.378× (z -11.3) |
| [[A-172 (line)]] | wt | 84.0 | 4 | 0 | [[Belinostat (drug)]] 5 µM 2.89× (z +11.6) | — |
| [[KATO III (line)]] | alt | 79.7 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.313× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~8% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.395× (z -9.3) |
| [[CFPAC-1 (line)]] | alt | 44.9 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.94× (z +9.8) | — |
| [[COLO 205 (line)]] | alt | 109 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.209× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.394× (z -8.9) |
| [[J82 (line)]] | alt | 42.3 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.33× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.344× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~11% of this change |
| [[SW480 (line)]] | alt | 54.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +9.8) | — |
| [[CHP-212 (line)]] | wt | 193 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.202× (z -14.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 83.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.390× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~11% of this change |
| [[HT-29 (line)]] | alt | 96.8 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.391× (z -10.2) |
| [[LoVo (line)]] | wt | 55.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.298× (z -12.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 65.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.420× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change |
| [[MIA PaCa-2 (line)]] | alt | 54.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +10.9) | — |
| [[NCI-H23 (line)]] | alt | 43.7 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.382× (z -9.2) ⚠ cell-cycle shift, explains ~22% of this change |
| [[NCI-H661 (line)]] | alt | 71.3 | 0 | 1 | — | [[Fluvoxamine (maleate) (drug)]] 0.5 µM 0.133× (z -9.3) |
| [[RKO (line)]] | wt | 49.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.259× (z -10.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 51.8 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.158× (z -8.7) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 39.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.94× (z +8.6) | — |
| [[SW 1271 (line)]] | alt | 45.2 | 0 | 1 | — | [[Berbamine (dihydrochloride) (drug)]] 5 µM 0.0422× (z -10.2) |
| [[A-427 (line)]] | wt | 66.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 59.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 69.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 42.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 72.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 43.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 68.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 64.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 108 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 53.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 60.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 68.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 90.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 69.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 65.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 35.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3794), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*45 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRPRA]] | +0.53 | +0.49 / +0.47 | both halves | 2e-05 | STRING 521 |
| [[SSR1]] | +0.51 | +0.45 / +0.48 | both halves | 3e-05 | STRING 514 |
| [[DAP]] | +0.51 | +0.38 / +0.48 | both halves | 6e-05 |  |
| [[ARCN1]] | +0.50 | +0.60 / +0.49 | both halves | 1e-05 | pathway: Asparagine N-linked glycosylation |
| [[FBXW8]] | +0.50 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[EP400P1]] | +0.50 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[DNAJC10]] | +0.49 | +0.50 / +0.46 | both halves | 3e-05 | STRING 771 |
| [[USO1]] | +0.49 | +0.52 / +0.47 | both halves | 2e-05 | pathway: Asparagine N-linked glycosylation |
| [[ATP6V0A2]] | +0.47 | +0.46 / +0.50 | both halves | 2e-05 |  |
| [[FAM98A]] | +0.47 | +0.28 / +0.56 | both halves | 3e-04 |  |
| [[SLC30A7]] | +0.46 | +0.45 / +0.44 | both halves | 3e-05 |  |
| [[BCAP29]] | +0.46 | +0.40 / +0.41 | both halves | 5e-05 |  |

## Genes that move opposite

*55 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAXDC2]] | -0.52 | -0.36 / -0.47 | both halves | 9e-05 |  |
| [[KANSL1]] | -0.51 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[ATP6V1H]] | -0.51 | -0.37 / -0.51 | both halves | 9e-05 |  |
| [[HEXA]] | -0.49 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[PISD]] | -0.48 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[MED28-DT]] | -0.48 | -0.22 / -0.44 | both halves | 6e-04 |  |
| [[ATP6V0E1]] | -0.47 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[ANO7]] | -0.47 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[ROR2]] | -0.46 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[SLC25A26]] | -0.46 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[FBXO44]] | -0.46 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[CCL28]] | -0.45 | -0.37 / -0.42 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers EDEM3's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.251). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-33.1, 36.1); signed map (-57.1, 9.5). **Vector** length 108, 29.2% of its response variance represented; |z| ≥ 3 in 1,125 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.5 | +4.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +2.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.2 | +0.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.9 | +3.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.6 | +1.5 |
|  | [[Gefitinib (drug)]] 5 µM |  | +2.3 | +2.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.8 | +4.5 |
|  | [[Erlotinib (drug)]] 5 µM |  | +1.6 | +2.4 |
|  | [[Lactate (calcium) (drug)]] 0.05 µM |  | +1.5 | +2.8 |
| fall | [[Selinexor (drug)]] 5 µM |  | -9.2 | -6.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -6.4 | -11.0 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -5.2 | -4.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.1 | -3.6 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.0 | -3.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.0 | -5.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.4 | -3.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -3.3 | -4.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.1 | -3.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.0 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | ER degradation enhancing alpha-mannosidase like protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q25.3 — chr1:184,690,237-184,754,907 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C1orf22 |
| Gene groups (HGNC) | Mannosidases alpha class 1 |
| Reactome | 4 pathways, smallest: ER Quality Control Compartment (ERQC); Calnexin/calreticulin cycle; N-glycan trimming in the ER and Calnexin/Calreticulin cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BZQ6](https://www.uniprot.org/uniprotkb/Q9BZQ6) (ER degradation-enhancing alpha-mannosidase-like protein 3):

> Involved in endoplasmic reticulum-associated degradation (ERAD). Accelerates the glycoprotein ERAD by proteasomes, by catalyzing mannose trimming from Man8GlcNAc2 to Man7GlcNAc2 in the N-glycans. May also participate in mannose trimming from all glycoproteins and not just misfolded ones targeted to ERAD. May have alpha 1,2-mannosidase activity (By similarity).

**Summary**, from NCBI Gene [80267](https://www.ncbi.nlm.nih.gov/gene/80267):

> Quality control in the endoplasmic reticulum (ER) ensures that only properly folded proteins are retained in the cell through recognition and degradation of misfolded or unassembled proteins. EDEM3 belongs to a group of proteins that accelerate degradation of misfolded glycoproteins in the ER (Hirao et al., 2006 [PubMed 16431915]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:16787](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16787) · Entrez [80267](https://www.ncbi.nlm.nih.gov/gene/80267) · UniProt [Q9BZQ6](https://www.uniprot.org/uniprotkb/Q9BZQ6) · Ensembl [ENSG00000116406](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116406)

## Data

Gene col 3794: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3794); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3794, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3794]; `tensor/DDL_lfc|DDL_z.npy` [3794]; `embed/gene_vectors.npy` [3794]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3794 or target_col == 3794). Every well: [[EDEM3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EDEM3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
