---
symbol: "PAXIP1-DT"
type: "gene"
col: 15781
ensembl_id: "ENSG00000273344"
name: "PAXIP1 divergent transcript"
location: "7q36.2"
module: 14
arm: "+"
pooled_cpm: 3.9
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 5
n_dd_up_clean: 15
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# PAXIP1-DT

*PAXIP1 divergent transcript* — 7q36.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.77× (z +13.0, q 1e-35, up in 4 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.83× (z +8.7, q 6e-16, up in 21 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.550× (z -5.7, q 7e-06, down in 20 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM200B]] (+0.63, fdr 7e-06), [[WASL-DT]] (+0.62, fdr 8e-06), [[GATM]] (+0.59, fdr 1e-05); moves opposite to [[HERC2P3]] (-0.57, fdr 2e-05), [[PCYT1A]] (-0.53, fdr 9e-05), [[UFD1]] (-0.52, fdr 1e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15781.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.77×** | +13.0 | 1e-35 | 4/5 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.67×** | +12.2 | 8e-32 | 5/7 (PANC-1, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.92×** | +10.9 | 3e-25 | 16/18 (HEC-1-A, KATO III, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +8.7 | 6e-16 | 21/35 (A498, A549, …) | top dose only | cell-cycle shift (explains ~3% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.73×** | +7.9 | 3e-13 | 20/45 (PANC-1, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.06×** | +7.1 | 2e-10 | 7/20 (PANC-1, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.87×** | +6.1 | 8e-08 | 22/42 (SW 900, A-172, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.67×** | +5.2 | 1e-05 | 10/17 (SW1417, NCI-H23, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.65×** | +5.1 | 2e-05 | 18/45 (A498, A-172, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.40×** | +4.9 | 6e-05 | 12/45 (A498, C32, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.33×** | +4.1 | 0.002 | 12/36 (CFPAC-1, SW 900, …) | rises with dose | composition shift |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.64×** | +3.6 | 0.015 | 2/34 (SW1417, SW48) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.42×** | +3.6 | 0.016 | 5/42 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.41×** | +3.5 | 0.017 | 5/47 (A498, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.40×** | +3.4 | 0.023 | 13/44 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.38×** | +3.3 | 0.038 | 8/47 (A498, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~19% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.37×** | +3.2 | 0.050 | 2/46 (A-172, Panc 03.27) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **1.36×** | +3.1 | 0.051 | 3/46 (A498, A-172, …) | all doses, flat | cell-cycle shift (explains ~20% here) |
| [[Entrectinib (drug)]] 5 µM |  | **1.34×** | +3.0 | 0.071 | 7/44 (KATO III, hTERT-HPNE, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.51×** | +3.0 | 0.071 | 1/18 (A-172) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.34×** | +3.0 | 0.074 | 13/35 (A-172, SW 900, …) | rises with dose | cell-cycle shift (explains ~5% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15781.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **0.550×** | -5.7 | 7e-06 | 20/41 (NCI-H23, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.673×** | -4.0 | 0.016 | 13/44 (MIA PaCa-2, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.677×** | -3.9 | 0.016 | 17/47 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Hydroxyurea (drug)]] 5 µM |  | **0.680×** | -3.7 | 0.027 | 10/42 (SW48, NCI-H460, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.707×** | -3.5 | 0.054 | 15/43 (LS 180, SW480, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15781. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 2.77 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.46× (z +9.0) | — |
| [[HEC-1-A (line)]] | alt | 6.77 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.91× (z +8.9) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 5.47 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.114× (z -8.8) |
| [[A-172 (line)]] | wt | 2.63 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.00 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.16 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.46 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.13 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.52 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.30 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15781), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM200B]] | +0.63 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[WASL-DT]] | +0.62 | +0.58 / +0.66 | both halves | 8e-06 | same gene group |
| [[GATM]] | +0.59 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[CLN5]] | +0.59 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[FMC1]] | +0.57 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[EBI3]] | +0.57 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[EMSY-DT]] | +0.56 | +0.59 / +0.60 | both halves | 7e-06 | same gene group |
| [[DHFR2]] | +0.55 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[ATP23]] | +0.54 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[BAMBI]] | +0.54 | +0.59 / +0.41 | both halves | 4e-05 |  |
| [[DNAH3]] | +0.53 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[MAP3K2-DT]] | +0.53 | +0.47 / +0.64 | both halves | 2e-05 | same gene group |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HERC2P3]] | -0.57 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[PCYT1A]] | -0.53 | -0.57 / -0.36 | both halves | 9e-05 |  |
| [[UFD1]] | -0.52 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[ZCCHC17]] | -0.52 | -0.57 / -0.42 | both halves | 4e-05 |  |
| [[HERC2P9]] | -0.52 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[DPP9]] | -0.51 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[VPS53]] | -0.51 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[SNX29]] | -0.50 | -0.48 / -0.29 | both halves | 2e-04 |  |
| [[AP1M1]] | -0.50 | -0.58 / -0.35 | both halves | 1e-04 |  |
| [[HERC2P9-1]] | -0.49 | -0.26 / -0.52 | both halves | 3e-04 |  |
| [[HERC2]] | -0.49 | -0.43 / -0.47 | both halves | 4e-05 |  |
| [[LYG1]] | -0.48 | -0.49 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises PAXIP1-DT's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[RSPH1]] | B | RSPH1 activity raises PAXIP1-DT's level | lines that do not express RSPH1 (13) vs lines expressing it (37) | 1.47× lower at baseline in the lines without RSPH1 | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: SLC37A1, ABCG1, SHROOM3; maybe low, not absent |
| [[CSF3]] | B | CSF3 activity lowers PAXIP1-DT's level | lines that do not express CSF3 (27) vs lines expressing it (23) | 1.61× higher at baseline in the lines without CSF3 | 0.0999 | ⚠ within organs, on part of the lines; also absent: CCBE1, LOX, RRAD |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.599). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.8, 32.2); signed map (38.2, 3.1). **Vector** length 49.5, 6.37% of its response variance represented; |z| ≥ 3 in 882 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +3.9 | +6.1 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.4 | +7.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | +3.0 | +4.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.7 | +12.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.4 | +3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +4.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.7 | +3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.4 | +0.4 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.2 | +2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.2 | +2.8 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -2.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.6 | -5.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | -3.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.6 | -2.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.0 | -1.2 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.9 | -1.4 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -0.9 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | PAXIP1 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 7q36.2 — chr7:155,003,421-155,005,703 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously PAXIP1-AS1 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:27328](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27328) · Entrez [202781](https://www.ncbi.nlm.nih.gov/gene/202781) · Ensembl [ENSG00000273344](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000273344)

## Data

Gene col 15781: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15781); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15781, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15781]; `tensor/DDL_lfc|DDL_z.npy` [15781]; `embed/gene_vectors.npy` [15781]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15781 or target_col == 15781). Every well: [[PAXIP1-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PAXIP1-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
