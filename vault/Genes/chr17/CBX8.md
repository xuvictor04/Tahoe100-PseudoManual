---
symbol: "CBX8"
type: "gene"
col: 6550
ensembl_id: "ENSG00000141570"
name: "chromobox 8"
location: "17q25.3"
module: 59
arm: "+"
pooled_cpm: 7.94
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 4
n_dd_up_clean: 18
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# CBX8

*chromobox 8* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.36× (z +10.8, q 1e-24, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.682× (z -4.6, q 0.002, down in 20 of 46 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.707× (z -4.4, q 0.003, down in 17 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CBX4]] (+0.71, fdr 7e-06, ⚠ same locus), [[DBP]] (+0.69, fdr 7e-06), [[MIDEAS]] (+0.64, fdr 1e-05), [[ECH1]] (+0.60, fdr 1e-05); moves opposite to [[ZNF731P]] (-0.63, fdr 9e-06), [[TTL]] (-0.55, fdr 3e-05), [[PTPN11]] (-0.53, fdr 1e-04).
> It sits in the **+** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6550.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.36×** | +10.8 | 1e-24 | 41/47 (NCI-H2030, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.18×** | +9.9 | 2e-20 | 37/46 (HOP62, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.68×** | +9.2 | 5e-18 | 25/43 (A498, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.48×** | +7.0 | 5e-10 | 27/47 (KATO III, NCI-H2347, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +6.1 | 1e-07 | 20/44 (HOP62, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.59×** | +5.8 | 6e-07 | 25/47 (NCI-H2030, PANC-1, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +5.7 | 8e-07 | 17/39 (SW1417, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.57×** | +5.7 | 1e-06 | 24/47 (A549, HOP62, …) | top dose only | cell-cycle shift (explains ~9% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +5.6 | 2e-06 | 8/48 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.46×** | +4.8 | 1e-04 | 15/46 (HEC-1-A, LS 180, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.03×** | +4.7 | 2e-04 | 16/46 (KATO III, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.97×** | +4.5 | 4e-04 | 17/43 (A-427, SW48, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.42×** | +4.4 | 5e-04 | 13/46 (A-427, NCI-H1573, …) | rises with dose | position effect removed |
| [[Radotinib (drug)]] 5 µM |  | **1.27×** | +4.2 | 0.001 | 14/46 (A-427, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.38×** | +4.0 | 0.002 | 13/45 (HEC-1-A, HOP62, …) | two highest doses | cell-cycle shift (explains ~18% here); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.51×** | +3.7 | 0.008 | 7/40 (A549, HepG2/C3A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.33×** | +3.6 | 0.010 | 9/47 (A549, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.29×** | +3.1 | 0.049 | 12/46 (SW 900, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6550.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.682×** | -4.6 | 0.002 | 20/46 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.707×** | -4.4 | 0.003 | 17/47 (NCI-H2030, PANC-1, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.733×** | -4.0 | 0.013 | 17/46 (PANC-1, NCI-H460, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.751×** | -3.7 | 0.034 | 18/46 (HepG2/C3A, LoVo, …) | rises with dose |  |
| [[Acetohexamide (drug)]] 5 µM |  | 0.848× | -3.0 | 0.30 | 4/47 (RKO, H4, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6550. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 17.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 4.94 | 0 | 2 (1 ⚠) | — | [[Doxycycline (monohydrate) (drug)]] 0.05 µM 0.0823× (z -9.0) |
| [[A498 (line)]] | wt | 7.73 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.25× (z +11.6) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[HEC-1-A (line)]] | alt | 12.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +9.0) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[KATO III (line)]] | alt | 14.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +9.1) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[LOX-IMVI (line)]] | wt | 4.26 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0929× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 6.74 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.158× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 10.1 | 0 | 1 | — | [[Terfenadine (drug)]] 0.5 µM 0.0680× (z -9.5) |
| [[SW1417 (line)]] | alt | 10.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0861× (z -13.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 5.33 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.35 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.08 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.81 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.42 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.01 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.79 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.58 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.83 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.71 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.90 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.93 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.31 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.08 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 14.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6550), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CBX4]] | +0.71 | +0.68 / +0.72 | both halves | 7e-06 | same gene group; pathway: Cellular Senescence; STRING 999; ⚠ same locus (31.5 kb, same strand: neighbours can correlate without regulation) |
| [[DBP]] | +0.69 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[MIDEAS]] | +0.64 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[ECH1]] | +0.60 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[BCOR]] | +0.59 | +0.52 / +0.61 | both halves | 1e-05 | STRING 971 |
| [[CAMSAP3]] | +0.58 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[REEP2]] | +0.57 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[VASN]] | +0.57 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[NAT14]] | +0.57 | +0.49 / +0.43 | both halves | 3e-05 |  |
| [[CDC42BPG]] | +0.57 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[CXXC5]] | +0.57 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[NR1D1]] | +0.56 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[KMT2E]] | +0.56 | +0.58 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF731P]] | -0.63 | -0.57 / -0.67 | both halves | 9e-06 |  |
| [[TTL]] | -0.55 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[PTPN11]] | -0.53 | -0.36 / -0.56 | both halves | 1e-04 | pathway: Intracellular signaling by second messengers |
| [[RBM19]] | -0.52 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[NAA50]] | -0.52 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[PRMT3]] | -0.52 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[DESI1]] | -0.51 | -0.25 / -0.55 | both halves | 4e-04 |  |
| [[NUTM2A-AS1]] | -0.51 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[MAPKAP1]] | -0.51 | -0.29 / -0.58 | both halves | 3e-04 | pathway: Intracellular signaling by second messengers |
| [[MFSD14CP-1]] | -0.51 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[MAN2A1]] | -0.50 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[DOCK1]] | -0.50 | -0.37 / -0.58 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises CBX8's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[SIGIRR]] | B | SIGIRR activity lowers CBX8's level | lines that do not express SIGIRR (9) vs lines expressing it (41) | 1.36× higher at baseline in the lines without SIGIRR | 0.057 | ⚠ within organs, on part of the lines; also absent: CLCF1, LTBR, MYOF |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **+** arm (projection on the module's main direction 0.601). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (21.2, -5.6); signed map (-5.4, 15.0). **Vector** length 69.0, 10.9% of its response variance represented; |z| ≥ 3 in 905 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +7.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.7 | +5.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | +3.6 | +3.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.0 | +3.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.9 | +4.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.8 | +4.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +3.7 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | -3.6 | -4.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.5 | -4.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.5 | -3.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.6 | -2.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -2.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.5 | -1.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.1 | -2.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | -2.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.7 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | chromobox 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:79,792,132-79,801,683 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RC1, HPC3, PC3 |
| Gene groups (HGNC) | Chromobox family |
| Hallmark sets | KRAS_SIGNALING_UP |
| Reactome | 19 pathways, smallest: SUMOylation of DNA methylation proteins; RUNX1 interacts with co-factors whose precise effect on RUNX1 targets is not known; SUMOylation of transcription cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HC52](https://www.uniprot.org/uniprotkb/Q9HC52) (Chromobox protein homolog 8):

> Component of a Polycomb group (PcG) multiprotein PRC1-like complex, a complex class required to maintain the transcriptionally repressive state of many genes, including Hox genes, throughout development. PcG PRC1 complex acts via chromatin remodeling and modification of histones; it mediates monoubiquitination of histone H2A 'Lys-119', rendering chromatin heritably changed in its expressibility.

**Summary**, from NCBI Gene [57332](https://www.ncbi.nlm.nih.gov/gene/57332):

> Enables histone H3K27me3 reader activity. Involved in negative regulation of transcription by RNA polymerase II. Located in chromatin and nucleoplasm. Part of PRC1 complex. Biomarker of esophagus squamous cell carcinoma and glioblastoma. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:15962](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15962) · Entrez [57332](https://www.ncbi.nlm.nih.gov/gene/57332) · UniProt [Q9HC52](https://www.uniprot.org/uniprotkb/Q9HC52) · Ensembl [ENSG00000141570](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141570)

## Data

Gene col 6550: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6550); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6550, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6550]; `tensor/DDL_lfc|DDL_z.npy` [6550]; `embed/gene_vectors.npy` [6550]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6550 or target_col == 6550). Every well: [[CBX8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CBX8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
