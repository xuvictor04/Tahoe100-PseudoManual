---
symbol: "DTX4"
type: "gene"
col: 3103
ensembl_id: "ENSG00000110042"
name: "deltex E3 ubiquitin ligase 4"
location: "11q12.1"
module: 44
arm: "+"
pooled_cpm: 8.59
n_lines_expressing: 43
n_dd_up: 23
n_dd_down: 15
n_dd_up_clean: 20
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 9
direction_downstream: 3
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# DTX4

*deltex E3 ubiquitin ligase 4* — 11q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.36× (z +6.4, q 7e-08, up in 12 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.659× (z -6.2, q 2e-07, down in 19 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMCC2]] (+0.54, fdr 3e-05), [[MIR3142HG]] (+0.53, fdr 1e-05), [[CDX2]] (+0.52, fdr 3e-05); moves opposite to [[GON4L]] (-0.42, fdr 5e-05), [[SLC25A16]] (-0.42, fdr 1e-04).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[PRR15L]] → it (grade B ⚠); 3 go from it, the strongest it → [[CAMK1D]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3103.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.36×** | +6.4 | 7e-08 | 12/39 (SW480, C32, …) | rises with dose | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.34×** | +6.2 | 2e-07 | 13/38 (A498, A-172, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.44×** | +5.8 | 2e-06 | 11/37 (A-172, A498, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.46×** | +5.6 | 3e-06 | 14/38 (SW480, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Radotinib (drug)]] 5 µM |  | **1.29×** | +5.4 | 7e-06 | 12/39 (AsPC-1, A-427, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.44×** | +5.4 | 7e-06 | 15/37 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +5.3 | 1e-05 | 3/41 (LoVo, Panc 03.27, …) | inconsistent across doses |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.35×** | +4.4 | 7e-04 | 6/38 (SW1417, A549, …) | inconsistent across doses | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.34×** | +4.4 | 7e-04 | 17/39 (LoVo, KATO III, …) | rises with dose |  |
| [[Bentamapimod (drug)]] 0.05 µM |  | **1.35×** | +4.2 | 0.001 | 9/38 (KATO III, Panc 03.27, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.22×** | +4.2 | 0.002 | 13/35 (A-172, CFPAC-1, …) | inconsistent across doses | composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.30×** | +3.9 | 0.005 | 8/36 (HepG2/C3A, LoVo, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.28×** | +3.7 | 0.010 | 2/39 (KATO III, HEC-1-A) | top dose only | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.28×** | +3.6 | 0.012 | 8/38 (SW480, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.29×** | +3.4 | 0.022 | 0/17 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.022 | 6/38 (NCI-H2030, NCI-H2347, …) | rises with dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.38×** | +3.4 | 0.024 | 8/37 (SW1417, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.38×** | +3.4 | 0.024 | 3/33 (A498, NCI-H2030, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.25×** | +3.3 | 0.029 | 4/39 (SNU-423, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3103.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.659×** | -6.2 | 2e-07 | 19/39 (RKO, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.671×** | -6.0 | 7e-07 | 18/38 (LOX-IMVI, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.676×** | -5.9 | 8e-07 | 20/38 (COLO 205, Panc 03.27, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.709×** | -5.1 | 3e-05 | 10/38 (NCI-H2347, NCI-H460, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.785×** | -5.1 | 3e-05 | 14/39 (HT-29, KATO III, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.736×** | -4.6 | 4e-04 | 15/38 (A-427, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.784×** | -3.7 | 0.020 | 14/25 (LOX-IMVI, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.796×** | -3.4 | 0.034 | 7/38 (SNU-423, hTERT-HPNE, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.796×** | -3.4 | 0.034 | 11/38 (LOX-IMVI, NCI-H460, …) | top dose only |  |
| [[Chlorhexidine (diacetate) (drug)]] 0.5 µM |  | **0.796×** | -3.4 | 0.034 | 6/39 (NCI-H23, CHP-212, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.797×** | -3.4 | 0.034 | 11/37 (SK-MEL-2, hTERT-HPNE, …) | all doses, stronger at high dose | position effect removed |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.801×** | -3.3 | 0.039 | 8/37 (SNU-423, A498, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.809×** | -3.2 | 0.061 | 11/38 (H4, HT-29, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.813×** | -3.1 | 0.069 | 15/38 (COLO 205, HT-29, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.813×** | -3.1 | 0.069 | 5/38 (SK-MEL-2, HT-29, …) | two highest doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3103. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 24.4 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -9.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.157× (z -9.5) |
| [[LOX-IMVI (line)]] | wt | 17.6 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0405× (z -19.3) ⚠ toxic; transcription drop · without an alert: [[Trametinib (drug)]] 5 µM 0.194× (z -9.9) |
| [[A-172 (line)]] | wt | 9.35 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.32× (z +11.5) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[A-427 (line)]] | wt | 7.88 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.128× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.162× (z -8.7) |
| [[BT-474 (line)]] | alt | 6.91 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0749× (z -12.4) ⚠ cell-cycle shift, explains ~28% of this change |
| [[HT-29 (line)]] | alt | 20.0 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.228× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 27.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.218× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~4% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.261× (z -9.4) |
| [[SNU-423 (line)]] | alt | 19.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0590× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~4% of this change · without an alert: [[Clobetasol propionate (drug)]] 0.5 µM 0.177× (z -9.4) |
| [[C32 (line)]] | wt | 4.83 | 0 | 1 | — | [[Fulvestrant (drug)]] 0.5 µM 0.0610× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 7.00 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.36× (z +9.4) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[H4 (line)]] | wt | 7.89 | 0 | 1 | — | [[Betamethasone dipropionate (drug)]] 5 µM 0.0358× (z -9.1) |
| [[HCT15 (line)]] | alt | 11.7 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0825× (z -9.4) ⚠ toxic |
| [[LoVo (line)]] | wt | 18.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0926× (z -15.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 5.33 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.129× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~34% of this change |
| [[RKO (line)]] | wt | 4.54 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0434× (z -9.7) |
| [[SNU-1 (line)]] | wt | 6.89 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0468× (z -9.4) |
| [[SW48 (line)]] | wt | 16.0 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 0.05 µM 0.0793× (z -9.7) |
| [[A498 (line)]] | wt | 7.54 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.94 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.67 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.85 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.33 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.64 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.41 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.10 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.780 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.79 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.951 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.761 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.32 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3103), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMCC2]] | +0.54 | +0.61 / +0.44 | both halves | 3e-05 |  |
| [[MIR3142HG]] | +0.53 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[CDX2]] | +0.52 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[ATP8B1]] | +0.51 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[PRR15]] | +0.51 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[PIK3C2B]] | +0.51 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[RASSF3]] | +0.51 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[SMAD7]] | +0.50 | +0.46 / +0.49 | both halves | 3e-05 |  |
| [[GATM]] | +0.49 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[RSPH1]] | +0.49 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[CYP2S1]] | +0.48 | +0.53 / +0.37 | both halves | 8e-05 |  |
| [[SLC11A2]] | +0.48 | +0.47 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GON4L]] | -0.42 | -0.42 / -0.39 | both halves | 5e-05 |  |
| [[SLC25A16]] | -0.42 | -0.36 / -0.41 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRR15L]] | B | PRR15L activity raises DTX4's level | lines that do not express PRR15L (38) vs lines expressing it (12) | 2.44× lower at baseline in the lines without PRR15L | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53, CDKN2A; also absent: TMEM30B, CDH17, ENSG00000267881 |
| [[TJP3]] | B | TJP3 activity raises DTX4's level | lines that do not express TJP3 (29) vs lines expressing it (21) | 1.91× lower at baseline in the lines without TJP3 | 0.017 | ⚠ within organs, on part of the lines; also absent: KDF1, EPCAM, CDH1 |
| [[PLEKHG6]] | B | PLEKHG6 activity raises DTX4's level | lines that do not express PLEKHG6 (26) vs lines expressing it (24) | 1.90× lower at baseline in the lines without PLEKHG6 | 0.022 | ⚠ within organs, on part of the lines; also absent: SCNN1A, KDF1, RNF39; maybe low, not absent |
| [[CLDN3]] | B | CLDN3 activity raises DTX4's level | lines that do not express CLDN3 (28) vs lines expressing it (22) | 1.76× lower at baseline in the lines without CLDN3 | 0.022 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, ESRP1 |
| [[ILDR1]] | B | ILDR1 activity raises DTX4's level | lines that do not express ILDR1 (31) vs lines expressing it (19) | 1.88× lower at baseline in the lines without ILDR1 | 0.024 | ⚠ within organs, on part of the lines; also absent: TMEM125, ESRP1, SLC5A1 |
| [[MUC13]] | B | MUC13 activity raises DTX4's level | lines that do not express MUC13 (40) vs lines expressing it (10) | 2.45× lower at baseline in the lines without MUC13 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, NPSR1, CDH17 |
| [[VIPR1]] | B | VIPR1 activity raises DTX4's level | lines that do not express VIPR1 (24) vs lines expressing it (26) | 1.88× lower at baseline in the lines without VIPR1 | 0.031 | ⚠ within organs, on part of the lines; also absent: ESRP1, IRF6, ENSG00000262302 |
| [[MUC3A]] | B | MUC3A activity raises DTX4's level | lines that do not express MUC3A (25) vs lines expressing it (25) | 1.57× lower at baseline in the lines without MUC3A | 0.058 | ⚠ within organs, on part of the lines; also absent: HSH2D, ADGRF1, CKMT1B |
| [[CRACDL]] | B | CRACDL activity raises DTX4's level | lines that do not express CRACDL (25) vs lines expressing it (25) | 1.67× lower at baseline in the lines without CRACDL | 0.060 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CGN, MARVELD3, CASC19 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CAMK1D]] | B | DTX4 activity lowers CAMK1D's level | lines that do not express DTX4 (7) vs lines expressing it (43) | 2.85× higher at baseline in the lines without DTX4 | 0.039 | ⚠ within organs, on part of the lines; also absent: NEO1, WNK4, STPG2 |
| [[TJP3]] | B | DTX4 activity raises TJP3's level | lines that do not express DTX4 (7) vs lines expressing it (43) | 2.80× lower at baseline in the lines without DTX4 | 0.092 | ⚠ within organs, on part of the lines; also absent: NEO1, WNK4, STPG2 |
| [[NEO1]] | C | DTX4 activity raises NEO1's level | lines that do not express DTX4 (7) vs lines expressing it (43) | 3.76× lower at baseline in the lines without DTX4 | 0.050 | ⚠ within organs, on part of the lines; also absent: NEO1, WNK4, STPG2; co-absent with the target |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.518). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (30.9, 0.5); signed map (49.9, 3.7). **Vector** length 79.9, 16.3% of its response variance represented; |z| ≥ 3 in 882 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.7 | +3.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.0 | +5.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.9 | +5.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.5 | +6.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +6.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +4.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +3.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.2 | +3.9 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -2.3 | -3.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.0 | -6.0 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.9 | -1.9 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.9 | -1.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.8 | -5.9 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.8 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | deltex E3 ubiquitin ligase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.1 — chr11:59,171,430-59,208,588 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0937, RNF155 |
| Gene groups (HGNC) | Ring finger proteins; Deltex E3 ubiquitin ligase family |
| Hallmark sets | NOTCH_SIGNALING |
| Reactome | 10 pathways, smallest: IRF3 mediated activation of type 1 IFN; IRF3-mediated induction of type I IFN; Regulation of innate immune responses to cytosolic DNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2E6](https://www.uniprot.org/uniprotkb/Q9Y2E6) (E3 ubiquitin-protein ligase DTX4):

> Regulator of Notch signaling, a signaling pathway involved in cell-cell communications that regulates a broad spectrum of cell-fate determinations (By similarity). Functions as a ubiquitin ligase protein in vivo, mediating 'Lys48'-linked polyubiquitination and promoting degradation of TBK1, targeting to TBK1 requires interaction with NLRP4.

**Summary**, from NCBI Gene [23220](https://www.ncbi.nlm.nih.gov/gene/23220):

> Enables ubiquitin protein ligase activity. Involved in negative regulation of innate immune response; proteasome-mediated ubiquitin-dependent protein catabolic process; and protein K48-linked ubiquitination. Is active in centrosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29151](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29151) · Entrez [23220](https://www.ncbi.nlm.nih.gov/gene/23220) · UniProt [Q9Y2E6](https://www.uniprot.org/uniprotkb/Q9Y2E6) · Ensembl [ENSG00000110042](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110042)

## Data

Gene col 3103: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3103); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3103, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3103]; `tensor/DDL_lfc|DDL_z.npy` [3103]; `embed/gene_vectors.npy` [3103]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3103 or target_col == 3103). Every well: [[DTX4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DTX4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
