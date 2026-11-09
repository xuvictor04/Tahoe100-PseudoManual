---
symbol: "DPY19L1P2"
type: "gene"
col: 13826
ensembl_id: "ENSG00000231952"
name: "DPY19L1 pseudogene 2"
location: "7p14.3"
module: 3
arm: "-"
pooled_cpm: 3.29
n_lines_expressing: 48
n_dd_up: 4
n_dd_down: 15
n_dd_up_clean: 1
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# DPY19L1P2

*DPY19L1 pseudogene 2* — 7p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.05× (z +8.8, q 1e-15, up in 0 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 1.67× (z +4.0, q 0.010, up in 12 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (9 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.312× (z -9.6, q 7e-19, down in 30 of 42 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.558× (z -4.8, q 2e-04, down in 20 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZMYND11]] (+0.65, fdr 1e-05), [[TRIM44]] (+0.65, fdr 1e-05), [[SFPQ]] (+0.63, fdr 1e-05); moves opposite to [[HSPB11]] (-0.64, fdr 1e-05), [[GMCL1]] (-0.64, fdr 1e-05), [[ZNF511]] (-0.63, fdr 1e-05).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TSPAN33]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13826.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.05×** | +8.8 | 1e-15 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.97×** | +5.1 | 9e-05 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.67×** | +4.0 | 0.010 | 12/37 (C-33 A, AsPC-1, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **1.35×** | +3.5 | 0.069 | 8/43 (SW480, SW1417, …) | top dose only | low cells (technical?) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.51× | +3.2 | 0.13 | 8/41 (PANC-1, A-427, …) | two highest doses |  |
| [[Finasteride (drug)]] 5 µM |  | 1.50× | +3.2 | 0.15 | 6/41 (H4, PANC-1, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 9 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13826.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.312×** | -9.6 | 7e-19 | 30/42 (PANC-1, KATO III, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.348×** | -8.6 | 1e-15 | 29/42 (SW1417, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.358×** | -8.4 | 7e-15 | 28/44 (KATO III, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.437×** | -6.8 | 2e-09 | 25/44 (PANC-1, LoVo, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.597×** | -6.0 | 2e-07 | 22/32 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.558×** | -4.8 | 2e-04 | 20/42 (C32, HT-29, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.563×** | -4.7 | 2e-04 | 20/41 (J82, PANC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **0.580×** | -4.5 | 6e-04 | 18/28 (PANC-1, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.607×** | -4.1 | 0.003 | 18/42 (PANC-1, SHP-77, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.599×** | -4.0 | 0.003 | 16/35 (HEC-1-A, SW 900, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.601×** | -4.0 | 0.003 | 12/42 (SW48, NCI-H2030, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.622×** | -3.7 | 0.011 | 14/41 (RPMI-7951, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.654×** | -3.5 | 0.021 | 17/38 (SHP-77, HOP62, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.669×** | -3.2 | 0.052 | 12/44 (SNU-423, HCT15, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.635×** | -3.0 | 0.093 | 8/44 (NCI-H2030, RKO, …) | all doses, stronger at high dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.64 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13826. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 7.68 | 0 | 5 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.187× (z -11.3) ⚠ cell-cycle shift, explains ~27% of this change |
| [[PANC-1 (line)]] | alt | 7.69 | 0 | 4 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.176× (z -11.9) ⚠ cell-cycle shift, explains ~27% of this change |
| [[C32 (line)]] | wt | 6.58 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0159× (z -12.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 3.01 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0303× (z -10.8) ⚠ cell-cycle shift, explains ~42% of this change |
| [[SW480 (line)]] | alt | 2.45 | 0 | 2 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0712× (z -9.4) ⚠ cell-cycle shift, explains ~34% of this change |
| [[A498 (line)]] | wt | 3.58 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0470× (z -10.3) ⚠ cell-cycle shift, explains ~78% of this change |
| [[SHP-77 (line)]] | alt | 5.42 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0502× (z -10.0) |
| [[SK-MEL-2 (line)]] | alt | 4.61 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0664× (z -8.5) ⚠ cell-cycle shift, explains ~36% of this change |
| [[SW1417 (line)]] | alt | 4.20 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0459× (z -10.0) ⚠ cell-cycle shift, explains ~36% of this change |
| [[A-172 (line)]] | wt | 2.94 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.85 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.767 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.51 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.549 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.23 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.88 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13826), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*45 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMYND11]] | +0.65 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[TRIM44]] | +0.65 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[SFPQ]] | +0.63 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[HNRNPM]] | +0.62 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[UTP20]] | +0.62 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[DPH5-DT]] | +0.62 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[EWSR1]] | +0.61 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[LINC02728]] | +0.61 | +0.68 / +0.52 | both halves | 1e-05 |  |
| [[TAPT1-AS1]] | +0.60 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[ZNF747]] | +0.60 | +0.56 / +0.37 | both halves | 9e-05 |  |
| [[ZNF507]] | +0.59 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[ABCE1]] | +0.58 | +0.54 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*55 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSPB11]] | -0.64 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[GMCL1]] | -0.64 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[ZNF511]] | -0.63 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[ABCB9]] | -0.62 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[MPG]] | -0.61 | -0.54 / -0.49 | both halves | 2e-05 |  |
| [[CBFA2T2]] | -0.61 | -0.53 / -0.46 | both halves | 2e-05 |  |
| [[CIAO2B]] | -0.60 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[SH3GL1]] | -0.60 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[CARD19]] | -0.60 | -0.46 / -0.57 | both halves | 3e-05 |  |
| [[VKORC1]] | -0.60 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[TRPT1]] | -0.60 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[MOSPD3]] | -0.60 | -0.45 / -0.50 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TSPAN33]] | B | TSPAN33 activity raises DPY19L1P2's level | lines that do not express TSPAN33 (12) vs lines expressing it (38) | 1.34× lower at baseline in the lines without TSPAN33 | 0.016 | ⚠ within organs, on part of the lines; also absent: SRCIN1, CRACD, GNAZ; maybe low, not absent |
| [[SLC17A7]] | B | SLC17A7 activity raises DPY19L1P2's level | lines that do not express SLC17A7 (9) vs lines expressing it (41) | 1.47× lower at baseline in the lines without SLC17A7 | 0.091 | ⚠ within organs, on part of the lines; also absent: GXYLT2, ITGA10, NT5M; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.652). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (3.3, -15.1); signed map (14.4, -39.4). **Vector** length 55.7, 7.52% of its response variance represented; |z| ≥ 3 in 1,212 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.5 | +5.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.1 | +1.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.1 | +4.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.8 | +8.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.8 | -1.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.6 | +0.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.5 | +0.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.3 | +1.0 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -3.1 | -9.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -3.1 | -8.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -2.6 | -8.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -0.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | -2.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.4 | -1.9 |
|  | [[Fumaric acid (drug)]] 5 µM |  | -1.3 | -2.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.2 | -2.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.2 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | DPY19L1 pseudogene 2 |
| Locus type | pseudogene |
| Location | 7p14.3 — chr7:32,812,757-32,838,570 (+) |
| Ensembl biotype | unprocessed_pseudogene |
| Also known as | THC1072510 |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:22851](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22851) · Entrez [102724668](https://www.ncbi.nlm.nih.gov/gene/102724668) · Ensembl [ENSG00000231952](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000231952)

## Data

Gene col 13826: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13826); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13826, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13826]; `tensor/DDL_lfc|DDL_z.npy` [13826]; `embed/gene_vectors.npy` [13826]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13826 or target_col == 13826). Every well: [[DPY19L1P2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DPY19L1P2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
