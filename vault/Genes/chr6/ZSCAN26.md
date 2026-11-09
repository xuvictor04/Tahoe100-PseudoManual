---
symbol: "ZSCAN26"
type: "gene"
col: 12334
ensembl_id: "ENSG00000197062"
name: "zinc finger and SCAN domain containing 26"
location: "6p22.1"
module: 16
arm: "+"
pooled_cpm: 9.01
n_lines_expressing: 49
n_dd_up: 20
n_dd_down: 15
n_dd_up_clean: 17
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# ZSCAN26

*zinc finger and SCAN domain containing 26* — 6p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.80× (z +11.6, q 2e-28, up in 29 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.499× (z -9.8, q 1e-19, down in 24 of 34 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.624× (z -9.3, q 3e-18, down in 27 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZFP37]] (+0.72, fdr 7e-06), [[ZSCAN12]] (+0.70, fdr 7e-06), [[ZNF613]] (+0.70, fdr 7e-06); moves opposite to [[ATP1B3]] (-0.61, fdr 1e-05), [[FBXW7]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[KLHL29]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 3 with an alert ⚠; shown: the 15 strongest. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12334.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.80×** | +11.6 | 2e-28 | 29/46 (RKO, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.22×** | +10.8 | 1e-24 | 32/45 (RKO, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.94×** | +9.3 | 4e-18 | 37/46 (RKO, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.90×** | +9.0 | 2e-17 | 28/43 (RKO, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.63×** | +6.5 | 9e-09 | 24/44 (LoVo, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.57×** | +6.4 | 2e-08 | 21/46 (A-427, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.50×** | +5.7 | 1e-06 | 20/46 (LS 180, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.41×** | +4.8 | 1e-04 | 15/46 (HOP62, LS 180, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.35×** | +4.2 | 0.001 | 12/46 (LS 180, LoVo, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.37×** | +4.1 | 0.002 | 12/43 (CFPAC-1, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.24×** | +4.1 | 0.002 | 8/47 (NCI-H2030, HepG2/C3A, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.33×** | +3.9 | 0.005 | 11/45 (SW480, NCI-H1792, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.69×** | +3.8 | 0.005 | 11/46 (LoVo, LS 180, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.31×** | +3.8 | 0.006 | 16/46 (LoVo, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.67×** | +3.8 | 0.006 | 11/43 (LS 180, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12334.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.499×** | -9.8 | 1e-19 | 24/34 (NCI-H460, SW1417, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.624×** | -9.3 | 3e-18 | 27/44 (RKO, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.516×** | -9.3 | 4e-18 | 31/46 (SNU-423, SW480, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.564×** | -7.7 | 2e-12 | 26/39 (NCI-H1792, SNU-423, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.578×** | -7.7 | 2e-12 | 26/44 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.603×** | -7.1 | 1e-10 | 22/46 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.587×** | -6.9 | 4e-10 | 12/22 (NCI-H1792, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.634×** | -6.4 | 1e-08 | 22/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.672×** | -5.4 | 5e-06 | 21/46 (SNU-1, NCI-H23, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.691×** | -5.2 | 1e-05 | 19/46 (Hs 766T, NCI-H460, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.707×** | -4.9 | 6e-05 | 18/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.732×** | -4.4 | 6e-04 | 18/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **0.771×** | -3.5 | 0.020 | 10/16 (SW480, NCI-H460, …) | all doses, flat | composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **0.643×** | -3.2 | 0.049 | 6/44 (SW48, RKO, …) | rises with dose | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.789×** | -3.2 | 0.054 | 18/44 (NCI-H23, SNU-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12334. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 15.6 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.53× (z +13.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 8.73 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0854× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -8.8) |
| [[SW480 (line)]] | alt | 8.71 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.222× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.275× (z -9.2) |
| [[NCI-H1792 (line)]] | alt | 10.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.103× (z -11.2) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 4.89 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0816× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 11.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +9.8) | [[Dinaciclib (drug)]] 0.05 µM 0.180× (z -9.1) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 13.6 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0921× (z -9.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.114× (z -8.7) |
| [[SNU-423 (line)]] | alt | 13.9 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0361× (z -18.5) |
| [[SW1417 (line)]] | alt | 7.39 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.0889× (z -11.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 9.82 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.127× (z -11.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 11.0 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 4.65× (z +8.7) | — |
| [[C32 (line)]] | wt | 8.87 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.0897× (z -9.4) |
| [[HOP62 (line)]] | alt | 11.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.237× (z -8.8) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 5.99 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.199× (z -8.9) |
| [[J82 (line)]] | alt | 12.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.205× (z -9.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 11.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +9.7) | — |
| [[LS 180 (line)]] | wt | 7.37 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.87× (z +10.3) | — |
| [[NCI-H23 (line)]] | alt | 14.7 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.160× (z -11.0) ⚠ cell-cycle shift, explains ~28% of this change |
| [[PANC-1 (line)]] | alt | 11.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.257× (z -9.8) |
| [[RPMI-7951 (line)]] | alt | 11.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.110× (z -9.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 2.48 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.35 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.87 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.39 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 6.37 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.78 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.58 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.25 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.21 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.78 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.82 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12334), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFP37]] | +0.72 | +0.74 / +0.66 | both halves | 7e-06 | same gene group |
| [[ZSCAN12]] | +0.70 | +0.74 / +0.67 | both halves | 7e-06 | same gene group |
| [[ZNF613]] | +0.70 | +0.64 / +0.71 | both halves | 7e-06 | same gene group |
| [[ASB8]] | +0.70 | +0.77 / +0.61 | both halves | 7e-06 |  |
| [[NUDT12]] | +0.69 | +0.76 / +0.62 | both halves | 7e-06 |  |
| [[ZNF780A]] | +0.69 | +0.77 / +0.64 | both halves | 7e-06 | same gene group |
| [[ZNF624]] | +0.68 | +0.61 / +0.67 | both halves | 7e-06 | same gene group |
| [[ZNF484]] | +0.68 | +0.60 / +0.65 | both halves | 7e-06 | same gene group |
| [[DBT]] | +0.68 | +0.75 / +0.57 | both halves | 9e-06 |  |
| [[PSMD4]] | +0.67 | +0.73 / +0.60 | both halves | 7e-06 |  |
| [[KLHL9]] | +0.66 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[PHAX]] | +0.66 | +0.77 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP1B3]] | -0.61 | -0.62 / -0.49 | both halves | 1e-05 |  |
| [[FBXW7]] | -0.59 | -0.61 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLHL29]] | B | KLHL29 activity raises ZSCAN26's level | lines that do not express KLHL29 (7) vs lines expressing it (43) | 1.51× lower at baseline in the lines without KLHL29 | 0.013 | ⚠ within organs, on part of the lines; also absent: PCNX2, ENSG00000229983, ENSG00000271204; maybe low, not absent |
| [[SOGA3]] | B | SOGA3 activity raises ZSCAN26's level | lines that do not express SOGA3 (21) vs lines expressing it (29) | 1.30× lower at baseline in the lines without SOGA3 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: KIAA0408, ENSG00000255330, RFTN1 |
| [[KIAA0408]] | B | KIAA0408 activity raises ZSCAN26's level | lines that do not express KIAA0408 (22) vs lines expressing it (28) | 1.29× lower at baseline in the lines without KIAA0408 | 0.069 | ⚠ within organs, on part of the lines; also absent: SOGA3, ENSG00000255330, RFTN1 |
| [[TOP2A]] | B | TOP2A activity raises ZSCAN26's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ZNF571]] | B | ZNF571 activity raises ZSCAN26's level | lines that do not express ZNF571 (6) vs lines expressing it (44) | 1.84× lower at baseline in the lines without ZNF571 | 0.091 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ZNF420, ZNF850, ZNF540 |
| [[ZNF480]] | C | ZNF480 activity raises ZSCAN26's level | lines that do not express ZNF480 (3) vs lines expressing it (47) | 2.08× lower at baseline in the lines without ZNF480 | 0.018 | ⚠ few lines (3 vs 47); across organs; also absent: ZFP14, CIBAR1, ZNF540; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.714). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-32.4, 9.2); signed map (1.3, -26.0). **Vector** length 84.8, 16.2% of its response variance represented; |z| ≥ 3 in 1,053 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +6.4 | +10.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.3 | +9.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.2 | +9.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.6 | +6.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.4 | +4.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.8 | +4.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | +3.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +4.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.7 | -9.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -5.0 | -3.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.7 | -5.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.5 | -9.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.7 | -7.1 |
|  | [[EX229 (drug)]] 5 µM |  | -2.1 | -1.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.8 | -3.2 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.7 | -2.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.7 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger and SCAN domain containing 26 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.1 — chr6:28,267,058-28,278,224 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SRE-ZBP; previously ZNF187 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; SCAN domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16670](https://www.uniprot.org/uniprotkb/Q16670) (Zinc finger and SCAN domain-containing protein 26):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [7741](https://www.ncbi.nlm.nih.gov/gene/7741):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Located in nucleolus and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:12978](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12978) · Entrez [7741](https://www.ncbi.nlm.nih.gov/gene/7741) · UniProt [Q16670](https://www.uniprot.org/uniprotkb/Q16670) · Ensembl [ENSG00000197062](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197062)

## Data

Gene col 12334: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12334); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12334, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12334]; `tensor/DDL_lfc|DDL_z.npy` [12334]; `embed/gene_vectors.npy` [12334]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12334 or target_col == 12334). Every well: [[ZSCAN26 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZSCAN26.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
