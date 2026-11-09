---
symbol: "GHDC"
type: "gene"
col: 9559
ensembl_id: "ENSG00000167925"
name: "GH3 domain containing"
location: "17q21.2"
module: 157
arm: "+"
pooled_cpm: 3.9
n_lines_expressing: 49
n_dd_up: 12
n_dd_down: 14
n_dd_up_clean: 6
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/157"]
generated_by: "tahoemap"
---

# GHDC

*GH3 domain containing* — 17q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.71× (z +9.5, q 2e-18, up in 6 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.69× (z +7.3, q 5e-11, up in 15 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.386× (z -13.4, q 5e-38, down in 32 of 38 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CTSF]] (+0.55, fdr 2e-05), [[SPPL3]] (+0.55, fdr 4e-05), [[PPM1M]] (+0.54, fdr 3e-05); moves opposite to [[IBTK]] (-0.50, fdr 0.001, ⚠ one half only (not replicated)), [[CCDC18]] (-0.44, fdr 6e-05), [[MIB1]] (-0.44, fdr 5e-05), [[UBE2V2]] (-0.43, fdr 5e-05).
> It is in [[Module 157]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9559.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.71×** | +9.5 | 2e-18 | 6/8 (NCI-H2030, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.49×** | +9.0 | 5e-17 | 19/21 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.69×** | +7.3 | 5e-11 | 15/44 (SW480, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.11×** | +6.8 | 1e-09 | 3/9 (HEC-1-A, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.16× | +5.1 | 3e-05 | 10/47 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.56×** | +4.4 | 0.001 | 7/24 (LS 180, A498, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.00×** | +3.6 | 0.028 | 2/11 (NCI-H2030, HEC-1-A) | top dose only | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.71×** | +3.3 | 0.060 | 1/39 (AsPC-1) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.70×** | +3.3 | 0.060 | 4/37 (SW480, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.67×** | +3.2 | 0.075 | 3/33 (HEC-1-A, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.075 | 6/45 (HS-578T, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.38×** | +3.2 | 0.075 | 10/35 (KATO III, SNU-423, …) | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.37×** | +3.1 | 0.075 | 7/34 (A-427, NCI-H1573, …) | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, none with an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9559.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.386×** | -13.4 | 5e-38 | 32/38 (NCI-H2030, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.449×** | -8.0 | 5e-13 | 26/35 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.516×** | -6.6 | 9e-09 | 21/44 (SHP-77, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.598×** | -4.9 | 1e-04 | 23/44 (COLO 205, LoVo, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Verteporfin (drug)]] 5 µM |  | **0.642×** | -4.3 | 0.002 | 14/39 (PANC-1, SW480, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.655×** | -4.2 | 0.002 | 16/43 (A-427, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.678×** | -3.9 | 0.009 | 15/46 (SNU-1, RKO, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Hydroxyurea (drug)]] 5 µM |  | **0.671×** | -3.8 | 0.009 | 13/42 (hTERT-HPNE, HOP62, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.684×** | -3.8 | 0.010 | 14/46 (LoVo, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.499×** | -3.6 | 0.017 | 8/38 (KATO III, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.698×** | -3.6 | 0.017 | 12/43 (SW480, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~8% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.702×** | -3.5 | 0.020 | 11/44 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.720×** | -3.3 | 0.046 | 9/43 (LoVo, C-33 A, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.544×** | -3.2 | 0.062 | 6/33 (A549, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9559. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 3.71 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0837× (z -8.6) |
| [[A-427 (line)]] | wt | 4.10 | 0 | 1 | — | [[Flumatinib (mesylate) (drug)]] 0.05 µM 0.0550× (z -9.3) |
| [[A498 (line)]] | wt | 6.14 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.176× (z -8.7) |
| [[LS 180 (line)]] | wt | 3.90 | 0 | 1 | — | [[Rifaximin (drug)]] 5 µM 0.0644× (z -8.6) |
| [[MIA PaCa-2 (line)]] | alt | 3.74 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0723× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 9.63 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -11.0) |
| [[NCI-H460 (line)]] | wt | 3.43 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -9.7) |
| [[Panc 03.27 (line)]] | alt | 6.44 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -10.5) |
| [[SW1417 (line)]] | alt | 4.47 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -9.7) |
| [[SW480 (line)]] | alt | 4.24 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -9.3) |
| [[A-172 (line)]] | wt | 3.76 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.806 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.89 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.11 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.66 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.60 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.61 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.37 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.98 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.07 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.20 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9559), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTSF]] | +0.55 | +0.56 / +0.46 | both halves | 2e-05 |  |
| [[SPPL3]] | +0.55 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[PPM1M]] | +0.54 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[GLMP]] | +0.54 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[DOC2A]] | +0.52 | +0.50 / +0.35 | both halves | 1e-04 |  |
| [[ATP6V1B2]] | +0.52 | +0.48 / +0.36 | both halves | 1e-04 |  |
| [[SPATA20]] | +0.51 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[GM2A]] | +0.51 | +0.54 / +0.40 | both halves | 4e-05 |  |
| [[IL11RA]] | +0.49 | +0.47 / +0.20 | both halves | 7e-04 |  |
| [[TMEM198B]] | +0.49 | +0.53 / +0.29 | both halves | 3e-04 |  |
| [[SLC9A3-AS1]] | +0.49 | +0.48 / +0.38 | both halves | 7e-05 |  |
| [[SCRN2]] | +0.49 | +0.40 / +0.73 | both halves | 5e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IBTK]] | -0.50 | -0.64 / -0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[CCDC18]] | -0.44 | -0.39 / -0.41 | both halves | 6e-05 |  |
| [[MIB1]] | -0.44 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[UBE2V2]] | -0.43 | -0.43 / -0.39 | both halves | 5e-05 |  |
| [[UBXN4]] | -0.43 | -0.54 / -0.15 | ⚠ one half (not replicated) | 0.001 |  |
| [[CLIP1]] | -0.42 | -0.43 / -0.34 | both halves | 1e-04 |  |
| [[CLOCK]] | -0.42 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[SELENOI]] | -0.42 | -0.31 / -0.54 | both halves | 2e-04 |  |
| [[CYCS]] | -0.41 | -0.26 / -0.55 | both halves | 3e-04 |  |
| [[UCHL5]] | -0.40 | -0.46 / -0.34 | both halves | 1e-04 |  |
| [[PDAP1]] | -0.39 | -0.33 / -0.42 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 157]]; 28 genes; every member is in the + arm (projection on the module's main direction 0.412). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (5.6, -29.0); signed map (-7.9, 1.3). **Vector** length 41.2, 4.39% of its response variance represented; |z| ≥ 3 in 870 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.6 | +7.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +9.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.7 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.4 | +6.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.3 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +2.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | +2.9 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.4 | +3.3 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.3 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +1.2 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.6 | -8.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.2 | -13.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -1.5 | -4.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -2.5 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.1 | -3.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -2.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.1 | -1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -0.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.0 | -2.0 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.0 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | GH3 domain containing |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.2 — chr17:42,188,799-42,194,513 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LGP1 |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

UniProt [Q8N2G8](https://www.uniprot.org/uniprotkb/Q8N2G8) carries no function annotation.

**Summary**, from NCBI Gene [84514](https://www.ncbi.nlm.nih.gov/gene/84514):

> Predicted to enable acid-amino acid ligase activity. Located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24438](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24438) · Entrez [84514](https://www.ncbi.nlm.nih.gov/gene/84514) · UniProt [Q8N2G8](https://www.uniprot.org/uniprotkb/Q8N2G8) · Ensembl [ENSG00000167925](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167925)

## Data

Gene col 9559: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9559); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9559, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9559]; `tensor/DDL_lfc|DDL_z.npy` [9559]; `embed/gene_vectors.npy` [9559]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9559 or target_col == 9559). Every well: [[GHDC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GHDC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
