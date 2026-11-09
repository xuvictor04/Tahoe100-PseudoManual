---
symbol: "CFAP418"
type: "gene"
col: 7956
ensembl_id: "ENSG00000156172"
name: "cilia and flagella associated protein 418"
location: "8q22.1"
module: 46
arm: "+"
pooled_cpm: 6.93
n_lines_expressing: 48
n_dd_up: 20
n_dd_down: 10
n_dd_up_clean: 17
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# CFAP418

*cilia and flagella associated protein 418* — 8q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.76× (z +10.3, q 3e-22, up in 30 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (none with an alert); the strongest is [[Auranofin (drug)]] 5 µM: 0.627× (z -6.0, q 5e-07, down in 22 of 44 measured lines).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CASD1]] (+0.65, fdr 2e-04), [[ZNF827]] (+0.65, fdr 5e-05), [[TRAF3IP2-AS1]] (+0.64, fdr 3e-04); moves opposite to [[PLEKHM1P1]] (-0.61, fdr 3e-05), [[MYO9B]] (-0.59, fdr 4e-05), [[ARHGAP27P1-BPTFP1-KPNA2P3]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7956.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +10.3 | 3e-22 | 30/39 (RKO, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.46×** | +7.0 | 7e-10 | 16/40 (PANC-1, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.62×** | +6.0 | 3e-07 | 18/43 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.58×** | +5.9 | 5e-07 | 22/44 (HOP62, NCI-H1573, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.53×** | +5.3 | 1e-05 | 1/9 (HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.45×** | +4.8 | 2e-04 | 5/25 (NCI-H2030, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.46×** | +4.7 | 2e-04 | 10/40 (NCI-H1573, NCI-H23, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.43×** | +4.7 | 2e-04 | 14/43 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +4.1 | 0.002 | 14/45 (Panc 03.27, LoVo, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.37×** | +4.1 | 0.003 | 11/45 (HEC-1-A, SW48, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +4.0 | 0.004 | 13/46 (SW1417, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.39×** | +3.9 | 0.004 | 2/16 (HEC-1-A, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.35×** | +3.9 | 0.005 | 5/29 (PANC-1, NCI-H23, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +3.9 | 0.005 | 13/38 (HOP62, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.37×** | +3.8 | 0.006 | 8/45 (NCI-H2030, NCI-H1573, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.33×** | +3.5 | 0.017 | 7/42 (NCI-H1573, SNU-1, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.30×** | +3.3 | 0.031 | 9/42 (NCI-H23, NCI-H2030, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.27×** | +3.1 | 0.059 | 8/45 (AsPC-1, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7956.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.627×** | -6.0 | 5e-07 | 22/44 (SW1417, NCI-H23, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.410×** | -6.0 | 5e-07 | 16/43 (PANC-1, NCI-H2030, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.649×** | -5.6 | 5e-06 | 21/44 (PANC-1, HCT15, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.768×** | -4.8 | 2e-04 | 22/45 (KATO III, HepG2/C3A, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.705×** | -4.5 | 7e-04 | 13/44 (PANC-1, HS-578T, …) | two highest doses | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.729×** | -4.1 | 0.004 | 19/44 (PANC-1, HS-578T, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.749×** | -3.7 | 0.016 | 16/45 (PANC-1, HS-578T, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.585×** | -3.6 | 0.021 | 12/39 (NCI-H1573, A549, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.769×** | -3.4 | 0.044 | 9/45 (NCI-H1573, Panc 03.27, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.929× | -3.2 | 0.089 | 6/46 (SW1417, LS 180, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.786×** | -3.1 | 0.098 | 16/45 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Infigratinib (drug)]] 5 µM |  | 0.638× | -3.0 | 0.11 | 6/40 (Hs 766T, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | 0.785× | -3.0 | 0.12 | 6/44 (MIA PaCa-2, BT-474, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7956. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 19.3 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.261× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.349× (z -9.2) |
| [[A-427 (line)]] | wt | 12.2 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.137× (z -11.4) ⚠ cell-cycle shift, explains ~84% of this change |
| [[A549 (line)]] | wt | 16.4 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0683× (z -9.1) ⚠ toxic |
| [[HOP62 (line)]] | alt | 3.73 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0908× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[NCI-H2030 (line)]] | alt | 16.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.119× (z -12.3) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 15.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.212× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 5.93 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.106× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[SW1417 (line)]] | alt | 2.87 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0654× (z -8.9) |
| [[A-172 (line)]] | wt | 5.62 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.28 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.18 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.07 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.14 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.08 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.81 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.16 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.01 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.21 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.15 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.17 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.15 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.27 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7956), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CASD1]] | +0.65 | +0.54 / +0.32 | both halves | 2e-04 |  |
| [[ZNF827]] | +0.65 | +0.50 / +0.40 | both halves | 5e-05 |  |
| [[TRAF3IP2-AS1]] | +0.64 | +0.53 / +0.28 | both halves | 3e-04 |  |
| [[REV3L]] | +0.63 | +0.60 / +0.44 | both halves | 3e-05 |  |
| [[NFYB]] | +0.62 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[CGGBP1]] | +0.61 | +0.58 / +0.39 | both halves | 5e-05 |  |
| [[TSTD3]] | +0.61 | +0.62 / +0.18 | ⚠ one half (not replicated) | 0.001 |  |
| [[DHRS4-AS1]] | +0.61 | +0.68 / +0.30 | both halves | 2e-04 |  |
| [[ATP23]] | +0.61 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[FAM111A-DT]] | +0.60 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[HFE]] | +0.60 | +0.40 / +0.39 | both halves | 6e-05 |  |
| [[FOXJ2]] | +0.60 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[PUS10]] | +0.60 | +0.54 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLEKHM1P1]] | -0.61 | -0.58 / -0.46 | both halves | 3e-05 |  |
| [[MYO9B]] | -0.59 | -0.56 / -0.42 | both halves | 4e-05 |  |
| [[ARHGAP27P1-BPTFP1-KPNA2P3]] | -0.59 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[RBAK-RBAKDN]] | -0.58 | -0.56 / -0.40 | both halves | 4e-05 |  |
| [[CAP1]] | -0.57 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[KPNA2P3]] | -0.57 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[QSOX1]] | -0.57 | -0.55 / -0.39 | both halves | 5e-05 |  |
| [[TBC1D22A]] | -0.56 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[TPST2]] | -0.56 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[RRP7BP-1]] | -0.56 | -0.34 / -0.52 | both halves | 1e-04 |  |
| [[PDE2A]] | -0.56 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[BMP8A]] | -0.55 | -0.39 / -0.43 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers CFAP418's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.642). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (0.4, 12.5); signed map (24.3, -18.2). **Vector** length 60.5, 8.89% of its response variance represented; |z| ≥ 3 in 928 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +10.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.8 | +6.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.7 | +7.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +5.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.3 | +2.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.9 | +3.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.6 | +4.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.5 | +3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.4 | +3.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.5 | -6.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.5 | -3.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.5 | -3.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -1.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~84% of this change | -2.3 | -0.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.1 | -4.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.1 | -2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.7 | -1.9 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -1.7 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | cilia and flagella associated protein 418 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q22.1 — chr8:95,244,913-95,269,201 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MOT25, FLJ30600, CORD16, RP64, BBS21, FAP418, SMALLTALK; previously C8orf37 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96NL8](https://www.uniprot.org/uniprotkb/Q96NL8) (Cilia- and flagella-associated protein 418):

> May be involved in photoreceptor outer segment disk morphogenesis (By similarity).

**Summary**, from NCBI Gene [157657](https://www.ncbi.nlm.nih.gov/gene/157657):

> This gene encodes a ubiquitously expressed protein of unknown function. It has high levels of mRNA expression in the brain, heart, and retina and the protein co-localizes with polyglutamylated tubulin at the base of the primary cilium in human retinal pigment epithelial cells. Mutations in this gene have been associated with autosomal recessive cone-rod dystrophy (arCRD) and retinitis pigmentosa (arRP). [provided by RefSeq, Mar 2012]

**Accessions** — [HGNC:27232](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27232) · Entrez [157657](https://www.ncbi.nlm.nih.gov/gene/157657) · UniProt [Q96NL8](https://www.uniprot.org/uniprotkb/Q96NL8) · Ensembl [ENSG00000156172](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156172)

## Data

Gene col 7956: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7956); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7956, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7956]; `tensor/DDL_lfc|DDL_z.npy` [7956]; `embed/gene_vectors.npy` [7956]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7956 or target_col == 7956). Every well: [[CFAP418 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CFAP418.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
