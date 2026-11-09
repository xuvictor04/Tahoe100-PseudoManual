---
symbol: "TTC30A"
type: "gene"
col: 12415
ensembl_id: "ENSG00000197557"
name: "intraflagellar transport 70A"
location: "2q31.2"
module: 16
arm: "+"
pooled_cpm: 2.5
n_lines_expressing: 44
n_dd_up: 12
n_dd_down: 22
n_dd_up_clean: 10
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 4
direction_downstream: 6
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# TTC30A

*intraflagellar transport 70A* — 2q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.83× (z +6.5, q 5e-08, up in 14 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.252× (z -10.4, q 2e-22, down in 32 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DUSP19]] (+0.73, fdr 7e-06), [[EID1]] (+0.70, fdr 7e-06), [[CSTF2T]] (+0.66, fdr 7e-06); moves opposite to [[SLC37A3]] (-0.56, fdr 1e-05), [[GAN]] (-0.56, fdr 1e-05), [[CAMKK2]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ID2-AS1]] → it (grade B ⚠); 6 go from it, the strongest it → [[LINC00205]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12415.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **1.83×** | +6.5 | 5e-08 | 14/40 (NCI-H1573, NCI-H2030, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.17×** | +5.7 | 4e-06 | 0/2 | inconsistent across doses | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.06×** | +5.1 | 7e-05 | 0/4 | inconsistent across doses | cell-cycle shift (explains ~10% here); composition shift |
| [[Darinaparsin (drug)]] 5 µM |  | **1.51×** | +4.4 | 0.001 | 8/39 (NCI-H1792, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.70×** | +3.9 | 0.012 | 9/32 (HS-578T, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.65×** | +3.8 | 0.012 | 9/37 (SK-MEL-2, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.60×** | +3.8 | 0.012 | 6/25 (HOP62, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.51×** | +3.7 | 0.018 | 9/31 (NCI-H23, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.40×** | +3.6 | 0.018 | 6/39 (NCI-H2030, Panc 03.27, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.60×** | +3.6 | 0.019 | 7/40 (A498, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.53×** | +3.2 | 0.060 | 6/41 (HOP62, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Larotrectinib (drug)]] 5 µM |  | **1.34×** | +3.2 | 0.073 | 1/38 (PANC-1) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM |  | 1.48× | +3.0 | 0.11 | 0/32 | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12415.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.252×** | -10.4 | 2e-22 | 32/41 (A-427, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.316×** | -8.7 | 1e-15 | 23/25 (CFPAC-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.318×** | -8.6 | 1e-15 | 28/38 (SHP-77, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.439×** | -5.8 | 7e-07 | 20/35 (PANC-1, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.608×** | -5.3 | 1e-05 | 21/37 (NCI-H1573, LoVo, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.517×** | -5.0 | 7e-05 | 21/36 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.545×** | -4.6 | 4e-04 | 16/36 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.545×** | -4.6 | 4e-04 | 18/40 (NCI-H460, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **0.319×** | -4.5 | 4e-04 | 14/25 (NCI-H460, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.679×** | -4.1 | 0.002 | 12/31 (A-172, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.686×** | -4.0 | 0.004 | 12/32 (COLO 205, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.596×** | -3.9 | 0.005 | 13/40 (Panc 03.27, LoVo, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.607×** | -3.7 | 0.008 | 14/37 (SW1417, SK-MEL-2, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.619×** | -3.6 | 0.013 | 12/41 (C-33 A, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.622×** | -3.6 | 0.014 | 12/40 (LOX-IMVI, A-172, …) | top dose only | position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **0.639×** | -3.2 | 0.042 | 10/36 (NCI-H2030, NCI-H23, …) | two highest doses |  |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.638×** | -3.2 | 0.046 | 6/39 (SW 900, RPMI-7951, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12415. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 3.41 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0323× (z -10.6) |
| [[NCI-H460 (line)]] | wt | 4.44 | 0 | 2 | — | [[Digitoxin (drug)]] 0.05 µM 0.0335× (z -14.7) |
| [[CFPAC-1 (line)]] | alt | 4.16 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0587× (z -9.1) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 5.45 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -9.0) |
| [[NCI-H1573 (line)]] | alt | 5.01 | 0 | 1 | — | [[Pioglitazone (drug)]] 0.5 µM 0.0658× (z -9.3) |
| [[SHP-77 (line)]] | alt | 4.42 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0347× (z -9.7) |
| [[A-172 (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.415 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.346 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.43 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.33 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.724 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.182 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.999 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.874 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.573 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.423 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.499 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.58 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12415), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DUSP19]] | +0.73 | +0.73 / +0.66 | both halves | 7e-06 |  |
| [[EID1]] | +0.70 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[CSTF2T]] | +0.66 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[BBS10]] | +0.66 | +0.66 / +0.61 | both halves | 7e-06 | pathway: Assembly of the 9+0 primary cilium |
| [[PABIR1]] | +0.65 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[FANCF]] | +0.63 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[B3GALT9]] | +0.63 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[HERPUD2-AS1]] | +0.62 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[ZKSCAN3]] | +0.61 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[FAM174A-DT]] | +0.61 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[PLPP6]] | +0.60 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[C7orf25]] | +0.58 | +0.56 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC37A3]] | -0.56 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[GAN]] | -0.56 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[CAMKK2]] | -0.55 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[CERS5]] | -0.54 | -0.61 / -0.45 | both halves | 3e-05 |  |
| [[MROH1]] | -0.53 | -0.42 / -0.59 | both halves | 4e-05 |  |
| [[TPTEP2-CSNK1E]] | -0.53 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[LIPE-AS1]] | -0.52 | -0.35 / -0.52 | both halves | 1e-04 |  |
| [[ABHD18]] | -0.52 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[PAM16]] | -0.51 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[LMBR1]] | -0.51 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[SLC35D2]] | -0.51 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[COX7A2L]] | -0.50 | -0.49 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ID2-AS1]] | B | ID2-AS1 activity raises TTC30A's level | lines that do not express ID2-AS1 (8) vs lines expressing it (42) | 1.54× lower at baseline in the lines without ID2-AS1 | 0.006 | ⚠ within organs, on part of the lines; also absent: ID2, RDM1P5 |
| [[FBXO15]] | B | FBXO15 activity raises TTC30A's level | lines that do not express FBXO15 (6) vs lines expressing it (44) | 1.98× lower at baseline in the lines without FBXO15 | 0.072 | ⚠ within organs, on part of the lines; also absent: DNAI1, EFCAB6, KCNK15-AS1 |
| [[EID1]] | C | EID1 activity raises TTC30A's level | lines that do not express EID1 (3) vs lines expressing it (47) | 2.41× lower at baseline in the lines without EID1 | 0.080 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: MNS1, ENSG00000283491, AGK |
| [[LRRIQ3]] | C | LRRIQ3 activity raises TTC30A's level | lines that do not express LRRIQ3 (4) vs lines expressing it (46) | 2.04× lower at baseline in the lines without LRRIQ3 | 0.088 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENTPD1-AS1, CEP41, C1orf216; maybe low, not absent; its own permutation p |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00205]] | B | TTC30A activity raises LINC00205's level | lines that do not express TTC30A (6) vs lines expressing it (44) | 2.11× lower at baseline in the lines without TTC30A | 0.015 | ⚠ within organs, on part of the lines; also absent: WDR35, GGT7, AGK; maybe low, not absent |
| [[DRD4]] | B | TTC30A activity raises DRD4's level | lines that do not express TTC30A (6) vs lines expressing it (44) | 1.61× lower at baseline in the lines without TTC30A | 0.025 | ⚠ within organs, on part of the lines; also absent: WDR35, GGT7, AGK; maybe low, not absent |
| [[EID1]] | B | TTC30A activity raises EID1's level | lines that do not express TTC30A (6) vs lines expressing it (44) | 2.69× lower at baseline in the lines without TTC30A | 0.070 | ⚠ within organs, on part of the lines; also absent: WDR35, GGT7, AGK; maybe low, not absent |
| [[CASC2]] | B | TTC30A activity raises CASC2's level | lines that do not express TTC30A (6) vs lines expressing it (44) | 1.59× lower at baseline in the lines without TTC30A | 0.079 | ⚠ within organs, on part of the lines; also absent: WDR35, GGT7, AGK; maybe low, not absent |
| [[ID2-AS1]] | B | TTC30A activity raises ID2-AS1's level | lines that do not express TTC30A (6) vs lines expressing it (44) | 1.57× lower at baseline in the lines without TTC30A | 0.083 | ⚠ within organs, on part of the lines; also absent: WDR35, GGT7, AGK; maybe low, not absent |
| [[CENPBD1P]] | B | TTC30A activity raises CENPBD1P's level | lines that do not express TTC30A (6) vs lines expressing it (44) | 1.42× lower at baseline in the lines without TTC30A | 0.089 | ⚠ within organs, on part of the lines; also absent: WDR35, GGT7, AGK; maybe low, not absent |

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.595). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-35.4, 17.9); signed map (-0.8, -30.4). **Vector** length 57.1, 9.07% of its response variance represented; |z| ≥ 3 in 980 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +4.6 | +3.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.4 | +3.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.0 | +6.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.8 | +3.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.8 | +3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +2.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.3 | +1.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.2 | +1.9 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.7 | -5.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.6 | -3.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.4 | -5.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.3 | -8.6 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.0 | -4.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.8 | -2.0 |
|  | [[EX229 (drug)]] 5 µM |  | -1.8 | -4.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.6 | -3.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.6 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | intraflagellar transport 70A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.2 — chr2:177,612,999-177,618,742 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13946, FAP259, CFAP259; previously TTC30A |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing; IFT-B1 complex |
| Reactome | 4 pathways, smallest: Intraflagellar transport; Assembly of the 9+0 primary cilium; Cilium Assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86WT1](https://www.uniprot.org/uniprotkb/Q86WT1) (Intraflagellar transport protein 70A):

> Required for polyglutamylation of axonemal tubulin. Plays a role in anterograde intraflagellar transport (IFT), the process by which cilia precursors are transported from the base of the cilium to the site of their incorporation at the tip.

**Summary**, from NCBI Gene [92104](https://www.ncbi.nlm.nih.gov/gene/92104):

> Predicted to enable intraciliary transport particle B binding activity. Predicted to be involved in intraciliary transport. Predicted to be located in centrosome. Predicted to be part of intraciliary transport particle B. Predicted to be active in axonemal microtubule. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25853](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25853) · Entrez [92104](https://www.ncbi.nlm.nih.gov/gene/92104) · UniProt [Q86WT1](https://www.uniprot.org/uniprotkb/Q86WT1) · Ensembl [ENSG00000197557](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197557)

## Data

Gene col 12415: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12415); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12415, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12415]; `tensor/DDL_lfc|DDL_z.npy` [12415]; `embed/gene_vectors.npy` [12415]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12415 or target_col == 12415). Every well: [[TTC30A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TTC30A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
