---
symbol: "RING1"
type: "gene"
col: 12833
ensembl_id: "ENSG00000204227"
name: "ring finger protein 1"
location: "6p21.32"
module: 189
arm: "+"
pooled_cpm: 19.79
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 8
n_dd_up_clean: 12
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/189"]
generated_by: "tahoemap"
---

# RING1

*ring finger protein 1* — 6p21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.43× (z +6.1, q 5e-07, up in 26 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.760× (z -6.6, q 3e-08, down in 23 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLPPR2]] (+0.65, fdr 1e-05), [[SYP]] (+0.63, fdr 3e-05), [[RELA]] (+0.60, fdr 2e-05); moves opposite to [[ZNF718]] (-0.61, fdr 1e-05), [[METTL4]] (-0.59, fdr 3e-05), [[LRRC69]] (-0.59, fdr 2e-05).
> It is in [[Module 189]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PTPRH]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠; shown: the 15 strongest. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12833.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.43×** | +6.1 | 5e-07 | 26/48 (LoVo, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Baicalin (drug)]] 0.5 µM |  | **1.36×** | +5.3 | 3e-05 | 25/48 (RKO, HT-29, …) | inconsistent across doses | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 0.05 µM |  | **1.39×** | +5.2 | 3e-05 | 22/47 (LoVo, RKO, …) | inconsistent across doses | position effect removed |
| [[Ixazomib (drug)]] 5 µM |  | **1.80×** | +5.2 | 3e-05 | 23/45 (A-427, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.35×** | +4.9 | 1e-04 | 21/47 (NCI-H1573, PANC-1, …) | rises with dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.23×** | +4.8 | 1e-04 | 18/47 (A-172, AsPC-1, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.29×** | +4.4 | 8e-04 | 20/48 (LoVo, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +4.3 | 0.001 | 14/48 (LOX-IMVI, SNU-423, …) | rises with dose |  |
| [[Cinacalcet (drug)]] 0.5 µM |  | **1.28×** | +4.2 | 0.002 | 15/48 (HepG2/C3A, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Baicalin (drug)]] 0.05 µM |  | **1.27×** | +4.1 | 0.002 | 11/48 (RKO, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[Pralsetinib (drug)]] 5 µM |  | **1.54×** | +3.8 | 0.007 | 11/46 (NCI-H460, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.26×** | +3.8 | 0.007 | 12/48 (NCI-H1792, LOX-IMVI, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.44×** | +3.8 | 0.007 | 10/48 (Hs 766T, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib (drug)]] 0.05 µM |  | **1.26×** | +3.7 | 0.009 | 5/47 (PANC-1, A-172, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.23×** | +3.5 | 0.017 | 12/48 (NCI-H2347, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12833.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.760×** | -6.6 | 3e-08 | 23/47 (H4, NCI-H23, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.746×** | -5.0 | 1e-04 | 21/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.611×** | -4.3 | 0.003 | 18/47 (LOX-IMVI, C-33 A, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.775×** | -4.1 | 0.005 | 16/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.782×** | -4.0 | 0.008 | 15/47 (BT-474, LOX-IMVI, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.798×** | -3.9 | 0.010 | 14/47 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.662×** | -3.6 | 0.022 | 13/48 (CFPAC-1, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.811×** | -3.5 | 0.039 | 18/47 (H4, NCI-H23, …) | top dose only | cell-cycle shift (explains ~1% here); position effect removed |
| [[Busulfan (drug)]] 5 µM |  | 0.868× | -3.3 | 0.064 | 6/48 (LS 180, CHP-212, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12833. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 27.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -16.2) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -8.9) |
| [[A-172 (line)]] | wt | 13.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +10.4) ⚠ cell-cycle shift, explains ~67% of this change | — |
| [[AsPC-1 (line)]] | alt | 23.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +8.8) ⚠ cell-cycle shift, explains ~67% of this change | — |
| [[H4 (line)]] | wt | 30.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.197× (z -12.2) |
| [[MIA PaCa-2 (line)]] | alt | 16.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -12.0) ⚠ cell-cycle shift, explains ~67% of this change |
| [[NCI-H23 (line)]] | alt | 23.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -9.3) |
| [[A-427 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 14.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12833), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLPPR2]] | +0.65 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[SYP]] | +0.63 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[RELA]] | +0.60 | +0.56 / +0.46 | both halves | 2e-05 | pathway: Cellular Senescence |
| [[HDAC5]] | +0.60 | +0.47 / +0.51 | both halves | 2e-05 | pathway: Differentiation of T cells; STRING 528 |
| [[POLM]] | +0.59 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[NAGK]] | +0.59 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[RCE1]] | +0.58 | +0.51 / +0.46 | both halves | 2e-05 |  |
| [[PORCN]] | +0.57 | +0.43 / +0.44 | both halves | 3e-05 |  |
| [[NECAP1]] | +0.57 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[RAB24]] | +0.57 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[NAT14]] | +0.56 | +0.41 / +0.44 | both halves | 4e-05 |  |
| [[ZMIZ2]] | +0.56 | +0.41 / +0.48 | both halves | 4e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF718]] | -0.61 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[METTL4]] | -0.59 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[LRRC69]] | -0.59 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[VSIG10]] | -0.58 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[ZNF876P]] | -0.57 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[MCM9]] | -0.56 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[SNTB2]] | -0.56 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[LAMTOR5-AS1]] | -0.55 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[TOR3A]] | -0.55 | -0.56 / -0.34 | both halves | 1e-04 |  |
| [[NSMAF]] | -0.55 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[RAN]] | -0.55 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[ANAPC1]] | -0.55 | -0.46 / -0.47 | both halves | 3e-05 | pathway: Cellular Senescence; STRING 901 |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTPRH]] | B | PTPRH activity lowers RING1's level | lines that do not express PTPRH (6) vs lines expressing it (44) | 1.17× higher at baseline in the lines without PTPRH | 0.071 | ⚠ within organs, on part of the lines; co-occurs with EP300, RNF43, ZFHX3; also absent: RAB32, PDE4A, ADAL |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 189]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.710). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (9.6, -0.0); signed map (-22.7, 23.4). **Vector** length 73.4, 13.2% of its response variance represented; |z| ≥ 3 in 629 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +4.3 | +4.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.7 | +6.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +4.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.2 | +4.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | +2.8 | +4.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.6 | +3.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +2.1 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +1.6 | +2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +1.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.3 | -6.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.1 | -3.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.9 | -5.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.6 | -4.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -0.0 |
|  | [[EX229 (drug)]] 5 µM |  | -2.1 | -4.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.8 | -1.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.8 | -1.3 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.8 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | ring finger protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.32 — chr6:33,208,500-33,212,722 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RNF1 |
| Gene groups (HGNC) | Ring finger proteins; RING finger E3 ubiquitin protein ligases |
| Reactome | 20 pathways, smallest: SUMOylation of DNA methylation proteins; Transcriptional Regulation by E2F6; RUNX1 interacts with co-factors whose precise effect on RUNX1 targets is not known |
| Matched by | ensembl_id |

