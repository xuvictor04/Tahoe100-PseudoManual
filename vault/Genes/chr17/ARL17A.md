---
symbol: "ARL17A"
type: "gene"
col: 11738
ensembl_id: "ENSG00000185829"
name: "ARF like GTPase 17A"
location: "17q21.31"
module: 21
arm: "+"
pooled_cpm: 9.42
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 5
n_dd_up_clean: 10
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# ARL17A

*ARF like GTPase 17A* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.83× (z +13.6, q 2e-39, up in 32 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.709× (z -5.5, q 3e-05, down in 15 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EHBP1-AS1]] (+0.61, fdr 1e-05), [[SMBD1P]] (+0.58, fdr 1e-05), [[SEM1]] (+0.55, fdr 3e-05); moves opposite to [[MRPL40]] (-0.55, fdr 3e-05), [[COMMD8]] (-0.55, fdr 8e-05), [[MDM1]] (-0.54, fdr 8e-05).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11738.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +13.6 | 2e-39 | 32/42 (A-172, SW 900, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.81×** | +9.1 | 3e-17 | 6/14 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +5.7 | 2e-06 | 16/38 (hTERT-HPNE, C32, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.37×** | +5.0 | 7e-05 | 9/29 (MIA PaCa-2, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +4.7 | 3e-04 | 12/39 (NCI-H2347, C32, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +4.6 | 4e-04 | 10/47 (SW1417, HOP62, …) | top dose only |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | **1.28×** | +3.9 | 0.008 | 6/42 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Orlistat (drug)]] 0.05 µM |  | **1.29×** | +3.7 | 0.014 | 3/41 (J82, NCI-H2030, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.35×** | +3.4 | 0.044 | 6/42 (A498, A-172, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.23×** | +3.3 | 0.053 | 3/47 (HOP62, HT-29, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.24×** | +3.3 | 0.055 | 7/43 (HOP62, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | **1.23×** | +3.2 | 0.057 | 4/48 (SW1417, HOP62, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.47×** | +3.2 | 0.058 | 5/46 (HOP62, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.22× | +3.0 | 0.10 | 5/46 (HEC-1-A, LOX-IMVI, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11738.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.709×** | -5.5 | 3e-05 | 15/42 (LOX-IMVI, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.731×** | -5.0 | 2e-04 | 14/47 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.733×** | -4.9 | 2e-04 | 14/45 (CHP-212, RPMI-7951, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.765×** | -4.1 | 0.006 | 15/47 (RPMI-7951, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Asciminib (drug)]] 0.05 µM |  | **0.808×** | -3.4 | 0.084 | 11/47 (CHP-212, CFPAC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11738. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 24.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -9.9) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 7.87 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.30× (z +8.5) | — |
| [[A549 (line)]] | wt | 22.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.131× (z -12.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 3.11 | 0 | 1 | — | [[Doxycycline (monohydrate) (drug)]] 0.5 µM 0.0622× (z -8.9) |
| [[BT-474 (line)]] | alt | 4.72 | 0 | 1 | — | [[Delamanid (drug)]] 0.05 µM 0.0648× (z -8.7) |
| [[KATO III (line)]] | alt | 15.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.117× (z -13.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 20.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.307× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 2.60 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.05 µM 0.0779× (z -9.3) |
| [[NCI-H460 (line)]] | wt | 7.59 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.265× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 5.27 | 0 | 1 | — | [[Berbamine (drug)]] 0.5 µM 0.0568× (z -9.0) |
| [[SHP-77 (line)]] | alt | 9.86 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.244× (z -9.1) ⚠ cell-cycle shift, explains ~75% of this change |
| [[SW480 (line)]] | alt | 29.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.401× (z -9.3) ⚠ toxic; cell-cycle shift, explains ~35% of this change |
| [[A-427 (line)]] | wt | 6.12 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.60 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.62 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.06 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.25 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.61 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.91 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.01 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.83 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.82 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.13 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.19 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.83 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.21 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11738), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EHBP1-AS1]] | +0.61 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[SMBD1P]] | +0.58 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[SEM1]] | +0.55 | +0.61 / +0.44 | both halves | 3e-05 |  |
| [[TMEM11-DT]] | +0.53 | +0.40 / +0.50 | both halves | 5e-05 |  |
| [[ANKHD1-EIF4EBP3]] | +0.52 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[MUC20-OT1]] | +0.52 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[OMG]] | +0.52 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[MESD]] | +0.51 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[TNXB]] | +0.51 | +0.43 / +0.50 | both halves | 4e-05 |  |
| [[ALG1L9P]] | +0.51 | +0.31 / +0.62 | both halves | 2e-04 |  |
| [[C2]] | +0.51 | +0.44 / +0.41 | both halves | 4e-05 |  |
| [[UBE2CP5]] | +0.51 | +0.50 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL40]] | -0.55 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[COMMD8]] | -0.55 | -0.37 / -0.53 | both halves | 8e-05 |  |
| [[MDM1]] | -0.54 | -0.37 / -0.54 | both halves | 8e-05 |  |
| [[ISOC1]] | -0.54 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[AMACR]] | -0.53 | -0.34 / -0.59 | both halves | 1e-04 |  |
| [[DGAT2]] | -0.51 | -0.38 / -0.37 | both halves | 9e-05 |  |
| [[AKAP11]] | -0.51 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[CSRP1]] | -0.50 | -0.48 / -0.38 | both halves | 6e-05 |  |
| [[CYRIA]] | -0.50 | -0.33 / -0.36 | both halves | 1e-04 |  |
| [[SLC25A30]] | -0.49 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[SSX2IP]] | -0.48 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[C12orf29]] | -0.48 | -0.28 / -0.49 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ARL17A's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.412). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.9, -20.9); signed map (10.1, 8.7). **Vector** length 54.3, 6.49% of its response variance represented; |z| ≥ 3 in 968 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +13.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +5.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +2.3 | +4.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.0 | +1.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.0 | +2.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.0 | +0.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +2.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.7 | +2.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.4 | +3.0 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.1 | -5.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | -2.8 | -4.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.9 | -4.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | +0.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -0.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.2 | -2.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.2 | -0.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.1 | -0.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.1 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | ARF like GTPase 17A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.31 — chr17:46,499,780-46,579,695 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ARF1P2, ARL17P1 |
| Gene groups (HGNC) | ARF GTPase family; Proteins encoded by multiple genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IVW1](https://www.uniprot.org/uniprotkb/Q8IVW1) (Putative ADP-ribosylation factor-like protein 17A):

> Putative small GTP-binding protein cycling between an inactive GDP-bound and an active GTP-bound form.

**Summary**, from NCBI Gene [51326](https://www.ncbi.nlm.nih.gov/gene/51326):

> Predicted to enable GTP binding activity. Predicted to be involved in intracellular protein transport and vesicle-mediated transport. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24096](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24096) · Entrez [51326](https://www.ncbi.nlm.nih.gov/gene/51326) · UniProt [Q8IVW1](https://www.uniprot.org/uniprotkb/Q8IVW1) · Ensembl [ENSG00000185829](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185829)

## Data

Gene col 11738: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11738); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11738, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11738]; `tensor/DDL_lfc|DDL_z.npy` [11738]; `embed/gene_vectors.npy` [11738]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11738 or target_col == 11738). Every well: [[ARL17A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARL17A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