**Function**, from UniProt [Q06587](https://www.uniprot.org/uniprotkb/Q06587) (E3 ubiquitin-protein ligase RING1):

> Constitutes one of the E3 ubiquitin-protein ligases that mediate monoubiquitination of 'Lys-119' of histone H2A, thereby playing a central role in histone code and gene regulation. H2A 'Lys-119' ubiquitination gives a specific tag for epigenetic transcriptional repression and participates in X chromosome inactivation of female mammals. Essential component of a Polycomb group (PcG) multiprotein PRC1-like complex, a complex class required to maintain the transcriptionally repressive state of many …

**Summary**, from NCBI Gene [6015](https://www.ncbi.nlm.nih.gov/gene/6015):

> This gene belongs to the RING finger family, members of which encode proteins characterized by a RING domain, a zinc-binding motif related to the zinc finger domain. The gene product can bind DNA and can act as a transcriptional repressor. It is associated with the multimeric polycomb group protein complex. The gene product interacts with the polycomb group proteins BMI1, EDR1, and CBX4, and colocalizes with these proteins in large nuclear domains. It interacts with the CBX4 protein via its …

**Accessions** — [HGNC:10018](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10018) · Entrez [6015](https://www.ncbi.nlm.nih.gov/gene/6015) · UniProt [Q06587](https://www.uniprot.org/uniprotkb/Q06587) · Ensembl [ENSG00000204227](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204227)

## Data

Gene col 12833: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12833); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12833, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12833]; `tensor/DDL_lfc|DDL_z.npy` [12833]; `embed/gene_vectors.npy` [12833]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12833 or target_col == 12833). Every well: [[RING1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RING1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
